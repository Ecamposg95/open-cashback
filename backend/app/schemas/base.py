from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ApiModel(BaseModel):
    model_config = ConfigDict(from_attributes=True, json_encoders={Decimal: lambda v: str(v)})


class TimestampedRead(ApiModel):
    id: str
    created_at: datetime
    updated_at: datetime
