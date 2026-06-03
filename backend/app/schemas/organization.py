from decimal import Decimal

from app.schemas.base import ApiModel, TimestampedRead


class OrganizationCreate(ApiModel):
    name: str
    legal_name: str | None = None
    tax_id: str | None = None
    default_currency: str = "MXN"
    default_cashback_rate: Decimal = Decimal("0.01")


class OrganizationUpdate(ApiModel):
    name: str | None = None
    legal_name: str | None = None
    tax_id: str | None = None
    status: str | None = None
    default_cashback_rate: Decimal | None = None


class OrganizationRead(TimestampedRead):
    name: str
    legal_name: str | None
    tax_id: str | None
    status: str
    default_currency: str
    default_cashback_rate: Decimal
