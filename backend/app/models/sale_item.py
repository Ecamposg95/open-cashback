from decimal import Decimal

from sqlalchemy import Boolean, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import TimestampMixin, UUIDPrimaryKeyMixin


class SaleItem(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "sale_items"

    sale_id: Mapped[str] = mapped_column(ForeignKey("sales.id"), nullable=False)
    product_id: Mapped[str | None] = mapped_column(String(120))
    sku: Mapped[str | None] = mapped_column(String(120))
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    category: Mapped[str | None] = mapped_column(String(120))
    quantity: Mapped[Decimal] = mapped_column(Numeric(18, 3), nullable=False)
    unit_price: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    discount_amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), default=Decimal("0.00"))
    total_amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    eligible_for_cashback: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    sale = relationship("Sale", back_populates="items")
