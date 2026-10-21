# L05: USGS geothermal resource assessments (2008 national, 2023-2026 Great Basin ML update)

Literature review. Ten primary sources were read: USGS fact sheets, USGS Open-File Reports, Geothermics papers, GRC Transactions papers and DOE final reports. Numbers are quoted from the documents. Anything not confirmed in a primary source is marked (unverified).

---

## 1. Source-by-source summaries

### S1. Williams, Reed, Mariner, DeAngelo & Galanis (2008). *Assessment of Moderate- and High-Temperature Geothermal Resources of the United States.* USGS Fact Sheet 2008-3082.
This is the headline national assessment. All figures assume 30 years of production.

| Category | F95 | F50 | Mean | F5 |
|---|---|---|---|---|
| Identified (241 systems on private or accessible public land; table N = 248 including 7 low-T Alaska systems) | 3,675 MWe | 8,356 | **9,057** | 16,457 |
| Undiscovered (conventional hydrothermal) | 7,917 | 23,739 | **30,033** | 73,286 |
| EGS (provisional) | 345,100 | 507,000 | **517,800** | 727,900 |

- Installed US capacity at the time was more than 2,500 MWe. Full development of identified systems alone would add about 6,500 MWe.
- California holds 59.7% of the identified resource, Nevada 15.4% and Alaska 7.5%. The undiscovered resource sits much more outside California (CA 37.8%). The fact sheet attributes this to "the limited degree of exploration and development in States other than California and Nevada" and to the uniqueness of The Geysers.
- By state, mean undiscovered: **Nevada 4,364 MWe** (identified 1,391), Oregon 1,893, Idaho 1,872, New Mexico 1,484, Utah 1,464, California 11,340.
- Regions with high favorability but few identified systems: **NE Nevada, western Utah, southern Idaho, eastern Oregon, and parts of New Mexico and Colorado.**
- Conventional fields run at 10-20 MWe/km². The EGS resource away from hydrothermal margins is about 0.5 MWe/km², which is diffuse.
- Systems on closed public lands, such as national parks, were excluded.
- URL: https://pubs.usgs.gov/fs/2008/3082/ (PDF https://pubs.usgs.gov/fs/2008/3082/pdf/fs2008-3082.pdf)

### S2. Williams, Reed & Mariner (2008). *A Review of Methods Applied by the USGS in the Assessment of Identified Geothermal Resources.* USGS OFR 2008-1296.
This report sets out the methodology for the identified resource.
- **Volume (heat-in-place) method** (Muffler 1979 lineage). For each system, the reservoir thermal energy comes from triangular min, most-likely and max distributions of temperature and volume. That energy is multiplied by a geothermal recovery factor Rg to give wellhead exergy, and then by a temperature-dependent utilization efficiency to give MWe over 30 years. The whole chain runs as a **Monte Carlo** simulation.
- **Recovery factor revised down.** Circular 790 (1979) used a mean Rg of 0.25 (range 0-0.5). Production histories from fields such as Dixie Valley show Rg closer to about 0.1. The 2008 assessment uses **Rg uniform on 0.08-0.20 for fracture-dominated reservoirs and 0.10-0.25 for sediment-hosted reservoirs.**
- Temperature classes are moderate (90-150 °C) and high (>150 °C). Depth goes to about 3 km in earlier practice.
- Historical baseline from Circular 790 (1979): about 23,000 MWe identified (>150 °C, <3 km) and **72,000-127,000 MWe undiscovered**. The 2008 figures are therefore a large downgrade, driven mostly by the lower recovery factors.
- URL: https://pubs.usgs.gov/publication/ofr20081296 (PDF https://pubs.usgs.gov/of/2008/1296/pdf/of2008-1296.pdf)

### S3. Williams & DeAngelo (2008). *Mapping Geothermal Potential in the Western United States.* GRC Transactions 32.
This is the spatial method behind the 30 GWe undiscovered figure.
- Weights-of-evidence and logistic regression in GIS. They built **28 favorability models** from five evidence layers: heat flow, Quaternary magmatism, Quaternary faulting, seismicity and tectonic stress. Expert judgement chose the layers, the binning and the weights.
- They found a strong correlation of systems with active deformation, magmatism and high heat flow. The under-explored high-favorability regions match S1.
- URL: https://openei.org/wiki/Mapping_Geothermal_Potential_In_The_Western_United_States

### S4. Williams, Reed, DeAngelo & Galanis (2009). *Quantifying the Undiscovered Geothermal Resources of the United States.* GRC Transactions 33.
- Restates 30,033 MWe undiscovered, more than 3x the 9,057 MWe identified.
- Past exploration "has been limited in technique and spatial coverage", mostly aimed at surface thermal features. That is the structural reason blind systems are expected.
- The largest systems (Geysers, Yellowstone) are unlikely to have undiscovered analogues. The largest undiscovered upside is magmatic and partly remote, for example the Aleutians.
- URL: https://pubs.usgs.gov/publication/70158979

### S5. Faulds et al. (UNR/NBMG with LBNL, NREL, U. Utah), DOE award DE-EE0006731. *Discovering Blind Geothermal Systems in the Great Basin Region: Play Fairways.* Final report, all phases (May 2021).
- Great Basin geothermal potential "may exceed 30,000 MW", while installed nameplate in the region is under 600 MW.
- **About 39% of known systems are blind (Faulds & Hinz 2015), and about 75% of all Great Basin geothermal resources are estimated to be blind (Coolbaugh et al. 2007).**
- Permeability, not temperature, is the binding constraint. It "can vary significantly over distances of 100-200 m."
- **Most known blind systems were found through regional gradient drilling (Desert Peak), by accident in agricultural wells (Stillwater), or in mineral-exploration holes (McGinness Hills, Tungsten Mountain, Blue Mountain).** McGinness Hills is a blind system that now hosts Ormat plants.
- Study area was about 96,000 km². The play fairway work led to two blind discoveries confirmed by drilling, in SE Gabbs Valley and N Granite Springs Valley (2019).
- URLs: https://www.osti.gov/biblio/1724080 (OSTI ID from a search listing; the record page itself was not opened). Data and reports are at https://gdr.openei.org/submissions/756

### S6. Mordensky, Lipor, DeAngelo, Burns & Lindsey (2023). *When less is more: How increasing the complexity of ML strategies for geothermal energy assessments may not lead toward better estimates.* Geothermics 110, 102662.
- Re-ran the 2008 western-US favorability problem with **9 maps**: 2 expert-dependent (WofE, logistic regression), logistic regression without expert input, XGBoost, SVMs with two training strategies, and an ANN.
- The core problem is **no true negative examples and severe class imbalance**.
- **All methods had F1 < 0.10.** Added complexity did not help, because the limit lies in the input features, not the algorithm. Simple non-linear methods such as XGBoost do as well as or better than neural nets.
- URL: https://pubs.usgs.gov/publication/70240475 (DOI 10.1016/j.geothermics.2023.102662)

### S7. DeAngelo, Burns, Mordensky & Lindsey (2023). GRC Transactions 47. Also DeAngelo et al., Stanford Geothermal Workshop 2023: *Maps of conductive heat flow in the Great Basin; separating conductive and convective influences.*
- Re-examining the Nevada Machine Learning Project data, they found the **DEM (elevation) to be the most important feature**. That led to the "detrending elevation" follow-ups (USGS pubs 70250639 and "Separating signals in elevation data improves supervised ML predictions").
- The conductive/convective separation of heat flow gives the **ordinal labels** used in S8. Wells where measured heat flow departs from the conductive baseline are labelled by the size of the convective upflow.
- URLs: https://pubs.usgs.gov/publication/70250639 ; https://www.usgs.gov/publications/separating-signals-elevation-data-improves-supervised-machine-learning-predictions ; heat-flow data https://doi.org/10.5066/P9BZPVUC
- (The SGW 2023 PDF returned HTTP 503 when fetched. The content above comes from the USGS abstracts.)

### S8. Mordensky, Burns, Lipor & DeAngelo (2025). *Favorability mapping for hydrothermal power resource assessments of the Great Basin, USA.* Geothermics 133, 103450.
This is the **core of the USGS hydrothermal update** of the 2008 Great Basin assessment, covering CA, ID, NV, OR and UT.
- Method:
  - **16 evidence layers**: conductive heat flow, magnetics, isostatic gravity, basement depth, distance to Quaternary faults and magmatism, shear/dilation strain rates and strain tensor, seismic density, and MT conductance from the surface to 200 km.
  - About **10x more training sites** than earlier work. Training sites are heat-flow wells, not power plants, with ordinal labels (low, high, very high convective signal) plus low-signal sites added in under-sampled areas.
  - **XGBoost** with Monte Carlo cross-validation (**n = 1,200** realizations). The published map is the median, with P05-P95 percentile maps available.
- Results:
  - **15 of 28 power-producing systems fall in the top 1% of map area.**
  - **26 of 28 (93%) fall above the 80th percentile.** Prior models had about half above it.
  - Hidden and exposed systems are predicted equally well.
  - The misses are small or low-temperature systems, which the authors suggest could point to new prospects.
- Data release: https://doi.org/10.5066/P14EET2C (labelled and unlabelled features, percentile favorability rasters). These are **public and free**.
- URL: https://pubs.usgs.gov/publication/70270953 (DOI 10.1016/j.geothermics.2025.103450). AAPG summary of the layers: https://newsletters.aapg.org/core-elements-11-03-25

### S9. Burns et al. / USGS (2025). *Enhanced Geothermal Systems Electric-Resource Assessment for the Great Basin, Southwestern United States.* USGS Fact Sheet 2025-3027 (method paper: Burns et al., SGW 2025).
- Provisional EGS figure: **135 GWe from the upper 6 km** of the Great Basin (633,072 km²), for all temperatures above 90 °C. That is **0.5% of the accessible electric-grade resource base**, so 99.5% is "residual". USGS says this would take geothermal from under 1% to 10% of current US capacity.
- Upside: more than 10x the best estimate if 5% of the resource proves useful. The theoretical maximum is 13 TWe (44% useful).
- Consistent with 2008: 518 GWe across the western US, about 150 GWe of it in NV and UT.
- Hot rock near active hydrothermal systems is under 1% of rock volume and is **excluded**. The hydrothermal update (S8 and the forthcoming quantitative assessment) is a separate product.
- Updates are driven by the **Energy Act of 2020**, which directs updated USGS geothermal assessments.
- URL: https://pubs.usgs.gov/fs/2025/3027/fs20253027.pdf (DOI 10.3133/fs20253027). Data: https://doi.org/10.5066/P14LU7WD ; 3-D temperature model: https://doi.org/10.5066/P149FR54

### S10. Trainor-Guitton, Menon, Pinchuk, Thomson, Hart-Wagoner, Lu, Mlawsky, Coolbaugh, Lindsey & Faulds (2025). *"Hidden" hydrothermal technical potential & technoeconomics: Revealing permeability & fluids with more data.* Geothermics 133, 103473 (NREL + UNR).
- XGBoost regression on **nameplate MW of 37 operating plants plus 248 zero-MW sites, using 48 geologic and geophysical features** (INGENIOUS region). The predictions were fed into NREL's reV model.
- **Great Basin hydrothermal technical capacity: 28.45 GW (MSE model), 23 GW (P50), 79.5 GW (P90).** The authors note these are consistent with the 30 GW figure of Williams et al. (2008).
- **Site LCOE is 58-62 $/MWh. All-in LCOE including transmission is about 65-70 $/MWh**, against about 75 $/MWh for temperature-only estimates.
- "Half of these operating geothermal plants are considered 'hidden' systems, and **most were discovered by accident**" (citing Edwards et al. 2025).
- URL: https://www.osti.gov/pages/servlets/purl/3018341 (Stanford 2025 version: https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2025/Trainorguitton.pdf)

### S11. Mordensky & DeAngelo (2026). USGS data release DOI 10.5066/P14QM39R: *Feature, Label, Prediction, and Zone Data for Great Basin Zone Classification and Hydrothermal Favorability Modeling Using Supervised ML.*
- 53 public input features, with labels drawn from modelled departures from conductive heat flow, for the INGENIOUS region. It supports Mordensky et al. (2026). The paper text itself was not retrieved (unverified).
- URL: https://sciencebase.gov/catalog/item/6927454dd4be02716f722cb3

---

## 2. Synthesis: what the assessments say, in numbers

1. **The size of the target pool is stable at about 23-30 GWe of hidden or undiscovered conventional hydrothermal resource**, most of it in the Great Basin (Nevada mean undiscovered 4.4 GWe by 2008 state allocation, against 1.4 GWe identified). The 2008 USGS figure is 30 GWe nationally; the 2025 NREL/UNR figures are 23 GW (P50) and 79.5 GW (P90) for the Great Basin. Installed Great Basin nameplate is under 600 MW in the Faulds report, and US installed is about 2.5-4 GW (unverified current figure). **Over 90% of the conventional prize is still in the ground.**
2. **About 75% of Great Basin resources are blind**, and the historical discovery mechanism is accidental: ag wells, mineral holes and gradient holes. That makes the archive of old non-geothermal drilling (mining assessment holes, oil/gas BHTs, water wells) the proven discovery channel, not a speculative one.
3. **The USGS has now released state-of-the-art ML favorability maps as free public data** (S8, S11): P05-P95 rasters, 16-53 features and 1,200 realizations. Base-layer regional favorability is now a commodity. Anyone, including BLM lease bidders, can download it.
4. **The binding constraint is the features, not the models** (S6: F1 < 0.10 across all algorithms; S5: permeability varies over 100-200 m). Regional maps narrow the search to the top 1-20% of area. They do not resolve where to drill. The lift comes from **new, denser, site-scale evidence**, such as digitised temperatures from old wells, lithology logs, assessment-file geochemistry and alteration mapping.
5. **Resource-per-asset economics.** Recovery factors of 0.08-0.20 mean that volumetric estimates for a single system are wide (F95/F5 spreads of about 4-5x even for identified systems). A typical blind Great Basin system is 10-100 MWe (unverified generalisation; Zanskar claims analogues of more than 100 MWe). At 10-20 MWe/km², a 30 MWe system needs only a few km² of lease. Reservoir footprints are small, and the right is cheap compared with the value of the asset once proven.
6. **EGS (135 GWe Great Basin, 518 GWe West) is a different game.** Its 0.5 MWe/km² density makes the land position more commodity-like and less a matter of being the one who discovered it. A Terranox-shape "information arbitrage" works best on **hydrothermal and hot-sedimentary targets where location knowledge is scarce**, with EGS as an option value layered on the same leases.

---

## 3. Implications for a Terranox-shape geothermal company and the gap vs Zanskar

**What the literature supports**
- **Large and under-explored target pool.** 23-30 GWe of undiscovered hydrothermal resource (USGS 2008; NREL 2025 P50), against under 600 MW installed in the Great Basin. At even $1-3M per proven MWe of resource value for a developer (unverified market range; other evidence files should confirm), the pool is worth tens of billions of dollars. "Too small" does not apply.
- **The discovery channel Terranox-for-geothermal would mine has a record of finding resources by accident.** McGinness Hills, Tungsten Mountain and Blue Mountain came from **mineral exploration holes**, and Stillwater from an ag well (S5). This is the Saskatchewan-assessment-file thesis transplanted almost exactly. Nevada and other Great Basin states keep mining-claim and drilling records, and many old holes record temperature or lost-circulation and alteration notes that no one has systematically digitised for geothermal (unverified extent; check the NBMG and state archives in other evidence files).
- **Owning the asset is credible.** BLM geothermal leases are auctioned through competitive sales, and the regional favorability maps are public. The edge therefore has to come from **proprietary site-scale evidence assembled before the lease sale or before a private-land deal**. That is the same buy-before-proof step-up Terranox runs on.

**Zanskar, for contrast**
- Zanskar builds its own prospecting toolkit and AI engine and acts as an **explorer-developer-operator**. It drills its own wells (Big Blind: two wells in July-August 2025, about 121 °C at about 2,700 ft), bought the operating Lightning Dock plant (NM) and works Pumpernickel (NV). Its pitch is "found the first industry-confirmed commercial blind system in 30+ years" (Dec 2025: https://www.thinkgeoenergy.com/zanskar-announces-discovery-of-big-blind-geothermal-site-in-western-nevada-usa/). Big Blind explicitly had **no prior well data**. Zanskar's process is a geophysics-plus-physics model followed by its own drilling, which is capital-heavy and vertically integrated through development and operation.

**The gap**
1. **Monetise at the proven-resource stage instead of building plants.** Zanskar's model needs plant capex and years of permitting per site. A Terranox-shape company would stop at a drilled, flow-tested, or volumetrically booked resource and **sell or farm out to Ormat, Fervo, utilities or data-centre offtakers**. That is the junior-explorer "prospect generator" model from mining, which geothermal largely lacks. Roughly 75% of resources are blind, and about 23-30 GW sit undeveloped, so there is far more inventory than any single developer-operator can build out.
2. **An archive-first data moat in place of a geophysics-first one.** USGS and NREL showed that algorithms plateau (F1 < 0.10) and that the binding constraint is the features. The defensible asset is a **proprietary digitised corpus**: millions of pages of mining assessment files, oil/gas BHTs, water-well logs and old gradient holes, with temperature and alteration data extracted by LLM and vision models. Zanskar's announced edge is its prospecting toolkit and new field data; it does not claim an archive moat (unverified, as Zanskar's internal data holdings are not public).
3. **Breadth over depth.** Zanskar concentrates its capital on a handful of drilled assets. A portfolio of dozens to hundreds of cheap leases, each de-risked to "drill-ready", is the Terranox playbook. Coverage can extend beyond the Great Basin into the 2008 USGS under-explored zones: NE Nevada, W Utah, S Idaho, E Oregon, NM and CO. The free USGS P05-P95 rasters serve as a prior, and proprietary data adds the lift.
4. **Option value on EGS and sedimentary resources.** The same leases carry an EGS option worth 135 GWe in the Great Basin per USGS 2025, which next-gen developers such as Fervo will pay for once a site is shown to be hot. A temperature-first archive is the direct input to that market.

**Risks the literature flags**
- Regional favorability is now public, which compresses the information edge at BLM lease sales.
- Permeability is hard to predict, and its heterogeneity at 100-200 m scale means archive data narrows targets but still needs drilling to prove them.
- Single-system resource uncertainty spans about 4-5x (F95 to F5).
- The proven-but-undeveloped resource market is thin and illiquid (unverified; needs comparable transactions).

---

## Sources
- https://pubs.usgs.gov/fs/2008/3082/ and https://pubs.usgs.gov/fs/2008/3082/pdf/fs2008-3082.pdf
- https://pubs.usgs.gov/publication/ofr20081296 and https://pubs.usgs.gov/of/2008/1296/pdf/of2008-1296.pdf
- https://openei.org/wiki/Mapping_Geothermal_Potential_In_The_Western_United_States
- https://pubs.usgs.gov/publication/70158979
- https://www.osti.gov/biblio/1724080 ; https://gdr.openei.org/submissions/756
- https://pubs.usgs.gov/publication/70240475
- https://pubs.usgs.gov/publication/70250639
- https://www.usgs.gov/publications/separating-signals-elevation-data-improves-supervised-machine-learning-predictions
- https://pubs.usgs.gov/publication/70270953 ; https://doi.org/10.5066/P14EET2C
- https://newsletters.aapg.org/core-elements-11-03-25
- https://pubs.usgs.gov/fs/2025/3027/fs20253027.pdf ; https://doi.org/10.5066/P14LU7WD ; https://doi.org/10.5066/P149FR54 ; https://doi.org/10.5066/P9BZPVUC
- https://www.osti.gov/pages/servlets/purl/3018341 ; https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2025/Trainorguitton.pdf
- https://sciencebase.gov/catalog/item/6927454dd4be02716f722cb3
- https://www.thinkgeoenergy.com/zanskar-announces-discovery-of-big-blind-geothermal-site-in-western-nevada-usa/
- https://www.technologyreview.com/2025/12/04/1128763/ai-geothermal-zanskar/
