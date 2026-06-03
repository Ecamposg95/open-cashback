from decimal import Decimal

from sqlalchemy import Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import TimestampMixin, UUIDPrimaryKeyMixin


class Organization(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "organizations"

    name: Mapped[str] = mapped_column(String(160), nullable=False)
    legal_name: Mapped[str | None] = mapped_column(String(200))
    tax_id: Mapped[str | None] = mapped_column(String(80))
    status: Mapped[str] = mapped_column(String(30), default="ACTIVE", nullable=False)
    default_currency: Mapped[str] = mapped_column(String(3), default="MXN", nullable=False)
    default_cashback_rate: Mapped[Decimal] = mapped_column(
        Numeric(8, 6), default=Decimal("0.010000"), nullable=False
    )

    branches = relationship("Branch", back_populates="organization")
    customers = relationship("Customer", back_populates="organization")
