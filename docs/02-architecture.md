# Arquitectura

Arquitectura modular API-first:

- `api/v1`: rutas REST.
- `models`: entidades SQLAlchemy.
- `schemas`: contratos Pydantic.
- `services`: reglas de negocio.
- `core`: configuracion, base de datos, seguridad, permisos y logging.

PostgreSQL es la fuente de verdad. Blockchain queda desacoplado mediante `BlockchainService` y registros `BlockchainTransaction`.

Toda entidad operativa relevante incluye `organization_id` para multi-tenancy.
