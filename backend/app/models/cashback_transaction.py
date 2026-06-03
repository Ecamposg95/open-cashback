from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Index, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.models.base import TimestampMixin, UUIDPrimaryKeyMixin


class CashbackTransaction(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "cashback_transactions"
    __table_args__ = (Index("ix_cashback_org_wallet_created", "organization_id", "wallet_id", "created_at"),)

    organization_id: Mapped[str] = mapped_column(ForeignKey("organizations.id"), nullable=False)
    branch_id: Mapped[str | None] = mapped_column(ForeignKey("branches.id"))
    customer_id: Mapped[str] = mapped_column(ForeignKey("customers.id"), nullable=False)
    wallet_id: Mapped[str] = mapped_column(ForeignKey("wallets.id"), nullable=False)
    sale_id: Mapped[str | None] = mapped_column(ForeignKey("sales.id"))
    redemption_id: Mapped[str | None] = mapped_column(ForeignKey("redemptions.id"))
    campaign_id: Mapped[str | None] = mapped_column(ForeignKey("campaigns.id"))
    transaction_type: Mapped[str] = mapped_column(String(30), nullable=False)
    status: Mapped[str] = mapped_column(String(30), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    currency: Mapped[str] = mapped_column(String(3), default="MXN", nullable=False)
    description: Mapped[str | None] = mapped_column(String(500))
    reference: Mapped[str | None] = mapped_column(String(180))
    hash: Mapped[str] = mapped_column(String(64), nullable=False)
    previous_hash: Mapped[str | None] = mapped_column(String(64))
    available_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    expires_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[str | None] = mapped_column(String(120))
