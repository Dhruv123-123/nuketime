# CRITIC.md: completeness review of SENTINEL-HELM (MODEL.md)

Date: 24 Oct 2026. Reviewer: completeness critic. Claims were checked against `evidence/L01-L40`, `redteam/`, `../MEMO.md` and `../model/evidence/M11, M20, M33`. The shared web-search budget was used up, so no new searches ran. Everything below comes from repo files. Anything not re-checked is marked (unverified).

**Overall.** The design is strong. Its key numbers check out (ICE 4.7 vs 5.1 C, NDWR 146,235 with 9.8% keyed, OSWCR 1,111,251, $3.50/acre median, GAO-26-108040, Martinelli +14.8%, Sodir 1.4-2.5x). Gaps are ranked by how much damage each would do if a top geothermal ML researcher or a YC partner found it first.

---

## Ranked gaps and fixes

**1. The gates score heat, but holes fail on permeability.** L40 says most Great Basin failures are "hot but tight" or "hot in the wrong place". Well productivity spans 0.5 to over 100 kg/s/bar. Yet the main gate (G3) and the buy list (G8, T(1 km) > 120 C) test temperature only. No gate tests the pathway field. "Deliverability" and "productivity index" never appear in MODEL.md.
*Fix:* Add gate G3b. Score the pathway and failure-mode posteriors on held-out flow tests, lost-circulation records and productivity data (NDOM well files, GDR flow tests, PFA Phase 3 wells, Ormat's 40-field back-solve). Make the buy list require both T(1 km) > 120 C and P(pathway open) above a bar.

**2. A model can win G3 on the conductive background and still miss upflows.** Convective readings are a small share of all T(z) readings (unverified share). A model that fits the regional gradient well will win mean log score even if it misses every upflow.
*Fix:* Report log score and coverage on the convective stratum: readings more than 2 sigma above the freeze-time conductive prior. Add upflow-detection PR-AUC and a profile-shape score (reversal, isothermal, Peclet curvature; L10 point 4). The stratified score is the pass bar.

**3. The leak through pretrained models is still open.** The D01 data and science red teams said ICE and the VLMs were trained on post-2008 wells and text, and asked for "ICE-West retrained per freeze". MODEL.md gives legality cards to INGENIOUS, USGS 2025, FSS, AlphaEarth and GeoDAWN, but not to the ICE weights, the Burns/Sui conductive priors, or the extraction VLMs. PoC contender (b), "ICE alone", may already have seen the test wells.
*Fix:* Give every pretrained weight file its own legality card. Retrain ICE per freeze on known_time-filtered wells only. Retrain contender (b) the same way. Rebuild the Burns/Sui-style prior from data available before the freeze, or drop it from legal-only runs.

**4. The model's exit logic does not match the MEMO business.** The MEMO says value jumps only at confirmation plus PPA plus interconnection: about $0.1M/MW without a PPA against $4.3-5.6M/MW when operating (L37). The bank keeps a carry or a $/MWh override. The binding federal limit is the 51,200-acre per-state cap. MODEL.md's rung ladder stops at "bankable". It has no PPA or queue rung, no override value and no acreage cap. Buyer demand (Ormat sourcing up to 150 MW for Google; Fervo's 658 MW of PPAs and 3 GW Google framework) appears nowhere in MODEL.md.
*Fix:* Add rungs for "queue position" and "PPA-ready". Value carries and overrides in L3. Make the 51,200-acre cap a hard planner limit. Add a buyer-demand head built from offtake announcements, LBNL Queued Up, utility IRPs and large-load filings.

**5. Planner lift is proven only on our own worlds.** Bar 7 plans on GHOST Tier 1 and scores on TOUGH3. We build both.
*Fix:* Replay real history. OFR 99-425 (786 holes, 82 prospects) and NBMG's 442 dated industry TG holes record which hole each company drilled next. Give HELM the evidence known at each date and test whether its order reaches the hot hole in fewer holes or dollars than the company did.

**6. Mining holes are wired as effort, not as heat data or as a sensor channel.** L31: in 8 of 11 US blind finds, the first signal was a hole drilled for something else. M20: Nevada drills more than 2,000 mining holes a year. NBMG's temperature layer has 226 mining and 82 dewatering wells, 41 of them at 50 C or more. Meikle mine rock reaches 140-160 C. MODEL.md uses mining only as claim-filing effort and an NI 43-101 fallback.
*Fix:* Make mining a P0 thermal channel. Extract the NBMG mining and dewatering wells. Have the Archivist mine SEDAR+ and NI 43-101 reports for "hot water", "steam" and "lost circulation". Run a ride-along memory-thermometer program with drilling contractors (proposal P07). It is the best source of lead time.

**7. Several schema data types are missing or thin.** GPS/GNSS strain rate was a layer in the Nevada PFA (L01; M11 says it correlated "significantly" with hot wells), but MODEL.md never mentions it. Thermal IR (ECOSTRESS, ASTER, Landsat), Curie depth, radiometric heat production, oil-and-gas 2D seismic reflection (basin depth for B3) and LMP/PPA prices are also absent.
*Fix:* Strain rate into the pathway field (P0). Thermal IR as a surface-leakage likelihood (P2). Curie depth and radiometrics into the deep heat prior (P1). Seismic lines into B3 basin geometry (P1). Prices into L3 (P1).

**8. The EGS buyer head has no validation.** ICE errors rise to 7.9 C at 2-4 km and 11.2 C at 4-6 km, and only 3% of readings are deeper than 4 km (L10). At FORGE the upflow is about 100 C cooler at 4-5 km than conduction predicts (L30). Fervo's Cape Station reached commercial operation on 30 Sep 2026; yet the EGS template waits until month 7+.
*Fix:* Add a coverage gate by depth band, built from deep oil-and-gas BHTs (Utah, Nevada), FORGE and public Cape data. Bring a B5 "buried basement under insulating fill" template into v1, at least for the value head.

**9. The size model ignores the repo's own evidence.** MODEL.md uses USGS 2008 triangles with a 0.5-0.7x haircut. L09 and M33 recommend power density (Wilmarth & Stimac 2014: median 12 MW/km2 across 53 fields) and a Great Basin lognormal (median about 29 MW, sigma about 0.95, power-law tail).
*Fix:* Use area x power density, with the M33 prior shifted by temperature and setting. Hindcast it on the 18 Nevada producing fields. Add a size-narrowing sensor (dense 2 m grid plus E-MT outline of the upflow) to the EVSI list.

**10. The random audit cannot see buried systems.** G9 uses one 2 m line or one Sentinel per cell. A 2 m probe cannot see lidded B3/B4 systems, so the audit is biased for them.
*Fix:* Model detectability per audit cell and archetype. Add a stratified subsample measured with deeper tools (water-well sondes via pump-pullers, P12; a few TG holes). Report audit results by archetype.

**11. Test power is assumed, not counted.** "Thousands" of post-2015 readings is open question 2. There are about 8-15 lead-time events. Bars such as AUC >= 0.7 and 12 months lead time are unverified.
*Fix:* Count by date now from the NBMG REST layers (10,991 records) and NDOM permits; set each bar from its minimum detectable effect.

**12. The scope is too big for the team, and there is no market test.** Months 1-3 ask three people for about ten subsystems; the PoC is desk-only.
*Fix:* Run a "money path" in parallel: extraction, heat, a static lock rule, 50 ranch letters (measures v1 kill 8, the refusal rate) and one buyer LOI on a case file.

**Minor.** Pandora assumes independent boxes; the play factor breaks that, so report the gap to POMCPOW. Fluid-appropriation rights (separate from heat title in some states) are absent from the title latent (unverified per state). Check that the Oregon vault has enough readings to have power.
