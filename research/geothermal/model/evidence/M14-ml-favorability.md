# M14: ML geothermal favorability models, why they plateau, and how to beat the plateau

Date: 23 Oct 2026. Slice M14, model track. This file builds on `../../evidence/L03-ml-geothermal.md` (which already lists Mordensky 2023 and 2025, Caraccioli 2023, Smith 2023, GeoThermalCloud 2022, Aljubran and Horne 2024, NREL quantile regression and Zanskar GeoCore), `M02-ingenious.md` (INGENIOUS layers and the Argenta Rise miss) and `M13-zanskar-methods.md` (Zanskar's 370-site inventory and its base rate of 1 blind system per ~550 holes). It does not repeat their headline numbers. What is new here: (1) the USGS "Cursed?" paper, which shows that adding features makes the model worse; (2) the full numbers behind the Bayesian neural network paper; (3) the 2026 GeoThermalCloud and EnviTrace update, which still has no metrics; (4) an arithmetic ceiling on F1 that explains the "F1 below 0.10" result; (5) the spatial cross-validation and positive-unlabeled (PU) learning literature from ecology and mineral exploration, with the specific way geothermal breaks the standard PU assumption; (6) a design for a better model. Web budget used: 10 searches and 9 fetches. Three fetches were blocked (the MDPI Tularosa NMFk paper, the PMC copy of Ploton et al. 2020, and the Turku spatial leave-pair-out page). Facts from those papers are from memory and are marked (unverified).

## Bottom line

Every public geothermal favorability model has hit the same ceiling. Changing the algorithm (logistic regression, XGBoost, SVM, neural network, Bayesian neural network, NMFk, GNN) moves the result very little. The reason is the data, not the method. There are only about 278 labeled positive cells against roughly 710,000 unlabeled ones. There are almost no true negatives. Input layers are smoothed over tens of kilometres, while upflow zones are 1 to 5 km wide. The labels are also biased in a specific way: a system becomes "known" mainly because its water reaches the surface. That violates the core assumption of standard PU learning, that labeled positives are a random sample of all positives. So the model learns "where hot water leaks out" as much as "where heat is", and that is the wrong lesson for blind systems. A short calculation shows that even a perfect model could not score F1 above about 0.4 on this label set, so the reported 0.04 to 0.10 is partly a scoring artefact and not proof the maps are useless. A better model treats the problem as a survey-bias problem. It models the chance a system would have been found (surface leakage plus exploration effort), uses temperature measurements as continuous and depth-censored labels instead of yes/no flags, validates with spatial blocks and a time-split back-test on blind systems only, and reports its uncertainty per cell. The quickest lift is not a new network. It is thousands of new, cheap, located temperature labels in unlabeled cells. Our sensors are built to make exactly those labels, so the sensor program and the model are one product.

## Findings

### F1. Adding data sets made the USGS model worse ("Cursed?", Mordensky et al. 2023)
Mordensky, Burns, Lipor and DeAngelo, "Cursed? Why One Does Not Simply Add New Data Sets to Supervised Geothermal Machine Learning Models", GRC Transactions 47, 1288-1313 (2023). https://par.nsf.gov/servlets/purl/10536404
- Setup: 278 positive cells, no labeled negatives, 709,800 cells in all, about 2,600 unlabeled cells per positive. Logistic regression and XGBoost. 120 random 80/20 splits. No spatial blocking is described.
- They added two new strain-rate layers (shear and dilation, Zeng 2022) to the five 2008 features. The 7-feature model did not beat the original 5. A 5-feature set that swapped stress and seismic density for strain did slightly better (XGBoost median normal-score at known positives 1.74 against 1.57). Only one comparison came close to significance (p = 0.06).
- Median F1 was below 0.04 for every model. In one example, XGBoost marked only about 2 of about 55 test positives as positive.
- The authors' own reasons: too few labels for more dimensions ("curse of dimensionality"); new layers correlated with old ones (|r| at least 0.29); broad, slowly varying layers cannot resolve small, discrete systems; heat flow is an interpolated surface with sampling bias; binary labels treat all systems as equal and bias the model toward easily found ones.
- What this means for us: a new regional layer only helps if it carries information at the 1 to 5 km scale of an upflow. A new smooth layer is close to worthless. A new point label is worth much more.

### F2. Expert-chosen negatives bias the map (Caraccioli et al. 2023, confirmed)
USGS abstract page: https://pubs.usgs.gov/publication/70251035 ; full PDF https://par.nsf.gov/servlets/purl/10536402
- Using NVML's 62 expert-chosen negatives, F1 looked best. Using random negatives at the natural rarity of systems, XGBoost put known positives higher and beat the NVML neural network.
- The authors say F1 was a less reliable guide than the probabilities at known positives, and that expert negatives "probably introduced bias".
- Lesson: negatives chosen by people are chosen because they are easy to call cold. A model then learns "easy cold" against "obvious hot", which is not the boundary that matters for blind systems.

### F3. The Bayesian neural network paper reports no hard accuracy number
Brown, Rodi, Gu, Fehler, Faulds, Smith and Treitel, "Bayesian Neural Networks for Geothermal Resource Assessment: Prediction with Uncertainty", arXiv 2209.15543 (submitted to Geophysics, 2022). https://arxiv.org/pdf/2209.15543
- Data: 10 feature maps on a 250 m grid, Nevada. The paper gives two different label counts: 83 positives and 62 negatives in one section, and 62 positives and 84 negatives in another. Each label was copied to its 4 neighbouring pixels, giving 620 examples. Split 67/33 at random.
- Ordinary neural networks gave very different maps across 10 runs with the same settings. The BNN was stable and gave a full probability distribution per pixel, sometimes skewed or with two peaks. The authors propose a map of the 5th percentile ("95% of models give at least this").
- No final accuracy or AUC is stated in the text. Data uncertainty was not modelled.
- Leakage risk: copying each label to its neighbours and then splitting at random puts near-copies of the same site in both train and test. Any test accuracy from that design is inflated. The paper does not discuss this.
- Lesson: the BNN's real value is a stable per-cell uncertainty. That is the quantity we need to choose where to put sensors (see Implications). Its accuracy claim is not usable.

### F4. GeoThermalCloud / NMFk: useful for finding hidden structure, never scored
- Ahmmed, Vesselinov and others, Stanford Geothermal Workshop 2023: NMFk (non-negative matrix factorisation with k-means) on 10 data sets. Great Basin: 18 water-chemistry attributes at 14,342 sites. Tularosa Basin: 21 play fairway attributes at 120 sites. SW New Mexico: 18 attributes at 44 sites. Tohatchi Springs: 19 attributes at 43 sites. It finds low, medium and high temperature "signatures" and the attributes that drive them. **No quantitative validation.** https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2023/Ahmmed1.pdf ; USGS record https://pubs.usgs.gov/publication/70237376 ; Energies 2023 Tularosa paper https://www.doi.org/10.3390/en16073098 (fetch blocked).
- Vesselinov and Kliphuis (EnviTrace), "Machine Learning Estimates of Geothermal and Critical Mineral Prospectivity of the Great Basin", Stanford Geothermal Workshop 2026, SGP-TR-230. https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Vesselinov.pdf
  - 126 attributes, including USGS GeoDAWN airborne geophysics (about 149,030 line-km over 51,857 km²), INGENIOUS, and spring and groundwater chemistry (Li, B, Mg, Na, Ca, SiO2, SO4). Many chemistry values are missing.
  - They say they tried GNN, SVM, XGBoost and diffusion models but show only NMFk. No accuracy, precision or recall is reported. Comparison is by eye. Uncertainty is "future work".
  - Honest finding: high-prospectivity cells often do not match measured groundwater temperature. The authors blame advective cooling, structural sealing and sampling bias. That is the masking problem again (see M02).
- Lesson: unsupervised factorisation is a good way to build compact features from messy chemistry, and GeoDAWN is a new high-resolution layer worth using. But nobody has yet shown it finds systems better than XGBoost.

### F5. Graph models: promising in mining, unproven in geothermal
- Sihombing, Palin, Hughes and Robb (Oxford), graph neural network prospectivity for Cu, Fe and Sn in southern England. Each point learns from its spatial neighbours. They report that graph models "significantly improve" three metrics over tabular ML and recommend more barren points than mineralised ones. Numbers not on the summary page. https://www.earth.ox.ac.uk/node/4208591 ; https://ora.ox.ac.uk/objects/uuid:cd710a18-9b40-4231-b193-4e6366dcc156
- Aljubran and Horne (2024) is a physics-informed graph network for temperature (MAE 4.8 °C over the US; see L03). It is a regression model of temperature, not a favorability classifier.
- No geothermal favorability paper reports a GNN score (EnviTrace 2026 tried one and did not report it).
- Why it could matter: hydrothermal systems sit on fault networks. A graph whose nodes are fault segments and intersections, with edges along faults and across step-overs, matches the physics better than a square grid. That is a model idea, not yet evidence.

### F6. Very high accuracy claims usually come from leakage
- Example: a 2026 ISPRS paper on Akita and Iwate, Japan, reports 94.1% accuracy for random forest and 96.7% for a GAN on 152 geothermal well sites. Its seven inputs include hot springs, fumaroles, mud volcanoes and surface alteration. Validation scheme is not stated. https://isprs-archives.copernicus.org/articles/XLIX-B2-2026/699/2026/
- When the inputs include surface manifestations, the model is told the answer for every non-blind system. Such a model cannot, by construction, find a blind system. Scores above 0.9 in this literature should be read as this kind of leakage or as a random split, until shown otherwise.
- The same goes for Zanskar's open GeoCore test set, which is INGENIOUS hot springs (M13 F2).

### F7. Spatial cross-validation: random splits overstate skill, often by a lot
- Ploton et al. (2020), Nature Communications 11:4540, "Spatial validation reveals poor predictive performance of large-scale ecological mapping models". For an African forest biomass map, random cross-validation suggested good skill, but spatial cross-validation showed the model had almost no skill far from training plots (exact R² values not re-checked because the fetch was blocked; my memory is roughly 0.5 under random splits against near zero under spatial splits, unverified). https://pmc.ncbi.nlm.nih.gov/articles/PMC7486894
- Roberts et al. (2017), Ecography 40:913-929, "Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure". The standard reference for block cross-validation: blocks should be larger than the range of spatial autocorrelation. https://doi.org/10.1111/ecog.02881 (from memory, not fetched)
- Airola et al. (2019), spatial leave-pair-out cross-validation for reliable AUC of spatial classifiers (Data Mining and Knowledge Discovery). It is built for rare positive classes like ours. https://www.utupub.fi/handle/11111/31115 (page blocked; details from memory, unverified)
- Meyer and Pebesma (2021), Methods in Ecology and Evolution, "Predicting into unknown space? Estimating the area of applicability of spatial prediction models". They define an "area of applicability" (AOA): cells whose feature values are too unlike the training data should be masked, because errors there are unknown. Free R package CAST. https://arxiv.org/abs/2005.07939
- In geothermal: Mordensky 2023 ("Cursed?") and Caraccioli 2023 used random splits. GeoCore uses 8-fold spatial block CV (M13). The USGS 2025 map uses 1,200 Monte Carlo realisations (L03). I found no geothermal paper that reports the same model under both random and spatial CV, so the size of the gap in our field is unknown. Since the input layers are smooth over tens of km, the gap is probably large.
- Within 2 to 3 km of a known system the features are nearly the same, so a random split mainly rewards the model for remembering neighbours. Blocks need to be bigger than the smoothing length of the coarsest layer (heat flow, tens of km).

### F8. Positive-unlabeled learning: geothermal breaks the standard assumption
- Standard PU learning (Elkan and Noto 2008, KDD; Bekker and Davis 2020 survey, Machine Learning 109:719-760) assumes labeled positives are "selected completely at random" (SCAR) from all positives. Then a constant label frequency c corrects the scores. (From memory; https://doi.org/10.1145/1401890.1401920 ; https://doi.org/10.1007/s10994-020-05877-5)
- In geothermal the label is NOT random. About 70% of known western US systems at 90 °C or more (258 of 370) were found because of surface features (Zanskar, M13 F1). Most of the rest were found by accident, through water wells and mines, which cluster near towns, ranches and roads. So the chance that a real system is labeled depends on features we also feed the model: shallow water table, permeable outflow paths, nearby wells. This is "selected at random given features" (SAR). Bekker, Robberechts and Davis (2019, ECML-PKDD, "Beyond the selected completely at random assumption") give a method that learns the labeling propensity e(x) jointly with the classifier (from memory, unverified).
- Practical result: a model trained naively learns "hot AND leaky AND looked-at". A blind system is "hot AND not leaky", so the model scores it down. That is the opposite of what a blind-system hunter wants. The USGS 2025 map scoring 5 of 9 hidden systems in the top 1% shows this bias is not fatal. Nine is a small test set, though, and "hidden" there includes systems found by drilling near known ones.
- Mineral prospectivity has the same problem and is ahead on fixing it. Example: De La Rosa and others (Beak Consultants, IAMG 2026) use a self-organising map to remove "prospective-looking" cells before sampling negatives, with 1,823 MVT positives across the US and Canada. They report it beats random negative sampling (no numbers in the abstract). https://beak.de/wp-content/uploads/2026/07/DeLaRosa_IAMG2026.pdf

### F9. An arithmetic ceiling on F1 explains the "below 0.10" result
My calculation, using numbers from F1 and from Caraccioli 2023:
- 278 known positive cells. Caraccioli assume about 1 in 4 systems is already found, so about 1,100 true positive cells exist.
- A perfect model flags all 1,100. On the known labels only 278 count as correct, so the measured precision is at most 278/1,100 = 0.25 and recall is 1.0. F1 = 2 × 0.25 × 1 / 1.25 = **0.40**.
- If 9 of 10 systems are still undiscovered (closer to Zanskar's "10 times underestimated" view), the ceiling falls to about **0.18**.
- So F1 of 0.04 to 0.10 means the models get about a quarter to a half of the way to the best possible score. That fits the area-capture results (85% of plants in the top 10% of area). F1 should not be used to judge these maps. The right scores are area-capture curves and, with care, PU-corrected AUC.

### F10. Why the models plateau: seven reasons, ranked
1. **Too few labels for the number of inputs.** 278 positives (western US) or about 83 (Nevada NVML). The effective number is even smaller, because positives cluster and nearby cells are not independent.
2. **Labels are chosen by surface leakage and by where people looked** (F8). Unlabeled cells are not "cold". Most have never been measured. Less than 10% of the western US has any subsurface temperature data (Zanskar, M13 F1).
3. **Inputs are too smooth.** Heat flow, strain rate and stress vary over tens of km. Upflows are 1 to 5 km wide (Mordensky GRC 2023, L03 1.7). The model cannot see better than its coarsest important layer.
4. **New layers are redundant** (F1). Most new public layers are other views of the same regional extension pattern, which is why adding them stalls.
5. **Binary labels throw away information.** A 40 °C spring and a 200 °C field count the same. A cold hole to 50 m and a cold hole to 1,000 m count the same. The USGS moved to ordinal and continuous labels (heat-flow residuals, 3,869 wells) and got better results (L03 1.7, 1.12).
6. **Wrong scoring and leaky validation** (F6, F7, F9) make it hard to tell real gains from noise. Fields often tune toward the wrong metric.
7. **No permeability or hydrology term.** Every model maps "structure that could be permeable". None maps whether a cool aquifer hides the heat. Argenta Rise was the top INGENIOUS target and came up cold to 244 m (M02).

## Datasets

| Dataset | Access | Coverage | Value for blind detection |
|---|---|---|---|
| USGS western US favorability features and labels (Mordensky et al. 2023), DOI 10.5066/P9V1Q9XM | Free, ScienceBase | 11 western states, about 710k cells, 278 positives | The standard benchmark. Use it to reproduce the plateau and show our lift on the same split |
| USGS Great Basin favorability, 1,200 realisations (Mordensky et al. 2025), DOI 10.5066/P14EET2C | Free, ScienceBase | Great Basin | P05 to P95 maps give a public uncertainty prior per cell. Use it as a prior or a baseline |
| USGS 2026 electric-grade systems list (DeAngelo, Burns and Mordensky, SGW 2026) https://pubs.usgs.gov/publication/70273870 | Free | Great Basin, 205 systems | Ordinal labels: 28 producing, 78 known, 99 probable |
| NVML / Nevada PFA ML (GDR 1351) https://gdr.openei.org/submissions/1351 | Free | Nevada, 250 m grid | 83 positives and 62 expert negatives. Code and BNN rasters. Good for checking negative-selection bias |
| INGENIOUS Great Basin compilation (GDR 1391) https://gdr.openei.org/submissions/1391 | Free | Great Basin | 3,869 heat-flow residuals as continuous labels. The base for GeoCore |
| GeoThermalCloud / NMFk data (GDR 1344, unverified title) https://gdr.openei.org/submissions/1344 | Free | Great Basin water chemistry (14,342 sites), New Mexico | Chemistry features and latent signatures |
| USGS GeoDAWN airborne magnetics and radiometrics (as used by Vesselinov 2026) | Free, USGS | About 52,000 km², Walker Lane and western Nevada | One of the few new high-resolution layers. It works at the scale of upflows, unlike strain and heat flow |
| Hawaii PFA (GDR 544) https://gdr.openei.org/submissions/544 | Free | Hawaii | Bayesian heat, fluid and permeability probabilities. Lānaʻi 1 km slimhole as a fresh test (Lautze 2025, https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Lautze.pdf) |
| Zanskar GeoCore code (LightGBM on an H3 grid) | Open source, GitHub (see Z03) | Great Basin | Competitor baseline with spatial CV ready to run |
| CAST R package (area of applicability) | Free, CRAN | Any | Masks cells where the model is extrapolating |

## What dominates uncertainty

1. **The labeling propensity.** How likely a system is to be labeled given its features: leakage to the surface, plus how hard people have looked nearby. Without it, "no label" and "cold" are mixed up, and blind systems get scored down by design.
2. **The undiscovered fraction (the class prior).** Whether 1 in 4 or 1 in 10 systems is known changes the F1 ceiling (0.40 against 0.18) and the expected number of blind systems per map cell, by about 2.5 times. Zanskar's 1 per 550 holes is a floor (M13).
3. **Resolution between features and upflows.** The coarsest important layer sets how sharply the map can point. Today that is about tens of km, against 1 to 5 km targets.
4. **Depth censoring.** A cold reading at 2 m or 150 m does not rule out a reservoir at 800 m below a cool aquifer. Treating shallow cold holes as hard negatives teaches the model wrong things. Treating them as nothing throws away data.
5. **Validation optimism.** Without spatial blocks and a time-split test, nobody, including us and Zanskar, knows the true out-of-area skill.

## What a sensor could fill

- **New labels in unlabeled cells.** Each ranch water-well temperature profile, 2 m probe line or gradient hole turns an unlabeled cell into a measured one. The label is continuous (temperature or gradient at a known depth), not yes/no. This attacks reasons 1, 2 and 5 at once. Zanskar holds about 27,000 such samples. The public set has 3,869 heat-flow residuals.
- **Depth-tagged negatives.** A sensor that logs the full temperature curve down a well, not just the bottom value, tells you whether the curve bends (outflow or a cool aquifer above heat) or is straight (truly conductive). That separates "cold, and no system" from "masked". This is the masking term that INGENIOUS lacks.
- **A propensity signal.** Water chemistry (silica, Na-K-Ca, B, Li geothermometers) from the same well visit measures how much deep fluid mixes into shallow water, which is a direct measure of leakage. That feeds the labeling-propensity model.
- **Resolution at the 1 to 5 km scale.** E-field MT nodes and dense 2 m probe grids measure at the upflow scale. They fill reason 3 locally, where the regional map has already pointed.
- **Placement by value of information.** With a Bayesian or ensemble model, every candidate sensor site has a computable expected reduction in uncertainty. Put sensors where (a) the posterior is wide, (b) the cell is outside the area of applicability, and (c) we can get the heat right cheaply (private ranch land, state land). That turns a sensor fleet into an active-learning loop.

## Implications for a better model

1. **Change the target from "is it a system?" to "what is the temperature at depth z, and how sure are we?"** Use a censored regression (Tobit style): known temperatures where measured, "at most T down to depth d" for cold holes, "at least T" for systems known only from springs. Then compute favorability as P(T > 150 °C at 1.5 km) from the predicted distribution. This uses every reading and keeps cold shallow holes from becoming false hard negatives.
2. **Model the labeling propensity explicitly.** Fit a second model e(x) for "would this system have been found?", using spring and leakage proxies, distance to roads and towns, water-well density, mining claims and historic drilling density. Train the two jointly (SAR PU learning). Then a blind-system score is "high heat AND low propensity", which is a ranked list of places where the heat would not have shown itself. That is our product.
3. **Score honestly.** Spatial block CV with blocks larger than the smoothing length of the coarsest layer. A time-split back-test: train on systems known before 2000, test on blind systems found after (Big Blind, Pumpernickel, Gabbs Valley, the USGS "probable" list). Report area-capture curves for blind systems only, and the PU-corrected AUC. Never put surface manifestations in the inputs of a blind-system model. Publish the F1 ceiling next to any F1.
4. **Keep XGBoost or LightGBM as the main learner, but add uncertainty.** Use deep ensembles or a BNN layer for a per-cell posterior, plus area-of-applicability masking. The algorithm is not the bottleneck (F1, F3), but the posterior is what drives sensor placement.
5. **Add a fault-graph model as a second view.** Nodes are fault segments, tips, step-overs and intersections. Edges follow faults. Attributes come from slip and dilation tendency, GeoDAWN magnetics and chemistry. Test whether it beats the grid model under the same spatial CV. If it does not, drop it.
6. **Add features at the 1 to 5 km scale, not more regional layers.** GeoDAWN airborne data, NMFk signatures of water chemistry, digitised water-well logs and BHTs. Each new layer must pass a "Cursed?" test: does it improve the spatial-CV score, or just add dimensions?
7. **Close the loop with our sensors.** Every sensor reading is a new censored label. Retrain weekly. Place the next sensors by expected information gain, weighted by how cheaply we can lock the heat right there. Over time the label set, not the algorithm, becomes the moat, as it already is for Zanskar (27,000 samples).
8. **Scale check (standing rules).** This is not too small. The USGS lists 205 electric-grade systems in the Great Basin alone, about 30 GWe of undiscovered blind resource is the USGS 2008 central figure, and the same method carries to other basins. The model gains here are plausible but not yet tested. Under the standing rules, that does not kill the plan. The back-test in point 3 is how we prove it.

## Sources
- https://par.nsf.gov/servlets/purl/10536404 (Mordensky et al. 2023, "Cursed?", GRC 47)
- https://pubs.usgs.gov/publication/70251035 and https://par.nsf.gov/servlets/purl/10536402 (Caraccioli et al. 2023)
- https://arxiv.org/pdf/2209.15543 (Brown et al. 2022, Bayesian neural networks)
- https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2023/Ahmmed1.pdf (GeoThermalCloud, SGW 2023)
- https://pubs.usgs.gov/publication/70237376 (NMFk hidden geothermal signatures)
- https://www.doi.org/10.3390/en16073098 (Tularosa NMFk, Energies 2023; fetch blocked)
- https://arxiv.org/pdf/2210.08685 (GeoThermalCloud 2022)
- https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Vesselinov.pdf (EnviTrace, SGW 2026)
- https://www.earth.ox.ac.uk/node/4208591 and https://ora.ox.ac.uk/objects/uuid:cd710a18-9b40-4231-b193-4e6366dcc156 (graph neural network prospectivity, Oxford)
- https://isprs-archives.copernicus.org/articles/XLIX-B2-2026/699/2026/ (Japan RF and GAN, leakage example)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7486894 (Ploton et al. 2020; fetch blocked)
- https://doi.org/10.1111/ecog.02881 (Roberts et al. 2017; from memory)
- https://www.utupub.fi/handle/11111/31115 (spatial leave-pair-out CV; page blocked)
- https://arxiv.org/abs/2005.07939 (Meyer and Pebesma 2021, area of applicability)
- https://doi.org/10.1145/1401890.1401920 (Elkan and Noto 2008; from memory)
- https://doi.org/10.1007/s10994-020-05877-5 (Bekker and Davis 2020 PU survey; from memory)
- https://beak.de/wp-content/uploads/2026/07/DeLaRosa_IAMG2026.pdf (SOM-filtered negatives for MVT prospectivity)
- https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Lautze.pdf (Hawaii PFA final)
- https://gdr.openei.org/submissions/1351 ; https://gdr.openei.org/submissions/1391 ; https://gdr.openei.org/submissions/1344 ; https://gdr.openei.org/submissions/544
