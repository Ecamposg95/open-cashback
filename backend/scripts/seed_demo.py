from decimal import Decimal

from app.core.database import SessionLocal
from app.core.security import hash_password
from app.models.branch import Branch
from app.models.customer import Customer
from app.models.organization import Organization
from app.models.redemption import Redemption
from app.models.sale import Sale
from app.models.user import User
from app.models.wallet import Wallet
from app.services.redemption_service import RedemptionService
from app.services.sale_service import SaleService
from app.schemas.redemption import RedemptionCreate
from app.schemas.sale import SaleCreate, SaleItemCreate

DEMO_ORG_ID = "11111111-1111-1111-1111-111111111111"
DEMO_BRANCH_ID = "22222222-2222-2222-2222-222222222222"
DEMO_CUSTOMER_ID = "33333333-3333-3333-3333-333333333333"
DEMO_USER_ID = "44444444-4444-4444-4444-444444444444"


def get_or_create(db, model, item_id: str, **values):
    item = db.get(model, item_id)
    if item:
        for key, value in values.items():
            setattr(item, key, value)
        db.flush()
        return item
    item = model(id=item_id, **values)
    db.add(item)
    db.flush()
    return item


def seed() -> None:
    db = SessionLocal()
    try:
        org = get_or_create(
            db,
            Organization,
            DEMO_ORG_ID,
            name="Demo Merchant",
            legal_name="Demo Merchant SA de CV",
            tax_id="DEMO010101XXX",
            default_currency="MXN",
            default_cashback_rate=Decimal("0.010000"),
            status="ACTIVE",
        )
        branch = get_or_create(
            db,
            Branch,
            DEMO_BRANCH_ID,
            organization_id=org.id,
            name="Centro",
            code="CENTRO",
            city="Toluca",
            state="Estado de Mexico",
            country="MX",
            status="ACTIVE",
        )
        get_or_create(
            db,
            User,
            DEMO_USER_ID,
            organization_id=org.id,
            branch_id=branch.id,
            name="Demo Admin",
            email="admin@demo.open-cashback.local",
            password_hash=hash_password("demo1234"),
            role="ORG_ADMIN",
            status="ACTIVE",
        )
        db.commit()

        customer = get_or_create(
            db,
            Customer,
            DEMO_CUSTOMER_ID,
            organization_id=org.id,
            first_name="Emmanuel",
            last_name="Campos",
            email="cliente@example.com",
            phone="7221234567",
            external_reference="DEMO-CUST-001",
            status="ACTIVE",
        )
        wallet = (
            db.query(Wallet)
            .filter(Wallet.organization_id == org.id, Wallet.customer_id == customer.id)
            .first()
        )
        if not wallet:
            db.add(Wallet(organization_id=org.id, customer_id=customer.id))
        db.commit()

        sale_exists = (
            db.query(Sale)
            .filter(Sale.organization_id == org.id, Sale.external_sale_id == "TICKET-DEMO-0001")
            .first()
        )
        if not sale_exists:
            SaleService(db).create(
                SaleCreate(
                    organization_id=org.id,
                    branch_id=branch.id,
                    customer_id=DEMO_CUSTOMER_ID,
                    external_sale_id="TICKET-DEMO-0001",
                    subtotal_amount=Decimal("1000.00"),
                    discount_amount=Decimal("0.00"),
                    tax_amount=Decimal("160.00"),
                    total_amount=Decimal("1160.00"),
                    eligible_amount=Decimal("1000.00"),
                    paid_with_cashback_amount=Decimal("0.00"),
                    payment_method="cash",
                    items=[
                        SaleItemCreate(
                            sku="SKU-DEMO-001",
                            name="Producto demo",
                            category="General",
                            quantity=Decimal("2"),
                            unit_price=Decimal("500.00"),
                            total_amount=Decimal("1000.00"),
                        )
                    ],
                )
            )

        redemption_exists = (
            db.query(Redemption)
            .filter(Redemption.organization_id == org.id, Redemption.redemption_code == "RED-DEMO-0001")
            .first()
        )
        if not redemption_exists:
            RedemptionService(db).create(
                RedemptionCreate(
                    organization_id=org.id,
                    branch_id=branch.id,
                    customer_id=DEMO_CUSTOMER_ID,
                    amount=Decimal("5.00"),
                    redemption_code="RED-DEMO-0001",
                )
            )

        print("Demo seed complete")
        print(f"organization_id={DEMO_ORG_ID}")
        print(f"branch_id={DEMO_BRANCH_ID}")
        print(f"customer_id={DEMO_CUSTOMER_ID}")
        print("merchant_login=admin@demo.open-cashback.local / demo1234")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
