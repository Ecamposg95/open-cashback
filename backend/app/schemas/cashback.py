from datetime import datetime
from decimal import Decimal

from app.schemas.base import ApiModel, TimestampedRead


class CashbackCalculationRequest(ApiModel):
    organization_id: str
    eligible_amount: Decimal


class CashbackCalculationResponse(ApiModel):
    cashback_rate: Decimal
    eligible_amount: Decimal
    cashback_amount: Decimal


class CashbackTransactionRead(TimestampedRead):
    organization_id: str
    branch_id: str | None
    customer_id: str
    wallet_id: str
    sale_id: str | None
    redemption_id: str | None
    campaign_id: str | None
    transaction_type: str
    status: str
    amount: Decimal
    currency: str
    description: str | None
    reference: str | None
    hash: str
    previous_hash: str | None
    available_at: datetime | None
    expires_at: datetime | None
    created_by: str | None
