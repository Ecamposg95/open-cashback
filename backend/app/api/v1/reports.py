from decimal import Decimal

from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.cashback_transaction import CashbackTransaction
from app.models.customer import Customer
from app.models.sale import Sale
from app.models.wallet import Wallet

router = APIRouter(prefix="/reports", tags=["reports"])


def _sum(db: Session, organization_id: str, tx_type: str) -> Decimal:
    value = (
        db.query(func.coalesce(func.sum(CashbackTransaction.amount), 0))
        .filter(CashbackTransaction.organization_id == organization_id, CashbackTransaction.transaction_type == tx_type)
        .scalar()
    )
    return Decimal(value or 0)


@router.get("/summary")
def summary(organization_id: str, db: Session = Depends(get_db)):
    return {
        "sales_count": db.query(Sale).filter(Sale.organization_id == organization_id).count(),
        "customers_count": db.query(Customer).filter(Customer.organization_id == organization_id).count(),
        "cashback_issued": str(_sum(db, organization_id, "EARNED")),
        "cashback_redeemed": str(abs(_sum(db, organization_id, "REDEEMED"))),
        "outstanding_liability": str(db.query(func.coalesce(func.sum(Wallet.available_balance), 0)).filter(Wallet.organization_id == organization_id).scalar() or 0),
    }


@router.get("/outstanding-liability")
def outstanding_liability(organization_id: str, db: Session = Depends(get_db)):
    value = db.query(func.coalesce(func.sum(Wallet.available_balance), 0)).filter(Wallet.organization_id == organization_id).scalar()
    return {"outstanding_liability": str(value or 0)}


@router.get("/cashback-issued")
def cashback_issued(organization_id: str, db: Session = Depends(get_db)):
    return {"cashback_issued": str(_sum(db, organization_id, "EARNED"))}


@router.get("/cashback-redeemed")
def cashback_redeemed(organization_id: str, db: Session = Depends(get_db)):
    return {"cashback_redeemed": str(abs(_sum(db, organization_id, "REDEEMED")))}
