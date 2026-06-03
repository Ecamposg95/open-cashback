from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.blockchain_transaction import BlockchainTransaction
from app.schemas.blockchain import BlockchainAnchorRequest, BlockchainTransactionRead
from app.services.blockchain_service import BlockchainService

router = APIRouter(prefix="/blockchain", tags=["blockchain"])


@router.post("/anchor", response_model=BlockchainTransactionRead)
def anchor_batch(payload: BlockchainAnchorRequest, db: Session = Depends(get_db)):
    return BlockchainService(db).anchor_batch(payload)


@router.get("/transactions/{tx_id}", response_model=BlockchainTransactionRead)
def get_blockchain_transaction(tx_id: str, organization_id: str, db: Session = Depends(get_db)):
    tx = db.query(BlockchainTransaction).filter(BlockchainTransaction.organization_id == organization_id, BlockchainTransaction.id == tx_id).first()
    if not tx:
        raise HTTPException(status_code=404, detail="Blockchain transaction not found")
    return tx
