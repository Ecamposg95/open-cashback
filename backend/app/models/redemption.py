from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.models.base import TimestampMixin, UUIDPrimaryKeyMixin


class Redemption(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "redemptions"
    __table_args__ = (UniqueConstraint("organization_id", "redemption_code", name="uq_redemption_code"),)

    organization_id: Mapped[str] = mapped_column(ForeignKey("organizations.id"), nullable=False)
    branch_id: Mapped[str] = mapped_column(ForeignKey("branches.id"), nullable=False)
    customer_id: Mapped[str] = mapped_column(ForeignKey("customers.id"), nullable=False)
    wallet_id: Mapped[str] = mapped_column(ForeignKey("wallets.id"), nullable=False)
    sale_id: Mapped[str | None] = mapped_column(ForeignKey("sales.id"))
    amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    status: Mapped[str] = mapped_column(String(30), default="COMPLETED", nullable=False)
    redemption_code: Mapped[str] = mapped_column(String(120), nullable=False)
