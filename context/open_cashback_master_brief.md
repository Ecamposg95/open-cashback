# Open Cashback — Master Brief para IA de Desarrollo

**Repositorio:** `git@github.com:Ecamposg95/open-cashback.git`  
**Nombre del proyecto:** Open Cashback  
**Tipo de proyecto:** Plataforma de cashback, loyalty, rewards, wallet y blockchain ledger  
**Estado:** Etapa conceptual / arquitectura inicial / preparación de MVP  
**Idioma principal de documentación:** Español  
**Audiencia de este documento:** IAs de desarrollo, agentes de código, arquitectos de software, product managers técnicos y desarrolladores full stack.  

---

# 0. Instrucciones para la IA de desarrollo

Este documento debe ser tratado como el **contexto maestro del proyecto Open Cashback**.

La IA de desarrollo que reciba este archivo debe:

1. Entender la visión completa del producto.
2. Respetar el enfoque modular.
3. Priorizar un MVP funcional antes que una implementación blockchain compleja.
4. Diseñar primero una arquitectura robusta de ledger interno.
5. Preparar la base para una futura capa blockchain.
6. Mantener compatibilidad con POS, ERP, e-commerce y APIs externas.
7. Considerar que Open Cashback forma parte de una visión más amplia de Atlas Tech.
8. Evitar sobreingeniería innecesaria en la primera etapa.
9. Documentar cada decisión técnica importante.
10. Mantener el proyecto limpio, escalable y fácil de auditar.

---

# 1. Resumen ejecutivo

**Open Cashback** es una plataforma abierta de cashback, lealtad y recompensas programables para negocios físicos y digitales.

El proyecto busca crear una infraestructura modular que permita a comercios, cadenas, franquicias, distribuidores, restaurantes, tiendas retail, marketplaces, sistemas POS, ERPs y plataformas e-commerce ofrecer recompensas digitales a sus clientes.

La plataforma debe permitir que cada compra genere valor de regreso para el cliente mediante cashback, puntos, saldo de recompensa o tokens internos. A su vez, el negocio debe obtener datos accionables sobre recompra, frecuencia, ticket promedio, campañas, redención y comportamiento comercial.

La visión a largo plazo es construir una red abierta de recompensas donde distintos comercios puedan integrarse, emitir beneficios, auditar saldos, crear campañas y eventualmente operar sobre una capa blockchain.

---

# 2. Repositorio

```bash
git@github.com:Ecamposg95/open-cashback.git
```

Nombre sugerido local:

```bash
open-cashback
```

Primer setup sugerido:

```bash
git clone git@github.com:Ecamposg95/open-cashback.git
cd open-cashback
```

---

# 3. Naturaleza del proyecto

Open Cashback no debe entenderse solamente como un módulo de descuentos.

Debe entenderse como una infraestructura de:

- Cashback as a Service.
- Loyalty as a Service.
- Rewards Engine.
- Wallet de recompensas.
- Ledger transaccional.
- API de fidelización.
- Motor de campañas.
- Capa de integración POS/ERP/e-commerce.
- Futuro protocolo de recompensas tokenizadas.
- Futuro sistema interoperable entre comercios.

---

# 4. Contexto estratégico

El proyecto surge como evolución de trabajos previos en:

- Atlas POS.
- Atlas ERP.
- DataX POS.
- Sistemas de punto de venta.
- Retail y comercializadoras.
- E-commerce.
- CRM.
- Wallets.
- Blockchain.
- Web3.
- Cashback.
- Programas de lealtad.
- Analítica comercial.
- Venture studio tecnológico.

Open Cashback debe poder integrarse en el futuro con plataformas de Atlas Tech y otros sistemas externos.

---

# 5. Relación con Atlas Tech

Open Cashback puede funcionar como una vertical, producto o módulo estratégico dentro del ecosistema Atlas Tech.

Relación potencial:

- **Atlas POS:** módulo de recompensas para ventas físicas.
- **Atlas ERP:** capa de fidelización conectada a ventas, clientes y finanzas.
- **Atlas Kapital:** posible conexión futura con tokenización, financiamiento e incentivos.
- **Atlas Retail Intelligence:** analítica de comportamiento, recompra y clientes.
- **Atlas Venture Lab:** producto con potencial de spin-off.
- **Atlas Web3:** base para smart contracts y token economy.
- **Atlas CRM:** campañas basadas en datos de clientes.

---

# 6. Problema

Los negocios físicos y digitales enfrentan problemas frecuentes:

1. Los clientes compran una vez y no regresan.
2. Las promociones se aplican sin datos.
3. Los descuentos reducen margen sin construir lealtad.
4. Los POS solo registran ventas, pero no fortalecen la relación con el cliente.
5. Los programas de puntos suelen ser manuales o confusos.
6. Las pequeñas empresas no tienen infraestructura avanzada de fidelización.
7. Las campañas no están conectadas con ventas reales.
8. No existe trazabilidad clara de recompensas emitidas y redimidas.
9. Los negocios no conocen con precisión su pasivo por recompensas.
10. Las franquicias no tienen visibilidad centralizada por sucursal.
11. Los sistemas de lealtad cerrados son difíciles de integrar.
12. No hay interoperabilidad entre comercios.
13. Los clientes no siempre entienden cuánto ganaron ni cómo redimirlo.
14. El negocio no mide correctamente recurrencia, ticket promedio ni lifetime value.

---

# 7. Propuesta de valor

Open Cashback permite convertir una compra en una relación continua entre cliente y negocio.

La plataforma permite que:

- El cliente compre.
- El sistema calcule una recompensa.
- El cliente acumule cashback en una wallet.
- El cliente regrese para redimir.
- El negocio mida la recurrencia.
- El comercio cree campañas.
- La administración audite saldos.
- El sistema evolucione hacia trazabilidad blockchain.

Declaración central:

> Open Cashback convierte cada transacción en una recompensa programable.

Declaración comercial:

> Open Cashback ayuda a los negocios a vender más, retener clientes y construir lealtad usando cashback, datos y tecnología.

Declaración técnica:

> Open Cashback es una infraestructura API-first para administrar wallets, reglas de cashback, transacciones de recompensa, redenciones, campañas y auditoría de saldos.

---

# 8. Usuarios objetivo

## 8.1 Comercios físicos

Ejemplos:

- Tiendas retail.
- Papelerías.
- Distribuidoras.
- Tiendas de conveniencia.
- Ferreterías.
- Boutiques.
- Farmacias.
- Restaurantes.
- Cafeterías.
- Gimnasios.
- Clínicas.
- Talleres.

## 8.2 Cadenas y franquicias

Necesitan:

- Control centralizado.
- Saldos por sucursal.
- Campañas globales.
- Campañas locales.
- Reportes por unidad de negocio.
- Reglas homogéneas.
- Auditoría de recompensas.

## 8.3 Mayoristas y distribuidores

Necesitan:

- Recompensar volumen.
- Premiar clientes recurrentes.
- Incentivar compras por caja.
- Activar cuentas inactivas.
- Segmentar clientes por frecuencia.

## 8.4 E-commerce

Necesitan:

- Cashback en compras online.
- Integración con WooCommerce, Shopify o plataformas propias.
- Campañas digitales.
- Wallet de cliente.
- Redención en checkout.

## 8.5 Plataformas POS/ERP

Necesitan:

- API externa de loyalty.
- Motor de recompensas configurable.
- Wallet por cliente.
- Redención en ticket.
- Historial transaccional.
- Webhooks.

---

# 9. Beneficiarios

## Para negocios

- Mayor recompra.
- Mayor retención.
- Mejor ticket promedio.
- Incentivos configurables.
- Datos comerciales.
- Diferenciación.
- Mejor experiencia de cliente.
- Control de pasivo por recompensas.
- Integración con ventas reales.
- Posibilidad de campañas inteligentes.

## Para clientes

- Reciben valor de regreso.
- Entienden sus recompensas.
- Consultan saldo.
- Redimen en compras futuras.
- Participan en promociones.
- Reciben beneficios personalizados.
- Pueden usar QR o wallet digital.

## Para Atlas Tech

- Producto SaaS escalable.
- Capa de valor sobre POS/ERP.
- Posible spin-off.
- Producto Web3 realista.
- Módulo vendible a comercios.
- Infraestructura para futuras redes de loyalty.

---

# 10. Principio de producto

Open Cashback debe ser:

- Simple para el cliente.
- Rápido para el punto de venta.
- Auditable para administración.
- Modular para desarrollo.
- Escalable para múltiples comercios.
- Seguro contra fraude.
- Compatible con operación offline parcial.
- Preparado para blockchain, pero no dependiente de blockchain desde el día uno.

Principio importante:

> La venta en POS nunca debe volverse lenta por depender de una transacción blockchain en tiempo real.

---

# 11. Estrategia técnica general

La implementación recomendada es híbrida y progresiva.

## Fase técnica 1: Ledger interno

PostgreSQL será la fuente de verdad inicial.

Se deben registrar:

- Ventas.
- Recompensas ganadas.
- Redenciones.
- Expiraciones.
- Reversos.
- Ajustes manuales.
- Bonos.
- Referidos.

## Fase técnica 2: Hash de integridad

Cada movimiento relevante debe poder generar un hash.

Objetivo:

- Trazabilidad.
- Auditoría.
- Detección de manipulación.
- Preparación para blockchain anchoring.

## Fase técnica 3: Blockchain anchoring

En vez de registrar cada venta on-chain, se pueden agrupar movimientos y anclar un hash por lote.

Ejemplo:

```text
1000 movimientos de cashback → hash batch → registro en blockchain
```

## Fase técnica 4: Smart contracts

Una vez validado el modelo de negocio, algunos procesos pueden migrarse a smart contracts:

- Emisión de reward tokens.
- Redención.
- Eventos de recompensa.
- Auditoría de campañas.
- Control de supply.

## Fase técnica 5: Tokenización

La tokenización debe considerarse cuidadosamente por implicaciones fiscales, financieras y regulatorias.

En primera etapa se recomienda tratarlo como:

- Cashback interno.
- Saldo de recompensa.
- Puntos con equivalencia.
- Reward balance.

No como activo financiero abierto.

---

# 12. Hipótesis económica inicial

Hipótesis simple:

```text
1 unidad de cashback = $1 MXN de valor interno de redención
```

Ejemplo:

```text
Compra: $1,000 MXN
Cashback: 1%
Recompensa: $10 MXN
Saldo wallet: +10 unidades
Valor interno: $10 MXN
```

Esta equivalencia facilita la adopción por parte de clientes y comercios.

Sin embargo, el sistema debe permitir que en el futuro existan otros modelos:

- 1 punto = $0.10 MXN
- 100 puntos = $1 MXN
- Cashback porcentual
- Cashback fijo
- Tokens promocionales
- Bonos por campaña
- Rewards no monetarios

---

# 13. Conceptos clave

## Cashback

Recompensa calculada normalmente como porcentaje del monto de compra.

## Wallet

Cuenta interna donde se acumula el saldo del cliente.

## Ledger

Registro histórico inmutable o semi-inmutable de todos los movimientos de recompensa.

## Redemption

Uso del saldo de recompensa para descontar parte o la totalidad de una compra futura.

## Campaign

Conjunto de reglas temporales o segmentadas para modificar la recompensa.

## Reward Rule

Regla que define cómo se gana, limita o redime cashback.

## Merchant

Comercio participante.

## Organization

Entidad dueña de uno o varios comercios, sucursales o marcas.

## Branch

Sucursal donde ocurren ventas y redenciones.

## Token

Unidad digital programable futura que puede representar una recompensa.

---

# 14. MVP funcional

El MVP debe resolver un flujo completo:

1. Crear organización.
2. Crear sucursal.
3. Crear usuario administrador.
4. Crear cliente.
5. Registrar venta.
6. Calcular cashback.
7. Acreditar cashback en wallet.
8. Consultar saldo.
9. Redimir saldo.
10. Ver historial.
11. Ver reporte básico.

## MVP mínimo

- Backend API.
- Base de datos.
- Auth simple.
- CRUD de organizaciones.
- CRUD de sucursales.
- CRUD de clientes.
- Registro de ventas.
- Regla global de cashback.
- Wallet por cliente.
- Ledger de movimientos.
- Redención.
- Reportes básicos.
- Documentación OpenAPI.

## MVP no debe incluir inicialmente

- Token real en mainnet.
- Marketplace complejo.
- App móvil nativa.
- KYC complejo.
- Multi-chain.
- DeFi.
- Exchange.
- Custodia financiera.
- Stablecoin real.
- Integraciones fiscales avanzadas.

---

# 15. Casos de uso iniciales

## Caso 1: Retail básico

Una tienda quiere dar 1% de cashback en cada compra.

Flujo:

1. Cliente compra $500.
2. Sistema calcula $5 de cashback.
3. El saldo se agrega a su wallet.
4. Cliente regresa y redime esos $5 en otra compra.

## Caso 2: Mayorista

Una distribuidora quiere recompensar compras por volumen.

Regla:

```text
Si compra más de $5,000 → 2% cashback
Si compra más de $10,000 → 3% cashback
```

## Caso 3: Restaurante

Un restaurante quiere aumentar ventas de lunes a jueves.

Regla:

```text
Lunes a jueves: 5% cashback
Viernes a domingo: 1% cashback
```

## Caso 4: Franquicia

Una cadena quiere controlar recompensas por sucursal.

Necesita ver:

- Cashback emitido por sucursal.
- Cashback redimido por sucursal.
- Saldo pendiente total.
- Campañas activas.
- Clientes frecuentes.

## Caso 5: E-commerce

Una tienda online quiere dar cashback en compras pagadas.

Integración:

- Webhook de orden pagada.
- Cálculo de cashback.
- Wallet de cliente.
- Código de redención en checkout.

## Caso 6: POS externo

Un POS externo quiere usar Open Cashback como módulo de lealtad.

Requiere:

- API key.
- Endpoint para registrar venta.
- Endpoint para consultar saldo.
- Endpoint para redimir.
- Endpoint para cancelar/revertir.

---

# 16. Modelo de negocio posible

## SaaS mensual

Cobro mensual por comercio o por sucursal.

Ejemplo:

- Starter: una sucursal.
- Business: varias sucursales.
- Enterprise: franquicias y cadenas.

## Comisión por transacción

Pequeño fee por cashback emitido o redimido.

## White label

Implementación personalizada para marcas.

## Enterprise license

Licencia privada para grandes cadenas.

## API usage

Cobro por número de llamadas o volumen transaccional.

## Red comercial

Comisión por uso de red compartida de beneficios.

## Módulo premium en Atlas POS

Open Cashback puede venderse como add-on de Atlas POS o Atlas ERP.

---

# 17. Riesgos

## Riesgo financiero

El cashback representa un pasivo para el comercio.

Se debe medir:

- Cashback emitido.
- Cashback redimido.
- Cashback pendiente.
- Cashback expirado.
- Pasivo por sucursal.
- Pasivo por campaña.

## Riesgo fiscal

El tratamiento de recompensas puede variar. Se requiere revisión fiscal si el saldo se maneja como dinero, descuento, monedero electrónico o token.

## Riesgo regulatorio

Si se crea un token transferible con valor fuera del ecosistema, podría acercarse a marcos regulatorios financieros.

## Riesgo de fraude

Posibles abusos:

- Ventas falsas.
- Doble redención.
- Redención después de reembolso.
- Manipulación manual de saldo.
- Referidos falsos.
- Cajeros coludidos.
- Clientes duplicados.

## Riesgo técnico

No se debe depender de blockchain en tiempo real para cerrar ventas.

## Riesgo de UX

Si el cliente no entiende el beneficio, no lo usará.

---

# 18. Reglas de negocio iniciales

## Regla base

Cada organización puede configurar un porcentaje global de cashback.

Ejemplo:

```text
global_cashback_rate = 0.01
```

## Monto elegible

El cashback debe calcularse sobre el subtotal elegible, no necesariamente sobre el total.

Se deben considerar exclusiones:

- Envío.
- Impuestos.
- Productos no elegibles.
- Descuentos.
- Propinas.
- Comisiones.
- Pagos con cashback.

## Cashback sobre venta con redención

No se debe generar cashback sobre la parte pagada con cashback, salvo que la organización lo permita explícitamente.

Ejemplo:

```text
Total ticket: $1,000
Redención cashback: $100
Monto pagado real: $900
Cashback calculado sobre: $900
```

## Redondeo

Se debe definir política de redondeo.

Sugerencia:

- Guardar montos en centavos como enteros.
- Evitar floats para dinero.
- Usar Decimal en Python.
- Definir precisión de 2 decimales.

## Devoluciones

Si una venta es cancelada o reembolsada:

- El cashback ganado debe revertirse si no ha sido redimido.
- Si ya fue redimido, se debe generar saldo negativo, bloqueo o ajuste.
- Debe quedar registro en ledger.

## Expiración

Cada recompensa puede tener fecha de expiración.

Ejemplo:

```text
Cashback expira después de 90 días.
```

## Límite de redención

Una organización puede limitar cuánto cashback se puede usar por venta.

Ejemplo:

```text
Máximo 30% del ticket puede pagarse con cashback.
```

## Saldo pendiente

El cashback puede pasar por estado pendiente antes de estar disponible.

Ejemplo:

```text
Disponible después de 24 horas o después de que la venta ya no pueda cancelarse.
```

---

# 19. Estados sugeridos

## Sale status

```text
DRAFT
COMPLETED
CANCELLED
REFUNDED
PARTIALLY_REFUNDED
```

## Cashback transaction type

```text
EARNED
REDEEMED
EXPIRED
ADJUSTED
REVERSED
BONUS
REFERRAL
LOCKED
UNLOCKED
```

## Cashback transaction status

```text
PENDING
AVAILABLE
CANCELLED
EXPIRED
REDEEMED
REVERSED
FAILED
```

## Wallet status

```text
ACTIVE
LOCKED
SUSPENDED
CLOSED
```

## Campaign status

```text
DRAFT
ACTIVE
PAUSED
EXPIRED
CANCELLED
```

## Organization status

```text
ACTIVE
SUSPENDED
CANCELLED
```

---

# 20. Arquitectura recomendada

## Backend

Stack recomendado:

- Python.
- FastAPI.
- PostgreSQL.
- SQLAlchemy.
- Alembic.
- Pydantic.
- JWT.
- Uvicorn.
- Pytest.
- Docker.

## Frontend

Stack recomendado:

- React.
- Vite.
- Tailwind CSS.
- TypeScript.
- Dashboard admin.
- Portal cliente simple.

## Blockchain

Stack recomendado:

- Solidity.
- Hardhat o Foundry.
- Web3.py.
- Ganache para pruebas locales.
- Polygon Amoy, Base Sepolia u otra testnet EVM.

## Infraestructura

- Docker Compose local.
- Railway, Render, VPS o similar para despliegue.
- GitHub Actions para CI.
- Variables de entorno.
- Logs estructurados.

---

# 21. Arquitectura por capas

```text
Client Apps
  ├── Admin Dashboard
  ├── POS Integration
  ├── Customer Portal
  └── E-commerce Plugin

API Layer
  ├── REST API
  ├── Webhooks
  └── API Keys

Application Services
  ├── Customer Service
  ├── Sale Service
  ├── Cashback Engine
  ├── Wallet Service
  ├── Ledger Service
  ├── Campaign Service
  └── Blockchain Service

Domain Layer
  ├── Organization
  ├── Branch
  ├── Customer
  ├── Sale
  ├── Wallet
  ├── CashbackTransaction
  ├── Campaign
  └── RewardRule

Infrastructure Layer
  ├── PostgreSQL
  ├── Redis optional
  ├── Blockchain node/provider
  ├── Email/SMS/WhatsApp optional
  └── External POS/ERP integrations
```

---

# 22. Estructura sugerida del repositorio

```bash
open-cashback/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── auth.py
│   │   │       ├── organizations.py
│   │   │       ├── branches.py
│   │   │       ├── customers.py
│   │   │       ├── sales.py
│   │   │       ├── wallets.py
│   │   │       ├── cashback.py
│   │   │       ├── campaigns.py
│   │   │       ├── redemptions.py
│   │   │       ├── reports.py
│   │   │       └── blockchain.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── database.py
│   │   │   ├── security.py
│   │   │   ├── permissions.py
│   │   │   └── logging.py
│   │   │
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── organization.py
│   │   │   ├── branch.py
│   │   │   ├── customer.py
│   │   │   ├── sale.py
│   │   │   ├── sale_item.py
│   │   │   ├── wallet.py
│   │   │   ├── cashback_rule.py
│   │   │   ├── cashback_transaction.py
│   │   │   ├── campaign.py
│   │   │   ├── redemption.py
│   │   │   ├── api_key.py
│   │   │   └── blockchain_transaction.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── auth.py
│   │   │   ├── organization.py
│   │   │   ├── branch.py
│   │   │   ├── customer.py
│   │   │   ├── sale.py
│   │   │   ├── wallet.py
│   │   │   ├── cashback.py
│   │   │   ├── campaign.py
│   │   │   └── blockchain.py
│   │   │
│   │   ├── services/
│   │   │   ├── auth_service.py
│   │   │   ├── customer_service.py
│   │   │   ├── sale_service.py
│   │   │   ├── cashback_engine.py
│   │   │   ├── wallet_service.py
│   │   │   ├── ledger_service.py
│   │   │   ├── campaign_service.py
│   │   │   ├── redemption_service.py
│   │   │   └── blockchain_service.py
│   │   │
│   │   ├── repositories/
│   │   ├── utils/
│   │   ├── tests/
│   │   └── main.py
│   │
│   ├── alembic/
│   ├── requirements.txt
│   ├── pyproject.toml
│   ├── Dockerfile
│   └── README.md
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── README.md
│
├── contracts/
│   ├── contracts/
│   │   └── OpenCashbackLedger.sol
│   ├── scripts/
│   ├── test/
│   ├── hardhat.config.js
│   └── README.md
│
├── docs/
│   ├── 00-master-brief.md
│   ├── 01-product-vision.md
│   ├── 02-architecture.md
│   ├── 03-api.md
│   ├── 04-data-model.md
│   ├── 05-business-rules.md
│   ├── 06-blockchain-strategy.md
│   ├── 07-roadmap.md
│   ├── 08-security.md
│   ├── 09-token-economy.md
│   └── 10-backlog.md
│
├── scripts/
├── docker-compose.yml
├── .env.example
├── .gitignore
├── README.md
└── LICENSE
```

---

# 23. Modelo de datos conceptual

## Organization

Representa una empresa, comercio, cadena, franquicia o entidad dueña de la operación.

Campos sugeridos:

```text
id
name
legal_name
tax_id
status
default_currency
default_cashback_rate
created_at
updated_at
```

## Branch

Sucursal, tienda, punto de venta o unidad operativa.

Campos sugeridos:

```text
id
organization_id
name
code
address
city
state
country
timezone
status
created_at
updated_at
```

## User

Usuarios administrativos o usuarios internos.

Campos sugeridos:

```text
id
organization_id
branch_id nullable
name
email
password_hash
role
status
created_at
updated_at
```

Roles sugeridos:

```text
SUPERADMIN
ORG_ADMIN
BRANCH_MANAGER
CASHIER
SUPPORT
API_CLIENT
```

## Customer

Cliente final.

Campos sugeridos:

```text
id
organization_id
first_name
last_name
email
phone
external_reference
birthdate nullable
status
created_at
updated_at
```

## Wallet

Wallet de recompensas del cliente.

Campos sugeridos:

```text
id
organization_id
customer_id
available_balance
pending_balance
redeemed_balance
expired_balance
lifetime_earned
lifetime_redeemed
status
created_at
updated_at
```

## Sale

Venta registrada desde POS, ERP o e-commerce.

Campos sugeridos:

```text
id
organization_id
branch_id
customer_id
external_sale_id
subtotal_amount
discount_amount
tax_amount
total_amount
eligible_amount
paid_with_cashback_amount
payment_method
status
sale_datetime
created_at
updated_at
```

## SaleItem

Producto o concepto vendido.

Campos sugeridos:

```text
id
sale_id
product_id nullable
sku
name
category
quantity
unit_price
discount_amount
total_amount
eligible_for_cashback
created_at
updated_at
```

## CashbackRule

Regla de cálculo.

Campos sugeridos:

```text
id
organization_id
campaign_id nullable
name
description
rule_type
cashback_rate
fixed_amount
min_purchase_amount
max_cashback_amount
max_redemption_percentage
valid_from
valid_to
status
created_at
updated_at
```

## CashbackTransaction

Movimiento de ledger.

Campos sugeridos:

```text
id
organization_id
branch_id nullable
customer_id
wallet_id
sale_id nullable
redemption_id nullable
campaign_id nullable
transaction_type
status
amount
currency
description
reference
hash
previous_hash nullable
available_at nullable
expires_at nullable
created_by nullable
created_at
updated_at
```

## Redemption

Redención de saldo.

Campos sugeridos:

```text
id
organization_id
branch_id
customer_id
wallet_id
sale_id nullable
amount
status
redemption_code
created_at
updated_at
```

## Campaign

Campaña comercial.

Campos sugeridos:

```text
id
organization_id
name
description
start_date
end_date
status
priority
created_at
updated_at
```

## ApiKey

Llave para integraciones externas.

Campos sugeridos:

```text
id
organization_id
name
key_hash
scopes
status
last_used_at
created_at
updated_at
```

## BlockchainTransaction

Registro de interacción blockchain.

Campos sugeridos:

```text
id
organization_id
batch_id
network
contract_address
transaction_hash
block_number
payload_hash
status
created_at
updated_at
```

---

# 24. Recomendación de dinero y precisión

No usar `float` para dinero.

Opciones:

1. Guardar montos en centavos como enteros.
2. Usar `Decimal` con precisión fija.

Recomendación:

- En base de datos: `Numeric(18, 2)` o enteros en centavos.
- En Python: `Decimal`.
- En API: strings o números decimales controlados.

Ejemplo:

```json
{
  "total_amount": "1000.00",
  "cashback_rate": "0.01",
  "cashback_amount": "10.00"
}
```

---

# 25. API draft

## Auth

```http
POST /api/v1/auth/login
POST /api/v1/auth/refresh
GET /api/v1/auth/me
```

## Organizations

```http
POST /api/v1/organizations
GET /api/v1/organizations
GET /api/v1/organizations/{organization_id}
PATCH /api/v1/organizations/{organization_id}
```

## Branches

```http
POST /api/v1/branches
GET /api/v1/branches
GET /api/v1/branches/{branch_id}
PATCH /api/v1/branches/{branch_id}
```

## Customers

```http
POST /api/v1/customers
GET /api/v1/customers
GET /api/v1/customers/{customer_id}
PATCH /api/v1/customers/{customer_id}
GET /api/v1/customers/{customer_id}/wallet
GET /api/v1/customers/{customer_id}/transactions
```

## Wallets

```http
GET /api/v1/wallets/{wallet_id}
GET /api/v1/wallets/customer/{customer_id}
POST /api/v1/wallets/{wallet_id}/adjust
POST /api/v1/wallets/{wallet_id}/lock
POST /api/v1/wallets/{wallet_id}/unlock
```

## Sales

```http
POST /api/v1/sales
GET /api/v1/sales
GET /api/v1/sales/{sale_id}
POST /api/v1/sales/{sale_id}/cancel
POST /api/v1/sales/{sale_id}/refund
```

## Cashback

```http
POST /api/v1/cashback/calculate
POST /api/v1/cashback/apply
GET /api/v1/cashback/transactions
GET /api/v1/cashback/transactions/{transaction_id}
POST /api/v1/cashback/transactions/{transaction_id}/reverse
```

## Redemptions

```http
POST /api/v1/redemptions
GET /api/v1/redemptions
GET /api/v1/redemptions/{redemption_id}
POST /api/v1/redemptions/{redemption_id}/cancel
```

## Campaigns

```http
POST /api/v1/campaigns
GET /api/v1/campaigns
GET /api/v1/campaigns/{campaign_id}
PATCH /api/v1/campaigns/{campaign_id}
POST /api/v1/campaigns/{campaign_id}/activate
POST /api/v1/campaigns/{campaign_id}/pause
POST /api/v1/campaigns/{campaign_id}/cancel
```

## Reports

```http
GET /api/v1/reports/summary
GET /api/v1/reports/cashback-issued
GET /api/v1/reports/cashback-redeemed
GET /api/v1/reports/outstanding-liability
GET /api/v1/reports/customers
GET /api/v1/reports/branches
GET /api/v1/reports/campaigns
```

## Blockchain

```http
POST /api/v1/blockchain/batches
GET /api/v1/blockchain/batches
GET /api/v1/blockchain/transactions/{tx_id}
POST /api/v1/blockchain/anchor
```

---

# 26. Payloads de ejemplo

## Crear cliente

```json
{
  "first_name": "Emmanuel",
  "last_name": "Campos",
  "email": "cliente@example.com",
  "phone": "7221234567",
  "external_reference": "POS-CUST-001"
}
```

## Registrar venta

```json
{
  "branch_id": "uuid-branch",
  "customer_id": "uuid-customer",
  "external_sale_id": "TICKET-0001",
  "subtotal_amount": "1000.00",
  "discount_amount": "0.00",
  "tax_amount": "160.00",
  "total_amount": "1160.00",
  "eligible_amount": "1000.00",
  "paid_with_cashback_amount": "0.00",
  "payment_method": "cash",
  "items": [
    {
      "sku": "SKU-001",
      "name": "Producto ejemplo",
      "category": "General",
      "quantity": 2,
      "unit_price": "500.00",
      "discount_amount": "0.00",
      "total_amount": "1000.00",
      "eligible_for_cashback": true
    }
  ]
}
```

## Respuesta esperada de venta con cashback

```json
{
  "sale_id": "uuid-sale",
  "customer_id": "uuid-customer",
  "eligible_amount": "1000.00",
  "cashback_rate": "0.01",
  "cashback_amount": "10.00",
  "wallet_balance": {
    "available_balance": "10.00",
    "pending_balance": "0.00"
  },
  "transaction": {
    "id": "uuid-transaction",
    "type": "EARNED",
    "status": "AVAILABLE",
    "amount": "10.00"
  }
}
```

## Consultar wallet

```json
{
  "customer_id": "uuid-customer",
  "available_balance": "120.00",
  "pending_balance": "30.00",
  "redeemed_balance": "80.00",
  "expired_balance": "10.00",
  "lifetime_earned": "240.00",
  "lifetime_redeemed": "80.00"
}
```

## Redimir cashback

```json
{
  "customer_id": "uuid-customer",
  "branch_id": "uuid-branch",
  "sale_id": "uuid-sale",
  "amount": "50.00"
}
```

---

# 27. Reglas críticas de redención

Antes de redimir, validar:

1. Cliente existe.
2. Wallet está activa.
3. Organización está activa.
4. Sucursal está activa.
5. Saldo disponible suficiente.
6. Monto mayor a cero.
7. Redención no supera límite por ticket.
8. No existe duplicidad de redención.
9. La venta pertenece a la misma organización.
10. La venta no está cancelada.
11. La campaña permite redención, si aplica.
12. La redención queda registrada en ledger.

---

# 28. Ledger

El ledger debe ser la parte más crítica del sistema.

Debe permitir reconstruir el saldo de una wallet a partir de movimientos.

Principios:

- Nunca borrar movimientos.
- No sobrescribir montos históricos.
- Usar reversos en vez de eliminar.
- Registrar usuario o sistema que ejecutó el cambio.
- Registrar timestamps.
- Registrar referencias externas.
- Registrar hashes.
- Mantener trazabilidad.

## Ejemplo de ledger

```text
+10.00 EARNED por venta TICKET-001
+20.00 EARNED por venta TICKET-002
-5.00 REDEEMED por redención RED-001
-10.00 REVERSED por cancelación TICKET-001
```

Saldo calculado:

```text
10 + 20 - 5 - 10 = 15
```

---

# 29. Hash de integridad

Cada movimiento puede generar un hash con campos clave.

Ejemplo conceptual:

```text
hash = SHA256(
  transaction_id +
  organization_id +
  wallet_id +
  amount +
  transaction_type +
  previous_hash +
  created_at
)
```

Esto permitiría crear una cadena interna tipo blockchain ligera.

Campos:

```text
hash
previous_hash
batch_hash
```

---

# 30. Blockchain strategy detallada

## No registrar cada venta on-chain al inicio

Razones:

- Costos.
- Latencia.
- Complejidad.
- Experiencia de POS.
- Dependencia externa.
- Riesgo de fallas en venta.

## Sí registrar batches

Proceso sugerido:

1. Se generan movimientos internos.
2. Se agrupan por periodo.
3. Se calcula hash del batch.
4. Se registra hash en smart contract.
5. Se guarda transaction_hash en base de datos.
6. Se permite verificar integridad.

## Smart contract inicial

Contrato mínimo:

- Registrar hash de lote.
- Emitir evento.
- Consultar hashes registrados.
- Controlar owner/admin.

Pseudoestructura:

```solidity
contract OpenCashbackLedger {
    event BatchAnchored(bytes32 indexed batchHash, string metadataURI, uint256 timestamp);

    address public owner;

    mapping(bytes32 => bool) public anchoredBatches;

    function anchorBatch(bytes32 batchHash, string calldata metadataURI) external onlyOwner {
        require(!anchoredBatches[batchHash], "Batch already anchored");
        anchoredBatches[batchHash] = true;
        emit BatchAnchored(batchHash, metadataURI, block.timestamp);
    }
}
```

---

# 31. Seguridad

## Autenticación

- JWT para usuarios.
- API keys para integraciones.
- Refresh tokens opcional.
- Hash seguro de contraseñas.

## Autorización

Control por:

- Organización.
- Sucursal.
- Rol.
- Scope de API key.

## Multi-tenant

Todo registro sensible debe tener `organization_id`.

Nunca devolver datos de otra organización.

## API keys

Las API keys deben:

- Guardarse hasheadas.
- Tener scopes.
- Poder revocarse.
- Tener rate limiting.
- Registrar último uso.

Scopes posibles:

```text
customers:read
customers:write
sales:write
wallets:read
redemptions:write
reports:read
admin
```

## Auditoría

Registrar:

- Creación de usuarios.
- Ajustes manuales.
- Redenciones.
- Reversos.
- Cambios en reglas.
- Cambios en campañas.
- Uso de API keys.

---

# 32. Fraude y abuso

Posibles reglas antifraude:

- No permitir cashback en ventas canceladas.
- Bloquear redención inmediata si hay riesgo.
- Limitar redención diaria.
- Alertar ajustes manuales altos.
- Alertar ventas repetidas anómalas.
- Detectar clientes duplicados por teléfono/correo.
- Requerir autorización para ajustes manuales.
- Validar que la venta externa no se registre dos veces.
- Idempotency keys para integraciones.

---

# 33. Idempotencia

Los endpoints críticos deben soportar idempotencia.

Especialmente:

- Registro de venta.
- Aplicación de cashback.
- Redención.
- Reverso.

Header sugerido:

```http
Idempotency-Key: external-system-unique-id
```

Esto evita duplicar recompensas si un POS reintenta la petición.

---

# 34. Reportes esenciales

## Resumen ejecutivo

- Total ventas registradas.
- Cashback emitido.
- Cashback redimido.
- Cashback pendiente.
- Cashback expirado.
- Clientes activos.
- Clientes recurrentes.
- Ticket promedio.
- Tasa de redención.
- Tasa de recompra.

## Reporte financiero

- Pasivo total por recompensas.
- Pasivo por sucursal.
- Pasivo por campaña.
- Redenciones del periodo.
- Expiraciones del periodo.

## Reporte comercial

- Clientes con más saldo.
- Clientes más frecuentes.
- Campañas con mejor desempeño.
- Categorías con mayor cashback.
- Sucursales con mayor redención.

## Reporte operativo

- Transacciones por día.
- Redenciones por cajero.
- Ajustes manuales.
- Reversos.
- Errores de integración.

---

# 35. Dashboard MVP

Pantallas sugeridas:

1. Login.
2. Dashboard principal.
3. Clientes.
4. Detalle de cliente.
5. Wallet.
6. Movimientos.
7. Ventas.
8. Campañas.
9. Reglas de cashback.
10. Reportes.
11. Configuración de organización.
12. API keys.

---

# 36. Portal cliente MVP

Puede ser web simple.

Funciones:

- Consultar saldo.
- Ver historial.
- Ver beneficios.
- Generar QR para redención.
- Ver promociones.
- Actualizar datos básicos.

---

# 37. Integración POS

Flujo en POS:

1. Cajero selecciona cliente.
2. POS consulta saldo.
3. Cliente compra.
4. POS manda venta a Open Cashback.
5. Open Cashback calcula cashback.
6. POS muestra recompensa generada.
7. En próxima venta, POS puede redimir saldo.

## Endpoints mínimos para POS

```http
GET /api/v1/customers/search?phone=...
GET /api/v1/customers/{id}/wallet
POST /api/v1/sales
POST /api/v1/redemptions
```

---

# 38. Integración e-commerce

Flujo:

1. Orden pagada.
2. Webhook a Open Cashback.
3. Se registra venta.
4. Se calcula cashback.
5. Cliente recibe saldo.
6. En checkout futuro puede redimir.

Integraciones futuras:

- WooCommerce.
- Shopify.
- Tienda propia.
- Mercado Pago.
- Stripe.

---

# 39. Backlog maestro

## Épica 1: Setup del proyecto

- Crear estructura de carpetas.
- Crear README.
- Crear docs.
- Configurar FastAPI.
- Configurar Docker.
- Configurar PostgreSQL.
- Configurar Alembic.
- Configurar variables de entorno.
- Configurar testing.
- Configurar linting.

## Épica 2: Autenticación

- Modelo User.
- Registro de usuario admin.
- Login.
- JWT.
- Roles.
- Middleware de usuario actual.
- Password hashing.

## Épica 3: Multi-tenant

- Modelo Organization.
- Modelo Branch.
- Validación de organization_id.
- Permisos por organización.
- Permisos por sucursal.

## Épica 4: Clientes

- Crear cliente.
- Editar cliente.
- Buscar cliente.
- Consultar detalle.
- Crear wallet automática.
- Validar duplicados.

## Épica 5: Wallet

- Crear wallet.
- Consultar saldo.
- Actualizar saldo mediante ledger.
- Bloquear wallet.
- Desbloquear wallet.
- Historial.

## Épica 6: Ledger

- Crear movimientos.
- Calcular saldo.
- Registrar hashes.
- Reversos.
- Expiraciones.
- Auditoría.

## Épica 7: Cashback engine

- Regla global.
- Cálculo por venta.
- Cálculo por monto elegible.
- Exclusiones.
- Límites.
- Redondeo.
- Estado pendiente/disponible.

## Épica 8: Ventas

- Crear venta.
- Asociar cliente.
- Asociar sucursal.
- Asociar items.
- Aplicar cashback.
- Cancelar venta.
- Reembolsar venta.
- Reversar cashback.

## Épica 9: Redención

- Validar saldo.
- Crear redención.
- Asociar a venta.
- Actualizar ledger.
- Evitar doble redención.
- Cancelar redención.

## Épica 10: Campañas

- Crear campaña.
- Activar campaña.
- Pausar campaña.
- Reglas por fechas.
- Reglas por categoría.
- Reglas por sucursal.
- Reglas por ticket mínimo.

## Épica 11: Reportes

- Dashboard resumen.
- Cashback emitido.
- Cashback redimido.
- Pasivo.
- Clientes.
- Campañas.
- Sucursales.

## Épica 12: API keys

- Crear API key.
- Hashear API key.
- Scopes.
- Revocación.
- Rate limiting.
- Logs de uso.

## Épica 13: Blockchain prototype

- Crear contrato.
- Configurar Hardhat.
- Desplegar local en Ganache.
- Crear endpoint de anchoring.
- Registrar hash batch.
- Guardar transaction hash.

## Épica 14: Frontend admin

- Login.
- Dashboard.
- Clientes.
- Wallet.
- Movimientos.
- Ventas.
- Campañas.
- Configuración.

## Épica 15: Portal cliente

- Consulta de saldo.
- Historial.
- QR.
- Promociones.

---

# 40. Sprints sugeridos

## Sprint 0: Fundación

Objetivo: levantar base técnica.

Entregables:

- Repo estructurado.
- Backend FastAPI corriendo.
- PostgreSQL conectado.
- Alembic funcionando.
- Docker Compose.
- README inicial.
- `.env.example`.

## Sprint 1: Auth + organizaciones

Entregables:

- User.
- Organization.
- Branch.
- JWT.
- Roles básicos.
- Middleware multi-tenant.

## Sprint 2: Clientes + wallets

Entregables:

- CRUD de clientes.
- Wallet automática.
- Consulta de saldo.
- Validación de duplicados.

## Sprint 3: Ventas + cashback

Entregables:

- Registro de venta.
- Items de venta.
- Regla global.
- Cálculo de cashback.
- Movimiento EARNED.
- Actualización de wallet.

## Sprint 4: Redención + reversos

Entregables:

- Redención.
- Movimiento REDEEMED.
- Cancelación de venta.
- Movimiento REVERSED.
- Validaciones de saldo.

## Sprint 5: Dashboard + reportes

Entregables:

- Métricas básicas.
- Clientes.
- Wallets.
- Movimientos.
- Pasivo.

## Sprint 6: API externa

Entregables:

- API keys.
- Scopes.
- Idempotency keys.
- Documentación para POS.

## Sprint 7: Blockchain anchoring

Entregables:

- Smart contract local.
- Batch hash.
- Anchor endpoint.
- Registro de tx hash.

---

# 41. README sugerido para GitHub

```markdown
# Open Cashback

Open Cashback is an open cashback, loyalty and programmable rewards infrastructure for POS, ERP, e-commerce and merchant networks.

The project starts as a reliable internal cashback ledger and is designed to evolve into a blockchain-auditable rewards protocol.

## Core idea

Every purchase can generate a reward.  
Every reward can drive retention.  
Every transaction can create actionable business data.

## Main features

- Customer wallets
- Cashback rules
- Reward ledger
- Redemption flow
- Campaign engine
- POS/ERP/e-commerce API
- Multi-merchant architecture
- Blockchain anchoring roadmap

## Tech stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- React
- Solidity
- Web3.py

## Repository

```bash
git@github.com:Ecamposg95/open-cashback.git
```

## Status

Early-stage architecture and MVP planning.
```

---

# 42. Comandos iniciales sugeridos

```bash
git clone git@github.com:Ecamposg95/open-cashback.git
cd open-cashback

mkdir -p backend/app/{api/v1,core,models,schemas,services,repositories,utils,tests}
mkdir -p frontend
mkdir -p contracts/{contracts,scripts,test}
mkdir -p docs scripts

touch README.md
touch docs/00-master-brief.md
touch docs/01-product-vision.md
touch docs/02-architecture.md
touch docs/03-api.md
touch docs/04-data-model.md
touch docs/05-business-rules.md
touch docs/06-blockchain-strategy.md
touch docs/07-roadmap.md
touch docs/08-security.md
touch docs/09-token-economy.md
touch docs/10-backlog.md
touch .env.example
touch .gitignore
touch docker-compose.yml

git add .
git commit -m "chore: initialize open cashback project structure"
git push origin main
```

---

# 43. Variables de entorno sugeridas

```env
APP_NAME=Open Cashback
APP_ENV=development
APP_DEBUG=true

DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/open_cashback

JWT_SECRET_KEY=change_me
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=60

CORS_ORIGINS=http://localhost:5173,http://localhost:3000

BLOCKCHAIN_ENABLED=false
BLOCKCHAIN_NETWORK=ganache
BLOCKCHAIN_RPC_URL=http://127.0.0.1:8545
BLOCKCHAIN_PRIVATE_KEY=
BLOCKCHAIN_CONTRACT_ADDRESS=

CASHBACK_DEFAULT_RATE=0.01
CASHBACK_DEFAULT_EXPIRATION_DAYS=90
```

---

# 44. Docker Compose sugerido

```yaml
version: "3.9"

services:
  db:
    image: postgres:16
    container_name: open_cashback_db
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: open_cashback
    ports:
      - "5432:5432"
    volumes:
      - open_cashback_pgdata:/var/lib/postgresql/data

  backend:
    build: ./backend
    container_name: open_cashback_backend
    env_file:
      - .env
    ports:
      - "8000:8000"
    depends_on:
      - db
    volumes:
      - ./backend:/app

volumes:
  open_cashback_pgdata:
```

---

# 45. Criterios de aceptación del MVP

El MVP se considera funcional cuando:

1. Un admin puede iniciar sesión.
2. Un admin puede crear una organización.
3. Un admin puede crear una sucursal.
4. Un admin puede crear un cliente.
5. El cliente recibe una wallet automáticamente.
6. Se puede registrar una venta.
7. La venta genera cashback.
8. El cashback aparece en la wallet.
9. Se puede consultar el saldo.
10. Se puede redimir saldo.
11. La redención queda en ledger.
12. Se puede cancelar una venta y revertir cashback.
13. Existen reportes básicos.
14. La API está documentada.
15. Existen pruebas básicas de cálculo y redención.

---

# 46. Pruebas unitarias críticas

Probar:

- Cálculo de cashback al 1%.
- Cálculo con descuento.
- Cálculo con productos no elegibles.
- Redención con saldo suficiente.
- Redención con saldo insuficiente.
- Redención con límite máximo por ticket.
- Cancelación de venta.
- Reverso de cashback.
- Idempotencia de venta.
- Doble redención.
- Expiración de saldo.
- Multi-tenant isolation.
- API key inválida.
- API key sin scope.

---

# 47. Testing examples

## Caso: cashback simple

```text
Dado un cliente con wallet activa
Y una venta de $1,000 elegible
Y una regla de cashback del 1%
Cuando se registra la venta
Entonces se genera un movimiento EARNED de $10
Y el saldo de wallet aumenta $10
```

## Caso: redención

```text
Dado un cliente con $100 disponibles
Cuando redime $50
Entonces se genera un movimiento REDEEMED de -$50
Y el saldo disponible queda en $50
```

## Caso: saldo insuficiente

```text
Dado un cliente con $20 disponibles
Cuando intenta redimir $50
Entonces el sistema rechaza la operación
Y no genera movimiento de ledger
```

## Caso: venta cancelada

```text
Dado una venta que generó $10 de cashback
Cuando la venta se cancela
Entonces se genera un movimiento REVERSED de -$10
Y el saldo se ajusta
```

---

# 48. Futuras integraciones

## POS

- Atlas POS.
- POS externo.
- POS local/offline.
- POS web.
- Terminal móvil.

## ERP

- Atlas ERP.
- Odoo.
- ERP personalizado.

## E-commerce

- WooCommerce.
- Shopify.
- Tienda propia.
- Mercado Libre futuro.
- Marketplace propio.

## Pagos

- Mercado Pago.
- Stripe.
- SPEI.
- Terminal bancaria.
- Wallet interna.

## Comunicación

- Email.
- SMS.
- WhatsApp Business.
- Push notifications.

---

# 49. Token economy preliminar

No implementar token económico en MVP.

Pero preparar documentación para:

- Reward unit.
- Supply.
- Emission.
- Redemption.
- Burn.
- Expiration.
- Merchant liability.
- Customer balance.
- Cross-merchant settlement.
- Treasury.
- Reserve.
- Fraud controls.

## Posible token

Nombres hipotéticos:

- OCASH.
- CASHX.
- OPEN.
- REWARD.
- Loyalty MXN.
- Cashback MXN.

## Principio

El token no debe lanzarse hasta tener claridad legal, fiscal y operativa.

---

# 50. Posicionamiento

Frases posibles:

- Open Cashback turns every transaction into a programmable reward.
- Cashback abierto para negocios modernos.
- Convierte ventas en lealtad.
- Convierte tickets en recompensas.
- Loyalty infrastructure for modern commerce.
- La capa de recompensas para POS y ERP.
- Del punto de venta al punto de relación.
- Recompensas programables para comercios físicos y digitales.
- Una red abierta de beneficios para clientes y negocios.

---

# 51. Roadmap de producto

## Etapa 1: Cashback Core

- Wallet.
- Clientes.
- Ventas.
- Cashback.
- Redención.
- Reportes.

## Etapa 2: Campaign Engine

- Reglas avanzadas.
- Segmentación.
- Fechas.
- Categorías.
- Sucursales.
- Clientes frecuentes.

## Etapa 3: Integraciones

- API keys.
- POS.
- E-commerce.
- Webhooks.
- SDK.

## Etapa 4: Customer Experience

- Portal cliente.
- QR.
- Promociones.
- Notificaciones.
- Perfil de cliente.

## Etapa 5: Blockchain Audit

- Hash ledger.
- Batch anchor.
- Smart contract.
- Explorador interno.

## Etapa 6: Multi-merchant Network

- Comercios afiliados.
- Redención cruzada.
- Campañas colaborativas.
- Marketplace de beneficios.

## Etapa 7: Tokenized Rewards

- Token.
- Smart contracts.
- Wallet Web3.
- Settlement.
- Governance opcional.

---

# 52. Decisiones técnicas recomendadas

## Usar UUIDs

Todas las entidades principales deben usar UUID.

## Usar timestamps

Campos:

```text
created_at
updated_at
deleted_at nullable
```

## Soft delete

Evitar borrar datos sensibles. Usar estado o `deleted_at`.

## Usar Alembic

Toda modificación de base de datos debe tener migración.

## Usar services

No poner lógica de negocio compleja directamente en rutas.

## Usar repositories

Opcional, pero recomendado para desacoplar acceso a datos.

## Usar schemas Pydantic

Separar input/output.

## Usar pruebas desde el inicio

Prioridad alta para cálculo financiero.

---

# 53. No hacer todavía

Evitar en MVP:

- App móvil nativa.
- Token real.
- Mainnet.
- Marketplace complejo.
- DeFi.
- Custodia.
- KYC.
- Integraciones bancarias.
- Contabilidad fiscal avanzada.
- IA predictiva.
- Multi-país.
- Arquitectura microservicios compleja.
- Event sourcing completo, salvo ledger simple.
- Kubernetes.

---

# 54. Sí preparar desde el inicio

- Multi-tenant.
- Auditoría.
- Ledger robusto.
- Idempotencia.
- API-first.
- Documentación.
- Seguridad.
- Escalabilidad razonable.
- Hashes de integridad.
- Separación por capas.
- Testing financiero.
- Configuración por organización.

---

# 55. Primer milestone

## Milestone: MVP Core Ledger

Objetivo:

Crear un backend funcional que permita registrar clientes, ventas, cashback y redenciones con trazabilidad.

Entregables:

- FastAPI backend.
- PostgreSQL.
- Auth.
- Organization.
- Branch.
- Customer.
- Wallet.
- Sale.
- CashbackTransaction.
- Redemption.
- CashbackRule global.
- Endpoints principales.
- Tests.
- Documentación.

---

# 56. Segundo milestone

## Milestone: POS Integration Ready

Objetivo:

Permitir que un POS externo pueda usar Open Cashback.

Entregables:

- API keys.
- Scopes.
- Idempotency keys.
- Endpoints documentados.
- Ejemplos de integración.
- Webhooks básicos.
- Logs de integración.

---

# 57. Tercer milestone

## Milestone: Blockchain Anchoring Prototype

Objetivo:

Probar trazabilidad blockchain sin comprometer operación POS.

Entregables:

- Hash por movimiento.
- Hash por batch.
- Smart contract local.
- Anchor batch.
- Guardar transaction hash.
- Verificar batch.

---

# 58. Definición de éxito inicial

El proyecto será exitoso en primera etapa si puede demostrar:

1. Que el cashback se calcula correctamente.
2. Que el cliente entiende su saldo.
3. Que el negocio puede controlar el pasivo.
4. Que el POS puede integrarse fácilmente.
5. Que el ledger puede auditarse.
6. Que la arquitectura está lista para blockchain futura.
7. Que el módulo puede venderse como producto independiente o add-on.

---

# 59. Prompt sugerido para IA de desarrollo

Usar este prompt junto con el archivo:

```text
Actúa como arquitecto de software senior, desarrollador backend experto en FastAPI/PostgreSQL y product engineer. Con base en el archivo maestro de Open Cashback, genera la primera versión funcional del proyecto respetando la arquitectura por capas, priorizando el MVP Core Ledger.

No implementes blockchain real todavía. Primero construye el ledger interno, wallets, clientes, ventas, cálculo de cashback y redenciones. Usa código limpio, servicios separados, modelos SQLAlchemy, schemas Pydantic, migraciones Alembic, pruebas unitarias y documentación OpenAPI.

El objetivo es que el sistema pueda integrarse posteriormente con POS, ERP, e-commerce y una capa blockchain de anchoring.
```

---

# 60. Prompt para generación de README

```text
Con base en el master brief de Open Cashback, genera un README profesional para GitHub. El README debe explicar visión, problema, solución, arquitectura, stack, módulos, roadmap, setup local, estructura del repositorio, endpoints iniciales, estrategia blockchain y estado del proyecto. El tono debe ser técnico, startup y open-source.
```

---

# 61. Prompt para generación de backlog

```text
Con base en el master brief de Open Cashback, genera un backlog técnico en formato épicas, historias de usuario, tareas técnicas y criterios de aceptación. Prioriza el MVP Core Ledger, después POS Integration Ready y finalmente Blockchain Anchoring Prototype.
```

---

# 62. Prompt para generación de código

```text
Con base en el master brief de Open Cashback, crea la estructura inicial del backend en FastAPI. Incluye configuración, conexión a PostgreSQL, modelos SQLAlchemy, schemas Pydantic, rutas v1, servicios, migraciones Alembic y pruebas unitarias para clientes, wallets, ventas, cashback y redenciones.

Respeta principios de multi-tenant usando organization_id en las entidades principales. Usa Decimal para dinero. Implementa idempotencia en registro de ventas y redenciones.
```

---

# 63. Resumen final para agentes

Open Cashback es una plataforma de cashback y loyalty API-first, diseñada para integrarse con POS, ERP, e-commerce y redes comerciales. El MVP debe iniciar con un ledger interno confiable en PostgreSQL, wallets de clientes, reglas básicas de cashback, registro de ventas y redención. La blockchain debe entrar después como capa de auditoría mediante hashes y batch anchoring, no como dependencia crítica de la operación diaria.

La prioridad es construir una base sólida, auditable, modular y comercialmente útil.

---

# 64. One-liner

**Open Cashback turns every transaction into a programmable reward.**

---

# 65. One-liner en español

**Open Cashback convierte cada compra en una recompensa programable.**
