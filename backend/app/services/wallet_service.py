from decimal import Decimal

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.wallet import Wallet


class WalletService:
    def __init__(self, db: Session):
        self.db = db

    def create_for_customer(self, organization_id: str, customer_id: str) -> Wallet:
        wallet = Wallet(organization_id=organization_id, customer_id=customer_id)
        self.db.add(wallet)
        self.db.flush()
        return wallet

    def get_by_customer(self, organization_id: str, customer_id: str) -> Wallet:
        wallet = (
            self.db.query(Wallet)
            .filter(Wallet.organization_id == organization_id, Wallet.customer_id == customer_id)
            .first()
        )
        if not wallet:
            raise HTTPException(status_code=404, detail="Wallet not found")
        return wallet

    def get(self, organization_id: str, wallet_id: str) -> Wallet:
        wallet = (
            self.db.query(Wallet)
            .filter(Wallet.organization_id == organization_id, Wallet.id == wallet_id)
            .first()
        )
        if not wallet:
            raise HTTPException(status_code=404, detail="Wallet not found")
        return wallet

    def apply_delta(self, wallet: Wallet, amount: Decimal, tx_type: str) -> Wallet:
        if tx_type in {"EARNED", "BONUS", "REFERRAL", "UNLOCKED"}:
            wallet.available_balance += amount
            wallet.lifetime_earned += amount
        elif tx_type == "REDEEMED":
            wallet.available_balance -= abs(amount)
            wallet.redeemed_balance += abs(amount)
            wallet.lifetime_redeemed += abs(amount)
        elif tx_type in {"REVERSED", "EXPIRED", "ADJUSTED", "LOCKED"}:
            wallet.available_balance += amount
            if tx_type == "EXPIRED":
                wallet.expired_balance += abs(amount)
        self.db.flush()
        return wallet
