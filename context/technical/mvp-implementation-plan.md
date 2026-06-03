# MVP Implementation Plan

## Target MVP definition

Open Cashback MVP is complete when the product can support:

1. Merchant login.
2. Customer login.
3. Merchant dashboard with loyalty KPIs.
4. Customer dashboard with wallet balance and history.
5. Sale registration with cashback generation.
6. Redemption intent/code or QR flow.
7. Merchant redemption confirmation.
8. Ledger explorer with hashes.
9. Basic API key management.
10. Blockchain anchoring placeholder visible in UI.

## Sprint 1 - Auth, roles and tenant context

### Backend

- Implement real `GET /api/v1/auth/me`.
- Add bootstrap admin command or endpoint for development.
- Add role-based dependencies.
- Add merchant user login.
- Add customer credential login.
- Ensure JWT includes subject type, organization_id and role.

### Frontend

- Add app shell.
- Add route groups for `/customer` and `/merchant`.
- Add login screens with mock/demo login support.
- Add auth state store.

### Tests

- Login success/failure.
- Role guard.
- Organization isolation.

## Sprint 2 - Customer Portal MVP

### Backend

- Add customer self-service endpoints:

```text
GET /api/v1/customer/me
GET /api/v1/customer/wallet
GET /api/v1/customer/transactions
GET /api/v1/customer/benefits
```

### Frontend

- Customer dashboard.
- Wallet page.
- History page.
- Web3 audit placeholder.

### Demo goal

A customer can see $10 earned from a registered sale.

## Sprint 3 - Merchant Dashboard MVP

### Backend

- Add merchant-scoped dashboard endpoints:

```text
GET /api/v1/merchant/summary
GET /api/v1/merchant/customers
GET /api/v1/merchant/sales
GET /api/v1/merchant/redemptions
GET /api/v1/merchant/ledger
```

### Frontend

- Merchant dashboard.
- Customers table.
- Sales table.
- Redemptions table.
- Ledger table.

### Demo goal

Merchant sees issued cashback, redeemed cashback and outstanding liability.

## Sprint 4 - Redemption code / QR intent

### Backend

Add model:

```text
RedemptionIntent
  id
  organization_id
  customer_id
  wallet_id
  amount
  code_hash
  status
  expires_at
  redeemed_at
  created_at
  updated_at
```

Endpoints:

```text
POST /api/v1/customer/redemption-intents
GET /api/v1/customer/redemption-intents/{id}
POST /api/v1/merchant/redemption-intents/{code}/redeem
POST /api/v1/customer/redemption-intents/{id}/cancel
```

### Frontend

- Customer redeem form.
- QR/code display.
- Merchant redeem/scan placeholder.

### Tests

- Intent expiration.
- One-time use.
- Insufficient balance.
- Cross-tenant rejection.

## Sprint 5 - API keys and idempotency

### Backend

Add:

```text
IdempotencyKey
ApiRequestLog
WebhookEndpoint
WebhookEvent
```

Implement:

- `Idempotency-Key` handling for sales and redemptions.
- API key creation with hashed key storage.
- API scopes.
- Basic API request logs.

### Frontend

- Merchant integrations page.
- API key manager.
- Webhook settings placeholder.

## Sprint 6 - Campaign MVP

### Backend

- CRUD cashback rules.
- CRUD campaigns.
- Active rule resolver.
- Rule priority.
- Date validity.
- Min purchase amount.

### Frontend

- Global cashback settings.
- Campaign list.
- Campaign create/edit form.
- Cashback simulator.

## Sprint 7 - Ledger explorer and reports

### Backend

- Paginated ledger endpoints.
- Date range filters.
- Report filters by branch/customer/campaign.
- CSV export later.

### Frontend

- Ledger explorer.
- Report pages.
- Movement detail drawer.
- Hash copy and chain view.

## Sprint 8 - Blockchain anchoring prototype

### Backend

Add:

```text
LedgerBatch
LedgerBatchItem
```

Implement:

- Build batch from cashback transactions.
- Compute batch hash.
- Simulate anchoring.
- Optional Hardhat/Ganache transaction.

### Frontend

- Blockchain status page.
- Batch list.
- Batch detail.
- Contract address display.

## Immediate implementation priorities

1. Frontend app shell and routing.
2. Demo seed script.
3. Customer dashboard with mock/API adapter.
4. Merchant dashboard with mock/API adapter.
5. Auth/me endpoint and demo users.
6. Redemption intent model.
7. API key model endpoints.

## Technical risks

- Current auth is placeholder; UI needs real subject separation.
- Current idempotency uses external sale uniqueness only; needs request-level idempotency.
- Alembic migration creates metadata wholesale; future migrations should be explicit.
- Current tests could not run in the original environment due missing pip/pytest.
- Frontend currently has no router, API client or state management.
- Customer login model is not yet defined separately from admin users.

## Demo seed data

Create a seed command/script that generates:

- Organization: Demo Merchant.
- Branch: Centro.
- Merchant admin user.
- Customer user.
- Customer wallet.
- Sale: TICKET-0001 for 1000 MXN.
- Cashback earned: 10 MXN.
- Optional redemption: 5 MXN.

This makes frontend demos deterministic.


## Sub-agent backend findings integrated

The backend can support a demo now, but a secure MVP must prioritize:

1. Auth and tenant isolation from JWT/API key claims.
2. Persistent `Idempotency-Key` handling.
3. API key auth and scopes for POS/ERP integrations.
4. QR redemption lifecycle with TTL and replay protection.
5. Paginated and filtered list endpoints.
6. Explicit migrations for future schema changes.
7. Tests for RBAC, idempotency, QR lifecycle and concurrency.

These items are tracked in `context/technical/backend-mvp-gap-analysis.md`.
