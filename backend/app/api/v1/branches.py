from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.branch import Branch
from app.schemas.branch import BranchCreate, BranchRead

router = APIRouter(prefix="/branches", tags=["branches"])


@router.post("", response_model=BranchRead)
def create_branch(payload: BranchCreate, db: Session = Depends(get_db)):
    branch = Branch(**payload.model_dump())
    db.add(branch)
    db.commit()
    db.refresh(branch)
    return branch


@router.get("", response_model=list[BranchRead])
def list_branches(organization_id: str, db: Session = Depends(get_db)):
    return db.query(Branch).filter(Branch.organization_id == organization_id).all()


@router.get("/{branch_id}", response_model=BranchRead)
def get_branch(branch_id: str, organization_id: str, db: Session = Depends(get_db)):
    branch = db.query(Branch).filter(Branch.organization_id == organization_id, Branch.id == branch_id).first()
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")
    return branch
