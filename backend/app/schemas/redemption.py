from decimal import Decimal

from app.schemas.base import ApiModel, TimestampedRead
from app.schemas.cashback import CashbackTransactionRead


class RedemptionCreate(ApiModel):
    organization_id: str
    branch_id: str
    customer_id: str
    sale_id: str | None = None
    amount: Decimal
    redemption_code: str | None = None


class RedemptionRead(TimestampedRead):
    organization_id: str
    branch_id: str
    customer_id: str
    wallet_id: str
    sale_id: str | None
    amount: Decimal
    status: str
    redemption_code: str


class RedemptionResponse(ApiModel):
    redemption: RedemptionRead
    transaction: CashbackTransactionRead
