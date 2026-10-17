# Hunt 9, Sweep D: physical assets whose hidden condition is revealed by an expensive test

Agent D. Scope: machines, vehicles, infrastructure, buildings, worldwide. Method: ~30 WebSearch calls (the shared
per-turn search budget ran out at that point; the last three planned searches on muni water FMV deals, EV-battery
SOH test cost and office $/sf were not run) plus ~35 WebFetch reads of the result pages. Numbers marked
"(my estimate)" are inferred; everything else has a URL.

## Headline finding (read this first)

The cluster is structurally weak for the drill test, and the reason is general, not candidate-specific:

1. For MACHINES (aircraft, engines, ships, turbines, transformers, fab tools, locomotives) the hidden condition
   lives in the owner's own maintenance records, which are private. The owner is therefore the informed party and
   sells by tender, broker or auction. Public datasets (FAA ADs/SDRs, Paris MOU, EIA-860, NID, NBI) are structured
   lookup tables, not illegible archives, and regulators have already written the status into a legible field
   (Paris MOU "Ship Risk Profile", EIA-860 status code, NID condition rating, LA's soft-story list).
2. For BUILDINGS the regulator publishes the list (soft-story, URM, cladding, milestone inspections), so the market
   prices the hazard the day the list is published; retrofit arbitrage step-ups are 1.2-1.5x, not 10x.
3. The only two places in the cluster where the signal is genuinely illegible AND the seller is genuinely
   unsophisticated are (a) small non-powered dams owned by towns and individuals (FERC eLibrary and state
   dam-safety PDFs) and (b) individual condo units in ageing Florida buildings (scanned milestone-inspection
   reports filed with county building departments). Neither scores above 4/10 because the step-up is modest or
   the right is first-come.

Best three, all provisional 4/10: non-powered-dam licensing options; Florida ageing-condo assembly; retired
jet-engine cores converted to data-centre turbines. Nothing here beats the rail-corridor or Lineage candidates
from earlier hunts.

## Candidates (four-part test each; scores 0-10)

### 1. Non-powered dam (NPD) hydro licensing options. NEW. Score 4.
- PROVING STEP: FERC licence (plus Army Corps Section 408 design review for Corps dams, 12-18 months of 30/60/90%
  submittals) and feasibility/environmental studies. Cost $1-5M per site (my estimate; FERC fees + studies), time
  5-11 years (Rye Development's Emsworth: "initial approval" 2016, power "by late 2027",
  https://www.asce.org/publications-and-news/civil-engineering-source/civil-engineering-magazine/article/2023/08/pittsburgh-dams-to-be-converted-to-low-impact-hydropower).
  Hit rate: 58 NPDs licensed for 888 MW in total (https://www.osti.gov/biblio/1470870); 42 retrofits built
  2000-2021 (588 MW) out of ~3,300 NPDs with >100 kW potential (ORNL, https://info.ornl.gov/sites/publications/Files/Pub177385.pdf).
  Permit-to-licence conversion is not published; 10-20% (my estimate) so lever cap 5-10. Paid today by developers
  (Rye, Emrgy, Natel, Hydro Green).
- SIGNAL: USGS gauges and NID head/storage are legible. The illegible part: (a) 40 years of abandoned permits and
  licence applications on FERC eLibrary (scanned PDFs, millions of documents) saying why each dam's previous
  attempt died (fish passage, flowage, 401 certification); (b) state dam-safety inspection reports, scanned and
  mostly offline. ORNL flags that NID storage/head fields "may not reflect actual operations" and are unvalidated,
  so the lookup field is wrong often enough to leave an edge. 89,000 NPDs; 12.1 GW technical, 3.6 GW economic
  potential by 2030 (same ORNL source).
- UNPROVEN RIGHT: two pieces. The FERC preliminary permit is free, 3-4 year exclusive, first-come (the brief's
  kill rule), though transferable with FERC consent. The dam itself: 63% of NPDs are private, ~33% of the >100 kW
  set are local-government owned (ORNL); these owners cannot read eLibrary and often regard the dam as a
  liability, so an option on the dam costs near zero (my estimate). FPA s.21 gives licensees eminent domain, so
  owning the dam is not a hard moat.
- PROVEN STATE: a licensed, unbuilt project. CapEx median $13,794/kW (range $1,840-52,852; ORNL), so only the
  low-cost tail is buildable. Buyers of operating small hydro: Eagle Creek and Cube Hydro (both Ontario Power
  Generation), Brookfield, Central Rivers, Gravity Renewables. Buyers of licensed-unbuilt NPD projects: unknown;
  no named transaction found (fetch of the NREL licensing study was blocked by robots.txt). Offtakers pay for
  the option indirectly (Iron Mountain contracted up to 150 MW from Rye's pipeline; Allegheny County 35-year PPA).
  R1: large in ratio (near-zero option to a licensed asset worth $0.3-1M/MW pre-build, my estimate), small in
  dollars per site ($3-10M).
- CEILING: 3.6 GW economic x $5-14k/kW = $18-50B built; the licensed-option pool is $1-3B (my estimate).
  Borderline "niche".
- INCUMBENTS: Rye Development (dozens of preliminary permits, e.g. three new WV filings,
  https://www.nacleanenergy.com/energy-storage/rye-development-grows-non-powered-dam-portfolio-filing-preliminary-permits-for-three-new-projects-in-west-virginia),
  Emrgy, Natel, Hydro Green; ORNL/INL publish NPD screening tools (https://npd-hydro.inl.gov/about), which pushes
  the legible part of the signal toward zero edge.
- KILL TEST (days): list every NPD preliminary permit issued 2008-2018 on eLibrary, count how many became licences
  and how many licences were sold before construction. If conversion >30% or zero pre-build sales, kill.
- DOUBT: the exclusive right is first-come, and the legible fields (head, flow) carry most of the predictive
  power.

### 2. Florida ageing-condo assembly through scanned milestone-inspection reports. NEW. Score 4.
- PROVING STEP: the SB 4-D milestone inspection (Phase 2 structural, $50-200k per building, my estimate) and the
  Structural Integrity Reserve Study. "Success" here is inverted: the play pays when the building FAILS and the
  cheapest exit is termination and land sale. Hit rate (fraction of 30-year-plus buildings that end in
  termination): unknown, low single digits per year (my estimate).
- SIGNAL: milestone reports and SIRS are filed with county/municipal building departments as scanned PDFs, plus
  decades of permit histories and 40-year recertification files; illegible at scale, legible per building.
  Market evidence that the market does NOT yet read them: 30-year-plus South Florida condos fell 21% since 2023
  (average $325k in 2022 to $218k) while sub-10-year condos rose 9%; 85% of listings are 30-year-plus buildings;
  72% of Miami condo listings went unsold in Sept 2023-Feb 2024; assessments up to $175k
  (https://www.bisnow.com/news/south-florida/multifamily/condo-report-isg-world-aging-condo-crisis-126503).
- UNPROVEN RIGHT: individual units, bought bilaterally from owners who cannot pay assessments; they cannot read
  the engineering file. Purchasable, exclusive per unit. Termination needs 80% of voting interests and fails if
  5%+ object (s.718.117; https://strangtryson.com/the-growing-trend-of-condo-terminations-in-south-florida-what-owners-need-to-know/);
  the Biscayne 21 appellate ruling let 10 owners block one.
- PROVEN STATE: developer buys the whole building for land. Named: Continuum offered $141M for 140 units
  (~$1.0M/unit) at Four Winds, Surfside, after Naftali's $100M (2022) and $115M (2023) and its own $125M
  (https://commercialobserver.com/?p=482253). R1 versus distressed unit prices of $218k average: 2-4x on
  waterfront, ~1.5x inland (my estimate). Trades before build (the developer buys units, not a finished tower).
- CEILING: South Florida alone has hundreds of thousands of 30-year-plus units; at $200-300k each the pool is
  tens of billions. Also NJ, NY and other coastal states adopting post-Surfside rules.
- INCUMBENTS: Continuum, Naftali, Related, 13th Floor, Two Roads; condo-termination lawyers (Siegfried Rivera,
  Duane Morris). They assemble by broker and letter, not by reading inspection archives.
- KILL TEST: for 50 Miami-Dade/Broward buildings, pull the filed milestone report dates and outcomes and plot unit
  price change in the 6 months before versus after filing. If prices move before the filing (the market already
  knows), kill. Also count completed terminations 2022-2026: if fewer than 20, the exit is too thin.
- DOUBT: this is assembly risk, not condition risk; the 5% blocking rule and litigation make the hit rate
  unknowable from public data.

### 3. Retired jet-engine cores (CF6-80C2) converted to data-centre gas turbines. NEW. Score 4.
- PROVING STEP: full overhaul and conversion of a run-out core to a 48 MW aeroderivative package (ProEnergy
  PE6000; https://eepower.com/news/can-repurposed-jet-engines-solve-ai-data-center-power-problems/). Cost per
  conversion unknown; $8-15M (my estimate). Hit rate: unknown; a core whose HPT disks are life-expired is scrap.
  Who pays: ProEnergy (75 packages built, 52 more in build/order; 21 units >1 GW sold to two data-centre projects).
- SIGNAL: none public. Engine records (LLP cycles, shop-visit history) are private. FAA ADs are a legible
  lookup. "About 1,000 engines could retire over the next 10 years" (eepower). Fails part 2.
- UNPROVEN RIGHT: run-out CF6 cores from 747/767/MD-11 part-outs. Sellers are part-out firms and lessors
  (AerSale, GA Telesis, VAS Aero), fully informed, selling by tender. A CFM56 was ~$7M in 2019 and expected to
  fall to $2-3M (GA Telesis CEO, https://aviationweek.com/air-transport/retirement-uptick-will-restock-used-engine-parts);
  engines are 80-90% of an aircraft's part-out value (https://www.aersale.com/media-center/plane-profit-from-passengers-to-part-out).
- PROVEN STATE: a 48 MW package deliverable in 2027 versus 3-7-year OEM lead times and new-turbine prices heading
  to $600/kW by 2027, 195% above 2019 (https://www.publicpower.org/periodical/article/gas-turbine-market-will-see-prices-surge-through-2027-report).
  Package value $25-45M (my estimate, $500-900/kW). R1 on the core 10-30x, but most of it is conversion capex.
  Buyers: hyperscale/colo developers, named in the article as two projects.
- CEILING: ~1,000 cores x 48 MW = 48 GW theoretical; at $700/kW, $30B+.
- INCUMBENTS: ProEnergy (occupies it), Siemens Energy, GE Vernova LM6000 (same core).
- KILL TEST: ask two part-out brokers for a run-out CF6-80C2 core quote and check whether any public record
  predicts core condition. There is none; the candidate fails on signal and becomes "be ProEnergy".
- DOUBT: no public signal; seller fully informed.

### 4. Remanufactured large power transformers (the Maddox model). NEW. Score 3.
- PROVING STEP: condition testing, disassembly, rewind if needed, retest to IEEE/ANSI. Cost unknown; a rewind
  of a 50 MVA unit $0.3-1M (my estimate). Hit rate unknown. Paid by remanufacturers.
- SIGNAL: none public. Utility retirements are not in a public file (FERC Form 1 retirements are aggregate
  dollars; rate cases are scanned but do not list serials). DGA/furan histories are private.
- UNPROVEN RIGHT: retired units bought bilaterally "from utilities, demolition contractors and recyclers" at
  "up to five times scrap value" (Maddox, sponsored, https://www.powermag.com/partner-content/beating-the-transformer-bottleneck-remanufacturing-build-to-stock-and-smart-procurement/).
  Purchasable, not auction; sellers (demolition contractors) often cannot read the unit's history.
- PROVEN STATE: reman unit shipped in 1-4 weeks versus 128-week LPT and 144-week GSU lead times (Wood Mackenzie
  via same source), priced 10-40% below new. Scrap of a 50 MVA LPT $150-300k, reman price $1.5-3M (my
  estimates): R1 5-10x. Liquid: utilities, data centres, industrials.
- CEILING: 55% of US distribution transformers are over 33 years old (NLR via same source); LPT fleet tens of
  billions.
- INCUMBENTS: Maddox Industrial Transformer (five shops), Northern Transformer, Pioneer, used-equipment brokers.
- KILL TEST: find any public dataset listing utility transformer retirements by unit. None found; without it
  this is a sourcing-network business, not a reading business.
- DOUBT: no illegible public signal; Maddox is already this company.

### 5. Idle and mothballed gas turbines (EIA-860 status SB/OS). Score 2.
- PROVING STEP: hot-gas-path/borescope inspection and, for 7FA units now ~25 years old, the OEM rotor life
  limit: rotor wheels have 2-3-year lead times and some 7EAs have had two life extensions
  (https://www.powermag.com/the-clock-is-ticking-on-7fa-gas-turbine-rotors/). Cost $1-5M per inspection/
  extension (my estimate). Hit rate unknown.
- SIGNAL: EIA-860 lists every unit with a legible status code (https://www.eia.gov/electricity/data/eia860/):
  the regulator has written the answer in a field. Operating records are private.
- UNPROVEN RIGHT: owner is a utility or IPP and sells by tender or broker (Phoenix Equipment lists an 81 MW 7EA,
  https://phxequip.com/plant/2435/81mw-general-electric-7ea-gas-turbine-generator-set). Fails the brief's
  tender rule.
- PROVEN STATE: lead times "past 2029" (https://www.credaily.com/briefs/gas-turbine-shortage-threatens-data-center-power-plans/),
  $600/kW new; a tested used frame unit is worth 2-3x its 2022 price (my estimate). Buyers: data-centre developers.
- CEILING: tens of GW idle; $10B+. INCUMBENTS: Phoenix Equipment, Suncoast, MDA (rotor life extensions), PowerGen.
- KILL: count SB/OS gas turbines in EIA-860 >20 MW and check how they were sold 2023-2025; all by tender = dead.
- DOUBT: owner informed, sells by tender, status legible.

### 6. Vintage bulk-carrier special-survey arbitrage (ships). Score 2.
- PROVING STEP: 4th/5th special survey in drydock with steel renewal; $1-4M (my estimate; a 12-year retrofit
  model bundles "15-year survey/steel/machinery" at $1.3M, https://www.shipuniverse.com/?p=19636).
- SIGNAL: PSC inspection and detention records are public (Paris MOU website; researchers collected 1,880
  detention records by hand, https://researchonline.ljmu.ac.uk/id/eprint/16959/), and the regulator publishes a
  per-ship Ship Risk Profile: the answer is in a legible field. Class survey status is on Equasis. AIS is public.
- UNPROVEN RIGHT: 20-23-year-old Panamaxes sold bilaterally via S&P brokers at $6-11M (Alpha Melody ~$6-7M;
  2004-built $8.5M and $11M; 2005-built $8.1M; https://www.rivieramm.com/news-content-hub/vintage-bulk-carriers-attract-buyers-as-two-tier-market-strengthens-83526).
  Sellers (Greek owners) are the best-informed party.
- PROVEN STATE: a 20-year-old Supramax trades only ~$3.8M above scrap (mid-$400/LDT in Bangladesh;
  https://www.breakwaveadvisors.com/insights/2025/1/29/demolition-activity). R1 about 1.3-1.5x. 9% of the bulk
  fleet is over 20 years.
- KILL: compare secondhand-minus-scrap spread to survey cost; it is already roughly equal, so no step-up.
- DOUBT: step-up ~1.4x, risk profile legible, seller informed. Dead.

### 7. Retired narrowbody part-out and engine green time (aircraft). Score 3.
- PROVING STEP: teardown plus 145-shop inspection to serviceable tag; teardown $0.3-0.5M per aircraft and 3-9
  months to sell high-value parts (Vallair via https://www.ajw-group.com/storage/downloads/1692876992_tony_aug_2023.pdf).
  Hit rate: unknown; for engines, value depends on LLP cycles remaining, which is known exactly from records.
- SIGNAL: FAA ADs, SDRs and the NTSB database are structured. Maintenance records are private and travel with
  the aircraft. Not illegible; not public.
- UNPROVEN RIGHT: ~500-700 retirements/year (Oliver Wyman via Aviation Week), sold by airlines/lessors by
  tender. AerSale bought 100+ aircraft since 2010. Engines 80-90% of value; a CFM56 ~$7M (2019).
- PROVEN STATE: serviceable-tagged USM; buyers are airlines and MROs. R1 on a whole aircraft 1.3-2x (my
  estimate), well known to incumbents.
- INCUMBENTS: AerSale, VAS Aero, GA Telesis, EirTrade, Vallair, Aventure, Air Salvage, APOC.
- DOUBT: an efficient market of informed sellers; no public illegible signal.

### 8. Dormant general-aviation aircraft via the FAA aircraft file. NEW. Score 2.
- PROVING STEP: annual inspection/AD catch-up/pre-buy, $5-30k (my estimate); hit rate >50%; lever cap <2.
- SIGNAL: the FAA aircraft file (registration + airworthiness, including major repair/alteration Form 337s that
  document damage history) is public on request at $10 per aircraft on CD, average 76 pages, one aircraft per
  order (https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/copies_aircraft_records;
  https://shackelford.law/news-aviation/obtaining-aircraft-records-from-the-faa/). Genuinely illegible at scale
  (no bulk download), and "Form 337 is often the most accepted document to confirm damage history"
  (https://duncanaviation.aero/intelligence/what-is-aircraft-damage-history-and-how-does-it-affect-aircraft-value).
  Damage-history discount is not quantified in sources; 5-20% (my estimate).
- UNPROVEN RIGHT: ~200,000 US GA aircraft owned by individuals, bought bilaterally; many owners of dormant
  aircraft do not know their file.
- PROVEN STATE: airworthy, clean-file aircraft, 1.2-2x (my estimate). Pool $30-40B (my estimate).
- INCUMBENTS: dealers, Aircraft Bluebook/Vref appraisers; none read files at scale.
- DOUBT: step-up and lever cap both too small; the illegibility is real but low-value.

### 9. UK cladding-discounted flats. NEW. Score 3.
- PROVING STEP: remediation, paid by developers or the government, not the buyer: 4,469 buildings 11m+ monitored,
  47% not started, ~239,000 dwellings (102,000 in not-started buildings); total cost £11.8-22.7bn with £9.2bn
  government funding (https://www.gov.uk/government/publications/building-safety-remediation-monthly-data-release-june-2026/building-safety-remediation-monthly-data-release-june-2026).
  Hit rate near 1; lever cap ~1.
- SIGNAL: building-level programme status is published monthly (legible). The illegible bit is timing: planning
  applications and FRAEWs on council portals.
- UNPROVEN RIGHT: flats bought bilaterally at 20-25% below market (Paragon,
  https://www.mortgagesolutions.co.uk/news/2024/05/03/btl2024-cash-buyer-landlords-are-mopping-up-cladding-affected-homes/);
  some cash-buyer offers 10-15% below (Which?, Open Property Group).
- PROVEN STATE: remediated flat at full value, R1 1.3x; mortgageable, liquid.
- CEILING: 100k+ affected flats, £20-30bn. INCUMBENTS: cash BTL landlords, Open Property Group.
- DOUBT: a free option with a 1.3x payoff; no ML needed; not a drill structure.

### 10. Soft-story and URM seismic retrofit arbitrage (California). Score 2.
- PROVING STEP: engineering assessment ($5-20k) then retrofit $20k-$350k per building (avg ~$11k/unit;
  brokerage source https://www.lametrohomefinder.com/blog/soft-story-retrofit-sell-los-angeles). Assessment
  rarely "fails"; lever cap ~1.
- SIGNAL: LA's list of ~13,500 buildings is public and legible (https://justintye.com/blog/why-your-los-angeles-apartment-building-is-worth-less-than-it-was-in-january-2026).
- UNPROVEN RIGHT: as-is buildings at 15-30% below compliant value (brokerage claim: retrofit cost plus a 10-20%
  risk premium). Owners were notified by the city; they know.
- PROVEN STATE: compliant building, R1 1.2-1.4x; half the cost is recoverable through rent surcharges over 10-15
  years. CEILING: LA+SF+Oakland+Berkeley ~25,000 buildings, $20-30B.
- DOUBT: no hidden state, no step-up. Dead.

### 11. Office-to-residential convertibility. NEW (borderline for this cluster). Score 3.
- PROVING STEP: feasibility scorecard; Gensler assessed 1,000+ buildings and "only 25 percent" pass
  (https://urbanland.uli.org/public/what-weve-learned-by-assessing-more-than-1000-potential-office-to-residential-conversions);
  lever cap 4 but the test costs tens of thousands against a $10-100M asset, so every owner can run it.
- SIGNAL: floor-plate depth, window-to-core and floor-to-floor are derivable from assessor polygons, LiDAR and
  scanned municipal structural drawings. Partly illegible, but Gensler sells the scorecard to cities and owners.
- UNPROVEN RIGHT: distressed office, bought bilaterally or from lenders; sellers are sophisticated.
- PROVEN STATE: entitled conversion; conversion costs ~30% less than new build. R1 on entitlement 1.5-3x (my
  estimate). INCUMBENTS: Metro Loft, Vanbarton, GFP, Silverstein. DOUBT: other sweeps own real estate; the
  signal is semi-legible.

### 12. Abandoned pipelines as fibre or cable conduit. NEW. Score 2.
- PROVING STEP: integrity/ILI run and easement/title check; $0.5-2M (my estimate). Hit rate unknown.
- SIGNAL: PHMSA abandonment filings; UK AssetHUB has mapped ~20,000 km of abandoned gas and ~20,000 km of
  water pipe but no altnet confirmed using any (https://www.theregister.com/2025/03/03/altnet_abandoned_pipes/).
  Williams pioneered fibre-in-pipeline in 1985 and built a 25,000-mile network (https://www.ogj.com/general-interest/companies/article/17215524/cyber-pipelines).
- UNPROVEN RIGHT: owned by pipeline/utility companies, sophisticated sellers; abandoned-in-place easements may
  have reverted. Overlaps the already-seen rail-corridor-title candidate.
- DOUBT: owner informed; the valuable piece is the easement, not the pipe.

### 13. Used semiconductor tools from fab closures. Score 2.
- PROVING STEP: refurbishment and re-qualification; refurbished tools sell "up to 65% less than new"
  (ClassOne, https://sst.semiconductor-digest.com/mysemicondaily/?p=12089817), SurplusGlobal claims "cost saving
  up to 30%", buys >$100M/yr, trades 1,500 tools/yr, holds 1,000 (https://www.surplusglobal.com/resources/SG/file/Company_Profile.pdf).
- UNPROVEN RIGHT: sold by auction, tender or trade-in by fabs that know every tool's log. Fails the tender rule.
- INCUMBENTS: SurplusGlobal, Moov, ClassOne, Liquidity Services, Hilco. DOUBT: auction market, informed sellers.

### 14. Second-life EV and grid batteries. Score 1.
- PROVING STEP: SOH test, now "minutes rather than hours" and cheap; not an expensive failing step. Market only
  $4.2B by 2035 (IDTechEx, https://www.idtechex.com/zh/research-report/second-life-ev-batteries-2025/1056).
- SIGNAL: per-VIN SOH is in OEM/fleet telematics, not public; NHTSA recalls are legible. Fails on every part.

### 15. Retired Class I locomotives for short lines. Score 1.
- "Prices for used locomotives are ridiculously cheap at times" when Class Is sell stored power; buyers G&W,
  Watco, R.J. Corman (https://www.trains.com/trn/railroads/locomotives/short-lines-and-regional-railroads-are-consistently-upgrading-locomotives).
  Sellers hold the records; sold in blocks by the Class I. Dead.

### Footnotes (excluded or out of cluster)
- Abandoned mines as pumped-storage or storage voids: proving needs drilling; excluded.
- InSAR (Copernicus EGMS, free, mm precision, 60M points in NL alone; Sensar sells subsidence maps,
  https://land.copernicus.eu/en/use-cases/using-egms-to-assess-infrastructure-risk-in-the-netherlands/using-egms-to-assess-infrastructure-risk-in-the-netherlands)
  as a public signal of building/dam movement: the proving step is a geotechnical borehole, drilling-adjacent;
  excluded. The data is a genuinely illegible public signal and a different sweep could use it for levee/dam or
  insurance plays.
- Powered waterfront land, telecom central offices, shipyards: same structure as powered brownfields (seen,
  fails, 1.1x); AT&T's CO sell-off is by tender.
- Small-hydro FERC relicensing arbitrage: a regulatory, not physical, proving step; hit rate near 1; numbers
  not gathered (NREL fetch blocked).
- Small municipal water systems (fair-market-value acquisitions): regulated rate-base roll-up, not a test; not
  researched (search budget exhausted).

## Ranking
1. NPD hydro licensing options, 4/10 (right is first-come; hidden state mostly legible).
2. Florida ageing-condo assembly, 4/10 (assembly risk, 80%/5% rule, step-up 1.5-3x).
3. CF6 cores to data-centre turbines, 4/10 (no public signal; ProEnergy occupies).
4. Reman transformers 3; 5. part-out 3; 6. cladding 3; 7. office conversion 3; the rest 1-2.
