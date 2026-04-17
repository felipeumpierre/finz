# §32a EStG Tax Formula Coefficients

**Last verified:** 2026-04-17
**Primary source:** Amtliches Lohnsteuer-Handbuch / Einkommensteuer-Handbuch (BMF), per tax year
**Scope:** Single-person tariff. For jointly assessed couples apply the Splittingverfahren: compute tax on zvE/2, then double.

---

## Formula structure (stable across all years)

The §32a tariff has five zones:

1. **Nullzone (Grundfreibetrag):** `tax = 0` up to the Grundfreibetrag.
2. **Progressionszone 1:** quadratic in `y`, where `y = (zvE - Grundfreibetrag) / 10000`.
3. **Progressionszone 2:** quadratic in `z`, where `z = (zvE - upper_P1) / 10000`, plus a constant.
4. **Proportionalzone 1 (42%):** linear in `x = zvE`, with a constant subtraction.
5. **Proportionalzone 2 / Reichensteuer (45%):** linear in `x`, with a larger constant subtraction.

The result is rounded **down** to full euros (Abrundung auf den nächsten vollen Euro; see §32a Abs. 1 Satz 6 EStG).

---

## Tax Year 2023

**Grundfreibetrag:** 10,908 EUR
**Upper edge of Progressionszone 1:** 15,999 EUR
**42% threshold:** 62,810 EUR
**45% threshold:** 277,826 EUR
**Source:** [BMF EStH 2023 §32a](https://esth.bundesfinanzministerium.de/lsth/2023/A-Einkommensteuergesetz/IV-Tarif/Paragraf-32a/inhalt.html) — retrieved 2026-04-17

Formula (official verbatim coefficients):

```
if  zvE <=    10,908: tax = 0
elif zvE <=  15,999: y = (zvE - 10908) / 10000; tax = (979.18 * y + 1400) * y
elif zvE <=  62,809: z = (zvE - 15999) / 10000; tax = (192.59 * z + 2397) * z + 966.53
elif zvE <= 277,825: tax = 0.42 * zvE - 9972.98
else:                tax = 0.45 * zvE - 18307.73
tax = floor(tax)    # round down to full euros
```

---

## Tax Year 2024

**Grundfreibetrag:** 11,784 EUR
**Upper edge of Progressionszone 1:** 17,005 EUR
**42% threshold:** 66,761 EUR
**45% threshold:** 277,826 EUR
**Source:** [BMF EStH 2024 §32a](https://esth.bundesfinanzministerium.de/esth/2024/A-Einkommensteuergesetz/IV-Tarif-31-34b/Paragraf-32a/inhalt.html) — retrieved 2026-04-17

Formula:

```
if  zvE <=    11,784: tax = 0
elif zvE <=  17,005: y = (zvE - 11784) / 10000; tax = (954.80 * y + 1400) * y
elif zvE <=  66,760: z = (zvE - 17005) / 10000; tax = (181.19 * z + 2397) * z + 991.21
elif zvE <= 277,825: tax = 0.42 * zvE - 10636.31
else:                tax = 0.45 * zvE - 18971.06
tax = floor(tax)
```

Note: The 2024 figures above reflect the retroactive increase enacted via the Steuerfortentwicklungsgesetz (Dec 2024) — the originally enacted 2024 Grundfreibetrag was 11,604 EUR and was raised to 11,784 EUR. Filings already assessed at the lower value receive an automatic adjustment.

---

## Tax Year 2025

**Grundfreibetrag:** 12,096 EUR
**Upper edge of Progressionszone 1:** 17,443 EUR
**42% threshold:** 68,481 EUR
**45% threshold:** 277,826 EUR
**Source:** [BMF LStH 2025 §32a](https://lsth.bundesfinanzministerium.de/lsth/2025/A-Einkommensteuergesetz/IV-Tarif-31-34b/Paragraf-32a/inhalt.html) — retrieved 2026-04-17

Formula:

```
if  zvE <=    12,096: tax = 0
elif zvE <=  17,443: y = (zvE - 12096) / 10000; tax = (932.30 * y + 1400) * y
elif zvE <=  68,480: z = (zvE - 17443) / 10000; tax = (176.64 * z + 2397) * z + 1015.13
elif zvE <= 277,825: tax = 0.42 * zvE - 10911.92
else:                tax = 0.45 * zvE - 19246.67
tax = floor(tax)
```

---

## Tax Year 2026

**Grundfreibetrag:** 12,348 EUR
**Upper edge of Progressionszone 1:** 17,799 EUR
**42% threshold:** 69,879 EUR
**45% threshold:** 277,826 EUR
**Source:** [BMF LStH 2026 §32a](https://lsth.bundesfinanzministerium.de/lsth/2026/A-Einkommensteuergesetz/IV-Tarif-31-34b/Paragraf-32a/inhalt.html) — retrieved 2026-04-17 (also mirrored on [gesetze-im-internet.de](https://www.gesetze-im-internet.de/estg/__32a.html))

Formula:

```
if  zvE <=    12,348: tax = 0
elif zvE <=  17,799: y = (zvE - 12348) / 10000; tax = (914.51 * y + 1400) * y
elif zvE <=  69,878: z = (zvE - 17799) / 10000; tax = (173.10 * z + 2397) * z + 1034.87
elif zvE <= 277,825: tax = 0.42 * zvE - 11135.63
else:                tax = 0.45 * zvE - 19470.38
tax = floor(tax)
```

---

## Splittingverfahren (joint filing)

For Zusammenveranlagung (or Gnadensplitting after spousal death, §32a Abs. 6 EStG):

```
tax_joint = 2 * tax_single_tariff(combined_zvE / 2)
```

Apply the single-tariff formula to `combined_zvE / 2`, then double the result. This produces the splitting benefit for couples with unequal incomes.

---

## Implementation notes

- Round `zvE` **down** to full euros before applying the formula (§32a Abs. 1 Satz 5 EStG).
- Round the resulting tax **down** to full euros (§32a Abs. 1 Satz 6 EStG).
- For Lohnsteuer (payroll withholding), the BMF publishes a separate Programmablaufplan (PAP) each year that implements the same formula with additional monthly/annual intermediate steps. PAPs are NOT a substitute for the §32a formula in the Einkommensteuer assessment — they are the withholding approximation.
- Do **not** apply these coefficients to anything other than the year they match. The coefficients are year-specific; mixing years produces silent errors.
- When a new year's values are published (typically via BMF letter in Q4 or early January), update both this file and `tax-parameters.md`.
