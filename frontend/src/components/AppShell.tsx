import { BarChart3, Blocks, Gift, LayoutDashboard, ReceiptText, Settings, Users, Wallet } from "lucide-react";
import type { ReactNode } from "react";

const merchantLinks = [
  { href: "/app/demo-org/dashboard", label: "Dashboard", icon: LayoutDashboard },
  { href: "/app/demo-org/customers", label: "Customers", icon: Users },
  { href: "/app/demo-org/sales/new", label: "POS simulator", icon: ReceiptText },
  { href: "/app/demo-org/transactions", label: "Ledger", icon: BarChart3 },
  { href: "/app/demo-org/campaigns", label: "Campaigns", icon: Gift },
  { href: "/app/demo-org/blockchain", label: "Web3 audit", icon: Blocks },
  { href: "/app/demo-org/settings", label: "Settings", icon: Settings },
];

const customerLinks = [
  { href: "/portal/demo-org/customers/demo-customer", label: "Wallet", icon: Wallet },
  { href: "/portal/demo-org/customers/demo-customer/transactions", label: "History", icon: ReceiptText },
  { href: "/portal/demo-org/customers/demo-customer/redeem", label: "Redeem", icon: Gift },
  { href: "/portal/demo-org/customers/demo-customer/web3", label: "Web3", icon: Blocks },
];

type AppShellProps = {
  mode: "merchant" | "customer";
  title: string;
  subtitle: string;
  children: ReactNode;
};

export function AppShell({ mode, title, subtitle, children }: AppShellProps) {
  const links = mode === "merchant" ? merchantLinks : customerLinks;
  return (
    <div className="app-shell">
      <aside className="sidebar">
        <a className="brand" href="/app/demo-org/dashboard">
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
          <a href="/portal/demo-org/customers/demo-customer">Customer portal</a>
          <a href="/app/demo-org/dashboard">Merchant app</a>
        </div>
      </aside>
      <main className="content">
        <header className="page-header">
          <div>
            <p>{mode === "merchant" ? "Merchant LaaS" : "Customer Portal"}</p>
            <h1>{title}</h1>
            <span>{subtitle}</span>
          </div>
        </header>
        {children}
      </main>
    </div>
  );
}
