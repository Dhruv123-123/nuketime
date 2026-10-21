# L04 — DOE INGENIOUS (Great Basin, 2021–2026): literature review

## 1. Project facts

- **Name and award:** INnovative Geothermal Exploration through Novel Investigations Of Undiscovered Systems. DOE Geothermal Technologies Office award **DE-EE0009254** (FOA DE-FOA-0002219). Recipient: University of Nevada, Reno (Great Basin Center for Geothermal Energy, GBCGE, part of the Nevada Bureau of Mines and Geology, NBMG). https://gbcge.org/current-projects/ingenious/ ; https://www.energy.gov/sites/default/files/2024-10/CX-031443_0.pdf
- **Money and dates:** $10,000,000 total. Official period of performance 1 Feb 2021 – 30 Jun 2025 (4.5 yr). The press at launch said about $5M was earmarked for drilling exploration wells (https://www.renewableenergyworld.com/energy-business/university-of-nevada-gets-10-million-doe-grant-for-geothermal-energy-exploration/).
  - The project has in practice run past June 2025. NBMG filed Granite Springs Valley temperature-gradient (TG) permits on 2 Apr 2026, approved 21 May 2026. BLM authorized Lund North TG drilling on 13 Aug 2026. So it was evidently extended (unverified: the formal no-cost-extension end date).
- **Leadership:** Bridget Ayling (PI) and James Faulds (co-PI).
- **Partners (12 institutions, >30 collaborators):**
  - Public bodies: USGS, Utah Geological Survey, Idaho Geological Survey, NREL, LBNL.
  - Industry: Raser/Cyrq Energy, Geothermal Resource Group, Petrolern (now Teverra), Hi-Q Geophysical, Aprovechar Lab L3C, Innovate Geothermal Ltd, W Team Geosolutions.
  - Drilling: RESPEC is the drilling engineer, with Envirotech and Welsco as contractors.
- **Scope change (important):** DOE's 2024 NEPA determination says **"slimhole drilling (previously Task 5) was removed from the project"**. TG holes are capped at **≤1,000 ft** (CX-031443). INGENIOUS therefore never drills deep enough to *confirm* a reservoir. It stops at shallow TG holes about 244 m deep.

## 2. Primary-source summaries (chronological)

**[S1] Faulds et al. (2015–2021), Nevada Play Fairway, DE-EE0006731 (the predecessor).**
- Built statistically based fairway and favorability maps over a 96,000 km² Nevada transect.
- Used about 10 parameters, weighted against 34 known high-temperature benchmark systems.
- Led to discoveries of hidden systems at Gabbs Valley and Granite Springs Valley.
- Granite Springs Valley numbers: six TG holes reached up to **~96 °C at ~240 m**, and sinter implies >180 °C at depth.
- This is the template INGENIOUS scales up. https://gdr.openei.org/files/756/Faulds-DE-EE0006731-Report-v2.pdf ; https://www.osti.gov/servlets/purl/1724080

**[S2] Ayling, Faulds, Clark, et al. (2022), "INGENIOUS Project Introduction and Activity Update", GRC 2022 abstract and poster.**
- Lists 33 authors across 13 affiliations.
- Objectives:
  1. Regional and local play fairway (PF) workflows and new favorability maps.
  2. Quantify resource potential and uncertainty at several hidden prospects.
  3. Release public data.
  4. Release geostatistics software.
  5. Write a developers' playbook.
- Plan: TG drilling at **up to four prospects** to validate the PF method. https://gbcge.org/wp-content/uploads/2023/03/Ayling-et-al_INGENIOUS_abstract.pdf

**[S3] Ayling et al. (2022), "INGENIOUS – Great Basin Regional Dataset Compilation", DOE GDR submission 1391 (DOI 10.15121/1881483, CC-BY-4.0, released 30 Jun 2022, modified Mar 2025).**
- Layers:
  - 2-m temperature probes
  - Quaternary faults and volcanics
  - Geodetic shear and dilation
  - Heat flow
  - Magnetotellurics (MT)
  - Gravity and magnetics
  - Paleogeothermal features
  - Seismicity
  - Spring and well temperatures and chemistry
  - Thermal conductivity
  - Fault slip and dilation tendency
- Well data carry a new **"residual"** attribute: the departure from modelled conductive background heat flow. This is effectively a "hidden convection" label. https://gdr.openei.org/submissions/1391 ; https://catalog.data.gov/dataset/ingenious-great-basin-regional-dataset-compilation
- Companion USGS releases:
  - DeAngelo et al. 2022/2023, heat-flow maps
  - Glen et al. 2022, regional geophysics
  - Peacock & Bedrosian 2022, conductance maps
  - Siler 2022, slip and dilation tendency
  - Kreemer & Young 2022, strain rates

**[S4] Faulds & Richards (2023), "INGENIOUS Transitions from Regional to Local Scale to Find Hidden Geothermal Systems", GRC Transactions v.47, p.1721+.**
- The Great Basin has **~28 operating systems, >1,200 MWe nameplate**, and most of its remaining potential is blind.
- McGinness Hills (~150 MWe, blind) is the proof case.
- Up to **15 regional PFA parameters**.
- **>1,000 favorable structural settings** identified. The 2026 update says **>1,430**.
- **>400 known geothermal systems** are available as positive training sites, which addresses the training-site scarcity that hampered the Nevada ML project.
- The 2015 Nevada PFA was re-run in March 2021 with updated layers. Detailed sites were down-selected from **~35 candidates** using PF score plus **land status**, access and prior exploration.
- Argenta Rise had the **highest predictive PF score**.
- Authors' own caveat: eastern Nevada was not chosen because the favorability and ML models "may not fully account" for its geology (carbonate aquifer, older faults, lower strain).
- At Granite Springs Valley:
  - 91 new 2-m temperature points found two subtle anomalies.
  - A 3D Leapfrog model covers ~280 km² to 6 km depth.
  - Stochastic temperature modelling and value-of-information (VOI) analysis were used to rank drill sites (Trainor-Guitton et al. 2023).
- ML used: weights-of-evidence and logistic regression to build "super parameter layers". https://publications.mygeoenergynow.org/grc/1034745.pdf

**[S5] Faulds, Earney, Glen, Queen, Peacock, et al. (2024), "Structural Setting and Geothermal Potential of Northeastern Reese River Valley…", GRC Transactions v.48, p.1240+.**
- Argenta Rise lies ~15 km SE of Battle Mountain, in a broad left-step pull-apart in the Humboldt structural zone. Beowawe is the analogue.
- Data: gravity, magnetics and MT, five reprocessed seismic profiles, and 139 2-m temperature points.
- The 2-m survey found **no definitive thermal anomaly**, only two very subtle ones. The authors suggest any resource may be masked by a cool aquifer or lie deep.
- Four fault intersections and six step-overs were mapped. https://publications.mygeoenergynow.org/grc/1035050.pdf

**[S6] Earney, Glen, Peacock, Faulds, et al. (2024), "Geophysical modeling of a possible blind geothermal system near Battle Mountain, NV", GRC Trans. v.48, p.1699–1719 (USGS).**
- Joint 2D gravity and magnetic modelling plus a 3D MT resistivity model.
- Found **four areas** with favorable structural settings.
- Depth to basement matches the base of shallow conductors, which suggests fluids are confined to basin fill and volcanics.
- Used to site the TG holes. https://pubs.usgs.gov/publication/70271418

**[S7] DOE NEPA Categorical Exclusion CX-031443 (Sep/Oct 2024).**
- Authorizes TG drilling at:
  - Buffalo Valley/Jersey Summit, Lander Co.: all BLM land, 5 areas of interest, up to 10 holes.
  - Argenta Rise: 23 candidate coordinates, 2–10 holes on BLM and/or adjacent private land.
- Maximum depth **1,000 ft**. Each hole takes 3–5 weeks on site, and the campaign runs 3–6 months.
- Truck-mounted rigs, no pads. All holes are plugged and abandoned, with **"No further development."**
- Granite Springs Valley was cleared earlier, on 7/7/2022. https://www.energy.gov/sites/default/files/2024-10/CX-031443_0.pdf

**[S8] Nevada Division of Minerals permits (2024–2026).**
- Argenta Rise:
  - Project Area permit 1627 (Oct 2024).
  - TG wells 1618, 1623 and 1640.
  - Permit 1640 was received 25 Mar 2025. It covers BLM land, 500–1,500 ft total depth, and a landowner/leaseholder agreement letter.
- Granite Springs Valley:
  - Project Area 1739, with **6 TG wells to 1,500 ft**.
  - Received 2 Apr 2026 and issued 21 May 2026.
  - BLM is the land and geothermal-resource owner. NBMG drills under a **leaseholder agreement**, so someone already holds the lease (unverified who).
- The universities drill *on other people's leases*. https://minerals.nv.gov/uploadedFiles/mineralsnvgov/content/Programs/Geo/GeoPermits/GEO%201640%204-4-2025%20NBMG%20Argenta%20Rise%20Lander%201-84.pdf ; https://prod.minerals.nv.gov/siteassets/content/programs/geo/geopermits/geo-1739-5-21-2026-nbmg-granite-springs-project-area-pershing.pdf

**[S9] Hardwick et al. (2025), "Exploration for Blind Geothermal Systems in the Eastern Great Basin of Utah: An Update on the Lund North INGENIOUS Detailed Study Site", 50th Stanford Geothermal Workshop.**
- Lund North (northern Escalante Valley, Iron Co., UT) is the **fourth** detailed site and was flagged by the preliminary PFA map.
- A legacy TG hole has heat flow **>220 mW/m²**.
- New gravity, MT, TEM and aeromagnetic surveys suggest a large E-dipping NE-SW normal fault.
- Follow-on: on 13 Aug 2026 BLM authorized up to 10 TG holes to about 800 ft (243 m) from 20 pre-permitted sites, on BLM and private land. https://www.usgs.gov/publications/exploration-blind-geothermal-systems-eastern-great-basin-utah-update-lund-north ; https://www.blm.gov/announcement/blm-authorizes-geothermal-temperature-gradient-hole-drilling ; https://www.thinkgeoenergy.com/blm-approves-drilling-in-utah-as-part-of-study-on-blind-geothermal-systems/

**[S10] Mordensky, Burns, Lipor & DeAngelo (2025), "Favorability mapping for hydrothermal power resource assessments of the Great Basin, USA", Geothermics 133:103450 (USGS). Data release DOI 10.5066/P14EET2C.**
- This is the USGS 2008-assessment update, run over the **INGENIOUS study region and data layers**.
- Method:
  - 16 features.
  - About 10× more training sites than earlier work.
  - Wells labelled by ordinal convective strength (low, high, very high) from heat-flow residuals.
  - Simple non-linear supervised ML (earlier work favoured XGBoost).
  - Monte Carlo cross-validation, with **1,200 realizations** published as P05–P95 GeoTIFFs.
- Results:
  - **15 of 28 power-producing systems fall in the top 1% of map area.**
  - 26 of 28 (93%) fall above the 80th percentile. Earlier maps captured only about half above the 80th percentile.
  - Highlights: 85% of producing systems sit in the top 10% of area. Of the 99th-percentile hits, 10 of 19 are exposed systems and 5 of 9 are hidden.
- Misses are small or low-temperature, and the authors flag them as possible new prospects. https://pubs.usgs.gov/publication/70270953 ; https://www.usgs.gov/data/geothermal-resource-favorability-select-features-and-predictions-united-states-great-basin

**[S11] Jacinto et al. (2026), Argenta Rise results, 51st Stanford Geothermal Workshop.**
- TG wells were drilled in spring 2025 to **~244 m (800 ft)** and equilibrated for about a month.
- Gradients start at 33.1 °C/km (well 34-41). The upper bound was not retrieved; the Stanford server was unreachable.
- **Neither the 2-m survey nor the ten TG wells found clear thermal anomalies.**
- Potential is "prospective but unresolved". The resource may lie outside the array, be masked by a cool aquifer, or be deeper. There are low-resistivity zones at ~1.5 km.
- Bottom line: **the top-scoring INGENIOUS PFA target came up dry at TG depth.** https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Jacinto.pdf (content via search snippets; full text unverified)

**[S12] Faulds et al. (2026), 51st Stanford Workshop.**
- The final regional favorability maps integrate **16 regional datasets**.
- **>1,430 favorable structural settings** were identified across the Great Basin, with step-overs the most common type.
- I found no final public favorability map or playbook release. As of this writing the playbook is still described as an objective. https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Faulds.pdf (snippet; full text unverified)

**Context: BLM leasing.**
- The Nevada geothermal sale on 20 Oct 2026 offered 83 parcels / 265,691 acres across 10 counties, including Lander, Pershing-adjacent counties and Churchill.
- Nominations cost $150 plus $0.14/acre. https://www.blm.gov/announcement/blm-hold-october-2026-geothermal-lease-sale-nevada ; https://www.blm.gov/sites/default/files/docs/2026-01/NV_20260112_Geo_Nominations_Due_2027.pdf

## 3. Synthesis: what INGENIOUS delivered

1. **Data products (public, free, CC-BY):**
   - A Great Basin-wide layer stack: 15–16 layers, >1,430 favorable structural settings, heat-flow residual labels, and USGS ML favorability P05–P95 rasters.
   - This is the best public "prospectivity substrate" in any geothermal province.
   - It is **public**, so the regional map itself carries no information edge.
2. **Method validation at 4 detailed sites:**
   - **Granite Springs Valley (NV):** already a play-fairway (PF) discovery (~96 °C at 240 m); 6 more TG holes permitted in 2026.
   - **Argenta Rise (NV):** highest PF score; 10 TG holes; **no clear anomaly**.
   - **Buffalo Valley/Jersey Summit (NV):** permitted; results not found.
   - **Lund North (UT):** >220 mW/m² legacy hole; drilling authorized Aug 2026.
3. **No reservoir confirmation:** slimholes were cut, and holes are ≤1,000–1,500 ft. Zanskar's Big Blind confirmation needed wells to **~823 m (2,700 ft)** to hit a 121 °C permeable reservoir (https://www.thinkgeoenergy.com/zanskar-announces-discovery-of-big-blind-geothermal-site-in-western-nevada-usa/). INGENIOUS stops at the step that creates value.
4. **No ownership:** NBMG drills on BLM land under existing leaseholders' permission and plugs every hole. It never takes rights, so the value of any discovery goes to whoever holds the lease.

## 4. Implications for a Terranox-shape geothermal company and the gap vs Zanskar

- **The data layer is now a commodity, and that favors a Terranox shape.** DOE and USGS paid about $10M and five years to produce Great Basin-wide favorability inputs and ML maps that anyone can download. Value is moving from making maps to **acting on maps faster than everyone else**: nominating parcels, taking leases and drilling cheap TG holes. That is exactly the Terranox move (cheap right before proof, own the step-up).
- **Public maps create a predictable leasing race.** Every developer gets the same top-1% cells, so the edge must come from layers *not* in INGENIOUS:
  - the residual of BLM, state and oil-gas well logs not in the GDR
  - mining-company assessment-file drill-hole temperatures
  - proprietary TG holes
  - re-weighting for under-modelled terrains
- INGENIOUS itself admits its maps under-serve **eastern Nevada and Utah** (carbonate aquifer, low strain). That is a map gap a newcomer can target.
- **Argenta Rise is the cautionary datapoint.** The highest-scoring PF site came back with no clear anomaly at 244 m. PFA plus 2-m surveys plus shallow TG holes cannot resolve systems masked by cold aquifers.
  - A Terranox-shape company must budget for **deeper (~500–900 m) TG or slimhole confirmation** on its own leases. Zanskar and Big Blind show this is where the step-up happens.
  - Using public priors as a cheap screen and spending capital only on owned acreage is the right capital stack.
- **Gap vs Zanskar.**
  - Zanskar is an AI explorer *and* operator: it bought Lightning Dock, drills its own confirmation wells and develops power. Big Blind gives no MWe yet, though Zanskar claims comparable systems produce >100 MWe.
  - It is not structured as a **landbank/royalty-style aggregator** that buys rights in bulk at $150 plus $0.14/acre nomination cost, de-risks only to "TG-confirmed anomaly", and flips to Ormat, Fervo or Cyrq or to data-centre offtakers.
  - INGENIOUS shows the academic system will keep producing **unowned, partially de-risked prospects**: Granite Springs, Lund North (>220 mW/m²), Buffalo Valley. These could be **acquired or optioned** from current leaseholders or nominated at the next BLM sale.
  - A Terranox-shape company that tracks INGENIOUS/GDR/USGS releases, BLM nomination lists and NDOM permit filings could systematically be first holder on every newly de-risked cell. Zanskar is not optimized for that portfolio-flip loop.
- **Scale check (not "too small"):**
  - The Great Basin has ~28 systems and >1,200 MWe installed, against far larger estimated blind potential. USGS 2008 put undiscovered hydrothermal at ~30 GWe western-US-wide (that figure is from memory, unverified here).
  - The 20 Oct 2026 BLM sale alone offered 265,691 acres.
  - Inventory to own is ample. The risk is competition for top-percentile parcels, not market size.
- **Watch items:**
  - the final INGENIOUS playbook and favorability map
  - Buffalo Valley, Lund North and Granite Springs 2026 TG results
  - who holds the Granite Springs lease NBMG is drilling under
  - Oct 2026 BLM sale winners in Lander/Pershing counties (all unverified/pending)

## Sources
- https://gbcge.org/current-projects/ingenious/
- https://gbcge.org/wp-content/uploads/2023/03/Ayling-et-al_INGENIOUS_abstract.pdf
- https://gbcge.org/wp-content/uploads/2023/03/Ayling-et-al_INGENIOUS_poster_FINAL.pdf
- https://gdr.openei.org/submissions/1391
- https://catalog.data.gov/dataset/ingenious-great-basin-regional-dataset-compilation
- https://publications.mygeoenergynow.org/grc/1034745.pdf
- https://publications.mygeoenergynow.org/grc/1035050.pdf
- https://pubs.usgs.gov/publication/70271418
- https://pubs.usgs.gov/publication/70270953
- https://www.usgs.gov/data/geothermal-resource-favorability-select-features-and-predictions-united-states-great-basin
- https://www.energy.gov/sites/default/files/2024-10/CX-031443_0.pdf
- https://minerals.nv.gov/uploadedFiles/mineralsnvgov/content/Programs/Geo/GeoPermits/GEO%201640%204-4-2025%20NBMG%20Argenta%20Rise%20Lander%201-84.pdf
- https://prod.minerals.nv.gov/siteassets/content/programs/geo/geopermits/geo-1739-5-21-2026-nbmg-granite-springs-project-area-pershing.pdf
- https://prod.minerals.nv.gov/siteassets/content/programs/geo/geopermits/geo-1744-5-21-2026-nbmg-pershing-granite-springs-68-02.pdf
- https://www.usgs.gov/publications/exploration-blind-geothermal-systems-eastern-great-basin-utah-update-lund-north
- https://www.blm.gov/announcement/blm-authorizes-geothermal-temperature-gradient-hole-drilling
- https://www.thinkgeoenergy.com/blm-approves-drilling-in-utah-as-part-of-study-on-blind-geothermal-systems/
- https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Jacinto.pdf
- https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Faulds.pdf
- https://gdr.openei.org/files/756/Faulds-DE-EE0006731-Report-v2.pdf
- https://www.renewableenergyworld.com/energy-business/university-of-nevada-gets-10-million-doe-grant-for-geothermal-energy-exploration/
- https://www.thinkgeoenergy.com/zanskar-announces-discovery-of-big-blind-geothermal-site-in-western-nevada-usa/
- https://www.blm.gov/announcement/blm-hold-october-2026-geothermal-lease-sale-nevada
- https://www.blm.gov/sites/default/files/docs/2026-01/NV_20260112_Geo_Nominations_Due_2027.pdf
