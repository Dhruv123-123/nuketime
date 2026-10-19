# V5 machines: AI-leveraged ownership in machines, robotics, manufacturing and industrial assets (19 Oct 2026)

Frame: `V5_OPTIMIST.md`. We assume the tech works and grade on the numbers and the clock: N numbers close, T time, C ceiling, A AI answers the killers, D defensibility/ownership. Each is 1-5. To pass, an idea needs 19+ with no leg below 3.
What died before and why (`VERDICT.md`, `triple_L1_L6_RML.md`): the rent-the-factory transformer scored 11 because the margin is a shortage margin with a half-life (L9) and Ayr already holds it. Transformer reman scored 11. GT hot-section used parts scored 17, held by PSM, EthosEnergy and MD&A, with OEM IP limiting it. Run-out aero cores scored 16 because FTAI holds that rung. V5 does not use "ML must be the illegible-data decider" (the Terranox shape). It scores AI as a cost and time lever, which is how Dhruv framed V5.

**Headline.** Three ideas reach 19+, and all three are about the **gas-turbine hot section** or a **scarce physical choke point** (castings, drydocks). The strongest is an AI-native PMA/non-OEM parts house, starting with industrial gas turbines (no FAA gate) and moving into FAA PMA. Its comparables are unusually strong. HEICO Flight Support did $3.1B of sales at a 24.1% operating margin in FY25. GE agreed to pay $11.75B (~26x standalone EBITDA) for CPP, a casting house, in Sep 2026. Howmet is worth ~$112B. Hadrian ($7.87B, Aug 2026) shows that investors will pay for "AI-run factory" stories in this sector. That also means the plain AI job-shop rung is now crowded.

Sources key: [S#] at the bottom. "(memory)" means not web-checked this pass. "(derived)" means arithmetic from stated inputs.

## Ranked table (33 ideas)

| # | Idea (one line) | Vertical killer(s) | AI counter-move, quantified | Rough numbers | N | T | C | A | D | Σ |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AI-native hot-section PMA house**: reverse-engineer and own non-OEM approvals for IGT (7F/7E/501F) parts, then FAA PMA for CFM56/V2500/CF6. Sell at ~70% of OEM and hold an exchange pool | OEM LTSAs lock the fleet; per-part qualification cost and time; OEM IP suits; HEICO/PSM/Ethos hold the rung | Scan→CAD→materials ID→test plan→DER/compliance package automated: engineering hours per part ~3,000→~1,000, dev cost ~$1M→~$0.35M, time 12-18→6-9 mo (derived; baseline memory). **~2.5-3x more approvals per R&D dollar than HEICO's model**, so a startup approval library compounds faster than an incumbent's | PMA mkt ~$11.8B [S1]; HEICO FSG $3.1B rev, 24.1% op margin [S2]; IGT service ~$16-20B (2012) [S3]; OEM turbine waits 5-7 yr [S4], so the fleet runs harder | 4 | 4 | 5 | 4 | 4 | **21** |
| 2 | **AI-run superalloy investment-casting foundry** (equiaxed→DS/SX airfoils for IGT, defence, space, then aero) | Capex; 18-24 mo OEM qualification; incumbents PCC/Howmet/CPP; end buyers go in-house (SpaceX, GE buying CPP) | Printed ceramic cores/shells remove $0.1-0.5M tooling and 6-12 mo per part (DDM claims 10-day castings [S5]); ML on solidification sim plus in-process sensing lifts SX/DS yield ~10-20 pts (memory baseline 60-80%); auto-generated FAI packs cut qualification to ~9 mo. **Per-furnace gross margin ~25%→~38%** (derived) | Lead times 18+ mo, US foundries -67% since 2000 [S5]; CPP $11.75B, ~26x EBITDA [S6]; Howmet ~$112B [S7]; Fabri $13.5M raised, shipping to LM/RTX [S8] | 3 | 3 | 5 | 4 | 5 | **20** |
| 3 | **AI-run Navy/Jones-Act ship-repair yard roll-up**: buy MSRA/ABR-holding yards (owning the drydocks), run them with AI planning and robotic surface prep and welding | Labour (welders); Navy one-ship-at-a-time contracting; drydock capex; BAE/Vigor/NASSCO | AI work-package generation from condition data plus scheduling cuts growth-work overruns and delay days ~30%, and robotic blast/paint/weld cuts direct labour ~20-25%. **EBITDA margin ~8%→~15%** (derived, baseline memory), which lets a startup outbid PE at 6-8x on a yard it values at 12x | Navy ship maintenance ~$16.2B FY26 request; private-yard on-time ~1/3; deferred maintenance ~$2.0B [S9] | 3 | 5 | 4 | 3 | 4 | **19** |
| 4 | Hot-section stack (1+2 merged): PMA approvals fed by own foundry and own rotable pool | Same as 1+2, plus capital | As 1+2; owning castings removes the 18-mo supply gate that would otherwise cap #1 | Phase 2 of #1, not a separate start | 3 | 3 | 5 | 4 | 5 | 20 (variant) |
| 5 | Uprate-for-share: AI-designed hot-gas-path upgrades adding +3-8% MW and efficiency to existing F-class units, paid as a share of incremental capacity revenue | OEM upgrade packages; LTSA lock; utility risk aversion | AI CFD/aero redesign cycle 18→6 mo; a share of $/kW-yr capacity value avoids the capex sale (derived) | New-build gas ~$2,000+/kW with 5-7 yr wait (memory/[S4]); +5% on ~150 GW F-class ≈ 7.5 GW (memory) | 4 | 4 | 3 | 4 | 3 | 18 |
| 6 | Owned BTM power fleet from remanufactured aero-derivatives and recips, sold as power-as-a-service | Capital; VoltaGrid/ProEnergy/FTAI; turbine supply | AI fleet ops run ~1 tech per 50 MW vs ~1 per 15 (memory); predictive maintenance lifts availability 92→97% | VoltaGrid $1B Blackstone/Halliburton, 7.5 GW order book [S10] | 3 | 4 | 5 | 3 | 3 | 18 |
| 7 | Third-entrant AI job-shop network for power equipment (switchgear enclosures, busbar, transformer tanks, turbine packaging) | Hadrian/Isembard hold aero-defence; customer qualification | Agentic quoting/CAM cuts quote-to-PO from days to hours and programming hours ~70% (Hadrian Opus claim [S11]) | Hadrian $7.87B, $1.37B raised [S11]; Isembard $50M A, 25 factories [S12] | 3 | 4 | 5 | 3 | 3 | 18 |
| 8 | Nadcap special-process roll-up (heat treat, coatings, NDT, chem-process) with AI quality/paperwork | Fragmented owners pricing scarcity; audits; Bodycote | AI audit-readiness and record automation cuts quality overhead ~40%; ML furnace control cuts re-runs | Bodycote £727M rev, 15.7% adj margin [S13]; caps ceiling | 4 | 4 | 3 | 3 | 4 | 18 |
| 9 | Nuclear obsolescence house: AI commercial-grade dedication, owning a dedicated-parts catalogue for 94 US reactors plus SMRs | Small market; Curtiss-Wright/Westinghouse/Paragon; 10 CFR 21 liability | AI drafts critical-characteristic and failure-mode analyses: dedication engineering ~200→~60 hrs per item (derived) | 1 in 5 of ~100k parts per plant hard to replace (CW claim) [S14] | 3 | 4 | 3 | 4 | 4 | 18 |
| 10 | AI-run sand/ductile foundry roll-up (pump, valve, mining, rail castings) | Retiring owners; environmental permits; low margins | ML pour/sand control cuts scrap 8→3% (memory); AI quoting cuts estimator labour ~70% | -67% US foundries [S5] | 3 | 4 | 4 | 3 | 3 | 17 |
| 11 | Mining/construction component reman with owned core pool; AI core grading plus robotic laser cladding | Cat/Komatsu dealer lock; core supply | Vision grading cuts teardown inspection ~50%; cladding salvages ~20% more cores | Mining reman ~$6.4B [S15]; Cat ~13.5% share | 3 | 4 | 4 | 3 | 3 | 17 |
| 12 | Aero-engine MRO with owned engine pool (FTAI-lite on PW/CFM narrow-body) | Capital; FTAI; OEM shop-visit lock | AI records/borescope triage cuts shop-visit induction cost ~15% | FTAI precedent (memory) | 2 | 4 | 5 | 3 | 3 | 17 |
| 13 | Spare large-power-transformer leasing pool ("GATX for LPTs") with AI DGA failure forecasting | Grid Assurance (utility-owned); L9 half-life; $3-10M/unit | AI failure forecasting sizes the pool at ~0.6x the naive count for the same fill rate (derived) | LPT lead 128-144 wk [S16] | 3 | 3 | 4 | 3 | 3 | 16 |
| 14 | AI-native LPT factory | $200-450M capex (Hitachi $457M plant [S16]) | AI auto-design per custom order: design weeks→days | 80% imported [S16] | 2 | 2 | 5 | 3 | 4 | 16 |
| 15 | Contract-built MV switchgear brand (Ayr for switchgear) | UL/IEEE listing; Eaton/Schneider/Siemens-Jabil | AI-generated listing documentation; configurator | MV switchgear 52-80 wk [S17]; Powell $400M+ order | 3 | 4 | 4 | 3 | 2 | 16 |
| 16 | Motor/generator rewind roll-up with exchange pool | Small shops; low ceiling | AI fault diagnosis from test data | Fragmented (memory) | 3 | 4 | 3 | 3 | 3 | 16 |
| 17 | Industrial valve reman and exchange pool for refining/LNG/power | Emerson/Flowserve service | Vision grading; AI turnaround planning | (memory) | 3 | 4 | 3 | 3 | 3 | 16 |
| 18 | Records-traced USM aero parts (Tracebird) | Records cost; teardown capital | ML trace (v4) | USM ~$8.5B [S1] | 3 | 4 | 3 | 3 | 3 | 16 |
| 19 | AI robotic ASME U-stamp fabrication (heat exchangers, pressure vessels for LNG/SMR/DC cooling) | Welder shortage; stamps | Robotic welding ~3x deposition per welder | (memory) | 3 | 4 | 3 | 3 | 3 | 16 |
| 20 | Hydro runner uprate-for-share (AI CFD runners, +3-5% MWh) | FERC licence amendments; small fleet | AI design 12→3 mo | US hydro ~80 GW (memory) | 3 | 3 | 3 | 3 | 3 | 15 |
| 21 | Refurbished 200/300mm semi-tool pool, AI recertification | Moov/SurplusGlobal; OEM service lock | Automated recertification | (memory) | 3 | 4 | 3 | 3 | 2 | 15 |
| 22 | Solid-state transformer product | Heron, Amperesand, DG Matrix | Topology search | (memory) | 2 | 3 | 5 | 2 | 3 | 15 |
| 23 | SF6-free HV breaker | OEM duopolies; type testing | AI test-campaign design | (memory) | 2 | 2 | 4 | 3 | 3 | 14 |
| 24 | Small aero-derivative new turbine (Boom-type) | Crusoe dropped Boom's 1.21 GW [S4]; supply chain | AI design | Boom 250 MW next yr claimed | 2 | 3 | 5 | 2 | 2 | 14 |
| 25 | Rare-earth-free motor factory | Niron etc.; capex | Materials ML | (memory) | 2 | 3 | 4 | 2 | 3 | 14 |
| 26 | Large open-die forgings (SMR vessels, naval shafts) | $0.5-1B press capex; JSW/Doosan | Process ML | (memory) | 1 | 2 | 4 | 2 | 5 | 14 |
| 27 | Robotic wind-blade repair fleet owning blade spares | Service shop; Aerones | Robotics | (memory) | 3 | 4 | 2 | 2 | 2 | 13 |
| 28 | Aero fastener plant | PCC/Howmet/LISI; supplier listing | AI qualification packs | (memory) | 2 | 3 | 3 | 3 | 3 | 14 |
| 29 | Large slewing/main bearings for wind and turbines | China cost; capex | ML heat treat | (memory) | 2 | 2 | 3 | 2 | 3 | 12 |
| 30 | Solid rocket motors / energetics | Anduril, Ursa Major, X-Bow | AI grain design | (memory) | 2 | 3 | 4 | 2 | 3 | 14 |
| 31 | Transformer reman (re-run) | L9; scored 11 in v3 | Robotic rewinds | (v3) | 2 | 3 | 2 | 2 | 3 | 12 |
| 32 | Robotic railcar repair roll-up | GATX/Trinity in-house | Vision inspection | (memory) | 3 | 4 | 2 | 2 | 2 | 13 |
| 33 | Recip-genset reman for DC prime power | Cat/Cummins dealers | Fleet ML | (memory) | 3 | 4 | 3 | 2 | 2 | 14 |

**Passes (19+, no leg under 3):** #1 (21), #2 (20), #3 (19). #4 is #1's phase 2, not a separate company. Near misses at 18: uprate-for-share (#5), which is better as a product line inside #1; power fleet (#6) and job-shop network (#7), both crowded and well funded; Nadcap roll-up (#8), where Bodycote's £727M of revenue caps the ceiling; and the nuclear obsolescence house (#9), which has too small a market.

---

## Model 1: AI-native hot-section PMA house (21/25)

**Company.** Own a library of non-OEM approvals and reverse-engineered designs for gas-turbine parts, and sell them at ~70% of OEM list. Start with **industrial gas turbines (7FA, 7EA, 501F, 9E)**, where no FAA PMA is needed and the customer (IPP or utility) is the approver. Then take the same engineering engine into **FAA PMA** for high-volume aero engines (CFM56, V2500, CF6/LM6000, which shares a core with the GE aeroderivative fleet).

**Why now.** GE Vernova and Siemens Energy quote 5-7 years for new turbines, and BNEF puts new combined-cycle lead time at 5 years [S4]. Existing units run harder and longer, hot-gas-path consumption rises, and OEM parts queues lengthen. PMA usage has grown since Covid because OEM supply is strained [S1/avm-mag].

**Market.** Commercial aero PMA is ~$11.8-12.1B (IMARC/Reanin) and engines are the largest share [S1]. IGT service was ~$16-20B/yr in 2012 per Chromalloy's president [S3] and is likely higher now (memory). Parts are reportedly ~64% of service, with OEMs holding ~62% of service revenue (unverified newsletter) [S3]. Serviceable non-OEM pool: ~$5-8B IGT plus a ~$3-5B aero engine PMA share that is not HEICO's (derived).

**Price and unit economics (derived; per-part baselines are memory, flagged).**
- HEICO-style price: ~70% of OEM, with the discount widening as OEM raises list prices [S2-secondary].
- Per approved part: development ~$1M today (memory), ~$0.35M with the AI pipeline. Annual revenue per part ~$1-3M for hot-section consumables. Gross margin ~50-55% and operating margin ~25% at scale (HEICO FSG 24.1% [S2]).
- **AI counter-move with stated effect.** 3D CT/blue-light scan to parametric CAD (hours, not weeks), ML alloy and coating identification from coupons, auto-generated test matrices, and a drafted DER/compliance data package. Engineer hours per part ~3,000→~1,000, calendar 12-18→6-9 months. The same R&D budget yields ~2.5-3x the approvals, and payback per part falls from ~12-18 months to ~4-6.
- Fleet: ~60 approved parts at $1.7M average ≈ $100M revenue.

**Capital path.**
- Seed $4-6M: 5 IGT combustion and transition parts (fabricated, so no casting needed), contract coating, and two IPP launch customers.
- Series A $25-35M: 20-25 IGT parts, a $10M rotable/exchange pool financed partly on an ABL against inventory, and first hot-gas-path cast parts through a partner foundry.
- Series B $80-120M: FAA PMA programme (CFM56/V2500), in-house coatings and repair (HIP, brazing), and the option to build #2's foundry (the hot-section stack).
- Total equity to $100M revenue: ~$150M. Inventory is debt-financed.

**Timeline.** First revenue in months 12-18, from fabricated combustion parts sold to IPPs outside LTSAs. $25M by year 4. $100M by year 6-7: ~60 parts plus exchange-pool revenue, with FAA PMA adding from year 4-5.

**Ceiling.** HEICO trades around $40B+ (memory) on $3.1B FSG plus electronics. A focused hot-section house at $1.5-2B revenue and 25% margin is worth ~$10-15B at aerospace-aftermarket multiples (derived from CPP's ~26x EBITDA [S6]).

**Competitors.** HEICO (aero PMA leader); PSM (Hanwha, 100+ patents, F-class upgrades) [S3]; EthosEnergy; Chromalloy (Veritas/Sequa) [S18]; MD&A; Sulzer; Liburdi; OEM in-house aftermarket. No funded AI-native PMA startup turned up. The closest is Novineer, an AI reverse-engineering tool with no funding found [S19].

**Kill risks.**
1. OEM LTSAs cover the most valuable F-class units. The addressable market is units outside LTSA plus LTSA expiries, which could be only ~40% of the fleet.
2. Hot-section cast parts need castings that are 18+ months out [S5], so the company must partner early or build #2.
3. Liability for a hot-section failure, which needs product insurance.
4. Aero lessors resist PMA on leased engines, which limits FAA PMA growth to owner-operated fleets.
5. HEICO could copy the AI pipeline. Mitigant: its value is the approval library and customer data, which take years to compound.

**Cheapest test (<$150k, 10 weeks).** Pick 3 7FA combustion parts. Run scan→CAD→drawing→test plan with an off-the-shelf pipeline and measure engineer-hours against a quote from a DER/RE shop. Get 2 IPP LOIs at 70% of OEM price. Pass if hours are ≤40% of baseline and there are 2 LOIs.

## Model 2: AI-run superalloy investment-casting foundry (20/25)

**Company.** A greenfield US foundry for superalloy turbine castings. Start with equiaxed structural and nozzle castings for defence, space and IGT, which have shorter qualification. Add directionally-solidified and single-crystal airfoils for IGT, and aero later. The casting becomes the owned, scarce thing, and the qualification files compound.

**Why now.** Aerospace investment-casting lead times are 18+ months and the US has lost 67% of its foundries since 2000 (AFS via DDM) [S5]. Gas-turbine demand for AI data centres doubles the pull. SpaceX is building its own blade foundry and Safran a Rennes airfoil plant (2027) [S5], and GE is paying $11.75B to own CPP [S6]. The scarcity is real enough that end buyers integrate vertically.

**Market.** Superalloy aero and IGT castings ~$8-10B global (memory). CPP alone is ~6,600 people and 20+ sites [S6]. Howmet Engine Products is the largest segment of a ~$112B company [S7].

**Unit economics (derived; baselines memory).**
- One VIM furnace cell plus shell line: capex ~$15-25M (equiaxed) and ~$35-60M (DS/SX). Revenue per mature cell ~$20-35M/yr.
- **AI counter-moves with stated effect:**
  1. Printed ceramic cores and shells remove $0.1-0.5M tooling and 6-12 months per part number. DDM claims first castings in ~10 days [S5]. New-part introduction cost falls ~5x, so the foundry can quote the long tail of spare and legacy parts that incumbents refuse.
  2. ML on solidification simulation plus in-process sensing lifts SX/DS yield by ~10-20 points from a ~60-80% baseline (memory). Gross margin rises from ~25% to ~38% (derived: scrap is ~30-40% of conversion cost).
  3. Auto-generated first-article and qualification packages cut OEM qualification from ~18-24 months to ~9.

**Capital path.**
- Seed $5-8M: pilot cell plus printed ceramics, with defence/space equiaxed parts. Fabri did this on $13.5M [S8].
- Series A $40-60M: 2 production cells, plus a defence DPA Title III or OSC loan for 30-50% of capex (memory precedent).
- Series B $120-200M: DS/SX line with IGT customer prepayments (turbine OEMs and the #1 PMA house pre-buy capacity).
- Total ~$250M equity plus ~$150M government and customer capital to reach $100M revenue.

**Timeline.** First revenue in year 1.5-2 (Fabri is already shipping to LM/RTX). $100M at ~4-5 cells by year 6-7. IGT DS/SX qualification lands in years 4-5.

**Ceiling.** CPP's ~26x EBITDA [S6] and Howmet's ~$112B say a $1B-revenue foundry at 30% EBITDA is worth ~$8-10B.

**Competitors.** PCC (Berkshire), Howmet, CPP (→GE), Doncasters, Arconic legacy, Safran, SpaceX in-house; startups Fabri ($13.5M), Rangeview (Kratos selection), DDM Systems (digital foundry).

**Kill risks.**
1. End buyers integrate (SpaceX, GE→CPP), which shrinks the merchant market for top OEMs (L8).
2. Single-crystal metallurgy know-how sits in a few hundred people. Hiring them is the real gate, and AI does not remove it.
3. Capex intensity with the risk of a 2029 downturn.
4. The L9 half-life: when PCC/Howmet expand, the premium fades. The mitigant is the long-tail/legacy spares niche, which incumbents structurally avoid.

**Cheapest test (<$200k, 12 weeks).** Pour 3 IGT legacy nozzle segments via printed ceramics at a toll foundry. Measure dimensional conformance, and get prices and LOIs from 2 IPPs or ISPs that are waiting on OEM castings. Pass if there are 2 LOIs at ≥30% gross margin.

## Model 3: AI-run ship-repair yard roll-up (19/25)

**Company.** Buy 2-4 private US ship-repair yards that hold Navy MSRA/ABR agreements and drydocks. Run them with AI planning (work-package generation, growth-work prediction, scheduling, materials) and robotic surface prep, painting and welding. Own the scarce asset (drydock plus certifications) and win availabilities on on-time delivery.

**Why now.** The Navy's FY26 request for ship maintenance is ~$16.2B. Only ~a third of private-yard surface availabilities finished on time (FY21-23), with 10,000+ destroyer delay days, and deferred maintenance is ~$2.0B [S9]. The Navy is weighing foreign yards (Japan, Korea, Singapore) and multi-ship awards [S9]. Dock demand runs at or above capacity (illustrative) [S9].

**Unit economics (derived; baselines memory).**
- A mid-size yard does ~$100-300M revenue at ~6-10% EBITDA and trades at ~6-8x.
- **AI counter-moves with stated effect:**
  1. Growth-work prediction from prior availabilities and condition data cuts unplanned work and delay days ~30%.
  2. Robotic blasting, painting and welding cut direct labour ~20-25% in the trades that are shortest of people.
- Together these take EBITDA margin from ~8% to ~15% and lift dock throughput ~15%, so a $150M yard's EBITDA goes from ~$12M to ~$25M. Paying 8x the old EBITDA ($96M) for an asset worth ~$200-250M after the change is the AI-financed step-up, and it lets a startup beat PE bids.

**Capital path.** Series A $30-50M equity plus seller notes and acquisition debt (Office of Strategic Capital/MARAD Title XI, memory) to buy yard 1 (~$100M EV). Yards 2-3 follow from cash flow plus a $150-250M raise.

**Timeline.** $100M revenue on day one of the first acquisition (years 1-2). $500M+ by year 5 with 3 yards. Ceiling $3-5B revenue (Navy, MSC, Jones Act, offshore wind vessels), worth ~$5-10B at HII/BAE-type multiples (memory).

**Competitors.** BAE Systems Ship Repair, Vigor, GD NASSCO, Huntington Ingalls, Fincantieri, Hanwha Philly. AI-native new-build startups (Saronic, Blue Water Autonomy) are new-build, not repair.

**Kill risks.**
1. Labour and union constraints cap the robotic gains.
2. Navy contracting is lumpy, and one lost availability hurts a single-yard company.
3. Sellers price in scarcity (L3), with drydocks valued at strategic premiums.
4. The ceiling depends on the Navy budget.
5. The AI lever is the least proven of the three. The A score of 3 reflects that.

**Cheapest test (<$100k, 8 weeks).** Pull 3 years of public GAO/Navy availability data plus one target yard's own job history under NDA. Backtest a growth-work predictor against the yard's actual change orders. Pass if it catches ≥40% of the dollars ≥30 days earlier.

---

## Cross-cutting findings
- The scarce physical thing in 2026 machines is the **gas-turbine hot section**, not transformers. It has a 5-7 year turbine wait, 18+ month casting lead times and a $11.75B CPP price tag. Transformers are easing toward ~30 weeks for distribution units (v3). LPTs are still long, but incumbent capex ($457M Hitachi, $340M Eaton) is landing in 2027-28, so the L9 half-life applies [S16].
- "AI factory" as a generic rung is now **held**. Hadrian has raised $1.37B at $7.87B and Isembard $50M for 25 factories [S11, S12]. New entrants need a scarce regulated output (approval, casting qualification, drydock) rather than generic CNC capacity.
- Of the three passes, only #1 has AI as a direct multiplier on the owned asset: approvals per R&D dollar. In #2 and #3, AI moves margin by 10-15 points, which matters but is copyable by incumbents over 3-5 years.

## Sources
- [S1] PMA market ~$11.8B 2025 (IMARC) https://www.imarcgroup.com/report/en/commercial-aircraft-parts-manufacturer-approval-market ; Reanin $12.1B https://www.reanin.com/reports/commercial-aircraft-parts-manufacturer-approval-market ; PMA growth https://avm-mag.com/pma-parts-surge-ahead-availability-and-innovation-drive-growth-in-2025 ; USM $8.55B (Fortune BI via secondary)
- [S2] HEICO FY25 8-K (FSG $3,117.3M, 24.1% op margin) https://www.sec.gov/Archives/edgar/data/46619/000004661925000076/a10312025ex991earningsrele.htm ; 70%-of-OEM pricing (secondary) https://www.itiger.com/news/1177484439
- [S3] IGT service $16-20B (2012) https://www.turbomachinerymag.com/view/aftermarket-parts-is-there-life-after-the-oem ; OEM share 62% / parts 64% (unverified) https://antonios-newsletter-aff62c.beehiiv.com/p/the-aftermarket-empire-why-service-not-sales-rules-the-gas-turbine-industry ; PSM https://www.psm.com/
- [S4] Turbine waits 5-7 yrs, Crusoe-Boom exit https://oilprice.com/Energy/Energy-General/US-Power-Boom-Triggers-Global-Gas-Turbine-Shortage.amp.html ; https://baxtel.com/news/crusoe-ends-1-25b-boom-supersonic-turbine-order-for-ai-data-centers
- [S5] DDM digital foundry, 18-mo lead, -67% foundries https://www.newsfilecorp.com/release/299864/DDM-Systems-Launches-the-Digital-Foundry-to-Address-Americas-Investment-Casting-Crisis ; SpaceX foundry https://www.foundry-planet.com/d/spacex-plans-its-own-turbine-blade-foundry-in-texas-ai-boom-meets-casting-bottleneck ; Safran Rennes https://foundrymag.com/melt-pour/article/21283776/engine-builder-plans-investment-casting-foundry-safran-aircraft-engines
- [S6] GE-CPP $11.75B https://www.geaerospace.com/news/press-releases/ge-aerospace-acquire-consolidated-precision-products-cpp-expanding-mission-critical ; multiples https://pulse2.com/ge-aerospace-to-acquire-consolidated-precision-products-for-11-75-billion/
- [S7] Howmet ~$112B (Aug 2026) https://www.suredividend.com/wp-content/uploads/2026/08/HWM-2026-08-09.pdf
- [S8] Fabri $13.5M https://www.tectonicdefense.com/fabri-announces-its-raised-13-5m-for-new-age-casting/ ; Rangeview/Kratos https://www.airframer.com/news/release/kratos-selects-rangeview-to-develop-advanced-cast-components-for-advanced
- [S9] Navy maintenance backlog (mostly ShipUniverse, citing GAO) https://www.shipuniverse.com/naval/the-navys-real-bottleneck-may-be-the-drydock/ ; https://news.usni.org/?p=41176
- [S10] VoltaGrid $1B https://www.blackstone.com/news/press/voltagrid-announces-1-billion-strategic-equity-investment-from-blackstone-and-halliburton/
- [S11] Hadrian $7.87B https://news.bloomberglaw.com/private-equity/defense-startup-hadrian-valued-at-7-87-billion-in-new-round
- [S12] Isembard $50M https://sifted.eu/articles/isembard-funding-round-ai-deeptech
- [S13] Bodycote FY25 https://data.fca.org.uk/artefacts/NSM/PRN/1d5cb1aa-fd70-4389-97d2-045f8ec2ca2f.html
- [S14] Curtiss-Wright obsolescence https://cwnuclear.com/products-and-services/obsolescencesolutions
- [S15] Mining reman $6.4B (GMI) https://www.gminsights.com/industry-analysis/mining-remanufacturing-components-market
- [S16] LPT capacity and lead times https://www.industrialinfo.com/iirenergy/industry-news/article/investments-in-us-transformer-manufacturing-aim-to-meet-surging-demand--361406 ; Grid Assurance https://kleinmanenergy.upenn.edu/commentary/blog/grid-assurance-llc-to-offer-resiliency-subscriptions-to-major-utilities/
- [S17] MV switchgear lead times https://terrapincg.com/news/switchgear-transformer-generator-lead-times-2026 ; Siemens-Jabil https://pv-magazine-usa.com/2026/05/28/siemens-and-jabil-to-expand-electrical-equipment-manufacturing-in-virginia/
- [S18] Veritas-Sequa/Chromalloy https://www.pehub.com/veritas-to-acquire-chromalloy-parent-sequa-from-carlyle/
- [S19] Novineer https://runwaygirlnetwork.com/2026/04/press-release-novineer-launches-ai-reverse-engineering-with-am-craft/

Caveats: the per-part PMA development cost, SX yield baselines, yard EBITDA margins and F-class fleet GW are memory, not web-checked. The IGT market figure dates from 2012. Navy figures come mostly via a trade newsletter citing GAO. All scores are one scorer's judgement.
