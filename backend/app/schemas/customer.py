from datetime import date

from app.schemas.base import ApiModel, TimestampedRead
from app.schemas.wallet import WalletRead


class CustomerCreate(ApiModel):
    organization_id: str
    first_name: str
    last_name: str | None = None
    email: str | None = None
    phone: str | None = None
    external_reference: str | None = None
    birthdate: date | None = None


class CustomerUpdate(ApiModel):
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    phone: str | None = None
    status: str | None = None


class CustomerRead(TimestampedRead):
    organization_id: str
    first_name: str
    last_name: str | None
    email: str | None
    phone: str | None
    external_reference: str | None
    birthdate: date | None
    status: str


class CustomerWithWallet(CustomerRead):
    wallet: WalletRead
