from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    return {"access_token": AuthService(db).login(payload)}


@router.get("/me")
def me():
    return {"status": "placeholder", "message": "JWT user resolution will be expanded in Sprint 1"}
