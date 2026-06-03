# Open Cashback - Collaborative Agent Context

This folder is the working context for AI collaborators and developers joining Open Cashback.

Before editing code, every agent should read:

1. `context/open_cashback_master_brief.md`
2. `context/agents/mvp-collaboration-brief.md`
3. `context/product/ui-mvp-spec.md`
4. `context/technical/mvp-implementation-plan.md`
5. `docs/02-architecture.md`
6. `docs/04-data-model.md`
7. `docs/10-backlog.md`

## Project principle

Open Cashback is not a points app. It is a Loyalty as a Service platform with wallet, cashback, rewards ledger, auditability and Web3-ready anchoring.

The MVP must prioritize:

- Useful product demo.
- Solid internal ledger.
- Multi-tenant isolation.
- Decimal-safe money handling.
- POS/ERP integration readiness.
- Customer and merchant UI.
- Blockchain preparation without runtime dependency.

## Agent collaboration rules

- Do not rewrite unrelated files.
- Do not remove context files.
- Keep business logic in services, not API routes.
- Preserve `organization_id` isolation in every operational query.
- Never use float for money.
- Do not implement ERC20 token logic in MVP.
- Document decisions in `docs/` or `context/` when they affect architecture.
- For frontend work, build the real app screens, not a landing page.
- For backend work, add tests for financial behavior.

## Current product target

Reach an MVP where a demo can show:

1. Merchant creates/configures a loyalty program.
2. Merchant creates customers or imports them through API.
3. A sale generates cashback.
4. Customer sees balance, history and redemption option.
5. Merchant sees liability, issued cashback and redeemed cashback.
6. Ledger shows auditable transactions and hashes.
7. Blockchain panel shows anchoring readiness.
