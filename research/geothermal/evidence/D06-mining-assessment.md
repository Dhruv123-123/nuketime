# D06: Mining assessment files and mineral-exploration drill data as a geothermal signal

*Research note, 2026-10-21. **Method caveat:** this agent started after the shared WebSearch budget was used up. Everything below comes from direct fetches of primary pages (OSTI, the NREL/NLR report PDF that I text-extracted, GDR, BC and WA government pages, Saskatchewan's SMAD page, Crossref metadata) and from sourced material in sibling files (L02, L16, D03, R04, Z03). Several targets could not be fetched: NBMG (503), SARIG (403), the Ontario AFRI pages (404), NRCan GEOSCAN (DNS failure) and OpenAlex (429). Anything I could not confirm is marked (unverified).*

## 1. Bottom line

- **The signal is real and has already found plants.** At least three operating Nevada plants started from **mineral-exploration holes**: McGinness Hills, Blue Mountain and Don A. Campbell. Tungsten Mountain is a likely fourth (S4 in L02). They add up to about 250 MW nameplate.
- **In all three documented cases, someone read the mining data and then took the geothermal right before proof.** Two were competitive BLM auctions and one was a non-competitive BLM lease. The data and leases were later sold on. This is the Terranox loop.
- **The archive geography is inverted.**
  - Canada (BC ARIS, Ontario AFRI, Saskatchewan SMAD) and Australia (WAMEX, SARIG) have exactly the legally mandated, time-released assessment archives that Terranox exploits. But they sit mostly on cold cratons or in places where geothermal economics have failed.
  - **Nevada has the geothermal resource but no assessment-report filing duty for federal mining claims.** The $100/yr assessment-work rule was replaced by a maintenance fee around 1992-93. Mining-hole temperatures are therefore mostly *private*.
  - So the US version of the play is **data acquisition from claim holders and directional-survey contractors plus text-mining the NBMG/county archives**, not a single SMAD-style public dump.
- **No published ML work** fuses mineral-hole temperatures or mining-report text into geothermal favorability, as far as I could find. The closest pieces are text mining of WAMEX reports for mineral content (GeoDocA, 2019), USGS ML favorability for geothermal (Mordensky et al., 2021-23), and the NREL keyword-query exercise (2022). This gap is open.

## 2. Primary evidence: Nevada (the resource side)

### 2.1 NREL "Mining G.O.L.D." (Levine, Rhodes and Kvien, 2022; NREL/TP-6A20-81946, OSTI 1855781)

This is the key primary source. I extracted the PDF text from https://docs.nlr.gov/docs/fy22osti/81946.pdf.

**Drilling volumes**
- "The mining industry drills **more than 2,000 holes in Nevada per year** to depths similar to those of temperature gradient holes." Over the same period, "the geothermal industry drilled **only 31 wells in Nevada in 2017**," and many of those were development wells (p. ~23, citing NBMG's John Muntean).
- On raw borehole count, mining is therefore the dominant exploration driller in the Great Basin by about 60x (calculated).

**No reporting rule**
- "Few measured temperatures are found in publicly available mining databases."
- Mineral exploration holes are not covered by the NDWR well-driller reporting form.
- "Mineral exploration companies are **not required to notify the state of Nevada if they encounter hot fluid**, and there is **no requirement to collect a temperature log**."

**Hidden temperature record in directional surveys**
- Most angled mineral holes are surveyed, and survey tools carry internal temperature sensors. That gives an unequilibrated T-z record that is "infrequently analyzed."
- "Directional survey providers likely possess a **vast database** of unequilibrated subsurface temperature data … which is **proprietary**."
- NREL got access from one claim holder to deviation surveys at a central-Nevada prospect. The data showed temperatures rising with depth across the prospect (Fig. 1). Sibling file L16 reports 74 holes, a 151 °F maximum and a gradient of about 10.5 °F/100 ft, against a background of about 2-3 °F/100 ft.

**Text cues in public files**
- "steam, geysering, hot pipe, increased mud temperatures, artesian flow, and boiling."
- Old hydrothermal-silica terms: "opal, chalcedony, sinter, amorphous, siliceous, quartz, fiorite, perlite, amatite, geyserite."
- NREL queried public databases for this vocabulary and "successfully identified **several prospective areas** … **not previously well known** to the geothermal community." It does not name them.

**Public databases listed**
- NBMG Great Basin Science Sample and Records Library, the NBMG Mining District Database, and NBMG Mineral Industry and Exploration Reports.
- County mineral reports and the Anaconda Mining Database (University of Wyoming).
- USGS core libraries (Mercury NV and Denver) and USGS MRDS.
- University of Utah EGI catalog, the UGS core database, the National Mine Map Repository, and NURE geochemistry (usable for geothermometry).

**Geologic association**
- Epithermal deposits younger than about 7-10 Ma are spatially associated with active geothermal systems (citing Coolbaugh et al., 2005, GRC Trans. 29).
- Alteration age is therefore itself a feature.

**Dewatering wells are a separate signal**
- Dewatering fluids "often [have] elevated temperatures."
- Barrick Goldstrike and Meikle dewatering wells are "constructed similarly to typical full-sized geothermal wells."

**Economics**
- GETEM scenarios that reuse mining data cut LCOE from **$87/MWh (BAU)** to **$65-67/MWh on BLM land** and **$62-65/MWh on private land**. That is the headline 23-29% reduction.
- Diesel at remote mines comes in at $109-185/MWh.

**Case histories (verbatim facts from §4)**

| Plant | How the mining data found it | How the right was taken |
|---|---|---|
| **McGinness Hills** (Ormat, Lander Co.) | Anaconda drilled 4 holes (1982) and FMC 12 RC holes (1984); both hit hot water. In 2004 Newcrest found **190 °F water at 980-1,200 ft**, saw geysering, and got silica geothermometry up to **346 °F**. | Ormat reviewed the mining data and won the BLM leases at a **competitive auction in Aug 2007**. Exploration was permitted in 2009 and the plant opened in 2012. It is about 160 MW today (L02). |
| **Blue Mountain** (Humboldt Co.) | Epithermal-gold drilling hit hot water in the early 1990s. | The mining company **took the BLM geothermal leases non-competitively**, presented the find at GRC in 1991, then **sold the leases plus data** to a geothermal developer. The plant is 49.5 MW nameplate and about 38 MW net, and came online in 2009. |
| **Don A. Campbell** (Ormat, Mineral Co.) | There were no surface features. Early-1990s mining holes showed **140-190 °F fluids and 203 °F vapour over about 46 km²**, plus propylitic alteration in Quaternary rocks. A mining-industry aeromagnetic survey showed a 4 × 1.5 km magnetic low. | Ormat reviewed the mining data **"at no cost"**, nominated the land in 2001 and won it at a BLM auction in Aug 2007. The plant is 42 MW and opened in 2013. |
| **Florida Canyon** (Pershing Co.) | Mine water-supply wells flowed **160 gpm at 223 °F**, giving more than 500 kW of heat. | It ran two 50-kW ORCs in 2013-14 and was then decommissioned after an ownership change and scaling problems. |

### 2.2 Blue Mountain follow-up: proof and value

- **Proof:** DOE GRED II funded Deep Blue No. 2 (2004), a step-out sited from shallow-hole gradients. It cored to 1,128 m and found a **permeable fracture zone at 500-750 m measuring 150-167 °C**, with fracture evidence of past fluids above 200 °C (OSTI 890022).
- **Discovery hole:** Deep Blue No. 1 (Fairbank and Niggemann, SAND2004-3115C, OSTI 957242) is the slimhole discovery.
- **Value:** Ormat bought the operating Blue Mountain plant from Cyrq for **$88.7M** in June 2025 (Ormat 10-Q, via R04).
- **Chain:** gold holes → non-competitive lease → data and lease flip → GRED cost-share → plant → resale.

### 2.3 Other US mining-district thermal data

- USGS Bulletin 1172 (1963), *Measuring geothermal gradients in drill holes less than 60 feet deep, East Tintic district, Utah* (doi:10.3133/b1172), shows that the USGS used mining-district holes for gradients very early.
- **The NREL GDR submission 1279** (doi:10.15121/1764505) publishes the "Geothermal Locatable Mining – Public Data Sources" spreadsheet and the TEA workbook (CC-BY). That is a ready-made seed list for an ingestion pipeline.
- **The ORNL/LBNL/NREL mine-land report** (2023, OSTI 1996689) counts **more than 17,000 US mine-land sites**. It notes that geothermal systems "have been discovered while in search for epithermal mineral resources." It does not count geothermal-prospective sites.

## 3. Assessment-file archives outside the US (the data side)

| Archive | Size | Confidentiality / release | Drill and temperature content | Geothermal relevance |
|---|---|---|---|---|
| **BC ARIS** | **41,760 approved reports** as of 21 Oct 2026; filing began in **1947** | **1 year** from work registration | Drill logs, geophysics and "as-is" digital data attached to reports. There is no structured temperature field (unverified). | The Cordillera and the Garibaldi/Meager volcanic belt are hot. GSC heat-flow work in the Cordillera (Bentkowski and Lewis, *Heat flow determinations in the Cordillera: 1988-1992*, doi:10.4095/194841) is believed to have used existing mineral holes (unverified). BC geothermal tenure is by public tender and is lumpy (R11). |
| **WA WAMEX** | Count not stated on the page | **5-year sunset**; holders can object for up to 5 more years per objection | GSWA publishes **harmonised drillhole and surface geochemistry extracted from WAMEX reports**, with bulk updates every May and November. That shows the state itself already runs the "make reports legible" step. | WA is mostly cratonic. GSWA compiled temperature and heat-flow data for geothermal (Ghori, 2011, *Preview* 153, doi:10.1071/pvv2011n153p31). The Perth Basin is low-enthalpy. |
| **Saskatchewan SMAD** | Count not stated on the page | Files enter the database "as they come off-confidential" (the Terranox premise is 3 years) | Categories listed are reports, digital submissions, maps and sections, and misc. Surveys are airborne, ground and underground. There is no temperature category. | Saskatchewan is cold Shield in the north. Its sedimentary-basin geothermal (Williston, DEEP) draws on O&G wells, not SMAD. |
| **Ontario AFRI** | Not fetched (404) | (unverified) | Shield drill holes | Shield heat flow is low. Jessop (1978, *Tectonophysics*, doi:10.1016/0040-1951(78)90199-3) and Čermák (1971-72) measured Superior Province heat flow, historically in mineral-exploration holes (unverified detail). Relevance is mine-water and direct-use only. |
| **SA SARIG** | Not fetched (403) | (unverified) | Mineral, petroleum and geothermal drillholes in one system (unverified) | The Australian hot-rock boom (Geodynamics, Petratherm and others) drilled to more than 4 km. Habanero's 1 MWe pilot reached 215 °C and ran for 160 days in 2013, then was abandoned as uneconomic (Wikipedia). The heat is real and the economics failed. |
| **Australia OZTemp** (GA) | Not fetched | Public | A BHT compilation, mostly petroleum and water bores (unverified). It is used in ML transfer tests (L09). | Baseline only |

**Reading:** the Commonwealth archives are the most SMAD-like and the most machine-readable. WAMEX even has state-harmonised drillhole tables. But geography caps their geothermal value: cold Shield and craton, or a jurisdiction where EGS economics already failed. **BC is the only one with a real high-enthalpy overlap**, and its tenure system is tender-gated and politically sensitive.

## 4. ML and NLP on mining files

| Work | What it does | Relevance |
|---|---|---|
| Holden et al. 2019, **GeoDocA**, *Ore Geology Reviews* (doi:10.1016/j.oregeorev.2019.05.005) | Text mining of WA mineral exploration reports to surface geological content quickly | Shows the WAMEX corpus is tractable to NLP. It was applied to minerals, not heat. |
| Qiu et al. 2023, *Ore Geology Reviews* (doi:10.1016/j.oregeorev.2022.105278) | Geological profile-text association in exploration reports | Same idea |
| Mordensky et al. 2021, GSA abstract (doi:10.1130/abs/2021am-365177); 2023 *Geothermics* (L16) | Data-driven ML geothermal favorability for the western US | Limited by features and labels: new temperature points are the binding input |
| Mineral-prospectivity ML (many papers, e.g. epithermal-Au MPM, EGU 2025) | Positive/negative label ML on geology, geochemistry and geophysics | The methods transfer directly. Epithermal-Au MPM is half a geothermal model, given the less-than-7-10 Ma Au-geothermal association. |
| NREL 2022 (above) | A manual keyword query of public mining databases that found new prospective areas | Proof of concept for LLM extraction. Nobody has scaled it (unverified). |

I found **no paper** that extracts temperature, hot-water or steam mentions from assessment reports at scale. I also found no paper that ingests directional-survey tool temperatures into a geothermal model. Both are open.

## 5. Hard numbers

- More than **2,000** mining holes per year in Nevada, against **31** geothermal wells in 2017 (NREL 2022).
- Nevada hydrothermal potential is about **5,755 MWe**, of which about **10%** is developed (Ayling 2020, via NREL). NREL also puts Nevada's undiscovered geothermal at more than **3,000 MW**.
- Up to **75%** of Great Basin systems may be blind (NREL, citing Coolbaugh 2006).
- Mining-hole discoveries: McGinness (about 160 MW), Blue Mountain (49.5 MW), Don A. Campbell (42 MW), and Tungsten Mountain (24-26 MW, L02).
- Measured mining-hole temperatures:
  - **190 °F** at 980-1,200 ft and a geothermometer of 346 °F (McGinness);
  - **203 °F** vapour over 46 km² (DAC);
  - **223 °F** at 160 gpm (Florida Canyon);
  - 150-167 °C at 500-750 m in the follow-up slimhole (Blue Mountain).
- Mining-data LCOE is **$62-67/MWh vs $87/MWh** (a 23-29% reduction).
- BC ARIS holds **41,760** reports with a **1-yr** confidentiality period. WAMEX has a **5-yr** sunset.
- Blue Mountain resale was **$88.7M** (2025).

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **The thesis has a documented track record.** Three to four Nevada plants (about 250-275 MW) came from mineral holes. Each time, the party that *read the mining data first* got the right:
   - Noramex/Blue Mountain took a non-competitive lease and flipped it with the data;
   - Ormat bought Don A. Campbell after reviewing data it got "at no cost," then nominated the land;
   - Ormat won the McGinness auction.

   This was done ad hoc, one site at a time, decades apart. Nobody has systematised it. The loop is Terranox's loop.
2. **The US data is private and scattered, not public and centralised.** There is no SMAD for Nevada mining. The scalable edge is therefore three things:
   - **(a) Data deals.** License or buy hole files, deviation-survey temperatures and dewatering logs from the roughly 2,000-holes-per-year Nevada mining industry and its survey contractors. Pay in cash, a geothermal ORRI, or a carried interest to the claim holder. NREL says this data sits unanalysed and miners could "monetize" it.
   - **(b) LLM extraction over the public NBMG, county, MRDS and Anaconda archives,** using NREL's thermal vocabulary.
   - **(c) Feature fusion,** adding epithermal alteration age and mineral-prospectivity outputs as geothermal features.

   Any one of these gives temperature points nobody else holds. Per Mordensky, those points are what limits geothermal ML.
3. **Gap vs Zanskar.** Zanskar's public story is physics and AI, its own geophysics and TG drilling, and digitised "analog data sets" (Z03). It **does not publicise mining-assessment files, deviation-survey temperatures, or data deals with claim holders**. This is (unverified) as to its internal practice. The mining-data channel is cheaper per temperature point than Zanskar's own field acquisition, and it is the channel that historically found blind plants. A Terranox-shape company can build a moat Zanskar would have to copy: *exclusive* hole-data licenses with mining companies.
4. **Legal fit.** A mining claim does not block a BLM geothermal lease, since the two are separate estates (see R13). A miner who sees hot water can, as at Blue Mountain, take the geothermal lease directly. A partnership in which the Terranox-shape company files the lease or nomination and the miner keeps a royalty is therefore workable. The BLM nomination-to-auction lag (DAC took 2001 → 2007) is the main timing risk (R03).
5. **The international archives are a secondary lane.** BC ARIS (41,760 reports, 1-yr release) is the best SMAD-analog with real heat, but tender-gated tenure limits a land grab there. WAMEX, SMAD and AFRI are cold or uneconomic for power. Their best use is as **training corpora for the extraction model** (GeoDocA shows WAMEX is NLP-ready) and for direct-use or mine-water niches.
6. **Scoring.**
   - **Not too small:** about 3 GW+ of undiscovered resource in Nevada alone, and roughly 30 GW undiscovered US hydrothermal (USGS, via L16).
   - **Owns the asset:** the right is taken before proof, the same as Terranox.
   - **Untested lift:** the ML lift from mining data is untested but plausible. NREL's manual keyword pass already found new areas.
   - **Main risk:** a data-access cost and velocity race with Zanskar and the 2024-26 crowd of BLM bidders (Z04). This argues for locking up exclusive mining-data partnerships early, before the auction market prices them in.

## Sources

- NREL (now NLR), Levine, Rhodes and Kvien 2022, *Mining G.O.L.D.*, NREL/TP-6A20-81946: https://docs.nlr.gov/docs/fy22osti/81946.pdf ; https://www.osti.gov/biblio/1855781
- Levine and Rhodes 2021, SME conference: https://www.osti.gov/biblio/1815395
- GDR 1279, mining public data sources and TEA: https://gdr.openei.org/submissions/1279
- Deep Blue No. 2, Blue Mountain (2005), OSTI 890022: https://www.osti.gov/biblio/890022
- Fairbank and Niggemann 2004, Deep Blue No. 1, OSTI 957242: https://www.osti.gov/biblio/957242
- ORNL/LBNL/NREL 2023, *Clean Energy Technology Applications on US Mine Land*: https://www.osti.gov/biblio/1996689
- BC ARIS search (report count): https://apps.nrs.gov.bc.ca/pub/aris/
- BC assessment reports page (1947 start, 1-yr confidentiality): https://www2.gov.bc.ca/gov/content/industry/mineral-exploration-mining/british-columbia-geological-survey/assessmentreports
- WA WAMEX page (5-yr sunset, harmonised drillhole geochem): https://www.wa.gov.au/node/29535/
- Saskatchewan SMAD: https://www.saskatchewan.ca/business/agriculture-natural-resources-and-industry/mineral-exploration-and-mining/saskatchewan-geological-survey/saskatchewan-mineral-assessment-database-smad
- Holden et al. 2019, GeoDocA: https://doi.org/10.1016/j.oregeorev.2019.05.005
- Qiu et al. 2023: https://doi.org/10.1016/j.oregeorev.2022.105278
- Mordensky et al. 2021, GSA abstract: https://doi.org/10.1130/abs/2021am-365177
- Ghori 2011, WA temperature and heat flow: https://doi.org/10.1071/pvv2011n153p31
- USGS Bulletin 1172, East Tintic gradients: https://doi.org/10.3133/b1172
- Bentkowski and Lewis 1994, Cordillera heat flow: https://doi.org/10.4095/194841
- Jessop 1978, Superior Province heat flow: https://doi.org/10.1016/0040-1951(78)90199-3
- Person et al. 2008, Great Basin geothermal and gold hydrology: https://doi.org/10.1130/ges00150.1
- Geothermal power in Australia (secondary): https://en.wikipedia.org/wiki/Geothermal_power_in_Australia
- Sibling files (sourced): L02-blind-systems.md, L16-gtc-holes.md, D03-great-basin-wells.md, R04-lease-transfers.md, Z03-data-methods.md, Z04-land.md, R11-canada-tenure.md, R13-mineral-claims-overlap.md
