# API v1

Endpoints iniciales:

- `POST /api/v1/auth/login`
- `GET /api/v1/auth/me`
- `POST /api/v1/organizations`
- `GET /api/v1/organizations`
- `GET /api/v1/organizations/{organization_id}`
- `PATCH /api/v1/organizations/{organization_id}`
- `POST /api/v1/branches`
- `GET /api/v1/branches?organization_id=`
- `GET /api/v1/branches/{branch_id}?organization_id=`
- `POST /api/v1/customers`
- `GET /api/v1/customers?organization_id=`
- `GET /api/v1/customers/{customer_id}?organization_id=`
- `PATCH /api/v1/customers/{customer_id}?organization_id=`
- `GET /api/v1/customers/{customer_id}/wallet?organization_id=`
- `GET /api/v1/customers/{customer_id}/transactions?organization_id=`
- `POST /api/v1/sales`
- `GET /api/v1/sales/{sale_id}?organization_id=`
- `POST /api/v1/sales/{sale_id}/cancel?organization_id=`
- `POST /api/v1/sales/{sale_id}/refund?organization_id=`
- `GET /api/v1/wallets/{wallet_id}?organization_id=`
- `GET /api/v1/wallets/customer/{customer_id}?organization_id=`
- `POST /api/v1/cashback/calculate`
- `GET /api/v1/cashback/transactions?organization_id=`
- `GET /api/v1/cashback/transactions/{transaction_id}?organization_id=`
- `POST /api/v1/redemptions`
- `GET /api/v1/redemptions/{redemption_id}?organization_id=`
- `POST /api/v1/redemptions/{redemption_id}/cancel?organization_id=`
- `GET /api/v1/reports/summary?organization_id=`
- `GET /api/v1/reports/outstanding-liability?organization_id=`
- `GET /api/v1/reports/cashback-issued?organization_id=`
- `GET /api/v1/reports/cashback-redeemed?organization_id=`
- `POST /api/v1/blockchain/anchor`
- `GET /api/v1/blockchain/transactions/{tx_id}?organization_id=`
