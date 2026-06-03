import React from "react";
import { createRoot } from "react-dom/client";
import { Wallet, ReceiptText, ShieldCheck } from "lucide-react";
import "./styles.css";

function App() {
  return (
    <main className="shell">
      <section className="panel">
        <div className="brand"><Wallet size={28} /> Open Cashback</div>
        <h1>Cashback, wallet y ledger auditable para POS/ERP.</h1>
        <div className="grid">
          <div><ReceiptText /> Ledger interno PostgreSQL primero.</div>
          <div><ShieldCheck /> Hashes y anchoring Web3 preparado.</div>
        </div>
      </section>
    </main>
  );
}

createRoot(document.getElementById("root")!).render(<App />);
