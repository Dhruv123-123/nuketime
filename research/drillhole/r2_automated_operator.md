# Round 2: is a crew-light, automated exploration-drilling OPERATOR a large company?

Written 19 Oct 2026. Builds on lane_B_market.md, lane_C_hardware.md and lane_H_ops_logistics.md.
Tags: (memory) means prior knowledge not re-checked this session. (estimate) means my own arithmetic or judgement.
Currency is stated each time.

## 10-line summary
1. **Labour really is the largest line in a contractor's cost, but not in an Athabasca program's all-in cost.** Durin's founder puts labour at about 60% of a drilling contractor's costs (TechCrunch). My per-rig model gets about 52% of contractor revenue. In a fly-in Athabasca program, where the contractor is 47-57% of spend, crew-driven cost (wages, crew camp-days, crew flights) is only about 20-30% of all-in $/m (estimate).
2. **Model.** One supervisor running 3-4 rigs, plus one helper-grade tech per rig per shift, cuts contractor cost per metre by about 20-30% (CAD 160/m to CAD 114-125/m). That allows for the automation capex and a 15-25% productivity gain. It also multiplies the rigs each scarce experienced driller can cover by 3.5-4x. In the Athabasca the all-in saving shrinks to about 12-20%, a 1.15-1.25x lever, which is below the rubric's 1.5-3x floor (estimate).
3. **The labour cap is cyclical, not structural.** Fleets sit at 40-75% utilisation even in this boom. In a bust, crews are cheap and automation capex is stranded. At 50% utilisation my model has the automated operator only at about break-even, while the incumbent loses money. Energold-style "better rig" contractors have died in the cycle before.
4. **Durin** (El Segundo, founded 2024): a USD 3.4M pre-seed in Apr 2025 led by 8090 Industries, with a16z, Lux, 1517, Bedrock, Champion Hill, Contrary and Day One, plus a Rio Tinto/Founders Factory accelerator slot. It builds and operates its own core rigs, initially 300 m deep with a 2.5-inch (BQ-class) hole, and sells metres ("revenue from every meter drilled"). It names no customers, gives no $/m figure and has announced no later round as of Oct 2026. It is too shallow and too small a core size for the Athabasca.
5. **Other attempts.** XtremeX (USD 11M Series A, Jan 2025): an automated coiled-tubing plus diamond-core rig to 2,000 m, with Ivanhoe Electric holding exclusivity on 3 rigs for up to 5 years and Precision Drilling and Baker Hughes as partners. No results found. Tribe Tech (autonomous RC rig, sold to Major Drilling/McKay for iron ore grade control). Earth AI owns its rigs inside an explorer: about USD 100/m claimed, a 7,000 m sample backlog, so its bottleneck moved to the lab.
6. **Incumbents already ship the pieces.**
   - Boart Longyear: LF160i plus FREEDOM rod handler, "up to 14%"; digital panel launching end-2025.
   - Epiroc: Diamec ARM at LaRonde, about 20%.
   - Sandvik: DE130i/140i auto mode, DA555 remote rod loader.
   - Major Drilling: RodBot, Smart 8 robot arm, and a buyer of the Tribe Tech rig.
   - Master Drilling: robotic slim rig, +50% productivity and -75% water; "Desert Elephant" commissioned. Slim drilling is only 4% of its revenue.
7. **Mining-face autonomy is mature; exploration core is not.** Production drilling runs one operator to 1-3 rigs (Sandvik), 6 rigs (Epiroc at Apatit) or up to 9 (Office TeleREMOTE). Exploration needs rods fetched from outside the mast, re-teaching for every hole, casing, fishing in bad ground and core handling. Industry estimates put full autonomy 3-5 years out and wide adoption 10-15 years out. One insider says savings in remote exploration are "minimal".
8. **Ladder and buyers.** A real ladder exists, but it runs the other way from discovery. Automation pays first in repetitive, high-volume, near-mine work: resource definition and grade control (78% of Australian metres, 45% of global budgets). Next come geotech, water and slim-hole geothermal. Greenfield fly-in exploration comes last. The capitalised buyers are majors and mid-tiers on term contracts (Rio, BHP, Agnico, Ivanhoe), and they pay per metre, not a step-up.
9. **Ceiling (estimate).** A crew-light operator taking 10% of the USD 7.5B contract-drilling pool at about 30% EBITDA is about USD 0.75B revenue and roughly USD 2-3B of value. Adding geotech, water and geothermal could double that. This is a good industrial company, not the "very large" ceiling. Only a drill-for-equity rung escapes, and that rung turns it into a prospect generator: Terranox's own model.
10. **Rubric score.** About 1.5 of 6. It fails item 1 (the physical step is the product), item 2 (it is robotics, not illegible public data) and item 3 (no cheap asset). Item 4 is partial and item 5 passes. Item 6 is borderline at best. It sits squarely inside the 2026-10-03 drilling ban. Kill it as a Terranox-adjacent new company. Watch Durin and XtremeX as future suppliers of Athabasca winter-window capacity.

---

## 1. What "the labour cap" actually is

Evidence carried over from round 1:
- Major Drilling FY26: "labour is expected to remain our most significant challenge ... the pool of available experienced drillers drying up". It is adding trainees, which lowers productivity. https://www.majordrilling.com/major-drilling-announces-fourth-quarter-results-and-record-annual-revenue/
- Fleet utilisation: Boart 47% (2023), Foraco 40% (Q4 2025), Major about 50%, Capital 74% (lane B, sources there).

New this round:
- Major Drilling had 3,825 employees in FY25, the year to Apr 2025 (Morningstar: https://dfd.dr.morningstar.com.au/investments/security/TSX/MDI).
  - FY25 revenue was about CAD 729M (CAD 889M FY26 / 1.22).
  - That gives about CAD 190k revenue per employee.
  - With about 340-400 working rigs, that is about 10-11 employees per working rig, including overhead (estimate).
- Durin's founder: labour is "about 60%" of drilling contractors' costs. Drilling takes "about 70%" of the capital exploration companies raise. https://techcrunch.com/2025/04/23/durin-digs-up-3-4m-to-automate-drills-for-critical-minerals-exploration/
  - The 70% is a pitch number. CanAlaska's audited split is 47-57% (lane H).
- Mine magazine (Apr 2025): wages during drilling campaigns "can run $10,000-50,000 a day". https://mine.nridigital.com/mine_apr25/automated-exploration-drill-rigs

Reading:
- Rigs are plentiful. About half of the biggest fleet is parked.
- Experienced drillers are scarce, but **only at the top of the cycle**. 2013-16 and 2023-24 were troughs with utilisation under 50% (lane B), and in those years crews were laid off, not scarce.
- An automation business sized on peak-cycle labour scarcity is betting the cycle stays up.

## 2. Crew per rig, wages, and labour's share of $/m

### 2.1 Crew structure
- A surface diamond rig runs two 12-hour shifts, day and night. Each shift has one driller and one to two helpers. Rotations are 14/7, 8/4 or 14/14. Job ads confirm 12-hour day and night shifts and 8/4 or 14/7 rotations (Orbit Garant, Full Force). Search summary of postings: https://fr.simplyhired.ca/job/1f3A632nAST0GTJegeeI9a1_eGA3um2z_YLulHMVtLP5-j4kNJfSpg
- On site that is 4-6 people per rig per day. Rotations make payroll about 1.5x that, so 6-9 people per rig. A foreman and mechanic are shared across rigs (estimate; lane H says the same).
- TechCrunch: rigs "typically need two to three people on site" per shift (Durin article, above).

### 2.2 Wages

**Canada (CAD)**
- Job Bank medians: diamond driller helper about CAD 25/hr, operator about CAD 33-35.55/hr (lane H: https://www.jobbank.gc.ca/marketreport/wages-occupation/24610/AB).
- Foraco heli-supported postings: driller CAD 36-40/hr, helper CAD 27-30/hr, plus overtime.
- Full Force (Smithers, BC): driller CAD 42/hr, helper CAD 28/hr, plus metre bonuses (simplyhired summary above).

**Australia (AUD, job-ad asking rates, not a survey)**
- Experienced diamond drillers: A$75-92.50/hr (Perth engineering-drilling ad), or A$50-70/hr plus metre bonus (surface diamond, FIFO).
- Trainee underground diamond driller: A$85-95k/yr.
- Search page: https://au.seek.com/multi-skilled-fifo-jobs/remote

**Loaded day cost used in my model (estimate)**
- Driller: about CAD 800/day. That is a 12-hour day of 8 regular hours at about CAD 40 plus 4 overtime hours at 1.5x, giving about CAD 600, plus about 30% burden (WCB, CPP/EI, benefits) and bonus.
- Helper: about CAD 560/day.
- Over about 240 days worked a year, a loaded driller costs about CAD 190k and a helper about CAD 130k (estimate).

### 2.3 Labour's share of $/m (estimate)

| View | Labour share | Basis |
|---|---|---|
| Contractor cost base | ~60% | Durin founder (TechCrunch) |
| Contractor revenue, my per-rig model (section 4) | ~52% | 1 driller + 2 helpers per shift, 2 shifts, 300 days, CAD 180/m, 15,000 m/yr |
| Quarry or mine-wide benchmarks | 35-45% (quarry, labour+maintenance+downtime); ~40% (mine personnel) | lane C sources |
| Athabasca all-in $/m (C$525-1,650) | **~20-30%** crew-driven: drill-crew wages ~12-20% plus crew share of camp and flights ~5-10% | Contractor line 47-57% of spend (CanAlaska MD&A, lane H) × ~40-50% labour, plus camp 11-13% × about half |

So automation attacks the biggest line for the *contractor*. But for a remote explorer, helicopters, fuel, camp, geology and assays stay. **Removing every person from the rig would cut Athabasca all-in $/m by at most about 25%.**

## 3. Who is trying (adversarial check)

### 3.1 Durin: the cleanest "operator" bet
| Item | Finding | Source |
|---|---|---|
| Founded / HQ | 2024, El Segundo CA (also reported as LA). Founder and CEO Ted Feldmann, third-generation mining family, Georgia Tech BSc. COO David Venegas. Head of Geoscience Christopher Seligman (PG). | https://dealroom.co/companies/durin/ ; https://www.venturescout.io/p/durin |
| Funding | USD 3.4M **pre-seed** (often called seed), Apr 23 2025. Led by 8090 Industries, with 1517, a16z, Bedrock, Champion Hill, Contrary, Day One and Lux. Dealroom puts the valuation at about USD 14M (lane H). | https://techcrunch.com/2025/04/23/durin-digs-up-3-4m-to-automate-drills-for-critical-minerals-exploration/ ; https://www.investmets.com/us-vc-firms-back-california-auto-drilling-firm/ |
| Rio Tinto | One of six startups in the Rio Tinto × Founders Factory Mining Tech Accelerator (2025 cohort): "automated drilling rigs to accelerate mineral discovery and reduce exploration costs". | https://foundersfactory.com/articles/mining-tech-press-release |
| Later rounds 2025-26 | **None found.** Searches across TechCrunch, aggregators (Preqin, Tracxn, VCBacked, PitchBook listing) and company pages through Oct 2026 show only the pre-seed. Aggregators list 11-50 staff; Built In says 20. Absence of evidence, not proof. | https://www.preqin.com/data/profile/asset/durin/738894 ; https://www.vcbacked.co/company/durin |
| What it builds | Its own rig, designed from early 2025. **300 m depth, 2.5-inch hole.** That is about BQ-class: BQ hole about 60 mm, NQ about 76 mm (memory). At first it was manually operated, with sensors logging data to train an automation model, plus an automatic pipe (rod) loader. Next version "autonomous". It built a remotely operable rig in 4 months, with testing in Nevada from late Apr 2025. A South Africa team built a solids-removal (mud) unit shipped to the US for field trials. | TechCrunch, above; https://x.com/tfeldmann/status/1915090442066305389 ; search summary of an Alfa Laval Africa post |
| Core or chips | **Core.** Humans "retrieving completed core samples at the end of the day". The site says "remotely operated, semi-autonomous core drilling rigs". | TechCrunch; https://www.durin.com/ |
| Business model | **Operator.** "Revenue from every meter drilled funds further R&D". It will run its own rigs on North American exploration projects before scaling production. Vertically integrated, with geological modelling, lab testing and drillhole planning on top. No mention of equity, royalties or rig sales. | https://www.durin.com/ ; venturescout |
| Customers | None named. No junior press release found naming Durin as contractor. | searches this session |
| Cost per metre | **Not claimed.** The pitch is "10X the speed of mineral exploration". | https://x.com/tfeldmann/status/1882461076417384640 |
| Autonomy timeline | Unattended in 2-3 years from 2025. People still deliver supplies, monitor and handle core. The goal is no crew standing at the rig. | TechCrunch; InvestMETS |

Read:
- Durin is exactly the company the question asks about. It is very early, about 18 months after pre-seed with no visible follow-on.
- Its first rig targets shallow US critical-minerals holes, not 400-800 m Athabasca holes in HQ/NQ.
- No published $/m and no named customer means no evidence yet that it breaks the labour cap.
- With a16z and Lux on the cap table, it owns the venture narrative for this idea.

### 3.2 XtremeX Mining Technology (XMT)
- USD 11M Series A (Jan 2025), led by GoGreen Partners. The rig is an "AC-electric automated coiled tubing and electric top-drive diamond core drilling rig" adapted from oil and gas.
  - Funded field trial with Ivanhoe Electric at Santa Cruz copper (Arizona), up to 2,000 m, twinning historic holes.
  - If successful, Ivanhoe contracts 3 rigs for up to 5 years.
  - Consortium includes Precision Drilling and Baker Hughes.
  - Sources: https://www.businesswire.com/news/home/20250113080687/en/ ; https://www.mining-technology.com/news/xmt-deploy-hybrid-drilling-rig-arizona-copper-project
- No trial results found as of Oct 2026.
- Read: this is the deep-core automated competitor, with depth suited to the Athabasca, and it already has a capitalised mid-tier buyer. Its model leans toward rig plus contract, not equity.

### 3.3 Tribe Tech (Belfast)
- TTDS GC 700, "the first autonomous reverse circulation rig". The pitch is to remove operators from the pad.
- First unit sold to Major Drilling (McKay subsidiary) for a Tier 1 iron ore mine in Australia, with field validation in Q4 2024. Partnered with Veracio (Boart Longyear). No results found.
- Sources: https://www.globalminingreview.com/mining/30072024/tribe-tech-ships-its-first-autonomous-rc-drill-rig ; https://mine.nridigital.com/mine_apr25/automated-exploration-drill-rigs
- Read: autonomy is landing first in **grade control, at a major's minesite, as chips**, sold to the incumbent contractor. That is the opposite of greenfield core.

### 3.4 Earth AI: owns rigs, but as an explorer
- USD 20M Series B (Jan 2025). Plans 100,000 m at "approximately $100/m". Rigs reach about 600 m (search summary). "Proprietary mobile low disturbance drilling". https://www.mining-technology.com/news/earth-ai-20m-ai-driven-mineral-exploration-drilling/
- TechCrunch, 29 Apr 2026: Earth AI "ramped up the drilling capacity" and is now building its own labs, because about "7,000 meters of samples we don't have data about" sit in lab backlogs. It targets a 5-day turnaround against about 5 months. https://techcrunch.com/2026/04/29/earth-ai-is-vertically-integrating-the-search-for-critical-minerals/
- No automation of its rigs is reported and no crew numbers are given. No resource estimate or sale to a major was found.
- Read: cheap metres just move the bottleneck to assays. That supports round-1 lane H: the step after the hole matters as much as the hole.

### 3.5 Incumbent automation roadmaps
| Player | What | Claim / status | Source |
|---|---|---|---|
| Boart Longyear (AIP-owned) | LF160i (2,000 m) with FREEDOM rod handling; automated inner-tube handling; digitised control panel tested in Chile and Australia, "launch expected end of 2025". Its manager envisions "one operator running several rigs, possibly remotely", conditions permitting. | "Up to 14%" productivity running through shift changes (lane C) | https://mine.nridigital.com/mine_apr25/automated-exploration-drill-rigs ; https://www.e-mj.com/features/battery-critical-minerals-demand-prompts-innovation/ |
| Epiroc | Diamec ARM: 84 N-rods, 252 m unassisted. Full-scale production at Agnico's LaRonde, run by contractor MRI. Earlier fully automated rod handler built with Ausdrill. | About 20% productivity gain (company data); no headcount cut stated | https://skillings.net/mining-technology-update-2026-autonomous-drilling-ai-ready-processing-and-deep-sea-robotics |
| Sandvik | DE130i/DE140i compact core drills with AUTO mode (SICA control). DA555 remote rod loader on DE800 iSeries; operator up to 50 m away. | Incremental | https://www.mining-technology.com/contractors/drilling/sandvik-mining/pressreleases/presssandvik-smarter-compact-core-drills ; https://www.miningmonthly.com:8443/exploration/news/1333421/helping-drillers-hands-rods |
| Major Drilling | RodBot (with MEDATech): manual, tip-control and semi-autonomous modes. Smart 8 underground drill with magnetic robotic arm (with Elite Automation). Bought the Tribe Tech rig. | Safety-led | https://www.majordrilling.com/major-drilling-usa-demonstrates-new-robotic-rod-handler-and-drill-analytics/ ; https://canadianminingjournal.com/news/major-drilling-joins-forces-with-medatech-to-use-robotic-rod-handler |
| Master Drilling (JSE) | Robotic underground core rig delivered (2024). Surface robotic core rig commissioning. Robotic slim rig: +50% productivity, -75% water against conventional rigs on the same contract. "Desert Elephant", a robotic, electric, water-recycling surface rig that "can work by itself", commissioned by 2026. New slim-drilling business in Namibia. **Slim drilling is about 4% of revenue.** | Company claims | https://www.miningweekly.com/article/robotic-rig-uplifts-productivity-50-cuts-water-75-master-drilling-reports-2025-03-27 ; https://www.engineeringnews.co.za/article/proudly-south-african-drill-rigs-without-human-intervention-on-way-2026-04-07 ; https://engineeringnews.co.za/article/driller-foresees-revenue-boost-with-strong-order-book-2024-04-19 (both 2025-26 pages returned 403; figures are from search snippets) |

Read: every large rig maker and contractor has a crew-light programme. A contractor-owner that builds its own rigs therefore competes with its suppliers. Today's productivity claims are 14-50%, not crew elimination.

## 4. Mining-face autonomy (mature) vs exploration core (not)

| | Production / blasthole / mining face | Exploration diamond core |
|---|---|---|
| Operator to rig ratio in service | Sandvik AutoMine surface: 1 operator to 1-3 rigs. Epiroc at Apatit: 1 operator to 6 Simba rigs, with +20% output and one machine at 95% utilisation. Office TeleREMOTE: up to 9 SmartROC rigs. First fully autonomous US quarry rig (Epiroc/Luck Stone 2025, GMG Level 4). | Still 2-3 per shift on the rig. Rod handlers and remote panels move the driller back from the rods, but they do not remove him. |
| Hole | Short, repetitive, known pattern, chips discarded | 300-2,000 m, every hole different, casing, wedges, orientation, core is the product |
| Rods | On-mast carousel | Rods "fetched from outside the mast", system "retaught for each hole" |
| Failure modes | Few | Lost circulation, stuck rods, fishing, broken clay-altered ground (Athabasca), -40 C |
| Site | Fixed pit, fibre/LTE, maintenance crew on hand | Moves every hole or two, fly-in, no maintenance base |
| Timeline | Deployed for about 10 years | Full autonomy "3-5 years"; wide adoption "at least ten to 15 years"; savings in remote exploration "minimal" (Saderholm) |

Sources: https://www.mining.sandvik/en/digital-solutions/automation/automine-autonomous/ ; https://www.epiroc.com/en-ae/newsroom/2019/epirocs-world-leading-automation-solutions-brings-apatit-js-to-new-levels ; https://canadianminingjournal.com/news/epiroc-introduces-the-office-teleremote ; https://www.epiroc.com/en-us/newsroom/2025/epiroc-and-luck-stone-launch-first-fully-autonomous-smartrocd65-drill-rig-in-us-aggregate-market ; https://mine.nridigital.com/mine_apr25/automated-exploration-drill-rigs

**Remote-operated exploration rigs.** Remote operation exists only as a panel 10-50 m from the rig (FREEDOM, DA555, Diamec ARM station). No exploration core rig was found operated from a distant control centre. That would need reliable comms at the pad: Starlink-class links now make this feasible in the north (memory), but no deployment was found. It would also need someone within reach to clear jams, change bits, add casing and box core.

## 5. Model: one supervisor runs 3-4 rigs (all estimate)

Per rig-year, generic Canadian surface diamond core (CAD). Script: /tmp/claude-0/-home-user-nuketime/b6d24066-bc2a-586f-8327-6094a85f677f/scratchpad/model.py

**Assumptions**
- Activity: 300 days, 2 shifts, 15,000 m/yr (50 m/day) at CAD 180/m. That gives CAD 2.7M revenue, consistent with CAD 2.2-2.5M per working rig at Major (lane B).
- Day rates: driller CAD 800/day, helper CAD 560, supervisor CAD 1,040, automation/maintenance tech CAD 900.
- Consumables: CAD 26.7/m. Rig depreciation and maintenance CAD 0.35M, fuel CAD 0.10M, overhead CAD 0.15M.
- Automation premium on rig capex (estimate; no list prices exist):
  - Scenario A: about USD 0.6M (CAD 0.82M).
  - Scenario B: about USD 1.0M (CAD 1.37M).
  - Both straight-line over 5 years, with software and maintenance opex on top.
- Productivity: +15% in A and +25% in B. The basis is no stops at shift change, the Boart "up to 14%" and Epiroc's about 20%, so B is a stretch.

| Scenario | Crew per rig-shift | Labour CAD/yr | Metres | Cost/m | Δ cost/m | Contractor EBIT at constant CAD 180/m | Experienced-driller days per rig-day |
|---|---|---|---|---|---|---|---|
| Base | 1 driller + 2 helpers | 1.40M (52% of revenue) | 15,000 | **CAD 160** | n/a | 11% | 2.0 |
| A: supervised, 1 supervisor : 3.5 rigs | 0.29 supervisor + 1 helper-grade tech + 0.25 automation tech | 0.82M | 17,250 | **CAD 125** | **-22%** | 31% | 0.57 (3.5x leverage) |
| B: near lights-out (Durin's vision), 1 : 4 | 0.25 remote supervisor + 0.5 on-site tech + 0.25 maintenance tech | 0.62M | 18,750 | **CAD 114** | **-29%** | 37% | 0.5 (4x leverage) |
| Downturn, 150 days, base | same as base | 0.83M | 7,500 | CAD 217 | n/a | -20% | |
| Downturn, A | | 0.50M | 8,625 | CAD 185 | -15% | -3% | |
| Downturn, B | | 0.39M | 9,375 | CAD 177 | -18% | +1% | |

What the model says:
1. **Cost per metre falls by about 20-30%, not 3x.**
   - Consumables, rig ownership, fuel and the automation premium do not scale down with headcount.
   - Someone still has to box core, mix mud, add casing and fix things. Helpers are cheaper and easier to train than drillers, but they are not zero.
2. **Capacity is the bigger effect.** Each experienced driller covers 3.5-4x as many rigs.
   - In an upcycle, an operator with 100 supervisors could field 350-400 rigs. Major fields about 340-400 working rigs with about 3,800 staff.
   - That is a real share-taking weapon *while* the shortage lasts.
3. **Who keeps the saving.** In a tight market, price is set by labour-capped incumbents, so the operator keeps it as margin: EBIT goes from 11% to 30-37%.
   - In a downturn, prices fall to incumbents' cash cost, utilisation halves, and capex stranding cuts the advantage to about 15-18%.
   - Lower operating leverage on labour is offset by higher fixed capital. Every downturn bankrupts somebody (Energold, CCAA 2019; Boart's restructurings).
4. **Athabasca all-in.** Assume the contractor is about 50% of spend and the contractor cost falls 22-29%, giving about 11-15% off. Fewer crew camp-days and crew flights add about 2-5%.
   - **Total: about 12-20% off a C$525-1,650/m all-in metre, a 1.15-1.25x lever.**
   - Helicopter moves, fuel, winter roads, geology and assays are untouched.
   - The bigger levers stay fewer holes and steering (lanes C and D): MinEx shows cost per discovery rising much faster than cost per metre.
5. **Sensitivity.**
   - If B achieved 1:6 (Epiroc production-grade) and the automation premium fell to USD 0.3M, cost/m would reach about CAD 100 (-37%) (estimate).
   - Even the best case does not reach the 1.5x lever for an Athabasca explorer.

## 6. Buyers and the ladder

**Who pays, and how much at once**
- **Majors and mid-tiers** are the capitalised buyers: Rio Tinto (Durin's accelerator), BHP, Agnico (the LaRonde ARM), Ivanhoe Electric (XtremeX exclusivity), and iron-ore majors (Tribe Tech via McKay).
  - They sign multi-year term contracts and care about safety (removing people from rotating rods) as much as cost.
  - They pay per metre, with no step-up; the step-up stays with the land owner.
- **Juniors** buy about 50-70% of greenfield metres in the Athabasca (lane H: juniors are 70.6% of Saskatchewan spend). They are cyclical, price-sensitive, and need a rig in the winter window, which is where a crew-light operator's capacity matters most. They cannot carry automation capex and will not pay a premium.

**The ladder exists, but automation climbs it top-down.** The best entry rungs are the high-volume near-mine ones.

| Rung | Size (lane B, estimate) | Automation fit | Note |
|---|---|---|---|
| Grade control (RC, minesite) | Part of about USD 3-4B minesite | **Highest**: repetitive, fixed site, chips; Tribe Tech is already here | Sold through incumbents |
| Resource definition / infill (core, near-mine) | Part of about USD 2.5B late-stage plus minesite | **High**: many similar holes from nearby pads, road access, term contracts | Best rung for a Durin-type operator |
| Geotech / site investigation | USD 5-10B (memory) | Medium: shallow, regulated, fragmented, local | Mostly sonic, auger and small core; low margin |
| Water wells | USD 10B+ (memory) | Low-medium: price-driven | |
| Slim-hole geothermal / temperature gradient | Under USD 1B, growing | Medium | Deep EGS is oilfield-style (Fervo); XtremeX's oilfield DNA fits better |
| Greenfield exploration (fly-in, deep core) | About USD 1.5-2B worldwide; Athabasca about CAD 300-450M | **Lowest**: every hole and site different, remote, short programs | The rung Terranox cares about |
| Drill-for-equity / carried interest | Discovery value about USD 13.5B/yr (MinEx) | n/a | Converts the operator into a prospect generator, Terranox's model |

So "exploration → resource definition → grade control → geotech/water/geothermal" is real as a market sequence. But the natural *entry* point for an automation operator is resource definition or grade control at a major's site, not greenfield. Greenfield is the rung where automation helps least.

## 7. Ceiling (estimate)
- The global contract exploration and resource-definition pool is about USD 7.5B (range 6-9B) (lane B). A 10% share is about USD 0.75B revenue. At 30% EBITDA and 8-10x, that is **about USD 1.8-2.3B of enterprise value**.
- Adding geotech, water and geothermal (about USD 15-25B combined, fragmented) could plausibly double revenue over a decade, taking value to about USD 3-5B.
- Comparables: Major Drilling (CAD 889M revenue, 11.6% EBITDA), Boart (sold for about USD 371M), Epiroc as an automation OEM (about SEK 60B revenue, memory). An automated operator is a better Major Drilling. If it instead licenses its autonomy stack, it becomes an Epiroc division.
- **Verdict on ceiling:** a credible USD 1-5B industrial, not "very large". The only route above that is the equity rung, which is a different company: the asset owner.

## 8. Scoring against Dhruv's gold rubric (honest)

| # | Test | Score | Why |
|---|---|---|---|
| 1 | Discovery is 80%+ of the work; physical step trivial | **Fail (0)** | The physical step *is* the product. The hard part is robotics in bad ground, not discovery. Holes still miss at the same rate; the operator just bills for them more cheaply. |
| 2 | Signal in illegible public data; ML essential | **Fail (0)** | ML matters for control (Durin logs sensor data to train an autonomy model), but the data is the company's own rig telemetry, not public data. Incumbents are doing the same. |
| 3 | Unproven asset bought cheap | **Fail / N/A (0)** | A service company buys no asset, unless drill-for-equity. |
| 4 | Capitalised buyer pays step-up at once | **Partial (0.5)** | Majors pay at once, per metre, on term contracts. That is cost-saving pricing, not a step-up. |
| 5 | Ladder to climb | **Pass (1)** | Grade control or resource definition, then exploration, then geotech, water and geothermal, then possibly drill-for-equity. The rungs are real and sellable. |
| 6 | Ceiling very large | **Borderline (0-0.5)** | About USD 1-5B. Above the USD 100-400M/yr tool band, below "very large". |
| | **Total** | **About 1.5 / 6** | |

- Lever check: 1.15-1.25x on Athabasca all-in $/m, and 1.3-1.4x on contractor $/m. Both are at or below the 1.5-3x the rubric now accepts.
- **Drilling ban:** this sits squarely inside the 2026-10-03 drilling ban. It is a drilling contractor by definition. Noted, not filtered.

## 9. Bottom line
- **Is there a large company here?** A good one, not a rubric one. A crew-light operator can cut contractor cost per metre by about 20-30%. While the driller shortage lasts, it can multiply each experienced driller's reach 3.5-4x and earn about 30% EBIT in place of about 11%.
- **The shortage is a cycle phenomenon.** Exploration-core autonomy is 3-5 years from commercial and 10-15 years from wide adoption.
- **Incumbents already sell the components:** Boart, Epiroc, Sandvik, Major and Master Drilling.
- **The idea is already funded:** Durin (a16z, Lux; operator model; 300 m BQ-class core; no later round or customers visible) and XtremeX (USD 11M; 2,000 m; Ivanhoe Electric as anchor).
- **For Terranox:** it does not change the economics of an Athabasca discovery hole by more than about 15-20%. Do not start it.
- **What to do instead:** treat Durin and XtremeX as potential suppliers of winter-window rig capacity. If one reaches Athabasca depth, a capacity or right-of-first-refusal agreement could be worth more to Terranox than the $/m saving. Fewer and better-steered holes remain the bigger lever (lanes C and D).

## 10. Gaps
- Durin: any 2026 round, customers or $/m. The only fetchable sources are 2025, and the Lever job page returned 404.
- XtremeX Santa Cruz trial outcome. Tribe Tech field-validation results.
- Master Drilling's Desert Elephant specs and whether it cores (2026 pages returned 403).
- No list prices for automation kits; the capex premium in section 5 is an estimate.
- No audited labour share of cost for any listed contractor. The Foraco and Major employee-benefit notes were not retrieved.
