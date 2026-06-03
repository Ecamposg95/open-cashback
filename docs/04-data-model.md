# Modelo de datos

Entidades iniciales:

- User
- Organization
- Branch
- Customer
- Wallet
- Sale
- SaleItem
- CashbackRule
- CashbackTransaction
- Redemption
- Campaign
- ApiKey
- BlockchainTransaction

Todas usan UUID textual como primary key inicial. Dinero usa `Decimal` y `Numeric(18,2)`. El ledger se reconstruye desde `CashbackTransaction`.
