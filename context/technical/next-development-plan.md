# Next Development Plan

## Current state after commit `c3d4b7d`

Open Cashback now has:

- Backend core for organizations, branches, customers, wallets, sales, cashback ledger and redemptions.
- Demo seed script with stable IDs and merchant credentials.
- Basic bearer auth with `/api/v1/auth/me`.
- Sales and redemptions list endpoints.
- Frontend Merchant LaaS Dashboard with API fallback.
- Frontend Customer Portal with API fallback.
- POS simulator capable of posting demo sales when backend is running.
- Context docs for collaborative agents.

## What can be advanced next

The next work should move the project from demo-connected to MVP-secure. The most useful progress is not more screens; it is making the existing flows safe enough for POS/ERP style usage.

## Priority 1 - Auth route guards and tenant context

### Why

The UI can call the backend, and `/auth/me` works, but most operational endpoints still accept `organization_id` from query/body. For MVP, merchant routes must derive tenant context from authenticated user or API key.

### Backend tasks

- Add a dependency that resolves `organization_id` from `current_user.organization_id`.
- Keep explicit `organization_id` only for superadmin/internal routes.
- Add role guards for:
  - `SUPERADMIN`
  - `ORG_ADMIN`
  - `BRANCH_MANAGER`
  - `CASHIER`
  - `API_CLIENT`
- Protect merchant-facing endpoints.
- Add clear 401/403 responses.

### Frontend tasks

- Add login page for merchant demo.
- Store token in local storage for now.
- Call `/api/v1/auth/me` after login.
- Show authenticated org/user in sidebar.
- Add simple route guard for `/app/*`.

### Acceptance criteria

- Merchant can login with demo credentials.
- `/auth/me` returns user info.
- Merchant dashboard uses token where required.
- A missing token receives 401 on protected endpoints.

## Priority 2 - Persistent idempotency for POS flows

### Why

POS and ERP systems retry requests. External sale ID helps, but the platform needs request-level idempotency to prevent duplicate rewards and double redemptions.

### Backend tasks

Create model:

```text
IdempotencyKey
  id
  organization_id
  key
  request_hash
  response_body
  status_code
  resource_type
  resource_id
  expires_at
  created_at
  updated_at
```

Add service:

```text
IdempotencyService
  get_existing_result()
  reserve_key()
  store_result()
  validate_payload_hash()
```

Apply first to:

- `POST /api/v1/sales`
- `POST /api/v1/redemptions`
- `POST /api/v1/sales/{sale_id}/cancel`

### Acceptance criteria

- Same idempotency key + same payload returns same result.
- Same key + different payload returns 409.
- Duplicate POS retry does not create duplicate ledger transactions.

## Priority 3 - API keys for LaaS integrations

### Why

Open Cashback is LaaS. Businesses must integrate POS/ERP/e-commerce without human JWT sessions.

### Backend tasks

Extend `ApiKey` fields:

```text
prefix
last4
expires_at
created_by
revoked_at
```

Add endpoints:

```text
POST /api/v1/api-keys
GET /api/v1/api-keys
POST /api/v1/api-keys/{id}/revoke
```

Add auth:

- `X-API-Key` header.
- Hashed key lookup.
- Scope validation.

Initial scopes:

```text
customers:read
customers:write
sales:write
wallets:read
redemptions:write
reports:read
admin
```

### Frontend tasks

- Add Integrations page.
- List API keys.
- Create API key modal.
- Copy once warning.
- Revoke key action.

### Acceptance criteria

- Merchant can create an API key.
- Raw key is shown only once.
- Stored key is hashed.
- API key can call `POST /sales` with `sales:write`.

## Priority 4 - Redemption intent / QR flow

### Why

Direct redemptions are fine for backend tests, but customer UI needs QR/code intent so POS can confirm redemption safely.

### Backend tasks

Add model:

```text
RedemptionIntent
  id
  organization_id
  branch_id nullable
  customer_id
  wallet_id
  amount
  code_hash
  display_code_last4
  status
  expires_at
  confirmed_at
  cancelled_at
  created_at
  updated_at
```

Statuses:

```text
PENDING
CONFIRMED
CANCELLED
EXPIRED
FAILED
```

Endpoints:

```text
POST /api/v1/customer/redemption-intents
GET /api/v1/customer/redemption-intents/{id}
POST /api/v1/merchant/redemption-intents/{code}/confirm
POST /api/v1/customer/redemption-intents/{id}/cancel
```

### Frontend tasks

- Customer Redeem page creates a real code.
- Merchant Redemption page confirms a code.
- Show TTL/expiry.

### Acceptance criteria

- Code expires.
- Code cannot be reused.
- Insufficient balance fails before intent creation.
- Confirmation creates `REDEEMED` ledger movement.

## Priority 5 - Demo hardening and public polish

### Backend tasks

- Add `scripts/reset_demo.py` or make seed fully idempotent for repeated demos.
- Add README demo path.
- Add health check for DB connectivity.

### Frontend tasks

- Add explicit empty/loading/error states.
- Add API status banner.
- Add backend unavailable instructions.
- Improve mobile layout for customer portal.

### Acceptance criteria

- A public reviewer can run the demo from README without guessing.
- UI makes it clear when it is using live API vs fallback demo.
- POS simulator produces a visible wallet balance change after refresh.

## Recommended next sprint order

1. Merchant login UI + token storage.
2. Backend route protection for merchant endpoints.
3. Idempotency model/service for `POST /sales`.
4. API keys CRUD.
5. Redemption intent model and QR/code UI.

## Notes for future AI agents

- Do not implement ERC20 yet.
- Do not replace the ledger with blockchain logic.
- Preserve the demo fallback in frontend until backend auth is stable.
- Keep `/portal` customer UX wallet-first.
- Keep `/app` merchant UX operational and table/KPI focused.
