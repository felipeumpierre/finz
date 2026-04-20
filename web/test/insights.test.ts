import { describe, expect, test } from 'bun:test';
import {
  computeNetWorth,
  computeCashFlow,
  computeEmergencyFund,
  computeIdleCash,
  computeSpbUsage,
  computeTaxReadiness,
  type LoadedState,
} from '../src/lib/insights';

import full from './fixtures/full.json';
import singlePerson from './fixtures/single-person.json';
import missing from './fixtures/missing.json';

const cast = (s: unknown) => s as LoadedState;

describe('computeNetWorth', () => {
  test('sums latest cash balances + latest broker snapshot values', () => {
    const r = computeNetWorth(cast(full));
    expect(r.total).toBe(77000);
    expect(r.cash).toBe(27000);
    expect(r.investments).toBe(50000);
    expect(r.pension).toBe(0);
  });

  test('returns zeros when all state missing', () => {
    const r = computeNetWorth(cast(missing));
    expect(r.total).toBe(0);
  });
});

describe('computeCashFlow', () => {
  test('averages last 3 monthly summaries and computes savings rate', () => {
    const r = computeCashFlow(cast(full).cash!);
    expect(r!.avgIncome).toBeCloseTo(8000);
    expect(r!.avgExpenses).toBeCloseTo(5500);
    expect(r!.avgSavings).toBeCloseTo(2500);
    expect(r!.savingsRate).toBeCloseTo(31.25, 1);
  });

  test('returns null when cash is null', () => {
    expect(computeCashFlow(null)).toBeNull();
  });
});

describe('computeEmergencyFund', () => {
  test('target=6mo for households with children; gap accounts for target', () => {
    const r = computeEmergencyFund(cast(full));
    expect(r!.liquidCash).toBe(27000);
    expect(r!.coverageMonths).toBeCloseTo(4.91, 1);
    expect(r!.targetMonths).toBe(6);
    expect(r!.gap).toBe(6000);
  });

  test('returns null when cash data unavailable', () => {
    const r = computeEmergencyFund(cast(singlePerson));
    expect(r).toBeNull();
  });
});

describe('computeIdleCash', () => {
  test('identifies 0% accounts with positive balance and computes opportunity cost', () => {
    const r = computeIdleCash(cast(full).cash!);
    expect(r.idleAccounts).toHaveLength(1);
    expect(r.idleAccounts[0].bank).toBe('DB');
    expect(r.opportunityCostAnnual).toBe(375);
  });
});

describe('computeSpbUsage', () => {
  test('uses 2000 € allowance for zusammenveranlagung', () => {
    const r = computeSpbUsage(cast(full));
    expect(r.used).toBe(620);
    expect(r.allowance).toBe(2000);
    expect(r.remaining).toBe(1380);
  });

  test('uses 1000 € allowance for einzelveranlagung', () => {
    const r = computeSpbUsage(cast(singlePerson));
    expect(r.allowance).toBe(1000);
    expect(r.used).toBe(200);
    expect(r.remaining).toBe(800);
  });
});

describe('computeTaxReadiness', () => {
  test('returns "yes" for each captured domain', () => {
    const r = computeTaxReadiness(cast(full));
    expect(r.income).toBe('yes');
    expect(r.investments).toBe('yes');
    expect(r.bankInterest).toBe('yes');
    expect(r.insurancePremiums).toBe('yes');
    expect(r.profileComplete).toBe('yes');
  });

  test('returns "no" everywhere when state missing', () => {
    const r = computeTaxReadiness(cast(missing));
    expect(r.income).toBe('no');
    expect(r.investments).toBe('no');
    expect(r.bankInterest).toBe('no');
    expect(r.insurancePremiums).toBe('no');
    expect(r.profileComplete).toBe('no');
  });
});
