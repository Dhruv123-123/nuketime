# M13: Zanskar's methods in depth, and where its model is weakest

Date: 23 Oct 2026. Slice M13, model track. This file builds on `../../evidence/Z03-data-methods.md` (GeoCore config, BEL mention, Lightning Dock and Big Blind numbers), `Z06-weak.md` (business and geography gaps), `Z10-zanskar-people.md` (people and hiring), `L03-ml-geothermal.md` and `M02`, `M05`, `M06`. It does not repeat them. What is new here: (1) the full numbers in Zanskar's 2025 Stanford "discoveries" paper, which is the base-rate engine behind every Zanskar claim; (2) a 2026 Stanford paper by Hoiland and co-authors on neural-operator surrogates, which is the missing piece of their Bayesian decision stack; (3) the founders' own admissions on the Volts podcast; (4) a staff-skills map; (5) a ranked list of where their model is weakest. Web budget used: 9 searches and 7 fetches. Two Stanford PDFs (Grujic 2025 on one mirror, Liang 2026 on one mirror) were blocked once, but the Liang PDF loaded from the second mirror. GitHub API access to the GeoCore repo was blocked in this session, so the repo facts come from Z03. The patent search found nothing (see F6).

## Bottom line

Zanskar runs a three-layer stack. Layer 1 is a regional favorability classifier (GeoCore: LightGBM on an H3 grid, spatial block CV), trained on known systems and cold wells. Layer 2 is a base-rate model built from its own compilation of 370 known systems and about 27,000 temperature samples. It says historic exploration found one blind system per ~550 holes (0.181%), and that two-thirds of unprotected Quaternary faults have no temperature data within 1 km. Layer 3 is a site-scale Bayesian loop: thousands of stochastic reservoir realizations, now being made cheap with neural-operator surrogates that run up to 10,000 times faster than full physics, scored against new wells for calibration. Their real moat is not the algorithm. It is the private label set (27,000 samples, more than 5 million acres tested, internal gradient holes) and the field crew that turns model output into holes within weeks. Their model is weakest in five places: (a) its labels are biased toward the places people already drilled, and its open test set is hot springs, which are exactly the visible systems; (b) it has no explicit "how hard have we looked here" term, so "no data" and "cold" are easy to confuse; (c) it predicts temperature far better than permeability, and the founders say so; (d) its "how much" number is a flat 30 MWe per discovery times a hit rate, with no size distribution or credible interval; (e) it ignores geochemistry, hydrologic masking and private ranch land. A better model for a heat-rights bank uses Zanskar's own published base rates as priors, adds an observation-effort term and a size distribution, and spends our sensors on the data-poor fault cells Zanskar itself says are the opportunity, but on private and state land it does not touch.

## Findings

### F1. Zanskar's base-rate paper: the numbers behind every claim
Edwards, Hoiland, Smith, Dereuil, Grujic, Lipscomb and Morrison, "A Look Into Geothermal Discoveries Across the Western United States", Stanford Geothermal Workshop 2025, SGP-TR-229. https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Edwards.pdf ; abstract page https://pangea.stanford.edu/ERE/db/IGAstandard/record_detail.php?id=38000
- **Inventory.** 370 unique sites at 90 °C or hotter across 11 western states: 258 active (surface features) and 112 blind or hidden. "Blind or hidden" means no active surface feature and more than 2.5 km from one. Zanskar's own discoveries are left out of the public map.
- **How systems were found.** Accidents (mainly water wells and mining) found about half of all utility-scale resources and most blind or hidden ones. Water wells alone found more than a third of the blind or hidden set. Water-well discoveries slowed to a trickle after homesteading ended in 1976.
- **How little has been looked at.** Less than 10% of the western US has any subsurface temperature data. About 90% of sampled H3 cells (resolution 8, about 0.7 km²) have only wells shallower than 20 m. Early-stage geothermal drilling covers about 0.4% of the area. About two-thirds of unprotected Quaternary faults have no temperature data within 1 km.
- **Land filter.** About 25% of the West is PAD-US status 1 or 2 protected. About 25% of high-potential sites are off-limits, and two-thirds of identified sites are either off-limits or already producing.
- **Base rate.** 49 blind systems from about 27,000 drill samples gives **0.181% per sample, or about 1 in 550 holes**.
- **Cost math.** About $1,000 per sample (mix of shallow gradient holes and 2 m probes). $100M buys 100,000 holes. At the historic rate that gives more than 100 discoveries (the paper gives 100, 175 and 181 in different places, not reconciled). At about 30 MWe per site, that is about 3 GWe in 10 years at under $600k per site, or under $20k per MWe.
- **Prior estimate it leans on.** About 30 GWe of undiscovered blind or hidden resource (USGS Williams et al. 2008), about three times the identified systems.
- **No Bayesian method is in this paper.** The projection is rate times holes times MWe per site.
- **Read-through.** The Big Blind post claims under $15k/MW (Z03). The paper says under $20k/MWe. Both rest on the flat 30 MWe per site. Zanskar's own team also says the 49 blind systems differ from the 112 blind or hidden total, and that confidential industry discoveries are missing, so the base rate is a floor.

### F2. The open model (GeoCore) is a favorability classifier with a visible-system test set
From Z03 (repo config `lightgbm_gbdt_model_ingenious.yaml`) and the 2025 Stanford paper by Grujic, Hossler, Lipscomb, Morrison and Smith (https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2025/Grujic.pdf; full text not re-read here).
- Features: INGENIOUS geodetic strain, gravity and magnetic gradients, earthquake density, MT conductance, distance to Quaternary volcanics, faults.
- Labels: INGENIOUS well temperatures thresholded to positive and negative classes by depth. The held-out test set is **INGENIOUS hot springs**.
- LightGBM, 30-iteration hyperparameter search on ROC-AUC, spatial block CV (8 folds).
- **Weakness I see.** Scoring on hot springs tests whether the model finds the systems you can already see from the road. It does not test the blind case, which is the whole business. No paper reports performance on blind systems only. This is my reading of the config, not a claim Zanskar makes.

### F3. The Bayesian layer: stochastic realizations, now with fast surrogates
- **Volts podcast (2025, Hoiland and Edwards).** Their models predict temperature and permeability versus depth as probability ranges. They track whether each new well fell inside the predicted range and how close it came to the median. Edwards says early models were "frankly much worse than expert explorers" and that they have beaten experts only "in the last year or two". He also says "we've missed way more than we've hit", that the hit rate is streaky, and "sometimes your models get worse". Hoiland says apparent setbacks often reflect better-calibrated uncertainty. They have tested more than 5 million acres in five years. Data release is limited by leasing rules. https://www.volts.wtf/p/is-there-way-more-conventional-geothermal
- **Surrogates (2026).** Liang, Yu, Thibaut, Zheng, Hoiland and Pollack, "Surrogate Modeling for Geothermal Systems: Accelerating Optimization, History Matching, and Uncertainty Quantification", Stanford Geothermal Workshop 2026. Contact email is at zanskar.us. They trained U-Net, FNO, U-FNO and Fourier-MIONet on 1,200 stochastic simulations (four fault scenarios times 300) of an anonymized fault-controlled field. Each full-physics run took 30 to 120 minutes. Output is a 64×64×64 temperature field at up to 8 time steps. FNO error was below 0.025 within a scenario and about 0.07 on unseen fault scenarios. Speedups reach about 10,000 times. **No uncertainty quantification or history matching was actually run in the paper.** The authors say the surrogates "could enable" full Bayesian inference. https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Liang.pdf ; https://pangea.stanford.edu/ERE/db/IGAstandard/record_detail.php?id=38332
- **Who brings BEL.** Robin Thibaut, a co-author, is a computational geoscientist from the Ghent University Bayesian Evidential Learning group (Hermans), the European branch of the Stanford Caers school (profile: https://app.icebreaker.xyz/profiles/linkedin-robin-thibaut-3aa49712b). His Zanskar affiliation is inferred from co-authorship and the zanskar.us email (unverified). BEL learns a direct statistical map from data to forecast across many prior realizations, skipping full inversion. That is what TechCrunch called Zanskar's "Bayesian evidential learning" (Z03). Example of the method: https://meetingorganizer.copernicus.org/EGU24/EGU24-10336.html (not Zanskar).
- **Read-through.** The decision engine is: fault-scenario priors, thousands of realizations, a fast surrogate, then posterior on temperature and flow at a candidate well, updated from each new well. It is site-scale and drilling-focused. The regional "where to look" step is still the GeoCore-style classifier plus base rates.

### F4. Staff skills map (what they are good at)
- Carl Hoiland, CEO: Stanford PhD in geological sciences, NSF fellow, then an Activate (Cyclotron Road) fellow at LBNL. https://climate.uchicago.edu/?p=9907 . The LBNL link explains the large-N seismology CRADA (Z03, OSTI 3015294).
- Joel Edwards, CTO: geologist (Heatmap, in Z10). Further education and prior employers not found in this pass (unverified).
- Aubry Dereuil, Head of Geoscience since Jan 2024, structural geologist since May 2022; rock mechanics and petroleum seal and trap background, Chevron listed (unverified). https://app.icebreaker.xyz/profiles/linkedin-aubry-dereuil-34a382249
- Ognjen Grujic and Thomas Hossler (GeoCore authors): both from Stanford's earth-data-science circle, Grujic with prior oil and gas ML work (from memory, unverified).
- Connor Smith: first author of the 2023 Nevada ML paper (L03). Ian Warren: NREL geomechanics and passive seismic (Z03).
- Ahinoam Pollack (2026 co-author): Stanford geothermal reservoir and uncertainty modeling (affiliation now unverified).
- **Gap in the map.** I found no named geochemist, hydrogeologist, landman or MT specialist in public author lists. Combined with Z03 ("geochemistry" never appears in their posts), this supports the view that chemistry and groundwater are not first-class inputs.

### F5. What they say they use, and what they appear to ignore
| Uses (stated) | Source | Appears to ignore or under-weight | Basis |
|---|---|---|---|
| Legacy 1970s–80s O&G and federal wells, DOE 2008 and 2012 campaigns | Volts | Geochemistry and geothermometers | Never in posts (Z03); no geochemist on papers |
| Water, mineral wells; USGS, university, lab studies | Volts; Edwards 2025 | Hydrologic masking and outflow (cold-water caps) | No term in GeoCore or base-rate paper |
| Satellite and remote sensing | MIT TR, Heatmap | Search-effort or "how well we looked" layer | Paper counts coverage but model does not use it as a feature (unverified) |
| ~27,000 temperature samples, internal TG holes | Edwards 2025 | Size distribution of systems | Flat 30 MWe per site |
| Large-N seismology, passive seismic, MT/gravity inversions | OSTI 3015294; Fishlake NF permit | Private and state land | Only BLM leases disclosed (Z04, Z06) |
| Fault-scenario stochastic models and neural surrogates | Liang 2026; Lightning Dock post | Sedimentary basins, O&G BHT archives at scale | No public activity (Z06) |

### F6. Patents
A search for Zanskar as assignee returned only company profile pages and no patent records (search run 23 Oct 2026). Earlier passes could not reach Google Patents (Z03). Status: no patent found, not proven absent. With GeoCore open-sourced and the SBIR fracture-prediction report embargoed until 2042 (OSTI 2339574), the strategy looks like trade secrets plus speed.

### F7. Where Zanskar's model is weakest (ranked)
1. **Permeability.** Hoiland: temperature is only "in some cases" a leading indicator of permeability. Edwards: "We have a gap in our conceptual understanding of where these systems form", and there is "very few data" on deep fluid circulation (Volts). The surrogate paper models four fault scenarios at one site. The model is a temperature predictor that hopes for flow.
2. **Biased labels and a visible-system test.** Positives come from places people drilled or saw springs. 90% of sampled cells only have wells under 20 m. Negatives from shallow cold wells are not true negatives. Testing on hot springs (F2) cannot show blind-system skill. This is a positive-unlabeled learning problem they do not frame as one in public.
3. **No observation-effort term.** Their own paper maps coverage, but the classifier treats an unsampled cell and a sampled cold cell alike unless the feature stack separates them (unverified). That is exactly where blind systems hide (M05).
4. **The "how much" number has no spread.** 30 GWe (USGS 2008) and 3 GWe per decade at 30 MWe per site are point values. No size distribution, no credible interval, unreconciled discovery counts (100, 175, 181).
5. **Calibration is self-reported and young.** "Better than experts only in the last year or two", "missed way more than we've hit", 3 of 3 named sites. No published reliability diagram or prospective test.
6. **Footprint.** BLM Nevada and New Mexico. Private, state and sedimentary land is unmodeled by them in public.

## Datasets

| Name | Access | Coverage | Value for blind detection |
|---|---|---|---|
| Zanskar 370-site inventory and ~27,000 samples (Edwards 2025) | Private; only summary stats public | 11 western states | The best label set in the West. Its published base rate (1 in 550 holes) and coverage stats are free priors for us |
| INGENIOUS Great Basin compilation (GDR 1391) | Free, CC-BY | Great Basin | GeoCore's public feature and label stack; the shared baseline |
| USGS Quaternary Fault and Fold Database | Free | US | Zanskar's "unsampled fault" target layer; we can rebuild the two-thirds-unsampled map ourselves |
| PAD-US protected areas | Free | US | Removes ~25% of land; also flags where private inholdings sit next to faults |
| H3 grid, resolution 8 | Open software | Global | Zanskar's cell unit (~0.7 km²); use the same to compare directly |
| GeoCore code (github.com/zanskar-geothermal/GeoCore) | Open source | n/a | Reproduce their public baseline on day one |
| Liang et al. 2026 surrogate setup | Paper only | One anonymized site | Recipe for our own fast site-scale Bayesian loop |
| USGS Williams et al. 2008 assessment | Free | Western US | The 30 GWe undiscovered prior Zanskar uses |

## What dominates uncertainty (per this slice)

1. **Permeability at 0.5 to 3 km.** Zanskar's founders name it as their conceptual gap. Heat without flow is a dry hole.
2. **The true base rate in unsampled fault cells.** The 0.181% is from historic, partly untargeted holes and is a floor. Whether targeted holes reach 1%, 2% or 5% sets the whole economics.
3. **System size.** A flat 30 MWe hides a long-tailed distribution. The total hidden resource is a sum over that tail.
4. **Negative-label quality.** Shallow cold wells under rain curtains look like "no system" when they mean "not looked deep enough".
5. **How much private industry data exists.** Confidential discoveries are missing from every public count, including Zanskar's.

## What a sensor could fill

- **Temperature below 20 m in fault cells off BLM land.** The 90%-of-cells-under-20 m gap is filled by our ranch water-well drop probe (wells often 50 to 300 m) and by logging 2 m probes. Each reading is a label in a cell Zanskar has not sampled.
- **A permeability proxy that is cheap.** E-field MT nodes for the clay cap and conductors at 0.5 to 2 km, plus short passive-seismic deployments on fault intersections. This attacks weakness 1 directly.
- **Chemistry on the same visit.** A filtered bottle and a helium sample from each ranch well. Zanskar shows no geochemistry layer.
- **Profile shape.** Repeat, equilibrated temperature logs show reversals that flag outflow and masking, turning false negatives into "masked" labels.
- **Search-effort logging.** Every probe visit logs depth and quality, so the model knows where we looked and how well.

## Implications for a better model

1. **Use Zanskar's published numbers as priors.** Start the per-cell prior from 1 in 550 holes, adjusted by fault proximity and INGENIOUS favorability. Calibrate the regional total to the 30 GWe USGS figure, but let the data move it.
2. **Frame it as positive-unlabeled learning with an observation model.** For each cell, model P(system) times P(detected | system, effort, depth, masking). Unsampled is not cold. This is the main structural upgrade over GeoCore.
3. **Test on blind systems only.** Hold out the blind and hidden systems (the 112-type set we can rebuild from public sources), not hot springs. Report hit rate per hole against the 1-in-550 baseline. That is the number buyers will ask for.
4. **Add a size distribution and sum over it.** Give each cell a lognormal MWe given a system, tied to structure type (M02 enrichment table) and temperature. The answer to "how much hidden hydrothermal" becomes a credible interval, not a point.
5. **Copy the surrogate trick for site work.** Build our own FNO surrogate over fault-scenario realizations (1,200 runs on one GPU is cheap) so we can run real Bayesian updates after every probe and every MT carpet. Zanskar's paper shows it works but did not yet run the UQ. We can.
6. **Value-of-information picks the next sensor.** Rank cells by expected drop in variance of MWe per dollar of sensor time. That points the drop probe and MT nodes to data-poor fault cells on private and state land, where Zanskar is absent and rights cost $1 to $2 an acre.
7. **Publish calibration.** A public reliability diagram and blind back-test would beat Zanskar's self-reported "3 of 3" in a buyer's data room.

## Sources
- Edwards et al. 2025 SGW: https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Edwards.pdf ; https://pangea.stanford.edu/ERE/db/IGAstandard/record_detail.php?id=38000
- SGW 2025 schedule: https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2025/Schedule_2025.html ; SGW 2026 schedule: https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2026/Schedule2026.html
- Grujic et al. 2025 (GeoCore): https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2025/Grujic.pdf (blocked this pass; via Z03 and L03)
- Liang et al. 2026: https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Liang.pdf ; https://pangea.stanford.edu/ERE/db/IGAstandard/record_detail.php?id=38332
- Volts podcast: https://www.volts.wtf/p/is-there-way-more-conventional-geothermal
- Hoiland bio: https://climate.uchicago.edu/?p=9907
- Dereuil profile: https://app.icebreaker.xyz/profiles/linkedin-aubry-dereuil-34a382249 ; Thibaut profile: https://app.icebreaker.xyz/profiles/linkedin-robin-thibaut-3aa49712b
- BEL example: https://meetingorganizer.copernicus.org/EGU24/EGU24-10336.html
- Prior repo files: Z03, Z06, Z10, L03, M02, M05, M06 (paths above)
