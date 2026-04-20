---
name: steuer-documents
description: >
  Generate personalized document checklists for a German tax declaration (Steuererklärung). Use this
  skill after the user's income and deductions have been identified (via steuer-intake and
  steuer-deductions). It tells the user exactly which documents they need, where to find or request
  each one, what to keep for their records vs. what to submit, and key deadlines. Trigger when the
  user asks about Belege, Nachweise, Unterlagen, what documents they need, or where to find a
  specific tax document.
---

# Steuer Documents — Checklist & Document Finder

This skill generates a personalized document checklist based on the user's specific tax situation. It explains where to get each document, whether it needs to be submitted or just kept, and what to do if it's missing.

## Important Context: Belegvorhaltepflicht

Since 2017, Germany has a **Belegvorhaltepflicht** system — you do NOT submit most documents proactively. Instead, you keep them and submit only if the Finanzamt requests them (which they may do within a certain period). However, some documents still need to be submitted or are transmitted electronically.

## Document Categories

### Always Required (Basis Documents)

**Lohnsteuerbescheinigung(en)**
- Source: Your employer issues this by end of February for the previous year
- Format: Paper or electronic (your employer transmits the data to the Finanzamt electronically via eDaten)
- Action: **Keep** — The Finanzamt already has this data electronically. You only need it for your own records and to verify the numbers
- If missing: Contact your employer's HR/payroll department (Lohnbüro/Personalabteilung). They must issue it. If the employer no longer exists, contact the Finanzamt — they have the electronically transmitted data

**Steuerbescheid from previous year**
- Source: Your Finanzamt sent this after processing your last tax return
- Action: **Keep** — Useful for reference (Verlustvortrag, carried-forward losses, etc.)
- If missing: You can request a copy from your Finanzamt

**Steuer-Identifikationsnummer (IdNr)**
- Source: Issued at birth or upon registration in Germany (Bundeszentralamt für Steuern)
- Action: You need this for filing — it's on your Steuerbescheid, Lohnsteuerbescheinigung, or the original letter from BZSt
- If missing: Request at https://www.bzst.de or call BZSt. Takes 4-6 weeks by post

### Income Documents

**Freelance / Self-Employment Income**
- What: Einnahmenüberschussrechnung (EÜR) — a profit/loss calculation
- Source: You create this yourself from your records (invoices, receipts, bank statements)
- Action: **Submit** (Anlage EÜR is mandatory for freelance income)
- Supporting docs: All invoices, receipts, bank statements — **Keep** for 10 years (Aufbewahrungspflicht)
- Tools: ELSTER has a built-in EÜR form, or use accounting software (e.g., SevDesk, lexoffice, FastBill)

**Capital Gains / Investment Income**
- What: Jahressteuerbescheinigung from your bank
- Source: Your bank issues this automatically (usually by March/April)
- Action: **Keep** — Only submit if claiming Günstigerprüfung or if taxes were not properly withheld
- If missing: Download from your online banking portal or request from your bank
- Note: If you have accounts at multiple banks, you need one from each

**Rental Income**
- What: Rental agreements, Nebenkostenabrechnung, receipts for repairs/maintenance, loan interest statements, depreciation schedule
- Source: Your own records, property management company, bank (for mortgage interest)
- Action: **Keep** all, submit Anlage V with calculated numbers

### Deduction Documents

**Commuting (Entfernungspauschale)**
- What: No specific document needed — you just need to know the distance and number of days
- Useful: Google Maps screenshot of route, calendar showing office days, employer attestation of on-site days
- If home office days are relevant: Keep a log or have employer confirm hybrid work arrangement
- Action: **Keep** — only submit if Finanzamt asks

**Home Office**
- What: Record of days worked from home
- Useful: Calendar entries, employer home office agreement, time tracking system exports
- Action: **Keep**

**Work Equipment**
- What: Receipts/invoices (Rechnungen) for each item
- Source: Retailers, online shops — check your email for digital receipts
- Action: **Keep** — receipts should show date, item, amount, and your name/address
- If missing: Check email (Amazon, etc.), credit card statements, bank statements as circumstantial evidence

**Professional Training**
- What: Invoices, certificates of attendance, travel receipts
- Source: Training providers, conference organizers
- Action: **Keep**

**Donations (Spenden)**
- What: Zuwendungsbestätigung (donation receipt) from the organization
- Source: The charity/organization issues this — often automatically, sometimes on request
- Action: **Keep** — For donations under 300€, a bank statement showing the transfer is sufficient (Vereinfachter Nachweis)
- For political parties: Zuwendungsbestätigung is always needed
- If missing: Contact the organization and ask for a Zuwendungsbestätigung

**Insurance (Vorsorgeaufwendungen)**
- What: Contribution confirmations (Beitragsbescheinigungen)
- Source: Insurance companies send these annually (often by February)
- Private health insurance: §10 Abs. 1 Nr. 3 Bescheinigung (shows Basisbeiträge separately)
- Riester: Anbieterbescheinigung — your Riester provider transmits data electronically (you need Zulagenummer)
- Rürup: Provider sends Beitragsbescheinigung
- Action: **Keep** — most data is transmitted electronically by providers

**Childcare Costs (Kinderbetreuungskosten)**
- What: Contract with provider + proof of payment by bank transfer
- Source: Kita/daycare contract, invoices from Tagesmutter, Au-pair contract
- Action: **Keep** — You need the provider's tax ID or Steuernummer
- Critical: Cash payments are NOT deductible! Must be bank transfer (Überweisung)
- If missing: Request duplicate invoices from the childcare provider. Bank statements show payments

**Haushaltsnahe Dienstleistungen / Handwerkerleistungen**
- What: Invoice (Rechnung) showing labor costs separately + proof of bank transfer payment
- Source: Service provider, craftsman
- Action: **Keep**
- Critical: Invoice MUST break out labor vs. materials. Cash payments are NOT deductible
- Nebenkostenabrechnung: Your landlord's annual utility bill often contains deductible amounts (Hausmeister, Gartenpflege, Schornsteinfeger, Aufzugswartung, etc.) — look for "§35a" or "haushaltsnahe" items
- If missing: Ask the craftsman/service provider for a duplicate invoice

**Medical Expenses (Außergewöhnliche Belastungen)**
- What: Receipts, prescriptions, doctor's attestations
- Source: Pharmacies, doctors, hospitals, opticians
- Action: **Keep** — Collect throughout the year. Only worth it if total exceeds zumutbare Belastung
- Useful: Prescription from doctor (for medications, therapies), Heil- und Kostenplan (for dental work)

**Disability (Behinderung)**
- What: Schwerbehindertenausweis or Feststellungsbescheid from Versorgungsamt
- Source: Versorgungsamt / Landesamt für Gesundheit und Soziales
- Action: **Keep** — Once filed, usually doesn't need to be resubmitted annually
- If not yet applied: Application at the local Versorgungsamt. Process takes 3-6 months

### Children Documents

**Per child, collect:**
- Birth certificate (Geburtsurkunde) — only needed on first filing
- Steuer-Identifikationsnummer of the child
- Kindergeld-Bescheid or confirmation of Kindergeld receipt (Familienkasse)
- If child is 18+: Proof of studies/training (Ausbildungsnachweis) or voluntary service confirmation

## Generating the Checklist

Based on the user's captured income and deductions, generate a personalized checklist. Format:

```
═══ Document Checklist: Steuererklärung 2025 ═══
═══ Max & Erika Mustermann                    ═══

STATUS LEGEND: ✅ Have it  ⬜ Need to get  📧 Request it  🔄 Transmitted electronically

BASIS DOCUMENTS
  ⬜ Lohnsteuerbescheinigung — Max (Muster GmbH)
      → 🔄 Data transmitted electronically by employer
      → Keep paper/PDF copy for your records
  ⬜ Lohnsteuerbescheinigung — Erika (Beispiel AG)
      → 🔄 Data transmitted electronically by employer

DEDUCTION DOCUMENTS
  ⬜ Commuting record — Max
      → Note: 25 km one-way, 210 days. Keep calendar/log as evidence
  ⬜ Home office log — Max
      → Note: 45 days. Keep calendar entries
  ⬜ Receipt: Laptop purchase — Max
      → Check email for digital receipt (Amazon, retailer)
      → Shows 1,200€ gross, claiming 80% = 960€
  ⬜ Training course invoice — Max
      → Request from: [training provider]
  ⬜ Union dues confirmation — Max
      → Source: IG Metall / ver.di sends annual Beitragsbescheinigung
  ⬜ Donation receipt(s) — Joint
      → 📧 Request Zuwendungsbestätigung from: [charity name]
      → Under 300€: bank statement is sufficient
  ⬜ Riester-Anbieterbescheinigung — Max
      → 🔄 Provider transmits electronically
      → You need your Zulagenummer
  ⬜ Kita invoice + bank transfer proof — Joint
      → Source: [Kita name]
      → Shows 3,600€/year. Must prove payment via bank transfer
  ⬜ Cleaning service invoices — Joint
      → 12 monthly invoices showing labor costs separately
      → Proof of bank transfer for each
  ⬜ Handwerker invoice (bathroom) — Joint
      → Must show labor (1,800€) vs. materials separately

DEADLINES
  📅 Regular filing deadline: 31. Juli 2026 (for tax year 2025)
  📅 With Steuerberater: 30. April 2027 (extended deadline)
  📅 Voluntary filing (no obligation): up to 4 years retroactively
```

## Proactive Suggestions

After generating the checklist, proactively suggest:

1. **Nebenkostenabrechnung check**: "If you rent, check your most recent Nebenkostenabrechnung for §35a items — this is free money many people miss."
2. **Digital receipt search**: "Search your email for receipts from Amazon, MediaMarkt, etc. for any work equipment you may have forgotten."
3. **Bank statement review**: "Your bank statements can help you find forgotten donations, insurance payments, or professional memberships."
4. **Employer attestation**: "If your employer offers hybrid work, ask HR for a written confirmation of your office/home split — this helps with both commuting and home office deductions."
