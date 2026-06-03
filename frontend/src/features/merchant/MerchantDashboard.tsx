import { Blocks, Gift, ReceiptText, Users, Wallet } from "lucide-react";
import { AppShell } from "../../components/AppShell";
import { KpiCard } from "../../components/KpiCard";
import { LedgerTable } from "../../components/LedgerTable";
import { demoCustomers, demoKpis, demoOrganization, demoTransactions } from "../../lib/demoData";
import { money } from "../../lib/format";

export function MerchantDashboard({ page }: { page: "dashboard" | "customers" | "sales" | "ledger" | "campaigns" | "blockchain" | "settings" }) {
  if (page === "customers") {
    return (
      <AppShell mode="merchant" title="Customers" subtitle="Wallet balances and loyalty status by customer.">
        <div className="table-wrap">
          <table>
            <thead><tr><th>Name</th><th>Email</th><th>Balance</th><th>Status</th></tr></thead>
            <tbody>{demoCustomers.map((customer) => <tr key={customer.id}><td>{customer.name}</td><td>{customer.email}</td><td>{money(customer.balance)}</td><td>{customer.status}</td></tr>)}</tbody>
          </table>
        </div>
      </AppShell>
    );
  }

  if (page === "sales") {
    return (
      <AppShell mode="merchant" title="POS simulator" subtitle="Preview cashback and register demo sales through the API later.">
        <section className="form-panel">
          <label>Customer<input value="Emmanuel Campos" readOnly /></label>
          <label>Branch<input value="Centro" readOnly /></label>
          <label>Eligible amount<input value="1000.00" readOnly /></label>
          <div className="cashback-preview">
            <span>Cashback rate: {(demoOrganization.cashbackRate * 100).toFixed(2)}%</span>
            <strong>Cashback preview: {money(10)}</strong>
          </div>
          <button>Register sale demo</button>
        </section>
      </AppShell>
    );
  }

  if (page === "ledger") {
    return (
      <AppShell mode="merchant" title="Ledger explorer" subtitle="Audit cashback movements, hashes and references.">
        <LedgerTable transactions={demoTransactions} />
      </AppShell>
    );
  }

  if (page === "campaigns") {
    return (
      <AppShell mode="merchant" title="Campaigns" subtitle="Global cashback is active; advanced campaign engine comes next.">
        <section className="audit-card">
          <Gift size={30} />
          <h2>Global cashback rule</h2>
          <p>{demoOrganization.name} currently issues {(demoOrganization.cashbackRate * 100).toFixed(2)}% cashback on eligible purchases.</p>
        </section>
      </AppShell>
    );
  }

  if (page === "blockchain") {
    return (
      <AppShell mode="merchant" title="Blockchain anchoring" subtitle="Web3 audit readiness without checkout latency.">
        <section className="audit-card">
          <Blocks size={32} />
          <h2>Anchoring mode: simulated</h2>
          <p>Ledger batches can be hashed and anchored later through OpenCashbackLedger.sol.</p>
          <code>Contract: contracts/contracts/OpenCashbackLedger.sol</code>
        </section>
      </AppShell>
    );
  }

  if (page === "settings") {
    return (
      <AppShell mode="merchant" title="Organization settings" subtitle="Configure the merchant loyalty program.">
        <section className="form-panel">
          <label>Organization<input value={demoOrganization.name} readOnly /></label>
          <label>Default currency<input value={demoOrganization.currency} readOnly /></label>
          <label>Global cashback rate<input value="0.01" readOnly /></label>
        </section>
      </AppShell>
    );
  }

  return (
    <AppShell mode="merchant" title="Merchant Dashboard" subtitle="Operate cashback, liability and rewards from one LaaS console.">
      <div className="kpi-grid">
        <KpiCard label="Outstanding liability" value={money(demoKpis.outstandingLiability)} icon={<Wallet size={20} />} />
        <KpiCard label="Cashback issued" value={money(demoKpis.cashbackIssued)} icon={<Gift size={20} />} />
        <KpiCard label="Cashback redeemed" value={money(demoKpis.cashbackRedeemed)} helper={`${demoKpis.redemptionRate}% redemption rate`} />
        <KpiCard label="Customers" value={String(demoKpis.customersCount)} icon={<Users size={20} />} />
        <KpiCard label="Sales registered" value={String(demoKpis.salesCount)} icon={<ReceiptText size={20} />} />
      </div>
      <section className="section-block">
        <div className="section-title">
          <h2>Recent ledger</h2>
          <a href="/app/demo-org/transactions">Open explorer</a>
        </div>
        <LedgerTable transactions={demoTransactions.slice(0, 3)} />
      </section>
    </AppShell>
  );
}
