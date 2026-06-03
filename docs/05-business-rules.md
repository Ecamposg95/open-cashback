# Reglas de negocio

Regla MVP: cashback global por organizacion.

```text
cashback_amount = eligible_amount * organization.default_cashback_rate
```

Ejemplo: $1,000 MXN al 1% genera $10 MXN.

No se borran movimientos historicos. Cancelaciones y correcciones crean movimientos `REVERSED` o `ADJUSTED`.

Tipos iniciales: `EARNED`, `REDEEMED`, `EXPIRED`, `ADJUSTED`, `REVERSED`, `BONUS`, `REFERRAL`, `LOCKED`, `UNLOCKED`.
