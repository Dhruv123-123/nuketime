# V5 deeptech sweep: own the material, let AI do the slow part (19 Oct 2026)

Frame: `V5_OPTIMIST.md`. Tech is assumed to work. The bar is the numbers and the clock. Lessons carried in from `deep_crop_actives.md` and `VERDICT.md`:
- licensing an ML molecule pays like a research grant (AgPlenus: $1-3M/yr);
- registration ($307M, 11 yrs) kills anything that needs a new regulated active;
- L9: policy premiums decay;
- L7: a pure ML tool gets sold to incumbents.

So every idea below owns a product and is chosen where **qualification is short or skippable**. The rule used to pick them:

> **Fast-qual rule.** The buyer can test the product in its own plant in weeks to months and sees the payoff in its own P&L (metal recovered, clinker saved, wells kept flowing). The molecule is built from chemicals already on TSCA/REACH inventories, so it needs no new-substance registration.

Status labels: **(src)** = web-checked this session, **(mem)** = from memory and not re-checked, **(der)** = derived here.

## Verdict
**Two ideas pass (19+, no leg below 3) and three near-miss at 18.**

| Rank | Idea | Score | Why it works |
|---|---|---|---|
| 1 | **Value-share flotation reagents (copper first)** | **20** | Trial in weeks; payback is visible in metal at about $14.7k/t copper; owns the reagent and a share of the extra metal |
| 2 | **Low-clinker admixture system** | **19** | Ready-mix trials take weeks; AI predicts 28-day strength from 1-3 days of data; the market is about $20-22B and Sika is the comparable |

Near-misses at 18:
- ex-China polymetallic scrap refinery (Dy/Tb + W + Ga);
- autonomous oilfield production chemicals;
- AI process roll-up of specialty chemicals.

Batteries, magnets, semiconductor chemicals and PFAS replacements all fail on the same three things: qualification takes 2-5 years, a funded incumbent or Chinese price-setter holds the rung, or the policy premium decays (L9).

## Ranked table (32 ideas)
Columns: **N** numbers close, **T** time, **C** ceiling, **A** AI answers the killers, **D** defensibility (each scored 1-5).

| # | Idea (one line) | Vertical killer(s) | AI counter-move (quantified) | Rough numbers | N | T | C | A | D | Tot |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Flotation reagents priced on extra metal recovered**: AI-designed collectors and depressants, built from TSCA/REACH-listed chemistry, tuned per ore body | Conservative metallurgists; ownership of plant trials; Syensqo/Clariant/Chinese xanthate price war; baseline disputes; new-substance registration | Ore mineralogy (QEMSCAN/MLA) plus a robotic lab-flotation rig screens 200-500 formulations in 4-8 weeks vs 6-12 months, so cost per mine qualified falls from ~$1M to ~$150k (der). Search limited to listed substances, so 0 registration. ML recovery attribution with a plant digital twin settles the baseline | Cu $14,751/t (src). A 100 kt/yr concentrator +1.5 pts recovery = 1.7 kt = ~$25M/yr; a 30% share is ~$7.5M/yr per mine (der) | 4 | 4 | 4 | 4 | 4 | **20** |
| 2 | **Low-clinker admixture system**: AI-designed PCE/accelerator chemistry plus an ML strength predictor, letting ready-mix plants replace a further 15-25% of cement with calcined clay/limestone/slag | Prescriptive DOT specs; 28-day strength cycles; liability; Sika/Saint-Gobain (Chryso+GCP) | Calorimetry + maturity + ML predicts 28-day strength at 1-3 days, so a mix-design cycle drops from ~3 months (3×28 d) to ~2-3 weeks. Uses the performance specs ASTM C1157 / C595 Type IT for private work. Same chemistry families, so no registration | US 379M yd³ (2024, src). Saves ~$2-4/yd³ in cement (der); capture $1-1.5/yd³. Admixtures $20-22B (src) | 4 | 4 | 4 | 4 | 3 | **19** |
| 3 | Ex-China polymetallic scrap refinery: Dy/Tb from magnet swarf, W from carbide scrap, Ga from wafer/LED scrap, on one AI-reconfigurable hydromet line | L9 premium decay; feedstock access; DoD-funded rivals; commissioning SX cascades takes 2-3 yrs | ML solvent-extraction flowsheet design plus autonomous commissioning: 24-36 → 9-12 months (der). One line switches between metals and follows whichever premium is widest | Dy oxide CIF Europe ~$3,500/kg, 16x China; Tb $6,745/kg; APT ~$3,000+/mtu (~10x 2024); 6N Ga ~$2,350/kg (src) | 4 | 4 | 4 | 3 | 3 | 18 |
| 4 | Autonomous oilfield production chemicals: AI-designed scale/corrosion/paraffin packages, sold through telemetry tanks and autonomous dosing pumps with no field-tech fleet | Incumbents bundle chemicals with truck and technician; oil-price cycles; SLB-ChampionX scale | Per-well ML (produced-water chemistry from USGS/RRC data plus pump telemetry) dispatches 50% fewer field visits, taking gross margin from ~35% to ~50% (der). Field trial in 2-6 weeks | Oilfield chemicals ~$30B (src); ChampionX $3.76B revenue, 64% production chemicals; SLB paid $7.8B (src) | 4 | 4 | 4 | 3 | 3 | 18 |
| 5 | Specialty chemical AI roll-up: buy PE-owned plants ($20-100M revenue) and use self-driving process optimisation (yield/energy, not formulation, so no customer requalification) | PE holds the rung; prices at 8-10x EBITDA; integration | +2-5 pts yield and −10-20% energy on a 15% EBITDA business lifts EBITDA ~30-50% (der) and turns 9x entry into ~6x | Specialty chem M&A is deep; Element Solutions/Quaker are the comparables (mem) | 4 | 5 | 4 | 3 | 2 | 18 |
| 6 | Chalcopyrite leach catalyst, run on miners' low-grade stockpiles for a share of cathode (Jetti-shaped) | Column tests take 12-18 months; plants cost $20-100M; Jetti/Ceibo/Nuton lead | Mineralogy-to-recovery ML cuts column testing to ~3-4 months; AI lixiviant design | Jetti $2.5B valuation (src); Ceibo $30M B (src) | 3 | 3 | 5 | 3 | 3 | 17 |
| 7 | TIM for AI accelerators (TIM2/server level): liquid-metal/PCM composites | Nvidia/TSMC choose TIM1; 1,000-cycle reliability tests | ML pump-out/dry-out predictor shortens thermal cycling from ~6 to ~2 months | TIM $2.56B (2025), 9% CAGR (src) | 4 | 4 | 3 | 3 | 3 | 17 |
| 8 | Tungsten-only carbide-scrap → APT refinery in the US | L9; H.C. Starck/Plansee expanding (src) | AI zinc-process/oxidative-leach control | APT ~$3,000/mtu (src) | 5 | 4 | 3 | 3 | 2 | 17 |
| 9 | Heavy RE (Dy/Tb) separation only | Crowded: Lynas 1,500 t SEG, Phoenix ($500M DoD loan), Vulcan ($1B+), USAR (src) | AI ligand and SX design | Ex-China Dy/Tb ~$1.5-2.5B at current prices (der) | 4 | 4 | 3 | 3 | 2 | 16 |
| 10 | Drop-in hydroprocessing/FCC catalysts with performance insurance | Changeout cycles of 2-4 yrs; Shell/Topsoe/Ketjen/Axens/ART | 64-reactor pilot plus ML kinetics yields a guaranteed-performance bid within 3 months | Refinery catalysts $5.5-6.3B (src); Ketjen control went to KPS for small proceeds (src) | 3 | 3 | 3 | 3 | 3 | 15 |
| 11 | Halogen-free flame retardants for EV packs/electronics | Clariant/ICL/Lanxess; UL 94 is fast, but OEM approval takes 12-18 months | AI synergist design; UL pre-screen in silico | FR ~$8-9B (mem) | 3 | 4 | 3 | 3 | 3 | 16 |
| 12 | Industrial water chemistry for data-centre cooling | Ecolab service model | AI dosing replaces technicians | Ecolab ~$15B revenue (mem) | 3 | 4 | 4 | 3 | 2 | 16 |
| 13 | Lubricant/e-fluid additives (EV e-axle, industrial) | 4-firm oligopoly; engine-oil approvals cost $1-2M and 2-3 yrs | Target non-API fluids; ML predicts test sequences | Additives $14.7-18B (src) | 3 | 3 | 4 | 3 | 3 | 16 |
| 14 | ABF-alternative build-up dielectric for AI packaging | Ajinomoto ~sole producer; substrate maker plus Nvidia qualification 18-36 months | AI low-Df/low-CTE resin; DOE-style test reduction | ABF sizing $3.75-11.6B, inconsistent (src) | 3 | 2 | 4 | 3 | 4 | 16 |
| 15 | Ga/Ge recovery from fab, LED and zinc residues | Small market | AI sorbent design | 6N Ga $2,350/kg ex-China (src); ceiling <$1B | 4 | 4 | 2 | 3 | 3 | 16 |
| 16 | Tailings reprocessing (buy legacy tailings, recover Cu/Co/Au/REE) | Seller prices the hope (L3); permitting; sampling borders on "drilling" | AI mineral mapping from historical mill records | Phoenix Tailings, Regeneration (mem) | 3 | 3 | 4 | 3 | 3 | 16 |
| 17 | Dirty (high-As) copper concentrate → clean cathode | Plant capex $300M+ | AI hydromet design | Concentrate penalties (mem) | 3 | 2 | 4 | 3 | 3 | 15 |
| 18 | Biocide-free marine antifouling sold on fuel-savings guarantee | Drydock cycles of 30-60 months; Jotun/Hempel | AIS plus noon-report ML proves savings in ~3 months (ISO 19030) | Antifouling ~$4B (mem) | 3 | 3 | 3 | 3 | 3 | 15 |
| 19 | Dy-free/Ce-substituted NdFeB magnets | Auto PPAP 18-36 months; Noveon $215M C, Vulcan, Niron (src) | ML grain-boundary design | NdPr $106-109/kg (src) | 3 | 3 | 4 | 2 | 2 | 14 |
| 20 | Superalloy/refractory AM powders (C103 etc.) for defence/space | Alloy allowables take 2-5 yrs | ICME + ML allowables | Niche (mem) | 3 | 3 | 3 | 3 | 3 | 15 |
| 21 | Captive fragrance molecules | Osmo; failed size earlier | ML olfaction | Givaudan comparable | 3 | 4 | 3 | 3 | 2 | 15 |
| 22 | Antimony refining in the US | Small; feedstock | AI process control | Ceiling <$1B (mem) | 4 | 3 | 2 | 3 | 2 | 14 |
| 23 | REBCO superconducting tape | Demand early (fusion) | AI deposition control | Faraday Factory (mem) | 2 | 3 | 4 | 3 | 3 | 15 |
| 24 | Synthetic graphite anode, non-China | Cell qualification 2-3 yrs; Novonix struggling | AI furnace control | AD/CVD support (mem) | 2 | 2 | 4 | 3 | 2 | 13 |
| 25 | Li-ion electrolyte additives | Chinese commodity; per-cell qualification 12-24 months | AI molecule design | ~$1.5B (src); top supplier 15% share | 2 | 3 | 2 | 3 | 3 | 13 |
| 26 | Semiconductor ALD/CVD precursors | Fab qualification 18-36 months; small market | AI precursor design | $0.6-0.7B (src) | 3 | 2 | 2 | 3 | 3 | 13 |
| 27 | PFAS-free fluoropolymer replacements | EU derogations 6.5-13.5 yrs weaken the pull (src) | AI polymer design | Fluoropolymers ~$9B (mem) | 2 | 2 | 4 | 3 | 2 | 13 |
| 28 | Silicon anode | Group14/Sila ahead; auto qualification 3-5 yrs | — | — | 2 | 2 | 4 | 2 | 2 | 12 |
| 29 | Na-ion cathode | Natron shut 2025 (mem) | — | — | 2 | 2 | 3 | 2 | 2 | 11 |
| 30 | DLE sorbents on oilfield brine | Li price; project capex | AI sorbent design | Lilac/EnergyX (mem) | 2 | 2 | 4 | 3 | 2 | 13 |
| 31 | Black-mass hydromet recycling | Li-Cycle failure; feedstock | AI process control | (mem) | 2 | 3 | 3 | 2 | 2 | 12 |
| 32 | Non-PGM electrolyser catalysts | Hydrogen demand collapse | AI catalyst discovery | (mem) | 2 | 2 | 3 | 3 | 2 | 12 |

**Context on platforms (the "own the product" test).** Platform labs are raising very large sums:
- Periodic Labs: $300M seed, reported in talks at $7.5B.
- Lila Sciences: ~$550M raised.
- CuspAI: $450M Series B at $2.6B, Jul 2026 (src).

As of CuspAI's raise, none had a product out of the lab. They are the likely **suppliers** of discovery tooling to idea #1/#2-type companies, and a threat only if they move down into products. The ideas that pass beat them on the asset side: plant-trial data and a share of the customer's P&L, neither of which a platform lab has.

---

## Model 1: Value-share flotation reagents (20/25)

**Idea.** Own a line of flotation collectors, depressants and promoters designed by ML for each ore body. Sell them to concentrators at reagent price plus a share (20-35%) of verified extra payable metal. Start with porphyry copper, then move to Cu-Au, Zn-Pb, spodumene, graphite and phosphate.

**Market.**
- Flotation reagents: $5.7-6B on narrow definitions, $12B on broad ones (src: TBRC, SkyQuest, GMI).
- The bigger pool is the metal. Mined copper is ~23 Mt/yr (mem, ICSG), roughly 75-80% of it via flotation (mem). Typical recovery is 85-90%, and plant/IMPC cases show 4-9 pt gains from collector changes (src: Sossego +6% with a secondary-collector change; IMPC 2024 simulation 86.6→95.9%).
- A fleet-wide +1 pt on ~18 Mt flotation copper = 180 kt = **$2.7B/yr of new metal** at $14.75k/t (der). Gold, zinc, lithium and phosphate roughly double the pool (der).

**Price and unit economics (per mid-size mine, der).**
- Concentrator at 100 kt Cu/yr, 88% recovery. Target gain +1.5 pts → 1.7 kt Cu → **$25M/yr** gross value.
- Fee is 30% of verified extra metal (~$7.5M) plus reagent at cost-plus (~$2M/yr on a ~$5-10M existing reagent bill).
- Reagent COGS ~$1.2M via toll blenders. Field metallurgist and attribution ~$0.5M/yr.
- **Contribution ~$7.5-8M/yr per mine, about 75% gross margin.**
- Customer payback is immediate, because there is no capex: the reagent goes into existing conditioning tanks.

**Vertical killers and AI counter-moves.**
1. *Plant-trial access and conservative metallurgists.* A robotic bench-flotation rig plus a mineralogy→recovery model screens 200-500 formulations on the mine's own ore in 4-8 weeks, against 6-12 months for a manual campaign. The plant trial then starts with a predicted gain and a confidence interval. Cost to qualify a mine falls from ~$1M to ~$150k (der). Plant trials themselves run 4-12 weeks (industry norm, mem).
2. *Baseline disputes over "extra metal".* A digital twin of the plant learns recovery as a function of feed grade, mineralogy, grind and throughput from historian data (the 12-24 months before the switch). Alternating on/off campaigns plus the twin give attribution to ±0.3 pts, written into the contract.
3. *New-substance registration.* The design space is limited to TSCA/REACH-listed molecules and new **mixtures** of them, which need no premanufacture notice. Novel collectors are filed later as a second line, once revenue exists.
4. *Incumbent price war (Syensqo/Cytec, Clariant, Chinese xanthates).* We do not compete on $/t of reagent. Our price is pegged to metal. Incumbents sell tonnes and the AI tools they own (Solvay SmartFloat) optimise dosing of their own catalogue (src), not the molecule per ore.
5. *Capital.* Asset-light. Toll blending; the plant is the customer's.

**Capital path.**
- Seed $4-6M: rig, 3 metallurgists, 2 ML engineers; first two bench-to-plant trials.
- Series A $25-35M at about 4-6 paid mines.
- Series B $60-100M: Chile/Peru/Zambia/Arizona field teams, gold and lithium extension, CoM patents on novel collectors.
- No project finance needed.

**Timeline (der).**
- First paid trial month 12-15.
- 3 mines by end of yr 2 (~$15M ARR); 12 mines by yr 4 (~$90M).
- **$100M+ revenue by yr 5** with 14-15 copper mines, or fewer copper mines plus gold and lithium.
- $1B+ revenue needs ~120 mine-equivalents, about 10-15% of the world's large flotation plants: yrs 10-12.
- At 75% gross margin, mining-tech multiples imply a **$5-15B ceiling**. Jetti reached $2.5B with ~1 commercial site (src).

**Competitors.**
- Syensqo, Clariant (Mining Solutions grew low-double-digit in 2025, src), Kemira, Nouryon, Orica, Chinese producers.
- Startups: **Giraffe Bio** (AI + cell-free bio promoters, $6.4M seed Oct 2026, Orion + BHP Ventures, src), MetSop (AI reagent R&D, src); academic work at Stanford (phosphate) and LTU (designed collectors).
- Giraffe validates the thesis and is the closest rival. Its bio-promoter route is narrower than full small-molecule collector/depressant design.

**What compounds.** Each plant trial adds labelled ore → reagent → recovery data, and no public dataset of that exists. Plants also send their historians to us for attribution, and the value-share contracts renew with each new ore zone.

**Kill risks.**
- (a) Well-run plants have only 0.3-0.7 pts of headroom, which is half the model. **Test:** pull 10 public NI 43-101 / technical-report metallurgy sections and compare lab locked-cycle recovery with plant recovery; if the median gap is under 1 pt, the copper base case halves.
- (b) Miners refuse metal-share and pay only for reagent. Fallback is a premium-reagent model at ~40% gross margin: N falls to 3, total 19.
- (c) Concentrate grade/penalty trade-offs (pyrite and arsenic) eat the gain.
- (d) An incumbent buys Giraffe/MetSop and copies the approach. The data flywheel is our only defence.

**Cheapest test (~$40-80k, 8 weeks).** Buy 3-5 porphyry ore samples (public cores and met-lab rejects; buying samples is not prospecting). Run a 100-formulation ML-guided bench campaign against each site's published reagent suite. Pass at ≥1.5 pts rougher recovery at equal grade on 2 of 3 ores; kill under 0.5 pts.

---

## Model 2: Low-clinker admixture system (19/25)

**Idea.** Sell an admixture plus mix-design system to ready-mix and precast producers. It has two parts:
- AI-designed PCE dispersants and accelerators (sulfate/C-S-H seeding, alkanolamines, all inventory-listed families) tuned to the local cement, slag, fly ash, calcined clay and limestone;
- an ML strength predictor.

Together they let the producer cut cement 15-25% further than today at equal performance. We charge per yd³ and share the cement savings.

**Market.**
- Admixtures $20-22B in 2025 (src: Ken Research, Insight Partners, MarketsandMarkets).
- US ready-mix 379M yd³ in 2024 (src: NRMCA). Global concrete ~14B m³/yr (mem).
- Comparables: Sika bought MBCC (~CHF 5.3B, mem, unverified, src notes); Saint-Gobain bought Chryso and GCP; Chryso has launched calcined-clay admixtures (src), so incumbents see the need.

**Unit economics (US, der).**
- Typical mix ~500 lb (0.23 t) cementitious/yd³. Removing another 20% of cement (~46 kg) and replacing it with SCM/filler that costs ~$40-80/t less saves **~$2-4/yd³**, plus ~40 kg CO₂/yd³ for Buy Clean/LEED and EPD bids.
- We price at a $1.0-1.5/yd³ premium over a standard admixture package (~$2-3/yd³, mem).
- Chemical COGS ~$0.6/yd³, toll-made. Producer margin is $14.59/yd³ pre-tax (src, NRMCA 2023), so $1.5-2.5 net saving is a 10-17% margin lift. That is a strong buyer reason.
- Gross margin ~55-60%. A 20-plant producer (2M yd³/yr) is worth ~$2.5-3M/yr in revenue.

**Vertical killers and AI counter-moves.**
1. *The 28-day strength clock.* Each mix-design iteration takes 28 days of curing, so a new low-clinker mix takes 3-6 months and producers rarely try it. Isothermal calorimetry, maturity sensors and early-age data feed a model that predicts 28-day strength at 1-3 days (±5%). That cuts a design cycle to ~2-3 weeks and shrinks the 28-day test to a single confirmation step. **Effect: a new plant onboards in ~1 month instead of ~4-6 months, so customer acquisition cost falls ~3x (der).**
2. *Prescriptive specs (DOTs, ACI 318 cement limits).* Start where performance specs are allowed: private commercial and data-centre slabs (hyperscalers buy low-carbon), precast, and ASTM C1157 / C595 Type IT blended cements (src: Sublime's C1157 path). Generate the DOT evidence from the plant data we already collect. DOTs follow in yrs 3-5.
3. *Liability and the producer's QC culture.* Each pour is backed by the model's prediction plus standard cylinders. A product-liability policy priced on our prediction error data covers the producer.
4. *Incumbents.* Sika and Saint-Gobain sell catalogue admixtures through dispensing contracts. Our wedge is the per-plant model plus molecules co-designed to local SCMs. AI cement-mix software (alcemy, $10M, src) owns no chemistry, and we do.

**Capital path.**
- Seed $5M: lab, calorimetry fleet, 3 pilot producers.
- Series A $30M: toll manufacturing, 60 plants.
- Series B $80M: own blending/dispensing assets, entry to the EU and India, where calcined clay is cheapest.
- Little capex: the customer's batch plant is the factory.

**Timeline (der).**
- First paid plant month 9-12.
- ~$10M revenue yr 3 (~8M yd³, about 2% of US).
- **$100M by yr 6-7** (~70M yd³-equivalent: ~15% of US, or US + EU + India).
- A $1B+ outcome needs ~$300M revenue at Sika-style multiples (~2.5-3.5x sales, mem). The ceiling is $10B+ only with global share of ~5% of concrete.

**Competitors.** Sika (MBCC), Saint-Gobain (Chryso/GCP), Mapei, Fosroc; CarbonCure (CO₂ injection, complementary); alcemy and Concrete.ai (software); Sublime and Brimstone (new cements, complementary as supply).

**Kill risks.**
- (a) Incumbents bundle a "free" ML mix-design tool with their admixtures within 2-3 years. D is 3 for this reason.
- (b) The savings are smaller where slag and fly ash are already short or expensive. The fallback is calcined clay, whose supply chain is immature in the US.
- (c) A strength-prediction failure on a structural pour means reputational death. Mitigation: confirmation cylinders on every new mix for year 1.
- (d) Construction downturns.

**Cheapest test (~$30-60k, 10 weeks).** Take 3 producers' historical batch and cylinder data (QC records), plus 60 new lab mixes with calorimetry. Pass at ≤6% MAE predicting 28-day strength from ≤3-day data across SCM levels of 30-50%. Then confirm one mix at ≥20% further cement reduction meeting the design strength.

---

## Near-misses at 18 (short notes)
- **Ex-China polymetallic scrap refinery (#3).**
  - The prices are extraordinary: Dy oxide CIF Europe ~$3,500/kg at 16.3x China; Tb $6,745/kg; APT ~$3,000+/mtu; 6N Ga ~$2,350/kg (src Benchmark, SMM, Fastmarkets-derived).
  - A reconfigurable line that follows whichever premium is widest is a real answer to L9.
  - **It fails on A and D.** The counter-move (faster commissioning) is real but does not stop the premium decaying when Lynas, Phoenix (with its $500M DoD loan), Plansee (12 kt WO₃ Towanda) and H.C. Starck add capacity.
  - Revisit if a scrap-feedstock lock (OEM take-back contracts) can be shown.
- **Autonomous oilfield production chemicals (#4).** The numbers and the comparable are strong (ChampionX: $2.4B production chemicals revenue, SLB paid $7.8B). The AI edge is mostly service efficiency, which SLB/ChampionX are also digitising, so D=3 and A=3.
- **Specialty chemical AI roll-up (#5).** The best T score (cash yield from day 1) and real numbers. D=2: any PE fund can hire the same optimisation vendors, so the edge is a yield (L12) unless the self-driving process lab is proprietary and compounding.

## Sources (web-checked this session)
- Flotation reagents: [GII/TBRC](https://www.gii.tw/report/tbrc1776035-flotation-reagents-global-market-report.html), [GMI](https://www.gminsights.com/industry-analysis/mining-flotation-chemicals-market), [Giraffe Bio seed](https://www.startupresearcher.com/news/giraffe-bio-raises-usd6-4-million-seed-round-to-scale-mineral-reagents), [MetSop](https://www.crown.co.za/modern-mining/industry-news/28700-metsop-embarking-on-a-journey-to-revolutionise-flotation-reagents-development-with-ai), [Solvay SmartFloat](https://www.solvay.com/en/news/solvay-marks-milestone-digital-mining-journey-smartfloat-solution-more-efficient-and), [IMPC 2024](https://store.smenet.org/22ocik7/946), [Clariant FY2025](https://www.clariant.com/-/media/Files/Corporate/News/2026/02/CLARIANT-ANALYST-PRESENTATION-Q4_FY_2025-EN_20260226b.pdf)
- Copper price: [Farmonaut, 14 Oct 2026 LME $14,751/t](https://farmonaut.com/?p=122581) (secondary aggregator)
- Jetti/Ceibo: [mining.com Jetti $2.5B](https://www.mining.com/web/jetti-raises-funds-at-2-5-billion-value/), [Ceibo $30M B](https://www.esgtoday.com/sustainable-mining-solutions-company-ceibo-raises-30-million/)
- Rare earths: [Benchmark Q3 2026](https://source.benchmarkminerals.com/article/ex-china-heavy-rare-earths-continue-to-surge-q3-2026-rare-earths-price-review), [Phoenix $76M](https://impactalpha.com/amid-trade-war-phoenix-tailings-snags-76-million-for-us-production-of-rare-earth-metals/), [Phoenix $500M DoD](https://news.bloomberglaw.com/construction-labor/rare-earth-startup-lines-up-500-million-in-pentagon-funding-1), [Vulcan $1B+](https://cincinnati.dealroom.co/news/feed/vulcan-elements-secures-1b-funding-boost), [Noveon $215M](https://pulse2.com/noveon-magnetics-215-million-series-c-funding/), [Cyclic $55M](https://www.inmotionventures.com/inmotion-ventures-invests-in-cyclic-materials/), [Lynas HRE](https://www.miningweekly.com/article/lynas-begins-first-heavy-rare-earth-output-outside-china-2025-05-16)
- Tungsten/gallium: [Mining Reporters APT](https://www.miningreporters.com/noticia/news/2026/04/tungsten-prices-record-china-export-controls-defence-demand), [Fastmarkets tungsten 2026](https://fastmarkets.com/insights/tungsten-2026-geopolitics-sets-global-tone), [SMM gallium](https://news.metal.com/newscontent/103927018-les-prix-du-gallium-de-haute-pureté-hors-chine-ont-continué-à-augmenter-fortement-rapport-smm-sur-le-gallium), [Plansee reserve](https://plansee-group.com/en/articles/detail/aufbau-einer-strategischen-wolframoxid-reserve), [H.C. Starck expansion](https://news.metal.com/en/newscontent/104041318-mitsubishi-materials-invested-50-million-euros-to-expand-production-of-hc-starck-tungsten-recycling)
- Concrete: [NRMCA production](https://www2.nrmca.org/my.nrmca.org/ProductionStatisticsEmbed/2025ProductionStats04_files/sheet002.htm), [Giatec cost/NRMCA margin](https://www.giatecscientific.com/education/the-role-of-material-costs-in-concrete-production/), [Ken Research admixtures](https://www.kenresearch.com/industry-reports/global-concrete-admixture-market), [Insight Partners](https://www.theinsightpartners.com/reports/concrete-admixtures-market), [alcemy](https://cemnet.com/News/story/177306/alcemy-secures-us-10m-funding-to-enter-us-market.html), [Chryso C-Clay](https://uk.chryso.com/news/innovative-tailor-made-admixtures-calcined-clay-based-cements-accelerating-decarbonization/), [Sublime](https://www.manufacturingdive.com/news/low-carbon-cement-factory-sublime-systems/711639/)
- Oilfield: [Enverus on SLB-ChampionX](https://www.enverus.com/blog/slb-taking-home-the-prize-in-8-2b-championx-acquisition/), [Spherical Insights $30.1B](https://www.sphericalinsights.com/blogs/top-20-companies-global-oilfield-chemicals-market-in-2026-2035-spherical-insights-analysis)
- Others: [refinery catalysts IMARC](https://www.imarcgroup.com/refinery-catalysts-market), [Ketjen/KPS](https://www.hydrocarbonengineering.com/refining/30102025/albemarle-to-sell-stake-in-ketjen-to-kps), [TIM $2.56B](https://www.fortunebusinessinsights.com/), [ABF sizing](https://www.marketsandmarkets.com/ResearchInsight/ajinomoto-build-up-film-companies.asp), [ALD precursors IMARC](https://www.imarcgroup.com/high-k-cvd-ald-metal-precursors-market), [electrolyte additives](https://www.giiresearch.com/report/moi2119249-battery-electrolyte-additives-market-share.html), [lubricant additives](https://emergenresearch.com/industry-report/lubricant-additives-market), [ECHA PFAS](https://www.pinfa.eu/news/echa-to-conclude-on-pfas-by-end-2026/), [CuspAI $450M](https://ai2.work/blog/cuspai-s-450m-bet-materials-science-as-an-ai-search-problem), [Periodic Labs](https://letsdatascience.com/news/periodic-labs-seeks-500-million-science-funding-c123b746)

## Caveats
- Market-research sizes disagree by up to 2-3x; ranges are shown.
- The copper price comes from a secondary aggregator.
- The Sika-MBCC price and global concrete volume are from memory.
- The plant-recovery headroom (the key assumption in Model 1) is untested and is the first thing to check.
- Scores are one scorer's judgement. Optimism on tech means each scoring assumes the ML works as described.
