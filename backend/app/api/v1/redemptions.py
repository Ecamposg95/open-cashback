from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.redemption import Redemption
from app.schemas.redemption import RedemptionCreate, RedemptionRead, RedemptionResponse
from app.services.redemption_service import RedemptionService

router = APIRouter(prefix="/redemptions", tags=["redemptions"])


@router.post("", response_model=RedemptionResponse)
def create_redemption(payload: RedemptionCreate, db: Session = Depends(get_db)):
    redemption, tx = RedemptionService(db).create(payload)
    return {"redemption": redemption, "transaction": tx}


@router.get("", response_model=list[RedemptionRead])
def list_redemptions(organization_id: str, db: Session = Depends(get_db)):
    return (
        db.query(Redemption)
        .filter(Redemption.organization_id == organization_id)
        .order_by(Redemption.created_at.desc())
        .all()
    )


@router.get("/{redemption_id}", response_model=RedemptionRead)
def get_redemption(redemption_id: str, organization_id: str, db: Session = Depends(get_db)):
    return RedemptionService(db).get(organization_id, redemption_id)


@router.post("/{redemption_id}/cancel", response_model=RedemptionRead)
def cancel_redemption(redemption_id: str, organization_id: str, db: Session = Depends(get_db)):
    return RedemptionService(db).cancel(organization_id, redemption_id)
