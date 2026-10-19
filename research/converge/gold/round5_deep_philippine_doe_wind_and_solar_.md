# Philippine DOE wind and solar pre-development RESCs: feasibility deep-dive (round 5, relaxed C3)

**Verdict: excluded on fit (C1–C5 = 2/2/2/1/4, 11/25).** This is a good business for a developer, but it is not a Terranox-pattern rung.

*Method note:* The shared WebSearch budget for this turn was already used up, so I ran no new searches. I checked the claims by fetching primary and secondary sources directly with WebFetch. Every number without a URL is marked **(estimate)**.

## Frame of reference
The rung is a pre-development RESC (Renewable Energy Service Contract) for one onshore wind or solar block. It runs from Certificate of Authority (COA, the DOE's early-stage permit) to a bankable package: 12+ months of met-mast or LiDAR data, P50/P90 yield, a grid study and an ECC (environmental clearance) screen.
- **Discovery is not 80%+ of the work.** The resource is already mapped in free rasters: Global Wind Atlas, ERA5 and the NREL atlas, which found about 11,055 km² of good-to-excellent windy land ([Wikipedia/NREL](https://en.wikipedia.org/wiki/Wind_power_in_the_Philippines)).
- **The binding work is execution.** It is land leases, NCIP FPIC (Indigenous consent), LGU (local government) endorsements and NGCP (grid operator) capacity. The DOE's 2024–25 terminations of 163 contracts (17.9 GW) were for non-performance, not bad resource ([eco-business](https://www.eco-business.com/ms/news/philippine-energy-department-lauded-for-clampdown-on-non-performing-renewable-energy-contracts/)).
- **Discovery share (estimate):** about 30–40% of the rung's work.

## Step-up ratio
- **Unproven price:** about $10–30k in DOE fees and application cost per contract **(estimate; the fee schedule was not retrieved)**.
- **Proven price:** no Philippine per-MW comparable is disclosed.
  - ACEN bought the remaining 60% of the 500 MW Unicorn wind project. It disclosed only that the price was "less than 10% of the book value of the Company", which is a stock-exchange disclosure threshold, not a deal price ([newsbytes](https://newsbytes.ph/2024/08/04/ayala-unit-completes-buy-out-of-500-mw-unicorn-wind-farm-project-in-quezon/)).
  - Global benchmarks for wind sites with proven resource but no permits are about $5–25k/MW. Ready-to-build projects are about $50–150k/MW **(estimate)**.
  - For a 50 MW site that gives about $0.25–1.25M. That is about **20–100x on the right and 2–6x on all-in cost**.
- **Transactions per year:** a handful of disclosed secondary trades of pre-development contracts **(estimate)**. The market is large on the primary side: 80 wind projects (29.2 GW) hold COAs ([philstar](https://www.philstar.com/business/2026/01/06/2498960/over-29-gw-wind-geothermal-projects-secure-doe-go-signal)).
- **Not immediate.** A pre-development contract can go to a non-affiliate only **once**, and only **two years after effectivity**, unless the minimum permits are already done ([GlobalComplianceNews on DC2024-06-0018](https://www.globalcompliancenews.com/2024/08/05/philippines-doe-issues-revised-guidelines-for-renewable-energy-contracts-and-developer-registration/)).

## Hit rate and proving capex, today and with ML
- **Proving cost:** about $150–400k and 12–18 months per site **(estimate)**. This passes the "expensive" test.
- **Base hit rates:** about 20–30% of sites reach bankable capacity factor and grid today, versus 40–60% for ML-picked sites. These are the candidate's own figures, **unsourced (estimate)**.
- **ML lift on the resource itself is small.** Free rasters already capture most of the wind-speed signal.
- **The plausible ML lever** is predicting grid headroom and FPIC or land risk from NGCP Transmission Development Plan data and from terminated-contract history. That gives about **1.2x on cost per proven asset (estimate)**, below the 1.5x bar.

## Data source
- **Named datasets:**
  - DOE lists of awarded, terminated and relinquished contracts (PDF and online pages; the DOE URLs I tried returned 404 at fetch time).
  - DOE work-program reports.
  - NREL Philippine wind atlas, Global Wind Atlas and ERA5 (all open).
  - PAGASA (weather agency) station records.
  - NGCP Transmission Development Plan.
  - ECC filings on the DENR-EMB portal.
- **Why parts are illegible:** work-program reports and old met data in terminated contracts are scanned and scattered.
- **The outcome is summarised.** DOE status lists record stage, termination and commerciality.
- **The regulator screens too.** REMB, the DOE's renewables bureau, designates Pre-Determined Areas (PDAs) from "sufficient available technical data" and puts them into the OCSP (Open and Competitive Selection Process) ([PDA definition](https://philippineenergylawterms.com/pre-determined-area-pda/)).
- **Incumbents screen with GIS.** ACEN, Mainstream and Citicore all do this already, so the edge from extracting data is small.

## How the right is bought
- **From whom:** it is not bought from an owner who cannot read the data. It is a **state grant**, either won through OCSP for PDAs or by direct application at fixed fees.
- **Use it or lose it:** the COA (3 years for wind, 1 year for land solar) cannot be extended ([GCN](https://www.globalcompliancenews.com/2024/08/05/philippines-doe-issues-revised-guidelines-for-renewable-energy-contracts-and-developer-registration/)).
- **Transfer:** assignment needs DOE approval, and the lock above applies.
- **Hostile regulator:** Secretary Garin publicly attacks holders who "simply hold the rights, waiting to flip them to another buyer at a premium", and threatens civil, criminal or administrative charges ([eco-business](https://www.eco-business.com/ms/news/philippine-energy-department-lauded-for-clampdown-on-non-performing-renewable-energy-contracts/)).
- **Land is a separate purchase.** Landowners must still be leased, under Filipino nationality rules.
- **Share of uplift kept:** about 100% of the sale price if a sale clears. But the realistic price is low, and a buyer will discount for the lock and the approval risk **(estimate)**.

## Capitalised buyer
- **Who:** ACEN, Aboitiz, Citicore, Mainstream, and CIP or Copenhagen Energy for larger assets. All are real and liquid.
- **They self-originate.** Mainstream got 440 MW of onshore contracts directly from the DOE, with no price paid to a third party ([renewablewatch](https://renewablewatch.in/2024/03/13/mainstream-awards-development-rights-for-440-mw-of-onshore-wind-in-the-philippines)).
- **What auctions buy:** Green Energy Auctions buy tariffs from IPPs that bring their own pipelines, not contracts from provers.

## Integration ladder above
- **The ladder:** pre-development contract, then development and permits, then financial close and EPC (construction), then owner-operator IPP, then a regional renewable platform.
- **A bigger rung:** offshore wind, with a 178 GW resource ([Wikipedia/World Bank](https://en.wikipedia.org/wiki/Wind_power_in_the_Philippines)).
- **Exit pressure:** the DOE's 35%-by-2030 renewables target sustains demand ([philstar](https://www.philstar.com/business/2026/01/06/2498960/over-29-gw-wind-geothermal-projects-secure-doe-go-signal)).

## Who else does this
- **IPP in-house origination teams:** ACEN, Aboitiz, Citicore and Mainstream.
- **Local land-bankers and contract flippers:** this is the class the DOE is now terminating. For example, Solar Philippines accounts for about 64% of terminated solar ([eco-business](https://www.eco-business.com/ms/news/philippine-energy-department-lauded-for-clampdown-on-non-performing-renewable-energy-contracts/)).
- **Global early-stage developers** that sell down at development stage, such as Mainstream's model.

## Smallest feasibility test (2 weeks)
- **What:** price discovery with buyers.
- **How:** contact BD leads at 6–8 IPPs (ACEN, Aboitiz, Citicore, Mainstream, CIP, Copenhagen Energy, Vena, and others). Ask what they would pay per MW for a 50 MW onshore contract with 12 months of LiDAR data, a P50/P90 yield and a grid study, but no land, FPIC or ECC. Assume it is 24 months old, so non-affiliate assignment is allowed.
- **Kill line:** fewer than 2 written indications above $30k/MW. Below that, all-in returns stay under 5x.
- **Optional desk check:** join DOE terminated and progressed contract lists to Global Wind Atlas data and substation distance. Then test whether any illegible feature beats that baseline by more than 0.05 AUC (a standard prediction-accuracy score).

## Verdict (relaxed rubric)
| | Score | Why |
|---|---|---|
| C1 Frame | 2 | Discovery is about 30–40% of the rung, and execution binds. |
| C2 Step-up | 2 | About 20–100x on the right and 2–6x all-in, and not immediate because of the 2-year lock. |
| C3 Hit-rate lever | 2 | Proving is expensive, but the ML lift is about 1.2x. |
| C4 Data + right | 1 | The resource data is legible, the outcome is in status fields, and the right is a fixed-fee state grant from a regulator opposed to flipping. |
| C5 Ladder | 4 | The ladder to IPP and offshore wind is clear. |
| **Total** | **11/25** | **Excluded on fit, not by hard rule.** |

**Fatal flaw:** relaxing C3 does not rescue it. Discovery is not the value-creating step. The right comes from a regulator that blocks quick flips. And capitalised buyers originate their own contracts directly from the DOE.