from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.organization import Organization
from app.schemas.organization import OrganizationCreate, OrganizationRead, OrganizationUpdate

router = APIRouter(prefix="/organizations", tags=["organizations"])


@router.post("", response_model=OrganizationRead)
def create_organization(payload: OrganizationCreate, db: Session = Depends(get_db)):
    organization = Organization(**payload.model_dump())
    db.add(organization)
    db.commit()
    db.refresh(organization)
    return organization


@router.get("", response_model=list[OrganizationRead])
def list_organizations(db: Session = Depends(get_db)):
    return db.query(Organization).all()


@router.get("/{organization_id}", response_model=OrganizationRead)
def get_organization(organization_id: str, db: Session = Depends(get_db)):
    organization = db.get(Organization, organization_id)
    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found")
    return organization


@router.patch("/{organization_id}", response_model=OrganizationRead)
def update_organization(organization_id: str, payload: OrganizationUpdate, db: Session = Depends(get_db)):
    organization = db.get(Organization, organization_id)
    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(organization, key, value)
    db.commit()
    db.refresh(organization)
    return organization
