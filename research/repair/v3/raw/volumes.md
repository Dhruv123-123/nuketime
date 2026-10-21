# volumes: How many CGD jobs, new plans, obsolescence events and emergent dedications happen per year in the US fleet

Date: 2026-10-21. Builds on v2/raw/g05.md. I used 6 WebSearch calls; everything else came from fetched primary documents, extracted locally with pdftotext. **(recalled)** marks a figure from memory that I did not verify this session. **(est.)** marks my own arithmetic or assumptions.

## Sources fetched
- EPRI 3002029261, *CGD Experience and Efficacy* (Nov 2024), full text: https://restservice.epri.com/publicdownload/000000003002029261/0/Product
- Westinghouse CGD data sheet NS-ES-0507 (2021): https://www.westinghousenuclear.com/media/ev3bi12i/commercial-grade-dedication.pdf (figures carried over from g05)
- Westinghouse POMS data sheet: https://westinghousenuclear.com/data-sheet-library/proactive-obsolescence-management-system-poms/
- Curtiss-Wright ObSolutions brochure 2020: https://cwnuclear.com/sites/default/files/Download-Library/Obsolescence-Brochure-2020.pdf ; obsolescence page: https://nuclear.curtisswright.com/products-and-services/obsolescencesolutions
- TVA OIG Evaluation 2023-17464, *TVA Nuclear Obsolete Equipment* (Jun 2024): https://www.oversight.gov/sites/default/files/documents/reports/2024-06/2023-17464.pdf
- NRC OIG-22-A-06, *Audit of NRC's Oversight of CFSI* (Feb 2022): https://www.oversight.gov/sites/default/files/oig-reports/NRC/ROAOIG-22-06Final.pdf
- AECL/CNS paper, "Obsolescence in nuclear industry" (CANDU): https://proceedings.cns-snc.ca/index.php/pcns/article/download/3626/3625/3661
- Reuters Events Nuclear, "Suppliers collaborate, develop data products in battle against obsolete parts": https://www.reutersevents.com/nuclear/node/54822
- ScottMadden, *Materials Management within U.S. Nuclear Generation Plants* (2009): https://www.scottmadden.com/content/uploads/2018/07/Materials-Management-within-U.S.-Nuclear-Generation-Plants.pdf
- Paragon (VanTassell), NRC CGD workshop deck, 14 Jun 2018: https://www.nrc.gov/docs/ML1815/ML18150A373.pdf
- NRC Part 21 report logs for 2023, 2024 and 2025: https://www.nrc.gov/reading-rm/doc-collections/event-status/part21/2024/index.html (and the /2023/ and /2025/ pages)
- Scientech 2004 utility obsolescence survey, via search snippet only: https://digital.library.unt.edu/ark:/67531/metadc780247/m2/1/high_res_d/840372.pdf

## 1. Dedicator volumes (evidence)
| Entity | Volume | Source |
|---|---|---|
| Westinghouse (New Stanton, PA) | ~50,000 CGD **parts** a year. Library of 1,000+ CGD plans and 4,000+ instructions covering ~50,000 unique part numbers. 50+ engineers and ~75 technicians. Claims to serve "the entire US market" and 75% of global utilities | WEC NS-ES-0507 (2021) |
| Paragon Energy Solutions | ~1,300 CGD **jobs** a year ("one job can include multiple lots of unique parts"). **70-100 new CGD plans a month (840-1,200 a year).** Digital items are under 5% of jobs but rising. Demand "steady", strongest just after the pandemic. ~120 approved commercial suppliers. Holds ~$100M of stock (2018 deck) | EPRI 3002029261 §4.2.2; ML18150A373 |
| UCI (Norcross, GA) | Library of 2,800+ digitized CGD plans covering 270 part classes. Uses Method 1 ~90% of the time. Throughput not disclosed | EPRI §4.2.3 |
| Duke Energy CRDF (Harris) | Handles 25-50% of all safety-related procurement for its 11 units at 6 sites. Performs 95% of Method 1 tests in-house. Carries a **CGD backlog** reported to leadership monthly. "Given more resources and personnel, Duke Energy would be performing more CGD." | EPRI §4.2.1 |
| KHNP (benchmark, ~26 units plus new build) | ~185 unique items dedicated in-house per year plus 515 outsourced (~700 a year). The CPE section manages ~600 dedication packages a year | EPRI §3, §4.8 |
| Supplier survey (8 CGD suppliers, global) | Unique items dedicated per year: 3 suppliers at **>500**, 4 at 100-500, 1 at 50-100. That sums to roughly 3,000-7,000 unique items a year across the 8 surveyed **(est.)** | EPRI Fig. 3-7 |
| Licensee survey | For >20 reactors, 25-50% of safety-related procurements involve CGD, and one licensee reports >50%. Licensees accept "hundreds of unique item types" per year through CGD. 31% of units report CGD use is increasing, 64% flat, 5% decreasing | EPRI Figs. 3-2 to 3-4 |
| Market structure | ">30 companies worldwide" offer CGD services, and the US is the largest market. North American NSSS suppliers do "large volumes" | EPRI §3.9 |
| Curtiss-Wright | Has qualified "thousands of commercial-grade equivalents". Catalogue of 10,000+ obsolescence solutions. Nova unit has reverse-engineered 1,000+ mechanical items (cumulative) | CW brochure; search snippet |

Other dedicators with no volumes found: Framatome, GE Hitachi, Nuclear Logistics (AZZ), Curtiss-Wright Qualtech NP, Ultra Energy, Global Power/others (recalled).

## 2. Plant item and procurement base
- "A nuclear plant typically relies on over 100,000 parts to operate" (Reuters Events).
- Warehouses (ScottMadden 2009): median 24,428 transactions a year covering receiving, issues and returns, worth $45M and 3.7M individual items. 2,901 SKUs managed per FTE (median). 995 days of inventory on hand; turnover 0.19-0.91 a year; ~$20M of slow or non-moving stock per plant. Nuclear inventory grows 3.8% a year against 2.7% for fossil.
- Catalogued stock codes per site: about 40,000-100,000, of which about 20-35% are safety-related (Q) **(recalled)**.
- Safety-related purchase-order lines per site: about 1,000-3,000 a year **(recalled / est.)**. I found no public source. The 2018 NRC/Paragon deck confirms CGD is "Today: Purchase Order Specific", meaning each PO line is a dedication event, with a push toward generic product-line dedications.
- POMS (Westinghouse): 170+ units subscribed worldwide, 12M+ equipment records, 30,000+ vendors contacted once a year for obsolescence status.
- RAPID/OIRD (Curtiss-Wright): Obsolete Item Replacement Database holds **55,000+ items identified as obsolete**, with equivalents. In use for 30+ years. The Seer inventory-matching tool flags duplicate stock codes across utilities.

## 3. Obsolescence rates
- **20-25% of plant components are no longer supported by the OEM** (Rolls-Royce study, via Reuters Events). An older 2004 multi-utility survey (Scientech) puts the obsolete share of replacement candidates at: mechanical ~12%, electrical ~33%, I&C ~27%, about 25% on average.
- **75% of obsolete items are discovered at procurement or procurement engineering**, i.e. reactively, when a part is needed. In the US market, "60+% of nuclear qualified manufacturers have exited the market or dropped their nuclear programs" (AECL/CNS paper). TVA's procedure makes the same point: discovery at procurement is "the most common" and "least desirable" route.
- **TVA, measured (OIG 2023-17464).** Over FY July 2022-June 2023, TVA's 3 sites (7 units) raised **63 obsolescence Action Tracking Items** (raised by supply chain at procurement) and **110 obsolescence Work Order Restraints** (raised by site personnel). That is ~173 a year, or **~58 per site** and **~25 per unit**. Restraint priorities include "Urgent" and "Outage". The fleet Top-5 obsolescence list sat unchanged for 2+ years because capital was on hold, and some solutions "become obsolete before [they are] implemented." Proactive vulnerability reviews were not being done.
- US fleet extrapolation from TVA: ~54 sites × ~58 ≈ **~3,000 obsolescence events a year** that surface in procurement or work orders **(est.)**. A large share of these require either an equivalency evaluation plus CGD of an alternate, or reverse engineering.
- Annual flow into obsolescence: about 3-5% of active part numbers a year for electronic and I&C items **(recalled)**. NUOG (Nuclear Utility Obsolescence Group) was formed in 2000 (Reuters). I found no NUOG or PUSH (Procurement Users ... ; recalled as a utility procurement peer group) statistics.
- Consequence example: an obsolete analog feedwater-pump control board could not be replaced in time and caused a 4-day shutdown of a US reactor, at "approximately 11 million dollars" (the text reads "per day"; probably the total, check) (AECL/CNS).

## 4. Reverse engineering volumes
- No annual counts were found in public sources. Curtiss-Wright (Nova) reports 1,000+ mechanical items reverse-engineered cumulatively. Framatome has 40+ years of I&C, mechanical and electrical reverse engineering. Duke CRDF and Paragon both do it in-house. Electronic reverse engineering "can take months to complete" (CW).
- Estimate: ~300-800 US reverse-engineering projects a year, roughly 10-25% of the ~3,000 obsolescence events, with the rest resolved by an equivalent item plus CGD, a stock search, refurbishment or a design change **(est.)**.

## 5. Part 21 and CFSI (NRC)
- All Part 21 reports, from the EPRI table of NRC data: 509 at the 1985 peak, under 100 from 1996, and 24-39 a year over 2018-2023 (2018 32, 2019 39, 2020 33, 2021 29, 2022 28, 2023 24).
- CGD-involved Part 21 reports: **16 of 28 in 2022 and 10 of 24 in 2023**, i.e. ~45% of all Part 21s involve dedicated items. 22 of those 26 were electrical or electromechanical (breakers/contactors 8, relays 4, power supplies 4).
- NRC Part 21 log counts as listed on nrc.gov: 2023 **31**, 2024 **37**, 2025 **22**. These differ from EPRI's figures because of how revisions and non-power reports are counted. 2024 includes 2024-13 (Transco, "unverified critical characteristics") and 2024-24 (TVA, a "commercially sourced" gate valve).
- CFSI: EPRI, INPO and NUPIC reported **fewer than 10 potential CFSI cases since 2016**, and one third-party organization collected **6 potential cases from 2019 to mid-2021**. The NRC RPS/ROE system flagged 18 "potential CFSI", of which 3 were not CFSI. Counterfeit breakers were found at a Florida utility in February 2021. OIG says the true population "could be greater" because CFSI need not be reported unless it substantially affects safety (OIG-22-A-06). Duke says dedication itself is "one of the primary means of identifying... potential counterfeit items."
- Reading: liability events run at about 10-16 CGD-related Part 21s a year against roughly 20-30k dedication jobs, i.e. on the order of 1 per 1,500-3,000 jobs **(est.)**. This is a priceable tail risk for a new dedicator.

## 6. Estimate: US dedication events, new plans and emergent share (est.)
Fleet basis: 94 operating units at about 54 sites (recalled), with about 60 refueling outages a year (18-24 month cycles, recalled).

**A. Bottom-up from dedicators (jobs, meaning a PO line or lot)**
| Segment | Jobs/yr | Basis |
|---|---|---|
| Westinghouse | 5,000-10,000 | 50,000 parts/yr at ~5-10 parts per job (assumed); part goes to non-US customers |
| Paragon | 1,300 | EPRI |
| UCI | 1,000-2,500 | 2,800-plan library, ">500 unique items" tier (assumed) |
| Framatome, Curtiss-Wright, GEH, NLI/AZZ and others | 3,000-6,000 | EPRI Fig. 3-7 tiers |
| Utility in-house (Duke CRDF, Constellation, TVA, Southern, Dominion, Entergy, Vistra and others) | 6,000-15,000 | Duke handles 25-50% of fleet SR procurement in-house; ~8 large fleets at 750-2,000 each |
| **Total** | **~16,000-35,000; central ~25,000** | |

**B. Top-down from procurement**: 54 sites × 1,000-3,000 safety-related PO lines × 25-50% CGD share ≈ 13,500-81,000; geometric centre ~30,000. **C. KHNP scaling**: ~27 packages per unit a year × 94 units ≈ 2,500 packages. This is a floor, counting unique-item packages rather than jobs; US CGD use is more intensive. A and B are consistent: about **20,000-30,000 dedication jobs a year in the US**, covering several hundred thousand individual parts (Westinghouse alone does 50k).

**New-plan (new technical evaluation) creation**: Paragon writes 840-1,200 a year, about 0.65-0.9 per job, because it writes its own plans and envelopes every possible function. Westinghouse reuses a mature library, so its new-plan rate is probably 5-15% of jobs. Blended new or substantially revised plans are about 15-25% of jobs, giving **~4,000-6,000 new CGD plans/technical evaluations a year in the US**. That pool is roughly fed by ~3,000 obsolescence events a year (TVA-scaled) plus supplier or part changes **(est.)**.

**Emergent / outage-critical share**: no public figure. TVA restraint priorities of "Urgent" and "Outage", and 75% of obsolescence being found at the point of need, point to a large reactive share. Estimate **20-35% of jobs are expedited or emergent, i.e. ~5,000-8,000 a year**, concentrated in the ~60 refueling-outage windows (~100-130 per outage) plus forced-outage events. About 1,000-2,000 a year are genuine critical-path or LCO-driven items, where a day of lost generation (~$1M+ per unit-day, recalled) dwarfs the dedication fee **(est.)**.

## 7. Implications for the AI-native dedicator
- The volume pool is ~25k jobs and ~5k new plans a year in the US. New-plan engineering is where days-versus-months matters most. Paragon's ratio of ~1 new plan per job shows that some incumbents redo engineering on almost every job.
- The emergent slice (~5-8k a year) is where speed is priced. The obsolescence funnel (~3k events a year, 75% discovered reactively, 60%+ of N-qualified suppliers gone, 20-25% of components unsupported) keeps feeding it.
- Capacity is the binding constraint, not demand: Duke has a backlog and is headcount-limited, and 31% of units report rising CGD use.
- Liability tail: about 10-16 CGD-related Part 21s a year industry-wide, concentrated in breakers, relays and power supplies. CFSI cases are rare (<10 reported 2016-2021) but under-reported.

## Gaps
- No public count of safety-related POs per plant. EPRI Fig. 3-3 bins (unique CGD items per unit-year) did not survive text extraction.
- No public NUOG, PUSH or EPRI obsolescence-rate statistics; EPRI PDO/obsolescence reports are member-only.
- No Westinghouse job count (only parts), and no UCI or Framatome throughput.
