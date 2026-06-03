from app.schemas.base import ApiModel


class LoginRequest(ApiModel):
    email: str
    password: str
    organization_id: str | None = None


class TokenResponse(ApiModel):
    access_token: str
    token_type: str = "bearer"
