# MVP Collaboration Brief

## Objective

Build Open Cashback MVP as a public, demoable Loyalty as a Service platform.

The MVP has two primary experiences:

1. Customer Portal: the end customer sees rewards, cashback, history, wallet state and redemption actions.
2. Merchant Dashboard: the business adopting Open Cashback as LaaS configures and monitors loyalty operations.

A third internal Admin Console can remain minimal until after the first demo.

## North-star demo

The target demo should complete this story:

```text
A merchant signs in
  -> sees loyalty KPIs
  -> creates or views a customer
  -> registers a sale from POS/API
  -> cashback is generated
  -> customer signs in
  -> sees wallet balance and transaction history
  -> customer generates redemption intent/QR
  -> merchant redeems it
  -> ledger shows EARNED and REDEEMED movements
  -> Web3 page shows hash/anchoring readiness
```

## MVP boundaries

In scope:

- Customer wallet UI.
- Merchant operations UI.
- Auth separation between customer and merchant users.
- Cashback sale flow.
- Redemption flow.
- Ledger explorer basics.
- API keys foundation.
- Idempotency foundation.
- Reports summary.
- Blockchain anchoring placeholder.

Out of scope for MVP:

- ERC20 token.
- Mainnet/testnet deployment requirement.
- DeFi, exchange, custody or KYC.
- Complex campaign engine with all rule types.
- Multi-merchant settlement.
- Native mobile app.

## Recommended agent ownership slices

### Backend Core Agent

Owns:

- Auth roles and permissions.
- Idempotency store.
- API keys.
- QR/redemption intent model.
- Tests.

Files:

- `backend/app/models/`
- `backend/app/schemas/`
- `backend/app/services/`
- `backend/app/api/v1/`
- `backend/app/tests/`
- `backend/alembic/versions/`

### Frontend Customer Agent

Owns:

- Customer routes.
- Wallet dashboard.
- Transaction history.
- Redemption intent/QR UI.
- Web3 audit status page.

Files:

- `frontend/src/features/customer/`
- `frontend/src/components/`
- `frontend/src/lib/`

### Frontend Merchant Agent

Owns:

- Merchant dashboard.
- Customers table.
- Sales view.
- Ledger view.
- Reports and settings.
- Integrations/API keys UI.

Files:

- `frontend/src/features/merchant/`
- `frontend/src/components/`
- `frontend/src/lib/`

### Docs/Product Agent

Owns:

- Roadmap.
- API documentation.
- Product specs.
- Demo script.
- Architecture decision records.

Files:

- `docs/`
- `context/`
- `README.md`

## Quality bar

- Backend endpoints should be testable independently.
- Frontend screens should be usable with mock data first, then API-wired.
- Every money field must use Decimal backend and formatted currency frontend.
- Every merchant query must be organization-scoped.
- Ledger movements are append-only; corrections are reverse/adjustment transactions.
