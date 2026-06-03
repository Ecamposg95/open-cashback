from decimal import Decimal

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.branch import Branch
from app.models.cashback_transaction import CashbackTransaction
from app.models.customer import Customer
from app.models.sale import Sale
from app.models.sale_item import SaleItem
from app.schemas.sale import SaleCreate
from app.services.cashback_engine import CashbackEngine
from app.services.ledger_service import LedgerService
from app.services.wallet_service import WalletService


class SaleService:
    def __init__(self, db: Session):
        self.db = db

    def _validate_scope(self, organization_id: str, branch_id: str, customer_id: str) -> None:
        branch = self.db.get(Branch, branch_id)
        customer = self.db.get(Customer, customer_id)
        if not branch or branch.organization_id != organization_id:
            raise HTTPException(status_code=404, detail="Branch not found in organization")
        if not customer or customer.organization_id != organization_id:
            raise HTTPException(status_code=404, detail="Customer not found in organization")

    def create(self, payload: SaleCreate) -> tuple[Sale, Decimal, Decimal, CashbackTransaction | None]:
        existing = (
            self.db.query(Sale)
            .filter(Sale.organization_id == payload.organization_id, Sale.external_sale_id == payload.external_sale_id)
            .first()
        )
        if existing:
            tx = (
                self.db.query(CashbackTransaction)
                .filter(CashbackTransaction.sale_id == existing.id, CashbackTransaction.transaction_type == "EARNED")
                .first()
            )
            rate, amount = CashbackEngine(self.db).calculate(existing.organization_id, existing.eligible_amount)
            return existing, rate, amount, tx

        self._validate_scope(payload.organization_id, payload.branch_id, payload.customer_id)
        sale_data = payload.model_dump(exclude={"items"})
        sale = Sale(**sale_data)
        self.db.add(sale)
        self.db.flush()
        for item_payload in payload.items:
            self.db.add(SaleItem(sale_id=sale.id, **item_payload.model_dump()))
        wallet = WalletService(self.db).get_by_customer(payload.organization_id, payload.customer_id)
        rate, amount = CashbackEngine(self.db).calculate(payload.organization_id, payload.eligible_amount)
        tx = None
        if amount > Decimal("0.00"):
            tx = LedgerService(self.db).create_transaction(
                organization_id=payload.organization_id,
                branch_id=payload.branch_id,
                customer_id=payload.customer_id,
                wallet=wallet,
                sale_id=sale.id,
                amount=amount,
                transaction_type="EARNED",
                description="Cashback earned from sale",
                reference=payload.external_sale_id,
            )
        self.db.commit()
        self.db.refresh(sale)
        return sale, rate, amount, tx

    def get(self, organization_id: str, sale_id: str) -> Sale:
        sale = self.db.query(Sale).filter(Sale.organization_id == organization_id, Sale.id == sale_id).first()
        if not sale:
            raise HTTPException(status_code=404, detail="Sale not found")
        return sale

    def cancel(self, organization_id: str, sale_id: str) -> Sale:
        sale = self.get(organization_id, sale_id)
        if sale.status == "CANCELLED":
            return sale
        earned = (
            self.db.query(CashbackTransaction)
            .filter(CashbackTransaction.sale_id == sale.id, CashbackTransaction.transaction_type == "EARNED")
            .first()
        )
        sale.status = "CANCELLED"
        if earned:
            wallet = WalletService(self.db).get(organization_id, earned.wallet_id)
            LedgerService(self.db).create_transaction(
                organization_id=organization_id,
                branch_id=sale.branch_id,
                customer_id=sale.customer_id,
                wallet=wallet,
                sale_id=sale.id,
                amount=-abs(Decimal(earned.amount)),
                transaction_type="REVERSED",
                status="REVERSED",
                description="Cashback reversed after sale cancellation",
                reference=sale.external_sale_id,
            )
        self.db.commit()
        self.db.refresh(sale)
        return sale
