from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.models.base import TimestampMixin, UUIDPrimaryKeyMixin


class CashbackRule(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "cashback_rules"

    organization_id: Mapped[str] = mapped_column(ForeignKey("organizations.id"), nullable=False)
    campaign_id: Mapped[str | None] = mapped_column(ForeignKey("campaigns.id"))
    name: Mapped[str] = mapped_column(String(160), nullable=False)
    description: Mapped[str | None] = mapped_column(String(500))
    rule_type: Mapped[str] = mapped_column(String(40), default="GLOBAL_PERCENTAGE", nullable=False)
    cashback_rate: Mapped[Decimal] = mapped_column(Numeric(8, 6), default=Decimal("0.010000"))
    fixed_amount: Mapped[Decimal | None] = mapped_column(Numeric(18, 2))
    min_purchase_amount: Mapped[Decimal | None] = mapped_column(Numeric(18, 2))
    max_cashback_amount: Mapped[Decimal | None] = mapped_column(Numeric(18, 2))
    max_redemption_percentage: Mapped[Decimal | None] = mapped_column(Numeric(8, 6))
    valid_from: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    valid_to: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    status: Mapped[str] = mapped_column(String(30), default="ACTIVE", nullable=False)
