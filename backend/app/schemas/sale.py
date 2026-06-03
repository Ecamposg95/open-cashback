from datetime import datetime
from decimal import Decimal

from app.schemas.base import ApiModel, TimestampedRead
from app.schemas.cashback import CashbackTransactionRead


class SaleItemCreate(ApiModel):
    product_id: str | None = None
    sku: str | None = None
    name: str
    category: str | None = None
    quantity: Decimal
    unit_price: Decimal
    discount_amount: Decimal = Decimal("0.00")
    total_amount: Decimal
    eligible_for_cashback: bool = True


class SaleCreate(ApiModel):
    organization_id: str
    branch_id: str
    customer_id: str
    external_sale_id: str
    subtotal_amount: Decimal
    discount_amount: Decimal = Decimal("0.00")
    tax_amount: Decimal = Decimal("0.00")
    total_amount: Decimal
    eligible_amount: Decimal
    paid_with_cashback_amount: Decimal = Decimal("0.00")
    payment_method: str | None = None
    sale_datetime: datetime | None = None
    items: list[SaleItemCreate] = []


class SaleItemRead(TimestampedRead):
    sale_id: str
    product_id: str | None
    sku: str | None
    name: str
    category: str | None
    quantity: Decimal
    unit_price: Decimal
    discount_amount: Decimal
    total_amount: Decimal
    eligible_for_cashback: bool


class SaleRead(TimestampedRead):
    organization_id: str
    branch_id: str
    customer_id: str
    external_sale_id: str
    subtotal_amount: Decimal
    discount_amount: Decimal
    tax_amount: Decimal
    total_amount: Decimal
    eligible_amount: Decimal
    paid_with_cashback_amount: Decimal
    payment_method: str | None
    status: str
    sale_datetime: datetime
    items: list[SaleItemRead] = []


class SaleCashbackResponse(ApiModel):
    sale: SaleRead
    cashback_rate: Decimal
    cashback_amount: Decimal
    transaction: CashbackTransactionRead | None
