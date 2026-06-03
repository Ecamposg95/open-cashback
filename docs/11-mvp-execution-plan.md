# MVP Execution Plan

## Goal

Reach a public, demoable MVP of Open Cashback as Loyalty as a Service.

The MVP must show two working experiences:

1. Customer Portal: customer sees wallet, rewards, transaction history and redemption flow.
2. Merchant Dashboard: business sees loyalty KPIs, customers, sales, redemptions, ledger and integrations readiness.

## Demo narrative

```text
Merchant opens dashboard
  -> sees outstanding liability and cashback metrics
  -> creates customer or selects existing customer
  -> registers POS-like sale
  -> cashback is calculated and ledger transaction is created
  -> customer opens portal
  -> sees available balance and history
  -> customer creates redemption intent/code
  -> merchant confirms redemption
  -> ledger shows REDEEMED movement
  -> blockchain page shows hash anchoring readiness
```

## MVP phases

### Phase 1 - Product shell and demo flow

- Frontend route groups: `/portal`, `/app`, `/admin`.
- Merchant shell with sidebar and dashboard.
- Customer shell with wallet-first dashboard.
- API client and typed money/date helpers.
- Mock/demo data support while auth is completed.
- POS simulator page.

### Phase 2 - Auth and tenant context

- Real `GET /api/v1/auth/me`.
- Merchant user login.
- Customer credential login.
- JWT subject type.
- Role-based route guards.
- Tenant-aware API dependencies.

### Phase 3 - Customer Portal

- Wallet dashboard.
- Transaction timeline.
- Redemption intent/code page.
- Profile page.
- Web3 audit status page.

### Phase 4 - Merchant LaaS Dashboard

- KPI dashboard.
- Customers table and customer detail.
- Sales/POS simulator.
- Ledger explorer.
- Redemptions operational view.
- Organization settings for cashback rate.

### Phase 5 - Integrations

- API keys CRUD.
- API key scopes.
- API request logs.
- Webhook endpoints placeholder.
- Idempotency-Key persistence.

### Phase 6 - Campaign MVP

- Cashback rules CRUD.
- Campaign CRUD.
- Active global rule resolver.
- Rule priority and validity windows.
- Cashback simulator.

### Phase 7 - Blockchain anchoring prototype

- Ledger batches.
- Batch hash computation.
- Simulated anchor and optional Ganache tx.
- Merchant blockchain page.

## Acceptance criteria

- A non-technical viewer can understand the customer value in less than 2 minutes.
- A merchant can understand liability and loyalty performance in less than 2 minutes.
- A developer can run backend and frontend locally from README.
- The demo can produce an EARNED ledger movement from a sale.
- The demo can produce a REDEEMED ledger movement from a redemption.
- Every operational view is organization-scoped.
- The product clearly communicates: internal ledger now, blockchain anchoring ready.

## Immediate next build tasks

1. Replace static frontend with routed app shell.
2. Add customer portal dashboard with demo data.
3. Add merchant dashboard with demo KPIs.
4. Add POS simulator UI shell.
5. Add frontend API client for existing endpoints.
6. Add backend seed script for demo data.
7. Add missing list endpoints for sales and redemptions.
8. Implement auth/me and demo users.


## Current progress

Implemented in this iteration:

- Demo seed script with stable organization, branch, customer and merchant admin IDs.
- Basic bearer auth `/api/v1/auth/me`.
- Sales list endpoint.
- Redemptions list endpoint.
- Frontend API client with demo fallback.
- Customer Portal connected to wallet and ledger endpoints.
- Merchant Dashboard connected to reports, customers and ledger endpoints.
- POS simulator can submit demo sales to `POST /api/v1/sales` when backend is running.

Demo command:

```bash
cd backend
alembic upgrade head
python scripts/seed_demo.py
uvicorn app.main:app --reload
```


## Next development focus

The next sprint should move the project from demo-connected to MVP-secure:

1. Merchant login UI and token storage.
2. Tenant context from authenticated user/API key.
3. Persistent idempotency for sales and redemptions.
4. API keys with scopes for POS/ERP/e-commerce.
5. Redemption intent / QR-code flow.

Detailed plan: `context/technical/next-development-plan.md`.
