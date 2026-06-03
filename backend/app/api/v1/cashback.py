from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.cashback_transaction import CashbackTransaction
from app.schemas.cashback import CashbackCalculationRequest, CashbackCalculationResponse, CashbackTransactionRead
from app.services.cashback_engine import CashbackEngine

router = APIRouter(prefix="/cashback", tags=["cashback"])


@router.post("/calculate", response_model=CashbackCalculationResponse)
def calculate_cashback(payload: CashbackCalculationRequest, db: Session = Depends(get_db)):
    rate, amount = CashbackEngine(db).calculate(payload.organization_id, payload.eligible_amount)
    return {"cashback_rate": rate, "eligible_amount": payload.eligible_amount, "cashback_amount": amount}


@router.get("/transactions", response_model=list[CashbackTransactionRead])
def list_transactions(organization_id: str, db: Session = Depends(get_db)):
    return db.query(CashbackTransaction).filter(CashbackTransaction.organization_id == organization_id).all()


@router.get("/transactions/{transaction_id}", response_model=CashbackTransactionRead)
def get_transaction(transaction_id: str, organization_id: str, db: Session = Depends(get_db)):
    tx = db.query(CashbackTransaction).filter(CashbackTransaction.organization_id == organization_id, CashbackTransaction.id == transaction_id).first()
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return tx
