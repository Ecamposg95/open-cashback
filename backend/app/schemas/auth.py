from datetime import datetime

from app.schemas.base import ApiModel


class LoginRequest(ApiModel):
    email: str
    password: str
    organization_id: str | None = None


class TokenResponse(ApiModel):
    access_token: str
    token_type: str = "bearer"


class CurrentUserRead(ApiModel):
    id: str
    organization_id: str | None
    branch_id: str | None
    name: str
    email: str
    role: str
    status: str
    created_at: datetime
    updated_at: datetime
