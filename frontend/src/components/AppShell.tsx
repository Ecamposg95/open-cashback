import { BarChart3, Blocks, Gift, LayoutDashboard, ReceiptText, Settings, Users, Wallet } from "lucide-react";
import type { ReactNode } from "react";
import { DEMO_CUSTOMER_ID, DEMO_ORG_ID } from "../lib/demoData";

const merchantLinks = [
  { href: `/app/${DEMO_ORG_ID}/dashboard`, label: "Dashboard", icon: LayoutDashboard },
  { href: `/app/${DEMO_ORG_ID}/customers`, label: "Customers", icon: Users },
  { href: `/app/${DEMO_ORG_ID}/sales/new`, label: "POS simulator", icon: ReceiptText },
  { href: `/app/${DEMO_ORG_ID}/transactions`, label: "Ledger", icon: BarChart3 },
  { href: `/app/${DEMO_ORG_ID}/campaigns`, label: "Campaigns", icon: Gift },
  { href: `/app/${DEMO_ORG_ID}/blockchain`, label: "Web3 audit", icon: Blocks },
  { href: `/app/${DEMO_ORG_ID}/settings`, label: "Settings", icon: Settings },
];

const customerLinks = [
  { href: `/portal/${DEMO_ORG_ID}/customers/${DEMO_CUSTOMER_ID}`, label: "Wallet", icon: Wallet },
  { href: `/portal/${DEMO_ORG_ID}/customers/${DEMO_CUSTOMER_ID}/transactions`, label: "History", icon: ReceiptText },
  { href: `/portal/${DEMO_ORG_ID}/customers/${DEMO_CUSTOMER_ID}/redeem`, label: "Redeem", icon: Gift },
  { href: `/portal/${DEMO_ORG_ID}/customers/${DEMO_CUSTOMER_ID}/web3`, label: "Web3", icon: Blocks },
];

type AppShellProps = {
  mode: "merchant" | "customer";
  title: string;
  subtitle: string;
  dataSource?: "api" | "demo";
  children: ReactNode;
};

export function AppShell({ mode, title, subtitle, dataSource, children }: AppShellProps) {
  const links = mode === "merchant" ? merchantLinks : customerLinks;
  return (
    <div className="app-shell">
      <aside className="sidebar">
        <a className="brand" href={`/app/${DEMO_ORG_ID}/dashboard`}>
          <Wallet size={24} />
          <span>Open Cashback</span>
        </a>
        <nav>
          {links.map((link) => {
            const Icon = link.icon;
            return (
              <a href={link.href} key={link.href}>
                <Icon size={18} />
                {link.label}
              </a>
            );
          })}
        </nav>
        <div className="sidebar-footer">
          <a href={`/portal/${DEMO_ORG_ID}/customers/${DEMO_CUSTOMER_ID}`}>Customer portal</a>
          <a href={`/app/${DEMO_ORG_ID}/dashboard`}>Merchant app</a>
        </div>
      </aside>
      <main className="content">
        <header className="page-header">
          <div>
            <p>{mode === "merchant" ? "Merchant LaaS" : "Customer Portal"}</p>
            <h1>{title}</h1>
            <span>{subtitle}</span>
          </div>
          {dataSource ? <span className={`source-pill ${dataSource}`}>{dataSource === "api" ? "Live API" : "Demo fallback"}</span> : null}
        </header>
        {children}
      </main>
    </div>
  );
}
