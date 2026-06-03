from datetime import datetime, timezone
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Numeric, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import TimestampMixin, UUIDPrimaryKeyMixin


class Sale(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "sales"
    __table_args__ = (
        UniqueConstraint("organization_id", "external_sale_id", name="uq_sale_org_external"),
    )

    organization_id: Mapped[str] = mapped_column(ForeignKey("organizations.id"), nullable=False)
    branch_id: Mapped[str] = mapped_column(ForeignKey("branches.id"), nullable=False)
    customer_id: Mapped[str] = mapped_column(ForeignKey("customers.id"), nullable=False)
    external_sale_id: Mapped[str] = mapped_column(String(140), nullable=False)
    subtotal_amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    discount_amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), default=Decimal("0.00"))
    tax_amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), default=Decimal("0.00"))
    total_amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    eligible_amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    paid_with_cashback_amount: Mapped[Decimal] = mapped_column(
        Numeric(18, 2), default=Decimal("0.00")
    )
    payment_method: Mapped[str | None] = mapped_column(String(80))
    status: Mapped[str] = mapped_column(String(30), default="COMPLETED", nullable=False)
    sale_datetime: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False
    )

    items = relationship("SaleItem", back_populates="sale", cascade="all, delete-orphan")
