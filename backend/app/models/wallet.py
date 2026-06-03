from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import TimestampMixin, UUIDPrimaryKeyMixin


class Wallet(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "wallets"
    __table_args__ = (UniqueConstraint("organization_id", "customer_id", name="uq_wallet_customer"),)

    organization_id: Mapped[str] = mapped_column(ForeignKey("organizations.id"), nullable=False)
    customer_id: Mapped[str] = mapped_column(ForeignKey("customers.id"), nullable=False)
    available_balance: Mapped[Decimal] = mapped_column(Numeric(18, 2), default=Decimal("0.00"))
    pending_balance: Mapped[Decimal] = mapped_column(Numeric(18, 2), default=Decimal("0.00"))
    redeemed_balance: Mapped[Decimal] = mapped_column(Numeric(18, 2), default=Decimal("0.00"))
    expired_balance: Mapped[Decimal] = mapped_column(Numeric(18, 2), default=Decimal("0.00"))
    lifetime_earned: Mapped[Decimal] = mapped_column(Numeric(18, 2), default=Decimal("0.00"))
    lifetime_redeemed: Mapped[Decimal] = mapped_column(Numeric(18, 2), default=Decimal("0.00"))
    status: Mapped[str] = mapped_column(String(30), default="ACTIVE", nullable=False)

    customer = relationship("Customer", back_populates="wallet")
