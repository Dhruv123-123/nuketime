# L09: Temperature-at-depth mapping, BHT corrections, and ML temperature models

**Question:** How good are US temperature-at-depth maps? How noisy is the oil and gas bottom-hole temperature (BHT) record? What have recent ML models achieved? What does that mean for a "Terranox for geothermal" company that acquires rights before proof?

## 1. Executive summary

- The US BHT record is large but noisy. The NGDS reported **~530,000 borehole temperature measurements, 650,000 well logs and 1.7M well headers** in 2014 (an earlier holdings estimate said BHTs from >750,000 wells). Stanford's 2024 national model merged **400,134 unique BHTs** from nine sources. In >95% of wells there is only **one** temperature measurement (O'Malley et al. 2026).
- Raw BHTs read cold. Uncorrected values are often **10-25 °C** below formation temperature. Single-point empirical corrections (Kehle 1973, Harrison 1983) are depth polynomials calibrated in one basin. Field checks put corrected-BHT accuracy at **~5-10%** in SMU's best case and **"not better than ±16 °C"** in a pessimistic review. Typical method-vs-method spreads are **8-20 °C**.
- **The input data are the main error, not the correction method.** Schölderle et al. (2022) show that unknown errors in the inputs (shut-in time, mud temperature, depth, rounding on log headers) outweigh the differences between correction schemes. A dataset whose main problem is bad metadata is exactly where document-reading ML adds value.
- ML is now the best method at national scale. Stanford's InterPIGNN (Aljubran & Horne 2024) reports **MAE 4.8 °C** on a hold-out set, against **49.5 °C** for the SMU/NREL maps on the same test. LANL's In-Context Earth (2026) reports **4.7 °C** (vs 6.4 °C for Stanford re-evaluated, 5.1 °C for kriging). But error grows with depth: **3.1 °C at 0-2 km, 7.9 °C at 2-4 km, 11.2 °C at 4-6 km**. Only **~3%** of data are deeper than 4 km.
- These national models are **public goods**. They use conductive physics on already-digitized BHTs, and they are commoditized (free API and ArcGIS layers). Any edge has to come from (a) data that has not been digitized yet (scanned log headers, state well files, mud logs, DSTs, temperature logs) and (b) owning the acreage.

## 2. Literature review (primary sources)

### 2.1 Kehle, Schoppel & DeFord (1970); Kehle (1973). AAPG Geothermal Survey of North America (GSNA)
The original continental BHT compilation: **>20,000 BHT points from >10,000 wells**. It produced the AAPG/USGS Geothermal Gradient Map of North America (DeFord & Kehle 1976). Kehle's correction is a **quartic polynomial in depth**. SMU later wrote that the GSNA data "received only limited use, in part because of the uncertain error associated with the raw measurements, and the lack of calibration comparisons to accurate equilibrium temperature measurements." (Summarized in Blackwell & Richards 2004 and Whealton et al. 2015, below.)

### 2.2 Harrison, Luza, Prater & Cheung (1983). Oklahoma Geological Survey SP 83-1
The most widely used single-BHT correction in North America. It is a quadratic in depth, calibrated mostly on **drill-stem-test (DST) temperatures in Oklahoma**:
`ΔT = -16.51 + 0.01827·Z - 2.345e-6·Z²` (Z in metres). It was calibrated only to **~3 km**. The correction is about **+9 °C at 1.5 km and about +13 °C at 2.5 km**, and peaks near 3.9 km (computed from the equation). Stanford's 2024 national model still uses it because it needs only depth and temperature. That shows how little metadata most US BHTs carry.

### 2.3 Deming (1989). "Application of bottom-hole temperature corrections in geothermal studies," *Geothermics* 18(5-6):775-786
A foundational review. Raw BHTs are on average cooler than true formation temperatures. Empirical corrections **may not transfer outside the area where they were calibrated**. Whealton et al. (2015) cite it for the point that BHTs are "notoriously problematic" because they record a temperature field disturbed by drilling.

### 2.4 Blackwell & Richards (2004). "Calibration of the AAPG GSNA BHT Data Base," AAPG poster #87616 (SMU)
The authors tested Harrison-corrected GSNA BHTs against **equilibrium logs at 34 US sites**. Corrected values "tended to be either too high or low." SMU added a second, gradient-dependent "SMU correction":
- no change below 20 °C/km
- up to −5 °C at 20-26 °C/km
- +2 to +10 °C at 27-31 °C/km
- +11 °C above 30 °C/km

After this correction, about half of ~20 Midcontinent/Gulf Coast sites (2,500 ± 500 m) had errors **<5 °C**, and the overall accuracy was **"about 5-10%."** Critically, **"the correction below 3-4 km is still not established with enough accuracy to be consistently used."** That depth is where EGS and hot sedimentary targets sit. The SMU correction was applied only from 750 to 3,000 m.

### 2.5 Blackwell, Richards, Frone, Batir, Ruzo, Dingwall & Williams (2011). "Temperature-at-Depth Maps for the Conterminous US and Geothermal Resource Estimates," *GRC Transactions* 35 (Google.org funded)
SMU's third-generation US heat-flow map used **~35,000 data sites**, about twice the 2004 map. **Most of the new data came from oil and gas drilling.** Temperatures were modeled at 3.5-9.5 km from site heat flow, thermal conductivity, sediment thickness and radiogenic heat. A notable result was that parts of the eastern US (e.g., West Virginia) were hotter than some western areas. The grid is coarse (about 8 km cells, per Aljubran & Horne). A later SMU/NREL Snake River Plain study (Batir et al., Dec 2020) found **75% more power potential at 3.5 km** than the 2011 map over the same area. Map vintage alone can move resource estimates that much.

### 2.6 Whealton, Stedinger & Horowitz (2015). "Application of Generalized Least Squares Regression in BHT Corrections" (Cornell, DOE GPFA-AB)
The authors built NY/PA/WV corrections using NGDS WV data and log-header data. Key data-quality observations:
- **"the depth of the BHT measurement is generally not recorded."** They had to use the minimum of driller depth, logger depth and bottom logged interval.
- Some depths were reassigned because of apparent data-entry errors.
- Drilling fluid (air vs mud) changes the correction, but WV NGDS data carry **no fluid information**.
- Frone & Blackwell (2010) recommended **capping** Harrison for deep BHTs. Shope (2012) found Harrison **less accurate than no correction** above 1 km in NY/PA.
- Spatial clustering biases OLS. GLS fixes it, and their nonlinear form avoids negative shallow corrections.

The basin-specific correction problem is real and has not been solved nationally.

### 2.7 Burke, Pearson, Kinney & Pitman (2018). USGS, *GCAGS Journal* v.7:93-106
For the onshore Gulf of Mexico Basin: "due to the lack of an applicable BHT correction method, virgin rock temperatures of the onshore portion of the basin remain largely uncharacterized." The authors derived **12 separate correction equations**, one for each physiographic province. Gradients run from 1.39 °F/100 ft (S. Louisiana Salt Basin) to 1.89 °F/100 ft (Sabine Uplift). A companion GCAGS (2014) offshore study found Harrison gives temperatures **≥~5 °C higher** and gradients 5% higher than Horner. So even in the most heavily drilled US basin, a consistent correction was only derived in 2018.

### 2.8 Schölderle, Götzl, Einsiedl & Zosseder (2022). *Energies* 15(17):6367, peer-reviewed
This is the key paper on uncertainty. Bavarian Molasse Basin: 935 wells in the area. **Log headers survive for 346 (292 O&G, 54 geothermal)**, and **155 have only a single BHT**. Six schemes were tested (Horner, Lachenbruch-Brewer, Brennand, Leblanc-based, etc.) with Sobol sensitivity analysis and Monte Carlo methods. Findings:
- The "unknown error in the input parameters exceeds the error of the individual BHT correction methods."
- BHT instrument error is about ±2 °C or ±3%.
- Thermal diffusivity assumptions alone shift results by **up to 8.3 K** in one well.
- P10-P90 ranges are **~10-14 K** in the two geothermal wells tested.

From their literature review: validated errors of conventional methods are **8-10 °C**; one review concluded corrected BHTs are **"not better than ±16 °C"**; another reported **10-20 °C** method disagreement, driven by mud-circulation practices. They also note: "BHT data found in older logging reports and logging headers are not reliable, as the values often suggest incorrect documentation and rounding." The follow-on EGU24 abstract applied the Monte Carlo workflow to **>300 wells**.

### 2.9 Petroleum Geoscience 7(3):241 (2001) (authors unverified; likely Waples-group statistical correction work)
Reported uncorrected BHTs deviate from formation temperature by **22.2 ± 10.2 °C (1σ)**. A corrected BHT is accurate only to about **±16 °C at 96% confidence**. Waples, Pacheco & Vera (2004, *Petroleum Geoscience*) extended the Waples & Mahadir Ramly (2001) correction to **3,500-6,500 m**, calibrated against DSTs in the Gulf of Campeche. The correction depends strongly on **time since circulation stopped**, a field often missing or mis-recorded on headers.

### 2.10 Shahdi, Lee, Karpatne & Nojabaei (2021). *Geothermal Energy* 9:18, peer-reviewed
ML (XGBoost, RF, DNN, etc.) applied to corrected O&G BHTs in the Northeastern US. **XGBoost reached MAE 3.19 °C and RMSE 4.94 °C** for temperature at depth. Validated on **58 West Virginia wells** with measured T-z profiles. On the validation table, the physics/conductivity model had MAE 6.6 against **5.6 for XGBoost** (DNN 7.0). It also produced continuous 2D maps at three depths. This showed early that tabular ML on BHT data matches or beats physics-based conductive models.

### 2.11 Aljubran & Horne (2024). "Thermal Earth model for the conterminous United States using an interpolative physics-informed graph neural network (InterPIGNN)," *Geothermal Energy* (July 2024); arXiv 2403.09961
- **400,134 unique BHTs** from nine sources (SMU, AASG, USGS, UGS, CGS, MGS, WSDNR, GTILO, GBCGE), all Harrison-corrected.
- Predicts temperature, heat flow and conductivity jointly under a Fourier's-law constraint.
- Output covers 0-7 km at 1 km steps, **18 km² cells**.
- Hold-out MAE: **temperature 4.8 °C**, heat flow 5.8 mW/m², conductivity 0.022 W/m/K. Baselines: **SMU/NREL 49.5 °C**, linear regression 13.0 °C, FFNN 6.5 °C.
- Validated on only **15 temperature logs**.
- The authors admit Harrison-corrected values "might be a few degrees Celsius off," that drilling disturbance is depth-dependent, and that BHTs become sparser with depth.
- Released free as an API and ArcGIS layers on NREL's GDR.

### 2.12 O'Malley et al. (LANL, 2026). "In-context learning enables continental-scale subsurface temperature prediction from sparse local observations," arXiv 2605.16665 (preprint)
A transformer that uses the 20 nearest neighbours as context. US MAE: **4.7 °C**. Baselines: Stanford model 6.4, universal kriging 5.1, AlphaEarth embeddings 6.0. It transfers to Alberta, Australia (OZTemp) and the UK. **Error by depth: 3.1 / 7.9 / 11.2 °C for 0-2 / 2-4 / 4-6 km. Only ~3% of data are >4 km. >95% of wells have a single measurement.** The largest outliers were data-quality problems: measured-while-drilling values, "temperature may be assigned," and "error in depth temp" flags. Note that plain kriging (5.1) almost matches deep models, so the information limit is the data, not the model.

### 2.13 Burns, DeAngelo & Williams (2024). "Updated 3D temperature maps for the Great Basin," 49th Stanford Geothermal Workshop; USGS data release (doi:10.5066/P149FR54)
A USGS conductive model (uniform heat production 1.89 µW/m³, k = 2.7 W/m/K under basins) built on DeAngelo et al. (2023) heat flow. It matches measurements only under "relatively simple uniform conditions." Near-surface heat flow is the largest uncertainty. Conductive maps by design **miss convective (hydrothermal) systems**, which is what Zanskar hunts. Mordensky et al. (2025, *Geothermics* 133:103450) is the USGS ML favorability layer for Great Basin hydrothermal.

## 3. How illegible and noisy is the O&G BHT record? (synthesis)

| Problem | Evidence | Magnitude |
|---|---|---|
| Cold bias from mud circulation | Deming 1989; Pet. Geo. 2001 | ~22 ± 10 °C raw underestimate |
| Correction method spread | Schölderle 2022 review | 8-20 °C |
| Corrected accuracy | SMU 2004; Pet. Geo. 2001 | 5-10% best case; ±16 °C at 96% |
| Missing or wrong metadata | Whealton 2015; Schölderle 2022 | Measurement depth "generally not recorded"; shut-in time and fluid often missing; rounding |
| Single-point wells | O'Malley 2026; Schölderle 2022 | >95% of US wells have 1 BHT; 155/346 Bavarian wells single BHT |
| Deep sparsity | O'Malley 2026; SMU 2004 | ~3% of data >4 km; corrections not established >3-4 km |
| Basin-specific calibration | Burke 2018; Whealton 2015 | 12 equations for onshore Gulf alone |
| Digitization gap | NGDS 2014: ~530k BHTs; Stanford: 400k | Small next to the millions of US O&G wells drilled (unverified count: ~4M+); most raw log headers, DSTs and temperature logs still sit as scanned TIFF/PDF in state archives (unverified) |

Bottom line: the record is **large, public, and badly documented**. It is structurally like the Saskatchewan assessment files. The noise is in the metadata, which can be recovered by reading the original documents: shut-in time, circulation time, mud type, logger depth, repeat runs, DSTs. Field-validated studies show that recovering multi-BHT and shut-in data allows physics-based corrections (Horner/Brennand) that cut error toward ~±2-5 °C, against ±10-16 °C for single-point Harrison.

## 4. Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **National temperature maps are commoditized; the raw documents are not.** InterPIGNN and In-Context Earth are free and reach about 5 °C MAE on easy, shallow data. Their quality is capped by the Harrison-corrected, single-BHT, metadata-poor inputs, and errors reach 8-11 °C below 2 km. A Terranox-style moat is to **OCR and parse the original log headers, mud logs, DSTs and temperature logs** in state oil and gas commission archives (TX RRC, OK OCC, ND, WV, CO, UT, NV) so that each BHT gets a proper physics correction. This is the "illegible public data" wedge, and nobody in the literature has done it at scale.
2. **Zanskar's focus is conductive-anomaly-to-convective hydrothermal discovery in the Great Basin.** Examples: Big Blind (~250 °F at ~2,700 ft, no surface manifestation, no prior wells) and Pumpernickel (~280 °F at ~2,500 ft). Their data is mostly geophysics, satellite data and temperature-gradient holes, in a region where **O&G BHT density is low**. **The gap is sedimentary basins with dense O&G drilling:** Permian, Anadarko, Williston, Gulf Coast, Appalachian (WV's SMU-flagged hot spot), Denver-Julesburg and Uinta. There, hot sedimentary aquifers and EGS targets at 3-5 km are ranked by BHT-derived temperature, and that is where better BHT processing matters most. These are also the basins Fervo- and Sage-style EGS developers, and data-centre offtakers in TX/OK, care about.
3. **Rights acquisition fits.** Geothermal rights in Texas, Oklahoma and other private-mineral states are often severed or ambiguous and can be leased from surface or mineral owners cheaply before proof. BLM and state leases cover the West. Better temperature-at-depth estimates at 3-5 km (where public maps err by 8-11 °C, or 49.5 °C for SMU per Stanford's test) directly re-rate acreage value. A 10-15 °C difference at 4 km is roughly the difference between uneconomic and bankable binary or EGS.
4. **Risk:** BHT improvements mainly sharpen **conductive** temperature. Permeability and convective upflow (Zanskar's real edge) still need geophysics and drilling. The ML lift (getting from ~8 °C to ~3 °C deep error by recovering metadata) is plausible but untested. Per the standing rules, it should be scored on plausibility, and the literature supports it: Schölderle shows input-data error dominates.
5. **Data scale argument for YC:** 400k+ digitized BHTs already exist. Millions of undigitized well files exist (unverified count). Error is concentrated exactly where the money is (>2 km), and the public baseline models are free, so an asset-owning player gains by being *more right than the public map* about specific parcels.

## Sources
- SMU 2011 map release: https://www.smu.edu/news/archives/2011/geothermal-24oct2011
- SMU temperature maps page: https://www.smu.edu/dedman/academics/departments/earth-sciences/research/geothermallab/datamaps/temperaturemaps
- Blackwell & Richards 2004 BHT calibration poster: https://smu.edu/dedman/academics/departments/Earth-Sciences/Research/GeothermalLab/DataMaps/GeothermalMapofNorthAmerica/BHTCallibrationPoster
- SMU/NREL Snake River Plain report 2020: https://gdr.openei.org/files/1290/SMU-NREL_SRP-FinalReport%20Dec%202020.pdf
- Whealton, Stedinger & Horowitz 2015 (GPFA-AB): https://gdr.openei.org/files/682/2_GPFA-AB_BHTCorrections.pdf
- Schölderle et al. 2022, Energies: https://www.mdpi.com/1996-1073/15/17/6367 (PDF mirror: https://opac.geologie.ac.at/ais312/dokumente/Uncertainty_Assessment_Corrected_Bottom-Hole.pdf)
- EGU24 follow-on: https://meetingorganizer.copernicus.org/EGU24/EGU24-10641.html
- Petroleum Geoscience 2001 (BHT error statistics): https://www.earthdoc.org/content/journals/10.1144/petgeo.7.3.241
- Waples, Pacheco & Vera 2004: https://www.earthdoc.org/content/journals/10.1144/1354-079302-542
- Deming 1989 (citation): https://dggs.alaska.gov/pubs/id/32042
- Burke et al. 2018 USGS Gulf Coast: https://pubs.usgs.gov/publication/70200516
- GCAGS 2014 Harrison vs Horner: https://archives.datapages.com/data/gcags/data/064/064001/293_gcags640293.htm
- Shahdi et al. 2021: https://geothermal-energy-journal.springeropen.com/articles/10.1186/s40517-021-00200-4 ; https://vtechworks.lib.vt.edu/items/11ad80e1-29bf-410e-9180-cb4d07000b66
- Aljubran & Horne 2024: https://arxiv.org/abs/2403.09961 ; https://gdr.openei.org/submissions/1592
- O'Malley et al. 2026 In-Context Earth: https://www.alphaxiv.org/abs/2605.16665
- Burns, DeAngelo & Williams 2024: https://pubs.usgs.gov/publication/70252068 ; https://www.usgs.gov/data/three-dimensional-temperature-model-great-basin-usa
- Mordensky et al. 2025 favorability: https://pubs.usgs.gov/publication/70270953
- NGDS counts (2014): https://www.petroleumnews.com/story/2014/06/08/news/state-contributes-geothermal-data/26622.html ; AZGS: https://azgs.arizona.edu/node/701
- Zanskar Big Blind: https://www.thinkgeoenergy.com/zanskar-announces-discovery-of-big-blind-geothermal-site-in-western-nevada-usa/ ; Pumpernickel: https://www.thinkgeoenergy.com/zanskar-validates-ai-based-discovery-method-with-drilling-at-pumpernickel-geothermal-site-nevada/
