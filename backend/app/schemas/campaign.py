from datetime import datetime

from app.schemas.base import ApiModel, TimestampedRead


class CampaignCreate(ApiModel):
    organization_id: str
    name: str
    description: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    priority: int = 100


class CampaignRead(TimestampedRead):
    organization_id: str
    name: str
    description: str | None
    start_date: datetime | None
    end_date: datetime | None
    status: str
    priority: int
