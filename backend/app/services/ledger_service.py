import hashlib
from datetime import datetime, timezone
from decimal import Decimal

from sqlalchemy.orm import Session

from app.models.cashback_transaction import CashbackTransaction
from app.models.wallet import Wallet
from app.services.wallet_service import WalletService


class LedgerService:
    def __init__(self, db: Session):
        self.db = db

    def _previous_hash(self, wallet_id: str) -> str | None:
        previous = (
            self.db.query(CashbackTransaction)
            .filter(CashbackTransaction.wallet_id == wallet_id)
            .order_by(CashbackTransaction.created_at.desc())
            .first()
        )
        return previous.hash if previous else None

    def _hash_payload(self, tx: CashbackTransaction, previous_hash: str | None) -> str:
        payload = "|".join(
            [
                tx.id,
                tx.organization_id,
                tx.wallet_id,
                f"{Decimal(tx.amount):.2f}",
                tx.transaction_type,
                previous_hash or "",
                tx.created_at.isoformat(),
            ]
        )
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()

    def create_transaction(
        self,
        *,
        organization_id: str,
        customer_id: str,
        wallet: Wallet,
        amount: Decimal,
        transaction_type: str,
        status: str = "AVAILABLE",
        branch_id: str | None = None,
        sale_id: str | None = None,
        redemption_id: str | None = None,
        campaign_id: str | None = None,
        description: str | None = None,
        reference: str | None = None,
    ) -> CashbackTransaction:
        previous_hash = self._previous_hash(wallet.id)
        tx = CashbackTransaction(
            organization_id=organization_id,
            branch_id=branch_id,
            customer_id=customer_id,
            wallet_id=wallet.id,
            sale_id=sale_id,
            redemption_id=redemption_id,
            campaign_id=campaign_id,
            transaction_type=transaction_type,
            status=status,
            amount=amount,
            description=description,
            reference=reference,
            previous_hash=previous_hash,
            hash="",
            created_at=datetime.now(timezone.utc),
        )
        self.db.add(tx)
        self.db.flush()
        tx.hash = self._hash_payload(tx, previous_hash)
        WalletService(self.db).apply_delta(wallet, amount, transaction_type)
        self.db.flush()
        return tx
