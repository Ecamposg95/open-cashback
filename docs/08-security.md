# Seguridad

Controles iniciales:

- JWT para usuarios.
- API keys hasheadas en roadmap cercano.
- Multi-tenancy por `organization_id`.
- No consultar ni mutar datos de otra organizacion.
- Ledger no destructivo.
- Hashes de integridad en transacciones.

Pendientes: middleware de usuario actual, RBAC, scopes de API key, rate limiting, auditoria de cambios manuales e idempotency store.
