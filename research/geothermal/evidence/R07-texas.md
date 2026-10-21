# R07: Texas geothermal rights. Is it a cheap private-right market?

**Method note.** The shared WebSearch budget (200 per turn, across all agents) was already used up when this agent started. Every fact below comes from direct WebFetch of primary pages: Texas Legislature Online, the Texas statutes site, the RRC, a BEG/DOE report PDF parsed locally, Meta and Sage pages, and ThinkGeoEnergy. A few figures are cross-referenced from sibling evidence files (L10, L11, L18, Z07, Z09) and are labelled that way. Anything not fetched is marked (unverified).

## 1. Correction: the 2023 ownership law is SB 785, not HB 1818

- **88R HB 1818** is a county property-tax rate bill (Muñoz). It died in House Ways & Means on 03/07/2023 and has nothing to do with geothermal. https://capitol.texas.gov/BillLookup/History.aspx?LegSess=88R&Bill=HB1818
- **The geothermal ownership law is SB 785** (Birdwell; House sponsor Darby; identical companion **HB 1336**).
  - It passed with a two-thirds vote in both chambers.
  - It was **filed without the Governor's signature and took effect immediately on 18 June 2023**.
  - Senate committee vote 8-1; House Energy Resources 8-0.
  - Sources: https://capitol.texas.gov/BillLookup/History.aspx?LegSess=88R&Bill=SB785 ; https://capitol.texas.gov/tlodocs/88R/billtext/html/SB00785F.htm

## 2. What SB 785 does (Texas Natural Resources Code ch. 141)

**New § 141.004.** Unless a conveyance, deed, reservation, lease or other binding instrument says otherwise, "the geothermal energy and associated resources below the surface of land are owned as real property by" the landowner. **Where the surface and mineral estates are severed, the surface estate owner owns them.** The owner or its lessee, heir or assignee may drill and produce.

**Carve-outs in § 141.004(c):**
- The section does not apply to "minerals dissolved or otherwise contained in groundwater, including in hot brines". Lithium and other brine minerals therefore stay outside the geothermal right.
- It does not change existing law on oil, gas and mineral extraction, **dominant/servient estate rights** (the mineral estate stays dominant), or groundwater ownership and use.

**§ 141.003 definition.** "Geothermal energy and associated resources" covers "indigenous steam, hot water and hot brines, and geopressured water", plus associated heat and by-products. Oil and gas and Property Code § 75.001 minerals are excluded.

**Title insurance.** A new Insurance Code § 2703.056 lets title insurers carve out mineral-estate and geothermal exceptions. The industry therefore treats the geothermal estate as a separate, insurable interest.

Statute text with history lines: https://tcss.legis.texas.gov/resources/NR/htm/NR.141.htm

**What this means.** Before 2023, Texas title to heat in a severed estate was ambiguous. The UT/InnerSpace "Future of Geothermal in Texas" report gave ownership a whole chapter (ch. 14) for that reason (https://energy.utexas.edu/research/geothermal-texas). SB 785 gave developers a default counterparty: **the surface owner**. That person is usually a rancher or farmer who has never been paid for heat and has no comparables to price it against.

The mineral owner stays dominant, though. A geothermal lessee has to accommodate oil and gas operations, and in active basins the right is in practice subordinate to a mineral lessee's existing and future wells.

## 3. Jurisdiction: the RRC

- **§ 141.011.** "The commission [RRC] shall regulate the exploration, development, and production of geothermal energy" on public and private land.
- **§ 141.012.** The RRC must adopt rules, after consulting the GLO Commissioner and the TCEQ, for "rapid and orderly exploration, development, and production". The rules cover the environment, waste, safety and correlative rights.
- **2025 amendment.** §§ 141.012 and 141.074 were amended by **Acts 2025, 89th Leg., Ch. 986 (SB 766), eff. 1 Sep 2025**. This looks like an agency-wide clean-up, and its content was not fetched. https://tcss.legis.texas.gov/resources/NR/htm/NR.141.htm
- **Practical upshot.** Geothermal wells go through the same agency, forms and operator (P-5) system as oil and gas wells. Sage says Texas permitting takes "a few weeks" (GRC 2023 paper, via sibling L18). Other 2025 bills on shallow or closed-loop geothermal and groundwater-district exemptions are (unverified) and need follow-up.

## 4. Data: the Texas well archive

**RRC "Wells Monitored" (as of 31 Aug 2026): 431,492 oil and gas wells. 273,371 are active and 158,121 inactive.**
- Producing oil: 155,036 wells.
- Producing gas: 82,573 wells.
- Injection/disposal: 28,760 wells.
- Inactive: 87,221 are 14(b)(2)-compliant with bond/LOC, 42,444 compliant shut-in under one year, and 28,456 non-compliant.
- Source: https://www.rrc.texas.gov/media/pp4jbxif/august-2026.pdf (parsed locally)

Wells ever drilled in Texas run to well over a million (unverified; the RRC "Historical Texas Drilling Statistics 1960-2018" PDF exists but was not parsed: https://www.rrc.texas.gov/media/3yhlylo4/drill_graph_2018.pdf).

**Logs.** Well logs are public as scanned **TIFF images** in the RRC GIS viewer and Imaged Records, listed monthly since July 2006. https://www.rrc.texas.gov/oil-and-gas/research-and-statistics/obtaining-commission-records/oil-gas-well-records-gis-well-logs/ . That is the "public but illegible" condition, the same shape as Saskatchewan's assessment files: BHTs sit in log headers as images, not in a database.

**Existing compiled BHT sets (from sibling files):**
- A 2013 Texas assessment used **>50,000 BHTs**.
- UT 2023 cites "hundreds of thousands" of public borehole records.
- West Texas (Delaware/Val Verde) deep BHTs run **120-180 °C**.
- A Pecos County model gives **~195 °C at 3.5 km and ~213 °C at 5 km**.
- Sources: sibling L10, L11. https://repositories.lib.utexas.edu/items/01be6734-86ac-4892-a3f2-1c5e362b3409 ; https://corpora.tika.apache.org/base/docs/govdocs1/291/291718.html

Raw BHTs carry a well-known cold bias (mud circulation), so they need correction (Harrison/Kehle-type). ML correction is the standard modern approach (sibling L03, L09). That correction-plus-fusion step is where an edge could come from.

## 5. Gulf Coast geopressured geothermal history (DOE, 1975-1990s)

- **BEG/DOE 1989 Annual Report** (Kreitler et al., May 1990, DOE cooperative agreement DE-FC07-85NV10412):
  - Pleasant Bayou Test Well No. 2 (Brazoria Co.) measured **307 °F (153 °C) at 14,674 ft (4.47 km)**.
  - The regional gradient is about **1.7-1.8 °F/100 ft (~31-33 °C/km)**.
  - Target reservoirs were >149 °C (300 °F) geopressured Frio sands.
  - Over sustained production, bottom-hole pressure fell by less than 300 psi.
  - Source: https://www.beg.utexas.edu/files/publications/contract-reports/CR1990-Kreitler-1.pdf
- **Program scale and outcomes:**
  - DOE studied **17 wells** across Texas and Louisiana.
  - Pleasant Bayou #2 produced **~12 million bbl of brine and 231 MMcf of gas** at a BHT of about 300 °F.
  - Its hybrid plant made **~1.2 MW**. https://www.searchanddiscovery.com/abstracts/html/2007/gcags/abstracts/erdlac02.htm
  - Sibling L10 adds a flow of **~20,000 bbl/d of 291 °F brine** and power sales to HL&P.
  - DOE called it technically feasible but marginal on economics at that era's gas prices.
- Reservoir model: Riney 1991, OSTI 893428. https://www.osti.gov/biblio/893428

**Takeaway.** The Gulf Coast resource is proven to exist and to flow, but it is low-grade per well (about 1 MW). It is not the target for a land play. It matters for brine-mineral and storage optionality, and as sunk data: DOE characterised the fairways in detail and published it.

## 6. Players: Project InnerSpace and Sage Geosystems

**Project InnerSpace** is a philanthropy-funded 501(c)(3).
- It co-produced the five-university report "The Future of Geothermal in Texas" (Jan/May 2023; 15 chapters, 13 lead authors) and runs the free **GeoMap** prospecting tool. https://projectinnerspace.org/ ; https://energy.utexas.edu/research/geothermal-texas
- Its framing is that geothermal drilled at the current oil and gas drilling rate could supply up to 77% of global electricity by 2050.
- **Implication: regional screening in Texas is now a free commodity.** Parcel-level temperature and permeability plus title is not.

**Sage Geosystems** (Houston) works on "pressure geothermal" in hot dry rock at 2.5-6 km, plus EarthStore storage.
- **Funding.** **$97M Series B, 21 Jan 2026**, co-led by **Ormat ($25M)** and Carbon Direct Capital, with Nabors, Exa and others; Barclays was placement agent. https://www.thinkgeoenergy.com/sage-geosystems-closes-97-million-series-b-funding-round-to-support-pressure-geothermal-deployment/
- **Meta deal.** Up to **150 MW**, phase 1 targeted for 2027, site undisclosed. https://about.fb.com/news/2024/08/new-geothermal-energy-project-to-support-our-data-centers/
- **Texas track record.**
  - It re-entered the plugged JFB Heard 1 gas well in Starr County, TX (about 19,000 ft).
  - It built a 3 MW EarthStore facility at San Miguel Electric Co-op, TX.
  - It ran a 2025 geothermal demo at the Starr County test well.
  - Sources: https://www.sagegeosystems.com/ ; sibling L18.
- **Next commercial site.** On **22 Sep 2026** Sage picked **Ormat's Blue Mountain plant (Nevada)** for its next commercial EGS facility. https://www.sagegeosystems.com/ . Even the Texas-native geothermal champion takes its first commercial power project to a known Nevada hydrothermal field with infrastructure. Texas is being used for storage and demos, not yet for power.

## 7. Prices of Texas geothermal rights: is it cheap?

**Hard public price data for private Texas geothermal leases: none found.** No public registry, auction or index exists. Private leases are recorded in county deed records (often as memoranda without price terms), which is itself an illegibility layer (unverified).

**Public-land comparables:**
- **GLO (Permanent School Fund).** § 141.073/141.076 require **sealed-bid** leasing, and the board sets the terms. In the Nov 2022 GLO sale, **six El Paso geothermal tracts** were offered by sealed bid via EnergyNet. https://www.thinkgeoenergy.com/texas-oil-gas-and-geothermal-lease-sale-nov-2-2022/ . Sibling L10 reports El Paso terms of a **10-year primary term, $3/acre delay rental, 10% gross royalty**, and that Ormat's first state lease was about **$5/acre** (not re-verified here).
- **University Lands** manages **~2.1M acres** of surface and mineral interests in 19 West Texas counties and is "actively seeking to lease PUF lands for renewable energy". No geothermal-specific terms are published. https://universitylands.utsystem.edu/

**Inference (unverified but structurally strong).** Private Texas geothermal rights are almost certainly cheap today, for four reasons:
1. The right was legally confirmed only in June 2023.
2. Surface owners have no price comparables.
3. No cash flow attaches to it.
4. Buyers are few: Sage, Fervo-type developers, and oil-service entrants.

A single-digit to low double-digit $/acre option or bonus is plausible, against Permian oil and gas bonuses of thousands of $/acre (unverified).

**Frictions:**
- **Fragmentation.** Texas has about 95% private land (unverified), so aggregating a 5-20 km² EGS block means dozens of surface owners.
- **Mineral dominance.** Mineral lessees can drill through the block, and § 141.004(c) preserves dominant-estate law.
- **Brines go to the mineral estate.** Any lithium upside needs separate tenure.
- **Pre-2023 deeds.** "Unless otherwise expressly provided" means old deeds that reserved "all minerals and other substances" invite title disputes. Title work becomes a moat.

## 8. Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **The rights market fits the pattern: new, cheap, illegible and private.** SB 785 created a clean, ownable, insurable geothermal estate held by about 400k scattered surface owners, with no price discovery. That is closer to Terranox's "buy before proof" than BLM, where nominations are public and auctions competitive (see R01-R03).
2. **The data fits too.** There are 431k monitored wells, more than a million drilled historically (unverified), and logs held as **TIFF scans**. BHTs, mud weights (geopressure) and DST permeability sit in images. ML-based OCR, BHT correction and temperature × permeability fusion, mapped onto **surface-parcel ownership**, is a real "illegible public data → mispriced right" engine. Free GeoMap removes regional screening as a moat but does not touch parcel-level title plus temperature.
3. **The weakness is the grade of the asset, not the right.** Texas sedimentary heat is moderate (31-33 °C/km on the Gulf Coast; 120-200+ °C at 3.5-5 km in the Delaware/Val Verde). Commercial power there is an **EGS or deep sedimentary** bet that depends on Fervo/Sage-style costs falling. Under the standing "assume the tech works" rule this does not kill the idea. If EGS gets cheap, the value of hot, permittable, ERCOT-connected, data-centre-adjacent parcels steps up without the rights holder drilling.
4. **Exit buyers exist and are funded.** They include Sage ($97M, Ormat-backed, Meta 150 MW), Fervo, Ormat, oil majors and service firms (Nabors), and ERCOT data-centre developers. Fast RRC permitting (weeks) makes a proven Texas parcel more liquid.
5. **The gap vs Zanskar.**
   - Zanskar's disclosed land is about 50k acres of **BLM leases in Nevada** plus Lightning Dock, NM (Z04). It is a **hydrothermal developer** that drills and operates.
   - It has **no disclosed Texas or private-fee position**, and its physics and ML stack is tuned to Great Basin blind convective systems, not sedimentary or EGS conduction plays.
   - The open seam is a **rights aggregator and prospect generator**: ML over RRC log images plus county title records, quietly leasing or optioning surface-owner geothermal estates (with bundled brine-mineral and pore-space options where possible) in the hottest Delaware/Val Verde, South Texas and East Texas fairways. It would then sell or farm out to EGS developers and hyperscalers.
   - Zanskar is structurally poorly placed to do this. It would be supplying its competitors, and its tooling and land team are BLM-oriented.
6. **Scoring caveats.**
   - Texas alone may be a slower-burning asset class than Nevada hydrothermal. Value depends on EGS cost curves and buyer demand, not on a blind 150 °C+ convective discovery.
   - Best as **one of several jurisdictions** (Texas + Williston/Saskatchewan + Alberta) in a "sedimentary-basin geothermal land bank".
   - Title fragmentation and mineral-estate dominance are the real execution risks. They are also the reason the right is cheap.

## Sources

- https://capitol.texas.gov/BillLookup/History.aspx?LegSess=88R&Bill=HB1818
- https://capitol.texas.gov/BillLookup/History.aspx?LegSess=88R&Bill=SB785
- https://capitol.texas.gov/tlodocs/88R/billtext/html/SB00785F.htm
- https://tcss.legis.texas.gov/resources/NR/htm/NR.141.htm
- https://www.thinkgeoenergy.com/new-texas-legislation-defines-ownership-of-geothermal-energy/
- https://www.thinkgeoenergy.com/texas-oil-gas-and-geothermal-lease-sale-nov-2-2022/
- https://www.rrc.texas.gov/media/pp4jbxif/august-2026.pdf
- https://www.rrc.texas.gov/oil-and-gas/research-and-statistics/obtaining-commission-records/oil-gas-well-records-gis-well-logs/
- https://www.rrc.texas.gov/media/3yhlylo4/drill_graph_2018.pdf
- https://www.beg.utexas.edu/files/publications/contract-reports/CR1990-Kreitler-1.pdf
- https://www.osti.gov/biblio/893428
- https://www.searchanddiscovery.com/abstracts/html/2007/gcags/abstracts/erdlac02.htm
- https://energy.utexas.edu/research/geothermal-texas
- https://projectinnerspace.org/
- https://www.sagegeosystems.com/
- https://www.thinkgeoenergy.com/sage-geosystems-closes-97-million-series-b-funding-round-to-support-pressure-geothermal-deployment/
- https://about.fb.com/news/2024/08/new-geothermal-energy-project-to-support-our-data-centers/
- https://universitylands.utsystem.edu/
- https://repositories.lib.utexas.edu/items/01be6734-86ac-4892-a3f2-1c5e362b3409
- https://corpora.tika.apache.org/base/docs/govdocs1/291/291718.html
