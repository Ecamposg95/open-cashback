export type LedgerType = "EARNED" | "REDEEMED" | "REVERSED" | "BONUS" | "EXPIRED" | "ADJUSTED";

export const DEMO_ORG_ID = "11111111-1111-1111-1111-111111111111";
export const DEMO_BRANCH_ID = "22222222-2222-2222-2222-222222222222";
export const DEMO_CUSTOMER_ID = "33333333-3333-3333-3333-333333333333";

export const demoOrganization = {
  id: DEMO_ORG_ID,
  name: "Demo Merchant",
  cashbackRate: 0.01,
  currency: "MXN",
};

export const demoCustomer = {
  id: DEMO_CUSTOMER_ID,
  firstName: "Emmanuel",
  lastName: "Campos",
  email: "cliente@example.com",
  phone: "7221234567",
  status: "ACTIVE",
};

export const demoWallet = {
  id: "demo-wallet",
  availableBalance: 245,
  pendingBalance: 38,
  redeemedBalance: 80,
  expiredBalance: 10,
  lifetimeEarned: 335,
  lifetimeRedeemed: 80,
  status: "ACTIVE",
};

export const demoKpis = {
  salesCount: 42,
  customersCount: 18,
  cashbackIssued: 4280,
  cashbackRedeemed: 1315,
  outstandingLiability: 2965,
  redemptionRate: 31,
};

export const demoTransactions = [
  {
    id: "tx_001",
    type: "EARNED" as LedgerType,
    status: "AVAILABLE",
    amount: 10,
    reference: "TICKET-0001",
    createdAt: "2026-06-02T18:20:00Z",
    hash: "a93f4b8c1f3e3a4c93d7b9e0f5c1a9a6",
    previousHash: null,
  },
  {
    id: "tx_002",
    type: "BONUS" as LedgerType,
    status: "AVAILABLE",
    amount: 50,
    reference: "WELCOME-BONUS",
    createdAt: "2026-06-02T18:25:00Z",
    hash: "be17cf93ac204fcb8b799a2ea553019f",
    previousHash: "a93f4b8c1f3e3a4c93d7b9e0f5c1a9a6",
  },
  {
    id: "tx_003",
    type: "REDEEMED" as LedgerType,
    status: "REDEEMED",
    amount: -5,
    reference: "RED-8F2A91",
    createdAt: "2026-06-02T18:40:00Z",
    hash: "c20388ac84fb499b9fd8ac01694f3352",
    previousHash: "be17cf93ac204fcb8b799a2ea553019f",
  },
  {
    id: "tx_004",
    type: "REVERSED" as LedgerType,
    status: "REVERSED",
    amount: -10,
    reference: "TICKET-OLD-CANCELLED",
    createdAt: "2026-06-02T19:05:00Z",
    hash: "d87cab59ad89473680aafd35079f750e",
    previousHash: "c20388ac84fb499b9fd8ac01694f3352",
  },
];

export const demoCustomers = [
  { id: DEMO_CUSTOMER_ID, name: "Emmanuel Campos", email: "cliente@example.com", balance: 245, status: "ACTIVE" },
  { id: "cust_002", name: "Ana Lopez", email: "ana@example.com", balance: 120, status: "ACTIVE" },
  { id: "cust_003", name: "Carlos Ruiz", email: "carlos@example.com", balance: 0, status: "ACTIVE" },
  { id: "cust_004", name: "Maria Torres", email: "maria@example.com", balance: 510, status: "ACTIVE" },
];
