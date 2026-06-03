from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.cashback_transaction import CashbackTransaction
from app.schemas.cashback import CashbackTransactionRead
from app.schemas.customer import CustomerCreate, CustomerRead, CustomerUpdate
from app.schemas.wallet import WalletRead
from app.services.customer_service import CustomerService
from app.services.wallet_service import WalletService

router = APIRouter(prefix="/customers", tags=["customers"])


@router.post("", response_model=CustomerRead)
def create_customer(payload: CustomerCreate, db: Session = Depends(get_db)):
    return CustomerService(db).create(payload)


@router.get("", response_model=list[CustomerRead])
def list_customers(organization_id: str, db: Session = Depends(get_db)):
    return CustomerService(db).list(organization_id)


@router.get("/{customer_id}", response_model=CustomerRead)
def get_customer(customer_id: str, organization_id: str, db: Session = Depends(get_db)):
    return CustomerService(db).get(organization_id, customer_id)


@router.patch("/{customer_id}", response_model=CustomerRead)
def update_customer(customer_id: str, organization_id: str, payload: CustomerUpdate, db: Session = Depends(get_db)):
    return CustomerService(db).update(organization_id, customer_id, payload)


@router.get("/{customer_id}/wallet", response_model=WalletRead)
def get_customer_wallet(customer_id: str, organization_id: str, db: Session = Depends(get_db)):
    return WalletService(db).get_by_customer(organization_id, customer_id)


@router.get("/{customer_id}/transactions", response_model=list[CashbackTransactionRead])
def get_customer_transactions(customer_id: str, organization_id: str, db: Session = Depends(get_db)):
    return (
        db.query(CashbackTransaction)
        .filter(CashbackTransaction.organization_id == organization_id, CashbackTransaction.customer_id == customer_id)
        .order_by(CashbackTransaction.created_at.desc())
        .all()
    )
