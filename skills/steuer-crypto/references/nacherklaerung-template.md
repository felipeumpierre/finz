# Nacherklärung (Self-Correction) Template

> Last verified: 2026-09-01 — Zeile numbers below follow the **TY 2024** Anlage SO (`anlage-so-mapping-2024.md`). For **TY 2025** the Kryptowerte block starts at Zeile 45 (Gewinn/Verlust Zeile 51) and the §22 Nr.3 Leistungen block is Zeilen 14–20 (Summe Einnahmen Zeile 18) — see `anlage-so-mapping-2025.md` [secondary-source, official PDF not yet checked]. Adjust the Zeile references per tax year being corrected.

Use this template when `needs_correction = true` for a tax year and the user wishes to
file a voluntary self-correction under §153 AO (unintentional error) or §371 AO (self-disclosure).

---

**[Ort], [Datum]**

**Betreff: Berichtigung der Einkommensteuererklärung [JAHR] gemäß §153 AO**

An das
Finanzamt [Name des Finanzamts]
[Adresse]

Sehr geehrte Damen und Herren,

hiermit berichtige ich meine Einkommensteuererklärung für das Jahr **[JAHR]** gemäß §153 AO.

**Steuernummer:** [Steuernummer]
**Name:** [Vollständiger Name]
**Adresse:** [Adresse]

---

## Berichtigte Angaben

### §23 EStG — Private Veräußerungsgeschäfte (Kryptowährungen)

| Position | Ursprünglich erklärt | Berichtigt |
|---|---|---|
| Summe Gewinne (Zeile 53, TY 2024) | [ursprünglicher Wert] EUR | [sect_23_gain_eur] EUR |
| Summe Verluste (Zeile 54, TY 2024) | [ursprünglicher Wert] EUR | [sect_23_loss_eur] EUR |
| Verbleibender Betrag (Zeile 55, TY 2024; TY 2025: Zeile 51) | [ursprünglicher Wert] EUR | [sect_23_net_eur] EUR |
| Steuerpflichtiger Betrag | [ursprünglicher Wert] EUR | [sect_23_taxable_eur] EUR |

### §22 Nr.3 EStG — Sonstige Einkünfte (Staking/Zinsen)

| Position | Ursprünglich erklärt | Berichtigt |
|---|---|---|
| Einnahmen (Zeilen 10–11, TY 2024; TY 2025: Zeile 18) | [ursprünglicher Wert] EUR | [sect_22_3_income_eur] EUR |
| Werbungskosten (Zeile 15, TY 2024; TY 2025: Zeile 19) | [ursprünglicher Wert] EUR | [Werbungskosten] EUR |
| Einkünfte (Zeile 16, TY 2024; TY 2025: Zeile 20) | [ursprünglicher Wert] EUR | [computed] EUR |
| Steuerpflichtiger Betrag | [ursprünglicher Wert] EUR | [sect_22_3_taxable_eur] EUR |

---

## Begründung

Die ursprüngliche Steuererklärung enthielt keine Angaben zu Einkünften aus
Kryptowährungstransaktionen. Nach vollständiger Aufarbeitung der Transaktionshistorie
für die Jahre 2017–[JAHR] ergeben sich die oben genannten berichtigten Beträge.

Die Berechnung basiert auf der FIFO-Methode (First-In-First-Out) gemäß den Grundsätzen
des BMF-Schreibens vom 10.05.2022 und der Ergänzung vom 06.03.2025.

---

## Unterlagen

Beigefügt:
- [ ] Disposals-Tabelle [JAHR] (alle Veräußerungsgeschäfte)
- [ ] Income-Tabelle [JAHR] (Staking/Zinserträge)
- [ ] Lot-Detail-Tabelle (Anschaffungskosten und Haltedauer)
- [ ] Berechnungsgrundlagen (crypto-ledger.json Auszug)

---

Mit freundlichen Grüßen,

[Unterschrift]
[Name]

---

*Hinweis: Dieses Template dient als Ausgangspunkt. Die endgültige Fassung sollte von einem
Steuerberater oder Lohnsteuerhilfeverein geprüft werden. Bei bewusster Steuerhinterziehung
ist §371 AO (Selbstanzeige) zu prüfen — hierfür ist zwingend anwaltliche Beratung erforderlich.*

*§371 AO — Vollständigkeitsgebot und Sperrwirkung (Zusammenfassung aus
`skills/crypto/references/german-crypto-tax-law.md`): Eine Selbstanzeige schützt nur, wenn sie
**vollständig** ist — alle unverjährten Steuerstraftaten derselben Steuerart, mindestens die
letzten 10 Kalenderjahre, müssen offengelegt werden; Teil-Selbstanzeigen sind unwirksam. Die
Sperrwirkung greift (keine Straffreiheit mehr), wenn vor Eingang der Selbstanzeige eine
Prüfungsanordnung (§196 AO) oder die Einleitung eines Straf-/Bußgeldverfahrens bekanntgegeben
wurde, ein Amtsträger zur Prüfung erschienen ist, die Tat bereits (ganz oder teilweise) entdeckt
war und der Steuerpflichtige dies wusste oder damit rechnen musste, oder die hinterzogene Steuer
je Tat 25.000 EUR übersteigt (dann nur §398a AO gegen Zuschlag). §153 AO (Berichtigung) und
§371 AO schließen sich gegenseitig aus — die Einordnung vor dem Versand mit Steuerberater/Anwalt klären.*
