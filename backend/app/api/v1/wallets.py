from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.wallet import WalletRead
from app.services.wallet_service import WalletService

router = APIRouter(prefix="/wallets", tags=["wallets"])


@router.get("/{wallet_id}", response_model=WalletRead)
def get_wallet(wallet_id: str, organization_id: str, db: Session = Depends(get_db)):
    return WalletService(db).get(organization_id, wallet_id)


@router.get("/customer/{customer_id}", response_model=WalletRead)
def get_wallet_by_customer(customer_id: str, organization_id: str, db: Session = Depends(get_db)):
    return WalletService(db).get_by_customer(organization_id, customer_id)
