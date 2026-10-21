# L17: EGS siting criteria and favourability: where next-generation EGS works, and which land becomes valuable

Status as of 2026-10-21. Method: a literature review built from full-text reads of primary documents. These are NREL technical reports, the USGS assessment, the DOE Liftoff report, Fervo's S-1 and preprint, Stanford papers, and a peer-reviewed stress synthesis.

Two limits on access during this run:
- The shared web-search budget ran out at the start of this task, so sources were reached only by direct fetch of known URLs.
- The Stanford pangea server (Stanford Geothermal Workshop papers) returned HTTP 503 throughout, and Nature/Springer pages redirected to a login.

Where a figure comes from secondary coverage, I say so. Anything without a source is marked (unverified).

## Bottom line

1. **The sweet spot for commercial EGS is now well defined.** Fervo's S-1 screen asks for a reservoir of about 300-625°F (about 150-330°C) at no more than about 13,000 ft (about 4.0 km) vertical depth. Its operating projects sit at about 190-230°C at 2.3-2.9 km, in low-permeability crystalline or metamorphic basement, in the extensional western US.
2. **National maps hardly see the sweet spot.** In NREL's GeoVision binning of the SMU national temperature maps, rock at **3-4 km and above 175°C holds only about 2.7 GWe** of the 5,157 GWe deep-EGS total. Regional maps built from denser local data found **3.6-3.8x more resource at 3-3.5 km**, and added **about 230 GWe of shallow (<4 km) EGS** that the national maps missed. That is the "public-but-illegible data" gap in one number.
3. **Cheap, shallow, hot cells are rare.** Aljubran and Horne (Stanford, 2024) find that a depth of 4 km or less minimises LCOE on only **0.27% of US land area**. My own arithmetic puts that at roughly 22,000 km², or about 5.4M acres. The cells are mostly in the West. On 89% of US land, the cost-optimal depth is 7 km.
4. **What makes a site good is now measurable without flow tests.** DOE Liftoff names three properties: **"temperature at depth, rock properties, and stress direction, none of which require test wells that produce fluids."** Those are exactly the variables recorded in old oil and gas logs, bottom-hole temperatures (BHTs), gradient holes and geophysics.

## Source-by-source review

### 1. Augustine, Ho & Blair (2019). *GeoVision Analysis Supporting Task Force Report: Electric Sector Potential to Penetration.* NREL/TP-6A20-71833.
- Method: deep EGS covers rock at 3-7 km above 150°C, taken from the SMU temperature-at-depth maps (Blackwell et al. 2011). Each 1 km slice assumes a 10°C drawdown and a 20% recovery factor over 20 years. Total: **5,157 GWe**.
- Table 3 (MWe by depth and temperature). Shallow, hot resource is a small fraction of the total:

  | Depth | 150-175°C | 175-200°C | 200-225°C | 225-250°C |
  |---|---|---|---|---|
  | 3-4 km | 74,217 | 2,592 | 100 | 0 |
  | 4-5 km | 740,466 | 233,228 | 11,886 | 325 |
  | 5-6 km | 517,601 | 724,689 | 373,680 | 57,281 |

- Sensitivity runs used regional maps: Cascades at 1-4 km (Frone et al. 2015) and the Great Basin at 3 km (Coolbaugh et al. 2005, NBMG Map 151). They added **63 GWe** with "higher temperature estimates than from the SMU maps." The conclusion: "Detailed regional maps of EGS resources are needed to identify the most favorable EGS resources."
- 2050 Technology Improvement (TI) scenario: **60.7 GWe**, mostly deep EGS.
- URL: https://docs.nlr.gov/docs/fy19osti/71833.pdf

### 2. Augustine, Fisher, Ho, Warren & Witter (2023). *Enhanced Geothermal Shot Analysis for the Geothermal Technologies Office.* NREL/TP-5700-84822.
- Representative plant: **175°C, 3,000 m, binary EGS.** Overnight capital cost falls from **$32,255/kWe** (business as usual) to **$3,565/kWe** (Shot assumptions, an 89% reduction).
- Assumptions behind that figure:
  - 125 kg/s per producer
  - productivity index 38.1 kg/s/bar for producers and 70 kg/s/bar for injectors (90th percentile of hydrothermal wells)
  - drilling at 80% of GeoVision "ideal" cost
  - 100 MWe plants
- Regional studies added shallow resource:
  - Cascades: **106 GWe** at 1-4 km
  - Snake River Plain: **about 25 GWe** at 1-4 km
  - Great Basin: **116 GWe** at 3 km
  - Net: **about 230 GWe of shallow (<4 km) EGS** added, plus about 3,000 GWe at depths over 4 km, using a 3.7x multiplier.
- Regional versus national maps: potential at 3.5 km rose **1.8x** for the Snake River Plain and **3.8x** for the Cascades. Potential at 3 km rose **3.6x** for the Great Basin.
- Near-field EGS (hot, tight rock next to hydrothermal sites) was set equal to the hydrothermal base, at **28,166 MWe**.
- ReEDS model output: **38.3 GWe by 2035 and 90.5 GWe by 2050.** Deployed EGS LCOE is **$30-70/MWh**. In the West, EGS deploys only where its cost is no more than about $50/MWh in 2035 or about $45/MWh in 2050. That set the **$45/MWh Shot target**.
- Installed EGS by state in 2050:

  | State | GW |
  |---|---|
  | CA | 27.9 |
  | LA | 10.5 |
  | AZ | 9.7 |
  | ID | 8.6 |
  | OR | 8.4 |
  | CO | 4.1 |
  | UT | 3.4 |
  | TX | 3.1 |
  | WV | 3.1 |
  | NM | 2.5 |
  | NV | 2.4 |

  Nevada's low figure is notable. ReEDS spreads build across balancing areas, so it is not a ranking of resource quality.
- URL: https://docs.nlr.gov/docs/fy23osti/84822.pdf

### 3. Williams, Reed, Mariner, DeAngelo & Galanis (2008). *Assessment of Moderate- and High-Temperature Geothermal Resources of the United States.* USGS Fact Sheet 2008-3082.
- EGS mean is **517,800 MWe**: F95 345,100, F5 727,900, on private and accessible public land.
- For comparison, identified hydrothermal is 9,057 MWe and undiscovered hydrothermal is 30,033 MWe.
- "The presence of elevated temperatures at drillable depths is the dominant factor controlling the quality of the resource." The high heat flow that favours EGS "is more uniformly distributed across the western United States."
- EGS density is diffuse: about **0.5 MWe/km²**, against 10-20 MWe/km² for hydrothermal fields.
- Implication: EGS land is valued for heat over area. That calls for big, contiguous lease blocks instead of a single upflow.
- URL: https://pubs.usgs.gov/fs/2008/3082/pdf/fs2008-3082.pdf

### 4. US DOE (March 2024). *Pathways to Commercial Liftoff: Next-Generation Geothermal Power.*
- Next-generation potential is **90 GW by 2050** in the base case, **90-132 GW** across scenarios, and over 300 GW with flexibility. Resource totals: 5+ TW next-generation versus about 40 GW conventional.
- Phase 1 (to about 2030) is **2-5 GW across 4-6 states** for $20-25B. "Early competitive regions include states across most of the western U.S."
- Siting physics: EGS well depths vary "depending on where in the subsurface sufficient temperature and appropriate stress conditions are encountered, but typically are **4,500-12,000 feet**."
- Key characterisation variables: "temperature at depth, rock properties, and stress direction", with no fluid-producing test wells needed. EGS shifts risk "from resource identification to engineering."
- BLM process:
  - Leasing comes first, and a lease sale "can take over 4 years."
  - A **noncompetitive geothermal lease may be secured using an existing oil & gas lease** (co-production).
  - Exploration under a categorical exclusion takes 2-4 months.
  - Liftoff lists BLM lease nominations as a tracked metric for industry health.
- URL (CATF mirror of the DOE PDF): https://cdn.catf.us/wp-content/uploads/2025/06/09154348/doe-liftoff-nextgen-geothermal.pdf

### 5. Norbeck & Latimer (2023). "Commercial-scale demonstration of a first-of-a-kind enhanced geothermal system." EarthArXiv preprint (Fervo, Project Red, Nevada).
- Horizontal doublet with **about 3,250 ft laterals**. Maximum measured formation temperature was **376°F (191°C)**, and production reached 336°F.
- Reservoir rock was **mixed metasedimentary and igneous: phyllite, quartzite, diorite, granodiorite**.
- Test results: up to **63 L/s** over a 37-day crossflow test, with a **3.5 MWe** peak. Calibrated models suggest **up to 8 MWe per producer**.
- Takeaway: commercial EGS works in heterogeneous basement and does not need uniform granite.
- URL: https://eartharxiv.org/repository/view/5704/

### 6. Fervo Energy (2026). Form S-1 (SEC).
- Site screen:
  - "minimum reservoir temperature of approximately 300°F", "maximum ... approximately 625°F"
  - "cutoff vertical depth of about 13,000 feet"
  - targets "low-permeability geothermal formations" via horizontal wells
  - weighs stress conditions, transmission, market and permitting
- Land: **595,900 acres** of geothermal leases at 31 Dec 2025, about 256,000 of them "Prospects". The position was assembled 2019-2021 at a **weighted average of about $4/acre**. 2025 BLM maximum bids reached **$344 (UT) and $410 (NV) per acre**.
- Capacity:
  - Cape is about 4.3 GW potential.
  - Pipeline: 550 MW ready to build, 2.6 GW advanced, and over 38 GW early-stage across 10 GeoClusters.
  - The thermal recovery factor is 30.5%, set from "reservoir temperature and thickness," fracture connectivity and drawdown.
- URL: https://www.sec.gov/Archives/edgar/data/1853868/000162828026025821/fervoenergy-sx1.htm

### 7. Aljubran & Horne (2024). "Thermal Earth Model for the Conterminous United States Using an Interpolative Physics-Informed Graph Neural Network." arXiv:2403.09961, published in *Geothermal Energy* (doi 10.1186/s40517-024-00304-7).
- A physics-informed graph neural network, constrained by 3D heat conduction, trained on **BHT measurements** plus elevation, sediment thickness, magnetics, gravity, gamma-ray, seismicity and conductivity.
- Output: temperature, heat flow and conductivity at 0-7 km in 1 km steps, on 18 km² cells. **Temperature MAE is 4.8°C.** Data are on the GDR, DOI 10.15121/2324793.
- Significance: proof that legacy BHTs plus ML give national-scale temperature-at-depth. It is now a public baseline, so differentiation has to come from finer, local data.
- URLs: https://arxiv.org/abs/2403.09961 ; https://gdr.openei.org/submissions/1592

### 8. Aljubran & Horne (2024). "Power supply characterization of baseload and flexible enhanced geothermal systems." *Scientific Reports* (s41598-024-68580-8).
I read this through ThinkGeoEnergy's summary; the Nature page needs a login.
- Gross EGS potential: **245,032 GW**.
- Average LCOE: $86.1/MWh with baseline drilling and $63.4/MWh with advanced drilling.
- Depth: **78% of potential is at 6-7 km.** A depth of 4 km or less is optimal on only **0.27% of US area**, and 7 km is optimal on 89.3%.
- Capacity under business as usual that beats marginal solar PV: only **0.65 GW**; with flexible dispatch, 46 GW.
- Top states by gross potential, in GW:

  | State | GW |
  |---|---|
  | CA | 20,882 |
  | OR | 18,270 |
  | NV | 16,484 |
  | MT | 15,681 |
  | TX | 14,578 |

- Model assumptions: 18 km² leases, 2,000 m laterals, 125 kg/s.
- URL: https://www.thinkgeoenergy.com/techno-economic-study-estimates-large-egs-potential-in-continental-us/

### 9. Ricks, Voller, Galban, Norbeck & Jenkins (2025). "The role of flexible geothermal power in decarbonized electricity systems." *Nature Energy* 10(1):28-40.
- Western-US capacity-expansion modelling. Flexible EGS, using in-reservoir storage at **59-93% round-trip efficiency**, raises EGS's least-cost share and lowers system cost.
- Value tilts towards sites near western load and transmission.
- URL: https://ideas.repec.org/a/nat/natene/v10y2025i1d10.1038_s41560-023-01437-y.html

### 10. Lund Snee & Zoback (2020). "Multiscale variations of the crustal stress field throughout North America." *Nature Communications* 11:1951.
- First quantitative continent-wide map of relative principal stress magnitudes, with hundreds of new SHmax orientations.
- Stress style shifts from **compression in the east, to strike-slip in the mid-continent, to "mostly extension in the west."** Short-wavelength rotations (under about 200 km) in the western US are not captured by geodynamic models.
- Implications for EGS siting:
  - The western US is mostly in a normal-faulting regime. There, hydraulic fractures open against the least horizontal stress, which is low compared with vertical stress, and that favours stimulation (unverified as a quantitative EGS claim in this source).
  - Local rotations mean stress direction has to be mapped site by site to orient laterals. Liftoff lists this as a key variable.
- URL: https://api.crossref.org/works/10.1038/s41467-020-15841-5 (DOI 10.1038/s41467-020-15841-5)

### 11. Utah FORGE (DOE GTO, 2017-2026).
- Granitic basement near Milford, UT. Stimulation in 2024 at wellbore temperatures above 200°C, in "hard hot granitic rock" from a 65° deviated well.
- On-bottom drilling time to 6,000 ft fell **from 440 to 60 hours**.
- 30-day circulation test (JPT): 420 gpm injection, **over 90% recovery**, about 370°F production.
- An extended circulation test began in Aug 2026.
- FORGE has contributed **more than 133 TB** of open data.
- FORGE sits next to Fervo's Cape Station. Both target the same buried, conductively heated basement under basin fill.
- URLs: https://www.energy.gov/eere/geothermal/forge ; https://jpt.spe.org/fervo-and-forge-report-breakthrough-test-results-signaling-more-progress-for-enhanced-geothermal

### 12. Mibei, Gold, Kolker, Dayo & Beckers (2024). "Geothermal Reservoir Characterization at Wattenberg area in Denver basin." NREL/PO-5700-90541 (GRC 2024).
- Corrected BHTs from about 2,500 m gas wells: **about 160°C, a 62°C/km gradient**, and an estimated **above 200°C at 3 km**.
- The anomaly is bounded by wrench-fault zones and sits over a vitrinite-reflectance anomaly.
- Takeaway: oil and gas data reveal EGS-grade heat outside the Basin and Range, in a basin with dense well control and existing mineral-rights structures.
- URL: https://docs.nlr.gov/docs/fy25osti/90541.pdf

## Synthesis: the siting criteria, ranked

1. **Temperature at 2-4 km.** Target 175-250°C, ideally above 200°C by 3 km, which means gradients of about 60-80°C/km.
   - This is the dominant cost lever (USGS, NREL).
   - Fervo's operating points: Red 191°C, and Cape and FORGE at about 200-230°C.
   - The Shot's representative case is 175°C at 3 km, at $3,565/kW.
2. **Basement or tight rock that can be drilled and fractured.**
   - Granite, granodiorite and metasediments all work (Red, FORGE).
   - Hydrothermal needs natural permeability; EGS does not. Liftoff says the needed inputs are temperature, rock properties and stress, with no flow test.
3. **Stress regime and orientation.**
   - The western US is extensional (Lund Snee & Zoback), which favours stimulation.
   - Local SHmax rotations under 200 km need mapping to orient laterals, and stress conditions set well depth (Liftoff, Fervo S-1).
4. **Thickness and contiguity.** EGS density is about 0.5 MWe/km² (USGS), and Fervo uses 30.5% recovery scaled by reservoir thickness. That means **large contiguous blocks**: Fervo has about 596k acres for over 40 GW.
5. **Surface factors.** Transmission, western load, permitting class (BLM versus private versus state) and seismic receptors. Liftoff reports lease sales taking over 4 years.

Where these overlap (from the sources above):
- Great Basin (UT/NV), the 116 GWe at 3 km set
- Cascades (OR/WA)
- Snake River Plain (ID)
- California
- Hot basins with oil and gas well control: Denver-Julesburg (CO); TX and LA appear in NREL's 2050 build

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **The data arbitrage is quantified in DOE's own numbers.** National maps put only about 2.7 GWe at 3-4 km above 175°C. Denser regional data multiply shallow resource 1.8-3.8x and added about 230 GWe below 4 km. The value sits in local, messy data: BHTs that need correction, scanned logs, gradient holes, state oil and gas archives. That is the Saskatchewan-assessment-file analogue.
   - Stanford's public BHT-ML model, at about 18 km² resolution, is now the baseline everyone has. The edge is parcel-scale resolution (about 1 km² or finer), plus stress and basement-depth layers that national models omit.
2. **The land that reprices is scarce and identifiable.** Aljubran and Horne find that shallow-optimal cells cover only 0.27% of US land, about 5.4M acres by my arithmetic. Fervo holds about 0.6M acres bought at about $4/acre, and BLM bids now clear at $344-410/acre. The step-up of roughly 100x on the bare right comes **before** any MW is proven.
   - A company that ranks the remaining EGS-grade cells and leases them first owns that step-up. That means BLM nominations, noncompetitive co-production leases on existing oil and gas leases, and state and private geothermal rights.
3. **Zanskar's gap.** Zanskar's public positioning is AI-led discovery of hydrothermal resources: blind convective systems such as Big Blind, and buying the Lightning Dock plant. Hydrothermal value depends on natural permeability and fluid. It is a hit-or-miss target with about 30 GWe undiscovered nationally (USGS).
   - EGS-grade land is the opposite class. It is conductive, tight, hot basement that hydrothermal models score as "dry hole". Its resource base is 10-100x larger (USGS 518 GWe versus 30 GWe; NREL 5 TWe+).
   - Zanskar's stack is optimised to find upflow, not to rank thick, hot, stress-favourable basement for horizontal multi-stage wells. The gap is an **EGS land bank**: map, acquire, lightly de-risk with one gradient hole and a stress log, then sell or joint-venture to Fervo-like developers, utilities and hyperscaler offtakers.
4. **De-risking is cheap compared with hydrothermal.** Liftoff says EGS characterisation needs no fluid-producing test well. A gradient or slim hole that confirms temperature at depth, plus image-log stress direction, can move a parcel into Fervo's screen (300-625°F, ≤13,000 ft). That is a cheap, Terranox-like proof step.
5. **Scale check (not too small).** The target is 90-132 GW by 2050 (DOE) and Fervo alone has a pipeline of over 38 GW. At about 0.5 MWe/km², 100 GW needs about 200,000 km² of heated footprint (my arithmetic; tighter well spacing would shrink this). Demand for EGS-grade rights is in the millions of acres.
6. **Risks.**
   - EGS land values depend on the EGS cost curve holding: Shot assumptions are at the 90th percentile of well productivity, and some critics argue per-well output is lower.
   - BLM lease timelines are slow, and Fervo, oil majors and Zanskar will compete for the same nominations.
   - Mitigation: score every parcel for both EGS and hydrothermal, and favour private and state rights in oil and gas basins (Denver-Julesburg, Permian, Gulf Coast), where well data are densest and BLM queues don't apply.

## Sources
- Augustine, Ho & Blair 2019 (GeoVision supply): https://docs.nlr.gov/docs/fy19osti/71833.pdf
- Augustine et al. 2023 (Enhanced Geothermal Shot): https://docs.nlr.gov/docs/fy23osti/84822.pdf
- USGS FS 2008-3082: https://pubs.usgs.gov/fs/2008/3082/pdf/fs2008-3082.pdf
- DOE Liftoff 2024 (mirror): https://cdn.catf.us/wp-content/uploads/2025/06/09154348/doe-liftoff-nextgen-geothermal.pdf
- DOE GeoVision page: https://www.energy.gov/eere/geothermal/geovision
- Norbeck & Latimer 2023: https://eartharxiv.org/repository/view/5704/
- Fervo Project Red release: https://fervoenergy.com/fervo-energy-announces-technology-breakthrough-in-next-generation-geothermal/
- Fervo S-1 2026: https://www.sec.gov/Archives/edgar/data/1853868/000162828026025821/fervoenergy-sx1.htm
- Aljubran & Horne 2024 InterPIGNN: https://arxiv.org/abs/2403.09961 ; https://gdr.openei.org/submissions/1592
- Aljubran & Horne 2024 Sci Rep (secondary): https://www.thinkgeoenergy.com/techno-economic-study-estimates-large-egs-potential-in-continental-us/
- Ricks et al. 2025 Nature Energy: https://ideas.repec.org/a/nat/natene/v10y2025i1d10.1038_s41560-023-01437-y.html
- Lund Snee & Zoback 2020: https://api.crossref.org/works/10.1038/s41467-020-15841-5
- Utah FORGE (DOE): https://www.energy.gov/eere/geothermal/forge
- JPT on Fervo/FORGE 2024: https://jpt.spe.org/fervo-and-forge-report-breakthrough-test-results-signaling-more-progress-for-enhanced-geothermal
- Mibei et al. 2024 Wattenberg: https://docs.nlr.gov/docs/fy25osti/90541.pdf
- Zanskar: https://www.zanskar.com/
