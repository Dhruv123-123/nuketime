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
