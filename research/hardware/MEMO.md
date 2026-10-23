# Own Hardware for the Heat-Rights Bank: Memo

Date: 23 Oct 2026. Question from Dhruv: "something hardware that can be done, such as designing our own sensor". Built from 14 research files (H01-H14) and 2 red-team files (V01, V02) in `evidence/`. The shared web budget ran out partway through most slices, so many prices are marked (unverified) in the evidence files. Treat those as estimates.

---

## 1. Verdict

**Yes, there is a sensor worth building. It makes the geothermal heat-rights bank more defensible. It is not a separate, bigger company.**

The best hardware is a **two-part heat-sensing kit that the bank's own field team carries:**

1. **A slim drop probe for ranch water wells** ("logger as landman"). It logs temperature, pressure and conductivity in private stock and irrigation wells. The rancher gets a free well-health check. We get a temperature profile nobody else has and, on the same visit, a geothermal option at about $1 per acre per year.
2. **Logging 2 m temperature probes plus cheap electric-field MT nodes** on open federal and state land. Under BLM IM 2026-024 these count as casual use: no permit, no notice, and no duty to file the data while the land is unleased.

Later, an own light gradient rig and an EGS block-rating kit are the next rungs, not the start.

**Score: 18/25** (c1 4, c2 4, c3 4-5, c4 3, c5 3). That is below the plain bank's 20/25. The hardware makes our data private and our proving cheaper. It does not raise the price a buyer pays, and it does not lift the size ceiling. So the honest framing is: **the bank is the company, the sensor is its moat.**

Nothing outside geothermal beat it. The best outside play, a grid-headroom sensor network for powered data-centre land, scored 20-21 on first pass and fell to **15/25** under red team (section 5).

---

## 2. Why hardware helps the bank at all

The bank's three weak spots from the geothermal memo were:

| Weak spot | Does own hardware fix it? |
|---|---|
| Public data is copyable (Enverus bought A2D; Zanskar could copy the archive wedge) | **Yes.** Probe series, ranch-well profiles and cold holes exist only in our files. Data from unleased federal land need not be filed (43 CFR 3253.10(b)). |
| Proving is expensive (gradient holes $0.3-1.5M all-in) | **Partly.** Screens cost $2-8k per km2 against one gradient hole for a whole basin. An own rig gives maybe 2-5x, not the 12x first claimed (V01). |
| Weak step-up before a PPA (about $0.1M/MW confirmed, less at anomaly stage) | **No.** Buyers re-drill before committing capital. Hardware lowers our cost, not their price. |

The first two are real, so the kit earns a place. The third is untouched, so the score does not rise above the bank.

---

## 3. The kit, with numbers

### 3a. Ranch water-well drop probe (H06). First product.
- **Hardware:** 16 mm probe that fits a pump sounding tube, with temperature, pressure and conductivity, plus a water sample for geothermometers and helium. Optional permanent IoT probe about $200 at scale.
- **Cost:** prototype $10-15k for two kits in 6-10 weeks. BOM about $2k now, about $800 at scale (unverified).
- **Why it matters:** DOE play fairway blind hits came at about 150-250 m, which is water-well depth (Gabbs Valley 124.9 C at 152 m). State well-log databases (NV NDWR since 1984, UT, OR, ID, NM) hold depth and water level but no temperature profiles.
- **The deal:** private heat is cheap. Raser leased about 11,600 Truckee River Ranch fee acres for roughly $2/acre (SEC exhibit), against about $40/acre it paid at a BLM auction. Texas SB 785 (2023) gives the surface owner the heat.
- **Trap to screen out:** land patented under the Stock-Raising Homestead Act reserves geothermal to the United States (US v. Union Oil, 9th Cir. 1977). Screen these from public GLO patent records before the visit.
- **Throughput:** one 2-person team might option 100-400k acres a year at $1-3/acre all-in (unverified).

### 3b. Open-land screen: logging 2 m probes + E-field MT nodes (H01, H03, H05, H13).
- **Legal window:** BLM IM 2026-024 (issued 31 Aug 2026, expires 30 Sep 2029) treats push rods under 2 inches, battery sensors in small holes, installs under 10 ft and MT as casual use. No notice or application. Grey area: it excludes "mechanised drilling equipment" and limits off-road travel, so a robot pusher needs a field-office check (V01).
- **2 m probes:** $200-500 per station today (median $300, OpenEI). A logging probe at scale is about $45-150 (unverified). A year of readings at three depths removes the seasonal and albedo noise that one-off readings carry.
- **E-field MT nodes:** contractor MT runs $522-2,298 per station (OpenEI; median $1,739). Low-cost electric-field-only loggers have run 2-4 months alone and matched commercial units (EGU21-16275). About $250-300 per node at 1,000 units plus one magnetic reference station per 5-10 km2 gives about $150-250 per site, or $3-8k per km2 (unverified).
- **Track record:** 2 m probes found or flagged Teels Marsh, Emerson Pass, Columbus Salt Marsh and Gabbs Valley. But about 6 of 11 valleys in one UNR campaign came back blank, so recall on deep blind systems is the open question.

### 3c. Later rungs (not the start)
- **Own light gradient rig (H11):** prototype about $1.1-1.5M and 9-12 months. Target $25-60k per 200 m hole, but sized to 500 m (our own evidence says 244 m missed at Argenta Rise) it is more like $60-120k (unverified). Earth AI's $100/m is a target, not achieved.
- **EGS block-rating kit (H12):** long-dwell thermistor strings in 150-300 m holes plus 30-60 seismic nodes for stress direction. Nobody measures stress before an auction. Utah EGS land already clears at $111/acre average and $1,207 top, so the ranking edge is worth a lot if it works. Free desk test on FORGE data first.

---

## 4. Four-part test for the kit (applied to the bank)

1. **Expensive, low-hit-rate proving step: 4/5.** About 50% first-well success; gradient holes $0.3-1.5M. The kit cuts the screening cost per basin by about 100x but does not reach a confirmation well.
2. **Data only we own: 4/5.** Ranch-well profiles and year-long probe series are not in any public database. Docked because methods are public and Zanskar already owns its own holes.
3. **Cheap right: 4-5/5.** The probe visit and the option signing are the same visit, at about $1-2/acre. Federal nominations and first-files still leak at lock.
4. **Step-up and a buyer: 3/5.** Unchanged from the bank. A gradient anomaly is a land-stage asset; buyers pay at confirmation plus PPA plus interconnection.

**Size ladder: 3/5.** Same 51,200-acre federal cap, but private ranch land sits outside it, which the probe is built to reach. EGS rating is the upside rung.

---

## 5. Every candidate scored

| Play | c1 | c2 | c3 | c4 | c5 | Total | Note |
|---|---|---|---|---|---|---|---|
| **Heat-rights bank + own sensor kit (pick)** | 4 | 4 | 4 | 3 | 3 | **18** | Red-teamed (V01). Moat for the bank, not a new company. |
| Logger as landman alone (H06) | 3 | 4 | 5 | 3 | 3 | 18 | Best single device. First product of the pick. |
| Own light gradient rig (H11) | 5 | 4 | 4 | 3 | 3 | 19 first pass, 18 after V01 | Real gain 2-5x, not 12x. |
| EGS block-rating kit (H12) | 4 | 4 | 3 | 4 | 4 | 19 (not red-teamed) | Best ladder rung. Unproven that shallow data predicts 3-5 km stress. |
| Dense E-field MT bank (H03) | 4 | 4 | 4 | 3 | 3 | 18 | Folded into the pick. |
| Heat carpet, 2 m probes (H01) | 4 | 4 | 3 | 3 | 3 | 17 | Folded into the pick. |
| Natural H2 / He seep nodes (H09) | 3 | 4 | 4 | 2 | 3 | 16 | Thin buyer set until a well flows. Side bet. |
| Brine lithium sensing (H08) | 3 | 4 | 2 | 4 | 3 | 16 | Texas gives produced water to the E&P (Cactus Water v. COG, 2025). |
| Grid headroom bank (H07, H14) | 3 | 2 | 2 | 5 | 3 | **15** after V02 (was 20-21) | Queue and contingency studies decide, not line flow. Wood Mackenzie bought LandGate; $50k/MW Texas deposits. |
| Soil gas / helium isotopes (H04) | 3 | 3 | 4 | 2 | 3 | 15 | Signal over blind systems is faint. Good add-on to the probe visit. |
| Old-well temperature census (H02) | 3 | 4 | 3 | 2 | 3 | 15 | Wells are where heat is weak (Texas, CA), scarce in NV (63 orphans) and UT (72). |
| Quantum / novel sensors (H05) | 2 | 2 | 3 | 2 | 2 | 11 | Quantum gradiometer error 20-23 E against 50-200 E signal; drone gravity drifts about 20 mGal. |

---

## 6. Why incumbents don't have this data

- **Survey contractors** (Quantec, Zonge, Phoenix) bill per station on $60k+ kit, so a carpet of cheap nodes undercuts their own business (H03).
- **Developers** (Ormat, Fervo) explore around fields they already hold. Fervo uses fibre after the lease is won, not to rank land (H12).
- **Zanskar** uses public data, LBNL large-n seismology and its own wells on BLM auction land. No ranch-well or private-land programme was found (geothermal memo, Z04).
- **Comps say own hardware only to cut the proving step, never to sell surveys.** KoBold (about $2.96B, pre-revenue) and Earth AI (own rig, owns tenements) are valued for the asset. Fleet Space sells surveys and owns no ground. CGG quit acquisition and kept the library (H10).

---

## 7. Cheapest first test

**Phase 0: 30 days, about $25-40k total.** Three parts:

1. **Ranch-well probe, $8-15k, 21 days.** Build two drop-probe kits. Log at least 15 ranch wells in one valley with a known system and one control valley.
   - Pass: at least 60% of wells logged without pulling the pump; the anomaly appears only in the known valley; at least 3 ranchers sign $1/acre options.
2. **Recall check, about $15k, 90 days of logging.** Put 40 logging 2 m probes across one known blind system (Teels Marsh or Dead Horse Wells) and one producing field.
   - Pass: corrected anomaly to background at least 3 to 1; residual noise under 0.3 C.
3. **EGS desk test, $0-20k, 14-21 days.** On public FORGE and Milford data, check whether shallow holes predict 3 km temperature within 25 C and surface seismic predicts stress direction within 20 degrees of the image log.

Also, before field work: a short lawyer's note confirming in writing that logging probes left for weeks are casual use under IM 2026-024 (about $5-10k).

---

## 8. Kill conditions

- **Depth blindness:** more than half of known blind or producing fields show no 2 m anomaly and no ranch-well anomaly. Then the screen tier is dead; fall back to 10-30 m pushes or the rig.
- **Access:** fewer than half of ranch wells can be logged without pulling pumps, or ranchers will not sign options alongside the free check.
- **Legal:** BLM field offices rule that logging probes or MT left out for weeks are not casual use.
- **Buyer:** no developer will price an anomaly-stage package (no carry, no override) even with private probe data. Then hardware cannot rescue c4 and the bank must fund confirmation itself, which is Zanskar's shape.
- **Copying:** Zanskar or Ormat starts a private-land or ranch-well programme before we lock 15k+ acres.

---

## 9. Answer in one line

Build the sensor, but build it as the bank's field tool: a ranch water-well probe that signs the heat option on the same visit, plus a no-permit probe and MT screen on open land, so our ML trains on temperatures only we own. That keeps the bank at about 18-20/25 and gives it the one moat it lacked. No hardware play found here is a bigger company on its own.
