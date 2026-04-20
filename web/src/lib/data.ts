import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import type {
  Profile,
  CashState,
  PortfolioState,
  InsuranceState,
  TaxState,
  CryptoSummary,
} from './types';

// Resolve workspace/ relative to this module.
// This file sits at web/src/lib/data.ts — three levels up gets us to the finz root.
const __dirname = dirname(fileURLToPath(import.meta.url));
const WORKSPACE = join(__dirname, '..', '..', '..', 'workspace');

function loadJson<T>(filename: string): T | null {
  const path = join(WORKSPACE, filename);
  try {
    const raw = readFileSync(path, 'utf-8');
    return JSON.parse(raw) as T;
  } catch (err: unknown) {
    if (isENOENT(err)) return null;
    throw new Error(`Failed to load ${filename}: ${(err as Error).message}`);
  }
}

function isENOENT(err: unknown): boolean {
  return typeof err === 'object' && err !== null && (err as { code?: string }).code === 'ENOENT';
}

export function loadProfile(): Profile | null {
  return loadJson<Profile>('profile.json');
}

export function loadCash(): CashState | null {
  return loadJson<CashState>('cash-state.json');
}

export function loadPortfolio(): PortfolioState | null {
  return loadJson<PortfolioState>('portfolio-state.json');
}

export function loadInsurance(): InsuranceState | null {
  return loadJson<InsuranceState>('insurance-state.json');
}

export function loadTax(): TaxState | null {
  return loadJson<TaxState>('tax-state.json');
}

export function loadCryptoSummary(): CryptoSummary | null {
  return loadJson<CryptoSummary>('crypto-summary.json');
}

export function loadAll(): LoadedState {
  return {
    profile: loadProfile(),
    cash: loadCash(),
    portfolio: loadPortfolio(),
    insurance: loadInsurance(),
    tax: loadTax(),
    crypto: loadCryptoSummary(),
  };
}

export type { LoadedState } from './insights';
import type { LoadedState } from './insights';
