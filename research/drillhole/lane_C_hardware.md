# Lane C: hardware attempts to make an exploration hole physically cheaper

Written 19 Oct 2026. Research limits: the shared WebSearch budget ran out partway through this lane. Items that
could not be checked against a source are marked "(memory)", and estimates are marked "(estimate)". Every number
that has a source cites its URL.

## 10-line summary
1. Drilling cost per metre has not fallen in decades; it has risen slowly in real terms. Off-mine-site core drilling in Quebec cost C$110.52/m in 2006 and C$170.16/m in 2018, which is +54% nominal and roughly +25% real (estimate, deflating by Canadian CPI from memory). Australian drilling went from A$89/m (1997) to A$207/m (2017) nominal. In both series the cost moves with the exploration cycle, not with technology.
2. The decisive comparison is the same contractor, same core and same rods. Drilling on a mine site, near the deposit, cost C$85-100/m in Quebec, against C$145-178/m for greenfield drilling in the same years. That gap of about 40-50% comes from logistics, moves, standby and utilisation. It does not come from rock physics.
3. On a remote program the contractor's metre rate is only a fraction of the all-in cost. Athabasca contractor rates are about C$250-400/m (older modelled figure: C$600/m). Refined Energy budgeted about C$1.7M for 1,200 m in 3 holes in Q1 2026, with helicopter, fixed-wing, fuel and camp, which is about C$1,400/m all-in. That is 3.5-5x the contractor rate. Novo Resources says extras routinely double the quoted base rate.
4. The cost is therefore mostly labour multiplied by time on site, plus logistics such as helicopters, fuel, camp, winter roads, standby and moves. Consumables come third. The physics of cutting rock is a small share, so a faster bit attacks the smallest bucket.
5. Coiled tubing (RoXplorer: DET CRC 2010-18, then MinEx CRC) is the best-funded attempt to change the drilling method itself. It is still "pre-commercial" 16 years after DET CRC began. The licensee, IMDEX, said it "does not intend to enter the drill rig manufacturing or drill rig operating businesses". The method returns chips, not core.
6. Chips-based methods are a dead end for the Athabasca target. RC, aircore, RAB, sonic, coiled tubing and water hammer are all cheaper per metre (RAB about $12-20/m, aircore $18-30/m, RC $30-55/m, diamond $110-250/m base). The target, however, sits under up to 100 m of drift and 400-800 m of sandstone. The drillers need intact core to log clay alteration, structure and graphite, and that sandstone is often friable and clay-altered.
7. Novel physics (GA Drilling plasma, Quaise millimetre-wave, Petra thermal, EarthGrid plasma) has all moved to geothermal or utility tunnelling, where the target is a big, hot, deep hole. None of it produces core, and none has a mineral-exploration product.
8. Automation from Boart Longyear (LF160i plus FREEDOM rod handler) and Epiroc (Diamec ARM) mostly delivers safety and modest productivity gains: "up to 14%" for semi-autonomous running through shift changes. It does not yet take a person off the rig on surface exploration, and the incumbents already own it.
9. Earth AI (YC S19, US$20M Series B in Jan 2025) is the only company here that combined its own cheap rig with its own targets. It claims a target of about US$100/m and "up to 80%" lower exploration cost, with no independent check. Its rigs suit shallow Australian targets, not 500-800 m Athabasca holes. Its business model is Terranox's model, so it is an analog or competitor, not a gap.
10. Verdict: the real cost-down is not a rig company. The largest contractor-plus-manufacturer, Boart Longyear, was taken private for about US$371M. The levers that matter are fewer holes, more information per hole, stopping or steering holes in real time, and cutting logistics and standby. That is mostly software and operations. A pure hardware play fails rubric items 2 and 6.

---

## 1. Baseline: what a metre costs and how it has moved

### 1.1 Long-run series
**Quebec, Annual Census of Mining Investment (Institut de la statistique du Québec), core drilling, CAD nominal.**
Source spreadsheet: https://statistique.quebec.ca/en/fichier/change-in-number-of-metres-drilled-and-cost-per-metre-for-core-drilling-quebec.xlsx
(page: https://statistique.quebec.ca/en/produit/figure/change-in-number-of-metres-drilled-and-cost-per-metre-for-core-drilling-quebec)

| Year | Off-mine-site exploration (C$/m) | On-mine-site exploration (C$/m) | Mine production drilling (C$/m) | Off-mine metres |
|---|---|---|---|---|
| 2006 | 110.52 | 68.28 | 69.18 | 814,895 |
| 2007 | 148.42 | 96.68 | 58.04 | 1,316,506 |
| 2008 | 166.84 | 91.64 | 84.55 | 1,488,125 |
| 2009 | 140.60 | 108.59 | 79.50 | 905,905 |
| 2010 | 142.19 | 127.57 | 90.15 | 1,352,924 |
| 2011 | 165.78 | 120.14 | 88.00 | 1,864,423 |
| 2012 | 178.64 | 132.85 | 107.48 | 1,349,498 |
| 2013 | 149.42 | 134.95 | 86.19 | 647,456 |
| 2014 | 146.75 | 178.43 | 87.24 | 532,280 |
| 2015 | 144.38 | 92.50 | 74.96 | 673,672 |
| 2016 | 143.47 | 88.46 | 80.10 | 873,138 |
| 2017 | 150.22 | 110.05 | 84.33 | 1,706,118 |
| 2018 | 170.16 | 128.53 | 100.76 | 1,273,588 |

How to read the table:
- The greenfield rate rises and falls with the cycle. It peaks with metres demanded (2008, 2012, 2018) and eases in the 2013-16 bust. That is pricing by rig and crew supply, not a technology curve.
- From 2006 to 2018 it rose 54% nominal. Canadian CPI rose about 22% over the same years (memory), so the real increase is about 25% (estimate). That is flat to slightly up over 12 years of rig-control, bit and wireline improvements.
- Mine-site production drilling uses the same core method, often with underground rigs, and costs 50-60% of greenfield in most years. The difference is short holes, no mobilisation, a rig that never moves far, a nearby workforce and very high utilisation. **This is the strongest single piece of evidence that the cost lies in logistics and utilisation, not physics.** (Caveat: some mine-site drilling is smaller-diameter, shorter-hole work, so not all of the gap is logistics.)

**Australia, ABS series (via MinEx CRC).** Exploration cost per metre drilled went from A$89/m (1997) to A$207/m (2017), nominal. Australian CPI rose about 70% over that period (memory), so the real increase is about 35% (estimate). Source (the original page returned 403 on fetch, so the figure was taken from the search snippet): https://www.mining.com/web/south-australian-geologists-to-drive-a-revolution-in-minerals-exploration/
An Australian trade report put the cost at A$238/m at end-2007, and noted that in the early-2000s slowdown it fell back to the same level as the 1990s: https://miningmonthly.com/markets/international-coal-news/1293657/spending-drilling
Metals Economics Group found that total exploration spend per metre drilled rose 2.5-3x between 2001 and 2008, partly because assaying and testing took a growing share: https://onemine.org/documents/trends-in-minerals-exploration-activity

Schodde (MinEx Consulting) reports that cost per discovery roughly tripled over a decade, from about US$86M to about US$238M (constant 2016 dollars). Per-discovery cost is rising much faster than per-metre cost. **The waste is in metres drilled per discovery, not in dollars per metre.** Source: https://emj.epubxp.com/i/822333/31

### 1.2 Method base rates (unspecified "$", Australian context, base rate only)
Novo Resources: RAB $12-20/m, aircore $18-30/m, RC $30-55/m, diamond $110-250/m. Consumables, slow penetration, standby, mobilisation and water cartage often bring the all-in cost to "double the base rate as quoted". https://novoresources.com/exploration/glossary/drilling-techniques-costs/
In a 2011 Australian budget, RC cost A$120/m and diamond A$200/m. RC is "usually 25-40% cheaper than diamond". https://www.rcdrilling.com/rc-drilling-guide/comparative-costs-of-drilling/

### 1.3 Athabasca specifically
- Contractor rate: C$250-400/m. Depth to the unconformity is 400-800 m across much of the basin and 0-200 m at the margin. https://uraniumx.ca/athabasca-basin
- A modelled seismic-integration paper used 121 holes at an average 650 m and C$600/m, for about C$47.2M of drilling. https://www.researchgate.net/publication/337143836_Effective_utilization_of_seismic_reflection_technique_with_moderate_cost_in_uranium_exploration
- All-in program: Refined Energy's Dufferin West Phase I is about 1,200 m in 3 holes, budget about $1.7M (CAD implied), Q1 2026. Contracts cover the driller plus helicopter and fixed-wing logistics, fuel, accommodation and a ground gravity survey. That is about C$1,400/m all-in (estimate, an upper bound because the gravity survey is included). https://www.stocktitan.net/news/RRUUF/refined-energy-provides-dufferin-project-drill-program-q4d63qse48fe.html
- Typical hole cost: 600 m at C$250-400/m is C$150-240k for drilling alone. Applying the 3-5x all-in multiplier gives roughly C$0.5-0.9M per hole for a small remote program (estimate).
- Ground conditions: at CanAlaska's Cree East, "intensely hydrothermally altered aureoles" made holes hard to complete. In one hole, the entire 400 m sandstone column was "heavily fractured, clay altered and friable". https://canalaska.com/winter-drilling-at-west-mcarthur-and-cree-east-uranium-projects-hit-graphitic-target-zones-and-strong-alteration-systems/
- The Fond du Lac winter program was hampered by -40 to -50 C conditions. https://canalaska.com/canalaska-uranium-completes-first-phase-fond-du-lac-drill-program/
- Cover: there is very little outcrop, and glacial drift is up to 100 m deep. https://www.seequent.com/page/uranium

### 1.4 Where the money goes (decomposition)
No source found gives a clean contractor-level percentage split; this gap was not filled. The best available evidence:
- SME-cited benchmarks for hard-rock drilling (quarry context): consumables about 30-40%, energy 20-25%, labour, maintenance and downtime 35-45%. https://setmakina.com/en/technical-insights/cost-per-meter-drilled-quarry/
- A mine-wide operating-cost model: personnel about 40%, materials 35%, energy 15%, services 10%. https://cdn-web-content.srk.com/upload/user/image/Operating%20Cost%20for%20Miners_BC_CIM22_May_02_2022_GMP_vp_2022050520220510165012372.pdf
- Labour is the binding constraint. Major Drilling has repeatedly cited the shortage of experienced crews as pressure on "labour costs and productivity". It raised wages to retain drillers, and in 2012 it called the labour shortage "our biggest operational challenge". https://www.majordrilling.com/wp-content/uploads/2023/08/Q4-2021-Press-Release-Final.pdf , https://www.majordrilling.com/wp-content/uploads/2023/08/Press-Release-Q3-2021-Final.pdf
- Combined estimate for a remote Athabasca hole, all-in (estimate):

| Bucket | Share (estimate) |
|---|---|
| Logistics: helicopter or fixed-wing, fuel, camp, winter road, moves, standby | ~35-50% |
| Rig and crew time (labour-dominated) | ~25-35% |
| Consumables: bits, rods, casing, mud, additives | ~10-15% |
| Geology and supervision: logging, core handling, probe | ~10% |
| Assays | ~5% |

  The pure "cut rock faster" share is a fraction of the rig-time line.

**Answer to the key question.** Cost per metre stays flat for four reasons:
- (a) Most of the cost is people times days in a remote place, and that cost grows with wages.
- (b) Penetration rate is rarely the binding constraint. Tripping rods, bad ground, casing, moves between holes, weather and standby dominate the clock.
- (c) The contractor market is a cyclical, crew-limited service, so any productivity gain is priced away when metres demand is high (see the 2008 and 2012 peaks).
- (d) Sample standards (core for structure and alteration, assay QA/QC under NI 43-101 and JORC) fix the method in place, and the method fixes the cost floor.

It is not physics.

---

## 2. Technology-by-technology

### 2.1 Portable, man-portable and heli-portable diamond rigs
- **Hydracore (Delta, BC).** Describes its rigs as "the most portable available in any depth capacity". Directory: https://business.deltachamber.ca/directory/Details/hydracore-drills-ltd-1469708
  - HC2000 (2008): maximum lift per move 1,100 lb (500 kg), total 3,860 lb, flyable. https://www.equipt.com/listings/1167998-used-2008-hydracore-2000-drill-rigs-in-british-columbia
  - HC5000MAX (2023): 1,500 m HQ or 2,000 m+ NQ, 8,000 lb on skid, "fly rig" option; listed used at US$240k. https://machinerytrader.eu/listing/for-sale/240069441/2023-hydracore-hc5000max-vertical-drills
  - **The saving is in moving the rig.** Heli-portable rigs cut pad building and roads, which matters in muskeg and summer Athabasca. They do not change crew size, metres per shift or the need for helicopter hours. They are widely adopted in BC, the Yukon and northern Canada and are already a commodity. No cost-per-metre reduction claim was found.
- **Zinex A5, Kluane Drilling rigs, "Discovery Drilling".** Not verifiable this session because search was exhausted. From memory: Zinex makes small man-portable core drills (shallow, BQ/AQ, roughly 100 m class); Kluane Drilling (Whitehorse) builds and operates light heli-portable core rigs. These are niche suppliers inside an existing contractor market (memory). None claims a step change in cost per metre.
- **Boart Longyear LF series and Epiroc Christensen (CT/CS series).** These are the standard surface core rigs, already the baseline in the numbers above (memory for the model list).
- **Why it does not change the curve:** portability reduces mobilisation and environmental footprint (with fewer pads, permitting gets easier). Crew, helicopter time and core handling remain. Portability is already priced into northern contracts.

### 2.2 Slimhole diamond (BQ/AQ/NQ vs HQ/PQ)
- A smaller diameter means lighter rods, smaller rigs, fewer helicopter loads, less mud and faster tripping. Costs rise with core diameter (Novo, above).
- The limits: in broken, clay-altered Athabasca sandstone, small holes get stuck more often, recover less and have less room to case off bad ground (memory). Smaller core also means less assay mass for QA/QC and, for uranium, a weaker sample for disequilibrium and density work (memory). Athabasca practice is generally NQ/HQ with PQ or HW casing through the overburden (memory).
- Adoption is already maximal where geology allows. This is an operator choice, not a company.

### 2.3 RC, aircore, RAB, percussion
- These are 3-10x cheaper per metre on base rates (Novo). RC is acceptable under JORC and NI 43-101 for many resource estimates (gold, iron ore, base metals) with QA/QC.
- They are used in the Athabasca only at the shallow margin. CanAlaska drilled 34 vertical RC holes at Fond du Lac in 2011, where hematisation and chloritisation were visible in the chips and radioactivity was logged down the rods. Core was then used for follow-up, and it found the mylonites of the Airport Fault. https://canalaska.com/canalaska-uranium-completes-first-phase-fond-du-lac-drill-program/
- **Why not basin-wide:**
  - (a) Depth: aircore and RAB are regolith tools (tens of metres to about 100 m), and RC rarely goes past 300-400 m cleanly (memory). The basin targets sit at 400-800 m+.
  - (b) Core is needed. Explorers map clay species (illite, chlorite, dravite) with TerraSpec spectrometers on core, and they need the orientation of structures and graphitic conductors. https://sedar-filings-primary.thecse.com/00010457/1203132042090378.pdf (Uravan program, systematic ASD TerraSpec on core)
  - (c) Water-saturated, friable sandstone under 100 m of drift loses circulation and contaminates chips (memory).
  - (d) Hitting high-grade uranium in RC returns radioactive dust at surface, a radiation-protection problem (memory).

### 2.4 Sonic drilling
- Sonic drilling is excellent for continuous core through unconsolidated drift and till, and it is used in environmental and geotechnical work and for overburden sampling (memory). In practice it reaches about 100-200 m, and it is slow and expensive per metre in hard rock (memory).
- Its fit in the Athabasca is limited to the drift: till or basal-sandstone geochemistry sampling at the margin, or pre-collaring. It is not a target-testing tool. No Athabasca sonic program was found (search exhausted).

### 2.5 Coiled tubing (DET CRC RoXplorer, then MinEx CRC CT500)
- History:
  - DET CRC (2010-2018, Australian Government CRC program plus industry) built RoXplorer. It uses a continuous steel coil in place of rods, so drilling and tripping need no rod connections, and it has a downhole motor, lower fuel use and a smaller footprint. https://www.globalminingreview.com/mining/07082018/revolutionary-new-drill-rig-licensed-to-imdex/
  - Licensed to IMDEX in 2018. IMDEX "does not intend to enter the drill rig manufacturing or drill rig operating businesses". A trial at a Barrick site in Nevada used Lab-at-Rig real-time geochemistry on cuttings (same source).
  - The Nevada trial "confirmed the potential of CT drilling but showed that fluid management could be improved, sampling procedures streamlined and the drill site footprint reduced" (MinEx CRC CEO).
  - The 2021 trials: 241.5 m through swelling clays and sandstone (best 115.5 m in 6 h), and 290 m in hard, fractured rock (80 m in 6 h). Samples came from a shaker-screen sampling system, in 1 m intervals. Article text: https://minexcrc.com.au/wp-content/uploads/2022/10/ADIA-Magazine-Trials-break-new-ground-002.pdf
  - June 2026: the CT500 prototype "completed pre-commercial trials". MRIWA's summary says it had competitive penetration, more than double conventional productivity and lower water and fuel use. It is now in "Phase 3" (MRIWA M10552). No commercial partner and no cost figure are named. https://www.mriwa.wa.gov.au/news-and-events/coiled-tubing-drilling-delivers-the-goods-for-mineral-exploration/
- What happened to commercialisation: 16 years and two CRCs have produced no product. The licensee will not build or run rigs, and Barrick's 2018-era option produced no public results (none found). The economic logic is the reason. Coiled tubing attacks rod handling and tripping, but contractors make their money on crew-days and have no reason to adopt a capital-heavy, non-standard rig. Explorers cannot buy rigs themselves.
- **Fatal for the Athabasca:** it returns chips, not core, and it has only been shown to about 300 m.

### 2.6 Automation, rod handlers and remote operation
- **Boart Longyear LF160i:** 2,000 m capacity, "autonomous and remote-control capabilities", paired with the FREEDOM automated rod-handling system. Semi-autonomous running through breaks and shift changes is claimed to add "up to 14%" productivity. Source (403 on direct fetch, so taken from the search snippet): https://www.e-mj.com/features/battery-critical-minerals-demand-prompts-innovation/
- The contractor Ranger Drilling used the FREEDOM Loader on a Rio Tinto contract. The selling point is that the remote panel moves the driller away from moving rods. https://www.rangerdrilling.com.au/?p=1635
- **Epiroc Diamec ARM** (May 2025): an 84 N-rod magazine reaches 252 m unassisted, and operators work from a remote station. The claims are safety and "boost productivity"; no crew reduction is stated. https://www.globalminingreview.com/mining/20052025/epiroc-launches-diamec-automated-rod-magazine/ . The first underground deployment was at Agnico Eagle's LaRonde. https://im-mining.com/tag/rod-handler
- **Owner:** Boart Longyear was taken private by American Industrial Partners for about A$500.7M (US$371M), completed 10 Apr 2024. https://bnamericas.com/en/news/american-industrial-partners-completes-take-private-acquisition-of-boart-longyear , https://canadianlawyermag.com/cl-plus/deals/1115
- **Read:** this is incremental (about 10-15%) and safety-driven, and the incumbents own it. The real prize is running a surface rig with one person, or none, which would remove the biggest line item, crew-days times rotation and camp. No one has shown that in remote surface exploration. The constraint is not the rod handler; it is bad ground, casing, core handling and orientation, and fixing things. If it arrives, Epiroc or Boart will sell it.

### 2.7 Hammers in hard rock (Wassara water-powered DTH)
- LKAB's Wassara W100 has drilled over 30M metres at LKAB (production blast holes, 1.5% maximum deviation). The vendor claims up to 5x penetration in some applications. https://lkab.com/en/who-we-are/lkab-wassara , https://wassara.com/
- The mining page lists production uses only (caving, stoping, degasification, utility holes) and says nothing about exploration core or sample recovery. https://www.wassara.com/what-we-do/mining
- **Read:** this is a production-drilling tool that makes chips. It is irrelevant to core-dependent exploration.

### 2.8 Novel physics
| Company | Physics | Funding | Status | Relevance to mineral exploration |
|---|---|---|---|---|
| GA Drilling (Slovakia) | Electric-arc plasma pulse (PLASMABIT) | Nabors US$8M (Mar 2022), total new rounds >US$20M; EUR 4.2M (Lead Ventures/MOL) for plug-and-abandon tests | "Laboratory-proven"; pivoted between ultra-deep geothermal and oil and gas plug and abandon | None; no core. https://www.thinkgeoenergy.com/nabors-invests-in-ultra-deep-geothermal-drilling-tech-firm-ga-drilling/ , https://www.thinkgeoenergy.com/slovakian-ga-drilling-receives-significant-funding-and-signs-service-agreement |
| Quaise Energy | Millimetre-wave (gyrotron) vaporisation | US$134M Series B first close (Jul 2026), US$230M total | >100 m in granite in 2025; "approaching 1 km" in Texas; first geothermal power targeted 2030 | None; it vaporises rock, so it returns no sample at all. https://www.energyglobal.com/other-renewables/10072026/quaise-energy-raises-us134-million-in-first-close-of-series-b/ |
| Petra | Non-contact thermal boring, 20-60 in diameter | US$33M total (Series A US$30M, DCVC, Dec 2021) | Pilot of 20 ft in Sioux Quartzite at about 1 in/min; targets utility undergrounding | None. https://techcrunch.com/2021/12/09/petra-emerges-from-stealth-with-30m-raised-for-tunnel-boring-robot-swifty/ |
| EarthGrid | Plasma-torch tunnel boring robot | Seed >US$30M | Jun 2024: 40 m3 in greywacke in 30 h with one torch; 1 m bore estimated at about 40-120 MW | None. https://www.undergroundinfrastructure.com/news/2024/june/earthgrid-successfully-field-tests-tunnel-boring-robot-launches-two-torch-plasma-excavation-system |
| Novamera (Canada) | Borehole mining (Sustainable Mining by Drilling), i.e. extraction rather than exploration | C$5M Series A (BDC, Chrysalix, 2021) plus SDTC | Trial at an Anaconda Mining site in Newfoundland; later status not found (site 503) | Adjacent: mining, not exploring. https://www.businesswire.com/news/home/20210727005129/en/Novamera-Closes-%245-Million-Series-A-Financing-to-Advance-Its-Precision-Mining-Solution-Sustainable-Mining-by-Drilling |
| Laser (Foro Energy) and thermal spallation (Potter Drilling) | | | Oil and gas or geothermal; faded (memory) | None |

**Why none of these came to exploration:**
- (a) They destroy the sample, and the sample is the product of an exploration hole.
- (b) Their economics only work where the hole is the product (geothermal wells, tunnels) and the hole is deep, wide, hot and hard.
- (c) Power needs are measured in MW (EarthGrid, Quaise gyrotrons), which is absurd at a fly-in Athabasca pad.

### 2.9 Earth AI (Sydney; YC S19) — the closest analog to "cheaper hole plus own targets"
- **Model:** predict deposits with AI, drill-validate with in-house rigs, then sell the rights to majors. It started as pure software. Prospective customers would not pay for predictions alone, so it built drills to prove them. https://www.all-ai.de/news/top-news24/milliarden-unter-der-erde-diese-ki-zeigt,-wo-der-schatz-liegt , https://www.ycombinator.com/companies/earth-ai
- **Rig:** "low disturbance drilling". It needs no groundworks and has onboard mud filtration (likely a mud-rotary or small diamond hybrid; the type is unconfirmed). https://www.esgtoday.com/earth-ai-raises-20-million-for-ai-powered-clean-energy-metals-exploration-solution/
- **Cost claims, all self-reported and mutually inconsistent:**
  - YC profile: site testing "1/4 cheaper and 4X faster".
  - Elsewhere: about half the cost of conventional drilling and fieldwork.
  - Series B release: plans 100,000 m "at a cost of approximately $100 per meter"; exploration cost "up to 80%" lower; 75% "discovery success rate" against an "industry average" of 0.5%.
  - Sources: https://www.ycombinator.com/companies/earth-ai , https://www.esgtoday.com/earth-ai-raises-20-million-for-ai-powered-clean-energy-metals-exploration-solution/ , https://www.mining.com/?p=1170737
  - US$100/m sits at the bottom of the diamond range and is RC-like pricing. That fits shallow holes in NSW. It says nothing about 600 m through Athabasca sandstone.
- **Funding:**
  - Gagarin Capital A$2.5M (2019). https://www.globalminingreview.com/finance-business/20082019/gagarin-capital-invests-aus25-million-in-earth-ai/amp/
  - US$20M Series B (Jan 2025), led by Tamarack Global and Cantos Ventures, with Overmatch, Alpaca, Sparkwave, YC and Scrum Ventures. https://www.esgtoday.com/earth-ai-raises-20-million-for-ai-powered-clean-energy-metals-exploration-solution/
  - YC lists a 12-person team.
- **Results:**
  - Fontenoy palladium with ASX-listed Legacy Minerals (Nov 2024), a mineralised system of about 2 km2, described as "one of the largest palladium mineral systems in Australia". https://www.globalminingreview.com/exploration-development/21112024/earth-ai-and-legacy-minerals-announce-first-ever-greenfield-palladium-discovery-using-ai/
  - Willow Glen gold (Dec 2024): 650 m drilled, with "seven samples ... grading 1.14 g/t gold". That is a modest early-stage indication, not an economic intercept. https://www.northernminer.com/news/earth-ai-finds-gold-near-willow-glen-molybdenum-project/1003874184/
  - Six new tungsten, cobalt and gold prospects, with drilling planned from May 2025. https://northernminer.com/news/earth-ai-unveils-six-mineral-prospects-in-australia/1003877110
  - As of these sources, there is no resource estimate and no reported sale of rights to a major.
  - Founder: "we really need to build more rigs" (2025) https://secure.northernminer.com/news/podcast-from-silicon-valley-to-mining-ft-earth-ai-founder-roman-teslyuk/1003890443/
- **Read for Terranox:**
  - Earth AI shows that a vertically integrated "AI plus own cheap rig" explorer can raise venture money. It also shows the rig is a means, not the product. After about 7 years, the evidence is claims of a "discovery" (anomalous mineralisation), not a monetised step-up.
  - Its cheap-rig advantage depends on shallow targets in accessible farmland. The Athabasca removes both conditions (deep holes, fly-in or winter-road access, core required).
  - It is the strongest existing owner of the "explorer that drills its own targets cheaply" idea, so treat that idea as owned.

---

## 3. Adoption filter: why cheaper-per-metre methods lose
1. **Sample requirements.** NI 43-101 and JORC do not mandate core, and RC is fine for many resources. The Athabasca workflow, however, needs core:
   - for structure orientation and graphitic fault logging;
   - for spectral clay alteration vectors (TerraSpec);
   - for radiometric probe calibration against chemical assay (disequilibrium);
   - for density.

   Any chips method downgrades a hole from "test" to "screen" (memory for the probe and disequilibrium practice).
2. **Depth.** Aircore, RAB, sonic and coiled tubing as demonstrated are all at 300 m or less. The basin needs 400-800 m+ (uraniumx.ca above).
3. **Ground.** Friable, clay-altered, fractured sandstone (Cree East, 400 m column) needs casing options and full-size core tools.
4. **Logistics.** Rig speed does not shorten winter-road windows, helicopter rates or camp. These dominate all-in cost (Refined Energy, about 3.5-5x the contractor rate).
5. **Market structure.** Contractors bill by metre or hour and are crew-limited, so productivity gains flow to contractor margins in tight markets. Explorers are juniors who cannot fund new rig classes. Manufacturers, Epiroc and Boart Longyear (now AIP-owned), already sell incremental automation.
6. **Ceiling.** The whole drilling-services and rig segment is small. Boart Longyear's equity was worth about US$371M at its take-private, and its Drilling Services revenue was about US$450-530M a year in 2015-16 (https://www.sec.gov/Archives/edgar/data/0001400561/000157104917005032/t1701531_ext3e.htm). A hardware company that wins this market lands in the "$100-400M/yr tool or service" band that rubric item 6 rejects.

---

## 4. Where the real cost-down opportunity is

The data points one way. Greenfield core costs about 1.7x mine-site core. All-in costs 2-5x the contractor rate. Cost per discovery grows far faster than cost per metre. So the money is in **metres per discovery** and **logistics per metre**, not in **dollars per metre of cutting**.

| Lever | Mechanism | Hardware? | Who owns it | Rubric fit |
|---|---|---|---|---|
| Fewer holes (targeting) | Better prior probability per hole | No: software or data | Terranox itself, Earth AI, KoBold, others (other lanes) | High, but this is Terranox's core business, not a new company |
| More information per hole | Downhole probes, core scanning (hyperspectral, XRF), Lab-at-Rig, structure from imagery | Partly | IMDEX (Lab-at-Rig, REFLEX), Corescan (acquired by Veracio/Boart), Minalyze (memory) | Medium; tool market, incumbents strong |
| Steer or stop holes in real time | Decide at 300 m whether to continue, wedge or abandon; directional daughter holes off one pad | Mostly software over existing tools (Devico, IMDEX directional) | Partly owned (directional coring is standard at big Athabasca projects; memory) | Medium; a decision layer, not a rig |
| Logistics optimisation | Pad sharing, winter-road batching, multi-rig scheduling, helicopter hours, standby reduction | No | Fragmented; consultants (e.g. Dahrouge-style operators) | Low ceiling as a service |
| One-person or no-person surface rig | Removes the crew-days multiplier | Yes | Epiroc and Boart R&D | Real, but owned by incumbents and years out |
| New cutting physics | Faster rock removal | Yes | Geothermal and tunnelling players | Wrong bucket; destroys the sample |

**Verdict on "is it a hardware company?" No.**
- Hardware that makes a metre cheaper attacks the smallest cost bucket, mostly yields chips the Athabasca target cannot use, and is captured by contractors in tight markets. Where it works, it has been absorbed by two incumbents. Even fully successful, it sits in a sub-$1B services market.
- The defensible cost-down is fewer and better-steered holes. That is a software and decision problem, sitting on public data and real-time hole data, and it overlaps Terranox's own business.
- The one "new company" shape left in this lane is an operator. It would run Athabasca drill programs as a logistics-optimised, data-driven service: batch holes across juniors, share camp and helicopter, steer holes in real time. This is an execution business, not a rubric-1 discovery business. It sits squarely inside the 2026-10-03 drilling-based ban, now lifted for this question.

## 5. Gaps (search budget exhausted)
- No contractor-level percentage split of labour, fuel, consumables and logistics was found for Canadian exploration. Next step: a SMAD assessment report with an itemised drilling invoice (Terranox has SMAD access).
- Zinex, Kluane and Discovery Drilling specifications and claims are unverified.
- Sonic drilling in the Athabasca, RC radiation handling, and the details of probe-versus-assay disequilibrium practice rest on memory.
- No Earth AI metres-drilled-to-date figure or third-party audit of its cost per metre was found.
