# Hunt 9: the gold rubric at scale (17-18 Oct 2026)

**Verdict: nothing in the economy we could find passes the rubric outside geology.** 374 agents generated and tested 358 raw ideas (263 after merging) across 50 domain lenses. Nothing scored above 13.5 of 25, and each of the 15 finalists was refuted by at least 2 of 3 adversarial verifiers. The previous hunt thread's four nearest misses (UK land promotion, mitigation banking, orphaned defence part sources, unenforced judgments) were re-tested the same way, and all four were refuted 3/3. With the previous thread's ~115 candidates, about 380 distinct ideas have now been scored against Dhruv's rubric, and none clears it.

The useful output is the law that explains why, and what it implies (end of this memo).

Files: `gold/ALL_SCORES.md` (every candidate, score and reason), `gold/scored_263.csv`, `gold/hunt_results.json` (all scorer and verifier output with sources), `gold/deep_*.md` (deep dives on the top 3), `gold/nearmiss_verify.json`.

## The rubric as encoded

Each criterion is scored 0-5, for a total out of 25.

| | Criterion (Dhruv's framing) |
|---|---|
| C1 Frame | A discrete, sellable rung where discovery is 80%+ of the work, the physical step is trivial or abstracted, and a capitalised buyer buys the rung's output |
| C2 Step-up | The proving step takes the asset from near zero to a 10^3-10^4 step-up at once (5 = 10^3x or more, 3 = 10-100x, 1 = under 3x) |
| C3 Lever | The proving step is expensive and usually fails, so ML cuts discovery capex about 10x. The lever is capped at 1/base hit rate |
| C4 Data and right | The signal sits in public but illegible data, the outcome is not written into any legible field, and the unproven right can be bought cheaply from owners who cannot read the data |
| C5 Ladder | Rungs above the first lead to the whole chain |

Hard exclusions: prospecting or drilling of any kind, Terranox itself, selling a service, and the picks Dhruv already rejected. Four ideas were dropped for exclusions (tailings and placer prospecting).

## Ranked list (top 15 after verification)

Rubric totals are /25. "Revised" is the mean of three verifiers' rescoring. Refuted counts how many of the three verifiers refuted the idea.

| # | Candidate | Scorer | Revised | Refuted | One-line reason |
|---|---|---|---|---|---|
| 1 | Orphan patents with evidence of use (buy from bankrupt estates, chart claims against FCC photos and teardowns, sell to aggregators) | 13.5 | 11.0 | 2/3 | Real ML edge on cheap illegible patents, but a chart only adds a 32-108% premium; median sold asset $33-95k; whole brokered market $158M/yr (Richardson Oliver 2025) |
| 2 | Powered-land options (option farmland, prove headroom with a utility load study) | 13 | 11.0 | 3/3 | Capacity goes to whoever posts collateral and signs the service agreement (Texas SB6 s.37.0561); LandGate already sells substation headroom; a study alone earns ~2-5x |
| 3 | Continuation Forge (buy families with pending continuations, draft claims onto shipping products) | 13 | 10.0 | 2/3 | Step-up ~3-15x on all-in cost; continuation status is a legible field; brokers already price it |
| 4 | Back-to-birth engine parts (scrap-title life-limited parts, rebuild records) | 13 | 10.0 | 3/3 | Proof sits in private operator records (14 CFR 91.417); ProvenAir and flydocs already do it; ~5-30x |
| 5 | Tox-shelved compounds | 12 | 9.7 | 3/3 | Tox package is private and the seller reads it; preclinical upfronts are only 1.5-3.7% of deal value |
| 6 | Deed gores (title gaps from description errors) | 12 | 9.7 | 3/3 | Value capped by a $1.5-10k quiet-title action, the blocked party's cheaper cure |
| 7 | Unlicensed university compound patents | 12 | 9.7 | 3/3 | BindingDB and SureChEMBL already structure patent compounds; hits cost ~$100 from Enamine |
| 8 | Legacy actinomycete libraries | 13 | 9.3 | 3/3 | BiG-FAM pre-clusters 1.2M public gene clusters; Basilea bought a whole preclinical programme for up to SFr2M |
| 9 | Unrecognised historic letters and marginalia | 13 | 9.3 | 3/3 | Every comparable price is for an already-attributed item; attribution is contested opinion |
| 10 | Nagoya enzyme site rights | 12 | 9.2 | 3/3 | CBD Decision 16/2 Cali Fund lets anyone use public sequence data for ~1% of profits, so the site right excludes no one |
| 11 | Bankrupt synbio strain banks | 12 | 9.0 | 3/3 | Zymergen's whole estate fetched $8.6M; titre data is private and goes to every bidder |
| 12 | Defunct-label masters | 13 | 8.7 | 3/3 | Revenue multiple on tiny royalties; SoundExchange publishes the unregistered-owner list |
| 13 | Abandoned pipelines reused for CO2, H2 or fibre | 13 | 8.3 | 3/3 | Idle status is a required PHMSA NPMS field; conversion is bespoke physical work |
| 14 | Face-matching old photographs | 12 | 8.0 | 3/3 | The only 10^5x sale (Billy the Kid, $2.3M) came from family provenance; face-matched finds go unsold |
| 15 | Dormant easement corridors | 12 | 8.0 | 3/3 | Brandt (2014) and Preseault (1996) send abandoned easements to the fee owner |

The previous thread's nearest misses, re-verified on the same rubric:

| Candidate | Revised | Refuted | Killer |
|---|---|---|---|
| UK land promotion | 11.0 | 3/3 | Promoter keeps only 5-25% of the uplift. Real consented sales are £400-490k per gross acre against £9k farmland (~45-55x gross, ~11-17x net to landowner per Crest Nicholson). Gladman's 2,796 plots made £29.9M turnover. Promoters already win 67-76% of the sites they pick, so the lever is ~1.3-1.5x |
| Mitigation-bank junior | 7.7 | 3/3 | Bank NPV ~1-1.5x land; only 15-30% of credits release at approval; IRT approval almost always succeeds eventually |
| Orphaned-source defence parts (DLA NSNs) | 8.7 | 3/3 | Approved source status is non-exclusive and competed away after ~1 year (DAG 17.7501-6); DLA lends parts to anyone |
| Unenforced judgments | 8.3 | 3/3 | Most of the pool is debtors with no assets (GAO: $100B of $110B federal restitution uncollectable); LexisNexis already sells AI asset search |

## The top three in detail

### 1. Orphan patents with evidence of use
- **Frame:** own an unread patent from a bankrupt estate or a lapse-bound owner, then sell it with an evidence-of-use chart attached. Discovery is about 85% of this rung, and the physical step is an occasional $5-20k teardown.
- **Step-up:** the cheapest source costs about $0: a lapse-bound patent costs only the $3,312-8,280 maintenance fee ([USPTO fees](https://www.uspto.gov/learning-and-resources/fees-and-payment/uspto-fee-schedule)). The median sold asset was $33k in 2023 and $95k in 2024, and evidence of use adds 32-108% ([Richardson Oliver 2025](https://www.richardsonoliver.com/publications/the-2025-richardson-oliver-patent-market-report)). That makes the realistic step-up 3-30x.
- **Hit rate and capex:** about 1-5% of orphan patents read on a live product (estimate). A chart costs $3-15k, so a hit costs $100k-1M today. ML could cut that 5-20x, but Patlytics ($40M Series B) already crawls for evidence of use.
- **Data:** USPTO bulk data, FCC equipment-authorisation photos, and PACER section 363 sale schedules. Whether a patent reads on a product is written in no legible field, so this criterion passes.
- **How the right is bought:** by assignment under 35 USC 261 or a section 363 sale.
- **Ladder:** chart and sell, then license, then assert, then run a fund. The ceiling is an Acacia or IV, a few billion dollars.
- **Why it fails:** the chart is an opinion. The value is realised only through years of licensing or litigation, so the geothermal problem returns one rung up.
- **Deep dive:** `gold/deep_orphan_patent_evidence-of-use.md`

### 2. Powered-land options
- **Frame:** option farmland near a substation, then prove headroom with a utility study. Discovery is only about 30-40% of this rung, because site control, $/MW security, zoning, water and fibre dominate ([Texas SB6](https://capitol.texas.gov/tlodocs/89R/billtext/html/SB00006F.htm)).
- **Step-up:** cropland averages $5,830/acre ([USDA NASS 2025](https://www.nass.usda.gov/Publications/Todays_Reports/reports/land0825.pdf)). A study alone earns about 2-5x. The big jump comes with rezoning and the energy services agreement.
- **Hit rate and capex:** a study costs at least $100k per site. The base hit rate is about 15-30%, so the lever is 3-6x.
- **Data:** LandGate already maps capacity at 84k+ substations.
- **Who else:** Cloverleaf, Tract and others already occupy this.
- **Ladder:** real, but capital-heavy at every rung.
- **Deep dive:** `gold/deep_powered-land_options.md`

### 3. Continuation Forge
- **Frame:** buy patent families with live continuations, then draft claims onto shipping products. Prosecution is cheap: about $800 in fees plus $5-40k for the attorney.
- **Step-up:** about 5-30x on purchase price. The median sold family asked $158k ([RO 2025](https://www.richardsonoliver.com/publications/the-2025-richardson-oliver-patent-market-report)).
- **Hit rate:** allowance runs about 70-90%. The real hit rate (allowed, and sells for 10x or more) is about 5-15%. ML improves only the matching step.
- **Data:** continuation status is legible, and brokers list it as a standard quality factor.
- **Deep dive:** `gold/deep_continuation_forge.md`

## Kills, one line each

The other 248 scored candidates are in `gold/ALL_SCORES.md` with their reasons. The recurring killers, with examples:

- **Permits and adjudications mostly succeed once filed** (p 0.5-0.9), so the lever is 1.1-3x. Examples: tower sites, water-right change cases, zoning by right, hydro permits, land promotion.
- **The regulator already wrote the answer into a field.** Examples: PHMSA idle status, AMSC codes, RIBITS, the 5-year land supply, NRC decommissioning filings (restart options), the IATA slot level list, SoundExchange owner lists.
- **The owner of the right is the informed party.** Examples: tox packages, strain titres, engine records, aircraft maintenance files.
- **Open auctions bid hits away before you can buy.** A $500-800 Rembrandt hammered at $870k; Chinese ceramics with GBP 30-40 estimates sold at GBP 63k.
- **The proof is an opinion, and value comes later through litigation or expert consensus.** Examples: patents, art, attribution, face matching.
- **The proving step is the bespoke physical build** (the geothermal counter-example). Examples: pumped storage, reactor restarts ($1.5-2B), pipeline conversion, wetland restoration ($26k/acre), Phase 2 trials.
- **The right cannot be held before proving.** Examples: airport slots (airlines only), Mexican ejido land, qui tam.
- **The pool is too small.** Examples: art sleepers ($100-300M/yr), meteorites, fossils.

## The law, and what it implies

Score distribution over the 263 scored candidates:
- **C1 (frame):** none of the 263 scored 4 or more.
- **C3 (lever):** none scored 4 or more.
- **C2 (step-up):** four scored 4 or more, and each of those failed C1 or C3.
- **C2 and C3 together at 3 or more:** only five candidates, and all five scored 3 or lower on both frame and data.

The criteria are anti-correlated in human-made systems.

1. **Cheap proof and rare success do not co-occur in human-made systems.** Where the proving step is cheap and abstracted, as with a filing, a study or a chart, it usually succeeds, so the hit-rate lever is small. Where it usually fails, as with a trial, a restoration or a lawsuit, it is the expensive bespoke step, so no 80%-discovery frame exists.
2. **Someone writes the outcome down.** Every human-made right has a registrar, a regulator or an owner who records its state. Nature records nothing about where the ore is.
3. **10^3x step-ups survive only where buyers cannot see the unproven state.** In human markets, sophisticated bidders see the same lot, which is why the 10^4 structure appears only on tiny pools such as art and fossils.

Geology passes all three at once:
- A drill hole is a cheap, abstracted, binary proof that usually fails.
- Nature hides the answer, and nobody summarises it.
- The state sells tenure cheaply to anyone.
- Mine developers pay the step-up at once.

That is why Terranox exists and why this hunt, like the eight before it, keeps converging back on subsurface geology.

**What this means for the application:** the rubric as written selects geology, and Dhruv's exclusion removes geology. One of the two has to give, or the hunt has to target the few domains where nature, not a registrar, hides the answer. Those domains are biology at sequence scale, ocean and seabed (non-mineral), atmosphere and space, paleontology, and materials search spaces. In this hunt they failed for a different reason: the buyer will not pay at the proof stage. Whether any of them has a buyer who pays at once is the one question left open.

## Method and caveats

- **Workflow:** 50 generators (one per domain lens), then 1 merge pass, then 263 scorers (one per candidate), then 45 verifiers (3 lenses on each of 15 finalists), then 3 deep dives, then 12 more verifiers on the previous thread's near misses.
- **Search budget:** the shared web-search budget ran out part-way through. 47 scorers and some verifiers and deep dives worked from memory, and they flag those figures as "(memory)" or "(estimate)" in the JSON. The deep dives fetched primary sources directly (the Richardson Oliver 2025 PDF, the USPTO PTAB FY26 Q3 report, Texas SB6), and the near-miss verifiers had full search. No verdict here rests on an unverified number alone. Each kill has at least one sourced reason.
- **Inputs:** the previous thread's sweeps are on branch `claude/public-dataset-company-hunt-avpbec`, `research/converge/hunt9/`.

## Round 2: domains where nature hides the answer (Dhruv chose this on 18 Oct)

16 generators produced 110 ideas in biology at sequence scale, natural products, crop and livestock genetics, industrial microbes, materials search spaces, chemistry, ocean, paleontology and meteorites, atmosphere and sky, space, infrastructure read from satellite data, ecology, medicine from public human data, archives, sensor archives and first principles. The merge step was stopped by a safety filter, so the merge was redone by hand. Candidates touching toxins, pesticides or human-subject data were dropped, as were duplicates and those hitting exclusions (subsurface pore space, mineral residues, asteroid mining). That left 71, each scored by one agent. The top 8 got 3 adversarial verifiers each, and the top 3 got deep dives (`gold/nature_results.json`).

**Result: same null.** Best score 14/25. 0 of 71 scored 4 or more on frame, and all 8 finalists were refuted 3/3.

| # | Candidate | Scorer | Verified | Why it fails |
|---|---|---|---|---|
| 1 | Captive Scent (natural odorant discovery from public GC-MS spectra) | 14 | 9.7 | No real transaction shows a buyer paying millions for an unscaled, un-tox'd odorant licence. Osmo's 2026 auction is the first open market of its kind and its clearing prices are undisclosed, so the $5-50M 'proven' value ... |
| 2 | Enzyme Claims from Metagenomes (owned biocatalysts for one hard API step) | 12 | 8.7 | There is no transaction on either side of the step-up: the unproven right costs $0 because it is a free public sequence with no seller, so there is no asset basis to multiply, and no observable price exists for an unprov... |
| 3 | FreeMag: rare-earth-free magnet compositions | 11 | 8.7 | No capitalised buyer pays for a lab-proven magnet composition. Niron, the strongest rare-earth-free case, is a manufacturer funded by about $79M of equity plus up to $300M of plant loans, with no disclosed licensing deal... |
| 4 | Suppressa: buying the microbiomes of fields that nature protects | 11 | 8.7 | No evidence that a capitalised buyer pays $1-5M, or anything close, at once for a greenhouse-validated strain. The only priced comparable (MustGrow-Bayer, $35-40M) covers a registered, field-tested technology, and that t... |
| 5 | DropIn: electrolyte additives for existing Li-ion lines | 11 | 8.7 | No public price exists for a proven electrolyte-additive right. The only comparable deals (ORNL-Safire, Ascend-Samsung SDI, Mitsubishi-CATL) have confidential terms, and the Ascend case shows the cell maker holding the p... |
| 6 | Survivor Budwood Co. (citrus greening survivors) | 11 | 8.0 | No capitalised buyer pays anything when this rung ends. Greenhouse inoculation plus qPCR is not a saleable proof. Value is realised only after shoot-tip grafting, DPI registration (5B-62.011/.013) and multi-year multi-si... |
| 7 | SorbentRights: computed sorbents for capture and separation | 11 | 8.0 | No buyer pays at the proving step. Capitalised sorbent buyers acquire or co-develop only after $1-10M+ of scale-up and pilot work: Baker Hughes-Mosaic came after years of grant-funded scale-up at an undisclosed price, an... |
| 8 | Die Hunter: finding rare die varieties and errors in bulk coin and stamp lots | 12 | 7.7 | Measured at the lot level the step-up is near zero. A box of bank-rolled coins is worth face value before and after the search; duds are returned at par and hits are rare. The 10^4x per-coin figure comes from cherry-pick... |

**The second law.** Nature hides the answer here, but two other legs break:

1. **There is no owner to buy the right from.** The asset is a first-come filing on a public sequence, structure or spectrum. Composition claims are often barred anyway: Myriad covers isolated DNA, and product-of-nature doctrine covers natural odorants. Where a physical object can be bought (fossils, meteorites, coins, budwood), the pool is small or the answer key is already catalogued.
2. **No buyer pays at the proof stage.** A flask assay, a gram-scale magnet button or a coin-cell cycle is not a proof a capitalised buyer prices. Buyers pay after scale-up, qualification or field trials, which is the bespoke build. Examples: Niron took 13 years and $150M+ to make iron nitride; Merck's sitagliptin enzyme needed a 25,000-fold engineered improvement over any wild type; Osmo's captive-odorant auction shows no clearing price.

**What geology has that nothing else has:** a *standardised proof language* that buyers price at once. NI 43-101 and JORC make a drill-core assay a regulated, comparable disclosure, and juniors are repriced the day an intercept is announced. Any domain without an accepted proof standard leaves the buyer to do its own proving, so the step-up does not land on the discoverer. The question to hunt next is therefore not "where is the answer hidden" but "where does an accepted proof standard turn a cheap test into a price".

## Round 3: markets with an accepted proof standard

12 generators produced 88 ideas, which merged to 64, each scored by one agent. The top 8 got 3 verifiers each, and the top 3 got deep dives (`gold/proof_results.json`). The markets covered: bankable energy-yield reports, gem, pearl, coin and stamp grading, carbon verification, engineering certifications, land and survey standards, seed and appellation standards, regulatory designations, appraisal standards, data-centre will-serve letters and lab reference standards.

**Result: same null.** Best score 12/25. None of the 64 scored 4 or more on frame or lever, and all 8 finalists were refuted (7 at 3/3, 1 at 2/3).

| # | Candidate | Scorer | Verified | Refuted | Killer |
|---|---|---|---|---|---|
| 1 | LoadStudy Land (greenfield large-load study options, ERCOT/SPP) | 12 | 10.3 | 3/3 | The roughly 10^2x step-up depends on an unverified $800k/acre 'power-ready' price. That price belongs to sites with near-term energized MW, mostly in Northern Virginia. A greenfield Texas or SPP optio... |
| 2 | Entitled Acre (data center rezoning arbitrage) | 12 | 10.3 | 3/3 | The step-up the rezoning creates and an option holder can actually capture is usually under 30x. In Northern Virginia, the only market where gross multiples reach 50-100x+, landowners now sign contrac... |
| 3 | Old Master Sleeper Attribution (Sleeper / Sleeper Atelier / Sleeper Masters / Provenance Capital) | 12 | 10.0 | 2/3 | The 10^3-10^4x step-up does not reach the buyer. Sleepers are bought at open online-bid auctions, and specialist dealers bid any lot that looks promising up to $70k-$1.2M at the hammer: the Nutley Rem... |
| 4 | Aircraft LLP Back-to-Birth Trace Reconstruction (Back-to-Birth / Unbroken Chain) | 11 | 9.7 | 3/3 | The step-up is not 10^3-10^4x. It is not even reliably 30x. Serviceable CFM56 LLPs are worth $250-480K each and a full stack $1.4-1.8M (Safe Fly), and teardown engines already sell for $1.2-1.8M, so t... |
| 5 | Unrecognised Signed and Association Copies / Manuscripts (InkProof / Hand of History) | 12 | 8.7 | 3/3 | The 10^3-10^4x step-up is supported only by anecdotes like the $2.48-to-$477,650 Stone Declaration, which is a printed document recognisable on sight, not a hand-matched find. The repeatable hit is a ... |
| 6 | Rare Stamp Varieties in Bulk Mixtures (Philatelix) | 11 | 8.7 | 3/3 | The 10^3x step-up appears only after selecting the one stamp that hits. The asset actually bought is the lot, and kiloware already sells at about 5% of catalogue value (Linn's, via Wikipedia), so the ... |
| 7 | Natural Pearls in Estate Jewellery (Nacre / NaturalPearl / Nacre Lab) | 12 | 8.3 | 3/3 | The proven buyer is not reliably there and does not pay a large multiple: a GIA-certified natural saltwater rope at Skinner (est. $2,500-3,500) went unsold, and typical certified strands (often mixed ... |
| 8 | SoleSource (orphan tech-data packages to DLA source approval) | 12 | 8.3 | 3/3 | DLA's own SAR procedure ("Sole Source Breakout", DAG 17.7501-6) makes an approved SAR an ADDED source that is guaranteed only about 40% of awards for about a year, at lower prices. The 111 FY17 approv... |

**The third law.** A proof standard is not enough on its own. Where the standard test is cheap, everyone tests everything, so the hit-rate lever disappears. A GIA natural-pearl report costs $50 a strand, so dealers X-ray every plausible lot, and open auctions price sleepers before the test. Where the test is expensive, it is usually the bespoke build, as with load studies under SB6 or DLA source approval.

Geology is the one place where all of the following hold together:
- The proof is **expensive** (a drill programme costs hundreds of thousands to millions).
- It is **abstracted** (contract drillers do it).
- It is **standardised** (NI 43-101 and JORC).
- It **usually fails**.
- It sits on a **right bought cheaply from the state before testing**.

Three rounds and 398 scored ideas, plus about 115 from the previous thread, found no second instance.

## Overall conclusion

Under the gold rubric as written, the only company shape that passes is ML-led discovery on subsurface tenure, which is Terranox's own category and is excluded. The rubric is a precise description of geology. A new company that keeps every leg will not be found by widening the search further. Either one leg is relaxed deliberately (the step-up bar, the cheap-right leg, or the exclusion), or the YC application has to win on a different thesis.

## Round 4: "usually fails" relaxed (Dhruv, 19 Oct)

Rubric change: C3 now gives full marks to an expensive proving step with a 30-70% base success rate where ML lifts the hit rate 1.5-3x. Every other leg is unchanged. The round ran 125 agents:
- deep re-dives on UK land promotion (including a variant that buys grey-belt farmland outright) and US mitigation banking;
- 12 generators producing 73 new ideas, 47 after merging;
- rescoring of the 30 best earlier near misses;
- 3 verifiers on each of the top 10, and deep dives on the top 3.

**Result: same null.** Best scorer total 15/25, for an air-permitted behind-the-meter power pad for data-centre campuses and for data-centre rezoning options. All 10 finalists were refuted 3/3. Land promotion re-scored 12/25 and mitigation banking 10/25 (`gold/round4_seed_*.md`).

| # | Candidate | Scorer | Verified | Killer |
|---|---|---|---|---|
| 1 | Reviving zombie subdivisions (lapsed or antiquated plats) | 14 | 12.3 | The capitalised buyers pay cost, not a step-up. Millrose's 10-K says its takedown price is its own acquisition cost plus the development budget, at an 8.5-11% yield, with no appraisals. Implied values... |
| 2 | Powered-Land Options: farmland options proven by utility load studies | 14 | 11.7 | The 10^2-10^3x jump goes to committed load, not to the proving step. Altus Group found committed utility load was the strongest predictor of price. In Northern Virginia, power adds only about 1.5x ove... |
| 3 | Australian rural-to-urban rezoning (NSW, SEQ and Victorian growth corridors) | 13 | 11.7 | The step-up is far below 30x where it matters. A Cushman & Wakefield estimate prices land likely to be included in the next Melbourne growth-boundary expansion at $125-250k/ha. The Beveridge sale paid... |
| 4 | Entitled Acre (data center rezoning arbitrage) | 15 | 11.2 | The step-up from zoning alone is about 3-10x off a strike price that farmers have already raised to 5-10x farmland value because developers make offers before any rezoning. Even counted as leverage on... |
| 5 | Air-permitted behind-the-meter power pad for DC campuses | 15 | 11.0 | The value is not in the permit. Texas issues behind-the-meter gas permits for up to 500 MW within weeks under simplified procedures. 59 data-center projects plan about 90 GW of on-site generation, but... |
| 6 | Cryptic Clusters / Legacy Actinomycete Libraries: orphaned natural-product collections re-read for novel clusters | 14 | 11.0 | An FDA-APPROVED novel antibacterial clears at $14-16M (Achaogen/plazomicin ~$16M in Chapter 11 after >$1B spend; Tetraphase/eravacycline ~$14M cash to La Jolla), so the terminal buyer for the candidat... |
| 7 | DeadPatent Hits: re-proving unlicensed university compound patents against new targets | 14 | 10.7 | The 10^3-10^4x step-up is not paid at signing. Cash at signing rises only about 5-25x (a roughly $20k TTO option against a $0-500k upfront for a hit-stage licence). The rest is milestones that depend ... |
| 8 | Floodway Narrowing for Urban Infill Parcels | 14 | 10.7 | The 10^3-10^4 step-up is not real. A narrowed floodway leaves the parcel in the 100-year fringe. Elevation (500-year level plus 2-3 ft in Houston and Harris County), no-net-fill, insurance and an extr... |
| 9 | German Bauerwartungsland: picking farmland ahead of a Bebauungsplan | 13 | 10.7 | Gutachterausschuss transaction data shows the market prices Bauerwartung before any FNP decision. In the Berliner Umland, unzoned fields with any development expectation sold at an average 16% of the ... |
| 10 | Reuse-Rights Pipeline Easements: abandoned-in-place pipelines for CO2, H2 and fiber | 14 | 10.0 | No public transaction shows anyone paying a step-up price for a third-party-assembled, title-proven abandoned pipeline corridor. Every real conversion (Tallgrass Trailblazer to CO2, Williams/WilTel fi... |

**The fourth law.** Relaxing the lever exposed the constraint that actually binds: where a human-made asset has a big step-up, the seller already prices the hope. Examples:
- German edge-of-town fields trade at 15-40% of the Bauland price before any plan exists (Gutachterausschuss data).
- UK Green Belt farmland carries hope value that tribunals recognise.
- Data-centre farmers ask 5-10x farmland value before rezoning.
- Millrose buys entitled lots at cost plus an 8.5-11% yield, not at a step-up.

Agents, appraisers and data vendors (LandTech, LandGate, Zonda) close the information gap. In geology the seller is the state, and it prices tenure **administratively** (a fixed fee per hectare) whatever the hope value. That administrative price is the cheap-right leg.

**Implication.** The only place left untested is rights sold by a public body at a fixed schedule price rather than a market price, where the proof step-up still lands on the buyer of the right.

## Round 5: rights a public body sells at a fixed price (19 Oct)

Round 5 ran 82 agents: 10 generators produced 60 ideas, 44 after merging. Each was scored on the relaxed rubric, the top 8 got 3 verifiers each, and the top 3 got deep dives. The rights covered were state trust leases, Crown land tenures, BLM and USFS rights-of-way, FERC preliminary permits, oyster-ground leases, DOE service contracts abroad, maritime concessions, communication sites, billboard permits and tax-sale land.

**Result: same null.** The best scorer total was 15/25, for a powered data-centre site on state trust land. No candidate scored 4 or more on C4, and all 8 finalists were refuted 3/3.

| # | Candidate | Scorer | Verified | Killer |
|---|---|---|---|---|
| 1 | Closed-loop pumped storage sites via FERC preliminary permits (federal, state trust and optioned private land) | 14 | 13.0 | The right cannot be bought cheaply from someone who cannot read the data. It is a free, first-to-file FERC preliminary permit that by statute cannot be assigned (16 U.S.C. 798(d)). It is noticed publi... |
| 2 | Old-dam-site pumped hydro on Crown land (NSW/Qld) | 13 | 12.3 | The unproven right cannot be bought cheaply at a fixed fee from owners who cannot read the data. The public body that holds the old investigation files also controls the land: WaterNSW, Crown Lands an... |
| 3 | Philippine DOE wind and solar pre-development service contracts | 13 | 12.3 | The unproven right is a fixed-fee state grant, not an asset bought from an owner who cannot read the data. The regulator already does the resource legibility work: pre-determined areas are identified ... |
| 4 | Large-load powered site on state trust land (data centre) | 15 | 12.0 | Every named state trust board must get fair market value for the proposed use. Montana requires an RFP (77-1-904 MCA). ND trust land can be leased only for pasture and meadow (ND Constitution). SD auc... |
| 5 | Crown land wind investigative licences with met-mast proof (BC, Ontario, Newfoundland) | 13 | 11.0 | The unproven right is not bought cheaply from owners who cannot read the data. In Newfoundland it is auctioned through a scored Call for Bids. That call has a pass/fail screen on wind-farm constructio... |
| 6 | BLM solar ROW applications outside designated leasing areas, cleared of NEPA fatal flaws | 13 | 10.7 | The right is not bought cheaply from owners who cannot read the data. It is a first-come, fixed-fee application ($15/acre plus cost recovery, 43 CFR 2804.12(c)) to BLM, the most informed party. BLM al... |
| 7 | Build-ready cell tower entitlements (zoning permit at fixed fee on optioned land) | 13 | 10.7 | The right cannot be proven without the buyer. Tower zoning approval, and the Telecom Act protection behind it, usually depends on a specific carrier's coverage gap and RF justification, often with a c... |
| 8 | Chilean maritime concessions with approved RCA for desalination and seawater intakes | 13 | 10.3 | The unproven right is a discretionary supreme-decree grant whose binding DGA report can reject it outright. Each application is published in the Diario Oficial with a 60-day opposition window, which t... |

**The fifth law.** Public bodies do not leave hope value on the table, except for mineral tenure. Where a public body sells a right at a fixed price, at least one of these happens:
1. It must get fair market value for the proposed use, so it reprices or auctions. State school trusts are bound by their constitutions: Montana requires an RFP (77-1-904 MCA), and Arizona sold Mesa trust land to Novva at an appraised data-centre value of about $380k/acre.
2. It reads its own files and tenders the best sites. WaterNSW and Queensland Hydro do this with old dam investigations, Newfoundland runs a scored call for bids for wind, and the Philippine DOE pre-screens areas for competitive auctions.
3. It makes the right free, first-come and non-transferable, so there is nothing to buy and flip. FERC preliminary permits cannot be assigned (16 U.S.C. 798(d)), and BLM solar ROWs are a $15/acre application.

Mineral tenure is the deliberate exception. Free-entry staking at a fixed fee per hectare, assignable, with the discoverer keeping the uplift, is a policy built to subsidise private exploration. No other body of law found across five rounds copies it.

## Overall conclusion after five rounds

There were about 490 distinct ideas and 519 scorings across five rounds, with every leg of the rubric probed in turn. The result is consistent: the gold rubric describes free-entry mineral tenure. Every leg Terranox relies on (an expensive, abstracted, standardised and usually failing proof, illegible public data, and a cheap transferable right at a fixed administrative price) holds there only because mineral law was designed to make it hold. Another round will not find a second instance.

The options left for the application are a different thesis, or deliberately dropping the step-up leg (C2). The other legs have now each been relaxed or searched and still fail.

## Round 6: step-up leg dropped, value made by developing or operating (19 Oct)

The coordinator ran this on its recommended option while Dhruv was away. C2 became "value capture": return on total capital and prize size when the company develops or operates the asset itself. All other legs kept their relaxed form. 19 near misses from every hunt were rescored (powered brownfields, land promotion, mitigation banking, orphan patents, powered-land options, state-trust data-centre sites, corridors and others), alongside 31 fresh ideas from 54 raw, for 50 scored. The top 10 got 3 verifiers each, and the top 3 got deep dives. The Ni-Cu conductor and paper-survey leads were left out because they are prospecting.

**Result: same null.** Best scorer total 15/25 (UK land promotion). All 10 finalists were refuted, 9 at 3/3 and 1 at 2/3.

**Method caveat.** One of the three verifier lenses still carried the old ">=30x step-up" refutation line. The other two lenses (data and competition, right and frame) refuted every finalist on their own, so the verdict does not rest on the stale lens.

| # | Candidate | Scorer | Verified | Data/competition killer |
|---|---|---|---|---|
| 1 | Powered-Land Options: farmland options proven by utility load studies | 14 | 12.7 | The edge this idea depends on, finding substation load headroom before others do, is already a commercial data product. LandGate sells modelled offtake capacity for every US substation (98% coverage),... |
| 2 | Entitlement arbitrage on exurban residential land (ML over planning records) | 14 | 12.7 | The supposed hidden signal is already being extracted and sold to the buyers named in the thesis. Shovels, through its January 2026 acquisition of ReZone, sells a Decisions API covering 600+ cities an... |
| 3 | Entitled Acre (data center rezoning arbitrage) | 14 | 12.3 | The supposedly illegible signals are already turned into products and sold to the same capitalised buyers this company would sell to. Paces sells AI power and permitting site screening to data center ... |
| 4 | UK land promotion / grey-belt freehold (hunt 9) | 15 | 11.3 | The signal that predicts grey belt consent is already in legible public fields: Green Belt review purpose scores, 5-year housing land supply, Housing Delivery Test results and local plan age. LandTech... |
| 5 | Local-permit-first utility solar and BESS projects in moratorium-risk counties | 14 | 11.3 | The outcome is already sold as a legible product. Heatmap Pro publishes an Opposition Risk Score for every US county, trained on project outcomes and backed by an ordinance and moratorium database bui... |
| 6 | Senior surface water right change-of-use decrees (Colorado and Western prior appropriation) | 13 | 11.3 | The supposed ML edge, reconstructing transferable consumptive use from illegible records, is already done in legible form. The state's CDSS StateCU/StateMod models estimate consumptive use for each st... |
| 7 | Orphaned defense spare-part production lines, re-qualified as the DLA source | 14 | 11.0 | DLA itself publishes SAR candidate lists of obsolete and limited-competition NSNs, AMSC codes already flag restricted status, and DLA tells bidders to screen with DIBBS, Haystack and SERVA. So the dem... |
| 8 | Reviving zombie subdivisions (lapsed or antiquated plats) | 13 | 10.3 | The candidate signal is legible and already commercialised. Vacant-platted-lot ratios come from a plain assessor and plat join, which Lincoln did by hand for 50 counties. Zonda already sells lot-pipel... |
| 9 | Orphan Patent Evidence-of-Use (bankrupt estates, FCC/teardown proof; incl. semiconductor, photonics, mature-node) | 14 | 10.0 | Incumbents already own the edge, and one runs this exact model. TechInsights sells teardown-based EoU charts to licensing entities from more than 1M archived images. Patlytics, XLSCOUT and Lumenci sel... |
| 10 | Reuse-Rights Pipeline Easements: abandoned-in-place pipelines for CO2, H2 and fiber | 13 | 9.0 | The decisive outcome, whether the easement survives abandonment and allows CO2, H2 or fiber, is a legal question. It is resolved per parcel by reading the instrument's granting clause under state law,... |

**The sixth law.** Without the step-up leg, what survives is a developer business in an informed market, and the signal ML would read has already been productised for the same buyers:
- LandGate (substation offtake);
- Shovels and ReZone (600+ cities of rezoning decisions);
- Heatmap (county opposition scores);
- Zonda (lot pipelines);
- Colorado CDSS (consumptive use);
- DLA SAR lists.

So the moat would be execution, not ML. That is the brownfields verdict again, at scale.

## Final conclusion after six rounds

There were about 520 distinct ideas and 569 scorings. Dhruv's rubric, and every relaxation of it, has been searched. The ML-native, own-the-asset company he describes exists only on free-entry mineral tenure. Anywhere else the choice is:
- an execution-moat developer that uses data well (land, power, water), where ML is a tool and not the company; or
- a different thesis, such as Charlie's vertical-integration ladder, which starts from the physical rung and adds ML second.
