# M16: Temperature-at-depth models, and how to push shallow readings down to drilling depth

Slice M16, model track. Date: 23 Oct 2026. This file builds on `../../evidence/L09-temperature-at-depth.md` (BHT corrections, SMU maps, Stanford InterPIGNN, LANL In-Context Earth, Burns 2024 headline numbers), `M04-bht-corrections.md` (quality ladder of temperature readings), `M05-heat-flow-databases.md` (Great Basin point density, 379 clean wells) and `M06-water-well-temperature.md`. It does not repeat them. What is new here: (1) how the Stanford model was really validated and what its uncertainty means, (2) the newest USGS and academic thermal models (Monte Carlo crustal model, geothermometer-to-depth, 2025 EGS assessment), (3) Utah FORGE as a worked test of shallow-to-deep prediction, (4) the 1D conductive plus advective column model and how sensitive it is, (5) a concrete design for folding our own shallow readings into a deep estimate.

## Bottom line

Every public temperature-at-depth model in the US is **conductive by design**: SMU 2011, Stanford InterPIGNN 2024, USGS Great Basin 3D (Burns 2024) and the new USGS Monte Carlo crustal model (Sui, Shen and Boyd 2025). They give a good background. By construction they cannot see a blind hydrothermal upflow, which is the thing we sell. At Utah FORGE the gap between conduction and reality is huge. Shallow gradient holes and a constant conductive extrapolation give one answer. The upflow zone runs **about 100 °C cooler at 4-5 km** than its conductive flanks. A young outflow plume shows a **temperature inversion at about 300 m**. Convective heat loss is **more than 10 times** the conductive heat flow (Allis et al. 2019). So the better model is not a better national map. It is a **per-parcel Bayesian column model**. It takes the national map as a prior. It fits each shallow profile with a 1D conduction plus vertical-flow equation (Bredehoeft-Papadopulos, Péclet number). It caps the result with geothermometer temperatures and the boiling-point curve. It carries thermal conductivity as an explicit unknown, because conductivity is the largest single error term once a good log exists. Our sensors should measure the three things this column model needs and public data lacks: **profile shape** (dense, 0.01 °C, many depths), **thermal conductivity** of the actual rock, and **repeat readings over time**. With those, every warm water well and 2 m probe line becomes a constraint on temperature at 1-3 km, with an honest error bar. That is the input that land decisions need.

## Findings

### F1. Stanford InterPIGNN: better validated than it looks, but blind to convection and thin where we work
- The 4.8 °C MAE comes from a **spatial-block hold-out**, not a random split. BHT anchor nodes were split 80/10/10 using 10 km x 10 km x 10 km cubic blocks "to decorrelate spatial features". This is a fair test for areas with data. (Aljubran and Horne 2024, arXiv 2403.09961, https://arxiv.org/pdf/2403.09961)
- The governing physics is **steady-state 3D conduction with radiogenic heat**. There is no advection term. The authors name convecting deep aquifers as an exception to their monotonic-temperature constraint.
- Uncertainty comes from Monte Carlo dropout only (model uncertainty). Median uncertainty is **10.3% of temperature**, 9.7% of heat flow and 5.2% of conductivity. It widens with depth. **Data (aleatoric) uncertainty is not modeled.** So the bands ignore the ~±8-16 °C BHT error in M04.
- The 15 temperature logs used for checking have **no reported error numbers**, only "closely matched most". No error breakdown by region is given, so there is no published number for the Great Basin.
- Grid: 18 km² cells (about 4.2 km side), 0-7 km at 1 km steps, 4,279,536 nodes. A blind-system halo is a few km wide (M05), so one halo is about one cell. Inputs include gravity, magnetics, radiometrics, crustal thickness and seismic features. The most important were elevation, crustal thickness, depth, electrical conductivity and seismic features.
- Data release: GDR 1592, https://gdr.openei.org/submissions/1592 (also data.openei.org/submissions/7669 and Stanford Digital Repository layers).
- Read-through: use it as a prior mean with an inflated sigma. In the Great Basin, where the BHT count is about 1-2% of Kansas's (M04), the real error is likely far above 10% (unverified, no regional test published).

### F2. Newest USGS-family thermal models are all conductive, and now come with Monte Carlo spread
- **Sui, Shen and Boyd (2025), Geophysical Journal International, doi:10.1093/gji/ggaf118.** They build a conterminous-US crustal thermal model with MCMC per location. The inputs are surface temperature, heat flow and conductivity, plus Moho temperature from seismology and Curie depth from magnetics. Heat production comes from seismically inferred crustal composition at **1,683 locations**. Output is a posterior conductive geotherm per column. (https://www.usgs.gov/publications/a-crustal-thermal-model-conterminous-us-constrained-multiple-data-sets-a-monte-carlo)
  - Value to us: a per-column MCMC conductive geotherm is exactly the "prior column" we need. Its deep constraints (Moho, Curie depth) pin the bottom of the column. Our shallow readings pin the top.
- **DeAngelo, Burns and Mordensky (Jan 2025), USGS data release doi:10.5066/P14B8XOH.** They take chemical geothermometer temperatures of Great Basin hot springs and look up the depth where the 3D conductive model reaches that temperature. That gives an estimated **circulation depth** per spring. Some reservoirs come out **deeper than 6 km**. Deep circulation is more common in high-strain areas and basins. (https://www.usgs.gov/data/depth-predictions-chemical-geothermometers-estimated-using-a-three-dimensonal-temperature)
  - Value to us: this is a published recipe for joining geochemistry to a thermal model. We can run it backwards. A warm well with a geothermometer temperature plus a column model gives a depth-to-reservoir estimate on our own parcels.
- **USGS EGS assessment, Great Basin (Birdwell, Burns, DeAngelo, Gardner, Gelman, Williams; GSA Connects 2025).** Best estimate **135 GWe** from hot, low-permeability rock at ≤6 km, built on an updated heat-flow analysis and the 3D temperature model. The USGS has already **calibrated basin thermal models for the Williston, onshore Gulf Coast, Denver-Julesburg and Upper Colorado River basins**. Outputs to come include depth-to-temperature maps by resource grade. (https://gsameetings.secure-platform.com/connects25/solicitations/103002/sessiongallery/schedule/items/95469/application/9317 ; EGS data release https://www.usgs.gov/data/data-estimating-enhanced-geothermal-systems-egs-electric-resources-great-basin-usa)
  - Read-through: the public conductive baseline will soon be free and good in four big sedimentary basins. Our edge there must be local data and land, not the baseline map.
- Burns et al. 2024 3D Great Basin model (4 km grid, 1-6 km) is covered in L09 and M05. The key point repeats here: it used only 379 clean conductive wells, and it removes convective wells on purpose.

### F3. Utah FORGE: a real test of shallow-to-deep prediction
Source: Allis, Gwynn, Hardwick, Hurlbut, Kirby and Moore (2019), "Thermal characteristics of the Roosevelt Hot Springs system, with focus on the FORGE EGS site", Utah Geological Survey Misc. Pub. 169-D (https://ugspub.nr.utah.gov/publications/misc_pubs/mp-169/mp-169-d.pdf). FORGE well temperature data: GDR 1012 (https://gdr.openei.org/submissions/1012).
- Method used before deep drilling: about 200 m gradient holes. Gradient times conductivity of basin fill (**1.5 ± 0.3 W/m/°C**) gives heat flow. Below about 1 km a constant 1D conductive gradient is assumed. Conductivity is cut by about 15% at reservoir temperature (granite trend). Acord-1 BHTs were corrected (Gwynn et al. 2016).
- Result in well 58-32: **199.4 °C at about 2.3 km** (accuracy ±0.1 °C). Heat flow there is **180 ± 20 mW/m²** after the temperature correction (200 before). Well 24-36 has **85 °C/km** below 750 m and 210 ± 20 mW/m². Acord-1 has 40 °C/km in granite and 100 ± 20 mW/m². The regional Milford Valley background is **90 ± 10 mW/m²**.
- The authors say thermal conductivity drives most of the uncertainty. Room-temperature values run **2.0 to 3.9 W/m/°C**, nearly a factor of two. With a good log, the temperature error is tiny and the heat-flow error is all conductivity.
- Conduction against convection:
  - In the upflow zone, rock-water equilibrium is **270-310 °C**. This is possibly **~100 °C cooler at 4-5 km** than the conductive extrapolation on either side. Conductive extrapolation gives 600-700 °C at 6-8 km, which is clearly wrong for the convecting part.
  - The northern outflow plume shows a **temperature inversion near 300 m**. The authors read it as young, about 100-1,000 years. The southern outflow has no inversion and a ~70 °C/km gradient, so it is old (tens of thousands of years).
  - Convective heat loss from the upflow zone (**3-7 W/m²**, 60-70 MW total) is **more than ten times** the conductive heat flow nearby.
  - The >200 °C area is about 25 km² at 2 km and about 70 km² at 3 km.
- Native-state model: Podgorney, Finnila, Simmons and McLennan (2021), Energies 14(16):4758 (https://www.mdpi.com/1996-1073/14/16/4758). FALCON/MOOSE, 2.5 x 2.5 x 2.75 km, 50 m mesh. The bottom boundary had to be **raised to about 220-270 °C** from the earlier Allis estimates to match the November 2018 logs. Even a site with many holes needed post-drilling recalibration. A 2025 update exists (https://catalog-old.data.gov/dataset/utah-forge-native-state-numerical-model-2025-update).
- Lessons for us:
  1. Shallow (200 m) gradients plus conduction got the conductive flank right within the conductivity error.
  2. The **shape** of the shallow profile (inversion or not) told the age and direction of the outflow. A single bottom-hole value cannot tell you this.
  3. Upflow zones cap and reverse the deep extrapolation. A linear deep extrapolation over-predicts at depth inside the system and under-predicts heat content near the surface.

### F4. 1D conductive and advective column models: the physics we should fit to every profile
- **Pure conduction** with constant conductivity k and heat production A: T(z) = T0 + (q0/k)·z − (A/2k)·z². Gradients drop with depth as k rises from about 1.5 W/m/K in shallow sediment to about 3 W/m/K in basement. McCarthy (Baker Hughes, SGW 2026) shows that a linear BHT extrapolation can over-predict by more than 20 °C/km. In his example, 200 °C is predicted at 3 km where about 150 °C is real. (https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Mccarthy.pdf ; note: an industry paper with some loosely supported numbers)
- **Conduction plus vertical flow** (Bredehoeft and Papadopulos 1965). The profile curvature depends on the Péclet number Pe = ρw·cw·qz·L / k. Upflow makes the profile convex (hot near the top). Downflow makes it concave. Pe > 1 means advection dominates.
  - My computation: with L = 100 m and k = 2 W/m/K, Pe = 1 at a vertical Darcy flux of about **4.8e-9 m/s, or about 15 cm/yr**. Very slow upflow already bends a 100 m profile visibly. A blind upflow zone moves far more than this. So profile shape is a sensitive upflow detector, even when the bottom temperature is unremarkable.
  - Reliability: Irvine, Cartwright, Post, Simmons and Banks (2016), Water Resources Research 52(2):813-826, doi:10.1002/2015WR017702. The method gives a good mean vertical flux even when the vertical-to-horizontal flux ratio is as low as **0.1**, in heterogeneous media. It **over-estimates** flux when the surface is warming (climate change, land clearing). They tested sensor precision of 0.1 to 0.001 °C. (https://researchers.cdu.edu.au/en/publications/uncertainties-in-vertical-groundwater-fluxes-from-1-d-steady-stat/)
  - So a column fit needs a transient surface term (paleoclimate and land-use warming of about 1-2 °C over the last century, unverified for each site). It also needs readings at 0.01 °C or better.
- **Lateral outflow** (a hot tongue in an aquifer) gives a profile that rises, peaks and then reverses, as at FORGE north. Ziagos and Blackwell (1986, J. Volcanol. Geotherm. Res. 27) built analytic models of the transient temperature of horizontal flow in geothermal systems (citation from memory, unverified details). The age of the inversion tells how long the plume has run. The plume direction points back to the upflow, which is often kilometres away (M05).
- **Hard cap.** Inside a two-phase or near-boiling system the temperature follows the boiling-point-with-depth curve (standard hydrothermal practice). That gives a physical upper bound on any extrapolation.
- **Geothermometer cap.** A Na-K-Ca or silica geothermometer temperature gives the reservoir temperature. The column model then gives the depth where that is reached (DeAngelo et al. 2025 method).

### F5. How large each error is when you push a shallow reading to 1-3 km (synthesis)
| Error source | Size | Basis |
|---|---|---|
| Conductivity of the real rock column | ±20% heat flow at a site (1.5 ± 0.3 W/m/K basin fill); 2.0-3.9 W/m/K range in FORGE rocks | Allis et al. 2019 |
| Temperature dependence of k | about −15% at reservoir temperature | Allis et al. 2019 |
| Linear extrapolation instead of k(z) | can exceed 20 °C/km of gradient | McCarthy 2026 |
| Unrecognised vertical flow | a 100 m profile is advection-dominated at ~15 cm/yr Darcy flux; ignoring it can move the projected 1 km temperature by tens of °C (my judgement, unverified) | Bredehoeft-Papadopulos physics; Irvine et al. 2016 |
| Convective upflow, at depth | conductive extrapolation wrong by ~100 °C at 4-5 km inside a system | Allis et al. 2019 |
| Surface warming | biases shallow flux estimates upward | Irvine et al. 2016 |
| BHT input error | ±8-16 °C | M04, L09 |
| National map, any one cell | 4.8 °C MAE in a spatial hold-out where data exist; 10.3% median model uncertainty; error grows with depth (3.1/7.9/11.2 °C at 0-2/2-4/4-6 km in LANL's test) | Aljubran and Horne 2024; O'Malley et al. 2026 (L09) |

Plain reading: once you have a good profile, temperature error is no longer the problem. **Conductivity and flow regime** are the problem. Both can be measured cheaply.

## Datasets
| Dataset | Access | Coverage | Value for blind detection |
|---|---|---|---|
| Stanford Thermal Earth Model (InterPIGNN) | Free, GDR 1592, ArcGIS, API | CONUS, 18 km² cells, 0-7 km | Conductive prior mean plus a model-only sigma. A residual (measured minus predicted) is a convective anomaly flag |
| USGS 3D temperature model, Great Basin (Burns et al. 2024) | Free, doi:10.5066/P149FR54 | Great Basin, 4 km grid, 1-6 km | Conductive baseline built from 379 clean wells. It removes convective wells, so its residuals are informative |
| USGS geothermometer depth predictions (DeAngelo et al. 2025) | Free, doi:10.5066/P14B8XOH | Great Basin springs | Ready labels: reservoir temperature and estimated circulation depth |
| USGS EGS Great Basin data and calibrated basin models (Williston, Gulf Coast, DJ, Upper Colorado) | Free, USGS data releases (basins partly forthcoming) | Great Basin plus four basins | Conductive baseline to 6 km. Commoditises sedimentary-basin baselines |
| Sui, Shen and Boyd 2025 crustal thermal model | Paper (GJI). Data release unverified | CONUS, 1,683 heat-production nodes | Posterior geotherms, with Moho and Curie constraints at the bottom of the column |
| Utah FORGE well temperatures and native-state models | Free, GDR 1012 and FORGE GDR submissions | FORGE/Roosevelt, many TG holes plus deep wells | A labelled test bed. Shallow-to-deep prediction can be scored against 2-3 km truth |
| SMU node / NGDS temperature logs | Free (see D04, M05) | 14,000+ equilibrium sites | Full profiles for Péclet fits. Most shape information is in scanned field notes |

## What dominates uncertainty
1. **Flow regime in the top few hundred metres.** It decides whether a shallow gradient extrapolates up or down. Lateral flow can hide an upflow (Argenta, M02) or fake one (outflow tongue, FORGE north).
2. **Thermal conductivity of the actual column.** It is about a ±20-50% factor on heat flow, and so on the deep temperature, once the temperature log itself is good.
3. **Depth to the convective cap and reservoir.** Public data has almost nothing between 300 m and 1,500 m in the Great Basin (M02). The boiling curve and geothermometers bound it from above, but not from below.
4. **Prior error in sparse regions.** National map uncertainty is model-only and not tested regionally in the Great Basin.
5. **Transients.** Surface warming and young plumes break steady-state assumptions.

## What a sensor could fill
- **A profile-shape logger, not a point thermometer.** The ranch drop probe (prior pick) should log continuously while it goes down (for example, every 0.5-1 m at 0.01 °C resolution, with a slow descent rate so the sensor settles). Output: the full T(z) curve and a Péclet fit on the spot. This turns the probe into an upflow and outflow detector. It is mostly a firmware and procedure change.
- **A field thermal-conductivity kit.** A needle probe (transient line source) for cuttings, drill chips or outcrop samples, and a divided-bar or optical scanner later for cores. Measuring k for the local basin fill turns each gradient into a heat flow with ±10% instead of ±20-50%. It is cheap and has no permit issues. This is the single largest error left after a good log at FORGE.
- **Repeat logging.** Log the same wells again after 6-12 months. A changing profile separates a transient (young plume, surface warming, recent pumping) from steady-state upflow. A low-cost string of thermistors left in a well (or a small DTS fibre where the owner allows it) does this automatically.
- **Hydraulic context per well.** Static water level, a short pump-induced flow log, or a heat-pulse flowmeter. This gives the measured Darcy flux, so the Péclet fit is constrained rather than fitted.
- **Deeper partner holes where it matters.** On the best optioned parcels, one 150-500 m slim hole with an equilibrium log is the step that converts a column model into a bankable P90. This is a carry-to-confirmation step, not a sensor product.

## Implications for a better model
1. **Build the model as a stack, not a map.** For each cell or parcel: (a) a conductive prior column from the Stanford or USGS model, or from a Sui-style MCMC geotherm, with the sigma inflated where data are thin; (b) a latent state of basal heat flow, a k(z) profile, vertical Darcy flux (Pe), an aquifer or outflow layer, and a convective cap depth; (c) a likelihood for each observation using its quality-ladder error (M04): BHT, water-well point, our logged profile, 2 m probe, geothermometer temperature; (d) physical bounds from the boiling-point curve. Solve each column with MCMC or with a neural posterior trained on simulated columns. Couple columns in space with a Gaussian process on the heat-flow and Péclet residuals.
2. **Train the column inverter on simulations, then check it on FORGE.** Run many 2D and 3D TOUGH or FALCON hydrothermal simulations (upflow along a fault, outflow tongue, cold lid). Sample synthetic shallow profiles from them. Train a network to map a shallow profile plus context to P(T at 1, 2, 3 km). Score it on FORGE: hide the deep wells, predict from the 200 m holes, compare with 58-32 and 24-36. Compute is cheap and plentiful, so this fits the standing rules.
3. **Use residuals against the conductive maps as a feature.** A measured shallow temperature far above the Stanford or USGS conductive value is direct evidence of convection. Because those maps exclude convection on purpose, their residuals are clean signals. Feed them into the blind-system classifier (M02, M13).
4. **Report what land decisions need.** For each parcel report P(T ≥ 150 °C at ≤ 1.5 km), P(T ≥ 175 °C at ≤ 3 km) and the expected value of the next measurement. Usually that next measurement is a logged profile, then a conductivity sample, then a slim hole.
5. **In sedimentary basins, do not compete on the baseline.** USGS is calibrating basin models now. Spend effort only on parcels where our own profiles or recovered BHT metadata (L09, M04) move the answer.
6. **Make the drop probe a profile logger and add a conductivity needle.** These two changes give the column model its two missing inputs on every ranch visit, at almost no extra cost.

## Sources
- Aljubran and Horne 2024 (InterPIGNN): https://arxiv.org/pdf/2403.09961 ; data https://gdr.openei.org/submissions/1592 ; https://data.openei.org/submissions/7669
- Sui, Shen and Boyd 2025, GJI: https://www.usgs.gov/publications/a-crustal-thermal-model-conterminous-us-constrained-multiple-data-sets-a-monte-carlo
- DeAngelo, Burns and Mordensky 2025 geothermometer depths: https://www.usgs.gov/data/depth-predictions-chemical-geothermometers-estimated-using-a-three-dimensonal-temperature
- Birdwell et al. 2025 USGS EGS assessment abstract: https://gsameetings.secure-platform.com/connects25/solicitations/103002/sessiongallery/schedule/items/95469/application/9317 ; data https://www.usgs.gov/data/data-estimating-enhanced-geothermal-systems-egs-electric-resources-great-basin-usa
- USGS 3D Great Basin temperature model: https://www.usgs.gov/data/three-dimensional-temperature-model-great-basin-usa
- Allis et al. 2019, UGS MP 169-D: https://ugspub.nr.utah.gov/publications/misc_pubs/mp-169/mp-169-d.pdf
- Utah FORGE GIS well temperature data: https://gdr.openei.org/submissions/1012
- Podgorney et al. 2021, Energies: https://www.mdpi.com/1996-1073/14/16/4758 ; 2025 update https://catalog-old.data.gov/dataset/utah-forge-native-state-numerical-model-2025-update
- McCarthy 2026, SGW: https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Mccarthy.pdf
- Irvine et al. 2016, WRR: https://researchers.cdu.edu.au/en/publications/uncertainties-in-vertical-groundwater-fluxes-from-1-d-steady-stat/
- Bredehoeft and Papadopulos 1965, Water Resources Research 1(2):325-328 (cited from memory)
- Ziagos and Blackwell 1986, J. Volcanol. Geotherm. Res. 27 (cited from memory, unverified details)
