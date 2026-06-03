import hashlib

from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.blockchain_transaction import BlockchainTransaction
from app.schemas.blockchain import BlockchainAnchorRequest


class BlockchainService:
    def __init__(self, db: Session):
        self.db = db

    def anchor_batch(self, payload: BlockchainAnchorRequest) -> BlockchainTransaction:
        simulated_hash = hashlib.sha256(
            f"{payload.organization_id}|{payload.batch_id}|{payload.payload_hash}".encode("utf-8")
        ).hexdigest()
        tx = BlockchainTransaction(
            organization_id=payload.organization_id,
            batch_id=payload.batch_id,
            network=settings.blockchain_network,
            contract_address=settings.blockchain_contract_address,
            transaction_hash=f"simulated-{simulated_hash[:48]}",
            block_number=None,
            payload_hash=payload.payload_hash,
            status="SIMULATED" if not settings.blockchain_enabled else "PENDING",
        )
        self.db.add(tx)
        self.db.commit()
        self.db.refresh(tx)
        return tx
