import type { ReactNode } from "react";

type Props = {
  label: string;
  value: string;
  helper?: string;
  icon?: ReactNode;
};

export function KpiCard({ label, value, helper, icon }: Props) {
  return (
    <section className="kpi-card">
      <div className="kpi-icon">{icon}</div>
      <p>{label}</p>
      <strong>{value}</strong>
      {helper ? <span>{helper}</span> : null}
    </section>
  );
}
