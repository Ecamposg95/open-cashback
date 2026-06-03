import { Gift, ShieldCheck, Wallet } from "lucide-react";
import { useEffect, useState } from "react";
import { AppShell } from "../../components/AppShell";
import { KpiCard } from "../../components/KpiCard";
import { LedgerTable } from "../../components/LedgerTable";
import { fetchCustomerPortalData, type CustomerView, type TransactionView, type WalletView } from "../../lib/api";
import { DEMO_CUSTOMER_ID, DEMO_ORG_ID } from "../../lib/demoData";
import { money } from "../../lib/format";

type CustomerData = {
  source: "api" | "demo";
  customer: CustomerView;
  wallet: WalletView;
  transactions: TransactionView[];
};

export function CustomerPortal({ page }: { page: "dashboard" | "transactions" | "redeem" | "web3" }) {
  const [data, setData] = useState<CustomerData | null>(null);

  useEffect(() => {
    fetchCustomerPortalData().then(setData);
  }, []);

  if (!data) {
    return <AppShell mode="customer" title="Loading wallet" subtitle="Preparing rewards data."><section className="section-block">Loading...</section></AppShell>;
  }

  const { customer, wallet, transactions, source } = data;

  if (page === "transactions") {
    return (
      <AppShell mode="customer" dataSource={source} title="Reward history" subtitle="All wallet movements are tracked in the internal ledger.">
        <LedgerTable transactions={transactions} />
      </AppShell>
    );
  }

  if (page === "redeem") {
    return (
      <AppShell mode="customer" dataSource={source} title="Redeem cashback" subtitle="Generate a short-lived redemption intent for POS confirmation.">
        <section className="redeem-panel">
          <div>
            <p>Available balance</p>
            <strong>{money(wallet.availableBalance)}</strong>
          </div>
          <label>
            Amount to redeem
            <input value="50.00" readOnly />
          </label>
          <div className="qr-box">RED-DEMO-8F2A91</div>
          <span className="muted">Next backend step: QR intent with TTL, token hash and one-time confirmation.</span>
        </section>
      </AppShell>
    );
  }

  if (page === "web3") {
    return (
      <AppShell mode="customer" dataSource={source} title="Web3 audit" subtitle="Ledger first, blockchain anchoring ready.">
        <section className="audit-card">
          <ShieldCheck size={32} />
          <h2>Auditable internal ledger</h2>
          <p>Your rewards are tracked with transaction hashes. Future anchoring can verify batches without slowing down checkout.</p>
          <code>Latest hash: {transactions[0]?.hash ?? "No ledger movements yet"}</code>
        </section>
      </AppShell>
    );
  }

  return (
    <AppShell mode="customer" dataSource={source} title={`Hola, ${customer.firstName}`} subtitle="Your rewards wallet is ready.">
      <section className="hero-wallet">
        <p>Available cashback</p>
        <strong>{money(wallet.availableBalance)}</strong>
        <span>Pending {money(wallet.pendingBalance)} · Wallet {wallet.status}</span>
        <a className="primary-action" href={`/portal/${DEMO_ORG_ID}/customers/${DEMO_CUSTOMER_ID}/redeem`}>Redeem</a>
      </section>
      <div className="kpi-grid">
        <KpiCard label="Lifetime earned" value={money(wallet.lifetimeEarned)} icon={<Wallet size={20} />} />
        <KpiCard label="Lifetime redeemed" value={money(wallet.lifetimeRedeemed)} icon={<Gift size={20} />} />
        <KpiCard label="Expired" value={money(wallet.expiredBalance)} helper="Keep an eye on expiration dates" />
      </div>
      <section className="section-block">
        <div className="section-title">
          <h2>Recent movements</h2>
          <a href={`/portal/${DEMO_ORG_ID}/customers/${DEMO_CUSTOMER_ID}/transactions`}>View all</a>
        </div>
        <LedgerTable transactions={transactions.slice(0, 3)} />
      </section>
    </AppShell>
  );
}
