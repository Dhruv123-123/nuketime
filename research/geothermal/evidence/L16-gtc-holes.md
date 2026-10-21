# L16: Historical temperature-gradient (TG) holes and mineral exploration holes as a geothermal signal

**Scope:** the 1970s-80s industry and DOE TG-hole programs (Phillips, Chevron, AMAX, Union and others), how much of that record is public and digitised, and mineral-exploration drill holes as an unexploited temperature source.

**Method note:** the shared WebSearch budget for this workflow ran out before this agent's first search. Everything below comes from direct fetches of primary repositories: USGS Pubs, OSTI/DOE, the NREL docs server, the GDR (OpenEI), USGS ScienceBase and Zanskar's own posts. I also analysed the raw USGS spreadsheet myself. NBMG (nbmg.unr.edu) and the Stanford geothermal server returned HTTP 503 on every attempt, so the NBMG and DOGAMI holdings are covered only indirectly. Anything without a source is marked (unverified).

---

## 1. Primary sources reviewed

### S1. Sass, Priest, Blanton, Sackett, Welch & Walters (1999/2000). *Geothermal industry temperature profiles from the Great Basin.* USGS Open-File Report 99-425
https://pubs.usgs.gov/of/1999/of99-425/webmaps/home.html

This is the anchor dataset for the topic.
- **History.** Starting in the 1970s, Chevron Geothermal and Phillips Petroleum "together evaluated more than 75 geothermal prospects" with potential for at least 150 °C. Other companies assessed 25 or more further sites, for over 100 industry-evaluated high-temperature sites in total.
- **Chain of custody.** Most Chevron/Phillips subsurface temperature data ended up with **CalEnergy**. In summer 1998 USGS staff inventoried the CalEnergy holdings, and **DOE bought the temperature data for "several hundred" holes** for curation at INEEL. The USGS digitised them as part of the deal.
- **Other data in the release.** The report adds data from GEO, Aminoil, AMAX and others, which the USGS had obtained from INEEL in 1995.
- **Format.** The originals were field data sheets, interpretive reports and analogue T-z plots, mostly located only by Section/Township/Range. The published gradient is "a visual straight-line fit of the lowermost section of each hole," measured with thermistor probes accurate to about 0.1 °C.

**My analysis of the released spreadsheet** (`database.xls`, downloaded from the page above):
- **786 holes across 82 prospects.**
- **By company:** Phillips 623 (plus 2 marked "Phillips(?)"), Chevron 83, AMAX 32, GTS 24, Magma Power 5, GRI 4, Earth Power 3, and Union, Supron, Geonomics and GEO Operator 2 each.
- **By state:** NV 669, UT 90, OR 25, CA 2.
- **Depths:** median **300 ft**, mean 415 ft, maximum 8,055 ft. These are shallow holes.
- **Gradients:** median **4.8 °F/100 ft**. 365 holes are at or above 5 °F/100 ft and **116 holes are at or above 10 °F/100 ft**. The highest is 91.5 °F/100 ft at San Emidio.
- **Prospects:** 28 of the 82 have a maximum gradient of at least 10 °F/100 ft. Examples are San Emidio, Silver Peak, Tracy, Reese River (median 13.3 °F/100 ft across 28 holes), Wilson Hot Springs, McCoy (AMAX), Trinity Mountains, Tule (UT), Baltazor, Drum Mountains (UT, 72 holes) and Glass Buttes (OR).
- **Comparison point.** Background Nevada gradients are about 2-3 °F/100 ft (S4).
- **What is missing.** The spreadsheet holds one gradient per hole, not the full T-z profiles (the clickable map offers profiles for some wells). "Several hundred" holes came out of a CalEnergy archive that covered more than 100 prospects, so the remaining CalEnergy holdings and other companies' files appear never to have been released (inference).

### S2. Sass, Priest, Lachenbruch, Galanis, Moses, Kennelly, Munroe, Smith, Grubb, Husk & Mase (2005). *Thermal data from the Great Basin* (USGS heat-flow program supporting data, 1970-1990). USGS OFR 2005-1207
https://pubs.usgs.gov/of/2005/1207/

- **Content.** Site heat flows, thermal conductivities and temperature profiles from USGS research holes across NV, CA and OR. The sites include Dixie Valley, Carson Sink (a 2.5 km NURE hole), Steamboat, Ruby Valley, San Emedio (Chevron test wells), Yerington and Black Rock.
- **Industry inputs.** Chevron, Geo Operator Corp, GTS reports and consultants.
- **Downstream use.** S2 and the SMU database are the two inputs to the USGS/INGENIOUS Great Basin heat-flow map (S7). The industry TG holes are therefore already in the public baseline models, but only as single gradient values and only where they were released.

### S3. Fortuna, R. (DOE) and DOE Geothermal Division (1995). *The Role of Cost Shared R&D in the Development of Geothermal Resources* (Program Review XIII). OSTI 860716
https://www.osti.gov/biblio/860716

- **Programme.** The DOE **Industry-Coupled (Drilling) Program** started in 1977 and covered **14 sites**: 2 in southern Utah and 12 in northern Nevada. It funded "deep exploratory wells, shallow thermal gradient test holes and geoscience investigative surveys."
- **Data terms.** One of its explicit objectives was "making data generated from the program available for unrestricted use."
- **Outcome by 1995.** 8 of the 14 sites were producing power: Roosevelt Hot Springs, Cove Fort-Sulphurdale, Beowawe, San Emidio, Soda Lake, Stillwater, Dixie Valley and Desert Peak. Together they had **137 MW installed**, which was 69% of Nevada's capacity and all of Utah's.
- **Cascades follow-on.** A separate 1985 Cascades Deep Thermal Gradient Drilling Program drilled 5 deep core holes in Oregon (Newberry, Breitenbush, Crater Lake and Santiam Pass).
- **Base rate.** In the 1970s-80s, cost-shared TG drilling at pre-selected, surface-expressed sites led to development at **57%** of sites. That success rate is for *known* systems. Blind ones are harder.

### S4. Levine, Rhodes & Kvien (2022). *Mining G.O.L.D.: Exploring Synergies Between the Geothermal and Mining Industries.* NREL/TP-6A20-81946, OSTI 1855781
https://docs.nlr.gov/docs/fy22osti/81946.pdf

This is the key source on mining holes.
- **No reporting rule.** "Few measured temperatures are found in publicly available mining databases." Mineral exploration holes are not regulated like water wells, and there is no requirement to collect a temperature log.
- **An existing temperature record.** Directional-survey tools carry internal temperature sensors, so most angled mineral holes already have an unequilibrated T-z record that is "infrequently analyzed." Directional-survey providers "likely possess a vast database" of these readings, which are proprietary.
- **Worked example.** NREL looked at deviation surveys from **74 mineral exploration holes** at one central Nevada prospect. The bottom-hole maximum was 151 °F, with a gradient of about **10.5 °F/100 ft**, against a background of about 2-3 °F/100 ft. Extrapolated, that reaches 300 °F about 1,400 ft deeper.
- **Blind plants found through mining data:**
  - **McGinness Hills** (Ormat, about 140 MW by 2020). Anaconda drilled 4 holes in 1982, FMC 12 RC holes in 1984, and Newcrest found 190 °F water at 980-1,200 ft in 2004, with silica geothermometry up to 346 °F. Ormat then won BLM leases at a competitive auction in August 2007.
  - **Blue Mountain** (49.5 MW nameplate, about 38 MW net). Epithermal gold drilling in the early 1990s hit hot water. The mining company took BLM geothermal leases *non-competitively* and later **sold the leases plus data** to a geothermal developer.
  - **Don A. Campbell** (Ormat, 42 MW, 2013). The site has no surface features. Early-1990s mining holes found 140-190 °F fluids and 203 °F vapour over about 46 km². Ormat reviewed the mining data **at no cost**, nominated the land in 2001 and won it at a BLM auction in 2007.
- **Other findings.** Cataloguing these data would be cheap. Co-development could cut LCOE by 23-29% (from about $87 to $65-67/MWh). The report lists 13 relevant archives, including the NBMG Great Basin Science Sample and Records Library, NBMG Mineral Industry and Exploration Reports, county mineral reports, the Anaconda database at the University of Wyoming, the USGS core libraries, the UGS Core Database, the National Mine Map Repository and NURE.

### S5. Faulds, Hinz, Coolbaugh, Ayling, Glen, Craig, McConville, Siler, Queen, Witter & Hardwick (2021). *Discovering Blind Geothermal Systems in the Great Basin Region… All Phases.* DOE final report, OSTI 1724080
https://www.osti.gov/biblio/1724080

- **Method.** 9 parameters over a **96,000 km²** area gave 24 prospective areas, 5 detailed studies and **12 new TG holes** at 2 sites.
- **Results.** Southeastern Gabbs Valley reached about 124 °C at 152 m with no surface manifestation. Northern Granite Springs reached about 96 °C at about 250 m.
- **Takeaway.** A dozen shallow TG holes were enough to confirm two blind systems, which shows TG holes are still the cheapest way to prove a system. Supporting thesis: Craig (2018), OSTI 1724116 (https://www.osti.gov/biblio/1724116), where 6 TG holes found 2 above boiling and a system of at least 130 °C.

### S6. Mordensky, Lipor, DeAngelo, Burns & Lindsey (2023). "When less is more…" *Geothermics* 110:102662. OSTI 2418597. Data: doi:10.5066/P9V1Q9XM
https://www.osti.gov/biblio/2418597 and https://www.sciencebase.gov/catalog/item/63090a9cd34e3b967a8c19c4

- **Setup.** 9 favourability models (weights of evidence, logistic regression, XGBoost, SVM, ANN) for the western US, all trained on the USGS 2008 assessment's 5 features (heat flow, distance to Quaternary fault, distance to Quaternary magma, seismic density, SHmax). Labels are the known systems.
- **Result.** **All F1 scores are below 0.10** and do not improve with model complexity. The authors say this is because the input *features* are the limit.
- **Takeaway.** Better data is the bottleneck, not better models. That is the core argument for any strategy built on recovering more heat-flow points.

### S7. DeAngelo, Burns, Gentry, Batir, Lindsey & Mordensky (2022). *Heat flow maps and supporting data for the Great Basin, USA.* USGS data release, doi:10.5066/P9BZPVUC
https://www.sciencebase.gov/catalog/item/6297d2fad34ec53d276c5b28

- **Method.** Background conductive heat flow from iterative LOESS regression that down-weights convective outliers. Inputs are only the **SMU (2021) database and Sass et al. (2005)**.
- **Useful output.** A per-well "residual" attribute that flags anomalous wells.
- **Takeaway.** The public baseline that everyone uses, Zanskar included as far as one can tell, rests on these two compilations. Any industry or mining holes not in SMU or USGS archives are invisible to it.

### S8. Allison, Richard et al. (2012, 2015). NGDS / State Geological Survey Contributions. OSTI 1172332 and 1172894
https://www.osti.gov/biblio/1172894

- **Size.** By May 2012 the NGDS (through AASG) had about **37,000 catalogue records and 550,075 online data resources**. By 2015 it described "millions of records" from 60+ providers in all 50 states.
- **Related.** Anderson et al. (2014), OSTI 1172334, cites about 41,000 documents and over 9 million data points.
- **Takeaway.** Much of the digitised material (scanned well logs, BHTs, TG reports) exists as images or PDFs rather than clean tables. That is the "public but illegible" condition Terranox exploits in Saskatchewan. The exact share that is machine-readable is (unverified).

### S9. Lienau & Ross (1996). *Low-Temperature Resource Assessment Program, Final Report.* OSTI 203977
https://www.osti.gov/biblio/203977

- **Content.** An inventory of **8,977 thermal wells and springs (20-150 °C)** across 10 western states, compiled by state teams (NBMG, UGS, DOGAMI, etc.).
- **Takeaway.** Another large, mostly point-level legacy dataset. Its focus is direct use.

### S10. Utah: Nash (2004). *Utah FORGE: Temperature Gradient Database,* hosted by UGS. GDR submission 698
https://gdr.openei.org/submissions/698

- **Content.** The UGS keeps a statewide TG database. The hole count is not shown on the GDR page (unverified).
- **Related.** Wright et al. (1990), OSTI 890978, describes the UURI/EGI archive: about 500 reports plus cuttings and core from **more than 180 geothermal drill holes**. Much of the Industry-Coupled output (Roosevelt and Cove Fort) sits there.

### S11. Zanskar, primary posts (Dec 2025)
https://zanskargeothermal.substack.com/p/zanskar-proves-first-blind-geothermal and https://zanskargeothermal.substack.com/p/zanskar-reveals-big-blind-the-discovery

- **Big Blind.** The site had "no history of any geothermal exploration or other prior well data." Zanskar flagged an above-background heat-flow anomaly in late 2023, **won BLM leases at auction**, and then collected high-resolution geophysics.
- **Drilling.** It drilled 2 intermediate wells in July-August 2025, reaching about 250 °F at about 2,700 ft (TD 2,668.5 ft) with total lost circulation.
- **Cost claim.** Exploration at "<$15k per MW."
- **Company news.** The news page (https://www.zanskar.com/news) lists a $115M Series C (January 2026), $40M of development capital that can scale to $100M (April 2026), a 100 MW PPA with NV Energy (May 2026), and a campaign spanning "millions of acres across the West."

---

## 2. Synthesis: how many holes exist and how much is digitised

| Pool | Approx. size | Public? | Machine-readable? |
|---|---|---|---|
| Chevron/Phillips/AMAX etc. TG holes released by USGS (S1) | **786 holes, 82 prospects** | Yes | One gradient per hole, no full profiles |
| The rest of the CalEnergy Chevron/Phillips archive covering 100+ prospects | Unknown; S1 says only "several hundred" holes were bought | Likely private or orphaned (inference) | No |
| DOE Industry-Coupled Program (14 sites, 1977-82) (S3) | Hundreds of TG holes (unverified count) | Released for "unrestricted use" | Mostly scanned reports at OSTI/EGI |
| USGS research heat-flow holes (S2) | Hundreds | Yes | Yes |
| SMU database plus NGDS/AASG (S7, S8) | Millions of records; heat-flow site counts not retrieved | Yes | Partly; many are scans |
| Low-temperature wells and springs (S9) | 8,977 | Yes | Yes (points) |
| Mineral exploration holes with directional-survey temperatures (S4) | Likely tens of thousands in Nevada (unverified); 74 at one prospect | **Mostly private** (claim holders, survey contractors) | Digital at source but never compiled |
| NBMG mining assessment, industry exploration reports and county files (S4) | Large (count unverified; NBMG offline) | Public | Mostly scanned text: hot water, steam, "hot pipe" and boiling are only described in drill logs |

**Main point.** The public thermal baseline for the Great Basin (S7) is built from roughly two curated compilations. Three large pools sit outside it:
1. The unreleased part of the 1970s-80s industry TG archive.
2. Text-only temperature hints in public mining assessment files and drill logs, which S4 says need keyword queries such as "steam, geysering, hot pipe, increased mud temperatures, artesian flow, boiling" plus old silica-alteration terms.
3. Directional-survey temperatures from mineral holes, which are private but cheap to license.

S6 shows that model quality is limited by features, so adding new heat-flow points is the highest-leverage input.

**Proof that this signal finds plants.** Three producing Nevada plants totalling about 220 MW were found from mining-hole temperatures: McGinness Hills, Blue Mountain and Don A. Campbell. In each case the right was secured *after* someone read the data. Blue Mountain's discoverer took non-competitive leases and **sold them with the data**, which is the Terranox playbook carried out in 1991.

---

## 3. Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **The Terranox analogue holds.** Nevada's mining assessment files and drill logs are public, they are illegible as narrative scans, and they hold temperature evidence: the Saskatchewan pattern. History shows the read-then-lease-then-flip loop works. In the Blue Mountain case, mining holes found hot water, the company took non-competitive BLM leases, then sold the leases plus data. McGinness and Don A. Campbell followed the same path: mining data, then a BLM nomination or auction, then a 42-140 MW plant.

2. **The data edge is real and specific.** Zanskar's posts describe a proprietary prospecting toolkit and new geophysics. For Big Blind they stress there was *no* prior well data. The public heat-flow baseline (S7) excludes three pools:
   - the unreleased CalEnergy and other industry TG files;
   - text-mined NBMG and county mining assessment records;
   - licensed directional-survey temperature streams from mining companies and survey contractors.

   An LLM/OCR pipeline over pools 1 and 2, plus data-licensing deals for pool 3, would give a company heat-flow points nobody else has. S6 says that is exactly what limits geothermal ML. Whether Zanskar already ingests these pools is not public (unverified). Their messaging centres on physics, AI and new geophysics rather than archive recovery.

3. **There is a wedge Zanskar is not visibly working.** Mining companies hold thousands of Nevada claims with private hole temperatures. The data could be bought as a portfolio deal, or swapped for a geothermal royalty or carried interest. BLM geothermal leases could then be nominated over the anomalies before anyone else sees them. Blue Mountain shows mining companies have done this alone, one site at a time, but nobody does it systematically. The 116 released industry holes at or above 10 °F/100 ft (28 prospects) also make an immediate re-screening list against current BLM lease status.

4. **The right is cheap but competitive.** Nominated BLM land usually goes to competitive auction: Ormat won both McGinness and DAC at auction in 2007, and Zanskar bought Big Blind's leases at auction. The edge is knowing *which* parcels to nominate and how much to bid. Private and state land, and mining-claim holders' option rights, are where non-auction access is possible (see the leasing L-files).

5. **Scope.** About 220 MW of operating plants already trace back to mining holes. The USGS estimates about 30 GW of undiscovered hydrothermal resources (https://pubs.usgs.gov/fs/2008/3082/), and NREL estimates about 10% of Nevada's roughly 5.8 GWe is discovered (S4, citing Ayling 2020). That is not too small.

6. **Risks.**
   - Mining temperatures are unequilibrated and taken in angled holes.
   - The DOE base rate of 57% development (S3) applies to surface-expressed sites.
   - Zanskar has $155M+ and an operating plant, and could copy the data-licensing wedge.

   Differentiation should therefore be exclusive data contracts with major claim holders, such as Nevada Gold Mines, Kinross and lithium juniors (named targets, unverified interest), plus speed to nominate.

---

## Sources
- https://pubs.usgs.gov/of/1999/of99-425/webmaps/home.html (Sass et al. 1999, OFR 99-425; database.xls analysed)
- https://pubs.usgs.gov/publication/ofr99425
- https://pubs.usgs.gov/of/2005/1207/ (Sass et al. 2005)
- https://www.osti.gov/biblio/860716 (DOE 1995, Industry-Coupled Program)
- https://docs.nlr.gov/docs/fy22osti/81946.pdf and https://www.osti.gov/biblio/1855781 (Levine et al. 2022, Mining G.O.L.D.)
- https://www.osti.gov/biblio/1724080 (Faulds et al. 2021)
- https://www.osti.gov/biblio/1724116 (Craig 2018)
- https://www.osti.gov/biblio/2418597 (Mordensky et al. 2023)
- https://www.sciencebase.gov/catalog/item/63090a9cd34e3b967a8c19c4
- https://www.sciencebase.gov/catalog/item/6297d2fad34ec53d276c5b28 (DeAngelo et al. 2022)
- https://www.osti.gov/biblio/1172894 (Allison & Richard 2015), OSTI 1172332, OSTI 1172334
- https://www.osti.gov/biblio/203977 (Lienau & Ross 1996)
- https://gdr.openei.org/submissions/698 (Utah TG database)
- https://www.osti.gov/biblio/890978 (Wright et al. 1990, UURI archive)
- https://gdr.openei.org/submissions/616 (Nevada PFA regional data)
- https://pubs.usgs.gov/fs/2008/3082/ (USGS 2008 assessment)
- https://zanskargeothermal.substack.com/p/zanskar-proves-first-blind-geothermal
- https://zanskargeothermal.substack.com/p/zanskar-reveals-big-blind-the-discovery
- https://www.zanskar.com/news
