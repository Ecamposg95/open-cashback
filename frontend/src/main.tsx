import React from "react";
import { createRoot } from "react-dom/client";
import { CustomerPortal } from "./features/customer/CustomerPortal";
import { MerchantDashboard } from "./features/merchant/MerchantDashboard";
import "./styles.css";

function resolveRoute() {
  const path = window.location.pathname;

  if (path.includes("/portal/") && path.endsWith("/transactions")) return <CustomerPortal page="transactions" />;
  if (path.includes("/portal/") && path.endsWith("/redeem")) return <CustomerPortal page="redeem" />;
  if (path.includes("/portal/") && path.endsWith("/web3")) return <CustomerPortal page="web3" />;
  if (path.startsWith("/portal")) return <CustomerPortal page="dashboard" />;

  if (path.includes("/customers")) return <MerchantDashboard page="customers" />;
  if (path.includes("/sales/new")) return <MerchantDashboard page="sales" />;
  if (path.includes("/transactions")) return <MerchantDashboard page="ledger" />;
  if (path.includes("/campaigns")) return <MerchantDashboard page="campaigns" />;
  if (path.includes("/blockchain")) return <MerchantDashboard page="blockchain" />;
  if (path.includes("/settings")) return <MerchantDashboard page="settings" />;
  return <MerchantDashboard page="dashboard" />;
}

createRoot(document.getElementById("root")!).render(<React.StrictMode>{resolveRoute()}</React.StrictMode>);
