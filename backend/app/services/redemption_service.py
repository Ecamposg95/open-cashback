from decimal import Decimal
from uuid import uuid4

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.branch import Branch
from app.models.customer import Customer
from app.models.redemption import Redemption
from app.schemas.redemption import RedemptionCreate
from app.services.ledger_service import LedgerService
from app.services.wallet_service import WalletService


class RedemptionService:
    def __init__(self, db: Session):
        self.db = db

    def create(self, payload: RedemptionCreate):
        if payload.amount <= Decimal("0.00"):
            raise HTTPException(status_code=400, detail="Redemption amount must be positive")
        branch = self.db.get(Branch, payload.branch_id)
        customer = self.db.get(Customer, payload.customer_id)
        if not branch or branch.organization_id != payload.organization_id:
            raise HTTPException(status_code=404, detail="Branch not found in organization")
        if not customer or customer.organization_id != payload.organization_id:
            raise HTTPException(status_code=404, detail="Customer not found in organization")
        wallet = WalletService(self.db).get_by_customer(payload.organization_id, payload.customer_id)
        if wallet.available_balance < payload.amount:
            raise HTTPException(status_code=400, detail="Insufficient wallet balance")
        redemption = Redemption(
            organization_id=payload.organization_id,
            branch_id=payload.branch_id,
            customer_id=payload.customer_id,
            wallet_id=wallet.id,
            sale_id=payload.sale_id,
            amount=payload.amount,
            redemption_code=payload.redemption_code or f"RED-{uuid4().hex[:12]}",
        )
        self.db.add(redemption)
        self.db.flush()
        tx = LedgerService(self.db).create_transaction(
            organization_id=payload.organization_id,
            branch_id=payload.branch_id,
            customer_id=payload.customer_id,
            wallet=wallet,
            sale_id=payload.sale_id,
            redemption_id=redemption.id,
            amount=-abs(payload.amount),
            transaction_type="REDEEMED",
            status="REDEEMED",
            description="Cashback redeemed",
            reference=redemption.redemption_code,
        )
        self.db.commit()
        self.db.refresh(redemption)
        return redemption, tx

    def get(self, organization_id: str, redemption_id: str) -> Redemption:
        redemption = (
            self.db.query(Redemption)
            .filter(Redemption.organization_id == organization_id, Redemption.id == redemption_id)
            .first()
        )
        if not redemption:
            raise HTTPException(status_code=404, detail="Redemption not found")
        return redemption

    def cancel(self, organization_id: str, redemption_id: str) -> Redemption:
        redemption = self.get(organization_id, redemption_id)
        if redemption.status == "CANCELLED":
            return redemption
        wallet = WalletService(self.db).get(organization_id, redemption.wallet_id)
        redemption.status = "CANCELLED"
        LedgerService(self.db).create_transaction(
            organization_id=organization_id,
            branch_id=redemption.branch_id,
            customer_id=redemption.customer_id,
            wallet=wallet,
            redemption_id=redemption.id,
            amount=abs(Decimal(redemption.amount)),
            transaction_type="REVERSED",
            status="REVERSED",
            description="Redemption cancelled",
            reference=redemption.redemption_code,
        )
        self.db.commit()
        self.db.refresh(redemption)
        return redemption
