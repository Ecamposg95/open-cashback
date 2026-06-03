from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.models.base import TimestampMixin, UUIDPrimaryKeyMixin


class BlockchainTransaction(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "blockchain_transactions"

    organization_id: Mapped[str] = mapped_column(ForeignKey("organizations.id"), nullable=False)
    batch_id: Mapped[str] = mapped_column(String(120), nullable=False)
    network: Mapped[str] = mapped_column(String(80), nullable=False)
    contract_address: Mapped[str | None] = mapped_column(String(120))
    transaction_hash: Mapped[str | None] = mapped_column(String(140))
    block_number: Mapped[int | None] = mapped_column(Integer)
    payload_hash: Mapped[str] = mapped_column(String(64), nullable=False)
    status: Mapped[str] = mapped_column(String(30), default="PENDING", nullable=False)
