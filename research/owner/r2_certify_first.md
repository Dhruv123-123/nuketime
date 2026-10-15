# Round 2 lane: certify first, own the aftermarket

Written 15 Oct 2026. 19 of my 20 WebSearch calls used. Figures marked "(memory)" are from my own
knowledge and were not checked this run. I could not fetch any FAA, NRC or DLA databases directly;
everything below about access is based on their documentation.

## Bottom line

**The lane fails Terranox law (1).** No regime I examined gives an exclusive right to whoever files
first for a replacement part or repair. An FAA PMA, a DLA Source Approval (SAR), a nuclear
commercial-grade dedication, an AAR approval or a class type approval only gives permission to
compete. Several holders can have approvals for the same part, and HEICO, Chromalloy and Jet Parts
often do on CFM56/V2500 parts. What a PMA house actually owns is:

- its design data (a trade secret);
- airline engineering acceptances, earned one customer at a time;
- catalog breadth.

None of these is a claim.

The data edge is also wrong:

- SDRs record in-service *difficulties*. They do not record shop-visit *consumption*, and
  consumption is what drives PMA revenue. Blades, seals, liners and brackets are replaced to manual
  limits and never show up as SDRs.
- The best selection data is private. HEICO gets it through equity partnerships with airlines and
  MROs: Lufthansa Technik's stake in HEICO Aerospace (memory), and parts purchase data from American,
  Delta and United, among others.
- OEM list prices sit in commercial catalogs (ILS, PartsBase, Spec2000 and OEM portals). They are not
  public.

Choosing which part to copy is not the bottleneck. These are:

- engineering, test and computation;
- FAA review: months for identicality, 9-18 months for test-and-computation parts, plus 4-8 weeks
  per comment round;
- airline, lessor and engine-OEM acceptance.

The ceiling is real, though. HEICO is a ~$35-45B company (memory). It has 19,000-20,000 FAA approvals
and makes 500+ new parts a year (IATA, Nov 2025; HEICO Q1 2026 call). The field is consolidating
fast, into strong hands:

- HEICO bought Wencor for ~$2.05B in 2023 (memory; Wencor went to HEICO, not Boeing).
- TransDigm bought Jet Parts Engineering and Victor Sierra for $2.2B in January 2026.

Realistic outcome: build a PMA catalog and sell it to HEICO or TransDigm at a high multiple. That is
a fine business, but it is neither unattackable nor uncrowded. **Best score in the lane: 4/10.**

One adjacent idea has a real exclusive right: **buying orphan or under-supported type certificates
(TCs)**. A TC is property, and its holder controls design data and ICAs. It is scored below, but it
is M&A, not ML.

---

## 1. Aviation PMA (main thesis)

**Datasets and why they are public**
- FAA SDRS. Operators must report under 14 CFR 121.703/135.415, and the FAA publishes the reports.
  Quality is poor: free text, reporting is uneven, and GA reporting is largely voluntary.
- Airworthiness Directives. These are rules, so they are published in the Federal Register.
- The FAA DRS holds the PMA and STC listings and the TCDS. These are public because installers must
  be able to verify approval.
- The FAA aircraft registry, which is public by statute.
- ADS-B utilisation, via OpenSky and ADS-B Exchange. ADS-B Out is mandatory and broadcast in the
  clear.

**ML problem.** Join SDR/AD free text to ATA chapter and part number. Join registry and ADS-B data to
get cycles and hours per tail. Estimate removals per part and fleet demand, then rank by demand x
OEM price x ease of copying x absence of competing PMAs. This is a real NLP and entity-resolution
task. But the demand signal is weak: SDRs miss most consumption, and prices are not public.

**What is owned**
- A PMA for the applicant's design. It is non-exclusive, has no fixed term, and anyone can obtain a
  competing PMA.
- Design data, held as a trade secret.
- Airline acceptances.
- Exclusivity: none in law. In practice, the first entrant on a part gets roughly 2-5 years before a
  second PMA splits the market.

**Pool**
- Engine PMA plus DER repair: ~$3.45B in 2025, of which PMA parts are ~$2.0B, growing 7-8% a year
  (Strategic Market Research). That is small against a $100B+ MRO market.
- PMA discount to OEM: 20-50%.
- HEICO estimates it holds about 2% of the replacement-parts market. Headroom is large on paper, but
  it is gated by acceptance.
- IATA's 2025 survey lists the obstacles to PMA use: lessor transferability and asset value, OEM
  contracts and warranties, and OEM threats to limit support (FAA SAIB NE-08-40).
- New-generation engines (LEAP, GTF) are mostly locked into OEM power-by-the-hour contracts. HEICO
  disagrees and says high next-generation spares prices are a tailwind.

**Who already farms it**
- HEICO/Wencor, which has a 20,000-part catalog and calls new entrants "imitation".
- TransDigm, through JPE and Victor Sierra.
- Chromalloy (with AAR distributing its parts), AerSale, ATS (which already uses AI 3D scanning for
  PMA), ACS, First Aviation, VSE, plus the engine OEMs' own alternative-parts arms.

AI-adjacent startups:
- Novineer: photo-to-CAD reverse engineering, aimed at defence.
- ePlaneAI: a parts marketplace.
- Intropy: an $11M seed for spare-parts pricing and inventory software. It sells software and does
  not own parts.

I found no startup doing "public data ML picks the target, then we own the PMA". That gap exists
because target selection is the cheap part of the job.

**First proof.** Take one CFM56 or V2500 consumable that has no competing PMA. Win an identicality
or test-and-computation PMA in under 12 months, and get two airline acceptances. Cost is roughly
$0.3-1M per engine part (my estimate).

**Scores (1-10)**

| Criterion | Score |
|---|---|
| Public data | 6 |
| ML edge | 3 |
| Claimability/exclusivity | 2 |
| Ceiling | 8 |
| Crowding (10 = empty) | 2 |
| **Overall** | **4** |

## 1b. Aviation STC modifications (fuel burn, cabin, avionics)

- **Data:** the same public data as PMA, plus ADS-B mission profiles. These allow modelling
  fuel-saving retrofits per fleet.
- **Owned:** the STC, which is non-exclusive in law but protected in practice by patents and
  flight-test cost.
- **Precedent:** Aviation Partners and APB winglets fly on more than 5,000 aircraft.
- **Costs and players:** retrofits cost $20-100M+ in aero engineering and flight test. Incumbents
  are OEMs, APB, Collins and the cabin integrators.
- **ML:** helps size the market but does not create the mod.

**Overall: 3.**

## 1c. Orphan or under-supported type-certificate acquisition (the one true "claim")

- **Data:** the TCDS (which names the TC holder) and the registry (active fleet by type) are public.
  SDRs and ADs show the support burden and the parts shortage.
- **Owned:** the TC itself. It is exclusive design authority, makes the holder the de facto
  sole-source OEM for parts, and has no expiry.
- **Precedents:**
  - Mitsubishi bought the CRJ programme from Bombardier, about $550M in 2020 (memory).
  - Longview/De Havilland Canada bought the Dash 8 and Twin Otter TCs.
  - Fokker Services holds the Fokker TCs.
  - TransDigm's whole model is buying sole-source certified designs.

The ranking problem is easy: TCDS joined to the registry is close to a lookup, so ML is not the
edge. The edge is M&A sourcing, and the owners know what they hold. Assets are lumpy, from $10M to
$1B, so this is a capital play.

**Overall: 4** (exclusive and asset-sized, but not ML-driven and not cheap to claim).

## 2. Defence alternate-source qualification (DLA SAR)

**Data**
- DIBBS solicitations and the SRVA, which gives 24-month forecast quantities.
- DLA's Value Management list of NSNs it wants broken out.
- FPDS award prices.
- cFolders technical data.

These are public because of competition-in-contracting law and DLA's small-business mandates.

**ML.** Rank sole-source or limited-source NSNs by spend x price inflation x feasibility of reverse
engineering, then use AI for reverse engineering itself.

**Owned:** SAR approval, which makes you an approved source. It is non-exclusive, and DLA then runs
a price competition. NSNs with less than $10k annual buy value are excluded from the reverse-
engineering programme.

**Pool:** sole-source spares spend runs to billions a year (memory). But breaking out a part
destroys exactly the margin that made it attractive.

**Crowding:** hundreds of small reverse-engineering shops, Haystack and PTAC tooling, Novineer, and
SBIR "AI for legacy drawings" topics.

**Overall: 3.**

## 3. Nuclear and utility spare-part obsolescence

**Data**
- NRC 10 CFR Part 21 reports and LERs, in ADAMS (public by law).
- EPRI material is members-only.
- RAPID, the utilities' surplus-parts database run for 30+ years, is private.

**ML.** Map Part 21 defects and obsolescence notices to the installed base of plant equipment. The
installed-base data is not public.

**Owned:** nothing exclusive. The utility or an Appendix B supplier does commercial-grade dedication
or reverse engineering. Supplier standing comes from NUPIC audits and is non-exclusive.

**Pool:** 94 US reactors. Obsolescence spend is a few hundred million dollars a year in the US
(estimate). The ceiling is a service market.

**Who farms it:** Curtiss-Wright (Idaho Falls and Middleburg Heights), Paragon Energy Solutions,
Framatome, Westinghouse and AtkinsRéalis. The nuclear contract manufacturer idea was already killed.

**Overall: 2.**

## 4. Rail (FRA, AAR)

**Data:** FRA accident and incident reports (Form 6180.54) and the equipment-defect data are public.
Failure data at component level is thin.

**Owned:** AAR M-1003 quality certification, plus approvals for each component. These are
non-exclusive.

**Market:** freight-car parts are largely commodities and already multi-sourced (Amsted, Wabtec,
Stucki and others). Locomotive parts are a Wabtec/Progress Rail duopoly that already has third-party
rebuilders.

**Pool:** low single-digit billions of dollars, at low margin.

**Overall: 2.**

## 5. Shipping class type approvals

**Data:** class type-approval registers (DNV and ABS finders) are public. IMO GISIS, MAIB and
Equasis carry casualty data.

**Approvals:** most engine spares need no type approval. Non-OEM spares for MAN and Wärtsilä engines
are a mature, fragmented market made up of Greek, Chinese and Korean suppliers. There is no
exclusivity.

**Overall: 1.**

## 6. Medical-device repair parts

**Data:** FDA MAUDE, the 510(k) database and recalls are all public by statute.

**Regulation:** ISO servicing parts mostly need no 510(k). FDA's 2018 report found no case for more
regulation, and its 2024 remanufacturing guidance draws the line between servicing and
remanufacturing. That makes the "approval" weak and non-exclusive.

**Who farms it:** CT tubes are already made by Varex (25,000+ tubes a year), Dunlee, Chronos and
Richardson. OEMs also lock systems with software keys.

**Pool:** CT tubes are about $1-1.5B (memory).

**Overall: 2.**

## 7. Wind-turbine aftermarket

**Data:** no public failure data at component level. The NREL Gearbox Reliability Database is a
consortium resource, and operator data is private. There is no certification moat for spares.

**Who farms it:** Liebherr, FST, ZF, Gearbox Express and marketplaces such as Spares in Motion.

**Overall: 1.**

## 8. Semiconductor fab legacy spares

**Data:** no public failure or consumption data.

**Approval:** each fab qualifies parts under copy-exact rules. This is non-exclusive and private.

**Who farms it:** a large spares market (OEM services run to tens of billions of dollars) is being
attacked by Chinese and Korean localisation programmes and US third parties such as AG Semiconductor
Services.

**Overall: 2.**

---

## Score table

| Candidate | Public data | ML edge | Exclusive claim | Ceiling | Uncrowded | Overall |
|---|---|---|---|---|---|---|
| Aviation PMA | 6 | 3 | 2 | 8 | 2 | **4** |
| Aviation STC mods | 6 | 3 | 4 | 6 | 3 | 3 |
| Orphan TC acquisition | 7 | 2 | 8 | 6 | 4 | 4 |
| DLA SAR breakout | 7 | 4 | 2 | 5 | 3 | 3 |
| Nuclear obsolescence | 4 | 3 | 1 | 2 | 3 | 2 |
| Rail (FRA/AAR) | 4 | 2 | 1 | 3 | 3 | 2 |
| Shipping class | 3 | 2 | 1 | 3 | 2 | 1 |
| Medical repair parts | 6 | 3 | 1 | 4 | 3 | 2 |
| Wind aftermarket | 1 | 2 | 1 | 4 | 3 | 1 |
| Fab legacy spares | 1 | 2 | 1 | 6 | 2 | 2 |

**Kill the lane as a Terranox analogue.** Regulators of safety-critical replacement parts give
permission, not exclusivity, because their whole purpose is to allow second sources. Where real
exclusivity exists (the TC), it is bought through M&A, not found by reading data. PMA remains a good
roll-up business to sell to HEICO or TransDigm, but it is not unattackable.

## Sources
- [HEICO: A Compounding Beast (Eagle Point)](https://eaglepointcapital.substack.com/p/heico-a-compounding-beast)
- [Engine PMA & DER repair market](https://strategicmarketresearch.com/market-report/engine-pma-parts-and-der-repair-market)
- [TransDigm $2.2B deal for JPE and Victor Sierra](https://pulse2.com/transdigm-2-2-billion-deal-for-jet-parts-engineering-and-victor-sierra-aviation)
- [TransDigm 8-K Jan 2026](https://www.sec.gov/Archives/edgar/data/1260221/000126022126000002/exhibit991pressreleaseanno.htm)
- [Aviation Maintenance: PMA parts 2025](https://avm-mag.com/pma-parts-surge-ahead-availability-and-innovation-drive-growth-in-2025)
- [IATA approved alternative parts webinar, Nov 2025](https://www.iata.org/globalassets/iata/programs/operations-infrastructure/technical-operations/events/2025-11-19_presentation-iata-webinar-approved-alternative-parts.pdf)
- [HEICO Q1 2026 call summary](https://finance.yahoo.com/news/heico-corporation-q1-2026-earnings-133000307.html)
- [Prime Propulsion: PMA timelines](https://www.primepropulsion.com/post/faa-pma-certification-timeline-delays)
- [Novineer AI reverse engineering](https://thedefensepost.com/2026/06/30/novineer-ai-reverse-engineering-sustainment/)
- [Intropy $11M seed](https://tech.eu/2026/07/30/ai-for-spare-parts-startup-intropy-raises-11m/)
- [DLA SAR / RPPOB breakout, NDIA 2024](https://ndia.dtic.mil/wp-content/uploads/2024/dla/Tue_Breakout_SAR_RPPOB.pdf)
- [DLA SAR Guide](https://www.dla.mil/Portals/104/Documents/SmallBusiness/DLA%20SAR%20Guide.pdf)
- [Curtiss-Wright nuclear obsolescence](https://nuclear.curtisswright.com/products-and-services/obsolescencesolutions)
- [DOTmed: CT tube market](https://www.dotmed.com/legal/print/story.html?nid=48020)
- [Aviation Week: winglets fuel saved](https://aviationweek.com/aerospace/three-billion-gallons-jet-fuel-saved)
- [Spares in Motion wind parts](https://www.sparesinmotion.com/wind-turbine-parts/gearbox-parts)
