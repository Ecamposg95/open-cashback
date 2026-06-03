# Open Cashback

Open Cashback es una infraestructura API-first de cashback, loyalty, rewards, wallet y ledger auditable para POS, ERP, e-commerce y redes comerciales.

El MVP prioriza un ledger interno robusto en PostgreSQL y prepara una capa Web3 para anchoring de hashes. No implementa token ERC20 ni depende de blockchain en tiempo real.

## Problema

Los comercios emiten promociones sin trazabilidad, no conocen su pasivo por recompensas y carecen de una capa simple para conectar ventas reales con lealtad medible.

## Solucion

Cada compra elegible puede generar cashback, acreditarse en una wallet de cliente, registrarse en un ledger inmutable por reversos y auditarse con hashes internos preparados para blockchain anchoring.

## Stack

- Backend: Python, FastAPI, SQLAlchemy, Alembic, PostgreSQL, Pydantic, JWT, Pytest.
- Frontend: React, Vite, TypeScript, Tailwind CSS.
- Web3: Solidity, Hardhat, Web3-ready anchoring placeholder.
- Infraestructura local: Docker Compose.

## Setup local

```bash
cp .env.example .env
docker compose up -d db
cd backend
python -m pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

API: http://localhost:8000
OpenAPI: http://localhost:8000/docs

## Comandos utiles

```bash
cd backend
python -m pytest app/tests -q

cd ../contracts
npm install
npm run compile
```

## Estado

Primera iteracion del MVP Core Ledger: estructura modular, modelos principales, services de cashback/wallet/ledger/sales/redemptions, endpoints v1, migracion inicial, contrato de anchoring y documentacion base.

## Roadmap

1. Auth y permisos multi-tenant completos.
2. Idempotency-Key persistente.
3. API keys para POS/ERP.
4. Campaign engine avanzado.
5. Batch anchoring real en EVM testnet.
6. Dashboard administrativo.
7. Token economy solo despues de validacion legal, fiscal y operativa.
