# D10: Satellite and airborne public data for geothermal exploration (thermal IR, InSAR, hyperspectral/EMIT, gravity, aeromag/Earth MRI)

*Method note: the shared WebSearch budget (200 calls per turn) was used up before this agent's first query, so no open web searches ran. Sources were found through primary catalogues (OSTI.gov API, Crossref, Semantic Scholar metadata, USGS Publications Warehouse) and by fetching primary pages directly (USGS, NASA JPL). Sibling file L14-geophysics.md had already read the BRIDGE report, Kraal & Schwering 2024, Faulds 2021 and Trainor-Guitton 2025 in full; facts taken from those reads are cited to the same OSTI records. Where only metadata could be fetched, contents are marked (unverified). Sensor facts recalled from general knowledge and not re-fetched in this pass are marked (unverified).*

---

## 1. Bottom line

- **Satellite data cannot see a truly blind geothermal system directly.** Blind systems have no surface heat, springs or sinter, by definition. Thermal IR picks up only systems that already leak heat. InSAR mostly sees fields that are already producing. Satellite hyperspectral (EMIT, 60 m) is too coarse for the small 1–500 m² alteration patches that point to blind systems.
- **The signal that is useful and public is airborne, plus indirect satellite products.** It comes from (a) airborne EM, magnetics and radiometrics now being flown under USGS Earth MRI; (b) airborne hyperspectral (AVIRIS, plus Earth MRI hyperspectral); (c) gravity and aeromagnetic grids, which the Nevada play fairway work weights heavily; and (d) geodetic strain and dilation from GPS and InSAR, used as permeability features.
- **For an ML system, remote sensing works as a prior and a filter, not a discoverer.** It narrows a basin of thousands of km² to targets of a few km² that shallow temperature surveys and TG holes then prove. The Sandia BRIDGE workflow and the DOE play fairway workflow are both built this way.

---

## 2. Sensor-by-sensor evidence

### 2.1 Thermal infrared: ASTER, Landsat 8/9 TIRS, ECOSTRESS, MODIS

**Specs (public, free)**
- **ECOSTRESS** (on the ISS since July 2018) has five TIR channels between 8 and 12 µm (Silvestri et al. 2020, https://doi.org/10.3390/rs12010184) at about 70 m resolution. NASA reports more than 670,000 scenes. https://ecostress.jpl.nasa.gov/
- **ASTER TIR** has 90 m pixels and five bands (unverified in this pass). The ASTER SWIR bands, which mapped alteration, failed in 2008, so the SWIR archive covers only 2000–2008 (unverified in this pass; widely documented).
- **Landsat 8/9 TIRS** has 100 m native resolution, resampled to 30 m, and a 16-day revisit per satellite (unverified in this pass).

**Key papers**
- **Coolbaugh, Kratt, Fallacaro, Calvin & Taranik (2007), *Remote Sensing of Environment*: "Detection of geothermal anomalies using ASTER thermal infrared images at Bradys Hot Springs, Nevada."** It has 142 citations and is the classic Great Basin TIR demonstration. Night-time ASTER TIR, after correcting for topography, albedo and thermal inertia, picks out ground heated by a few °C over a known field (contents unverified; abstract not retrievable). https://doi.org/10.1016/j.rse.2006.09.001
- **Vaughan et al. (2012), JVGR, at Yellowstone**: ASTER radiant heat flux was about 2.0 GW, only **30–45%** of the geochemical heat budget. MODIS at 1 km is dominated by seasonal cycles (via L14). https://doi.org/10.1016/j.jvolgeores.2012.04.022
- **Wei et al. (2026), *Remote Sensing* 18(9):1362**: the paper gives the signal-to-noise problem in numbers. The geothermal surface signal is **typically 1–3 °C**, while the seasonal amplitude is **>20 °C**. The authors fitted an annual sinusoid to about 50 cloud-free Landsat 8 scenes on Google Earth Engine over the Shanxi Graben, after correcting for elevation (−4 °C per 100 m), slope and aspect. Over known fields with >100 °C at 100 m depth they recovered a background-temperature (T0) offset of only **+1–2 °C (3–5%)** and an amplitude deficit of about **2 K**. https://doi.org/10.3390/rs18091362
- **Soszynska et al. (2024), *RSE* 114103**: ECOSTRESS LST anomalies at Olkaria, Kenya, a high-enthalpy field with surface expression (abstract not retrieved). https://doi.org/10.1016/j.rse.2024.114103
- **Silvestri et al. (2020)**: a cross-calibration of ECOSTRESS, ASTER and Landsat 8 over Italian volcanic and geothermal areas, including the Biancane geothermal area. It shows ECOSTRESS adds denser revisits at different times of day, including diurnal coverage. https://doi.org/10.3390/rs12010184

**Limits**
- TIR detects only systems with surface heat. Even at Yellowstone, the strongest case on Earth, it captures 30–45% of the heat.
- Most Great Basin blind systems are capped by cool groundwater and alluvium. The Gabbs Valley blind discovery was found with a 2 m probe temperature survey, not with satellite TIR (Faulds 2021, https://www.osti.gov/biblio/1724080).
- Value for blind exploration: **low**. Its best use is as a negative or noise filter, and for finding small leaking fault segments that are worth a 2 m survey.

### 2.2 InSAR: Sentinel-1, ALOS, TerraSAR-X, NISAR

- **Ali, Akerley, Feigl et al. (2016), *Geothermics* 61**: used ERS-2, Envisat, ALOS and TerraSAR-X/TanDEM-X data from **2004–2014** at Brady Hot Springs. They found a **~4 km × 1.5 km elliptical subsidence bowl** aligned with the dominant normal-fault strike, with smaller features at about 1 km scale. Modelling places the contraction at **≤600 m depth**, in damaged fault-interaction zones that act as "high permeability conduit[s] to the production wells". Deformation rate correlates with shallow-well production rate. https://doi.org/10.1016/j.geothermics.2016.01.008
- **Coso (Eneva et al., GRC Trans 42)**: maximum subsidence was **−27.6 mm/yr (Envisat)** and **−19.1 mm/yr (Sentinel)** (via L14).
- **Los Humeros, Mexico (Békési et al. 2019, *Geofluids*)**: PS-InSAR measured **≤8 mm/yr** of subsidence from 2003 to 2007 against **5×10⁶ m³/yr** of production. The pattern shows reservoir compartments bounded by sealing faults. https://doi.org/10.1155/2019/2306092
- **Reinisch et al. (2024, LANL)**: a deep-learning InSAR denoiser recovers **±2.5 mm** of deformation (via L14). https://www.osti.gov/biblio/2426558

**Limits**
- These InSAR signals need production to happen. An untouched blind reservoir does not deform measurably, so InSAR is a **monitoring and reservoir-characterisation tool** for an asset owner.
- The exploration value is indirect. Geodetic strain and dilation rates, mostly from GPS today, are features in the Nevada play fairway model and in INGENIOUS. Trainor-Guitton et al. (2025) list geodetic shear and strain among their importance features (https://www.osti.gov/biblio/3018341).
- A free, basin-scale InSAR strain and fault-creep layer for the Great Basin, built from Sentinel-1 and now NISAR (launched 2025, L-band; unverified in this pass), is an under-built input (inference).

### 2.3 Hyperspectral: airborne AVIRIS/HyMap/ProSpecTIR, satellite EMIT, ASTER SWIR

**EMIT specs** (USGS OFR 2021-1030-R, https://pubs.usgs.gov/publication/ofr20211030R/full)
- Range **380–2,500 nm**, 7.5 nm sampling and **60 m GSD**.
- **70 km swath**, ISS orbit covering **52°N–52°S**, launched **14 July 2022**.
- Radiometry agrees with RadCalNet to within 5% across most channels.
- JPL says EMIT is in an extended mission "through at least 2026" and focuses on arid dust-source regions, which include the Great Basin. https://earth.jpl.nasa.gov/emit/

**Key papers**
- **Kratt, Calvin & Coolbaugh (2010), *RSE***: mapped hydrothermal alteration and chemical precipitates (tufa, sinter) in the Pyramid Lake basin, Nevada, and tied them to geothermal potential. It has 55–62 citations (abstract not retrieved). https://doi.org/10.1016/j.rse.2010.05.006
- **Littlefield & Calvin (2014), *RSE***: used AVIRIS, HyMap and ProSpecTIR data (0.4–2.5 µm) over Fish Lake Valley, NV, and **delineated four new exploration targets**. These were two new sinter/travertine areas northwest of the playa (Pleistocene, fault-controlled), previously undocumented Miocene travertine in the Emigrant Hills, and argillic alteration in the ranges. Results were verified in the field with a portable spectrometer. https://doi.org/10.1016/j.rse.2013.09.007
- **Kraal & Schwering (2024, Sandia, GRC Trans 48)**: compared AVIRIS-Classic (225 channels, 14 m) with the USGS ASTER alteration map (30 m argillic/phyllic, 90 m silica).
  - Hyperspectral **found altered outcrops that ASTER missed**.
  - The best blind-system clues are **1–500 m²** exposures in the footwalls of Quaternary faults. These are too small for ASTER and, by implication, for 60 m EMIT.
  - The authors expect more blind discoveries "as additional high-quality, publicly available hyperspectral data is acquired … (e.g., through the USGS Earth MRI program, and new satellites)." https://www.osti.gov/biblio/3009542
- **Cavur, Yu, Demir & Duzgun (2024), *Remote Sensing* 16(7):1223 (Colorado School of Mines, DOE-funded)**: ASTER at Coso with a local spectral library built from 97 field samples. Overall accuracy was **96% kaolinite, 95% opal, 87% alunite, 83% chalcedony and 60% hematite**, and fusing algorithms beat any single one. https://www.osti.gov/biblio/2331359
- **Moraga, Duzgun, Cavur & Soydan (2022), *Renewable Energy***: a "Geothermal AI" over Brady (surface expression) and Desert Peak (blind), using satellite mineral markers, LST, faults and InSAR deformation. It reached **92–95% accuracy** within a site and **72–76%** when trained on one site and tested on the other. https://doi.org/10.1016/j.renene.2022.04.113 ; https://www.osti.gov/biblio/1867408
- **Demir et al. (2024), *Energies* 17:3255**: the same approach across Brady, Desert Peak and Coso. Desert Peak and Coso transfer to each other, but **Brady is incompatible with both**. Satellite-only models generalise poorly across system types. https://www.osti.gov/biblio/2382838

**Limits**
- These methods find **fossil or leaking** systems (sinter means a reservoir above ~175 °C at some past time).
- Signals are lost under alluvium, playa and vegetation.
- EMIT's 60 m pixel is good for regional screening of silica, kaolinite and carbonate, but misses small fault-footwall patches. Airborne data at 1–15 m is the workhorse.

### 2.4 Gravity and aeromagnetics, including Earth MRI

- **Nevada play fairway (Faulds et al. 2021)**: the 96,000 km² model uses 9 parameters, including **gravity gradients**. The SE Gabbs Valley blind system was flagged by intersecting and terminating gravity gradients plus a **magnetic low**. TG holes reached **124 °C at 152 m**. https://www.osti.gov/biblio/1724080
- **Phase II field work**: 237–415 new gravity stations per area, plus 728 Ormat gravity points and about 145 line-km of Ormat magnetics shared (via L01). https://www.osti.gov/biblio/1724099
- **Don A. Campbell (Ormat)**: a mining-industry aeromagnetic survey showed a **4 × 1.5 km magnetic low**, which was later validated petrologically against drill core. That is mining-assessment geophysics finding a 42 MW blind field. https://www.osti.gov/biblio/17315922
- **USGS Earth MRI** is a USGS Mineral Resources Program initiative. Since 2019 it has collected geophysics (airborne magnetics, radiometrics, EM), lidar, hyperspectral and geochemistry, prioritising critical-mineral areas. Its page **does not mention geothermal**. https://www.usgs.gov/special-topics/earth-mri
- **Sandia BRIDGE (2025)**: a regional HTEM survey like BRIDGE's (3,000 km², 1,877 line-km in 12 days) "will become publicly available as part of the USGS Earth Mapping Resources Initiative" for "most of the US Great Basin that is prospective for hidden geothermal systems," together with lidar, magnetics and gamma-ray data. https://www.osti.gov/biblio/2540220
- **Folsom et al. (2024)**: HTEM is the better *search* tool for the conductive smectite clay cap above blind systems, while MT is better for targeting. MT spaced more than 1 km apart "can easily miss" alteration footprints under 2 km². https://www.osti.gov/biblio/3683813
- **GRACE**: excluded. Its ~300+ km resolution is useless at prospect scale (unverified).

### 2.5 ML stacks that use these layers

- **INGENIOUS / Trainor-Guitton et al. (2025)**: 48 features and 37 positive plants. The top features are surface and lower-crust conductivity, elevation trend and distance to young faults. Heat flow and MT mantle conductivity also rank high. Remote-sensing TIR and hyperspectral are not the drivers. https://www.osti.gov/biblio/3018341
- **LANL GeoThermalCloud** (Frash, Ahmmed et al. 2024): unsupervised ML over geology, geochemistry, geophysics, satellite and airborne data to find "hidden geothermal signatures". https://www.osti.gov/biblio/2480434

---

## 3. Scorecard for blind-system discovery

| Layer | Resolution | Cost | Blind signal | Role |
|---|---|---|---|---|
| ASTER/Landsat/ECOSTRESS TIR | 70–100 m | Free | Weak (1–3 °C vs >20 °C seasonal noise) | Filter, leaky-segment flags |
| InSAR (Sentinel-1/NISAR) | ~10–30 m, mm/yr | Free | Indirect (strain); strong for monitoring | Permeability feature; asset monitoring |
| EMIT satellite hyperspectral | 60 m | Free | Moderate for fossil sinter/argillic; misses small patches | Regional mineral screen |
| AVIRIS/airborne hyperspectral | 1–15 m | Free where flown | Moderate–good (Fish Lake Valley gave 4 new targets) | Prospect-scale |
| Gravity grids | km-scale public; denser where surveyed | Free / cheap infill | Strong (PFA weighted layer) | Structure |
| Aeromag (USGS, Earth MRI, mining) | Line spacing 100s of m | Free | Moderate (magnetic lows from alteration) | Structure and alteration |
| Earth MRI AEM | Soundings ~30 m apart, lines ~km | Free as released | **High** (clay cap) | Best new public search layer |

---

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **Satellite data is table stakes, not a moat.** Every serious player, Zanskar included, ingests satellite, gravity and magnetic grids. Zanskar says publicly that it uses "geological data, satellite data" and "newer satellite and remote sensing databases" (Z03). TIR and InSAR have a low ceiling for blind systems, so a pitch built on "AI on satellite imagery" would be weak and easy to copy. Do not lead with it.
2. **The Terranox-shaped data event is Earth MRI.** It is government-funded, collected for *another commodity* (critical minerals), released basin by basin, and absent from geothermal workflows: the Earth MRI page does not mention geothermal. The released layers are AEM, high-resolution magnetics, radiometrics and hyperspectral. BRIDGE says the AEM will cover most of the prospective Great Basin, and AEM is the best search tool for the clay cap. This is the closest analogue to SMAD becoming public after 3 years. The play is **release-triggered acquisition**: ingest each Earth MRI block on release day, rank conductive anomalies against faults, gravity gradients and magnetic lows, and file BLM nominations or private-rights deals before anyone else reads the data.
3. **Mining geophysics is the second illegible pile.** Don A. Campbell, a 42 MW field, was a blind discovery flagged by a *mining-industry* aeromagnetic low and mining holes. Converting scanned assessment-file geophysics (IP/resistivity, mag, drill temperatures) into features is Terranox's existing skill.
4. **The gap vs Zanskar.** Zanskar is vertically integrating into drilling, its own field crews (100 sq mi of shallow holes at Big Blind), its own seismic arrays and plant ownership (Lightning Dock). Its edge is field data per prospect and capital. It does not publicly describe systematic first-reader ingestion of new public airborne releases or of mining-assessment scans (Z03).
   - A Terranox shape wins on **breadth and speed to rights**: hundreds of cheap leases on Earth MRI and mining-data anomalies, each proven with 2 m surveys and shallow TG holes (Gabbs: 124 °C at 152 m), then sold or partnered at a step-up to Zanskar, Ormat, Fervo or utilities.
   - Once it owns producing assets, InSAR becomes an owner's cheap monitoring tool rather than an exploration claim.
5. **Risks**
   - Satellite-only ML transfers poorly between sites (Brady was incompatible with Coso and Desert Peak).
   - Labels are scarce (37 plants).
   - Earth MRI release timing and Great Basin coverage are not confirmed in this pass (unverified).
   - BLM competitive leasing means first-mover advantage decays from the release date.

---

## Sources
- Coolbaugh et al. 2007, ASTER TIR Bradys: https://doi.org/10.1016/j.rse.2006.09.001
- Vaughan et al. 2012, Yellowstone TIR: https://doi.org/10.1016/j.jvolgeores.2012.04.022
- Wei et al. 2026, Landsat time-series TIR: https://doi.org/10.3390/rs18091362
- Soszynska et al. 2024, ECOSTRESS Olkaria: https://doi.org/10.1016/j.rse.2024.114103
- Silvestri et al. 2020, ECOSTRESS/ASTER/Landsat comparison: https://doi.org/10.3390/rs12010184
- ECOSTRESS: https://ecostress.jpl.nasa.gov/
- Ali et al. 2016, InSAR Brady: https://doi.org/10.1016/j.geothermics.2016.01.008
- Békési et al. 2019, PS-InSAR Los Humeros: https://doi.org/10.1155/2019/2306092
- Reinisch et al. 2024, InSAR denoising: https://www.osti.gov/biblio/2426558
- EMIT system characterization (USGS OFR 2021-1030-R): https://pubs.usgs.gov/publication/ofr20211030R/full
- EMIT mission: https://earth.jpl.nasa.gov/emit/
- Kratt et al. 2010, Pyramid Lake: https://doi.org/10.1016/j.rse.2010.05.006
- Littlefield & Calvin 2014, Fish Lake Valley: https://doi.org/10.1016/j.rse.2013.09.007
- Kraal & Schwering 2024, hyperspectral Basin & Range: https://www.osti.gov/biblio/3009542
- Cavur et al. 2024, ASTER mineral fusion at Coso: https://www.osti.gov/biblio/2331359
- Moraga et al. 2022, Geothermal AI: https://www.osti.gov/biblio/1867408
- Demir et al. 2024, AI transferability: https://www.osti.gov/biblio/2382838
- Faulds et al. 2021, Nevada PFA: https://www.osti.gov/biblio/1724080
- Faulds et al. 2016, PFA Phase II: https://www.osti.gov/biblio/1724099
- Don A. Campbell petrologic validation: https://www.osti.gov/biblio/17315922
- BRIDGE 2025: https://www.osti.gov/biblio/2540220
- Folsom et al. 2024, HTEM vs MT: https://www.osti.gov/biblio/3683813
- Trainor-Guitton et al. 2025: https://www.osti.gov/biblio/3018341
- GeoThermalCloud 2024: https://www.osti.gov/biblio/2480434
- USGS Earth MRI: https://www.usgs.gov/special-topics/earth-mri
- USGS 2008 assessment: https://pubs.usgs.gov/fs/2008/3082/
