from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.security import create_access_token, verify_password
from app.models.user import User
from app.schemas.auth import LoginRequest


class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def login(self, payload: LoginRequest) -> str:
        query = self.db.query(User).filter(User.email == payload.email, User.status == "ACTIVE")
        if payload.organization_id:
            query = query.filter(User.organization_id == payload.organization_id)
        user = query.first()
        if not user or not verify_password(payload.password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return create_access_token(user.id, {"organization_id": user.organization_id, "role": user.role})
