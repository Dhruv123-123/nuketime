# D03 — Great Basin well and hole records: Nevada (NDOM/NBMG) and Utah (DOGM / Division of Water Rights)

*Research note, 2026-10-21. Method caveat: the shared WebSearch budget ran out before this agent started, so everything here comes from direct fetches of primary sources: statutes and regulations, agency ArcGIS services, and bulk downloads I analysed myself. Some secondary context (NBMG holdings, mining-hole rules) could not be fetched because nbmg.unr.edu returned 503 or TLS errors. Those parts are marked (unverified).*

## 1. Bottom line

1. **Confidentiality windows in the Great Basin are short. Almost everything drilled before about 2021 is legally public now.**
   - Nevada geothermal: "exploration and subsurface information... is confidential for **5 years** after the date of filing" (NRS 534A.031). It must be filed within 30 days of being collected.
   - Nevada oil and gas: records are confidential only if the operator asks, and then for just **1 year** after drilling is completed (NAC 522.540).
   - Utah geothermal, as amended in 2026: a well log is **public when filed** unless the operator asks for protection. Protection is capped at the earliest of:
     - 5 years from production or injection;
     - 2 years from abandonment;
     - **2 years from completion of an exploration or test well project** that does not move straight into production (Utah Code 73-22-6(4)).
   - Federal (BLM): exploration on unleased land, or on land where you are not the lessee, does **not** have to be reported to BLM (43 CFR 3253.10(b)). Data that is submitted has **no fixed confidentiality end date** and is reviewed case by case under FOIA (43 CFR 3255.12, 3266.12, 3278.12).
2. **The datasets are small and countable, which suits a small team.**
   - NDOM's current geothermal well table (Excel, dated 2026-09-29) lists **938 permitted geothermal wells**:
     - 261 temperature-gradient (TG) wells, 244 industrial production wells, 231 observation wells and 170 industrial injection wells;
     - 554 on BLM/USFS land and 383 on private land;
     - spread over 63 field codes.
   - It also includes about 25,700 monthly production rows and about 19,900 monthly injection rows, many with fluid temperature. My own analysis.
   - NDOM's oil and gas well-document search layer has **775** wells. Its geothermal document layer (a 2020 snapshot) has **646** wells.
   - Utah DOGM's well file has **40,414** records statewide, but only **536** are in the western Great Basin counties (Millard, Beaver, Juab, Tooele, Box Elder, Iron, Washington). **315** of those are wildcats and **49** have a proposed depth of 10,000 ft or more. My own analysis.
3. **The data is open but hard to use**, which is the Terranox condition.
   - Nevada logs come as paper or scanned files. LAS digital format has only been required for electric logs (NAC 534A.550(3)).
   - Utah well files and logs are "scanned images" or PDFs. The bulk CSVs do not include temperatures.
   - Temperatures sit inside lithologic logs ("depths and temperatures of water-bearing and steam-bearing strata", NAC 534A.550(1)), temperature logs, and the production and injection TempF columns. Nobody has gathered them into one table for these states (unverified that no private compilation exists).
4. **Ownership law favours buying private rights.**
   - Nevada: "The owner of real property owns the rights to the underlying geothermal resources" unless they were reserved or conveyed (NRS 534A.050).
   - Utah: the surface owner holds title to the geothermal resource "**notwithstanding the severance or conveyance of the mineral estate**" unless it was expressly conveyed by a recorded instrument (Utah Code 73-22-4(2)).
   - So a ranch owner, not an oil or mining company holding severed minerals, is the counterparty. Exception: Utah school trust (SITLA) mineral estate held as of May 6, 2026 keeps its geothermal title in the state (73-22-4(3)(c)).

## 2. Nevada

### 2.1 Legal framework (NRS/NAC 534A, Division of Minerals = NDOM)
- **Permit required.** No one may drill a geothermal well or an exploratory well without a permit from the NDOM Administrator (NRS 534A.060). Exploratory-well applications must be decided within **10 days**, and the permit lasts up to 2 years and can be extended. Geothermal-well applications are decided within 90 days (NRS 534A.070).
- **Well types.**
  - A "thermal gradient well" is "a well drilled to obtain a temperature gradient reading in an area of potential geothermal resources" (NAC 534A.069).
  - The TG bond is at least **$10,000**, against at least $25,000 for commercial or industrial wells (NAC 534A.250).
  - A TG permit costs $100 (NAC 534A.210).
  - TG wells do not need a location survey (NAC 534A.205(3)).
- **What must be filed within 30 days of completion (NAC 534A.550):**
  - a completion report;
  - a directional survey, if the well was drilled directionally;
  - a lithologic log with temperatures of water- and steam-bearing strata;
  - a **temperature log for all well types, including TG wells**;
  - gamma and cement-bond logs, if they were run.
- **Format:** two paper copies, one digital copy, and LAS for electric logs. **NDOM sends one set of logs to NBMG** (NAC 534A.550(4)).
- **Cuttings:** two sets, taken at least every 30 ft, go to NBMG within 30 days of completion (NAC 534A.310).
- **Confidentiality.** 5 years from filing. Earlier release needs the operator's written consent. Other state agencies that receive the data must also keep it confidential (NRS 534A.031). Sources: https://www.leg.state.nv.us/NRS/NRS-534A.html and https://www.leg.state.nv.us/NAC/NAC-534A.html
- **Oil and gas (NAC 522).**
  - Two copies of every logging survey run in the wellbore go to NDOM, which sends one set to NBMG (NAC 522.510(2)).
  - Confidentiality applies only if requested or if exploratory-well logs are marked confidential, and then lasts **1 year** after drilling ends (NAC 522.540).
  - Cuttings go to NBMG and are open to the public once confidentiality ends (NAC 522.215).
  - Practical result: the bottom-hole temperatures (BHTs) in log headers from every Nevada oil and gas wildcat are public. Source: https://www.leg.state.nv.us/NAC/NAC-522.html

### 2.2 What NDOM actually publishes (digitisation status)
NDOM runs an ArcGIS Online organisation (services.arcgis.com/CXYUMoYknZtf5Qr3) with 126 feature services.

**"Geothermal Production And Well Data – 09/29/2026"** (Excel item dcccb7e35aee4885aa4e2aed84b505cf) is the main file. My parse of it:

- **Sheet GeoDH4GIS:** 938 wells. Fields: permit number, operator, well name, field, county, API, well type, UTM coordinates, completion date, status, land type, BLM lease number.
  - **Status:** 390 In Use, 220 Expired, 148 Shut-In, 132 P&A, 43 Pending.
  - **Counties:** Churchill 314, Washoe 139, Lander 103, Mineral 81, Humboldt 70, Elko 64, Pershing 51, Esmeralda 43.
  - **Completions by 5-year bin:**

    | Period | Completions |
    |---|---|
    | 1985–94 | 151 |
    | 2005–09 | 145 |
    | 2010–14 | 154 |
    | 2015–19 | 91 |
    | 2020+ | 37 |

    The 2005–2014 drilling boom is now entirely past the 5-year window.
  - **Top TG operators:** Ormat 115, Standard Steam 28, Sierra Geothermal Power 24, NBMG 21, City of Wells 13, Rockwood Lithium 9. Several of these are defunct or have exited, so their pre-2021 TG data is public and stranded.
  - **Recent permits:** the highest permit number is 1552, which suggests about 1,550 geothermal permits have been issued historically (unverified inference). Recent permits are dominated by Ormat entities (ORNI 32/36/39/47), Fish Lake Geothermal, NGP Blue Mountain, Forty Mile Desert Resources and Star Peak Geothermal.
  - **No operator in the table is named Zanskar or Fervo.** They may file through project LLCs. The table may also not show all recent TG/exploratory permits. Either way, the public table does not reflect 2021+ exploration well (unverified why).
- **Sheets GeothermalProduction / GeothermalInjection / MonthlyMWH:** about 25,700, 19,900 and 4,760 monthly rows from 2009 on. Includes produced gallons, injection rates, and injection temperatures, e.g. Beowawe Batz-1 at 194–196 °F.

**Other NDOM layers and items:**
- **GeoDHSearch** (layer "GeothermalDH08202020"): 646 records of permit/well/API. It works as an index to scanned well documents.
- **OGDHSearch:** 775 oil and gas well records.
- **OGGDhMap:** active oil, gas and geothermal fields, drawn as half-mile buffers around active production, injection, observation, water and TG wells "in the NDOM Geothermal Well Database".
- A web map titled "Oil, Gas, and Geothermal Resources and Groundwater Basins with High Temperature Gradients".
- A PDF "DWR_NDOM Geothermal Table_20221102".
- An "All BLM Case Recordation Products – NV" layer from MLRS, showing leases and claims.

Sources:
- https://www.arcgis.com/sharing/rest/search?q=orgid%3ACXYUMoYknZtf5Qr3%20AND%20geothermal&f=json
- https://www.arcgis.com/sharing/rest/content/items/dcccb7e35aee4885aa4e2aed84b505cf/data
- https://services.arcgis.com/CXYUMoYknZtf5Qr3/arcgis/rest/services/GeoDHSearch/FeatureServer/0
- https://services.arcgis.com/CXYUMoYknZtf5Qr3/arcgis/rest/services/OGDHSearch/FeatureServer/0

**Scale context:** NDOM's geothermal program page reports 26 plants at 17 locations, up to 827 MW of theoretical capacity, and 4,544,175 MWh gross generation in 2018. Contact: Dustin Holcomb, Fluid Minerals Program Manager. Source: https://minerals.nv.gov/Programs/Geo/Geo/

**NBMG holdings** (unverified; the site was down when fetched):
- the statewide cuttings and core library;
- copies of all geothermal and oil and gas logs;
- older geothermal reports and the DOE-era TG-hole compilations (1970s–80s industry-coupled programs);
- Nevada contributions to NGDS (AASG state contributions).

### 2.3 Mining holes
Nevada has tens of thousands of mineral-exploration drill holes. Unlike Saskatchewan, though, **the US federal mining-claim system has had no assessment-report filing requirement** since the 1993 switch to maintenance fees (unverified here; not fetched). Hole temperatures and lithology from mining exploration are therefore mostly **not** in public files.

The exceptions:
- NDWR driller/plugging records for exploration boreholes (unverified);
- company technical reports (NI 43-101/S-K 1300) that sometimes note hot water or steam in holes. Examples: Florida Canyon Mining and Rockwood Lithium both appear in the NDOM geothermal table.

This is a major gap compared with the Terranox uranium playbook. **Nevada's mining record is not a Saskatchewan-style public assessment archive.**

## 3. Utah

### 3.1 Geothermal (Utah Geothermal Resource Conservation Act, Utah Code 73-22, amended 2026 Ch. 477)
- **Regulator:** the Division of Water Rights (73-22-3(2)), not DOGM.
- **Definition:** a "geothermal resource" is heat **>100 °C**, now explicitly including "enhanced geothermal, or advanced geothermal system[s]" (73-22-3(5)).
- **Ownership:** derives from the surface estate, even where the minerals were severed (73-22-4(1)–(2)). Using geothermal *fluid* requires a water right (73-22-4(4)).
- **Records:** the division may require well logs (73-22-6(1)(c)). Logs are **public on filing** unless protection is requested in writing. Protection lasts no longer than the earliest of:
  - 5 years from non-test production or injection;
  - 2 years from abandonment;
  - 2 years from completion of a monitoring, exploration, investigation or test well project that does not go straight into production (73-22-6(4)).

  The State Tax Commission and regulators can always inspect. Source: https://le.utah.gov/xcode/Title73/Chapter22/C73-22_1800010118000101.pdf
- **Implication:** Utah exploration and TG data become public **2 years** after a project ends, faster than Nevada's 5 years. Utah FORGE data is already openly released (see L07).

### 3.2 Oil and gas (DOGM)
- **Bulk downloads** are CSVs from https://oilgas.ogm.utah.gov/oilgasweb/data-center/dc-main.xhtml. Files include Wells, WellHistory, Production 1984–2029, lat/long, and directional surveys. Well files and logs are scanned images or PDFs ("scanned images of the division's files for all wells drilled in Utah").
- **Wells.csv (downloaded 2026-10-21):**
  - 40,414 records, concentrated in the Uintah (20,026) and Duchesne (9,684) basins;
  - 1,468 flagged Confidential, with explicit `ConfRelDate` release dates (e.g. 2027–2028);
  - western Great Basin counties hold only 536 wells (320 wildcat, 173 development, 43 extension); 130 have a proposed depth of 5,000 ft or more and 49 of 10,000 ft or more.
  - The file has no temperature fields. BHTs must be pulled from the scanned log headers.
  - The statutory confidentiality term for Utah oil and gas (R649 rules) could not be fetched (unverified). DOGM's data shows confidentiality is time-limited, with release dates.

## 4. Federal overlay (BLM, 43 CFR 3200)
- **TG wells on BLM land** fall under exploration operations (subpart 3252). Data only has to be submitted for operations on your own lease, or when claiming diligence or extension credit (3253.10).
- **Implication:** exploration on unleased federal land leaves no public record. Old BLM-lease exploration data is kept by BLM with no automatic release date (3255.12). NDOM's state permit is still required for any well (NRS 534A.060), so the state file is the more complete public record.
- **Leasing mechanics:**
  - competitive nominations of up to 5,120 acres (3203.10);
  - the winning bidder pays 20% on sale day and the balance within 15 days (3203.17);
  - parcels with no bids can be leased noncompetitively for 2 years after the sale, with $1/acre advance rent (3204.10, 3204.11).
- **BLM scale:** 51 operating plants and more than 2.65 GW on BLM-managed land. https://www.blm.gov/programs/energy-and-minerals/renewable-energy/geothermal-energy
- **Regulation text** was extracted from https://www.govinfo.gov/content/pkg/CFR-2023-title43-vol2/xml/CFR-2023-title43-vol2-part3200.xml

## 5. Implications for a Terranox-shape geothermal company and the gap vs Zanskar

**The analogue works, with differences.**

**1. The release clock is there and is fast.**
- Saskatchewan opens assessment files after 3 years. The comparable clocks here are:
  - Nevada geothermal: 5 years;
  - Utah geothermal: 2 years after exploration;
  - Nevada oil and gas: 1 year;
  - Utah oil and gas: dated release.
- Every exploration program that failed, was abandoned, or was sold off in 2005–2021 is a public dataset. That includes the 261 Nevada TG holes, mostly from Ormat, Standard Steam, Sierra Geothermal and NBMG, plus the 1,500-plus geothermal permits overall.
- A company can watch NDOM permits (each Pending or Expired permit is a dated signal) and know exactly when each competitor's subsurface data becomes readable.
- A data pipeline is also possible: monthly OCR of NDOM/NBMG scanned logs and Utah well-file PDFs into a structured temperature-at-depth table.

**2. The legal target is the surface owner.** In both states, geothermal follows the surface estate: in Utah even over severed minerals, in Nevada unless reserved. 383 of the 938 Nevada wells are on private land. Buying or leasing geothermal rights from ranchers over a model-flagged anomaly is the closest equivalent of Terranox's cheap claim staking. Geothermal rights on private land change hands outside any auction, so no BLM lease sale reveals your hand.

**3. BLM land is the bigger but noisier half.** 554 of 938 Nevada wells are on federal land. Nominating parcels exposes the target at a public competitive sale. The 2-year noncompetitive window after a sale, for parcels nobody bid on, is a cheap "buy before proof" channel: run ML over parcels that already went unsold.

**4. The data is small enough to own in full.** About 1,000 geothermal wells, about 775 Nevada oil and gas wells, and about 536 western-Utah oil and gas wells are all hand-curatable. The moat comes from extracting the temperature data, not from compute.

**5. Weakness compared with Saskatchewan: mining holes.** US federal mining claims produce no public assessment reports, so the uranium-style "mine the mining files" lever is weak in Nevada (unverified, but structurally likely).

**The gap vs Zanskar:**
- Zanskar's public positioning is a "world model for the subsurface" plus its own TG drilling and plant ownership (Lightning Dock). Its backers include Lowercarbon, USV, Prime Impact and Spring Lane (https://www.zanskar.com/).
- Zanskar runs its own drilling programs and owns operating assets.
- The opening is a **capital-light rights aggregator**:
  - acquire private geothermal rights and post-sale noncompetitive BLM leases using models trained on the *released* public archives;
  - sell de-risked positions to Ormat, Fervo or developers that need data-centre MW.
- Two less-contested assets are also open to an aggregator:
  - private-land rights in Utah, where SITLA-carved-out trust lands aside, the surface owner holds geothermal even over severed minerals and the 2026 amendment now covers EGS;
  - legacy oil and gas BHT data in western Utah and Nevada.
- In the public NDOM table, Zanskar does not appear under its own name. Its own TG data will itself become public under Nevada's 5-year rule, and that would help a follower (unverified how Zanskar files).

## Sources
- NRS 534A (Nevada geothermal statute; 534A.031 confidentiality, 534A.050 ownership, 534A.060/.070 permits): https://www.leg.state.nv.us/NRS/NRS-534A.html
- NAC 534A (Nevada geothermal regulations; .069, .205, .210, .250, .310, .540, .550, .560): https://www.leg.state.nv.us/NAC/NAC-534A.html
- NAC 522 (Nevada oil and gas; .215, .510, .540, .728): https://www.leg.state.nv.us/NAC/NAC-522.html
- NDOM geothermal program page: https://minerals.nv.gov/Programs/Geo/Geo/
- NDOM ArcGIS item search: https://www.arcgis.com/sharing/rest/search?q=orgid%3ACXYUMoYknZtf5Qr3%20AND%20geothermal&f=json
- NDOM Geothermal Production and Well Data (2026-09-29): https://www.arcgis.com/sharing/rest/content/items/dcccb7e35aee4885aa4e2aed84b505cf/data
- NDOM GeoDHSearch layer: https://services.arcgis.com/CXYUMoYknZtf5Qr3/arcgis/rest/services/GeoDHSearch/FeatureServer/0
- NDOM OGDHSearch layer: https://services.arcgis.com/CXYUMoYknZtf5Qr3/arcgis/rest/services/OGDHSearch/FeatureServer/0
- NDOM OGGDhMap: https://services.arcgis.com/CXYUMoYknZtf5Qr3/arcgis/rest/services/OGGDhMap/FeatureServer
- Utah Code 73-22 (2026 amendments): https://le.utah.gov/xcode/Title73/Chapter22/C73-22_1800010118000101.pdf
- Utah DOGM Data Research Center: https://oilgas.ogm.utah.gov/oilgasweb/data-center/dc-main.xhtml
- Utah DOGM Wells.zip: https://oilgas.ogm.utah.gov/pub/Database/Wells.zip
- 43 CFR Part 3200 (BLM geothermal): https://www.govinfo.gov/content/pkg/CFR-2023-title43-vol2/xml/CFR-2023-title43-vol2-part3200.xml
- BLM geothermal program: https://www.blm.gov/programs/energy-and-minerals/renewable-energy/geothermal-energy
- INGENIOUS Great Basin regional dataset (GDR 1391): https://gdr.openei.org/submissions/1391
- Zanskar: https://www.zanskar.com/
