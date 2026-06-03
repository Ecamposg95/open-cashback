from decimal import Decimal, ROUND_HALF_UP

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.organization import Organization


TWOPLACES = Decimal("0.01")


class CashbackEngine:
    def __init__(self, db: Session):
        self.db = db

    def get_rate(self, organization_id: str) -> Decimal:
        organization = self.db.get(Organization, organization_id)
        if not organization or organization.status != "ACTIVE":
            raise HTTPException(status_code=404, detail="Active organization not found")
        return Decimal(organization.default_cashback_rate)

    def calculate(self, organization_id: str, eligible_amount: Decimal) -> tuple[Decimal, Decimal]:
        if not isinstance(eligible_amount, Decimal):
            raise TypeError("eligible_amount must be Decimal")
        if eligible_amount < Decimal("0.00"):
            raise HTTPException(status_code=400, detail="eligible_amount must be positive")
        rate = self.get_rate(organization_id)
        amount = (eligible_amount * rate).quantize(TWOPLACES, rounding=ROUND_HALF_UP)
        return rate, amount
