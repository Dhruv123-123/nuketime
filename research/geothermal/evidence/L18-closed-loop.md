# L18: Closed-loop / advanced geothermal (Eavor, XGS, Sage, GreenFire) and geologic thermal energy storage. Does "any hot rock" kill rights scarcity?

**Method note.** The shared WebSearch budget for this run ran out before this agent started. All sources below were pulled directly from primary repositories: the OSTI.gov records API and full-text PDFs, Sage Geosystems' own published papers, and company and trade pages fetched by URL. The publisher pages for Beckers et al. 2022 and White et al. 2024 (Elsevier) were paywalled, so their numbers are taken from the NLR 2025 Market Report's summary of them. Eavor.com was bot-blocked.

## Bottom line

1. **Closed-loop (CLG/AGS) does not make "any hot rock" valuable. It makes *hot, shallow, high-gradient* rock more valuable.** CLG gets heat out by conduction only. Output scales with how hot the rock is at the depth you can drill economically, and with how much wellbore length sits in that hot rock. Every primary techno-economic study finds CLG power uneconomic at normal gradients: $136 to $560/MWh, against $64 to $98/MWh for EGS or caged systems in the same rock. NLR's study of the Eavor-Loop 2.0 design says reaching under $70/MWh needs **60 °C/km**, a discount rate below 9%, and laterals below $400/m. That is roughly double the US average gradient.
2. **Heat (direct use) is the exception.** CLG heat is already near cost parity at 30 °C/km (LCOH $4 to $30/MWh). But heat is local, small, and does not compete for scarce land.
3. **"Geothermal anywhere" developers still pick sites.** Sage is the clearest case. Its own L48 study says only **53 GW** of hot-dry-rock potential has 180 °C at 2 to 3 km depth (cheapest tier). There are 562 GW at 3 to 4 km, 1,044 GW at 4 to 5 km, and 2,327 GW at 5 to 6 km (+$35/MWh). The cheapest tier is about 1.3% of the resource. That is exactly the scarce, mappable, acquirable thing.
4. **Geologic storage needs specific geology**: a permeable reservoir with closure and a seal (GeoTES/RTES), or deep, high-closure-stress tight rock (Sage EarthStore). Depleted oil fields and old wells are the favoured hosts. That is a *second* rights class a data-plus-land company could own.

## Literature reviewed (primary sources)

### 1. Akindipe, Martinez Smith, Witter, Pauling et al. (NLR, 2026). *2025 U.S. Geothermal Market Report*, section 3.6 (Advanced/Closed-Loop). OSTI 3014949.
- CLG "exchange[s] thermal energy from hot rocks mostly by conductive heat transfer… the rate of conductive heat exchange is dependent on the wellbore surface area." "There is currently no resource potential assessment for CLG."
- CLG skips exploration and resource-confirmation spend, but it "require[s] extensive drilling" and suffers a "sharp early decline in production temperature".
- **Eavor-Lite** (Sylvan Lake, AB): two 2.4 km verticals joined by two 1.7 km open-hole laterals. Rock was at 78 °C and outlet stabilised at 50 °C. Total output was about **20 GWh-thermal over 4 years** (2019 to 2023), i.e. roughly 0.6 MWth average (my arithmetic).
- **Eavor-Deep** (NM, 2022): about 18,000 ft TVD at about 250 °C. It proved multilateral drilling in hot hard rock.
- **Geretsried** (Germany): 4 loops at 4.5 km, planned 8.2 MWe / 64 MWth.
- Eavor raised about **$529M** (2021 to June 2025: $387M equity plus €130M/$142M debt). XGS raised $56.7M and GreenFire $19M.
- **GreenFire GreenLoop**: a coaxial loop in an existing Coso well (BHT 200 °C) gave **1.2 MWe gross**. It relies on *convection of steam or multiphase fluid in an existing hydrothermal reservoir*, so it is a retrofit of a known resource, not "anywhere".
- **XGS**: a conductive slurry (up to 50x rock conductivity) placed 1 to 10 m around the bore. It claims **3 to 10 MWth per well**.
- **Meta PPAs**: Sage up to 150 MWe (2024), XGS up to 150 MWe in NM by 2030 (June 2025).
- "A first-of-a-kind commercial CLG power plant has not been developed in the United States as of June 2025."
- URL: https://www.osti.gov/servlets/purl/3014949

### 2. Beckers et al. (2022), *Geothermics* 100:102318, "Techno-economic performance of closed-loop geothermal systems for heat production and electricity generation", plus Beckers and Johnston (2022). Numbers via source 1.
- Covers coaxial and U-loop designs (1 to 13 laterals), water or sCO2, 100 to 500 °C.
  - LCOH: about $20 to $110/MWh coaxial, $10 to $70/MWh U-loop.
  - LCOE: from **$83/MWh** (2-lateral U-loop, 500 °C, $200/m drilling) up to **$2,200/MWh** (coaxial, 200 °C, $1,000/m).
  - Cutting drilling cost from $1,000/m to $200/m lowers LCOE by only 28%.
- Eavor-Loop 2.0 (12 laterals, 7.5 km):
  - Getting LCOE under $70/MWh needs **60 °C/km**, a discount rate below 9% and laterals below $400/m.
  - LCOH is $4.32 to $29.52/MWh at 30 °C/km and $600/m.
- I could not open the paper directly. URL: https://doi.org/10.1016/j.geothermics.2021.102318

### 3. White, Martinez, Vasyliv, Bran-Anleu, Parisi, Balestra, Horne, Augustine (2021), Closed-Loop Geothermal Working Group (PNNL/SNL/INL/NREL/Stanford). OSTI 1837565.
- Multi-code intercomparison of closed-loop performance in hot-dry-rock and hot-wet-rock reservoirs, built on Utah FORGE rock and costs.
- The follow-on paper is White et al. 2024, *Geothermics* 116:102852. The group established that the steep early temperature decline is common to all designs because conduction dominates (per source 1). This work fed the public **GeoCLUSTER** tool.
- URL: https://www.osti.gov/biblio/1837565

### 4. Hakes, Bozinoski, Beckers, Ketchum (2024), *GRC Transactions* 48, "Influence of Reservoir Convection on Heat Extraction with Closed-Loop Geothermal Systems" (Sandia/NREL).
- Natural convection only lifts CLG output when permeability is **≥ about 100 mD**. Forced convection needs Darcy velocity ≥ 1e-7 m/s.
- Typical crust at 2 km is about 1 mD, "several orders of magnitude smaller" than that.
- **Implication:** CLG gets materially better only in *permeable hot reservoirs*, which are hydrothermal resources, the very thing Zanskar hunts.
- URL: https://www.osti.gov/servlets/purl/2586305

### 5. Beckers, Ketchum, Augustine (2024), 49th Stanford Geothermal Workshop, "Closed-Loop Geothermal Systems with Thermally Conductive Enhancements in Conduction-Only Reservoirs".
- This is an independent check on the XGS-type concept.
  - Disc enhancements (5 mm thick, 5 m radius, every 1 m, 100x rock conductivity) raise thermal output by **about 20%**.
  - Fishbone enhancements raise it by about 7%.
- This is far below the 30 to 50% heat-uptake claim XGS made in 2024 (JPT, source 13). Under the standing rule we score on plausibility, but the physics ceiling is still set by rock temperature.
- URL: https://www.osti.gov/biblio/2324601

### 6. Akindipe, Gold, Mibei, Ketchum, Beckers (2024), GRC preprint, "Thermal and Well Flow Performance of Closed-Loop Geothermal in the Wattenberg Area".
- Setting: Denver-Julesburg basin, basement above 200 °C, laterals at 6 km approaching 300 °C.
- Optimised U-loop: 10 laterals at 50 m spacing, 1,000 m well spacing, **60 °C/km**, 60 kg/s. It produces an **average 19 MWth**.
- Costs: **LCOE $136/MWh**, LCOH $1.53/GJ over 20 years.
- URL: https://www.osti.gov/biblio/2476300

### 7. Mibei, Gold, Akindipe, Aljubran, Acero-Allard (NLR, 2026), TEA of EGS vs closed-loop in the Wattenberg Field.
- Same rock, both designs compared:

| | Output | LCOE | NPV |
|---|---|---|---|
| EGS | **13.5 MWe** | **8.25 to 12.1 ¢/kWh** | $85.9M |
| Multilateral closed loop | **5.8 MWe** | **13.5 to 14 ¢/kWh** | $35M |

- Lateral spacing beyond 25 m gave diminishing returns. Lower-conductivity rock and sCO2 both hurt performance. The study calls closed loop the "lower-risk, predictable" option where EGS is infeasible.
- URL: https://www.osti.gov/biblio/3408143

### 8. Frash (LANL, 2024/2026), *GRC Transactions* 48, "Whispers of a New Frontier for Safe and Profitable Geothermal Anywhere".
- Monte Carlo (about 48,000 realisations, GeoDT model) of AGS, EGS and fracture-caged CGS in greenfield hot dry rock. Results:
  - AGS (closed loop) **$275 to $560/MWh**
  - CGS $64 to $98/MWh (about $70M capex)
  - EGS cheapest but carries seismic risk
- **Reservoir temperature and flow rate are first-order drivers; depth and gradient are second-order.** Thermal conductivity (2.2 to 3.6) had no discernible effect.
- Even the "geothermal anywhere" optimist still ranks sites by temperature.
- URL: https://www.osti.gov/servlets/purl/3388421

### 9. Anderson, Eros, Klarin, Ring, Simpkins (Sage Geosystems, 2025), 50th Stanford Workshop, "Hot Dry Rock Geothermal Power Generation Estimates for the USA (L48) Using Reduced Order Physical Models".
- Hot-dry-rock power needs **rock above 150 °C** plus engineered fractures. The study builds on the Aljubran and Horne thermal model (more than 400,000 BHTs).
- Potential: more than 5 TW above 5 km and 13 TW above 6 km.
- LCOE and capacity by depth to 180 °C:

| Depth to 180 °C | Capacity | LCOE vs base |
|---|---|---|
| 2 to 3 km | **53 GW** | −$5/MWh |
| 3 to 4 km | 562 GW | base |
| 4 to 5 km | 1,044 GW | +$5 |
| 5 to 6 km | 2,327 GW | +$35 |

- Deeper than 6 km is "economically infeasible with current technologies". "Shallow HDR resource enables projects with low LCOE, though these are sparsely available."
- URL: https://cdn.prod.website-files.com/67c9634e56bc9ae5113f2fcb/67e6c076244be58baf21aa7f_Stanford%202025.pdf

### 10. Simpkins, Rivas, Eros, Ring (Sage, 2023), *GRC Transactions* 47, "Energy Storage in Deep Hydraulic Fractures: Mathematical Model and Field Validation".
- Sage re-entered a plugged and abandoned gas well (JFB Heard 1, Starr County, TX): about **19,000 ft TVD**, casing to about 11,500 ft. It made a vertical fracture and ran five weeks of huff-and-puff cycles at 3,000 to 4,000 psi.
- Best results: **about 1 MW peak over a 44-minute flowback**, and about 200 kW sustained for about 3 hours in a long cycle.
- Claims (company-reported):
  - Capex about $2M/MW vs $2.64M/MW for pumped hydro.
  - Deeper fractures give higher energy density because closure stress is higher.
  - Permitting takes "a few weeks in Texas".
- **Resource need:** deep, tight, high-stress rock plus *reusable legacy wells*.
- Commercial follow-on: a **3 MW** EarthStore facility with San Miguel Electric Co-op (Christine, TX), commissioned around Q1 2025 per Sage's projects page. In Sep 2026 Sage picked Ormat's Blue Mountain (NV) for its next commercial EGS facility, i.e. *a known hydrothermal field with existing infrastructure*.
- URL: https://cdn.prod.website-files.com/67c9634e56bc9ae5113f2fcb/67e6bfab995eb743d94983c9_2023_GRC_SageGeosystems_EnergyStorageInDeepHydraulicFractures_2023.09.08.pdf

### 11. Halloran, Simpson, Ho (NLR, 2026), *Value of Geothermal Energy Storage for Supply-Side and Demand-Side Applications*. OSTI 3377911.
- In-reservoir storage added to an EGS plant adds a regional median **$470/kW** at 20 h of duration. That is more than double the value at 5 h, and could cover **18% of deep-EGS flash capex** (2050 advanced costs). At 1,000 h it reaches **$703/kW**.
- Most of the value comes from added *firm capacity*, so it does not depend on round-trip efficiency.
- Demand side: seasonal hot and cold reservoir thermal energy storage (RTES) cuts grid costs in most building types.
- **Implication:** storage-capable reservoirs (tight, good seal, low leak-off) are worth a premium per kW on top of plain heat.
- URL: https://www.osti.gov/servlets/purl/3377911

### 12. Zhu, Akindipe, McTigue, Witter, Atkinson, McLing, Kumar, Dobson (2023), SPE 215756 preprint, "Techno-Economic Analysis and Market Potential of GeoTES… into Depleted Oil/Gas Reservoirs and Shallow Reservoirs"; plus McTigue et al. (2026), "A Demonstration System for GeoTES of Concentrating Solar Thermal" (OSTI 3364532).
- GeoTES levelized cost of storage (LCOS) has "minimal marginal cost with increasing hours" because the reservoir already exists.
- Site criteria:
  - production temperature above 91 °C for small binary plants
  - porous, permeable formation with **closure**
  - low-permeability caprock
  - manageable salinity/scaling
  - suitable depth and pressure
- The DOE-funded demo in Kern County (Premier Resource Management): 2 MWth parabolic trough, **7 wells**, 100 kWe cycle. It is the seed of a planned **400 MW** dispatchable project converting oilfields.
- URLs: https://www.osti.gov/servlets/purl/2001115 ; https://www.osti.gov/biblio/3364532

### 13. Supporting sources
- **Rutqvist et al. (2026)**, *J. Energy Storage*. High-temperature aquifer storage (up to 90 °C) at Geostorage Forsthaus, Bern. Safe operation needs sand lenses inside a clay seal plus active pressure control. https://doi.org/10.1016/j.est.2026.123303
- **Mello et al. (2026, NLR/USGS)**, *Renewable Energy*. Ten-city screening finds storage fraction is the main economic lever. https://doi.org/10.1016/j.renene.2026.125540
- **JPT (Feb 2024) on XGS**. Targets thick homogeneous granite or basalt basement and says it must "go deeper… until we reach a certain temperature". LCOE targets are $35/MWh (existing wellbores) and $50/MWh (new). https://jpt.spe.org/hot-rock-slurry-developer-of-emerging-geothermal-tech-readies-for-field-tests

## What resource characteristics each needs

| Technology | Needs | Scarce element |
|---|---|---|
| Eavor (multilateral U-loop) | High gradient (≥60 °C/km for competitive power), drillable hard rock, long lateral room, 4.5 to 7.5 km | Shallow heat; land footprint for km-scale lateral arrays |
| XGS (single-well + conductive slurry) | Thick homogeneous hot basement; existing wellbores preferred ($35 vs $50/MWh) | Hot existing wells (abandoned geothermal/O&G) |
| GreenFire (coaxial retrofit) | Existing hot well, ideally in a convecting reservoir (≥100 mD helps per Hakes) | Known hydrothermal fields and legacy wells |
| Sage (pressure geothermal/EarthStore) | Rock above 150 to 180 °C at 3 to 5 km (power); deep tight high-stress rock and P&A wells (storage) | 2 to 3 km depth-to-180 °C tier (53 GW); legacy wells |
| GeoTES/RTES | Permeable reservoir with closure plus seal; depleted O&G fields | Depleted-field pore space and wells |

## Does "any hot rock" kill rights scarcity?

No. Three reasons:

1. **The physics is conduction-limited.** Output and cost track rock temperature at drillable depth, and neither conductivity tweaks (+7 to 20%) nor drilling-cost cuts (−28%) change that. Literature LCOEs for CLG power run $136 to $560/MWh at moderate gradients, so CLG power only pencils at the hottest shallow sites.
2. **The cheapest tier of "anywhere" rock is small.** In Sage's own numbers, 2 to 3 km depth to 180 °C is 53 GW, about 1.3% of the L48 potential.
3. **Revealed preference shows the developers going back to known heat and existing wells:**
   - Sage chose Ormat's Blue Mountain field.
   - GreenFire tests inside Coso.
   - XGS prices existing wellbores 30% cheaper.
   - Eavor-Deep and the Geretsried project sit in high-heat or known-aquifer settings.

So next-generation technology *widens the buyer pool* for the same high-gradient parcels and *adds new rights classes*: legacy wells, depleted reservoirs and storage-capable tight rock. It does not flatten their value. The one real risk is to *low-temperature direct-use* rights. Closed-loop heat at 30 °C/km is cheap almost anywhere, so heat-only parcels lose scarcity (unverified at portfolio scale).

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

- **The thesis holds and gets broader.** The target asset is the "top-percentile thermal parcel": highest temperature at the shallowest depth, mapped from BHT, temperature-gradient-hole and geophysics data. That parcel is valuable *however* it is later developed: hydrothermal (Zanskar/Ormat), EGS (Fervo), pressure geothermal (Sage) or closed loop (Eavor/XGS). The Stanford/SMU temperature-at-depth models (400,000+ BHTs, used by Sage itself) are exactly the public-but-illegible data layer. An ML layer that sharpens the depth-to-180 °C map at parcel scale directly prices land into the 53 GW tier.
- **Adjacent rights the literature flags as scarce, which Zanskar does not target:**
  1. **Legacy hot wellbores.** P&A oil, gas and geothermal wells are valuable to XGS and GreenFire (retrofit), Sage (EarthStore) and GeoTES. They are acquirable cheaply through state plugging programmes and orphan-well inventories.
  2. **Depleted reservoirs with closure and seal** for GeoTES/RTES. Storage adds up to $470 to $703/kW per NLR.
  3. **Deep tight high-stress sedimentary rock** in ERCOT for pressure geothermal and storage. Texas permitting takes "weeks".
- **Gap vs Zanskar.**
  - Zanskar's model is *find convective blind hydrothermal systems, then build and operate plants* (Big Blind, Lightning Dock). By physics, its targets are permeable reservoirs. Those are also the only places closed loop gets a convection bonus (≥100 mD), so CLG is complementary to Zanskar, not competitive with it.
  - Zanskar does not appear to aggregate (unverified as to its land book):
    - *conduction-dominated hot dry rock*, which is the EGS/CLG/Sage buyer pool and the majority of the TW-scale resource
    - *legacy-well and storage rights*
    - the *east-of-Rockies* and ERCOT parcels where Meta's Sage PPA sits
  - A Terranox-shape company can be the **land and data-room supplier to the entire next-generation developer set**, i.e. Fervo, Sage, XGS, Eavor and Quaise. That set has raised more than $700M combined (Eavor $529M, XGS $56.7M, GreenFire $19M, plus Sage/Fervo) and has hyperscaler PPAs (Meta 2 × 150 MW, Google 115 MW). Each developer needs specific top-tier parcels.
- **Kill-check against "too small":** it passes. The asset base is GW-scale: 53 GW cheapest tier plus 562 GW next tier, before hydrothermal.
- **Main risk:** if superhot drilling or CLG drilling costs collapse (below $200/m laterals at 7+ km), the scarcity premium compresses toward the 3 to 5 km tier. That tier is still finite and still ranked by gradient.

## Sources
- https://www.osti.gov/servlets/purl/3014949 (NLR 2025 U.S. Geothermal Market Report)
- https://doi.org/10.1016/j.geothermics.2021.102318 (Beckers et al. 2022; via the market report)
- https://www.osti.gov/biblio/1837565 (White et al. 2021, CLGWG)
- https://doi.org/10.1016/j.geothermics.2023.102852 (White et al. 2024)
- https://www.osti.gov/servlets/purl/2586305 (Hakes et al. 2024)
- https://www.osti.gov/biblio/2324601 (Beckers, Ketchum, Augustine 2024)
- https://www.osti.gov/biblio/2476300 (Akindipe et al. 2024)
- https://www.osti.gov/biblio/3408143 (Mibei et al. 2026)
- https://www.osti.gov/servlets/purl/3388421 (Frash 2024/2026)
- https://cdn.prod.website-files.com/67c9634e56bc9ae5113f2fcb/67e6c076244be58baf21aa7f_Stanford%202025.pdf (Anderson et al. 2025, Sage)
- https://cdn.prod.website-files.com/67c9634e56bc9ae5113f2fcb/67e6bfab995eb743d94983c9_2023_GRC_SageGeosystems_EnergyStorageInDeepHydraulicFractures_2023.09.08.pdf (Simpkins et al. 2023, Sage)
- https://www.sagegeosystems.com/projects ; https://www.sagegeosystems.com/technology
- https://www.osti.gov/servlets/purl/3377911 (Halloran et al. 2026)
- https://www.osti.gov/servlets/purl/2001115 (Zhu et al. 2023)
- https://www.osti.gov/biblio/3364532 (McTigue et al. 2026)
- https://doi.org/10.1016/j.est.2026.123303 (Rutqvist et al. 2026)
- https://doi.org/10.1016/j.renene.2026.125540 (Mello et al. 2026)
- https://jpt.spe.org/hot-rock-slurry-developer-of-emerging-geothermal-tech-readies-for-field-tests (XGS, JPT 2024)
- https://xgsenergy.com/
