import type {
  Profile,
  CashState,
  PortfolioState,
  InsuranceState,
  TaxState,
  CryptoSummary,
  CashAccount,
  Broker,
} from './types';

export interface LoadedState {
  profile: Profile | null;
  cash: CashState | null;
  portfolio: PortfolioState | null;
  insurance: InsuranceState | null;
  tax: TaxState | null;
  crypto: CryptoSummary | null;
}

// ---------- helpers ----------

function latestBalance(account: CashAccount): number {
  const b = account.balances;
  if (!b || b.length === 0) return 0;
  return b[b.length - 1].balance ?? 0;
}

function latestSnapshotValue(broker: Broker): number {
  const snaps = broker.portfolio_snapshots;
  if (snaps && snaps.length > 0) return snaps[snaps.length - 1].total_value ?? 0;
  const stmts = broker.annual_statements;
  if (stmts && stmts.length > 0) {
    const last = stmts[stmts.length - 1];
    const v = (last.portfolio_value_year_end ?? last.account_value_year_end ?? last.total_portfolio_value) as number | undefined;
    return typeof v === 'number' ? v : 0;
  }
  return 0;
}

// ---------- computeNetWorth ----------

export interface NetWorth {
  total: number;
  cash: number;
  investments: number;
  pension: number;
}

export function computeNetWorth(state: LoadedState): NetWorth {
  const cash = (state.cash?.accounts ?? [])
    .filter(a => a.status !== 'closed')
    .reduce((sum, a) => sum + latestBalance(a), 0);

  const investments = (state.portfolio?.brokers ?? [])
    .reduce((sum, b) => sum + latestSnapshotValue(b), 0);

  const pension = state.profile?.pension?.current_value ?? 0;

  return { total: cash + investments + pension, cash, investments, pension };
}

// ---------- computeCashFlow ----------

export interface CashFlow {
  avgIncome: number;
  avgExpenses: number;
  avgSavings: number;
  savingsRate: number;
}

export function computeCashFlow(cash: CashState | null): CashFlow | null {
  if (!cash) return null;
  const byMonth = new Map<string, { income: number; expenses: number; savings: number }>();
  for (const a of cash.accounts) {
    for (const m of a.monthly_summaries ?? []) {
      const prev = byMonth.get(m.month) ?? { income: 0, expenses: 0, savings: 0 };
      byMonth.set(m.month, {
        income: prev.income + m.total_income,
        expenses: prev.expenses + m.total_expenses,
        savings: prev.savings + m.savings,
      });
    }
  }
  if (byMonth.size === 0) return null;

  const months = Array.from(byMonth.keys()).sort().slice(-3);
  if (months.length === 0) return null;

  const sums = months.reduce(
    (acc, m) => {
      const s = byMonth.get(m)!;
      acc.income += s.income;
      acc.expenses += s.expenses;
      acc.savings += s.savings;
      return acc;
    },
    { income: 0, expenses: 0, savings: 0 },
  );

  const avgIncome = sums.income / months.length;
  const avgExpenses = sums.expenses / months.length;
  const avgSavings = sums.savings / months.length;
  const savingsRate = avgIncome > 0 ? (avgSavings / avgIncome) * 100 : 0;

  return { avgIncome, avgExpenses, avgSavings, savingsRate };
}

// ---------- computeEmergencyFund ----------

export interface EmergencyFund {
  liquidCash: number;
  monthlyExpenses: number;
  coverageMonths: number;
  targetMonths: number;
  gap: number;
}

export function computeEmergencyFund(state: LoadedState): EmergencyFund | null {
  if (!state.cash) return null;

  const liquidCash = state.cash.accounts
    .filter(a => a.status !== 'closed' && (a.account_type === 'girokonto' || a.account_type === 'tagesgeld'))
    .reduce((sum, a) => sum + latestBalance(a), 0);

  const flow = computeCashFlow(state.cash);
  if (!flow || flow.avgExpenses === 0) return null;

  const monthlyExpenses = flow.avgExpenses;
  const coverageMonths = liquidCash / monthlyExpenses;
  const hasChildren = (state.profile?.children ?? []).length > 0;
  const targetMonths = hasChildren ? 6 : 3;
  const gap = Math.max(0, targetMonths * monthlyExpenses - liquidCash);

  return { liquidCash, monthlyExpenses, coverageMonths, targetMonths, gap };
}

// ---------- computeIdleCash ----------

export interface IdleCash {
  idleAccounts: Array<{ bank: string; owner: string; balance: number; annualMissed: number }>;
  opportunityCostAnnual: number;
}

export function computeIdleCash(cash: CashState | null): IdleCash {
  if (!cash) return { idleAccounts: [], opportunityCostAnnual: 0 };

  const rates = cash.accounts
    .map(a => a.interest?.[a.interest.length - 1]?.interest_rate_pct ?? 0)
    .filter(r => r > 0);
  const bestRate = rates.length > 0 ? Math.max(...rates) : 0;

  const idleAccounts = cash.accounts
    .filter(a => {
      const latestInterest = a.interest?.[a.interest.length - 1];
      return (
        a.status !== 'closed' &&
        latestBalance(a) > 0 &&
        (latestInterest?.interest_rate_pct ?? 0) === 0
      );
    })
    .map(a => {
      const balance = latestBalance(a);
      return {
        bank: a.bank,
        owner: a.owner,
        balance,
        annualMissed: balance * (bestRate / 100),
      };
    });

  const opportunityCostAnnual = idleAccounts.reduce((s, a) => s + a.annualMissed, 0);
  return { idleAccounts, opportunityCostAnnual };
}

// ---------- computeSpbUsage ----------

export interface SpbUsage {
  used: number;
  allowance: number;
  remaining: number;
  bankInterestYtd: number;
  portfolioSpbUsed: number;
}

export function computeSpbUsage(state: LoadedState): SpbUsage {
  const year = new Date().getFullYear();

  const bankInterestYtd = (state.cash?.accounts ?? [])
    .flatMap(a => a.interest ?? [])
    .filter(i => i.year === year)
    .reduce((s, i) => s + (i.total_interest_earned ?? 0), 0);

  const portfolioSpbUsed = state.portfolio?.tax_year_summary?.sparerpauschbetrag_used ?? 0;
  const used = bankInterestYtd + portfolioSpbUsed;

  const allowance = state.profile?.filing_status === 'zusammenveranlagung' ? 2000 : 1000;
  const remaining = allowance - used;

  return { used, allowance, remaining, bankInterestYtd, portfolioSpbUsed };
}

// ---------- computeTaxReadiness ----------

export type Readiness = 'yes' | 'no' | 'partial';

export interface TaxReadiness {
  income: Readiness;
  investments: Readiness;
  bankInterest: Readiness;
  insurancePremiums: Readiness;
  profileComplete: Readiness;
}

export function computeTaxReadiness(state: LoadedState): TaxReadiness {
  const year = new Date().getFullYear();
  const prevYear = year - 1;

  const income: Readiness = (() => {
    const persons = state.tax?.persons;
    if (!persons || persons.length === 0) return 'no';
    const anyEmployers = persons.some(p => (p.employers?.length ?? 0) > 0);
    return anyEmployers ? 'yes' : 'partial';
  })();

  const investments: Readiness = (() => {
    const brokers = state.portfolio?.brokers ?? [];
    if (brokers.length === 0) return 'no';
    const withStmts = brokers.filter(b => (b.annual_statements?.length ?? 0) > 0);
    if (withStmts.length === brokers.length) return 'yes';
    if (withStmts.length > 0) return 'partial';
    return 'no';
  })();

  const bankInterest: Readiness = (() => {
    const accounts = state.cash?.accounts ?? [];
    const entries = accounts.flatMap(a => a.interest ?? []).filter(i => i.year === prevYear || i.year === year);
    return entries.length > 0 ? 'yes' : 'no';
  })();

  const insurancePremiums: Readiness = (() => {
    const policies = state.insurance?.policies ?? [];
    const withPremium = policies.filter(p => (p.annual_premium ?? 0) > 0);
    if (policies.length === 0) return 'no';
    return withPremium.length > 0 ? 'yes' : 'partial';
  })();

  const profileComplete: Readiness = (() => {
    const p = state.profile;
    if (!p) return 'no';
    const hasTaxClass = p.persons.every(person => typeof person.tax_class === 'number');
    const hasFiling = typeof p.filing_status === 'string';
    const hasIncome = p.persons.every(person => typeof person.gross_annual_salary === 'number');
    if (hasTaxClass && hasFiling && hasIncome) return 'yes';
    if (hasTaxClass || hasFiling || hasIncome) return 'partial';
    return 'no';
  })();

  return { income, investments, bankInterest, insurancePremiums, profileComplete };
}

// ---------- priority actions ----------

export interface PriorityAction {
  severity: 'high' | 'medium' | 'low';
  title: string;
  detail: string;
  amountEur?: number;
}

export function computePriorityActions(state: LoadedState): PriorityAction[] {
  const actions: PriorityAction[] = [];

  const ef = computeEmergencyFund(state);
  if (ef && ef.gap > 0) {
    actions.push({
      severity: 'high',
      title: `Emergency fund ${ef.gap.toFixed(0)} € short of ${ef.targetMonths}-month target`,
      detail: `Target ${(ef.targetMonths * ef.monthlyExpenses).toFixed(0)} € · current ${ef.liquidCash.toFixed(0)} €`,
      amountEur: ef.gap,
    });
  }

  const idle = computeIdleCash(state.cash);
  if (idle.opportunityCostAnnual > 100) {
    actions.push({
      severity: 'medium',
      title: `Idle cash costing ${idle.opportunityCostAnnual.toFixed(0)} €/year`,
      detail: `${idle.idleAccounts.length} account(s) at 0 %`,
      amountEur: idle.opportunityCostAnnual,
    });
  }

  const spb = computeSpbUsage(state);
  const monthOfYear = new Date().getMonth();
  if (monthOfYear >= 6 && spb.remaining > 500) {
    actions.push({
      severity: 'medium',
      title: `${spb.remaining.toFixed(0)} € Sparerpauschbetrag unused`,
      detail: 'Consider realizing gains before year-end',
      amountEur: spb.remaining,
    });
  }

  const tr = computeTaxReadiness(state);
  const missing = Object.entries(tr).filter(([, v]) => v === 'no').map(([k]) => k);
  if (missing.length > 0) {
    actions.push({
      severity: 'low',
      title: `Tax readiness: ${missing.length} domain(s) missing`,
      detail: missing.join(', '),
    });
  }

  return actions.slice(0, 5);
}
