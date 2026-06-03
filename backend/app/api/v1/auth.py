from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.permissions import get_current_user
from app.models.user import User
from app.schemas.auth import CurrentUserRead, LoginRequest, TokenResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    return {"access_token": AuthService(db).login(payload)}


@router.get("/me", response_model=CurrentUserRead)
def me(current_user: User = Depends(get_current_user)):
    return current_user
