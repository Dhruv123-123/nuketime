# D02 TRIBUNAL: red team, business edge and buildability lens

Date: 24 Oct 2026. Reviewer lens: does TRIBUNAL beat Zanskar by enough to buy rights first? Can 2-4 people plus agents ship v1 in 6 months? Does it drive land and sensor decisions? No new web searches. Figures come from D02, MODEL.md and the L-digests. Anything I did not check is marked (unverified).

## Verdict

Not refuted. Score 16/25. The core idea is sound: LLMs propose conceptual models, a non-LLM judge scores them. That keeps probabilities honest. The weak points are scope (v1 is really an 18-month plan) and an unproven claim that LLM councils beat a cheap automated card generator. Both have clear fixes.

| Axis | Score | Why |
|---|---|---|
| Calibrated certainty | 4 | No LLM sets a probability. BMA plus unknown card plus MMD flag is the right shape. Per-archetype calibration on about 11 positives is too thin. |
| Data realism | 3 | Evidence graph and censored columns are real. Month-4 extraction "at scale" across NBMG, NDOM, NDWR and DOGM is optimistic but agent-doable. |
| Buildable in 6 months | 2 | Twelve major components for 4.5 people. FNO, POMCPOW and the crowd model will not land by month 6. |
| Edge vs Zanskar | 3 | Upflow-location density is a real, saleable edge. The council's lift over plain SENTINEL-COX is unproven, and Zanskar can copy an LLM council. |
| Drives rights and sensors | 4 | Challenges become priced field actions. Conformal buy list with FDR. Land agent routes to private and state ground. Missing a lead-time KPI. |

## Flaws and AI-leveraged fixes

**1. Scope is not a 6-month v1 (serious).** Months 1-6 ask for a card DSL, compiler, per-archetype NPE with SBC, MMD test, a multi-family council, geo-blinding, statewide extraction, failure tagging, three hindcast freezes, calibration, conformal selection, a POMDP planner, a crowd model and an FNO. The team is one modeller, one sim engineer, one agent engineer, one geologist and half a land analyst. Each of FNO (5,000-20,000 TOUGH3 runs, about 100k CPU-hours, unverified) and POMCPOW is a quarter of work on its own.
*Fix:* cut v1 to the spine that buys land: evidence graph, Stage-0 extraction, SENTINEL-COX prior, council writing cards, GHOST Tier-1 judge, greedy EVSI/$ ranking, conformal buy list. Move FNO, POMDP look-ahead and the crowd model to months 7-12. Use coding agents to build the card compiler and test harness in parallel; the geologist only signs off golden cards. This keeps v1 at about 6 components.

**2. The council may be an expensive proposal sampler (serious).** The judge does all the scoring. So the LLMs add value only if they propose cards a machine would miss. A script that samples cards from archetype priors along every mapped fault, with upflow positions on a grid up-gradient of warm wells, may match them at 1% of the cost. D02's gate (2) compares the council to SENTINEL-COX, not to this enumerator.
*Fix:* add an ablation arm to the 40-prospect test: "auto-enumerator, same judge, same compute". Keep LLM roles only where they win. Likely winners: the Archivist reading old company reports, and the Skeptic finding failure modes in completion reports. Those are text tasks a script cannot do. This turns the council from a claim into a measured asset.

**3. Edge over Zanskar is narrower than section 9 says (serious, not fatal).** Zanskar has its own drilled holes, a digitised archive, a large BLM position and a geology team (unverified size). Points 1, 3 and 4 in section 9 are copyable: an LLM council is a few months of work for them, and they could add censored columns too. Real, durable edges are three: (a) upflow placement in outflow-first cases, where the hindcast can show we buy the right acre before the first hole (Don A. Campbell, Granite Springs, McGinness); (b) private-ranch and state ground, where Zanskar's BLM focus is thin; (c) a hashed public ledger that buyers trust.
*Fix:* aim councils first at private and state parcels and at non-Nevada provinces (Utah, Oregon, Idaho, New Mexico basin tiles), where nobody runs models. Make the pitch "upflow acre plus audit trail", not "we reason better".

**4. No lead-time metric (serious for the business).** Land edge is about time. D02 scores rank and log score, not how many months ahead of the first public signal (BLM nomination by others, a lease, a press release) we would have flagged a cell.
*Fix:* add "median lead time to first public signal" to the hindcast, using the bitemporal graph's known_time. Agents can scrape BLM MLRS nomination and sale history and state lease rolls to date those signals. Gate: at least 12 months median lead on the 11 cases (unverified bar).

**5. Per-archetype calibration has too few labels.** With 11 blind cases over 7 archetypes, most bins hold 0-3 positives. Isotonic or Venn-Abers per bin will overfit.
*Fix:* hierarchical recalibration that pools archetypes, plus GHOST synthetic worlds with planted systems for calibration where truth is known. Widen labels with the 205-system inventory, thinned by the Cox effort term.

**6. Geo-blinding of famous systems is leaky.** Fault geometry plus a lithology column can betray McGinness Hills even with rotated coordinates. A "name it" probe misses silent recognition.
*Fix:* add counterfactual probes: swap one key fact (e.g. flip a geothermometer) and check that card proposals move as the data say, not as memory says. Because the judge sets weights, leakage can only bias proposals; the ablation arm in flaw 2 also catches it.

**7. Senior geologist is the bottleneck.** One person writes the DSL, sets archetype priors and audits dossiers for 3,000 councils a month.
*Fix:* agents extract the 300-600 archetype cards from GRC, Stanford Geothermal Workshop and NBMG papers. The geologist reviews a stratified 10% sample. Dossiers get human review only above a buy threshold.

## Buildability check

Token cost ($15k-$90k a month, unverified) is fine against one TG hole. The cheapest first test (40 prospects, $5k-$10k, three weeks) is good and should run in month 1, not month 3. That ordering de-risks the whole design early. With the cut scope in flaw 1, a v1 that produces a hashed buy list and a first sensor batch by month 6 is credible.

## Does it drive land and sensors?

Yes, better than most designs. Every field challenge has a price, the buy list has an FDR, and bids carry a winner's-curse term. The upflow density tells you which aliquot to file on. Add lead time (flaw 4) and private-land routing (flaw 3) and it becomes a land machine, not just a map.
