export function money(value: number, currency = "MXN") {
  return new Intl.NumberFormat("es-MX", {
    style: "currency",
    currency,
    minimumFractionDigits: 2,
  }).format(value);
}

export function shortHash(value: string | null) {
  if (!value) return "Genesis";
  return `${value.slice(0, 8)}...${value.slice(-6)}`;
}

export function dateTime(value: string) {
  return new Intl.DateTimeFormat("es-MX", {
    dateStyle: "medium",
    timeStyle: "short",
  }).format(new Date(value));
}
