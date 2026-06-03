import { dateTime, money, shortHash } from "../lib/format";
import type { LedgerType } from "../lib/demoData";

type Tx = {
  id: string;
  type: LedgerType;
  status: string;
  amount: number;
  reference: string;
  createdAt: string;
  hash: string;
  previousHash: string | null;
};

export function LedgerTable({ transactions }: { transactions: Tx[] }) {
  return (
    <div className="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Type</th>
            <th>Amount</th>
            <th>Reference</th>
            <th>Status</th>
            <th>Hash</th>
            <th>Previous</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {transactions.map((tx) => (
            <tr key={tx.id}>
              <td><span className={`badge ${tx.type.toLowerCase()}`}>{tx.type}</span></td>
              <td className={tx.amount < 0 ? "negative" : "positive"}>{money(tx.amount)}</td>
              <td>{tx.reference}</td>
              <td>{tx.status}</td>
              <td><code>{shortHash(tx.hash)}</code></td>
              <td><code>{shortHash(tx.previousHash)}</code></td>
              <td>{dateTime(tx.createdAt)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
