from app.schemas.base import ApiModel, TimestampedRead


class BranchCreate(ApiModel):
    organization_id: str
    name: str
    code: str
    address: str | None = None
    city: str | None = None
    state: str | None = None
    country: str = "MX"
    timezone: str = "America/Mexico_City"


class BranchRead(TimestampedRead):
    organization_id: str
    name: str
    code: str
    address: str | None
    city: str | None
    state: str | None
    country: str
    timezone: str
    status: str
