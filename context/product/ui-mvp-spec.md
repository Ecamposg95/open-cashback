# UI MVP Specification

## Product shape

Open Cashback needs an operational UI, not a marketing landing page.

The app should expose three route groups:

```text
/portal/*      Customer Portal demo routes
/app/*         Merchant LaaS Dashboard routes
/admin/*       Internal platform routes
```

Admin can be minimal for MVP. Customer and merchant are required.

## Customer Portal

### Purpose

Help the end customer understand and use their rewards.

### Routes

```text
/portal
/portal/:organizationId/customers/:customerId
/portal/:organizationId/customers/:customerId/transactions
/portal/:organizationId/customers/:customerId/redeem
/portal/:organizationId/customers/:customerId/profile
/portal/:organizationId/customers/:customerId/web3
```

### Dashboard

Primary content:

- Available balance.
- Pending balance.
- Expiring soon amount.
- Lifetime earned.
- Lifetime redeemed.
- Recent transactions.
- Active benefits/campaigns.
- Primary action: redeem.

Required components:

- BalanceSummary.
- RewardStatusStrip.
- RecentTransactionsList.
- BenefitPreviewList.
- RedeemActionButton.

### Wallet

Primary content:

- Wallet status.
- Available, pending, locked, redeemed, expired balances.
- Wallet ID.
- Merchant/organization context.
- Currency.

Future content:

- Reward units.
- Crypto/reward token status.
- External wallet connection.

### History

Primary content:

- Timeline/table of ledger movements.
- Filters by movement type.
- Search by sale reference.
- Movement detail drawer.

Movement labels:

- EARNED: cashback earned.
- REDEEMED: cashback used.
- REVERSED: sale/refund reversal.
- BONUS: promotional reward.
- EXPIRED: expired balance.
- LOCKED/UNLOCKED: balance hold state.

### Redeem

MVP behavior:

- Customer enters amount.
- System validates balance.
- UI creates redemption intent.
- UI displays QR-like token or redemption code.
- Code expires.

Backend needed:

- RedemptionIntent or RedemptionCode model.
- Expiration timestamp.
- One-time use status.
- Optional PIN.

### Web3

MVP behavior:

- Explain audit readiness without promising token value.
- Show internal hash status.
- Show latest ledger hash.
- Show anchored/not anchored state.

Copy direction:

```text
Your rewards are tracked in an auditable internal ledger.
Blockchain anchoring can later verify batches of movements without slowing down checkout.
```

## Merchant Dashboard

### Purpose

Let the business operate Open Cashback as Loyalty as a Service.

### Routes

```text
/app
/app/:organizationId/dashboard
/app/:organizationId/customers
/app/:organizationId/customers/:customerId
/app/:organizationId/sales/new
/app/:organizationId/transactions
/app/:organizationId/redemptions
/app/:organizationId/branches
/app/:organizationId/campaigns
/app/:organizationId/reports
/app/:organizationId/integrations
/app/:organizationId/settings
/app/:organizationId/blockchain
```

### Dashboard

Primary KPIs:

- Cashback issued.
- Cashback redeemed.
- Outstanding liability.
- Active customers.
- Sales registered.
- Redemption rate.
- Average ticket.

Components:

- KpiGrid.
- LiabilityTrend.
- RecentSalesTable.
- RecentLedgerMovements.
- IntegrationHealthCard.

### Customers

Table columns:

- Name.
- Phone/email.
- Wallet balance.
- Lifetime earned.
- Lifetime redeemed.
- Last activity.
- Status.

Actions:

- View customer.
- View wallet.
- Manual adjustment, later with approval.
- Lock wallet.

### Sales

Table columns:

- External sale ID.
- Customer.
- Branch.
- Eligible amount.
- Cashback generated.
- Status.
- Date.

Actions:

- View sale.
- Cancel sale.
- Refund sale.

### Ledger

Core audit view:

- Transaction ID.
- Type.
- Status.
- Amount.
- Customer.
- Wallet.
- Sale/redemption reference.
- Hash.
- Previous hash.
- Created at.

Actions:

- Copy hash.
- View movement detail.
- Filter by wallet/customer/type/date.

### Campaigns

MVP minimal:

- Global cashback rate editor.
- List campaigns placeholder.
- Future rule builder placeholder.

### Integrations

Required for LaaS positioning:

- API keys list.
- Create/revoke API key.
- Scopes.
- Webhook URL list.
- API usage logs.
- POS integration docs link.

### Blockchain

Merchant sees:

- Anchoring mode: simulated/off/testnet.
- Latest batch hash.
- Anchored batches count.
- Pending batches count.
- Contract address if configured.

## Visual direction

Customer:

- Mobile-first.
- Wallet-like.
- Large balance.
- Clear redemption action.
- Simple timeline.

Merchant:

- Dense SaaS/ERP style.
- Sidebar navigation.
- KPI cards.
- Tables with filters.
- Neutral professional palette.

Do not build a landing page as the primary screen. Build the working app experience.


## Demo-first quick wins

- Build a POS simulator inside `/app/:organizationId/sales/new`.
- Use `/reports/summary` and `/cashback/transactions` for dashboard KPIs and ledger preview.
- Use hash chips instead of full hashes in customer-facing views.
- Use demo selectors until auth is complete, clearly scoped as development/demo mode.
- Seed one organization, two branches, five customers and mixed ledger movements.

## Current backend gaps affecting UI

- No `GET /sales` list endpoint yet; sales table should start from newly created sale responses or wait for backend Sprint 3.
- No `GET /redemptions` list endpoint yet; redemptions list can initially derive from ledger transactions of type `REDEEMED`.
- Campaigns exist as CRUD but do not affect cashback calculation yet.
- Auth `/me` is placeholder; frontend should start with demo context selectors.
