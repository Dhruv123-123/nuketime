# D01 SCX2: red team, business edge and buildability lens

Date: 24 Oct 2026. Lens: does SCX2 beat Zanskar by enough to buy rights first? Can 2-4 people plus agents ship v1 in 6 months? Does it drive land and sensor decisions? No new web searches. Facts come from D01, MEMO.md, M13 and the L-digests. Unchecked items are marked (unverified). The data and science red teams (D01-data.md, D01-science.md) already cover identifiability and small-sample scoring. I do not repeat them.

## Verdict

Not refuted. Score 15/25. SCX2 is the strongest science stack in the program. But it is a 10-person, 18-month machine labelled as a 6-month v1. Its edge over Zanskar is real only in a few places, and those places are about land and timing, not model class. Its rival model points at the wrong rival. Its land layer misses who actually owns the heat under ranches. All of this is fixable with agents and scope cuts.

| Axis | Score | Why |
|---|---|---|
| Calibrated certainty | 4 | Bitemporal joins, SBC/TARP, OOD fallback, hashed ledger. Best in class. |
| Data realism | 3 | Extraction plan is credible. 50k GPU-hours of seismic re-picking and a West-wide MT atlas are side quests. |
| Buildable in 6 months | 2 | Seven engines. Section 11 itself asks for 8-10 people. The brief is 2-4. |
| Edge vs Zanskar | 3 | Effort term and censored cold wells are copyable in a quarter. Durable edge is off-auction land plus lead time, which SCX2 does not measure. |
| Drives rights and sensors | 3 | Hurdle-to-sensor routing is excellent. Land layer ignores split estate, outreach capacity and the 51,200-acre cap. |

## Flaws and AI-leveraged fixes

**1. Team and scope mismatch (serious).** Section 11 lists 9 roles. Month 4 alone holds hindcasts at six freezes, CSEP tests, decision replay, seismic re-picking and a chemistry NPE. A 2-4 person team cannot also run a 2x10^4 Waiwera bank, a Simformer, a BetaZero value net and a West-wide MT atlas by month 6.
*Fix:* define v1 as the spine that buys land: E0 lake, Stage 0 extraction, SCX2-lite Cox with shared effort, analytic Tier 1 columns, a greedy EVSI-per-dollar ranker and the buy list. Move the Simformer, FNO, POMDP, MT atlas, seismic re-pick and chemistry NPE to months 7-18. Coding agents build the harness, unit contracts and golden-trap suites in parallel. Buy rather than build where possible: use published ICE grids as the conductive prior, and USGS/INGENIOUS MT models instead of re-inverting every EDI. Roles for v1: one Bayesian modeller, one data/agent engineer, one geologist, one land lead.

**2. The crowd posterior is not Zanskar (serious).** E5 refits the pipeline on public layers. That models a BLM bidder. Zanskar holds about 27,000 private temperature samples, its own TG holes and more than 5 million acres tested (M13). Its map is better than the crowd map exactly where it has drilled. Leak cost and edge are then wrong in the cells that matter most.
*Fix:* fit Zanskar's revealed beliefs, not its imagined data. Agents scrape public footprints by affiliate name: BLM nominations and lease assignments in MLRS, Nevada NDOM and Utah DOGM thermal-gradient permit filings, county drilling permits, water-right filings for test holes, and DOE award sites. Each filing is a dated vote. A point-process model over these votes gives "Zanskar has looked here" as a layer. Our edge is then cells where our posterior is high and their revealed effort is low. Score E5 by how well it forecasts next quarter's nominations (also in D01-science).

**3. The edge is timing, but no metric measures time (serious).** Section 9 claims wins on labels, effort, physics and skill reporting. Zanskar can add an effort term, censored cold wells and an FNO in one quarter. What it cannot copy fast is: being on private and state ground first, in provinces it does not work, before the first public signal. SCX2 reports capture and calibration but not lead time.
*Fix:* add "median months ahead of first public signal" to every hindcast, using known_time in E0. Signals are the first nomination, lease, permit or press release by anyone. Pass bar: at least 12 months median lead on the dated blind set (unverified bar). Add "acres lockable per $ before signal" to the decision replay.

**4. Private ranch heat is often federal (serious for land).** Much western ranch land was patented under the Stock-Raising Homestead Act, which reserved minerals to the United States. Courts held geothermal resources to be a reserved mineral (US v. Union Oil, 9th Cir. 1977; unverified here). So a "ranch option" target may need a BLM lease, not a landowner deal. State law also splits heat between water and mineral regimes. SCX2's land_rights row treats tenure as a cost field.
*Fix:* add a title latent per parcel: surface owner, mineral estate owner, heat regime by state, existing leases and claims. Agents join the BLM surface/subsurface management layers, county assessor rolls and recorded deeds. The prior-claimant agent already exists; give it this job. Route split-estate targets to the federal path with decoy nominations.

**5. The POMDP is overbuilt for the price of land (moderate).** Rights cost about $1-10 per acre. At that price, sensing before buying rarely pays. The binding limits are elsewhere: the 51,200-acre per-state federal cap, ranch outreach bandwidth, and lease clocks.
*Fix:* replace POMCPOW and BetaZero in v1 with a knapsack under those three constraints. Pandora values stay as a rule for when to stop sensing. Add a landowner-conversion model learned from outreach logs, with an agent drafting and tracking letters. Keep the full POMDP for drilling and farm-out decisions, where costs run $1-5M per hole.

**6. Land action starts too late (moderate).** "First options signed" sits in month 6. Nominations grew 40x from 2020 to 2025. Six months of silence costs ground.
*Fix:* issue a v0 buy list at week 4 from the Freeze-2008 duel model, refit to today. Start ranch and state outreach in month 2 on the top 50 cells. Use the model's later releases to drop or add, not to start.

**7. The calibration campaign needs access we may not have (moderate).** Twenty known blind systems are mostly leased by operators. Running sensors on their ground needs permission.
*Fix:* run detectors on public roads and adjacent open BLM land, or partner with an operator for a data swap. Use AI-extracted published surveys at those sites as a desk calibration first.

**8. Too many value heads too early (minor).** EGS, superhot and closed-loop heads dilute a hydrothermal v1. *Fix:* keep only the EGS screen (depth to 200 C), because Fervo-type buyers pay for it. Defer the rest.

## What is genuinely strong for the business

- Cold and silent wells as censored data plus an effort term. This finds "unexplored, not empty" cells, which are the cheap ones.
- Sense-by-hurdle routing ties each cell's weakest link to a cheap sensor.
- The hashed forecast ledger and AGRCC-style data rooms are what a buyer of rights pays for.
- Leak-aware routing to private, state and leftover parcels fits the MEMO's off-auction thesis.

## Buildability check (2-4 people + agents, 6 months)

Spine (E0, extraction, SCX2-lite, Tier 1 columns, knapsack, buy list, lead-time hindcast): yes, if agents do extraction and harness work. Full SCX2: no. That is a year-two target.

## Bottom line

Keep SCX2 as the north star. Ship the spine in six months. Re-aim the rival model at Zanskar's public footprints. Measure lead time. Add title to the land layer. Then the model answers the question that pays: which acres to lock this month, before anyone else looks.
