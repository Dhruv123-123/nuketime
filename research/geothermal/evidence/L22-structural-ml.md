# L22 — Structural geology as a geothermal signal: faults, slip/dilation tendency, stress, seismicity/InSAR, and their use in ML favourability

Method note: the shared WebSearch budget ran out before this agent started, so every source below was opened directly with WebFetch, mostly OSTI records, GDR, USGS, Nature Comms and Zanskar's own posts. Several OSTI pages show only the abstract. Where a number comes from the full text and I could not open it, it is marked (unverified). Classic method papers that I know by citation but could not fetch (Morris et al. 1996; Ferrill et al. 1999; Barton et al. 1995) are cited as cited inside fetched sources, not from the papers themselves.

## 1. Why structure is the key permeability layer

Most Great Basin hydrothermal systems are amagmatic. They are convective systems in extended crust, so heat is everywhere at depth and **permeability is the scarce input**. Permeability in these systems comes from faults, specifically small parts of faults that are complex and critically stressed. Structure is therefore the main way to find the permeability term of the play fairway "heat × permeability × fluid" equation. It is also the term that old well logs and BHT datasets (the other Terranox-style inputs) capture worst.

## 2. Literature reviewed (primary sources)

### 2.1 Faulds & Hinz (2015), WGC Melbourne: "Favorable tectonic and structural settings of geothermal systems in the Great Basin region… Proxies for discovering blind geothermal systems"
- This is an inventory of **426 known systems (≥37 °C)**, with structural settings classified for ~250 of them.
- **Shares by setting:**

  | Setting | Share |
  |---|---|
  | Step-overs / relay ramps | ~32% |
  | Normal-fault terminations | 25% |
  | Fault intersections | 22% |
  | Accommodation zones | 9% |
  | Displacement transfer zones | 5% |
  | Strike-slip pull-aparts | 3% |
  | Fault bends | 2% |
  | Major range-front faults | 1% |

- **~39% of known systems are blind.** Up to **75%** of the regional resource may be blind.
- Geothermal density and MW capacity track **tectonic strain rate**: highest in the NW Great Basin and the Walker Lane pull-aparts.
- Key point: **~88% of systems sit in a few mappable fault-geometry patterns** (step-overs, terminations, intersections, accommodation zones). Mid-segment range fronts, the classic drilling target, host ~1%.
- https://www.osti.gov/biblio/1724082 (dataset: https://www.osti.gov/biblio/1148722, Faulds 2013, 426-system structural inventory)

### 2.2 Faulds, Hinz, Coolbaugh, Ayling, Glen, Craig, McConville, Siler, Queen, Witter, Hardwick (2021), DOE final report: "Discovering Blind Geothermal Systems in the Great Basin… Play Fairways: All Phases"
- The model combined **9 geologic, geochemical and geophysical parameters** into a weighted fairway map covering **96,000 km²** of Nevada.
- It produced **24 highly prospective areas**, and **5** of them went to detailed study.
- **Temperature-gradient (TG) drilling** tested two valleys:
  - SE Gabbs Valley: **124 °C at 152 m**, from 6 TG holes.
  - N Granite Springs Valley: **~96 °C at ~250 m**, from 6 holes.
- This is the clearest public proof that a structure-led fairway map can find blind systems with cheap shallow holes.
- https://www.osti.gov/biblio/1724080

### 2.3 Craig (2018), DOE-UNR report, and Faulds, Craig, Hinz et al. (2018), GRC Trans. 42: Gabbs Valley blind discovery (later in Geothermics 2021 as Craig et al. (unverified bibliographic detail))
- **Structural setting.** The system sits in a displacement transfer zone where the dextral Petrified Springs fault ends in normal faults. Concealed NW dextral-normal faults intersect NNE–ENE normal faults there, forming a dense fault-intersection zone that shows up as a gravity high.
- **Coincident anomalies.** Intersecting gravity gradients, a magnetic low, low MT resistivity, and a 2 m temperature anomaly all overlap.
- **Temperatures.** **2 of 6 TG holes exceeded boiling (114.5 °C and 124.9 °C).** Geothermometers give **130–140 °C**.
- **Surface expression.** None: "no surface hot springs, fumaroles, or paleo-geothermal deposits."
- **Lesson.** The productive target was a concealed fault intersection found from gravity and magnetics, not from surface fault maps. Inferred buried structure matters as much as mapped Quaternary faults.
- https://www.osti.gov/biblio/1724116 ; https://www.osti.gov/biblio/1724101

### 2.4 Siler & Pepin (2021), Geothermics 94:102112: "3-D geologic controls of hydrothermal fluid flow at Brady geothermal field"
- The authors built 3D structural variables from a 3D geologic map: fault proximity, slip and dilation tendency, fault and fracture density, and intersections.
- They compared these variables with productive and non-productive well intervals using PCA.
- **Production intervals sit within or near stress-loaded (critically stressed) macro-scale faults and in zones of high fault and fracture density.**
- Vertical connectivity is "rare and patchy." This is why 2D maps undersell the problem and well-scale 3D structure matters for development.
- https://www.osti.gov/biblio/1848395

### 2.5 Faulds (2013), GDR/NGDS datasets: slip and dilation tendency for Patua, Tuscarora, McGinness Hills, Salt Wells, San Emidio, Neal Hot Springs
- **Method.**
  - Slip tendency Ts = τ/σn (Morris et al. 1996).
  - Dilation tendency Td = (σ1−σn)/(σ1−σ3) (Ferrill et al. 1999).
  - Both computed in 3DStress, scaled 0–1.
- **Stress inputs.** Stress came from the World Stress Map plus regional and local data. Great Basin ratios: Shmin/SHmax = 0.527 and Shmin/Sv = 0.46. Shmin azimuth ≈105° at Patua.
- **Regimes.** Both normal and strike-slip regimes were tested.
- **Dip handling.** Dip was set to the value that maximises Ts and Td, so the outputs are **upper bounds**.
- **Read-across.** These open per-field Ts/Td layers exist for **operating Ormat fields such as McGinness Hills, Tuscarora and San Emidio**. They can serve as labelled positives for the "critically stressed fault" feature.
- https://www.osti.gov/biblio/1136720 (and sister records 1136717–1136722)

### 2.6 Lund Snee & Zoback (2020), Nature Communications 11:1951: "Multiscale variations of the crustal stress field throughout North America"
- **Data.** Faulting regime at **~2,000 locations**, **~800 new or recent SHmax orientations** on top of **>1,500 WSM** orientations, and a catalogue of **>50,000 focal mechanisms**.
- **Western US.** The region is mostly normal and strike-slip. **SHmax rotates up to ~90° over tens of km** at the edges of extensional provinces, including the Great Basin and Rio Grande Rift.
- **Models.** Current geodynamic models do not predict rotations shorter than ~200 km.
- **Implication.** Regional-average stress (as in the 2013 Ts/Td layers) is too coarse in exactly the transitional zones, such as the Walker Lane/Basin-and-Range boundary, where geothermal clusters. A finer stress map from focal mechanisms and borehole breakouts is a real data-product edge.
- https://www.nature.com/articles/s41467-020-15841-5

### 2.7 Smith, Faulds, Brown, Coolbaugh, DeAngelo, Glen, Burns, Siler et al. (2023), Geothermics 111:102693: "Exploratory analysis of ML techniques in the Nevada geothermal PFA"; plus Faulds et al. (2023), Stanford SGW, and Smith et al. (2021), Stanford SGW
- **Two methods worked:**
  - Supervised **Bayesian probabilistic neural networks**, which give favourability with confidence intervals.
  - Unsupervised **PCA + k-means**.
- **Training set:** about **85 active systems** as positives, plus drilled "unsuitable" sites as negatives.
- **Features:** more than 12, including "potential structures" and slip/dilation tendency.
- **Feature ranking.** The 2021 paper ranks features by permutation and drop-out. The ranking itself was not in the abstract (unverified).
- **Open release.** The ML GeoTIFFs and Python code are public.
- https://www.osti.gov/biblio/1999607 ; https://www.osti.gov/biblio/1999432 ; https://www.osti.gov/biblio/1999597 ; code: https://www.osti.gov/biblio/1897035

### 2.8 Mordensky, Lipor, DeAngelo, Burns, Lindsey (2023), Geothermics 110:102662: "When less is more…"
- The authors compared 9 western-US favourability maps built on the USGS 2008 inputs: expert WofE/LR, plus LR, XGBoost, SVM and ANN.
- **All F1 < 0.10.** F1 did **not improve with model complexity**. XGBoost ≥ ANN.
- The authors conclude that **features, not algorithms, are the bottleneck**. The data are positive-unlabelled with severe class imbalance.
- **Implication.** The edge is in better feature layers: fine-scale stress, inferred buried faults, and digitised BHTs. Fancier models are not the edge.
- https://www.osti.gov/biblio/2418597

### 2.9 INGENIOUS: Ayling, Faulds, Siler, Kreemer, DeAngelo, Glen et al. (2022), GDR 1391; Hart-Wagoner, Lindsey, Trainor-Guitton, Coolbaugh, Faulds (2024 GRC / 2025 NREL CP)
- **Open regional stack** for NV, W UT, S ID, SE OR and E CA. Layers:
  - **Quaternary faults v1/v2** (traces, ages, slip rates).
  - **Slip and dilation tendency** on Quaternary faults.
  - **Geodetic shear- and dilation-strain models.**
  - **Earthquake-density models.**
  - Heat flow, 2 m temperatures, MT conductance, gravity and magnetics, sinter/tufa, and detrended topography.
- **Clusters.** PCA + k-means gives clusters that match geologic domains: Walker Lane, the extensional western Great Basin, low-strain eastern NV/W UT, Quaternary volcanic fields, and the Snake River Plain margin.
- **Implication.** Feature weights differ by domain, so multiple conceptual models are needed.
- https://gdr.openei.org/submissions/1391 ; https://www.osti.gov/biblio/2523997

### 2.10 Trainor-Guitton, Menon, Pinchuk, Thomson, Hart-Wagoner, Lu, Mlawsky, Coolbaugh, Lindsey, Faulds (2025), Geothermics 133: "'Hidden' hydrothermal technical potential & technoeconomics"
- **Model.** XGBoost regression on **48 geologic and geophysical features**, trained on the nameplate MW of **37 operating plants** plus 0-MW negatives.
- **Pipeline.** The predictions feed NREL's reV model for capacity and LCOE.
- **Result.** Great Basin hidden-hydrothermal capacity and LCOE distributions are **tighter and lower** than earlier temperature-only estimates. MW totals were not in the abstract (unverified).
- **Implication.** Adding permeability proxies (structure) *reduces* headline MW but makes it bankable.
- https://www.osti.gov/biblio/3018341

### 2.11 Trainor-Guitton, Siler, Ayling (2023), Geoenergy 1(1): structural proxies as geostatistical constraints, Granite Springs Valley NV
- **Approach.** Measured temperatures are the primary data. Structural proxies are secondary data: distance to faults, distance to fault intersections and terminations, Coulomb stress change, and dilation tendency.
- **Outputs.** **V_prior** gives P(economic T). **Entropy** gives where to drill next.
- **Value for an acquirer.** This is a value-of-information framework, which is exactly what is needed to decide which leases to bid on and where to put the first TG hole.
- https://www.osti.gov/biblio/2217601

### 2.12 Wannamaker, Moore, Nash, Simmons et al. (2020), DOE PFA, eastern Great Basin, Utah
- **Permeability layers:** fault density, critically stressed zones, **seismicity**, and gravity, combined with heat (MT lows, BHTs, chemistry, volcanism) by probability kriging.
- **Regional heat:** ~5 GWt above background.
- **Outcome.** The test well near Cove Fort was cancelled. This is a reminder that fairway work often stalls at the drilling step, not at the mapping step.
- https://www.osti.gov/biblio/1695591

### 2.13 Seismicity / InSAR as permeability signal
- **Vasco, Rutqvist, Jeanne, Samsonov, Hartline (2020), The Leading Edge 39(12).** InSAR is "the method of choice" for deformation monitoring at geothermal fields. Geodesy is a cost-effective complement for resource characterisation (The Geysers case). https://www.osti.gov/biblio/1828553
- **Reinisch, Cardiff, Kreemer, Akerley, Feigl (2020), JGR Solid Earth.** Brady InSAR+GPS from 2003–2018, modelled in 1,656 voxels. Subsidence is dominated by **thermal contraction**, and rate changes track well operations. This is a **monitoring/production** signal, not a greenfield exploration signal. https://www.osti.gov/biblio/1639028
- **Feigl et al. (2025), WHOLESCALE, San Emidio.** Shutdowns raise pore pressure and lower effective normal stress on faults. Pumping reduces microseismicity. This supports the critically stressed fault–fluid link. https://www.osti.gov/biblio/2588223
- **Akerley (Ormat), Warren (Zanskar), Gasperikova (LBNL), Pullammanappallil (2023), DOE report.** Passive seismic emission tomography plus cooperative MT/gravity/active-seismic inversion maps 3D permeability at **San Emidio and Crescent Valley** without a full 3D active survey. **A Zanskar employee is a co-author.** https://www.osti.gov/biblio/1986084
- **Geodetic strain.** INGENIOUS includes geodetic dilation-strain rasters (Kreemer). Faulds & Hinz 2015 report that geothermal density tracks strain rate.
- **Bottom line on InSAR for greenfield work:** broadly useful as a regional strain/dilatation feature. Pixel-level InSAR anomalies over undeveloped blind systems are not established in the literature I reviewed (unverified gap).

### 2.14 USGS Quaternary Fault and Fold Database
- **Coverage:** US faults with evidence of surface deformation in roughly the last 1.6 Ma, with 12 state cooperators.
- **Attributes:** 4 age classes, 4 slip-rate classes, sense, dip direction, and evidence class A–D.
- **Access:** GIS download ~16 MB. Database search was retired 26 Feb 2026; access is now through the map.
- **Caveat:** it is a hazard archive. Concealed faults under basin fill (the Gabbs-type targets) are by definition missing.
- https://www.usgs.gov/programs/earthquake-hazards/faults

### 2.15 USGS 2008 assessment, Williams et al., FS 2008-3082
- Identified: **9,057 MWe**. Undiscovered mean: **30,033 MWe**. EGS: **517,800 MWe**.
- This is the size of the blind-hydrothermal prize that structural targeting addresses: **~3.3× identified**.
- https://pubs.usgs.gov/fs/2008/3082/

## 3. Zanskar (comparator), as it relates to structure

- **Big Blind, W Nevada (announced Dec 2025):**
  - No surface expression.
  - Reservoir **~250 °F (~121 °C) at ~2,700 ft**, with total lost circulation and open fractures.
  - The anomaly was flagged in late 2023 from above-background heat flow. Two intermediate wells were drilled in Jul–Aug 2025.
  - Leases were bought **at BLM auction**.
  - Zanskar claims discovery cost **< $15k/MW**.
  - https://zanskargeothermal.substack.com/p/zanskar-proves-first-blind-geothermal
- **Pumpernickel (Sep 2025):** an "overlooked conventional" site found with AI. No public numbers.
- **Funding and model:**
  - $115M Series C (Jan 2026), **$180M total equity**, and $40M development capital (Apr 2026).
  - 100 MW PPA with NV Energy (May 2026).
  - Business model: **develops, builds, owns and operates**.
  - Pipeline described as "multi-GW."
  - https://zanskargeothermal.substack.com/p/zanskar-raises-115m-series-c-following ; https://www.zanskar.com/news
- **Structure in its public statements:** its posts stress heat-flow anomalies and "full-physics" models. Structure appears only as faulting seen in logs. Structural/stress feature engineering is not described publicly (unverified whether it is internal).

## 4. Synthesis: what structure buys an ML favourability model

1. **Signal is strong and well localised.**
   - ~88% of Great Basin systems sit in four mappable geometries.
   - Productive intervals sit on critically stressed faults (Brady).
   - Fairway maps found two blind systems (≥96–125 °C at <250 m) with only 6 TG holes each.
2. **Off-the-shelf layers are commoditised.** Quaternary faults, Ts/Td, strain, seismicity and gravity are all public in INGENIOUS. Anyone, including Zanskar, can use them.
3. **The bottlenecks are features:**
   - Mordensky (F1 < 0.1, flat across models).
   - Lund Snee & Zoback (stress rotates over tens of km, and regional-average Ts/Td is wrong at domain boundaries).
   - Gabbs (the target fault was buried and inferred from potential fields).
4. **Where a new entrant could build a better layer:**
   - (a) Inferred concealed faults from gravity/magnetic/LiDAR plus old oil, gas and water well picks.
   - (b) A local stress tensor from focal mechanisms and borehole breakouts or image logs in legacy O&G wells.
   - (c) Ts/Td recomputed on those inferred faults with locally rotated stress.
   - (d) 3D fault-intersection density.

## 5. Implications for a Terranox-shape geothermal company and the gap vs Zanskar

- **What carries over from Terranox.** Public-but-illegible data is the structural one: legacy O&G logs, image logs and mud logs (breakouts, lost circulation, fracture picks), unpublished state-survey fault maps, and mining assessment drilling. These are the inputs for concealed-fault and local-stress layers that INGENIOUS and USGS lack. Zanskar's public story centres on heat flow and physics simulation. A structure- and stress-first model ("permeability-first") is a defensible way to stand apart: heat is common in the Great Basin, and permeability is what kills wells.
- **The gap Zanskar leaves.** Zanskar is vertically integrated: it buys leases at BLM auction, drills and proves, then builds, owns and operates plants (Lightning Dock, 100 MW NV Energy PPA). Its capital goes into a few large sites. That leaves room for a **portfolio acquirer** that:
  - (i) uses structural ML to rank **hundreds of** BLM, state and private parcels;
  - (ii) leases many cheaply, including at the nomination/auction step;
  - (iii) proves them up with **$-cheap 2 m probes and 150–250 m TG holes**. Gabbs and Granite Springs show that 6 holes can confirm >100 °C.
  - (iv) sells or JVs the proven-up state to Ormat, Fervo, Zanskar itself, utilities or data-centre developers.

  This is the Terranox "own the step-up" model, which has lower capex per asset than Zanskar's build-own-operate model.
- **Size check (not too small).**
  - USGS undiscovered mean is ~30 GWe, ~3.3× identified.
  - ~39–75% of Great Basin resource is blind.
  - Each blind proved-up system likely means tens of MWe at shallow depth.
  - Zanskar claims >10× more with depth.
- **Risks:**
  - The public structural stack is free to all. The moat must be **proprietary derived layers plus the lease position**, not the model.
  - Zanskar co-authors DOE permeability-mapping work (Warren on the San Emidio/Crescent Valley PST report), so it is not structurally naive.
  - BLM competitive auctions expose nominations, so pre-proof cheapness is weaker than in Saskatchewan's staking regime (see other agents' lease-regime files).
  - InSAR's greenfield value is unproven. Use it as a regional strain feature, not as the core signal.
- **Score implication.** The structure signal is real, sourced and quantified, and an ML lift is plausible: features, not models, are the documented bottleneck, and better features are exactly what illegible legacy data provides. This supports a Terranox-shape acquirer if the lease-acquisition mechanics hold.

## Sources
- https://www.osti.gov/biblio/1724082 — Faulds & Hinz 2015 WGC, structural settings statistics
- https://www.osti.gov/biblio/1148722 — Faulds 2013 structural inventory dataset
- https://www.osti.gov/biblio/1724080 — Faulds et al. 2021 Nevada PFA final report
- https://www.osti.gov/biblio/1724116 — Craig 2018 Gabbs Valley
- https://www.osti.gov/biblio/1724101 — Faulds et al. 2018 GRC Gabbs Valley
- https://www.osti.gov/biblio/1848395 — Siler & Pepin 2021 Brady 3D controls
- https://www.osti.gov/biblio/1136720 — Faulds 2013 slip/dilation tendency, Patua (and 1136717–1136722)
- https://www.nature.com/articles/s41467-020-15841-5 — Lund Snee & Zoback 2020
- https://www.osti.gov/biblio/1999607 — Smith et al. 2023 Geothermics ML PFA
- https://www.osti.gov/biblio/1999432 — Faulds et al. 2023 SGW ML PFA
- https://www.osti.gov/biblio/1999597 — Smith et al. 2021 SGW
- https://www.osti.gov/biblio/1897035 — ML PFA code
- https://www.osti.gov/biblio/2418597 — Mordensky et al. 2023
- https://gdr.openei.org/submissions/1391 — INGENIOUS regional dataset
- https://www.osti.gov/biblio/2523997 — Hart-Wagoner et al. 2024/25
- https://www.osti.gov/biblio/3018341 — Trainor-Guitton et al. 2025 Geothermics
- https://www.osti.gov/biblio/2217601 — Trainor-Guitton, Siler, Ayling 2023
- https://www.osti.gov/biblio/1695591 — Wannamaker et al. 2020 Utah PFA
- https://www.osti.gov/biblio/2004915 — Pauling et al. 2023 PFA best practices
- https://www.osti.gov/biblio/1828553 — Vasco et al. 2020 TLE
- https://www.osti.gov/biblio/1639028 — Reinisch et al. 2020 JGR
- https://www.osti.gov/biblio/2588223 — Feigl et al. 2025 WHOLESCALE
- https://www.osti.gov/biblio/1986084 — Akerley, Warren et al. 2023 passive seismic permeability
- https://www.usgs.gov/programs/earthquake-hazards/faults — USGS Qfaults
- https://pubs.usgs.gov/fs/2008/3082/ — USGS 2008 assessment
- https://zanskargeothermal.substack.com/p/zanskar-proves-first-blind-geothermal — Big Blind
- https://zanskargeothermal.substack.com/p/zanskar-raises-115m-series-c-following — Series C
- https://zanskargeothermal.substack.com/p/using-custom-built-artificial-intelligence — Pumpernickel
- https://www.zanskar.com/news — Zanskar news index
