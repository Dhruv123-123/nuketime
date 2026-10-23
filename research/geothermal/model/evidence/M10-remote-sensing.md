# M10: Remote sensing for blind hydrothermal systems (thermal IR, hyperspectral, InSAR, ET, vegetation, snow)

Date: 23 Oct 2026. This file builds on `../../evidence/D10-satellite.md`, which already covers sensor specs, the classic papers (Coolbaugh 2007 at Bradys, Vaughan 2012 at Yellowstone, Ali 2016 InSAR at Brady, Littlefield and Calvin 2014, Kraal and Schwering 2024, the Moraga and Demir "Geothermal AI" transfer tests) and the scorecard. It does not repeat them. This file asks a narrower question: **what is the physical detection limit of each remote method for a truly blind system, and how should remote sensing enter a better "how much hidden hydrothermal is there" model?** Web budget used: 8 searches and 9 fetches. Physics estimates are my own arithmetic from textbook constants and are marked (calc). Anything recalled and not re-fetched is marked (unverified).

## Bottom line

Satellite remote sensing cannot see most truly blind systems, and the reason is physics. A pixel's skin temperature is set by a surface energy balance that moves about 10 to 20 W/m² per kelvin. So a 1 K satellite anomaly needs roughly 10 to 20 W/m² of extra heat coming up. That is 100 to 300 times normal heat flow (0.06 to 0.09 W/m²). A typical Great Basin blind upflow under a cool aquifer pushes perhaps 0.3 to 3 W/m² through the ground surface, so it makes a skin anomaly of only about 0.02 to 0.3 K (calc). The noise is 1 to 2 K per scene, and the seasonal swing is more than 20 K. The 2 m probe works where satellites fail because, at 2 m, the same 1 to 3 W/m² gives a 1 to 5 K anomaly with very little seasonal noise. Satellites still earn a place in three ways. (1) **Stacked thermal time series** (hundreds of Landsat and ECOSTRESS scenes, with a physics model of solar heating removed) push the noise floor down toward a few tenths of a kelvin. That is good enough to flag the leakiest 10 to 20% of blind systems, and to say "nothing leaking here" everywhere else, which is still useful as a weak negative. (2) **Hyperspectral mineral maps find fossil or leaking systems that the heat maps call blind.** Columbus Salt Marsh, Nevada, was a new blind system found by 4 m airborne hyperspectral, then confirmed by about 100 two-metre probes, which showed a 4.1 × 1.7 km warm area. (3) **Snow and InSAR are under-used integrators.** Snow at 0 °C adds up a small heat flux over a whole winter, so a few W/m² melts tens of mm of snow water per season (calc). That makes earlier melt-out a possibly more sensitive blind-heat detector than skin temperature (inference, untested). NISAR L-band data went public in July 2026, which gives a new free layer of fault creep and strain. The model should not use remote sensing as a "hot or not" label. It should enter as **physics-aware likelihood terms with explicit detection probabilities**: P(seen | system, cap depth, flux, cover). Each blind discovery then tells the model how many similar systems the satellites missed. That missed fraction is what sizes the hidden resource. The sensor that fills the gap is not a satellite. It is our 2 m probe carpet, used as ground truth to train the satellite residuals, plus a cheap drone pass (pre-dawn thermal and SWIR spectrometer) on the same ranch visit.

## Findings

### F1. The detection limit of skin thermal IR, in numbers
- **Energy balance (calc).** Radiative sensitivity is 4εσT³ ≈ 5.5 W/m²/K at 290 K. Add convective and latent exchange (about 5 to 15 W/m²/K on calm pre-dawn nights) and you get h ≈ 10 to 20 W/m²/K. So ΔT_skin ≈ Δq / h.
- **Measured thresholds agree.** In the Kenyan Rift, Romaguera et al. (2018) needed a mean geothermal LST residual of **≥ 2 K** (with temporal SD ≤ 1.5 K) to call a pixel geothermal. They found about **1.7 K** inside the Olkaria–Menengai field boundaries versus 1.2 K outside, and local maxima above 5 K. ASTER radiant flux over Olkaria was **9 to 24 W/m²**. Olkaria is a high-enthalpy field with surface expression, i.e. the easy end. https://ris.utwente.nl/ws/files/72985263/Romaguera2018detecting.pdf
- **The Landsat time-series fit** (Wei et al. 2026, in D10) recovered only **+1 to 2 °C** of offset over fields with more than 100 °C at 100 m depth.
- **What a blind system gives (calc).** Take a cool aquifer capping a 150 °C upflow, with a near-surface gradient of 0.2 to 2 K/m and k = 1.5 W/m/K. That gives q ≈ 0.3 to 3 W/m², and so ΔT_skin ≈ 0.02 to 0.3 K. At 2 m depth the same system gives ΔT ≈ 0.4 to 4 K, and the seasonal wave at 2 m is damped to a few K and is predictable. This is why Gabbs Valley and Columbus Salt Marsh were confirmed with 2 m probes and not with satellites (Faulds 2021, via D10).
- **Airborne TIR does better on resolution, not on physics.** The DOGAMI Summer Lake survey (night, winter, −5 to −8 °C air, 8 to 9.2 µm, lidar co-registered, 0.5 °C accuracy) found 37 warm springs and a 6 to 8 K anomaly along the Summer Lake fault. It also found false anomalies of 3 to 10 K from basalt, dunes and stream mouths (emissivity and thermal-inertia artifacts). Those false anomalies are as big as the real one. https://www.oregon.gov/dogami/gtilo/data/supplemental/ARRA_Using_Airborne_Thermal_Infrared.pdf

### F2. Stacking beats single scenes, and that is the satellite model to build
- **Yuan et al. (SGW 2026)** split the Landsat 8/9 LST stack into a solar part (which varies) and a geothermal part (stable over human time). They then flagged pixels that stay warm across the whole stack at Mount Meager, Burwash Landing and Cornwallis Island. They found four anomaly types, and only two were geothermal: surface discharge and deep fault-controlled heat. The others were landslides and scarps, drainage, and human heat. The paper reports no validated magnitudes. https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Yuan.pdf
- **Noise floor (calc, optimistic).** Landsat 8 and 9 together give about 45 scenes per year, perhaps 20 of them clear and at night or dawn-like in the Great Basin (unverified). ECOSTRESS adds scenes at varying times of day, including pre-dawn. If errors were random, 200 scenes would cut 1.5 K noise to about 0.1 K. In practice, soil moisture, emissivity and topographic shading are correlated errors, so a realistic floor is about 0.2 to 0.5 K (inference). That catches the upper end of blind fluxes (≥ 3 to 5 W/m²): leaky fault segments and outflow plumes.
- **Better geography is coming.** TRISHNA (CNES/ISRO, 57 m, planned Oct 2027) is listed on https://en.wikipedia.org/wiki/TRISHNA. ESA LSTM (about 50 m, almost daily) and NASA SBG-TIR (about 60 m) are planned for around 2029 to 2030 (unverified). A pipeline built now gets better every year with no new capex.

### F3. Hyperspectral: the remote method with real blind discoveries
- **Columbus Salt Marsh, Esmeralda County, NV.** ProSpecTIR VS2 at **4 m over 380 km²** (flown 2008) mapped borate and sulfate evaporites, opal/chalcedony, carbonates and argillic alteration. The maps guided about **100 two-metre temperature points**, which found a **4.1 × 1.7 km** anomaly. A cold spring nearby gave geothermometers of **115 °C (quartz)** and **137 °C (Mg-corrected Na-K-Ca)**. Title per DRI: "Identification of a new blind geothermal system with hyperspectral remote sensing and shallow temperature measurements at Columbus Salt Marsh". https://www.dri.edu/publication/3786 ; https://www.gisresources.com/identification-of-a-new-blind-geothermal-system-with-hyperspectral-remote-sensing/
- **This is the exact funnel the company wants:** cheap public pixels → 2 m probes → rights. Hyperspectral picks up *chemical* traces (evaporites, opal, alteration) that outlive the heat, or that sit downflow of it, so it is not bound by the skin-temperature physics in F1.
- **EMIT and PRISMA at 30 to 60 m now map alteration well in arid belts.** Almasi et al. (2026, J. Asian Earth Sci. X 15:100221) used combined EMIT and PRISMA to map argillic, advanced argillic, propylitic, gossan and carbonate-zeolite zones along faults in central Iran (no accuracy numbers reported). https://pure.kfupm.edu.sa/en/publications/integrated-emit-and-prisma-hyperspectral-analysis-for-mapping-hig/
- **The weak spot is pixel size.** The best blind-system clues are 1 to 500 m² footwall patches (Kraal and Schwering, via D10). A 60 m EMIT pixel is 3,600 m², so a 100 m² opal patch is under 3% of the pixel. That is at or below typical unmixing limits (unverified, about 5 to 10%). EMIT is a regional screen. The airborne data (AVIRIS-classic/NG/3, NASA–USGS GEMx flights over the arid West, 2023 onward (unverified), Earth MRI hyperspectral) is the prospect tool.
- **USGS multiscale work at Yellowstone** ties satellite, airborne and field spectra together and shows how alteration grades with scale. https://pubs.usgs.gov/publication/70237672

### F4. InSAR: a strain and creep layer, not a heat detector
- An untouched blind reservoir does not move enough to see. Production-driven bowls at Brady and Coso (mm to cm per year, D10) only appear after pumping starts.
- **NISAR L-band data has been public since 20 July 2026** through ASF DAAC: GUNW interferograms, GSLC, offsets and soil moisture. It images each place twice every 12 days, through cloud. The full first-year record is due by the end of 2026. https://www.earthdata.nasa.gov/news/nisar-l-band-data-released-expanding-record-surface-changes ; https://asf.alaska.edu/notices/nisar-l-band-data-now-publicly-available/
- **Uses for us.**
  - (a) Fault-creep and dilation maps at valley scale, as permeability features. Geodetic strain is already an importance feature in INGENIOUS and play fairway work (via D10).
  - (b) Market intelligence: subsidence or uplift shows which neighbour fields are being produced or injected, and how hard.
  - (c) The L-band soil-moisture product helps strip soil-moisture noise from thermal residuals (F2).
- **Detection limit.** Natural tectonic strain in the Great Basin is about 10⁻⁸ per year, i.e. 1 to 10 mm/yr over basins (unverified). Single-fault creep under about 1 mm/yr is near the floor of Sentinel-1 or NISAR stacks (LANL denoiser ±2.5 mm, D10).

### F5. Evapotranspiration and vegetation: weak, indirect and confounded
- **ET.** Satellite ET (OpenET, 30 m Landsat-based) maps groundwater discharge areas (phreatophytes, wet meadows). USGS uses this to budget Great Basin groundwater (https://pubs.usgs.gov/wri/wri014195). Geothermal outflow plumes often surface in those same discharge areas, but ET does not measure temperature. So ET is a *where the water comes out* layer: it locates where to probe the outflow. Its value comes from co-location with faults plus a thermal residual (inference).
- **Vegetation stress from soil CO2.** Airborne hyperspectral (Pika II, 0.33 m pixels) caught CO2-stressed plants within **5 days** of a 0.2 t/day release at the ZERT site. It used the red edge (750/674 nm, p < 0.001), but no flux threshold was set and there were false positives. https://remotesensing.montana.edu/documents/bellante_et_al_2013.pdf
  - Most blind Great Basin systems leak little CO2 through alluvium, and desert shrub cover is sparse. So the vegetation signal is very weak at 30 to 60 m and needs sub-metre data (inference).
  - Winter green-up or longer growing seasons over warm ground may be a better proxy, but this is untested (inference).

### F6. Snow and frost as heat integrators (new idea, untested)
- **Arithmetic (calc).** Latent heat of fusion is 334 kJ/kg. A steady 1 W/m² gives 86.4 kJ/m² per day, which melts **0.26 mm of snow water equivalent (SWE) per day**. Over a 100-day snow season, an upflow of 3 W/m² melts about **78 mm SWE**. That is comparable to a whole thin valley-floor snowpack in the northern Great Basin.
- **Why it works where TIR fails.** Snow sits at 0 °C, so the extra flux shows up as *timing* (earlier melt-out, patchy cover after storms), not as a skin temperature hidden in noise. Sentinel-2 (10 to 20 m, 5-day revisit, 2015 onward) and Landsat give cheap snow-cover time series.
- **Confounders.** Wind scour, aspect, shrub height, and solar heating of dark ground. These are partly removable with lidar terrain models and pairs of nearby pixels.
- **Status.** Snow-free patches are known over hot ground at Yellowstone and Long Valley (unverified for the literature). A systematic melt-out residual layer over the northern Great Basin, Oregon and Idaho does not seem to exist (inference). Frost or hoarfrost lingering on clear mornings is a similar integrator for drones.

### F7. ML evidence on remote layers (from D10, repeated only as numbers)
- Within one site, satellite-only models reach 92 to 95% accuracy. Across sites they reach 72 to 76%, and Brady does not transfer to Coso or Desert Peak.
- In INGENIOUS feature importance, TIR and hyperspectral are not drivers. Conductivity, faults and heat flow are.
- The lesson: raw pixels used as features overfit to site style. Detection-probability terms built from physics transfer better (inference).

## Datasets

| Dataset | Access | Coverage | Value for blind detection |
|---|---|---|---|
| Landsat 8/9 Collection 2 L2 LST (100 m native TIRS, 30 m grid) | Free, USGS EarthExplorer, Google Earth Engine, AWS | Global, 2013 onward (plus TM/ETM+ from 1984) | Stacked residuals flag leaky segments ≥ 3 to 5 W/m²; weak negative evidence elsewhere |
| ECOSTRESS L2 LST and ET (≈70 m, variable time of day) | Free, LP DAAC | ISS track 52°N to 52°S, 2018 onward | Pre-dawn and diurnal-phase scenes reduce solar noise; thermal-inertia features |
| ASTER TIR (90 m) and the SWIR archive (2000 to 2008) | Free, LP DAAC | Global | Night TIR history; ASTER alteration maps (USGS) for argillic and silica |
| EMIT L2A reflectance and L2B minerals (60 m) | Free, LP DAAC | Arid belts incl. Great Basin, 2022 onward | Regional screen for kaolinite, alunite, opal, carbonate, borate; misses small patches |
| PRISMA (30 m hyperspectral) | Free with registration, ASI | Tasked scenes | Fills 30 m gaps over targets |
| AVIRIS-classic/NG/3, GEMx, Earth MRI hyperspectral (1 to 15 m) | Free where flown, NASA/USGS | Patchy, growing across the arid Southwest and the Great Basin (unverified extent) | Best prospect-scale alteration and sinter layer; Columbus Salt Marsh-type finds |
| Sentinel-1 C-band InSAR (EGMS-like stacks; OPERA DISP-S1 for North America) | Free, ASF | 2014 onward, 6 to 12 days | Fault creep, strain, neighbour-field production |
| NISAR L-band (GUNW, GSLC, soil moisture) | Free since 20 Jul 2026, ASF | Global, 12-day | Better coherence over desert shrub; strain and soil-moisture correction |
| OpenET (30 m monthly ET) | Free, openetdata.org | Western 17 states, 1985 onward | Groundwater discharge areas, places to probe outflow plumes |
| Sentinel-2 MSI (10 to 20 m, 5-day) | Free, Copernicus | 2015 onward | Snow melt-out residual; red-edge vegetation stress; NDVI |
| DOGAMI and other state airborne TIR + lidar | Free, state portals | Oregon pilot areas (Summer Lake) | Night airborne TIR examples and false-positive library |
| Future: TRISHNA (57 m, ~2027), LSTM, SBG-TIR (~2029 to 2030) | Free (planned) | Global | Near-daily 50 to 60 m TIR makes stacking much stronger |

## What dominates uncertainty

1. **The flux-to-surface coupling of each blind system is unknown.** A cool aquifer or deep alluvium can swallow almost all the heat. Whether a system is "seeable" depends on cap depth and aquifer flow, not on reservoir size. So a satellite miss says little about size.
2. **Correlated noise in thermal stacks** (soil moisture, emissivity, thermal inertia, topographic shading) sets the real floor. Random error does not. We do not know whether the floor is 0.2 K or 0.8 K in Great Basin valleys, and it decides whether TIR catches 5% or 30% of blind systems.
3. **Mineral clues are not heat clues.** Sinter and argillic alteration may be fossil (dead systems), and evaporites may be cold-water playa chemistry. The live fraction of mapped alteration is unknown.
4. **There are almost no labelled negatives.** Nobody publishes "probed here, found nothing." So detection probabilities cannot be fitted yet.
5. **Coverage of airborne hyperspectral is patchy**, and release timing is unclear (unverified extent of GEMx and Earth MRI).

## What a sensor could fill

- **2 m probe carpet as the satellite's teacher.** Every 2 m probe reading is a ground-truth heat value under a pixel. A few thousand probes across many valleys let us fit P(thermal residual | 2 m anomaly) and the correlated-noise model. This turns the free 40-year Landsat archive into a calibrated likelihood everywhere else. This reuses the existing hardware pick (H01), with no new device.
- **Ranch-visit drone kit (≈$5k to $15k, unverified price).**
  - A radiometric LWIR camera (NETD ≤ 50 mK) for pre-dawn passes at 0.1 to 1 m. This beats the satellite pixel-mixing problem on small leaky fault segments, and with a frost or snow pass it reads the integrator signal.
  - A small SWIR spectrometer or line-scanner (1.0 to 2.5 µm) to catch 1 to 500 m² opal, alunite and kaolinite footwall patches that EMIT cannot resolve.
  - It flies on the same visit where the landman signs the heat option.
- **Snow-stake and time-lapse cameras ($100 each).** Cheap ground truth for the melt-out residual (F6) at a few known fields and controls.
- **Soil CO2 flux chamber (H04).** It tells us whether red-edge vegetation stress is worth chasing at all.
- **What not to build: our own satellite.** TRISHNA, LSTM and SBG will give near-daily 50 to 60 m TIR for free by about 2030. The edge is in calibration labels and physics, not pixels.

## Implications for a better model

1. **Model each remote layer as a detection process, not a feature.** For each candidate system i with latent flux q_i, cap depth d_i, cover c_i: P(TIR residual > τ | q_i, d_i, c_i), P(alteration seen | age, size, pixel), P(snow melt-out anomaly | q_i, snow regime). Non-detection then lowers, but does not zero, the probability of a system. Known blind discoveries (Gabbs, Columbus Salt Marsh, McGinness, Don A. Campbell) that satellites missed set the detection rate. In turn, that gives the multiplier from "seen" to "total" systems, which is the hidden-resource estimate itself.
2. **Build three new free layers that competitors do not publish:**
   - (a) a Great Basin physics-detrended LST residual stack (Landsat + ECOSTRESS, soil moisture from NISAR or SMAP);
   - (b) a Sentinel-2 snow melt-out residual;
   - (c) an EMIT plus airborne hyperspectral alteration-age map, with fossil vs live separated using co-located thermal and chemistry.
   Each costs only compute.
3. **Use thermal residuals mainly as negative and leakiness evidence.** A clean no-anomaly over a favorable fault setting says "deep cap or no system". Combined with resistivity (M08), that splits the two.
4. **Rank 2 m probe campaigns by value of information.** Probe where the remote likelihood is ambiguous (alteration but no thermal, or thermal but no alteration), because those labels teach the detection model the most.
5. **Re-run the pipeline on each new release** (NISAR backfill late 2026, new EMIT scenes, TRISHNA 2027), so the prior keeps improving and new anomalies trigger rights filings first.
6. **Do not pitch "AI on satellite imagery".** The detection floor makes it weak alone. The moat is the label set that pairs pixels with 2 m and well temperatures.

## Sources
- Romaguera et al. 2018, geothermal LST component in the Kenyan Rift: https://ris.utwente.nl/ws/files/72985263/Romaguera2018detecting.pdf
- Yuan et al. 2026, SGW, Landsat geothermal/solar decomposition: https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Yuan.pdf
- DOGAMI 2013, airborne TIR at Summer Lake: https://www.oregon.gov/dogami/gtilo/data/supplemental/ARRA_Using_Airborne_Thermal_Infrared.pdf
- Columbus Salt Marsh blind system (DRI record and summary): https://www.dri.edu/publication/3786 ; https://www.gisresources.com/identification-of-a-new-blind-geothermal-system-with-hyperspectral-remote-sensing/
- Almasi et al. 2026, EMIT plus PRISMA alteration: https://pure.kfupm.edu.sa/en/publications/integrated-emit-and-prisma-hyperspectral-analysis-for-mapping-hig/
- USGS multiscale hyperspectral, Yellowstone: https://pubs.usgs.gov/publication/70237672
- NISAR public release, July 2026: https://www.earthdata.nasa.gov/news/nisar-l-band-data-released-expanding-record-surface-changes ; https://asf.alaska.edu/notices/nisar-l-band-data-now-publicly-available/
- TRISHNA: https://en.wikipedia.org/wiki/TRISHNA ; https://cnes.fr/en/projects/trishna
- Bellante et al. 2013, hyperspectral CO2 vegetation stress: https://remotesensing.montana.edu/documents/bellante_et_al_2013.pdf
- USGS groundwater ET, Great Basin: https://pubs.usgs.gov/wri/wri014195
- Prior D10 sources (Coolbaugh 2007, Vaughan 2012, Wei 2026, Ali 2016, Kraal and Schwering 2024, Moraga 2022, Demir 2024, Faulds 2021): see `../../evidence/D10-satellite.md`
