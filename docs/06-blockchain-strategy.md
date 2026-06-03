# Estrategia blockchain

Open Cashback no depende de blockchain en tiempo real para el MVP.

Estrategia:

1. Ledger interno PostgreSQL.
2. Hash y `previous_hash` por movimiento.
3. Batch hash de movimientos.
4. Anchoring en smart contract EVM.
5. Tokenizacion futura solo despues de validacion legal y operativa.

Contrato inicial: `OpenCashbackLedger`, que registra `batchHash`, evita duplicados y emite `BatchAnchored`. No maneja fondos ni tokens.
