from decimal import Decimal

import pytest
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.database import Base
from app.models import *  # noqa: F403
from app.models.branch import Branch
from app.models.organization import Organization
from app.schemas.customer import CustomerCreate
from app.schemas.redemption import RedemptionCreate
from app.schemas.sale import SaleCreate, SaleItemCreate
from app.services.cashback_engine import CashbackEngine
from app.services.customer_service import CustomerService
from app.services.redemption_service import RedemptionService
from app.services.sale_service import SaleService
from app.services.wallet_service import WalletService


@pytest.fixture()
def db():
    engine = create_engine("sqlite+pysqlite:///:memory:")
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    session = SessionLocal()
    yield session
    session.close()


def seed_org_branch(db, rate=Decimal("0.01")):
    org = Organization(name="Atlas Demo", default_cashback_rate=rate)
    db.add(org)
    db.flush()
    branch = Branch(organization_id=org.id, name="Centro", code="CENTRO")
    db.add(branch)
    db.commit()
    db.refresh(org)
    db.refresh(branch)
    return org, branch


def create_customer(db, org):
    return CustomerService(db).create(
        CustomerCreate(
            organization_id=org.id,
            first_name="Cliente",
            last_name="Demo",
            email="cliente@example.com",
            external_reference="POS-CUST-001",
        )
    )


def sale_payload(org, branch, customer, external_sale_id="TICKET-0001"):
    return SaleCreate(
        organization_id=org.id,
        branch_id=branch.id,
        customer_id=customer.id,
        external_sale_id=external_sale_id,
        subtotal_amount=Decimal("1000.00"),
        discount_amount=Decimal("0.00"),
        tax_amount=Decimal("160.00"),
        total_amount=Decimal("1160.00"),
        eligible_amount=Decimal("1000.00"),
        paid_with_cashback_amount=Decimal("0.00"),
        payment_method="cash",
        items=[
            SaleItemCreate(
                sku="SKU-001",
                name="Producto ejemplo",
                quantity=Decimal("2"),
                unit_price=Decimal("500.00"),
                total_amount=Decimal("1000.00"),
            )
        ],
    )


def test_create_customer_creates_wallet(db):
    org, _ = seed_org_branch(db)
    customer = create_customer(db, org)
    wallet = WalletService(db).get_by_customer(org.id, customer.id)
    assert wallet.available_balance == Decimal("0.00")
    assert wallet.customer_id == customer.id


def test_register_sale_generates_cashback_and_wallet_balance(db):
    org, branch = seed_org_branch(db)
    customer = create_customer(db, org)
    sale, rate, amount, tx = SaleService(db).create(sale_payload(org, branch, customer))
    wallet = WalletService(db).get_by_customer(org.id, customer.id)
    assert rate == Decimal("0.010000")
    assert amount == Decimal("10.00")
    assert tx.transaction_type == "EARNED"
    assert tx.hash
    assert sale.status == "COMPLETED"
    assert wallet.available_balance == Decimal("10.00")


def test_redeem_sufficient_balance(db):
    org, branch = seed_org_branch(db)
    customer = create_customer(db, org)
    SaleService(db).create(sale_payload(org, branch, customer))
    redemption, tx = RedemptionService(db).create(
        RedemptionCreate(organization_id=org.id, branch_id=branch.id, customer_id=customer.id, amount=Decimal("5.00"))
    )
    wallet = WalletService(db).get_by_customer(org.id, customer.id)
    assert redemption.status == "COMPLETED"
    assert tx.transaction_type == "REDEEMED"
    assert wallet.available_balance == Decimal("5.00")


def test_reject_redemption_with_insufficient_balance(db):
    org, branch = seed_org_branch(db)
    customer = create_customer(db, org)
    with pytest.raises(HTTPException):
        RedemptionService(db).create(
            RedemptionCreate(organization_id=org.id, branch_id=branch.id, customer_id=customer.id, amount=Decimal("50.00"))
        )


def test_cancel_sale_reverses_cashback(db):
    org, branch = seed_org_branch(db)
    customer = create_customer(db, org)
    sale, _, _, _ = SaleService(db).create(sale_payload(org, branch, customer))
    SaleService(db).cancel(org.id, sale.id)
    wallet = WalletService(db).get_by_customer(org.id, customer.id)
    assert wallet.available_balance == Decimal("0.00")


def test_sale_external_reference_is_idempotent(db):
    org, branch = seed_org_branch(db)
    customer = create_customer(db, org)
    SaleService(db).create(sale_payload(org, branch, customer))
    SaleService(db).create(sale_payload(org, branch, customer))
    wallet = WalletService(db).get_by_customer(org.id, customer.id)
    assert wallet.available_balance == Decimal("10.00")


def test_multi_tenant_isolation(db):
    org1, branch1 = seed_org_branch(db)
    org2, _ = seed_org_branch(db)
    customer = create_customer(db, org1)
    SaleService(db).create(sale_payload(org1, branch1, customer))
    with pytest.raises(HTTPException):
        WalletService(db).get_by_customer(org2.id, customer.id)


def test_money_uses_decimal(db):
    engine = CashbackEngine(db)
    org, _ = seed_org_branch(db)
    _, amount = engine.calculate(org.id, Decimal("1000.00"))
    assert isinstance(amount, Decimal)
    with pytest.raises(TypeError):
        engine.calculate(org.id, 1000.00)  # type: ignore[arg-type]
