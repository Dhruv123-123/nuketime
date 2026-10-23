# M03: DOE Play Fairway Analysis results as a scorecard. What was drilled, what hit, how deep, and which weighting worked

Date: 23 Oct 2026. This file builds on `../../evidence/L01-play-fairway.md`, which already covers programme history, per-project narratives, the 2019 Nevada lease sale and the BLM reprice. That material is not repeated here. This file treats the eight-plus PFA projects as a **labelled experiment**: what the maps predicted, what the holes found, which weighting schemes were used, and what that means for building a better blind-resource model and sensor. Web budget used: 9 searches, 9 fetches. The NREL best-practices PDF (NREL/TP-5700-86139) loaded in full this time, so its Table 5 (methods) and Table 7 (drilling) are quoted directly.

## Bottom line

DOE's PFA programme (2014-2021, 11 to 6 to 5 teams, 96 follow-up areas named in Phase 1) drilled only **about 17 holes at 7 sites**. The holes were shallow: 10 GeoProbe holes under 50 m, 12 gradient holes of 150-250 m in Nevada, and single holes of 318-1,057 m elsewhere. Read as a test of the maps, the result is strong for *anomaly detection* and weak for *commercial confirmation*. **Every one of the five high-favourability sites drilled to depth gave an anomalous gradient** (Gabbs Valley 190-400 °C/km, Granite Springs over 220 °C/km, Camas Prairie ~70, Mt Baker ~64, Lana'i 42 °C/km). The one low-favourability control hole (St Helens MSH17-24) came back at background (~15 °C/km), just as the map predicted. But only **1 of 5 reached power-grade temperature in the hole** (Gabbs, 124.9 °C at 152 m), 2 of 5 exceeded 90 °C, and **0 of 5 were proven commercial**. NREL counts "4 of 7 plays" as anomalous. The Basin and Range blind targets hit best. Arc and ocean-island targets gave heat that was real but too deep or too cool. On method, **only two of six teams used data-driven weights**: Nevada (weights of evidence plus logistic regression, blended with expert fuzzy logic) and Tularosa (stochastic weights of evidence). Everyone else used expert opinion, sometimes with the Analytic Hierarchy Process (AHP). No team reported a quantitative hit-rate test of its map before drilling. In Phase 1, 9 of 11 teams graded permeability as their weakest evidence. Hawaii learned that cold groundwater does not mean no heat, because rainfall masks it. Granite Springs showed that a hot gradient does not tell you where the upflow is. The practical lesson is that the public maps are good at finding *where to put a cheap thermometer*, and that the missing piece is a cheap, dense way to go from "anomalous gradient" to "upflow location and temperature at 0.5-1.5 km". That gap is our model's target variable and our sensor's job. Granite Springs is being deepened to about 500 m under INGENIOUS in 2026, so a real outcome label is arriving soon.

## Findings

### F1. Programme funnel (numbers)
- Phase 1: 11 teams, **96 areas identified for follow-up**. Areas: Aleutians and Cascades, Appalachian Basin, Cascades (Oregon), Eastern Great Basin (Utah), Hawaii, Modoc Plateau, Nevada Great Basin, Rio Grande rift (LANL "hydrogeologic windows"), Snake River Plain, Tularosa Basin, Washington.
- Phase 2: 6 teams (Eastern Great Basin, Hawaii, Nevada, Snake River Plain, Tularosa, Washington).
- Phase 3: 5 teams (Tularosa dropped).
- About 435,000 mi² of geologic data were compiled, with over 100 publications.
- Source: Pauling et al. 2023, *Geothermal Play Fairway Analysis Best Practices*, NREL/TP-5700-86139, https://www.nrel.gov/docs/fy23osti/86139.pdf

### F2. Phase 3 drilling scorecard (NREL Table 7, plus final reports)

| Project / site | Blind at the drill site? | Holes | Max depth | Gradient / temperature | Map favourability | Outcome |
|---|---|---|---|---|---|---|
| Nevada: SE Gabbs Valley | Yes (no surface features, no prior exploration) | 6 | 152 m | 190-400 °C/km (one outlier at 57); **124.9 °C at 152 m** | High | Hit. P50 16 MWe (P90 6, P10 38). Peak captured, extent not closed |
| Nevada: N Granite Springs Valley | Yes | 6 TG + 10 GeoProbe (<50 m) | 150-250 m | >220 °C/km; ~96 °C at ~240-250 m | High | Hit on heat. **Upflow location not constrained.** Being deepened in 2026 (F7) |
| Snake River Plain: Camas-1 | Partly (warm springs in the valley) | 1 | 533-618 m | ~70 °C/km; 66.7-80 °C; ~120 °C geothermometer | High | Hit on permeability and seal. Too cool for power, so direct use |
| Washington: MB76-31 (Mt Baker) | Yes at the site | 1 | 448 m | ~64 °C/km; 141-159 mW/m² | High | Anomalous heat flow (about 2x regional) |
| Washington: MSH17-24 (St Helens) | Control | 1 | 318 m | ~15 °C/km | Low | Background, **as predicted** |
| Washington: MSH77-2 | n/a | 1 | 15.7 m | n/a | n/a | Abandoned on day 8 |
| Hawaii: Lana'i Well 10 deepening | Yes | 1 | 1,057 m | 42 °C/km; 61-66 °C at ~0.9-1 km | High | About 2x Hawaii background. Sub-commercial at this depth |
| Utah: N Cove Fort | Yes | 0 | (planned 600-900 m) | n/a | High | **Cancelled.** The USGS drilling programme declined because of expected heat and H2S |

Sources: NREL/TP-5700-86139 Table 7; Faulds et al. 2021, OSTI 1724080, https://www.osti.gov/servlets/purl/1724080 ; Steely et al. 2021, OSTI 1823116, https://www.osti.gov/biblio/1823116 ; Lachmar et al. 2023, https://geothermal-energy-journal.springeropen.com/articles/10.1186/s40517-023-00264-4 ; GDR 1411, https://gdr.openei.org/submissions/1411 ; Wannamaker et al. 2020, OSTI 1695591, https://www.osti.gov/biblio/1695591

**Hit-rate arithmetic. These are our own counts from the table, so treat them as our reading.**
- Anomalous gradient: **5 of 5** high-favourability holes drilled to TD.
- Background where the map said low: **1 of 1** control hole.
- Power-grade (over ~120 °C) measured in the hole: **1 of 5**.
- Over 90 °C: **2 of 5**.
- Commercial confirmation: **0 of 5** as of 2026.
- NREL's official count is "anomalous at 4 of 7 plays". The difference comes from counting the abandoned hole and the control hole.
- Depth of hits: Basin and Range hits came at **150-250 m**. Arc and island anomalies needed **450-1,057 m** to show and were still under 70 °C. A hit at 150 m in Nevada is worth far more than a hit at 1 km in Hawaii.

### F3. Weighting methods by team (NREL Table 5)

| Project | How layers were combined | How weights were set | How confidence was handled |
|---|---|---|---|
| Eastern Great Basin (UT) | Weighted sum | Expert + AHP | Probability kriging |
| Hawaii | Logistic "voter-veto" (generalised linear model) | Expert elicitation | Data quality and number of data types |
| Nevada Great Basin | Weighted sum | **Expert-guided fuzzy logic + Bayesian weights of evidence + logistic regression** | Error analysis of inputs |
| Snake River Plain | Weighted sum (CRS) | Expert | Fuzzy logic |
| Washington | Weighted sum (CRS) | Expert + AHP | Expert input confidence |
| Tularosa | Deterministic overlay + **stochastic weights of evidence** | Weights of evidence | Probability kriging |

- NREL's recommendation: use weights of evidence "when enough training data exists". Otherwise use expert opinion with AHP, and model confidence separately (stochastic kriging). Cross-validate across areas to avoid overfitting. **No team used ML in the PFA phases**; ML appears only as a recommended next step. Source: NREL/TP-5700-86139.
- **Nevada:** the published expert weights "took into account the statistical analyses" (weights of evidence and logistic regression). The paper does not print a numeric expert-versus-statistical comparison. The 34 benchmark systems (≥130 °C) averaged a fairway score of **51.4** on a scale that runs from about 28 to 65, so known systems sit well inside the top of the range but not at the ceiling. Source: Faulds et al. 2017, Stanford Geothermal Workshop, https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2017/Faulds.pdf
- **Tularosa, a direct test of expert versus weights of evidence:** deterministic logic found **8 plays** and weights of evidence found **10**. Six overlapped (12 in total), and 4 were rated medium-to-high. So the two schemes agree about 50-75% of the time. Source: NREL/TP-5700-86139.
- **Washington CRS weights** (heat / permeability / fluid-filled fractures) were close to equal: Mt Baker 0.32/0.34/0.33, St Helens N 0.24/0.35/0.41, Wind River 0.49/0.39/0.12. Equal-ish expert weights carry almost no information about which layer matters. Source: NREL/TP-5700-86139.
- **Hawaii, the most explicit Bayesian structure.** It used separate logistic models for heat, permeability and fluid, then multiplied them ("veto"), so P(resource) = PrH x PrP x PrF.
  - Expert priors were **PrH 0.06, PrP 0.14, PrF 0.78**, on a 200 m grid.
  - The largest weights went to seismicity and ground deformation for permeability (w = 2.1 each) and MT resistivity for fluid (|w| = 2.3). For heat, groundwater temperature had the largest weight (1.7), but its quality factor was only 0.25.
  - **No formal sensitivity test or blind validation was run.** The only checks were relative ones against Puna (PGV, PrR about 0.4) and the Humu'ula Saddle well (140 °C at 1.7 km, ~165 °C/km in the bottom 700 m).
  - Source: Ito et al. 2017, *Geothermics* 70, https://www.soest.hawaii.edu/GG/FACULTY/ITO/Ito_etal_PlayFairway_II_Geotherm17.pdf
- **LANL Rio Grande rift ("hydrogeologic windows", Phase 1 only).** Each layer was scored 0-1 by how strongly it is associated with known sites, then summed into an index from 0 to 6. Known hot springs and wells averaged **3.6**.
  - The strongest single signal was chemistry: **median boron about 0.5 mg/L at thermal sites against about 0.05 mg/L across about 4,000 wells**, a 10x contrast.
  - The models also say fault-controlled windows can give up to about 85 °C above 200 m.
  - Source: LANL HGW Phase 1 report, https://gdr.openei.org/files/611/HGW_PhaseI_Report.pdf
- **Oregon Cascades (Phase 1 only, OSU, EE0006727).** It kriged heat flow (80 mW/m² threshold) and fault density into CRS layers. It did not advance. Source: GDR 646, https://gdr.openei.org/submissions/646

### F4. Which evidence mattered, and which failed
- **Permeability was the weak leg everywhere.** In the Phase 1 GeoRePORT grading, 9 of 11 projects gave permeability consistently low grades. Source: Garchar et al. 2016, SGW, https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2016/Garchar.pdf
- **Masking by shallow water is the main false-negative mechanism.** Hawaii's 2025 revision says Phase 1 resource probabilities (under 10% across most of the state) were "too conservative". The team now *removes* groundwater data from the heat model, because rainfall swamps the thermal signal, and it reports heat probability rather than combined resource probability. Washington's "rain curtain" caused the same problem. INGENIOUS's Argenta (see M02) failed shallow for a similar reason. Source: Lautze 2025, SGW, https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Lautze.pdf
- **In the Basin and Range, the evidence that collocated at the hit (Gabbs)** was:
  - a displacement-transfer zone with fault intersections and Quaternary faults;
  - gravity gradients and a magnetic low;
  - a 2 m temperature anomaly of about 5 °C above background;
  - a low-resistivity zone;
  - chalcedony geothermometry above 110 °C from 32 °C irrigation wells.

  The 2 m probe anomaly and the warm-well chemistry are the cheap, direct heat signals. The rest is permeability context. Source: Faulds et al. 2017 SGW; Faulds et al. 2018 GRC, https://pubs.usgs.gov/publication/70201803
- **Phase 2 data barely moved the grades** in Nevada and Utah ("very little advancement in drilling grade"). More data of the *same* kind (gravity, mapping) did not change the forecasts. Drilling did. Source: NREL/TP-5700-86139.
- **Data coverage was thin.** Only about 20% of Nevada had detailed geological mapping, and lidar was scarce. Source: NREL/TP-5700-86139.

### F5. The ML successor results
- **Smith et al. (2023) re-ran the Nevada PFA with Bayesian neural networks.** They used **83 positive sites (≥39 °C) and 62 negative sites**, mostly deep, cool oil and gas wells, with about 10 feature layers on a 250 m grid. They found model variability on this small dataset and used Bayesian neural networks to put uncertainty on the predictions. Sources: https://arxiv.org/abs/2209.15543 ; https://pubs.usgs.gov/publication/70241433
- **The USGS 2025 favourability map** (Mordensky et al.) puts **54% of producing systems in the top 1% of the map area**. Earlier maps put about half in the top 20%. See L01 and M02.

### F6. Value of the PFA holes as labels
- About 17 PFA holes, plus the INGENIOUS gradient holes (Argenta has 10 to about 244 m), are public, logged, and sit at map-selected sites. They are the rare labelled examples where the map was asked a question and the earth answered. They include the hits, the background control, and the shallow masked cases. Data are on the GDR PFA portal: https://gdr.openei.org/pfa (Nevada reports GDR 756, https://gdr.openei.org/submissions/756 ; retrospective GeoRePORTs GDR 1276, https://gdr.openei.org/submissions/1276).

### F7. New outcome arriving: Granite Springs deepening (2026)
- Nevada Division of Minerals permit 1744 (approved 21 May 2026) covers TG well **68-02 (H2)**. The operator is NBMG/UNR, the drilling engineer is RESPEC, and the driller is Welsco. The planned depth is **about 1,650 ft (about 503 m)**, with an open uncemented liner for repeat temperature logs. Location: SW¼ SE¼ Sec 2, T27N R27E, Pershing County. Funding: INGENIOUS DE-EE0009254. This is the first deeper test of a PFA blind discovery, and it is roughly twice the depth of the 2018-19 holes. Source: https://prod.minerals.nv.gov/siteassets/content/programs/geo/geopermits/geo-1744-5-21-2026-nbmg-pershing-granite-springs-68-02.pdf
- Result not yet public (unverified). We should watch the GDR for logs. It is a free label, and it is also a signal about whether nearby private and fee heat rights are worth locking now.

## Datasets

| Dataset | Access | Coverage | Value for blind detection |
|---|---|---|---|
| GDR PFA portal (all phases, all teams) | Free, https://gdr.openei.org/pfa | NV, UT, ID, WA, OR, HI, NM, Modoc, Appalachia | Expert CRS layers plus confidence maps. These are the "public prior" to beat |
| Nevada PFA reports and appendices (GDR 756) and regional data (OEDI 6866) | Free | 96,000 km² of NV | Nine-parameter stack, 34 benchmarks, Gabbs and Granite Springs TG logs |
| PFA Retrospective GeoRePORTs (GDR 1276) | Free | All Phase 2-3 sites | Graded heat, permeability and fluid at each site. A structured label set |
| Washington PFA Phases 1-3 (GDR 1333) | Free | Mt Baker, St Helens, Wind River | A rare *negative control* hole (MSH17-24) |
| Camas-1 well data (USU, GDR 1316) | Free | Camas Prairie, ID | Permeability and seal validation, temperature profile to 618 m |
| Lana'i Well 10 core and logs (GDR 1411) | Free | Lana'i | 1 km gradient. Calibrates the masking depth in wet volcanic terrain |
| LANL Hydrogeologic Windows (GDR 611) | Free | SW New Mexico | Boron, Li and silica chemistry for about 4,000 wells. A 10x B contrast |
| Smith et al. BNN training set (83 positive, 62 negative) | Paper and supplement | NV | A negative-label template drawn from cool oil and gas wells |
| NV Division of Minerals geothermal permits | Free PDFs | NV | **Leading indicator** of who is drilling where (e.g. permit 1744) |

## What dominates uncertainty about blind resources (from this slice)
1. **Depth of masking.** Shallow cold water hides upflow. In wet arcs and islands the heat appeared only at 450-1,057 m, and even there it was under 70 °C. In dry Basin and Range it appeared by 150 m. The masking depth is set by local hydrology, and no public layer captures it.
2. **Upflow location inside an anomaly.** Granite Springs had over 220 °C/km gradients, but the upflow "was not well constrained". The public maps find the right 10 km² cell. They do not find the right 0.5 km² inside it, which is where a production well must go.
3. **Permeability at reservoir depth.** It was the weakest leg in 9 of 11 Phase 1 projects, and Phase 2 surface data did not improve it.
4. **Label scarcity and bias.** About 17 holes, positives defined at different temperature thresholds (39 °C versus 130 °C), and almost no negatives except oil and gas wells. The expert weights were never back-tested.
5. **Shallow-to-deep extrapolation.** None of the five anomalous sites has a deep test. Every MWe figure (e.g. Gabbs P50 16 MWe) is extrapolated from 150 m.

## What a sensor could fill
- **Dense, cheap temperature at 2 m plus 30-50 m GeoProbe depth across a whole anomaly.** This turns "hot gradient somewhere" into "upflow is here". Granite Springs already used 10 GeoProbe holes. Push-probe thermistor strings (or DTS fibre in a push rod) costing a few hundred dollars per point could map the outflow plume and trace it back up-gradient.
- **Water-well chemistry probes plus bottle kits (B, Li, SiO2, Cl/Mg, conductivity, temperature log) on ranch and irrigation wells.** At Gabbs, 32 °C irrigation wells gave a chalcedony geothermometer above 110 °C, and in New Mexico boron showed a 10x contrast. This is the single strongest "see-through-the-cold-aquifer" signal. It extends our prior ranch-well drop probe: add a field boron/silica test and log the full temperature profile, not just bottom-hole temperature.
- **Repeat temperature logging in existing open holes** (PFA TG holes, the INGENIOUS 68-02 liner, abandoned water wells). A cheap wireline or DTS logger gives equilibrated profiles. Isothermal or convex segments diagnose convection and lateral outflow.
- **E-field-only MT or AMT nodes over 0.5-2 km.** These image the clay cap and conductor beneath a masked aquifer. Hawaii gave MT the largest fluid weight (|w| = 2.3), and the Gabbs hit sat on a low-resistivity zone.
- **Passive seismic or ground-deformation nodes** for the permeability leg (Hawaii gave them w = 2.1). This matters most in areas without lidar or detailed mapping.

## Implications for a better model
1. **Predict a continuous, depth-indexed temperature, not a binary "system yes/no".** The PFA outcomes are gradients and temperatures at 150-1,057 m. Train on T(z) and gradient, using PFA, INGENIOUS and oil and gas wells, so that cool holes become informative partial labels instead of being thrown away.
2. **Keep Hawaii's heat x permeability x fluid "veto" structure, but learn the weights.** Use explicit expert priors (PrH ~0.06, PrP ~0.14) as Bayesian priors, then update them with weights of evidence or gradient-boosting likelihoods where labels exist. This is what NREL recommends, and almost no team actually did it.
3. **Add a hydrology/masking term.** Inputs: recharge or precipitation, water-table depth, aquifer flow direction. Then down-weight "no shallow heat" evidence wherever masking is likely. This lesson came from Hawaii, Washington and Argenta.
4. **Treat surface-data favourability as a regional prior and chemistry plus cheap thermometry as the local likelihood.** Phase 2 surface data barely moved the grades. Holes, 2 m probes and well chemistry did. That is where our own data, gathered on the same ranch visit as signing the heat option, beat Zanskar's public-layer model.
5. **Back-test the expert maps on the PFA holes.** Test the Washington control, all five anomalous sites, and Granite Springs 68-02 when it reports. This gives us a calibration curve between expert favourability and measured gradient that nobody has published.
6. **Prioritise Basin and Range blind targets for buying rights.** There, a 150 m hole (about $100-300k) or a probe array resolves the question. Arc and island plays need 1 km or more to answer, which is too expensive per option for a rights bank.
7. **Use state drilling permits as a live competitive and label feed.** Permit 1744 shows the public programme is still drilling PFA discoveries. Its results will reprice nearby private and fee land, so lock options near Granite Springs before the log is released.
