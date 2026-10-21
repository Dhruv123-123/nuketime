# L03 — Machine learning for geothermal exploration: literature review (2015–2026)

**Question:** How much measurable lift does ML give over classical geothermal exploration methods (expert play fairway analysis, weights of evidence, physics-based conductive models)? What are the benchmarks, validation metrics and validation wells?

**Bottom line:** The peer-reviewed literature is about 90% USGS, UNR, PSU and LBNL work on the Great Basin. It shows real but modest and unevenly measured lift.
- **Best headline result.** Mordensky et al. (2025, *Geothermics*) put **85% of power-producing systems with operating plants into the top 10% of map area**. They predict hidden and exposed systems about equally well: **5 of 9 hidden** and **10 of 19 exposed** systems fall in the 99th percentile.
- **Classification metrics are poor.** F1 is below 0.10 for every western-US model, because negative labels are missing and classes are extremely imbalanced (about 1:5,100 positives to negatives).
- **Algorithms.** Gradient boosting (XGBoost) consistently matches or beats neural networks.
- **Where the limit lies.** The binding constraint is feature-data resolution and labels, not the algorithm. This is the central fact for a Terranox-shaped company. The edge comes from new and better-digitised data and from ground truth. Model architecture adds little.
- **Zanskar.** No peer-reviewed paper reports Zanskar's model performance. Its public technical output is an infrastructure paper (GeoCore, Stanford 2025), and its validation is company-reported drilling.

---

## 1. Primary sources reviewed (chronological)

### 1.1 Faulds et al. — Nevada Play Fairway Analysis (DOE, 2015–2021): the classical baseline
- **Method.** Expert-weighted fairway maps over about 96,000 km² of Nevada. Inputs: structural setting, slip and dilation tendency, recency of faulting, geochemistry, gravity/MT. Phase III drilled temperature-gradient (TG) holes, generally about 500 ft deep, at the two top sites.
- **Result.**
  - Southern Gabbs Valley: **about 120 °C at about 150 m** in TG wells, a blind system with no surface manifestations.
  - Six TG holes overall gave **about 96 °C at about 250 m**.
  - Faulds called success at **2 of 2 drilled sites** "initial validation."
- **Relevance.** Expert play fairway analysis (PFA) has already found blind systems, so ML has to beat a non-trivial baseline. A lesson recorded in the project: sites in Cenozoic basins "cannot be recognized without detailed geophysical surveys." Regional data alone are not enough.
- Sources: https://www.usgs.gov/publications/discovering-blind-geothermal-systems-great-basin-region-integrated-geologic-and ; https://www.energy.gov/sites/prod/files/2017/12/f46/3_2_Play%20Fairway_Nevada%20Bureau%20of%20Mines%20and%20Geology_Discovering%20Blind%20Geothermal_Presentation.pdf

### 1.2 Brown, Coolbaugh, DeAngelo, Faulds, Fehler, Gu, Queen, Treitel, Smith, Mlawsky (2020), GRC Trans. v.44, 920–932 — "ML for natural resource assessment: blind geothermal systems of Nevada"
- **Method.** The first-year Nevada Machine Learning (NVML) workflow, built in TensorFlow/Keras on the PFA dataset.
- **Data.** About 85 known active systems as candidate positives and more than 12 geologic, geophysical and geochemical features.
- **Result.** No quantitative performance metrics are reported. The paper is mainly about data problems: very few labels, and features with mixed resolution.
- Sources: https://pubs.usgs.gov/publication/70217661 ; https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2020/Faulds.pdf

### 1.3 Shahdi, Lee, Karpatne, Nojabaei (2020 preprint; published 2021 in *Geothermal Energy*) — ML subsurface temperature, NE US
- **Method.** Several ML regressors (XGBoost, random forest, neural networks and others) predict temperature at depth and geothermal gradient. They are trained on oil and gas bottom-hole temperatures (BHTs) plus geological features.
- **Result.** XGBoost was best, with **MAE 3.19 °C and RMSE 4.94 °C**. The model produced 2D temperature maps at three depths.
- **Relevance.** This is direct evidence that legacy oil and gas BHT data, which is public but messy, can be turned into usable temperature-at-depth maps by ML. That is the Terranox analogue to "illegible assessment files."
- Source: https://www.researchsquare.com/article/rs-131433/v1 (journal version: Geothermal Energy 9, 2021 — journal details unverified)

### 1.4 Mordensky, Lipor, DeAngelo, Burns, Lindsey (2023), *Geothermics* 110, 102662 — "When less is more"
- **Method.** Nine favorability maps of the western US built from the USGS 2008 assessment inputs: heat flow, distance to Quaternary fault, distance to Quaternary magma, seismic density and SHmax. The approaches were:
  - the 2008 expert weights-of-evidence and logistic-regression maps;
  - logistic regression, XGBoost and SVM without expert input, under two positive-unlabeled (PU) and class-imbalance training strategies;
  - a neural network.
- **Data.** 278 known positives and **no known negatives**.
- **Results.**
  - Modern ML **outperformed expert-dependent methods**.
  - **All F1 scores were below 0.10** and did not improve as models got more complex.
  - XGBoost was as good as or better than the neural network.
  - The authors conclude the limiting factor is the input features, not the algorithm.
- Sources: https://www.usgs.gov/publications/when-less-more-how-increasing-complexity-machine-learning-strategies-geothermal-energy ; data release DOI 10.5066/P9V1Q9XM

### 1.5 Smith, Faulds, Brown, Coolbaugh, DeAngelo, Glen, Burns, Siler, Treitel, Mlawsky, Fehler, Gu, Ayling (2023), *Geothermics* 111, 102693 — Exploratory ML in Nevada PFA
- **Method.**
  - Supervised: **Bayesian probabilistic neural networks**, which give favorability with confidence intervals.
  - Unsupervised: **PCA plus k-means**.
  - Training: positives are known systems; negatives are drill sites with unsuitable conditions.
- **Result.** The models revealed controls on favorability that had not been recognised before, tied to structural-hydrologic domains, and were compared against the expert PFA. The abstract gives no AUC or accuracy.
- **Data.** Model GeoTIFFs (ANN, ELM, BNN, PCA) and Python code are public on the Geothermal Data Repository (GDR).
- Sources: https://pubs.usgs.gov/publication/70241433 ; https://gdr.openei.org/submissions/1351

### 1.6 Caraccioli, Mordensky, Lindsey, DeAngelo, Burns, Lipor (2023), GRC Trans. v.47, 1672–1689 — "Don't Let Negatives Hold You Back"
- **Method.** Re-fits the NVML data, with **83 positives and 62 expert-chosen negatives**, under three strategies:
  - NVML's expert negatives;
  - random negatives at the same frequency;
  - random negatives at the **natural class imbalance of about 1:5,100**, assuming about 1 in 4 systems is already found.
- **Models.** XGBoost and logistic regression, run over 60 train/test splits, with ROC-AUC, F1 and SHAP sensitivity analysis.
- **Results.**
  - F1 *favoured* the expert-negative strategy.
  - The authors argue F1 is misleading under positive-unlabeled data, because "false positives" may be undiscovered systems.
  - On the metric that matters for exploration, the CDF of favorability at known positives against unlabeled cells (the smallest area that captures the known systems), **natural-imbalance XGBoost beat the NVML neural network**.
  - Expert selection of negatives "imparted modeling bias."
  - All maps show an east-west bias driven by elevation and strain rate, and smooth interpolated inputs limit fidelity.
- Source: https://par.nsf.gov/servlets/purl/10536402 (full PDF read)

### 1.7 Mordensky, Burns, DeAngelo, Lipor (2023), GRC Trans. v.47, 1763ff — "Predicting Large Hydrothermal Systems" (INGENIOUS)
- **Method.** Regression rather than classification. XGBoost and linear regression are trained on **3,869 well-based "convective signals"**: well heat flow minus modelled conductive background, from -91 to 11,105 mW/m². Features come from the DOE INGENIOUS Great Basin dataset.
- **Results.**
  - XGBoost beats linear regression.
  - Truncated-label XGBoost puts **half of the high-signal wells in the top 3% of predictions**. The all-data model needs the top 13%.
  - The all-data model is better at capturing the **18 power plants above 130 °C**.
  - Both underpredict magnitude, which the authors attribute to input resolution being coarse compared with upflow zones only a few km wide.
- **Relevance.** The labels are well heat-flow residuals. Legacy wells are the training signal, which is exactly a Terranox-type data moat.
- Source: https://par.nsf.gov/servlets/purl/10536406 (full PDF read)

### 1.8 Shima, Ishitsuka, Lin et al. (2024), *Geothermal Energy*; Ishitsuka & Lin (2023), *Applied Energy* — physics-informed neural networks (PINNs) for natural-state temperature
- **Method.** PINNs that enforce the heat and mass-transport equations to invert for temperature, pressure and permeability fields. The 2024 paper pre-trains on numerical reservoir simulations, then fine-tunes on well logs through transfer learning.
- **Result.**
  - The PINN beats a plain neural network in 2D synthetic tests (2023).
  - Transfer learning improves predictions **away from wells**, the regime that matters for greenfield exploration (2024).
  - Gains are shown on synthetic and field-scale cases, not as regional prospect hit rates.
- Sources: https://repository.kulib.kyoto-u.ac.jp/dspace/bitstream/2433/284028/1/j.apenergy.2023.120855.pdf ; https://link.springer.com/article/10.1186/s40517-024-00312-7

### 1.9 Aljubran & Horne (2024), arXiv 2403.09961 (Stanford) — InterPIGNN thermal Earth model of the conterminous US
- **Method.** A physics-informed graph neural network. It is trained on BHTs plus elevation, sediment thickness, magnetics, gravity, gamma-ray, seismicity and electrical conductivity, and constrained by 3D heat conduction.
- **Result.** Temperature at 0–7 km on an 18 km² grid, with **MAE 4.8 °C (temperature), 5.8 mW/m² (heat flow) and 0.022 W/m·°C (conductivity)**. The authors claim it beats prior baselines. The specific baselines are not named in the abstract.
- **Relevance.** A public, national ML temperature model already exists. Basic temperature-at-depth maps are being commoditised, and the edge has to come from local, proprietary or ground-truthed data.
- Source: https://arxiv.org/abs/2403.09961

### 1.10 Mudunuru, Vesselinov, Ahmmed (2022), arXiv 2210.08685 (LANL) — GeoThermalCloud / NMFk
- **Method.** Unsupervised non-negative matrix factorisation with k-means (NMFk), applied to PFA datasets: Brady, SW New Mexico, Great Basin and others.
- **Result.** Extracts "hidden signatures" that support blind-system discovery. The work is **qualitative and has no validation metrics**.
- Source: https://arxiv.org/abs/2210.08685

### 1.11 Trainor-Guitton et al. (2025), Stanford SGW 50 — quantile regression of nameplate MW (NREL)
- **Method.** XGBoost quantile regression on **37 nameplate capacities (positives) and 248 zero-MW sites**, with 48 attributes. Its P50 and P90 outputs feed NREL's reV model.
- **Result.** Technical capacity and LCOE distributions are "much tighter and lower" than earlier estimates. Headline MWe was not retrieved (unverified).
- **Relevance.** ML is moving from "is it hot?" to "how many MW?", which is the valuation question for a right-flipping model.
- Source: https://research-hub.nrel.gov/en/publications/quantile-model-regression-of-nameplate-capacities-p50-and-p90-meg/

### 1.12 Mordensky, Burns, Lipor, DeAngelo (2025), *Geothermics* 133, 103450 — USGS Great Basin favorability for the new assessment (the strongest result)
- **Method.**
  - Combined data-driven ML with 16 input features and a "much larger training set."
  - Uncertainty from Monte Carlo cross-validation with **n = 1,200 realisations**; the median map is used.
  - Feeds the 2025–26 USGS hydrothermal assessment update.
- **Results.**
  - **85% of power-producing systems with operating plants fall in the most favorable 10% of the area.**
  - **Over half fall in the 99th percentile: 10 of 19 exposed and 5 of 9 hidden.** Hidden and exposed systems are predicted about equally well.
  - The map favours systems with higher convective heat flow.
  - It outperforms prior mapping because of better methods, input data and labels.
- **Companion work.** DeAngelo, Burns & Mordensky (2026, SGW 51) compile **28 systems with operating plants, 78 known electric-grade systems and 99 new probable electric-grade systems (205 total)**.
- Sources: https://pdxscholar.library.pdx.edu/ece_fac/862 ; https://www.usgs.gov/publications/favorability-mapping-hydrothermal-power-resource-assessments-great-basin-usa ; https://pubs.usgs.gov/publication/70273870 ; data DOI 10.5066/P14EET2C

### 1.13 Grujic, Hossler, Lipscomb, Morrison, Smith (2025), Stanford SGW 50 — "GeoCore" (Zanskar)
- **Method.** An infrastructure paper. Feature engineering is pushed into a data warehouse (Snowflake with an H3 hex grid). Models run on about **4 million grid cells on an M1-Max laptop**, with spatial cross-validation.
- **Result.** No prospect-level performance metrics.
- **Note.** Co-author Connor M. Smith is the first author of the Smith et al. 2023 NVML paper. Zanskar hired directly out of the UNR/USGS ML pipeline.
- Source: https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Grujic.pdf ; https://pangea.stanford.edu/ERE/db/IGAstandard/record_detail.php?id=38023

---

## 2. What lift does ML deliver? Synthesis

| Metric | Classical baseline | ML result | Source |
|---|---|---|---|
| Plants captured in top 10% of area | 2008 expert WoE/LR maps (inferior; exact number not retrieved) | **85%** of plants; 5/9 hidden in the 99th percentile | Mordensky 2025 |
| F1 (western US) | Expert 2008 maps | All models **below 0.10**; no gain from complexity | Mordensky 2023 |
| Area needed to capture half the high-heat-flow wells | — | **3%** (truncated XGB) or **13%** (all-data XGB) | Mordensky GRC 2023 |
| Temperature-at-depth error from BHTs | Physics/conductive interpolation | MAE **3.2 °C** (NE US) and **4.8 °C** (CONUS) | Shahdi 2021; Aljubran & Horne 2024 |
| Expert-picked versus natural-imbalance negatives | NVML neural net with 62 expert negatives | XGBoost with natural imbalance wins on area efficiency | Caraccioli 2023 |
| Field drilling validation | PFA: 2 of 2 sites hot in TG holes | Zanskar claims 3 of 3 sites (company-reported) | Faulds; TechCrunch 2026 |

Key observations:
1. **Lift is measured as area efficiency, not AUC.** Because there are no true negatives, the field has standardised on cumulative-distribution metrics of the form "the share of known systems that falls in the top X% of the map." Area efficiency translates straight into economics: fewer leases and TG holes per discovery.
2. **XGBoost beats deep learning** on current regional data. Model complexity does not improve the scores.
3. **Feature resolution is the ceiling.** The cited papers attribute the remaining errors to smooth, coarse inputs relative to upflow zones a few km wide. Better and denser data — digitised legacy well logs, BHTs, TG holes, mining drill holes, newly acquired geophysics — is where the next lift will come from.
4. **No study reports a blind prospective test with a held-out drilling program**, meaning "we ranked N prospects and then drilled them." The only real out-of-sample validation is industry drilling: Zanskar and the PFA TG holes.
5. **Gradient-hole data are decisive.** Zanskar's field crews drill shallow TG holes over areas of about 100 square miles. PFA also confirmed via TG holes. ML narrows the area to search, and cheap thermal holes provide the proof.

## 3. Zanskar's position, from the literature

- **Claimed record.**
  - Big Blind (NV): **121 °C at about 823 m**, on **one federal lease** it purchased. Billed as the first commercial blind discovery in the US in over 30 years.
  - Pumpernickel (NV): **about 137 °C at about 762 m**. Phase 1 plan is **20 MWe**, and discovery cost per MW is claimed **10x lower** than historical greenfield explorers.
  - Lightning Dock plant (NM) revived; "three of three" sites called successes.
  - Pipeline of **at least 1 GW**; target of 10 confirmed sites for project finance; Series C of **$115M**.
- **Methods.** Supervised models trained on known and accidental discoveries plus simulations, Bayesian evidential learning for appraisal, and a proprietary simulator.
- **Disclosure.** There is **no peer-reviewed performance disclosure**. Validation is drilling results reported by the company.
- Sources: https://www.technologyreview.com/2025/12/04/1128763/ai-geothermal-zanskar ; https://techcrunch.com/2026/01/21/zanskar-thinks-1-tw-of-geothermal-power-is-being-overlooked/ ; https://www.thinkgeoenergy.com/zanskar-validates-ai-based-discovery-method-with-drilling-at-pumpernickel-geothermal-site-nevada/

---

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **Algorithms are commoditised and public. Data and rights are not.** USGS, NREL and UNR have published XGBoost favorability maps, code and features (GDR submission 1351; DOIs 10.5066/P9V1Q9XM and 10.5066/P14EET2C). Anyone, including a new entrant, starts with a Great Basin map that already puts 85% of plants in the top 10% of area. Zanskar's model edge over these public baselines is undisclosed and probably incremental. The defensible edge for a Terranox-shaped company is therefore what Terranox already does in uranium:
   - (a) turn **illegible, un-digitised records** into features: scanned oil and gas well logs and BHTs, state mining assessment files, old TG-hole reports, BLM well files;
   - (b) **buy the right before proof**.
2. **The literature names the gap.** Every ML paper here says lift is capped by coarse, smooth regional inputs and too few labels. The training labels are **well-based heat-flow residuals** (3,869 points in INGENIOUS). Each additional digitised legacy BHT or TG hole is both a new label and a new feature. Mass digitisation of historical subsurface records maps one-to-one onto Terranox's assessment-database machine. It attacks the bottleneck the USGS authors themselves identify.
3. **Geography gap vs Zanskar.** Nearly all published ML and Zanskar's activity sit in the Nevada/Great Basin extensional hydrothermal play, the place every company with a public map is now looking. A Terranox shape can go where BHT-rich but under-explored geology is:
   - sedimentary basins with dense oil and gas wells, such as the Williston (including Saskatchewan's own BHT archive), Permian, Gulf Coast geopressured, Denver-Julesburg and Uinta. These favour low-to-moderate-temperature and EGS/sedimentary-geothermal targets, now relevant given Fervo-style EGS and data-centre offtake;
   - state and private geothermal rights outside BLM competitive-lease hot zones.

   Shahdi (MAE 3.2 °C) and Aljubran & Horne (MAE 4.8 °C) show BHT-based ML temperature mapping works. What does not yet exist is a *rights-acquisition* engine built on it.
4. **Business-model gap.** Zanskar is vertically integrated: it explores, drills, builds and operates plants such as Lightning Dock, and raised $115M to do so. That is capital-heavy and slow, with about 3 years to first power at Pumpernickel. The Terranox shape **owns rights and flips proven states**, with confirmation by cheap TG holes. Literature and practice both show TG holes, at about 150–500 m, are the decisive, low-cost proof step. It sells upgraded prospects to Ormat, Fervo, utilities and data-centre developers, and keeps royalties or a carry. That is a land and royalty company, closer to a prospect generator than to a developer. No ML-native player seems to occupy this slot (unverified from a market scan; see the other evidence files).
5. **Validation risk is the same for everyone.** No paper reports AUC on a prospective drilling program, so the ML lift is still "plausible, not proven," Zanskar's included. Under the standing rules that must not kill the idea. A clear plan to close it: publish a held-out back-test (rank legacy prospects, then check against later drilling, as Mordensky did for 9 hidden systems) and run a cheap TG-hole program on the top-ranked leases.
6. **Scale check.**
   - USGS now counts **205 electric-grade systems in the Great Basin alone**: 28 producing, 78 known undeveloped and 99 new probable.
   - Zanskar argues undiscovered conventional resources are underestimated by 10x or more.
   - Even the conservative public numbers leave dozens of drillable, un-leased or cheaply leased prospects. Expanding to sedimentary-basin BHT plays and private and state rights makes the opportunity not "too small."

---

## Sources
- https://pdxscholar.library.pdx.edu/ece_fac/862 (Mordensky et al. 2025, Geothermics 133, 103450)
- https://www.usgs.gov/publications/favorability-mapping-hydrothermal-power-resource-assessments-great-basin-usa
- https://www.usgs.gov/publications/when-less-more-how-increasing-complexity-machine-learning-strategies-geothermal-energy (Mordensky et al. 2023)
- https://pubs.usgs.gov/publication/70241433 (Smith et al. 2023)
- https://pubs.usgs.gov/publication/70217661 (Brown et al. 2020)
- https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2020/Faulds.pdf
- https://par.nsf.gov/servlets/purl/10536402 (Caraccioli et al. 2023)
- https://par.nsf.gov/servlets/purl/10536406 (Mordensky et al. GRC 2023)
- https://www.researchsquare.com/article/rs-131433/v1 (Shahdi et al.)
- https://arxiv.org/abs/2403.09961 (Aljubran & Horne 2024)
- https://arxiv.org/abs/2210.08685 (GeoThermalCloud)
- https://repository.kulib.kyoto-u.ac.jp/dspace/bitstream/2433/284028/1/j.apenergy.2023.120855.pdf (Ishitsuka & Lin 2023)
- https://link.springer.com/article/10.1186/s40517-024-00312-7 (Shima et al. 2024)
- https://research-hub.nrel.gov/en/publications/quantile-model-regression-of-nameplate-capacities-p50-and-p90-meg/ (Trainor-Guitton et al. 2025)
- https://pubs.usgs.gov/publication/70273870 (DeAngelo et al. 2026)
- https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Grujic.pdf (Zanskar GeoCore)
- https://www.usgs.gov/publications/discovering-blind-geothermal-systems-great-basin-region-integrated-geologic-and
- https://www.energy.gov/sites/prod/files/2017/12/f46/3_2_Play%20Fairway_Nevada%20Bureau%20of%20Mines%20and%20Geology_Discovering%20Blind%20Geothermal_Presentation.pdf
- https://gdr.openei.org/submissions/1351
- https://www.technologyreview.com/2025/12/04/1128763/ai-geothermal-zanskar
- https://techcrunch.com/2026/01/21/zanskar-thinks-1-tw-of-geothermal-power-is-being-overlooked/
- https://www.thinkgeoenergy.com/zanskar-validates-ai-based-discovery-method-with-drilling-at-pumpernickel-geothermal-site-nevada/
