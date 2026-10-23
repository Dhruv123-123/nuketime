# H08: Sensing lithium, bromine, iodine and heat in produced water and SWD streams

Note: the shared web-fetch and web-search budgets ran out partway through this slice. Facts I could check against fetched pages carry URLs. Facts from search-result titles only, or from memory, are marked "(unverified)" or "(title only)".

## Summary

- The flow is huge and it is already piped. The Permian made more than 20M bbl/day of produced water in 2024, heading past 26M by 2030 ([JPT](https://jpt.spe.org/twa/balancing-growth-and-risk-why-water-management-is-the-permian-basins-biggest-challenge)). Most of it goes through gathering lines to SWD wells at $0.25 to $1/bbl.
- Public brine chemistry is thin. The USGS Smackover ML model had to predict lithium at about 1.5 mi² cells from a small sample set. Its in-place estimate spans almost 4x (5.1 to 19.0 Mt Li) ([USGS FS 2024-3052](https://pubs.usgs.gov/publication/fs20243052/full)). The input data is the limit, which is the same pattern seen in geothermal.
- Buyers are real and paying. Exxon paid more than $100M for about 120,000 Smackover acres from Galvanic, so at least about $833/acre ([Daily Upside](https://www.thedailyupside.com/industries/energy/exxonmobil-breaks-into-the-lithium-market-with-arkansas-land-purchase/)). Chevron bought about 125,000 net acres from TerraVolta and ETNR (price not disclosed) ([OGJ](https://ogj.com/energy-transition/article/55297744/chevron-enters-us-lithium-sector-with-leasehold-acquisitions)). Equinor holds 45% of Standard Lithium's projects.
- The right is the weak leg. In Arkansas, lithium is unitized and royalty is set by the state (2.5%, Reynolds Unit, May 2025) ([Arkansas Advocate](https://arkansasadvocate.com/2025/05/29/arkansas-oil-and-gas-commission-approves-first-lithium-royalty/)). In Texas, the Supreme Court held in 2025 that produced water belongs to the oil and gas lessee (*Cactus Water v. COG*) ([Liskow, title only](https://www.liskow.com/insights/texas-supreme-court-rules-produced-water-belongs-to-lessees-102lyzu/)). So in the Permian the water owner is the E&P, not a cheap third party.
- Best play: a sensor network clipped onto SWD and gathering lines that maps Li, Br, I, Sr and temperature by source well over time. It is a data moat that midstream water companies will host, because it turns their waste stream into a mineral option they can sell. The cheap asset is a mineral royalty or offtake option on that water, plus brine leases in the unproven fringes (East Texas, Mississippi and Alabama Smackover) that our data de-risks first.

## Key facts

- **Permian volumes:** more than 20M bbl/d in 2024, more than 26M by 2030. Trucking costs up to $2.50/bbl, disposal $0.25 to $1/bbl, recycling $0.15 to $0.20/bbl ([JPT](https://jpt.spe.org/twa/balancing-growth-and-risk-why-water-management-is-the-permian-basins-biggest-challenge)). At $0.50/bbl that is about $3.6B/yr spent on disposal.
- **Permian lithium value:** Enverus estimated Delaware Basin wastewater could yield about 225,000 t/yr LCE, worth about $19B, built from "academically sourced" concentrations and no sample count was given ([Global Mining Review](https://www.globalminingreview.com/mining/16122022/enverus-uncovers-direct-lithium-extraction-potential-in-the-permian-basin/)). Typical Permian Li is about 20 to 60 mg/L (unverified). That is low grade, but the volume is enormous.
- **Smackover:** Li runs about 1 to 477 mg/L across the Gulf Coast, and many SW Arkansas wells exceed 100 mg/L. 1960s reports above 500 mg/L could not be verified. In-place lithium is 5.1 to 19.0 Mt in southern Arkansas ([USGS FS 2024-3052](https://pubs.usgs.gov/publication/fs20243052/full); [PMC paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11430454/)). Standard Lithium reports East Texas Smackover samples above 600 mg/L (unverified).
- **Marcellus:** a Pittsburgh/NETL study (Mackey et al., 2024) says Pennsylvania produced water could meet about 40% of US lithium demand ([Interesting Engineering, title](https://interestingengineering.com/energy/pennsylvania-wastewater-could-meet-40-of-us-lithium-needs-study); [NETL slides](https://netl.doe.gov/sites/default/files/netl-file/24RS_CMM_Mackey.pdf)). The data came from operator reports to PA DEP. The median is near 100 mg/L (unverified).
- **Bakken:** Li is roughly tens of mg/L, with very high TDS (unverified).
- **Public chemistry database:** the USGS National Produced Waters Geochemical Database v3.0 (Dec 2023) is still provisional ([data.gov](https://catalog.data.gov/dataset/u-s-geological-survey-national-produced-waters-geochemical-database-ver-3-0-december-2023)). It holds on the order of 100,000+ samples, mostly major ions. Only a small fraction report Li, Br or I, and many are decades old with no timestamp tied to current production (unverified count).
- **Arkansas right:** the AOGC set a 2.5% royalty for SWA Lithium (Standard plus Equinor) in the Reynolds Unit, rejecting the 1.82% offered. The project costs more than $1B and has $225M in DOE funding ([Arkansas Advocate](https://arkansasadvocate.com/2025/05/29/arkansas-oil-and-gas-commission-approves-first-lithium-royalty/)). Arkansas pools lithium by unit, so holdouts get the state rate. That caps the upside of a small lease but also floors it.
- **Texas right:** the RRC adopted brine mining rule 3.82 (effective Feb 18, 2025), and it excludes produced water. SB 1763 (2025) would give brine minerals to the mineral estate ([V&E](https://velaw.com/insights/brine-time-texas-latest-in-lithium-law)). *Cactus Water* gives produced water to the oil and gas lessee ([Texas Tribune, title](https://www2.texastribune.org/2025/07/01/texas-supreme-court-produced-water-oil-gas)).
- **Buyers:** Exxon (Saltwerx, 120k ac), Chevron (125k ac), Equinor (45% of SWA/East Texas, about $160M, unverified), and Koch (Koch Strategic Platforms invested about $100M in Standard Lithium in 2021, unverified). Others include EnergyX, Albemarle (Magnolia, AR) and Smackover Lithium.
- **Sensors:** LiVision (Fraunhofer IPM) is an optical inline lithium monitor built for geothermal brine DLE ([Fraunhofer PDF, title](https://www.ipm.fraunhofer.de/content/dam/ipm/en/PDFs/product-information/PK/OOA/LiVision-lithium-monitoring.pdf)). Metrohm sells online ion chromatography for Li in brine ([Metrohm AN-PAN-1058, title](https://www.metrohm.com/content/metrohm/en/applications/application-notes/prozess-applikationen-anpan/an-pan-1058.download.pdf)). Lilac publishes that brine analysis is "harder than it looks", with lab-to-lab scatter ([Lilac](https://lilacsolutions.com/news/the-lithium-needle-in-the-haystack-why-brine-analysis-is-harder-than-it-looks)). Li ISEs suffer Na interference at about 100,000x Na:Li, and MXene-coated ISEs are a research fix ([PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10795166/)). Rough prices: a process IC is about $60k to $120k installed, a lab ICP-OES about $50k to $100k, and a Li ISE probe about $500 to $1,500 (all unverified).

## Hardware design sketch

**What we build:** a skid-mounted "brine node" on the SWD intake manifold or gathering trunk. It has:
1. A slipstream sampler with a 1 µm filter and pressure letdown.
2. An inline temperature and conductivity probe.
3. An auto-sampler that drops a 10 mL aliquot into a sealed vial every 6 to 24 hours, linked to the meter ticket (which trucks or wells fed the line).
4. On larger nodes, a compact LIBS head or online IC measures Li, Br, Sr, K and B on site.
5. An ISE array (Li, Br, I) for trend data between calibrated reads.
6. LTE or satellite backhaul, solar power.

Vials from small nodes go to a central lab for ICP-MS once a week. The key ML trick is unmixing: a node sees blended water from many wells, so we combine flow-allocation tickets with isotope and minor-ion fingerprints (Sr, B, Br/Cl) to back out chemistry per well and per formation.

**Cost (unverified estimates):**
- Basic node (sampler, T/EC, ISE, telemetry): BOM about $8k to $15k. At scale about $5k.
- LIBS or online-IC node: about $60k to $120k.
- Lab ICP-MS: about $40 to $80 per sample.
- Install: about $3k to $10k per site with operator crews.
- A 50-node Permian network plus 5 analyzer nodes: about $1.5M capex plus $0.5M/yr lab and operations.
- Coverage: a large SWD gathering system (for example 1M+ bbl/d, hundreds of wells) is visible from about 20 to 40 nodes.
- Time to a working prototype: 3 to 4 months with off-the-shelf parts.

## What data it unlocks that is not public

- Time-resolved, well-allocated Li, Br, I and temperature for the water actually flowing today. Public data is static, sparse and mostly major ions.
- Formation-level maps of Li grade from deep Delaware and Midland zones (Wolfcamp, Bone Spring, Devonian, Ellenburger SWD zones) and East Texas Smackover. Nobody samples these routinely, because disposal does not need it.
- Heat: wellhead and line temperatures by zone feed the geothermal heat-rights thesis, in the same network.
- Incumbents miss this because E&Ps treat water as a cost centre, and midstream water firms (Aris, now under Western Midstream, WaterBridge, NGL, Select) sample only for scaling and compliance. DLE companies sample only their own acreage. Enverus models are built on the same public points.

## How it compounds into owned assets

1. **Permian:** sign mineral offtake or royalty agreements with SWD and midstream operators. Pay nothing up front; take a share of lithium value from their water. We then aggregate the best-grade streams and sell that aggregated supply to a DLE operator or to Exxon or Chevron. *Cactus Water* means the E&P or its water contractor owns the water, so our "right" is a contract, not a lease. The step-up is a firm, measured multi-year Li supply versus a vague option.
2. **Smackover fringes** (East Texas, Mississippi, Alabama, north Louisiana): lease brine or mineral rights where our wellhead sampling shows grade before the majors arrive. Lease bonuses there are likely tens to low hundreds of dollars per acre (unverified). Then sell to Exxon, Chevron or Equinor at the observed about $833+/acre bar. That is a 5 to 20x step-up on proven-grade acreage.
3. The same network proves bromine and iodine streams (Albemarle and ICL buy bromine) and hot zones that feed the heat-rights bank.

## Risks and kill conditions

- **Grade:** if Permian Li is consistently below about 30 mg/L, DLE economics fail there. Then the Permian network only feeds geothermal and fringe Smackover use.
- **Ownership:** E&Ps may keep mineral value to themselves after *Cactus*. Water midstream contracts may already assign mineral rights. Kill if 3 of the top 5 water midstreams refuse the data-for-revenue-share deal.
- **Arkansas** state-set royalty and unitization cap lease upside.
- **Copying:** majors could just sample their own wells. Our edge is breadth across operators, which needs early exclusivity.
- **Lithium price:** a lithium price slump (the 2023 to 2025 type) stalls buyers.
- **Sensor accuracy:** ISE drift in brine above 200,000 mg/L TDS. The mitigation is to rely on lab calibration of the vials.

## Who lets us install, and why

- **SWD and water midstream operators** (WaterBridge, NGL, Aris/Western, Select, Deep Blue): they get free scale and corrosion data, plus a revenue share on minerals in water they already handle. This is the most likely yes.
- **Small E&Ps:** they get free produced-water chemistry for scale control and a possible lithium upside.
- **Arkansas and East Texas salt water operators:** existing brine (bromine) gathering and old Smackover oil field disposal.

## Cheapest first test

- **Cost and time:** about $25k and 30 days.
- **Steps:** buy 100 vial samples from 3 cooperating SWD operators through a field technician, spanning Delaware, Midland and East Texas, at about $150 each for collection plus ICP-MS. Also test 2 commercial Li ISEs and one rented portable XRF/LIBS on splits.
- **Pass bar:** at least 15% of streams have Li of 60 mg/L or more, or the samples reveal a mapped anomaly absent from the USGS PWGD. The ISE must read within ±20% of ICP-MS after Na correction, and at least 1 operator must sign a sampling-plus-revenue-share LOI.

## Sources

- JPT, Permian water: https://jpt.spe.org/twa/balancing-growth-and-risk-why-water-management-is-the-permian-basins-biggest-challenge
- USGS FS 2024-3052: https://pubs.usgs.gov/publication/fs20243052/full
- USGS/PMC Smackover ML: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11430454/
- USGS PWGD v3.0: https://catalog.data.gov/dataset/u-s-geological-survey-national-produced-waters-geochemical-database-ver-3-0-december-2023
- Arkansas royalty: https://arkansasadvocate.com/2025/05/29/arkansas-oil-and-gas-commission-approves-first-lithium-royalty/
- Exxon/Galvanic: https://www.thedailyupside.com/industries/energy/exxonmobil-breaks-into-the-lithium-market-with-arkansas-land-purchase/
- Chevron: https://ogj.com/energy-transition/article/55297744/chevron-enters-us-lithium-sector-with-leasehold-acquisitions
- Texas brine law: https://velaw.com/insights/brine-time-texas-latest-in-lithium-law
- Cactus Water: https://www.liskow.com/insights/texas-supreme-court-rules-produced-water-belongs-to-lessees-102lyzu/
- Enverus Permian Li: https://www.globalminingreview.com/mining/16122022/enverus-uncovers-direct-lithium-extraction-potential-in-the-permian-basin/
- NETL Marcellus: https://netl.doe.gov/sites/default/files/netl-file/24RS_CMM_Mackey.pdf
- Fraunhofer LiVision: https://www.ipm.fraunhofer.de/content/dam/ipm/en/PDFs/product-information/PK/OOA/LiVision-lithium-monitoring.pdf
- MXene Li ISE: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10795166/
- Lilac on brine analysis: https://lilacsolutions.com/news/the-lithium-needle-in-the-haystack-why-brine-analysis-is-harder-than-it-looks
- Standard Lithium SEC filings: https://www.sec.gov/Archives/edgar/data/1537137/000117184325003511/exh_991.htm
