import { Blocks, Gift, ReceiptText, Users, Wallet } from "lucide-react";
import { useEffect, useState } from "react";
import { AppShell } from "../../components/AppShell";
import { KpiCard } from "../../components/KpiCard";
import { LedgerTable } from "../../components/LedgerTable";
import { fetchMerchantData, registerDemoSale, type CustomerRow, type KpiView, type TransactionView } from "../../lib/api";
import { demoOrganization } from "../../lib/demoData";
import { money } from "../../lib/format";

type MerchantData = {
  source: "api" | "demo";
  organization: typeof demoOrganization;
  kpis: KpiView;
  customers: CustomerRow[];
  transactions: TransactionView[];
};

export function MerchantDashboard({ page }: { page: "dashboard" | "customers" | "sales" | "ledger" | "campaigns" | "blockchain" | "settings" }) {
  const [data, setData] = useState<MerchantData | null>(null);
  const [saleStatus, setSaleStatus] = useState<string>("");

  useEffect(() => {
    fetchMerchantData().then(setData);
  }, [saleStatus]);

  async function submitDemoSale() {
    setSaleStatus("Registering sale...");
    try {
      const response = await registerDemoSale(1000);
      setSaleStatus(`Sale registered. Cashback generated: ${money(Number(response.cashback_amount))}`);
    } catch {
      setSaleStatus("Backend unavailable. Run the API and seed demo data, then retry.");
    }
  }

  if (!data) {
    return <AppShell mode="merchant" title="Loading dashboard" subtitle="Preparing merchant data."><section className="section-block">Loading...</section></AppShell>;
  }

  const { customers, kpis, organization, source, transactions } = data;

  if (page === "customers") {
    return (
      <AppShell mode="merchant" dataSource={source} title="Customers" subtitle="Wallet balances and loyalty status by customer.">
        <div className="table-wrap">
          <table>
            <thead><tr><th>Name</th><th>Email</th><th>Balance</th><th>Status</th></tr></thead>
            <tbody>{customers.map((customer) => <tr key={customer.id}><td>{customer.name}</td><td>{customer.email}</td><td>{money(customer.balance)}</td><td>{customer.status}</td></tr>)}</tbody>
          </table>
        </div>
      </AppShell>
    );
  }

  if (page === "sales") {
    return (
      <AppShell mode="merchant" dataSource={source} title="POS simulator" subtitle="Preview cashback and register demo sales through the API.">
        <section className="form-panel">
          <label>Customer<input value="Emmanuel Campos" readOnly /></label>
          <label>Branch<input value="Centro" readOnly /></label>
          <label>Eligible amount<input value="1000.00" readOnly /></label>
          <div className="cashback-preview">
            <span>Cashback rate: {(organization.cashbackRate * 100).toFixed(2)}%</span>
            <strong>Cashback preview: {money(10)}</strong>
          </div>
          <button onClick={submitDemoSale}>Register sale demo</button>
          {saleStatus ? <span className="muted">{saleStatus}</span> : null}
        </section>
      </AppShell>
    );
  }

  if (page === "ledger") {
    return (
      <AppShell mode="merchant" dataSource={source} title="Ledger explorer" subtitle="Audit cashback movements, hashes and references.">
        <LedgerTable transactions={transactions} />
      </AppShell>
    );
  }

  if (page === "campaigns") {
    return (
      <AppShell mode="merchant" dataSource={source} title="Campaigns" subtitle="Global cashback is active; advanced campaign engine comes next.">
        <section className="audit-card">
          <Gift size={30} />
          <h2>Global cashback rule</h2>
          <p>{organization.name} currently issues {(organization.cashbackRate * 100).toFixed(2)}% cashback on eligible purchases.</p>
        </section>
      </AppShell>
    );
  }

  if (page === "blockchain") {
    return (
      <AppShell mode="merchant" dataSource={source} title="Blockchain anchoring" subtitle="Web3 audit readiness without checkout latency.">
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
      <AppShell mode="merchant" dataSource={source} title="Organization settings" subtitle="Configure the merchant loyalty program.">
        <section className="form-panel">
          <label>Organization<input value={organization.name} readOnly /></label>
          <label>Default currency<input value={organization.currency} readOnly /></label>
          <label>Global cashback rate<input value={String(organization.cashbackRate)} readOnly /></label>
        </section>
      </AppShell>
    );
  }

  return (
    <AppShell mode="merchant" dataSource={source} title="Merchant Dashboard" subtitle="Operate cashback, liability and rewards from one LaaS console.">
      <div className="kpi-grid">
        <KpiCard label="Outstanding liability" value={money(kpis.outstandingLiability)} icon={<Wallet size={20} />} />
        <KpiCard label="Cashback issued" value={money(kpis.cashbackIssued)} icon={<Gift size={20} />} />
        <KpiCard label="Cashback redeemed" value={money(kpis.cashbackRedeemed)} helper={`${kpis.redemptionRate}% redemption rate`} />
        <KpiCard label="Customers" value={String(kpis.customersCount)} icon={<Users size={20} />} />
        <KpiCard label="Sales registered" value={String(kpis.salesCount)} icon={<ReceiptText size={20} />} />
      </div>
      <section className="section-block">
        <div className="section-title">
          <h2>Recent ledger</h2>
          <a href={`/app/${organization.id}/transactions`}>Open explorer</a>
        </div>
        <LedgerTable transactions={transactions.slice(0, 3)} />
      </section>
    </AppShell>
  );
}
