from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerUpdate
from app.services.wallet_service import WalletService


class CustomerService:
    def __init__(self, db: Session):
        self.db = db

    def create(self, payload: CustomerCreate) -> Customer:
        if payload.external_reference:
            existing = (
                self.db.query(Customer)
                .filter(
                    Customer.organization_id == payload.organization_id,
                    Customer.external_reference == payload.external_reference,
                )
                .first()
            )
            if existing:
                return existing
        customer = Customer(**payload.model_dump())
        self.db.add(customer)
        self.db.flush()
        WalletService(self.db).create_for_customer(customer.organization_id, customer.id)
        self.db.commit()
        self.db.refresh(customer)
        return customer

    def get(self, organization_id: str, customer_id: str) -> Customer:
        customer = (
            self.db.query(Customer)
            .filter(Customer.organization_id == organization_id, Customer.id == customer_id)
            .first()
        )
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        return customer

    def list(self, organization_id: str) -> list[Customer]:
        return self.db.query(Customer).filter(Customer.organization_id == organization_id).all()

    def update(self, organization_id: str, customer_id: str, payload: CustomerUpdate) -> Customer:
        customer = self.get(organization_id, customer_id)
        for key, value in payload.model_dump(exclude_unset=True).items():
            setattr(customer, key, value)
        self.db.commit()
        self.db.refresh(customer)
        return customer
