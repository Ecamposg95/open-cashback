from datetime import date

from sqlalchemy import Date, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import TimestampMixin, UUIDPrimaryKeyMixin


class Customer(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "customers"
    __table_args__ = (
        UniqueConstraint("organization_id", "external_reference", name="uq_customer_org_external"),
    )

    organization_id: Mapped[str] = mapped_column(ForeignKey("organizations.id"), nullable=False)
    first_name: Mapped[str] = mapped_column(String(120), nullable=False)
    last_name: Mapped[str | None] = mapped_column(String(120))
    email: Mapped[str | None] = mapped_column(String(160))
    phone: Mapped[str | None] = mapped_column(String(40))
    external_reference: Mapped[str | None] = mapped_column(String(120))
    birthdate: Mapped[date | None] = mapped_column(Date)
    status: Mapped[str] = mapped_column(String(30), default="ACTIVE", nullable=False)

    organization = relationship("Organization", back_populates="customers")
    wallet = relationship("Wallet", back_populates="customer", uselist=False)
