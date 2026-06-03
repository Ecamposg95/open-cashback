# Backend MVP Gap Analysis

## Current backend state

The backend already supports a partial core flow:

- Create organization.
- Create branch.
- Create customer.
- Auto-create wallet.
- Register sale.
- Calculate global cashback.
- Create `EARNED` ledger transaction.
- Redeem balance directly.
- Create `REDEEMED` ledger transaction.
- Cancel sale and create `REVERSED` ledger transaction.
- Basic reports.
- Simulated blockchain anchor.

## Critical gaps before production MVP

### Auth and tenant isolation

Current risk:

- `/auth/me` is placeholder.
- Operational routes are open.
- `organization_id` comes from query/body instead of authenticated claims.

Needed:

- `current_user` dependency.
- JWT subject type: merchant user, customer user, api client.
- RBAC policies.
- Tenant derived from token/API key.
- Bootstrap admin command.

### Idempotency

Current risk:

- Sales are idempotent only by `organization_id + external_sale_id`.
- Redemptions/cancellations/refunds are not idempotent.

Needed model:

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
```

### API keys

Current state:

- `ApiKey` model exists.
- No router/service/header auth.

Needed:

- Hashed key storage.
- Prefix/last4 visible metadata.
- Scopes.
- Revocation.
- Expiration.
- `last_used_at`.
- API request logs.

### QR redemption lifecycle

Current state:

- Redemptions are direct and immediate.

Needed:

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
  confirmed_at
  cancelled_at
  created_at
```

Flow:

1. Customer creates redemption intent.
2. Backend validates and optionally locks balance.
3. Customer receives short-lived QR/code.
4. Merchant validates code.
5. Merchant confirms redemption.
6. Ledger creates `REDEEMED`.
7. Intent cannot be reused.

### Reports

Current state:

- Summary endpoints exist.

Needed:

- Date filters.
- Branch filters.
- Paginated ledger.
- Liability by branch.
- Issued/redeemed/reversed/expired breakdown.
- Ledger-wallet reconciliation.

### Migration strategy

Current state:

- Initial migration uses `Base.metadata.create_all`.

Needed:

- Future migrations should be explicit.
- Add indexes for tenant/report queries.
- Add unique constraints for idempotency keys and QR token hashes.

## Backend sprint order

1. Auth/me + RBAC + tenant isolation.
2. Idempotency store for POS flows.
3. API keys and scopes.
4. QR redemption intents.
5. Cashback rules engine.
6. Reports and ledger pagination.
7. Blockchain batch anchoring.
8. Migration hardening and concurrency tests.
