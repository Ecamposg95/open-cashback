from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.sale import SaleCashbackResponse, SaleCreate, SaleRead
from app.services.sale_service import SaleService

router = APIRouter(prefix="/sales", tags=["sales"])


@router.post("", response_model=SaleCashbackResponse)
def create_sale(payload: SaleCreate, db: Session = Depends(get_db)):
    sale, rate, amount, tx = SaleService(db).create(payload)
    return {"sale": sale, "cashback_rate": rate, "cashback_amount": amount, "transaction": tx}


@router.get("/{sale_id}", response_model=SaleRead)
def get_sale(sale_id: str, organization_id: str, db: Session = Depends(get_db)):
    return SaleService(db).get(organization_id, sale_id)


@router.post("/{sale_id}/cancel", response_model=SaleRead)
def cancel_sale(sale_id: str, organization_id: str, db: Session = Depends(get_db)):
    return SaleService(db).cancel(organization_id, sale_id)


@router.post("/{sale_id}/refund", response_model=SaleRead)
def refund_sale(sale_id: str, organization_id: str, db: Session = Depends(get_db)):
    sale = SaleService(db).cancel(organization_id, sale_id)
    sale.status = "REFUNDED"
    db.commit()
    db.refresh(sale)
    return sale
