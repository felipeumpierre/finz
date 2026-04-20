# Expense Categories — Bank Skill Reference

Predefined expense categories for German household transaction classification. These patterns are used when scanning Kontoauszug and Kreditkartenabrechnung documents. Apply them in the order listed under each category — first match wins.

All pattern matching is **case-insensitive** and **substring-based** (the description just needs to contain the pattern, not equal it exactly).

---

## Category Definitions

### `miete` — Rent

**German context:** Monthly rent payment (Kaltmiete, Warmmiete, or Betriebskostenvorauszahlung) to a landlord or property management company. Typically a recurring fixed amount on the 1st-5th of the month.

**Classification rules:**
- Usually a single large debit, same amount each month
- Recurring transfers to the same IBAN not classified as `ueberweisungen_intern` (not own IBAN)
- Dauerauftrag (standing order) label is a strong signal

**Merchant/description patterns:**
- `BUWOG`
- `DEUTSCHE WOHNEN`
- `VONOVIA`
- `ADLER REAL ESTATE`
- `SAGA`
- `MIETE`
- `KALTMIETE`
- `WARMMIETE`
- `BETRIEBSKOSTEN`
- `HAUSGELD`
- `WOHNUNGSMIETE`
- `NETTOMIETE`
- `MIETKOSTEN`

**Notes:** If the landlord is a private individual, there will be no corporate pattern — rely on recurring amount + "MIETE" in Verwendungszweck or the description entered by the user when setting up the Dauerauftrag.

---

### `lebensmittel` — Groceries

**German context:** Supermarket and discount grocery store purchases. Includes weekly shopping at major chains. Does not include restaurant or delivery spending (see `restaurants`).

**Classification rules:**
- Point-of-sale (POS) transactions at known grocery chains
- Online grocery orders (REWE online, Picnic, Gorillas, etc.)
- Drug store purchases at DM/Rossmann that include food are split: classify as `haushalt` if the merchant is DM/Rossmann (most purchases are household); reclassify to `lebensmittel` only if the user corrects it

**Merchant/description patterns:**
- `REWE`
- `EDEKA`
- `LIDL`
- `ALDI`
- `PENNY`
- `NETTO`
- `KAUFLAND`
- `REAL MARKT`
- `NORMA`
- `HIT HANDELSGRUPPE`
- `TEGUT`
- `GLOBUS`
- `FAMILA`
- `MARKTKAUF`
- `DENN'S BIOMARKT`
- `BASIC BIO`
- `BIO COMPANY`
- `PICNIC`
- `GORILLAS`
- `FLINK`
- `BRINGMEISTER`

---

### `transport` — Public Transit & Mobility

**German context:** Public transportation (BVG, U-Bahn, S-Bahn, bus, regional trains), ride-hailing, bike/scooter sharing, and fuel. Does not include long-distance travel for holidays (classify those under `freizeit`).

**Classification rules:**
- BVG and DB tickets/subscriptions are always `transport`
- Fuel purchases at gas stations are `transport`
- Ride-hailing (Uber, Bolt, FreeNow) are `transport`
- Micro-mobility (Tier, Lime, Nextbike) are `transport`
- Car repair/maintenance → `haushalt` (reclassify if user corrects)
- KFZ insurance → `versicherungen`

**Merchant/description patterns:**
- `BVG`
- `BERLINER VERKEHRSBETRIEBE`
- `DB BAHN`
- `DEUTSCHE BAHN`
- `DB FERNVERKEHR`
- `S-BAHN BERLIN`
- `MVV`
- `MVG`
- `HVV`
- `VRN`
- `VRS`
- `UBER`
- `BOLT`
- `FREENOW`
- `MYTAXI`
- `TAXI`
- `TIER`
- `LIME`
- `NEXTBIKE`
- `CALLABIKE`
- `ARAL`
- `SHELL`
- `TOTAL`
- `ESSO`
- `JET TANKSTELLE`
- `BP`
- `TANKSTELLE`
- `FLIXBUS`

---

### `versicherungen` — Insurance Premiums

**German context:** Monthly or annual insurance premium payments. Includes health insurance (GKV contribution if separately billed), liability, BU, household, dental, and any other Versicherung policies.

**Classification rules:**
- Cross-reference `workspace/insurance-state.json` — use provider names from known policies as patterns
- Descriptions typically contain the provider name + "BEITRAG", "PRAEMIE", or "VERSICHERUNG"
- GKV contributions (Techniker Krankenkasse, AOK, Barmer, etc.) are `versicherungen`
- If the transaction matches a known policy in insurance-state.json, classify with high confidence

**Merchant/description patterns (generic — supplement with insurance-state.json providers):**
- `VERSICHERUNG`
- `VERSICHERUNGS`
- `BEITRAG`
- `PRAEMIE`
- `ALLIANZ`
- `ARAG`
- `AXA`
- `ERGO`
- `GENERALI`
- `HDI`
- `ZURICH`
- `R+V`
- `DEBEKA`
- `DEVK`
- `HUK-COBURG`
- `GOTHAER`
- `SIGNAL IDUNA`
- `NUERNBERGER`
- `TECHNIKER KRANKENKASSE`
- `TK KRANKENKASSE`
- `AOK`
- `BARMER`
- `DAK`
- `IKK`
- `KNAPPSCHAFT`
- `KKH`

---

### `abos_subscriptions` — Recurring Subscriptions

**German context:** Digital streaming, music, fitness, and software subscriptions. Typically monthly fixed amounts to digital service providers. Also includes annual software licenses.

**Classification rules:**
- Recurring monthly fixed amount from a known digital provider → high confidence
- Amazon transactions: only AMAZON PRIME membership and KINDLE UNLIMITED are `abos_subscriptions`; product purchases are `sonstiges` (or corrected by user)
- Annual charges from subscription services still classify as `abos_subscriptions`

**Merchant/description patterns:**
- `NETFLIX`
- `SPOTIFY`
- `APPLE.COM/BILL`
- `APPLE SERVICES`
- `AMAZON PRIME`
- `AMAZON DIGITAL`
- `KINDLE UNLIMITED`
- `DISNEY PLUS`
- `DISNEY+`
- `HULU`
- `DAZN`
- `SKY DEUTSCHLAND`
- `MAGENTA TV`
- `RTL+`
- `JOYN`
- `URBAN SPORTS CLUB`
- `URBAN SPORTS`
- `FITX`
- `MCFIT`
- `EVO FITNESS`
- `HOLMES PLACE`
- `YOUTUBE PREMIUM`
- `GOOGLE ONE`
- `DROPBOX`
- `MICROSOFT 365`
- `ADOBE`
- `AUDIBLE`
- `DUOLINGO`
- `BABBEL`
- `HEADSPACE`
- `CALM`
- `NOTION`
- `CHATGPT`
- `OPENAI`
- `LINKEDIN PREMIUM`
- `XING PREMIUM`

---

### `restaurants` — Eating Out & Food Delivery

**German context:** Restaurant meals, cafe visits, fast food, and food delivery services. Distinct from `lebensmittel` (grocery shopping). Includes bar tabs and bakery purchases.

**Classification rules:**
- Food delivery platforms are always `restaurants`
- On-site restaurant POS transactions
- Bakeries (Baeckerei) are `restaurants` by default; reclassify to `lebensmittel` if user prefers
- Coffee shops (Starbucks, local cafes) are `restaurants`

**Merchant/description patterns:**
- `LIEFERANDO`
- `WOLT`
- `DELIVEROO`
- `UBER EATS`
- `MCDONALDS`
- `BURGER KING`
- `KFC`
- `SUBWAY`
- `NORDSEE`
- `STARBUCKS`
- `COFFEE FELLOWS`
- `BACKWERK`
- `BAECKER`
- `BAECKEREI`
- `RESTAURANT`
- `RISTORANTE`
- `PIZZERIA`
- `SUSHI`
- `THAI`
- `KEBAB`
- `FEINKOST`
- `IMBISS`
- `GASTSTATTE`
- `GASTHAUS`
- `WIRTSHAUS`
- `PIZZASERVICE`

---

### `kinderbetreuung` — Childcare

**German context:** Daycare (Kita), nursery, kindergarten fees, and after-school care (Hort). Usually a monthly recurring amount to a Kita or city administration.

**Classification rules:**
- Typically a recurring monthly payment to a Kita, Kindergarten, or Jugendamt
- City of Berlin Kita contributions may come from Jugendamt or directly from the facility
- Private nanny/au pair payments: classify as `kinderbetreuung` if user confirms the IBAN
- Babysitter one-off cash withdrawals: not automatically classifiable — will appear as `sonstiges`

**Merchant/description patterns:**
- `KITA`
- `KINDERGARTEN`
- `KINDERHAUS`
- `KINDERTAGESSTATTE`
- `KINDERTAGESSTAETTE`
- `HORT`
- `JUGENDAMT`
- `KRIPPE`
- `TAGESMUTTER`
- `TAGESPFLEGE`
- `ELTERNBEITRAG`
- `BETREUUNGSKOSTEN`
- `KINDER`

---

### `gesundheit` — Health & Medical

**German context:** Prescription pickup at pharmacies, doctor copayments (Praxisgebuehr), dental treatments, physiotherapy, and health-related purchases. Distinct from health insurance premiums (those are `versicherungen`).

**Classification rules:**
- Pharmacy purchases (Apotheke) are always `gesundheit`
- Doctor office payments (Arzt, Praxis) are `gesundheit`
- Physiotherapy (Physiotherapie, Krankengymnastik) is `gesundheit`
- Gym memberships are `abos_subscriptions` unless the user specifically uses them for medical reasons
- Contact lenses and glasses: `gesundheit`

**Merchant/description patterns:**
- `APOTHEKE`
- `PHARMACY`
- `ARZT`
- `PRAXIS`
- `ZAHNARZT`
- `ZAHNARZTPRAXIS`
- `PHYSIOTHERAPIE`
- `KRANKENGYMNASTIK`
- `OPTIKER`
- `FIELMANN`
- `APOLLO OPTIK`
- `MCOPTIK`
- `KRANKENKASSE ZUZAHLUNG`
- `HEILPRAKTIKER`
- `PSYCHOTHERAPEUT`
- `LABOR`
- `DOCMORRIS`
- `SHOP APOTHEKE`
- `MEDPEX`

---

### `kleidung` — Clothing & Shoes

**German context:** Clothing, shoes, and accessories purchases at retail stores and online fashion platforms.

**Classification rules:**
- Online fashion retailers (Zalando, About You, H&M online) are `kleidung`
- Physical store purchases at clothing chains
- Sports clothing at dedicated sports retailers (Decathlon, Intersport) → classify as `kleidung` by default; reclassify to `freizeit` if sports equipment dominates

**Merchant/description patterns:**
- `ZALANDO`
- `ABOUT YOU`
- `H&M`
- `ZARA`
- `MANGO`
- `UNIQLO`
- `C&A`
- `NEW YORKER`
- `PRIMARK`
- `RESERVED`
- `ESPRIT`
- `TOMMY HILFIGER`
- `HUGO BOSS`
- `ADIDAS`
- `NIKE`
- `PUMA`
- `DECATHLON`
- `INTERSPORT`
- `SPORT SCHECK`
- `PEEK & CLOPPENBURG`
- `P&C`
- `GALERIA`
- `KA.DE.WE`

---

### `haushalt` — Household Items & Home Supplies

**German context:** Furniture, home decor, cleaning supplies, personal care products, electronics, and general household goods. Includes drug store purchases (DM, Rossmann) since most purchases there are household supplies.

**Classification rules:**
- IKEA is always `haushalt`
- DM and Rossmann default to `haushalt` (even if food items are also purchased)
- Hardware stores (Baumarkt) are `haushalt`
- Electronics for home use (MediaMarkt, Saturn) are `haushalt`
- Cleaning services and Putzkraft payments: classify as `haushalt`

**Merchant/description patterns:**
- `IKEA`
- `DM DROGERIE`
- `DM-MARKT`
- `ROSSMANN`
- `MUELLER`
- `BUDNIKOWSKY`
- `BAUHAUS`
- `OBI`
- `HORNBACH`
- `TOOM`
- `BAUMARKT`
- `MEDIAMARKT`
- `SATURN`
- `EXPERT`
- `EURONICS`
- `AMAZON` (non-Prime, non-subscription — general Amazon purchases default here; user can correct)
- `OTTO`
- `WAYFAIR`
- `HOME24`
- `XXXLUTZ`
- `ROLLER`
- `POCO`
- `DEPOT`
- `TCHIBO`
- `BUTLERS`

---

### `freizeit` — Entertainment & Leisure

**German context:** Entertainment, hobbies, sports activities, concerts, cinema, museums, books, and recreational spending. Also covers holiday-related transport (long-distance train/flight) and accommodation when on vacation.

**Classification rules:**
- Cinema and theatre tickets are `freizeit`
- Concerts and event tickets (Eventim, Ticketmaster) are `freizeit`
- Museums and cultural institutions are `freizeit`
- Book purchases (Thalia, Hugendubel) are `freizeit`
- Hobby supplies (craft stores, music instrument shops) are `freizeit`
- Vacation hotel/Airbnb/flight bookings are `freizeit`
- Gambling or lottery: `sonstiges` (flag for user review)

**Merchant/description patterns:**
- `KINO`
- `CINEMA`
- `CINEStar`
- `ODEON`
- `VUE`
- `THEATER`
- `OPER`
- `PHILHARMONIE`
- `KONZERT`
- `EVENTIM`
- `TICKETMASTER`
- `RESERVIX`
- `AIRBNB`
- `BOOKING.COM`
- `HOTELS.COM`
- `HRS`
- `EXPEDIA`
- `RYANAIR`
- `EASYJET`
- `LUFTHANSA`
- `EUROWINGS`
- `THALIA`
- `HUGENDUBEL`
- `WELTBILD`
- `MUSEUM`
- `GALERIE`
- `FREIZEITPARK`
- `MOVIEPARK`
- `LEGOLAND`
- `TIERPARK`
- `SPORT VEREIN`
- `SPORTCLUB`
- `HALLENBAD`
- `SCHWIMMBAD`

---

### `kreditkarte` — Credit Card Lump Payment

**German context:** The monthly debit from the Girokonto to pay the credit card balance. This is NOT an expense category — it is a pass-through. The actual spending detail lives in the linked credit card statement (`linked_credit_cards[].monthly_statements`).

**Classification rules:**
- ALWAYS exclude from expense totals — this would double-count spending already tracked in card statements
- Identify by: the bank's own credit card provider name in the Verwendungszweck + the word "KREDITKARTE", "ABRECHNUNG", "KARTENABRECHNUNG", or a card reference number
- Classified as `kreditkarte` in `monthly_summaries.categories` for bookkeeping, but excluded from all expense subtotals and savings rate calculations

**Merchant/description patterns:**
- `KREDITKARTE`
- `KARTENABRECHNUNG`
- `VISA ABRECHNUNG`
- `MASTERCARD ABRECHNUNG`
- `AMEX ABRECHNUNG`
- `AMERICAN EXPRESS`
- `KREDITKARTENABRECHNUNG`
- `KARTENUMSATZ`
- `KREDITKARTENZAHLUNG`
- `DEUTSCHE BANK KREDITKARTE`
- `ING KREDITKARTE`
- `DKB KREDITKARTE`
- `N26 MASTERCARD`
- `COMDIRECT KREDITKARTE`

---

### `ueberweisungen_intern` — Internal Transfers

**German context:** Transfers between the user's own accounts (e.g., moving money from Girokonto to Tagesgeld). These are cash movements, not expenses. Excluding them is critical for accurate savings rate and expense total calculations.

**Classification rules:**
- Match the destination IBAN against all known own-account IBANs from `cash-state.json`
- ALWAYS exclude from expense totals — internal transfers are not spending
- This is the highest-confidence category when an IBAN match is found — do not override with other patterns
- If the user has IBANs at multiple banks for multiple family members, load all of them

**Merchant/description patterns:**
- Own IBAN match (primary rule — loaded from `cash-state.json`)
- `EIGENUBERWEISUNG`
- `EIGENE UBERWEISUNG`
- `UMBUCHUNG`
- `DEPOT EINZAHLUNG` (when transferring to broker account — check if the IBAN matches)

---

### `sonstiges` — Uncategorized

**German context:** The catch-all for everything that doesn't match a known pattern. The goal is to minimize this category over time through corrections and learned patterns.

**Classification rules:**
- Apply only when NO other category matches
- After scanning, present all `sonstiges` transactions to the user for review
- For each corrected item, store the pattern to prevent future misclassification
- Target: `sonstiges` should be <10% of total monthly expenses after corrections

**What commonly ends up here (and how to handle it):**
- PayPal payments (merchant unknown) — ask the user what the PayPal payment was for
- Amazon product purchases — ask whether to classify as `haushalt`, `freizeit`, or `kleidung`
- Transfers to individuals (friends, family) — may be loan repayments, gifts, or shared expenses; ask the user
- ATM cash withdrawals — classify as `sonstiges` by default; user can assign a category
- Fees (Kontoführungsgebühren, bank fees) — ask user if they want a dedicated category or keep as `sonstiges`

---

## Quick Reference Table

| Category | Key Patterns | Exclude from totals? |
|----------|-------------|---------------------|
| `miete` | MIETE, BUWOG, VONOVIA, BETRIEBSKOSTEN | No |
| `lebensmittel` | REWE, EDEKA, LIDL, ALDI, PENNY, NETTO | No |
| `transport` | BVG, DB BAHN, TIER, LIME, UBER, TANKSTELLE | No |
| `versicherungen` | VERSICHERUNG, ALLIANZ, TK, AOK (+ insurance-state.json providers) | No |
| `abos_subscriptions` | NETFLIX, SPOTIFY, AMAZON PRIME, URBAN SPORTS | No |
| `restaurants` | LIEFERANDO, WOLT, RESTAURANT, BAECKEREI | No |
| `kinderbetreuung` | KITA, KINDERGARTEN, HORT, ELTERNBEITRAG | No |
| `gesundheit` | APOTHEKE, ARZT, ZAHNARZT, FIELMANN | No |
| `kleidung` | ZALANDO, H&M, ZARA, NEW YORKER | No |
| `haushalt` | IKEA, DM, ROSSMANN, MEDIAMARKT, AMAZON (general) | No |
| `freizeit` | KINO, EVENTIM, AIRBNB, THALIA, SPORTVEREIN | No |
| `kreditkarte` | KREDITKARTE, VISA ABRECHNUNG, own card payment | **Yes — excluded from totals** |
| `ueberweisungen_intern` | Own IBAN match, EIGENUBERWEISUNG | **Yes — excluded from totals** |
| `sonstiges` | Catch-all — minimize via corrections | No |
