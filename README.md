<div align="center">

# Open Cashback
### Cashback · Loyalty · Rewards · Wallet · Auditable Ledger · Web3-ready

**Infraestructura API-first para convertir ventas reales de POS, ERP y e-commerce en recompensas programables, wallets de cliente y un ledger auditable preparado para blockchain anchoring.**

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](#)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)](#)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Ledger-336791?logo=postgresql)](#)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00)](#)
[![Alembic](https://img.shields.io/badge/Alembic-Migrations-6B7280)](#)
[![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react)](#)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6?logo=typescript)](#)
[![Solidity](https://img.shields.io/badge/Solidity-Smart%20Contracts-363636?logo=solidity)](#)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker)](#)
[![Status](https://img.shields.io/badge/Status-MVP%20Core%20Ledger-orange)](#)

</div>

---

## Vision

Open Cashback no es una simple app de puntos. Es una plataforma modular de **cashback, loyalty, rewards, wallet y ledger auditable** para comercios fisicos, cadenas, franquicias, distribuidores, restaurantes, e-commerce y plataformas POS/ERP.

El proyecto arranca con una fuente de verdad solida en PostgreSQL y queda preparado para evolucionar hacia **blockchain anchoring**, smart contracts y una futura red abierta de recompensas tokenizadas.

> Primero ledger interno confiable. Despues hashes. Despues anchoring. Finalmente tokenizacion, solo cuando tenga sentido legal, fiscal y operativo.

## Problema

Los comercios suelen operar promociones sin trazabilidad real:

- No conocen con precision su pasivo por recompensas.
- No conectan loyalty con ventas reales.
- No tienen historial auditable de cashback emitido y redimido.
- No pueden integrarse facilmente con POS, ERP o e-commerce.
- No cuentan con una base preparada para modelos Web3 sin afectar la velocidad de caja.

## Solucion

Open Cashback permite que una compra elegible:

1. Se registre desde POS, ERP o e-commerce.
2. Calcule cashback con reglas configurables.
3. Acredite saldo en una wallet de cliente.
4. Genere un movimiento inmutable en ledger.
5. Permita redencion futura.
6. Revierta cashback si una venta se cancela.
7. Prepare hashes para auditoria y anchoring blockchain.

## Arquitectura

```text
Client Apps
  Admin Dashboard · POS Integration · Customer Portal · E-commerce Plugin

API Layer
  FastAPI REST API · API Keys · Webhooks

Application Services
  CashbackEngine · LedgerService · WalletService · SaleService · RedemptionService

Domain Layer
  Organization · Branch · Customer · Wallet · Sale · CashbackTransaction · Redemption

Infrastructure
  PostgreSQL · Alembic · Docker · Solidity · Hardhat · EVM Anchoring
```

## Stack

| Capa | Tecnologia |
| --- | --- |
| Backend | Python, FastAPI, SQLAlchemy, Alembic, Pydantic |
| Database | PostgreSQL, `Numeric(18,2)`, UUIDs |
| Auth | JWT, roles y API keys en roadmap |
| Frontend | React, Vite, TypeScript, Tailwind CSS |
| Web3 | Solidity, Hardhat, Web3-ready anchoring |
| Testing | Pytest |
| Infra local | Docker Compose |

## Estructura

```text
open-cashback/
├── backend/
│   ├── app/
│   │   ├── api/v1/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── tests/
│   └── alembic/
├── frontend/
├── contracts/
│   └── contracts/OpenCashbackLedger.sol
├── docs/
├── context/
├── docker-compose.yml
└── README.md
```

## MVP Core Ledger

El primer entregable incluye:

- Organizaciones multi-tenant.
- Sucursales.
- Clientes.
- Wallet automatica por cliente.
- Registro de ventas.
- Cashback global por organizacion.
- Ledger interno con `hash` y `previous_hash`.
- Redenciones.
- Reversos por cancelacion de venta.
- Reportes basicos.
- Placeholder de blockchain anchoring.
- Contrato Solidity minimo para registrar batch hashes.

## Modelos principales

- `User`
- `Organization`
- `Branch`
- `Customer`
- `Wallet`
- `Sale`
- `SaleItem`
- `CashbackRule`
- `CashbackTransaction`
- `Redemption`
- `Campaign`
- `ApiKey`
- `BlockchainTransaction`

## Flujo MVP

```text
Crear organizacion
  -> Crear sucursal
  -> Crear cliente
  -> Crear wallet automatica
  -> Registrar venta
  -> Calcular cashback
  -> Crear movimiento EARNED
  -> Actualizar wallet
  -> Redimir saldo
  -> Crear movimiento REDEEMED
  -> Cancelar venta
  -> Crear movimiento REVERSED
```

## Setup local

```bash
cp .env.example .env
docker compose up -d db

cd backend
python -m pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

API:

```text
http://localhost:8000
```

OpenAPI:

```text
http://localhost:8000/docs
```

## Comandos utiles

Backend:

```bash
cd backend
python -m pytest app/tests -q
```

Contracts:

```bash
cd contracts
npm install
npm run compile
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

## API inicial

| Recurso | Endpoints |
| --- | --- |
| Auth | `POST /api/v1/auth/login`, `GET /api/v1/auth/me` |
| Organizations | `POST /api/v1/organizations`, `GET /api/v1/organizations` |
| Branches | `POST /api/v1/branches`, `GET /api/v1/branches` |
| Customers | `POST /api/v1/customers`, `GET /api/v1/customers`, `GET /api/v1/customers/{id}/wallet` |
| Sales | `POST /api/v1/sales`, `GET /api/v1/sales/{id}`, `POST /api/v1/sales/{id}/cancel` |
| Wallets | `GET /api/v1/wallets/{id}`, `GET /api/v1/wallets/customer/{customer_id}` |
| Cashback | `POST /api/v1/cashback/calculate`, `GET /api/v1/cashback/transactions` |
| Redemptions | `POST /api/v1/redemptions`, `GET /api/v1/redemptions/{id}` |
| Reports | `GET /api/v1/reports/summary`, `GET /api/v1/reports/outstanding-liability` |
| Blockchain | `POST /api/v1/blockchain/anchor`, `GET /api/v1/blockchain/transactions/{id}` |

## Web3 Strategy

Open Cashback mantiene enfoque Web3 sin hacer lenta la operacion del POS.

- No registra cada venta on-chain.
- No implementa ERC20 en el MVP.
- No maneja fondos en smart contracts.
- Si genera hashes de integridad por movimiento.
- Si prepara anchoring por batches.
- Si incluye contrato `OpenCashbackLedger` para registrar `batchHash` y evitar duplicados.

## Documentacion

- [Master Brief](docs/00-master-brief.md)
- [Product Vision](docs/01-product-vision.md)
- [Architecture](docs/02-architecture.md)
- [API](docs/03-api.md)
- [Data Model](docs/04-data-model.md)
- [Business Rules](docs/05-business-rules.md)
- [Blockchain Strategy](docs/06-blockchain-strategy.md)
- [Roadmap](docs/07-roadmap.md)
- [Security](docs/08-security.md)
- [Token Economy](docs/09-token-economy.md)
- [Backlog](docs/10-backlog.md)
- [MVP Execution Plan](docs/11-mvp-execution-plan.md)
- [Collaborative Agent Context](context/agents/README.md)
- [UI MVP Spec](context/product/ui-mvp-spec.md)
- [Backend MVP Gap Analysis](context/technical/backend-mvp-gap-analysis.md)

## Roadmap

1. Auth y permisos multi-tenant completos.
2. API keys para integraciones POS/ERP/e-commerce.
3. Persistencia de `Idempotency-Key`.
4. Reglas avanzadas de cashback y campaign engine.
5. Expiracion de recompensas y limites de redencion.
6. Dashboard administrativo.
7. Batch anchoring real en Ganache y testnets EVM.
8. Webhooks e integraciones externas.
9. Explorador interno de ledger y hashes.
10. Token economy futura, sin implementacion prematura.

## Estado del proyecto

```text
MVP Core Ledger: en desarrollo inicial.
Backend core: scaffold funcional.
Frontend: customer portal y merchant LaaS shell iniciados.
Blockchain: placeholder y contrato minimo.
Produccion: no listo todavia.
```

---

<div align="center">

**Open Cashback turns every transaction into a programmable reward.**

</div>
