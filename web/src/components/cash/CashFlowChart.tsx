import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Legend, ResponsiveContainer, Tooltip } from 'recharts';
import type { CashState } from '@/lib/types';

interface Row { month: string; income: number; expenses: number; savings: number; }

function rollup(cash: CashState): Row[] {
  const byMonth = new Map<string, Row>();
  for (const a of cash.accounts) {
    for (const m of a.monthly_summaries ?? []) {
      const prev = byMonth.get(m.month) ?? { month: m.month, income: 0, expenses: 0, savings: 0 };
      byMonth.set(m.month, {
        month: m.month,
        income: prev.income + m.total_income,
        expenses: prev.expenses + m.total_expenses,
        savings: prev.savings + m.savings,
      });
    }
  }
  return Array.from(byMonth.values()).sort((a, b) => a.month.localeCompare(b.month)).slice(-6);
}

export function CashFlowChart({ cash }: { cash: CashState }) {
  const data = rollup(cash);
  if (data.length === 0) {
    return <p className="text-sm text-muted-foreground">No monthly data.</p>;
  }
  return (
    <ResponsiveContainer width="100%" height={240}>
      <BarChart data={data}>
        <CartesianGrid strokeDasharray="3 3" stroke="var(--color-border)" />
        <XAxis dataKey="month" stroke="var(--color-muted-foreground)" fontSize={11} />
        <YAxis stroke="var(--color-muted-foreground)" fontSize={11} />
        <Tooltip
          contentStyle={{
            background: 'var(--color-card)',
            border: '1px solid var(--color-border)',
            color: 'var(--color-foreground)',
          }}
        />
        <Legend wrapperStyle={{ fontSize: 11 }} />
        <Bar dataKey="income" fill="var(--color-positive)" />
        <Bar dataKey="expenses" fill="var(--color-destructive)" />
        <Bar dataKey="savings" fill="var(--color-primary)" />
      </BarChart>
    </ResponsiveContainer>
  );
}
