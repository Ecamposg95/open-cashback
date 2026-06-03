import {
  DEMO_BRANCH_ID,
  DEMO_CUSTOMER_ID,
  DEMO_ORG_ID,
  demoCustomer,
  demoCustomers,
  demoKpis,
  demoOrganization,
  demoTransactions,
  demoWallet,
  type LedgerType,
} from "./demoData";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000";

export type WalletView = typeof demoWallet;
export type CustomerView = typeof demoCustomer;
export type CustomerRow = (typeof demoCustomers)[number];
export type TransactionView = (typeof demoTransactions)[number];
export type KpiView = typeof demoKpis;

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    ...init,
    headers: {
      "Content-Type": "application/json",
      ...(init?.headers ?? {}),
    },
  });
  if (!response.ok) {
    throw new Error(`API ${response.status}: ${await response.text()}`);
  }
  return response.json() as Promise<T>;
}

function numberValue(value: unknown): number {
  if (typeof value === "number") return value;
  if (typeof value === "string") return Number(value);
  return 0;
}

function normalizeTransaction(item: any): TransactionView {
  return {
    id: item.id,
    type: item.transaction_type as LedgerType,
    status: item.status,
    amount: numberValue(item.amount),
    reference: item.reference ?? item.sale_id ?? item.redemption_id ?? "ledger",
    createdAt: item.created_at,
    hash: item.hash,
    previousHash: item.previous_hash,
  };
}

function normalizeWallet(item: any): WalletView {
  return {
    id: item.id,
    availableBalance: numberValue(item.available_balance),
    pendingBalance: numberValue(item.pending_balance),
    redeemedBalance: numberValue(item.redeemed_balance),
    expiredBalance: numberValue(item.expired_balance),
    lifetimeEarned: numberValue(item.lifetime_earned),
    lifetimeRedeemed: numberValue(item.lifetime_redeemed),
    status: item.status,
  };
}

function normalizeCustomer(item: any): CustomerView {
  return {
    id: item.id,
    firstName: item.first_name,
    lastName: item.last_name ?? "",
    email: item.email ?? "",
    phone: item.phone ?? "",
    status: item.status,
  };
}

export async function fetchCustomerPortalData() {
  try {
    const [customer, wallet, transactions] = await Promise.all([
      request<any>(`/api/v1/customers/${DEMO_CUSTOMER_ID}?organization_id=${DEMO_ORG_ID}`),
      request<any>(`/api/v1/customers/${DEMO_CUSTOMER_ID}/wallet?organization_id=${DEMO_ORG_ID}`),
      request<any[]>(`/api/v1/customers/${DEMO_CUSTOMER_ID}/transactions?organization_id=${DEMO_ORG_ID}`),
    ]);
    return {
      source: "api" as const,
      customer: normalizeCustomer(customer),
      wallet: normalizeWallet(wallet),
      transactions: transactions.map(normalizeTransaction),
    };
  } catch {
    return {
      source: "demo" as const,
      customer: demoCustomer,
      wallet: demoWallet,
      transactions: demoTransactions,
    };
  }
}

export async function fetchMerchantData() {
  try {
    const [summary, customers, transactions] = await Promise.all([
      request<any>(`/api/v1/reports/summary?organization_id=${DEMO_ORG_ID}`),
      request<any[]>(`/api/v1/customers?organization_id=${DEMO_ORG_ID}`),
      request<any[]>(`/api/v1/cashback/transactions?organization_id=${DEMO_ORG_ID}`),
    ]);
    const issued = numberValue(summary.cashback_issued);
    const redeemed = numberValue(summary.cashback_redeemed);
    return {
      source: "api" as const,
      organization: demoOrganization,
      kpis: {
        salesCount: numberValue(summary.sales_count),
        customersCount: numberValue(summary.customers_count),
        cashbackIssued: issued,
        cashbackRedeemed: redeemed,
        outstandingLiability: numberValue(summary.outstanding_liability),
        redemptionRate: issued > 0 ? Math.round((redeemed / issued) * 100) : 0,
      },
      customers: customers.map((customer) => ({
        id: customer.id,
        name: `${customer.first_name} ${customer.last_name ?? ""}`.trim(),
        email: customer.email ?? customer.phone ?? "",
        balance: 0,
        status: customer.status,
      })),
      transactions: transactions.map(normalizeTransaction),
    };
  } catch {
    return {
      source: "demo" as const,
      organization: demoOrganization,
      kpis: demoKpis,
      customers: demoCustomers,
      transactions: demoTransactions,
    };
  }
}

export async function registerDemoSale(eligibleAmount: number) {
  return request<any>("/api/v1/sales", {
    method: "POST",
    body: JSON.stringify({
      organization_id: DEMO_ORG_ID,
      branch_id: DEMO_BRANCH_ID,
      customer_id: DEMO_CUSTOMER_ID,
      external_sale_id: `TICKET-DEMO-${Date.now()}`,
      subtotal_amount: eligibleAmount.toFixed(2),
      discount_amount: "0.00",
      tax_amount: "0.00",
      total_amount: eligibleAmount.toFixed(2),
      eligible_amount: eligibleAmount.toFixed(2),
      paid_with_cashback_amount: "0.00",
      payment_method: "demo",
      items: [
        {
          sku: "SKU-DEMO-API",
          name: "Producto demo API",
          category: "General",
          quantity: "1",
          unit_price: eligibleAmount.toFixed(2),
          discount_amount: "0.00",
          total_amount: eligibleAmount.toFixed(2),
          eligible_for_cashback: true,
        },
      ],
    }),
  });
}

export async function loginDemoMerchant() {
  return request<{ access_token: string; token_type: string }>("/api/v1/auth/login", {
    method: "POST",
    body: JSON.stringify({
      email: "admin@demo.open-cashback.local",
      password: "demo1234",
      organization_id: DEMO_ORG_ID,
    }),
  });
}
