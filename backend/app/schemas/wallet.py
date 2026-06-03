from decimal import Decimal

from app.schemas.base import TimestampedRead


class WalletRead(TimestampedRead):
    organization_id: str
    customer_id: str
    available_balance: Decimal
    pending_balance: Decimal
    redeemed_balance: Decimal
    expired_balance: Decimal
    lifetime_earned: Decimal
    lifetime_redeemed: Decimal
    status: str
