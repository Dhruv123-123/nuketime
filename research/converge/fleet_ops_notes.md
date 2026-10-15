# R5 — Operating fleet software/hardware niches (research log, started 2026-10-03)

## Competitors (raw)
- Nuclearn: $10.5M Series A, Sep 9 2025, led Blue Bear Capital (+AZ-VC, Nucleation, SJF). Deployed at 65+ reactors globally. Founders ex-Palo Verde. Doc automation, "junior employee". https://techcrunch.com/2025/09/09/nuclearn-gets-10-5m-to-help-the-nuclear-industry-embrace-ai/
- Atomic Canyon: $7M seed May 28 2025, led EIP. Diablo Canyon customer (late 2024). RAG search "Neutron"; 20k GPU hrs ORNL. https://techcrunch.com/2025/05/28/atomic-canyon-wants-to-be-chatgpt-for-the-nuclear-industry
## A. SFCP
- EPM Inc. sells SFCP support (IDP support, data collection, STRIDES tool). No counts/costs on page. https://www.epm-inc.com/nuclear/surveillance-frequency-control-program-support/
- TSTF-425 Rev3 NOA: Federal Register July 6 2009 https://www.federalregister.gov/documents/2009/07/06/E9-15780/
- TSTF-596 Rev2 (Oct 2024): "TSTF-425 has been incorporated into the TS of all plants except Vogtle Units 3 and 4"; >75% adopted TSTF-545; ~2/3 of sites approved for 50.69. https://www.nrc.gov/docs/ML2428/ML24282B020.pdf
- PSAM14 paper (2018): Callaway (SFCP approved Jul 2011) had implemented only 2 STI changes by Dec 2017 (batteries 2014, TADOT 2016). NextEra ~100 STRIDEs. Process = data collection -> PRA (RG1.174/1.177) -> IDP -> performance monitoring. https://iapsam.org/psam14/proceedings/paper/paper_37_1.pdf
- INL LWRS report (June 2019): 68 STRIDEs across STARS plants saved >12,110 person-hours/yr (~178 h/yr per STRIDE), ~$605k/yr (~$8.9k/STRIDE) + ~$378k/yr replacement power. Sizewell B online monitoring of transmitter cal: -75% outage calibrations, -5 outage days, ~$5M/cycle. Oconee digital RPS: -2,296 work hours. https://lwrs.inl.gov/content/uploads/11/2024/03/Technical_Specification_Surveillance_Interval_Extension_of_Digital_Equipment_NPP_Review_Research.pdf
- NEI (Mar 2023, ML23045A289): TSTF-425 SBO test extension cut outage up to 24h; 50.69 -> 230 eng h/yr; TSTF-505 RICT 42h/36h outage reductions. https://www.nrc.gov/docs/ML2304/ML23045A289.pdf
- TAKE: SFCP is universal (not the bottleneck); per-change value small (~$9k/yr labour); value concentrates where an extension removes outage critical-path work (online monitoring -> calibration extension). Incumbents: EPM (STRIDES), Jensen Hughes, utility PRA groups. Wedge is thin as standalone.

## B. Outages
- Constellation: 2025 avg refuel outage 21.5 days, "~16 days better than industry average" (=> industry ~37 days); CF 94.7%. https://www.constellationenergy.com/work/generation/nuclear/reliability.html (accessed 2026-10-03)
- ANS/INL (Sep 26 2025): outages 3-4 weeks, "more than $1 million a day", tens of thousands of activities. https://www.ans.org/news/article-7402/
- INL LWRS RISA 2023 (INL/RPT-23-74439): ~30 days avg; delays cost "several million dollars per day"; emergent issues primary disruptor; INL building ML schedule-resilience tools. https://www.osti.gov/biblio/1999587
- OPG AI outage scheduling (Power Eng, 2019/2024): 20-25k tasks/outage, 8 yrs history, engineers spend up to 40% of time on repetitive admin. https://www.power-eng.com/nuclear/improving-nuclear-unit-outage-scheduling-with-artificial-intelligence/
- Back-of-envelope: ~94 reactors, ~60 refuel outages/yr (18-24mo cycles). Gap between best (21.5d) and avg (~37d) ~ 15 days x ~$1M+/day = $15M+ per laggard outage.
- Existing tools: Oracle Primavera P6 (schedule), Primavera Risk/Safran/Acumen for risk, utilities' in-house; Knowledge Relay (blogging AI for outages), nPlan (AI schedule forecasting in construction).

## C. Uprates/restarts
- NRC expected uprate applications page (updated Sep 8 2026): 32 applications 2026-2032, 7,336 MWt total. Incl. Constellation EPU 1,014 MWt Q4 2026; Brunswick MU, Wolf Creek MU, McGuire EPU, Salem SPU, Hatch EPU (Q1-Q2 2027); Columbia EPU 1,923 MWt Q2 2028; Catawba 1, Vogtle 1&2 EPU 2028; Perry EPU 598 MWt 2029; Beaver Valley 2030-31; Davis-Besse 2032. https://www.nrc.gov/reactors/operating/licensing/power-uprates/status-power-apps/expected-applications
- DOE UPRISE (Mar 13 2026), INL-managed: 2.5 GW by 2027, 5 GW by 2029; LPO/EDF up to 80% financing. https://www.ans.org/news/article-7841/doe-launches-uprise-to-boost-nuclear-capacity/
- POWER (Mar 2026): bottlenecks = engineering bandwidth & scheduling at utilities, long-lead equipment, staffing, investment decisions, NRC capacity. NRC targets: EPU 12 mo, SPU 9 mo, MUR 6 mo. Restarts: Palisades $1.52B/800MW; Crane $1.6B/835MW. https://www.powermag.com/doe-unveils-initiative-to-add-5-gw-of-nuclear-capacity-through-uprates-and-restarts/
- Who does uprate engineering: NSSS vendors (Westinghouse, Framatome, GE Vernova/GNF), A/Es (Sargent & Lundy, Enercon, Jensen Hughes, Zachry), utility engineering.

## Competitors (cont.)
- Atomic Canyon NIVA (Aug 18 2026): with EPRI, INPO, NEI; moved from 6-month pilot at Constellation (26 reactors) to fleetwide availability for North American INPO/EPRI/NEI members. Knowledge assistant + OE assistant; troubleshooting assistant pilot later 2026. New investors NVIDIA, Mortimer Buckley (undisclosed). https://neutronbytes.com/2026/08/20/atomic-canyon-launches-ai-virtual-assistant-for-nuclear-reactor-operations/ ; https://igrownews.com/atomic-canyon-latest-news/
  => knowledge search / OE / generic chat is CLOSED as a wedge.
- Everstar: $4M pre-seed Feb 2025, "Gordian" AI compliance/licensing platform (Kevin Kong). https://www.finsmes.com/2025/02/everstar-raises-4m-in-pre-seed-funding.html
- Westinghouse + Google Cloud (Jul 15 2025): HiVE, bertha, WNEXUS on Vertex/Gemini; mainly AP1000 construction work packages + "existing fleet optimization". https://info.westinghousenuclear.com/news/westinghouse-to-accelerate-us-nuclear-reactor-construction-and-enhance-operations-with-google-cloud-ai
- Palantir + The Nuclear Company (Jun 26 2025): "Nuclear Operating System" focused on construction. https://www.businesswire.com/news/home/20250626371726/en/
- CB Insights map "nuclear operations software & AI": Mirion, Bentley, IBM (Maximo), Atomic Canyon, Framatome, Kinectrics, L3Harris (simulators), Nuclearn (CR coding, CAP screening), Palantir, Studsvik, TNC, Westinghouse. https://www.cbinsights.com/esp/enterprise-tech/enterprise-applications/nuclear-operations-software-%26-ai
- Nuclearn site (accessed 2026-10-03): products Equipment AI, Parts AI, PI AI, Engineering AI, AtomAssist, Capitalizer, Project Genius, CAP AI; "over 70 facilities in North America and UK"; covers CAP screening (~40 CRs/day x 15 min, ~50% automated), work package & procedure mgmt. https://nuclearn.ai/  => CAP + work packages heavily contested.
- Blue Wave AI Labs: DOE $6M (Mar 26 2024) with Constellation, BWR core sensor (LPRM/TIP) calibration ML, fuel cycle optimisation; target all 32 BWRs; est ~$80M saving over 3 yrs. https://www.energy.gov/ne/articles/new-ai-tools-could-save-constellation-reactor-fleet-millions ; total funding ~$6.9M https://www.energystartups.org/startup/bluewaveailabs/

## A2. Condition-based calibration (OLM)
- NRC-approved AMS-TR-0720R2-A "Online Monitoring Technology to Extend Calibration Intervals of Nuclear Plant Pressure Transmitters" (topical, ML20231A199). https://www.nrc.gov/docs/ML2023/ML20231A199.pdf
- PG&E Diablo Canyon LAR DCL-24-118 (Dec 2024): switch RTS/ESFAS/PAM/etc pressure/level/flow transmitters from time-based to condition-based calibration via OLM; approval requested by Sep 30 2025. https://www.nrc.gov/docs/ML2436/ML24366A169.pdf
- Entergy presubmittal meeting on similar LAR (2023). https://www.nrc.gov/public-involve/public-meetings/pmns/20231406
- Incumbent: AMS Corp (Knoxville) owns the approved methodology; EPRI OLM guidance. Opening exists for software that does fleet-scale OLM + drift detection for more instrument classes (RTDs, valves, pumps) feeding SFCP/LARs.
## Sales cycle data
- Diablo/Atomic Canyon: talks spring 2024 -> FERMI test Sep 2024 -> announced Nov 2024 -> on-prem NVIDIA hw end-2024 -> internal docs Q3 2025 (~12-18 mo to production). PG&E est. ~15,000 h/yr search time saved. Contract value undisclosed. https://calmatters.org/economy/technology/2025/04/first-nuclear-plant-ai-at-diablo-canyon/

## Market sizing
- NEI Nuclear Costs in Context (Aug 2026): 2025 avg total generating cost $36.46/MWh = fuel $5.95 + capital $9.69 + operating $20.82. Capital spend +23.9% y/y. CF 92%. 73,000 jobs. https://www.nei.org/getContentAsset/47fa8caa-9b0d-4029-932c-07f902e82f4f/8d8ff8d6-b2ae-401b-a63c-f6b108e809d2/2024-Costs-in-Context-final.pdf
- => ~780 TWh/yr x $20.82 = ~$16B/yr US fleet operating cost; capital ~$7.5B/yr (rising: uprates, LTO, digital).
- INL ION cross-pathway (Sep 2023, INL/RPT-23-74595): work reduction in maintenance (CBM), engineering (licensing), operations (fewer manual surveillances), security. Savings plant-specific. https://lwrs.inl.gov/content/uploads/11/2024/03/ION_CrossPathway.pdf

## D. Other fleet problems
- Digital I&C: NRC approved Limerick digital safety I&C retrofit Jan 5 2026 ($167M; first multi-system digital safety retrofit at operating US plant; DOE $50M cost share). https://www.ans.org/news/2026-01-08/article-7658/nrc-oks-ic-upgrade-for-limerick/ ; https://www.power-eng.com/nuclear/constellation-gets-nrc-approval-for-167m-upgrade-at-limerick-nuclear-site/
- Inspection relief requests justified by history: e.g., Constellation Ginna relief I6R-11 (Mar 25 2025) - visual only for 55th-yr containment tendon surveillance, citing precedents Wolf Creek, Palo Verde, Millstone, Vogtle, TMI, Braidwood, Byron. https://www.nrc.gov/docs/ML2508/ML25086A205.pdf  (pattern: data-justified reductions are repetitive document work)
- Hiring (EnergyMonitor, Jun 19 2026): N.A. nuclear active postings 14,016 May 2026 (-12% y/y), peak 15,167 Mar 2026; operators Vistra +74%, Exelon +40%; 97% entry/mid level. https://www.energymonitor.ai/sponsored/nuclear-energy-hiring-is-slowing-in-north-america-but-leaders-can-see-where-capacity-and-risk-are-shifting/
- Roll Call (Nov 5 2025): DOE EWAB says workforce must triple to quadruple capacity. https://rollcall.com/2025/11/05/worker-shortage-looms-over-new-us-nuclear-power-focus/
- YC energy list: nuclear cos = Oklo, Atomarine (S26), Terranox AI (W26, exploration - excluded), Maritime Fusion, Helion. No YC fleet-ops software co. https://www.ycombinator.com/companies/industry/energy

## Europe
- Cour des comptes (Nov 17 2025): EDF annual maintenance spend >EUR 6bn (+28% vs 2006-14); availability 74% in 2014-24 vs 80% prior decade; Grand Carenage EUR 100.8bn 2014-2035 (131.9bn incl opex); LTO to 60y ~EUR51/MWh. https://www.connaissancedesenergies.org/afp/prolonger-jusqua-60-ans-le-parc-nucleaire-francais-inevitable-et-avantageux-selon-la-cour-des-comptes-251117
- EDF 2025 results (Feb 20 2026): 373 TWh; START 2025 programme -> 23 of 43 outages ended ahead of schedule; maintenance investment EUR5.9bn. https://www.edf.fr/sites/groupe/files/2026-02/annual-results-edf-2025-presentation-2026-02-20.pdf
## Uprate process
- NEI 08-10 (Jul 2009): uprate total ~3-4 yrs; analysis phase 12-36 mo; NRC review 6-12 mo; implementation 18-42 mo. Analyses: fuel/core, NSSS, BOP, Ch.15 transients, containment, radiological, FIV, PRA, grid. LAR scope rivalled only by license renewal / ITS conversion. https://www.nrc.gov/docs/ml0925/ml092540581.pdf
- Nuclearn Project Genius (accessed 2026-10-03): ML + Monte Carlo on historical P6 outage data to forecast completion; schedule risk; resource planning; case: US plant found an activity on critical path 90% of time using 10 yrs data. https://nuclearn.ai/our-product/project-genius/  => OUTAGE SCHEDULE RISK IS CONTESTED by Nuclearn.
- Nuclearn Feb 2026: Certified Service Provider program (Raisun), NPX collaboration, Park Nuclear partnership on Parts AI. https://nuclearn.ai/2026/02/
- EDF stress-corrosion 2022: earnings hit raised to EUR18.5bn (WNN May 19 2022). https://www.world-nuclear-news.org/Articles/EDF-revises-up-cost-of-nuclear-plant-outages
- AMS OLM NRC approval Sep 22 2021: "hundreds of pressure, level, flow transmitters" calibrated ~every 2 yrs; up to 90% fewer calibrations; up to $5M/plant/18 mo (Sizewell B basis). https://www.ams-corp.com/the-u-s-nuclear-regulatory-commission-approves-ams-technology-for-widespread-implementation-in-nuclear-power-plants/
- Entergy fleet LAR CNRO2024-00002 (Dec 4 2024): ANO 1&2, Grand Gulf, River Bend, Waterford 3 -> OLM condition-based calibration per AMS-TR-0720R2-A; ~1 yr review expected. https://www.nrc.gov/docs/ML2433/ML24339B304.pdf
- NRC audit of Diablo OLM LAR Aug 19 2025 (still under review then). https://www.nrc.gov/docs/ML2523/ML25230A241.pdf
- => 7 units filed in Dec 2024, ~3 yrs after topical approval. Adoption slow; incumbent AMS (services + OLM software).
- Duke M&D (AVEVA PRiSM) 11,000 models, 500k points, $34M single catch 2016 (non-nuclear fleet). https://www.aveva.com/en/perspectives/success-stories/duke-energy/
- Nuclearn: 50+ facilities (Power Technology, Nov 21 2025), "50% procedure prep time reduction"; licensing pre-check 400 h -> <1 day (Heatmap). Pricing undisclosed. https://www.power-technology.com/features/working-smarter-in-nuclear-nuclearn-on-using-ai-to-optimise-operations/ ; https://heatmap.news/climate-tech/nuclearn-ai-nuclear
- Byron/Braidwood uprate (WNN Feb 22 2023): $800M for 135 MWe (~$5,900/kW), turbine replacements, first output 2026, full by 2029. https://www.world-nuclear-news.org/Articles/Reprieved-Illinois-plants-to-be-uprated
- Bloomberg/EnergyConnects (Sep 25 2026): US nuclear startups raised $4.6B in 2026 (vs $3.8B 2025); only 2 new commercial reactors under construction in US/Canada; widespread commercialization ~2035. https://www.energyconnects.com/news/renewables/2026/september/ai-s-nuclear-power-push-runs-into-cost-and-regulatory-hurdles

---------------------------------------------------------------------
# SYNTHESIS REPORT — Selling software to the operating nuclear fleet (as of 2026-10-03)

## 0. Frame: where the fleet's money is
- US fleet operating cost in 2025 was $20.82/MWh. Total generating cost was $36.46/MWh. Capital spend rose 23.9% y/y as uprates, life extension and digital work ramped (NEI Costs in Context, Aug 2026). At ~780 TWh/yr, that is roughly $16B/yr of opex plus about $7.5B/yr of capex across ~94 reactors. Only the per-MWh figures are sourced; the totals are my arithmetic.
- New-build is slow. Two commercial reactors are under construction in the US and Canada, and widespread commercialization is put at ~2035, even though nuclear startups raised $4.6B in 2026 (Bloomberg via EnergyConnects, Sep 25 2026). In 2026-2028, money changes hands at the existing fleet: availability, uprates, restarts and life extension.
- Europe: EDF spends more than EUR 6bn/yr on French maintenance. Availability fell to 74% in 2014-24 (Cour des comptes, Nov 2025). Grand Carénage is budgeted at EUR 100.8bn for 2014-2035. In 2025, 23 of 43 outages finished early under the START 2025 programme (EDF results, Feb 2026). EDF is a single, centralised buyer that is already working on outage performance.

## A. Surveillance-test-interval optimisation (SFCP / TSTF-425 / NEI 04-10)
**Adoption.** SFCP is universal. TSTF-596 Rev 2 (Oct 2024) says TSTF-425 "has been incorporated into the TS of all plants except Vogtle Units 3 and 4". It also says more than 75% have TSTF-545 and about two-thirds of sites hold 50.69 approval (ML24282B020). Getting the license is not the constraint.
**How intervals change today.** Each change is a STRIDE-type evaluation under NEI 04-10. The steps are: collect test history from several site organisations, quantify risk in the PRA per RG 1.174/1.177, take the case to an Integrated Decision-making Panel (IDP), then monitor performance after extension. Usage is low: Callaway got SFCP in 2011 and had implemented only two STI changes by Dec 2017 (PSAM14 paper). NextEra had about 100 STRIDEs.
**Value per change is small.** An INL LWRS review (June 2019) counted 68 STRIDEs at STARS plants. They saved more than 12,110 person-hours/yr, about 178 h and about $8.9k per STRIDE per year, plus about $378k/yr of replacement power. The value concentrates where an extension takes work off the outage critical path. NEI (Mar 2023) cites the station-blackout test extension at up to 24 h of outage, and 50.69 at 230 engineering h/yr.
**Condition-monitoring as the justification. This is the sharper part of A.** NRC approved AMS-TR-0720R2-A in Sep 2021. It lets pressure, level and flow transmitter calibrations move from time-based to condition-based using online monitoring (OLM). AMS claims up to 90% fewer calibrations and up to $5M per plant per 18 months, based on Sizewell B. Sizewell B also cut 5 outage days and 75% of outage transmitter calibrations (INL 2019). Adoption is slow. The first US LARs came about three years after approval: Entergy for ANO 1&2, Grand Gulf, River Bend and Waterford 3 (Dec 4 2024), and Diablo Canyon 1&2 (Dec 2024). NRC was still auditing Diablo in Aug 2025.
**Who does this now.** EPM (STRIDES tool and IDP support), Jensen Hughes and other PRA consultancies, utility PRA groups, AMS (the OLM methodology owner and a small services and software firm), and EPRI guidance.
**Verdict.** An "SFCP optimiser" on its own is too thin, at about $9k/yr per change. The real opportunity is a general engine for condition-based compliance: it turns historian, surveillance and CAP data into NRC-grade evidence for removing time-based tests (OLM calibrations, STRIDEs, IST/ISI relief requests). Relief requests already lean on inspection history; Ginna's Mar 2025 tendon relief cites seven precedents. It fits an ML team. Two problems: adoption is paced by the regulator and the IDP, and plant data access is hard because historian and OT data sit behind 73.54 cyber controls.

## B. Outage emergent-work prediction and schedule risk
**Durations.** Constellation averaged 21.5 days per refuelling outage in 2025 and says that is about 16 days better than the industry average, which implies roughly 37 days (Constellation reliability page). INL LWRS put the average at about 30 days (2023).
**Cost per day.** "More than $1 million a day" (ANS/INL, Sep 2025). Delays cost "several million dollars per day" (INL/RPT-23-74439). Point Lepreau (CANDU) refuelling problem "up to $600k daily" (Global News headline, date unverified: https://globalnews.ca/news/371657/).
**Overrun causes.** Emergent issues found during the outage, such as inspection findings and equipment failures, are the main disruptor. Others are missing tasks and logic errors in schedules of 20-25k activities, plus contractor and resource mismatches (OPG case; INL). Up to 40% of the time of highly trained engineers goes to repetitive admin such as populating schedules (OPG).
**Existing tools.** Oracle Primavera P6 is the system of record. Risk overlays include Primavera Risk, Safran and Acumen. INL is building ML tools for schedule resilience. OPG built a custom ML/NLP scheduler. **Nuclearn Project Genius** already sells ML plus Monte Carlo on historical P6 data. One reference: a US plant used 10 years of data to find an activity that sat on the critical path 90% of the time. EDF runs START 2025 internally.
**Verdict.** The value is real: about 60 US outages a year at roughly $1M+/day, with a ~15-day gap between best and average. But the category is contested. Nuclearn sells into 50-70+ facilities, and EDF does this in-house. Emergent-work prediction from CAP, work-order and inspection history is the less-served subproblem, and Nuclearn holds the CAP data at many sites.

## C. Uprate and restart engineering throughput
**Pipeline.** NRC's expected-applications page (updated Sep 8 2026) lists 32 applications for 2026-2032, totalling 7,336 MWt. They include:
- a Constellation EPU of 1,014 MWt in Q4 2026
- Brunswick, Wolf Creek and Constellation MURs in 2027
- McGuire and Hatch EPUs and a Salem SPU in Q2 2027
- Columbia EPU (1,923 MWt) in 2028
- Catawba 1 and Vogtle 1&2 EPUs in 2028
- Perry in 2029, Beaver Valley in 2030-31, Davis-Besse in 2032
**Policy.** DOE UPRISE (Mar 2026, INL-managed) targets 2.5 GW by 2027 and 5 GW by 2029, with loans covering up to 80% of costs. NRC review targets: EPU 12 months, SPU 9, MUR 6.
**Bottlenecks named.** "Engineering bandwidth and scheduling at utilities", long-lead equipment, staffing, investment decisions and NRC capacity (POWER, Mar 2026). On economics: Byron/Braidwood cost $800M for 135 MWe, about $5,900/kW (WNN 2023). Restarts: Palisades $1.52B for 800 MW, Crane $1.6B for 835 MW.
**What the work is.** NEI 08-10 puts a full uprate at about 3-4 years, with analysis taking 12-36 months. It covers fuel/core, NSSS, BOP, Ch. 15 transients, containment, radiological, flow-induced vibration, PRA and grid studies. The LAR scope is "rivalled only by license renewal and ITS conversion".
**Who does it.** NSSS and fuel vendors run the critical-path safety analyses with NRC-approved proprietary codes: Westinghouse, Framatome, GE Vernova/GNF. A/Es handle BOP calcs, modifications and the LAR: Sargent & Lundy, Enercon, Jensen Hughes, Zachry. Utility engineering owns design-basis configuration management.
**Could software compress it?** Partly. A power change ripples through hundreds of design-basis calcs, setpoints, procedures, drawings, EQ files and UFSAR sections. Today engineers trace that impact by hand across legacy PDFs. Software that builds a parameter-to-document dependency graph could do the impact scoping, flag affected calcs, pre-draft revisions and assemble the LAR and UFSAR markups. Nuclearn reports cutting a licensing pre-check from 400 hours to under a day. I found no product dedicated to uprates. Nearby players are Nuclearn "Engineering AI", Everstar (Gordian, $4M pre-seed in Feb 2025, focused on licensing) and Westinghouse bertha/HiVE.
**Verdict.** This has the highest value and the clearest "why now" (data-centre PPAs, UPRISE, an application peak in 2027-28). The weakness: the critical path partly runs through vendor-owned codes, and 10 CFR 50 Appendix B QA forces every output to be independently verified.

## D. Other operating-fleet problems
- **Knowledge search, OE and Q&A: closed.** Atomic Canyon's NIVA was built with EPRI, INPO and NEI. It moved from a six-month pilot at Constellation (26 reactors) to fleetwide availability for North American members on Aug 18 2026, with NVIDIA as a new investor. PG&E estimated about 15,000 h/yr of search time saved at Diablo.
- **CAP screening, procedures and work packages: heavily contested.** Nuclearn has CAP AI, procedure and work-package tools, Parts AI, 50-70+ facilities and a "50% procedure prep time" claim.
- **Digital I&C upgrades.** NRC approved Limerick's $167M digital safety retrofit on Jan 5 2026, the first multi-system one at an operating US plant (DOE cost share $50M). More will follow. The work is vendor-dominated (Westinghouse Common Q and others). There is a software opening in V&V, the 50.59/LAR evidence package and the cyber assessment, but each project is lumpy.
- **Cybersecurity (10 CFR 73.54, NEI 08-09 Rev 7, RG 5.71 Rev 1).** This is a compliance burden with established OT-security vendors. I found no quantified fleet cost in the time available.
- **Workforce.** DOE's advisory board says the workforce must triple to quadruple capacity. North American nuclear postings were 14,016 in May 2026, down 12% y/y, but operator hiring rose: Vistra +74%, Exelon +40%. Training and simulators belong to L3Harris and GSE.
- **Fuel and core.** Blue Wave AI Labs has a $6M DOE award with Constellation for BWR core sensor calibration and fuel optimisation, with about $80M of savings estimated across 32 BWRs.
- **Equipment monitoring.** GE Vernova SmartSignal and AVEVA PRiSM run utility M&D centres. Duke's centre has 11,000 models and caught a single $34M issue (non-nuclear fleet). This is mature and commoditised.

## E. Competitor map, 2025-2026
| Company | Funding | Traction | Lane |
|---|---|---|---|
| Nuclearn | $10.5M Series A, Sep 2025 (Blue Bear) | 50-70+ facilities in US/CA/UK; certified service-provider programme Feb 2026 | CAP, procedures, work packages, parts, outage schedule (Project Genius), engineering, licensing |
| Atomic Canyon | $7M seed, May 2025 (EIP); NVIDIA plus others Aug 2026, undisclosed | Diablo Canyon; NIVA fleetwide via EPRI/INPO/NEI; Constellation pilot | Search, OE, troubleshooting (FERMI models with ORNL) |
| Everstar | $4M pre-seed, Feb 2025 | Gordian compliance platform | Licensing documents, mostly new reactors |
| Palantir + The Nuclear Company | TNC raised $51M (May 2025) | NOS launched Jun 2025 | Construction |
| Westinghouse + Google Cloud | n/a | HiVE, bertha, WNEXUS (Jul 2025) | AP1000 work packages, some fleet optimisation |
| GE Vernova SmartSignal, AVEVA | incumbents | M&D centres | Predictive equipment monitoring |
| Blue Wave AI Labs | ~$6.9M including DOE $6M | Constellation BWRs | Core sensors, fuel |
| AMS Corp | private, small | NRC-approved OLM TR; Entergy and Diablo LARs | Condition-based calibration |
| EPM, Jensen Hughes, S&L, Enercon | services | everywhere | SFCP, PRA, uprate engineering |
| EPRI, INL LWRS | non-profit, lab | research tools, NIVA partner | Free or cheap research tools that compete with startups |
| Curio | n/a | recycling, not fleet ops | not a competitor |
I found no YC company in fleet-ops software. The YC energy list shows Oklo, Atomarine (S26), Terranox (W26, exploration), Maritime Fusion and Helion.

## F. How utilities buy
- **Cycle.** Atomic Canyon at Diablo: first talks in spring 2024, model test in Sep 2024, announcement in Nov 2024, on-prem NVIDIA hardware at end-2024, internal documents in Q3 2025. That is about 12-18 months to production, after founder-led relationship selling. PG&E staff shadowed the vendor on site for weeks.
- **Shape.** Pilot at one site, then fleet rollout. The industry-blessed channel now runs through EPRI, INPO and NEI (NIVA). Deployment is on-prem or in a private cloud with QA classification (non-safety, "junior employee" with a human signoff). Nuclearn now uses certified service providers to reach more sites.
- **Contract sizes.** Not disclosed by any vendor. Do not quote a number without a source. Budgets come from the site's O&M or capital project. Uprate work would be paid from the capital budget (about $5,900/kW), which is far larger than IT budgets.

## G. Ranking of wedges
1. **Uprate and LAR design-basis impact engine.** Highest value, most urgent, no dedicated product. Its risk is that vendor codes own the critical path.
2. **Condition-based surveillance and calibration evidence engine** (OLM, SFCP, IST/ISI relief). Open and recurring, and it suits an ML team. The value per unit is capped at about $3M/yr and adoption is regulator-paced.
3. **Emergent-work prediction for outages.** Large value, but Nuclearn is already there.
4. Knowledge search, CAP and procedures: closed.
