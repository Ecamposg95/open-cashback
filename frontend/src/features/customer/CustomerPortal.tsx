import { Gift, ShieldCheck, Wallet } from "lucide-react";
import { AppShell } from "../../components/AppShell";
import { KpiCard } from "../../components/KpiCard";
import { LedgerTable } from "../../components/LedgerTable";
import { demoCustomer, demoTransactions, demoWallet } from "../../lib/demoData";
import { money } from "../../lib/format";

export function CustomerPortal({ page }: { page: "dashboard" | "transactions" | "redeem" | "web3" }) {
  if (page === "transactions") {
    return (
      <AppShell mode="customer" title="Reward history" subtitle="All wallet movements are tracked in the internal ledger.">
        <LedgerTable transactions={demoTransactions} />
      </AppShell>
    );
  }

  if (page === "redeem") {
    return (
      <AppShell mode="customer" title="Redeem cashback" subtitle="Generate a short-lived redemption intent for POS confirmation.">
        <section className="redeem-panel">
          <div>
            <p>Available balance</p>
            <strong>{money(demoWallet.availableBalance)}</strong>
          </div>
          <label>
            Amount to redeem
            <input value="50.00" readOnly />
          </label>
          <div className="qr-box">RED-DEMO-8F2A91</div>
          <span className="muted">MVP next step: backend QR intent with TTL, token hash and one-time confirmation.</span>
        </section>
      </AppShell>
    );
  }

  if (page === "web3") {
    return (
      <AppShell mode="customer" title="Web3 audit" subtitle="Ledger first, blockchain anchoring ready.">
        <section className="audit-card">
          <ShieldCheck size={32} />
          <h2>Auditable internal ledger</h2>
          <p>Your rewards are tracked with transaction hashes. Future anchoring can verify batches without slowing down checkout.</p>
          <code>Latest hash: {demoTransactions[0].hash}</code>
        </section>
      </AppShell>
    );
  }

  return (
    <AppShell mode="customer" title={`Hola, ${demoCustomer.firstName}`} subtitle="Your rewards wallet is ready.">
      <section className="hero-wallet">
        <p>Available cashback</p>
        <strong>{money(demoWallet.availableBalance)}</strong>
        <span>Pending {money(demoWallet.pendingBalance)} · Wallet {demoWallet.status}</span>
        <a className="primary-action" href="/portal/demo-org/customers/demo-customer/redeem">Redeem</a>
      </section>
      <div className="kpi-grid">
        <KpiCard label="Lifetime earned" value={money(demoWallet.lifetimeEarned)} icon={<Wallet size={20} />} />
        <KpiCard label="Lifetime redeemed" value={money(demoWallet.lifetimeRedeemed)} icon={<Gift size={20} />} />
        <KpiCard label="Expired" value={money(demoWallet.expiredBalance)} helper="Keep an eye on expiration dates" />
      </div>
      <section className="section-block">
        <div className="section-title">
          <h2>Recent movements</h2>
          <a href="/portal/demo-org/customers/demo-customer/transactions">View all</a>
        </div>
        <LedgerTable transactions={demoTransactions.slice(0, 3)} />
      </section>
    </AppShell>
  );
}
