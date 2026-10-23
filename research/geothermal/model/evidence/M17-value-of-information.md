# M17: Value of information and sequential exploration design for blind hydrothermal

Slice M17, model track. Date: 23 Oct 2026. This builds on `M02-ingenious.md` (Granite Springs VOI pointer, Argenta Rise miss), `M04-bht-corrections.md` and `M05-heat-flow-databases.md` (rank sensing by VOI), `M08-magnetotellurics.md` (E-field carpet at $150-250 per site), `M13-zanskar-methods.md` (1 blind system per ~550 holes, Bayesian evidential learning), `M15-uq-methods.md` (occupancy-detection model, calibration limits) and the hardware cost numbers in `../../../hardware/evidence/H01`, `H03`, `H06`, `H11`. It does not repeat them. What is new: how geothermal VOI is actually computed in the published work, what numbers exist, what is missing, a worked VOI-per-dollar ranking for our own kit, and a design for a sequential (active-learning) exploration loop.

Search notes: 7 web searches and 10 fetches worked. Several papers only showed their abstracts or dataset pages, so some numbers come from figures I could not see and are marked (unverified). The VOI-per-dollar table in F7 is my own illustrative arithmetic, not a published result.

## Bottom line

Value of information (VOI) is simple in principle. It is the expected value of the best decision after you see the data, minus the expected value of the best decision now. Its two hard inputs are a **prior** (how likely a hot system is here) and a **reliability matrix** (how often the measurement says "hot" when it is hot, and "cold" when it is cold). Whitney Trainor-Guitton (LLNL, then Colorado School of Mines, now NREL) built the geothermal versions: MT at Darajat (VOI only $11k-50k per well decision, but **2-5x higher when the prior dry-hole risk is high**), spatial VOI for MT clay-cap "throats", Granite Springs gradient-hole siting by prior value and entropy, and a 2025 open-source VOI app tested on hidden-hydrothermal, EGS and district-heat cases. Caers and Athens (Stanford) gave the Bayesian evidential learning version that Zanskar now uses. Kobold Metals and Caers showed a POMDP drill planner reaching the same go/no-go accuracy with **fewer than half the holes** of grid drilling (9 vs 36 in one example). **No published geothermal study ranks data types by VOI per dollar, and no one has published the reliability matrix of 2 m probes, water-well logs, E-field MT or geochemistry against known blind systems.** That missing likelihood table is the single biggest unknown in every geothermal VOI calculation, and it is cheap for us to measure. My worked numbers (F7) say that, for a blind-system bank whose rights cost $1-2 per acre, **cheap screening sensors (ranch-well drop probe, water chemistry, robotic 2 m probes) have 10x to more than 100x VOI per dollar, an E-field MT carpet about 2-4x, and a contract gradient hole about 0.3-1x unless our own rig cuts it to under $40k.** Cheap rights also flip the classic sequence: you lock the right first (the option is nearly free) and spend VOI money only on what to *carry*. The better model is therefore a sequential Bayesian loop with a two-part acquisition score: local decision VOI on the parcel plus global information gain on the shared model (each new label calibrates every other cell). The sensor to build is the one that raises sensitivity under hydrologic masking, and the first job for it is a **reliability calibration run over known blind systems and cold controls**, which turns every VOI number from a guess into a measured fact and becomes a data-room asset nobody else holds.

## Findings

### F1. How geothermal VOI is computed (the Trainor-Guitton recipe)
- Decision analysis set-up: a set of actions a (drill / do not drill, lease / walk), uncertain states theta (e.g. steam-flow classes or temperature bins), and a value v(a, theta) for each pair. V_prior = max over a of sum over theta P(theta) v(a, theta). With data d, V_imperfect = sum over d P(d) max over a sum over theta P(theta | d) v(a, theta). VOI = V_imperfect - V_prior. Perfect information (VOI_perfect) is the ceiling. Source: LLNL DOE peer review deck, https://www.energy.gov/sites/default/files/2015/06/f23/19-Information%20Evaluation_LLNL.pdf
- The reliability (likelihood) P(d | theta) is the hard part. At Darajat it was built empirically: MT conductance voxels were paired with steam flow at feed zones within 750 m, binned, and counted. Trainor-Guitton, Caers and Mukerji (Math. Geosci. 2011, 43(8):929-949) give a general method for a data reliability measure in spatial VOI. Trainor-Guitton, Mukerji and Knight (SERRA 2013, 27(4):969-983) extend it to spatial and dynamic problems. Publication list: https://people.mines.edu/wtrainor
- Synthetic version for blind systems: Trainor-Guitton, Hoversten, Ramirez, Roberts, Juliusson, Key and Mellors (Geophysics 2014, 79(5) W27-W41, doi 10.1190/geo2013-0337.1) simulated MT over many clay-cap models and asked how often the inversion finds the **"throat"** of the cap (the upflow) that marks a hidden resource. Data and spreadsheet: https://gdr.openei.org/submissions/426 ; https://www.osti.gov/biblio/1148896
- Follow-on: "Value of MT inversions for geothermal exploration" (Trainor-Guitton, Hoversten, Nordquist, Intani, Geothermics 2017, 66:13-22) uses field data and multiple interpretations (also LLNL-PROC-668598, https://www.osti.gov/biblio/1245716).

### F2. Published VOI numbers are small per well, and depend on the prior
- Darajat (Indonesia, 271 MW, volcanic): seven steam-flow classes, worth about -$500k to +$700k per well. Results (LLNL deck): with the data-based prior, VOI of MT = **$11,030 (0.12 S/m cap) and $19,950 (0.10 S/m)** on V_prior of $151,550. With a more pessimistic "dry-hole" prior, V_prior = $0 and VOI = **$48,775 and $37,090**. So MT was worth **2.5-4.4x more when the prior was pessimistic**. That is the general rule: data are worth most when you are close to indifferent or when the prior says "do not drill" and the data can reverse it.
- Meaning for us (my analysis): blind-system cells sit at a very low prior (about 0.2% per hole, M13). That is exactly where a measurement that can flip "walk" to "carry" has high VOI, but only if it is sensitive enough to overcome the low prior. A test with poor specificity at a 1% prior mostly generates false alarms.

### F3. Granite Springs: gradient-hole siting by prior value and entropy, not full VOI
- Trainor-Guitton, Siler and Ayling (SGW 2023): 50 geostatistical realizations of temperature in a 69 x 138 x 90 cell (75 x 75 x 10 m) model, from 47 shallow TGH datasets, 6 wells under 260 m, and structural proxies from a 3D Leapfrog model. Utility: below 45 °C a loss, 45-80 °C neutral, above 80 °C rising profit.
- Results for nine candidate holes: V_prior (x10^6) ranges from **7.26 (site B) to -9.81 (site J)**. Entropy is lowest at B (2.68) and highest at A (3.80), J (3.72), I (3.66). So **the best place to drill for profit (B) and the best place to drill for learning (A, J, I) are different**. This is the exploit-versus-explore trade-off in a real Nevada dataset.
- Proxy strength: dilation tendency correlated -0.56 with measured temperature, Coulomb stress change 0.35, distance to fault 0.29, distance to fault intersections 0.21. Max measured 96 °C at 150-250 m.
- What it lacks: no costs, no reliability matrix, no VOI per dollar. https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2023/Trainorguitton.pdf ; https://www.osti.gov/biblio/2217601

### F4. 2025 open-source VOI app (NREL) and three industry cases
- "Open-Source Value of Information App: Insight From Three Geothermal Case Studies", GRC Annual Meeting Reno, Oct 2025 (NREL/NLR CP-5700-95630). Binary decision (drill / do nothing), binary outcome (positive / negative). Users enter four payoffs, vary the prior, and upload labelled data to see how well a data type separates productive from non-productive sites. Cases: **hidden hydrothermal, EGS, district heating**. Data types used: stress, temperature gradient, MT. The public abstract gives no ranking (unverified which won). https://research-hub.nrel.gov/en/publications/open-source-value-of-information-app-insight-from-three-geotherma/
- Use for us: this app's binary frame is exactly our "carry / drop the parcel" decision. Our job is to feed it measured likelihoods, which it lets users upload.

### F5. Bayesian evidential learning (Stanford, used by Zanskar)
- Athens and Caers (Applied Energy 2019, 256:113932): a Monte Carlo prior of basin-scale extensional geothermal models, then posterior temperature predictions conditioned on a temperature well **without explicit inversion**, using canonical correlation analysis between simulated data and predictions. Target temperature was most sensitive to **bulk permeability of basement and basin rock**. https://ideas.repec.org/a/eee/appene/v256y2019ics0306261919316198.html
- Why it matters: BEL makes VOI cheap. You simulate data and outcomes across the prior once, then the VOI of any proposed measurement is the expected shrinkage of the posterior on the decision variable. Zanskar's neural-operator surrogates (up to 10,000x faster, M13) make this run on thousands of prospects.

### F6. Sequential design and active learning outside geothermal show 2x savings
- Mern, Corso, Burch, House (Kobold Metals) and Caers, "Intelligent prospector v2.0" (arXiv 2410.10610, 2024): drill planning as a POMDP with a hierarchical Bayesian belief (hypothesis class plus GP grade and thickness), re-planning after each hole, with actions drill / walk away / commit. **Same go/no-go accuracy with less than half the boreholes of grid drilling; one example converged at 9 holes versus 36.** A maximum-entropy null hypothesis catches a wrong geologic prior; without it the agent walked away from a profitable prospect. https://arxiv.org/pdf/2410.10610
- GFZ (Siegel, Degen, Cacace, EGU26-11172, 2026): Bayesian optimal experimental design for placing temperature sensors, made affordable with physics-based ML surrogates (model-order reduction). https://meetingorganizer.copernicus.org/EGU26/EGU26-11172.html
- Netherlands (Niederau et al., EGC 2025): "efficacy of information" over 100 structural models picks the best 3 km borehole; the loss from misjudging drilling depth is about 7.5% of a 1.1 km well cost (€119k-161k). https://europeangeothermalcongress.eu/wp-content/uploads/2025/11/Jan-Niederau-et-al-2.pdf
- Reykjavik University (Muzi, 2023, adapting Trainor-Guitton 2014): **3D active seismic is not worth its cost for exploring large areas with one planned well**; passive seismic gets similar answers cheaper. https://en.ru.is/ise/research/research-projects/voi-geothermal-seismic-value-of-seismic-survey-in-geothermal-assessment
- NREL decision-making review (2015 peer review): VOI analysis was judged "highly subjective" because priors and likelihoods are guessed; the fix proposed was historical analogs. IRR was most sensitive to temperature gradient and reservoir temperature, least to exploration cost. https://www.energy.gov/sites/prod/files/2015/06/f23/3-Exploration%20Decision%20Making_NREL_1.pdf
- Meaning: the industry knows how to compute VOI. It has never had the likelihood tables or the cheap measurements to make it a daily tool. The cost of exploration is small next to the value of being right on temperature, so spending more on cheap information is almost always rational.

### F7. Worked VOI per dollar for our kit (my analysis, illustrative, unverified inputs)
Decision: carry a locked parcel to a confirmation hole costing C = $150k, or drop it. If the cell holds a blind system, the confirmed prospect sells for V = $3M (about $0.1M/MW x 30 MW, from hardware memo arithmetic). Prior p = 5% for a top-decile fault cell (INGENIOUS top 10% holds 85% of systems, M02; this is far above the 0.18% per random hole). With p x V = C, V_prior = 0, so any useful data has value. VOI_perfect = p(V - C) = **$142k**. For a test with sensitivity s and specificity q: VOI = p s (V - C) - (1 - p)(1 - q) C.

| Measurement | Assumed s / q (unverified) | VOI | Cost per parcel | VOI per $ |
|---|---|---|---|---|
| Water chemistry grab (Si, Na-K-Ca, Li, B) from ranch well | 0.4 / 0.9 | ~$43k | $0.3-1k | 40-140x |
| Ranch water-well drop probe (T profile + conductivity) | 0.6 / 0.85 | ~$64k | $1-3k | 20-60x |
| Robotic 2 m probe grid (50 points) | 0.5 / 0.9 | ~$57k | $1.5k (at $30/pt) - $15k (at $300/pt) | 4-38x |
| E-field MT carpet (~4 km², 250 m) | 0.7 / 0.7 | ~$57k | $15-30k | 2-4x |
| Own-rig 150 m gradient hole | 0.75 / 0.95 | ~$100k | $8-40k | 2.5-12x |
| Contract gradient hole | 0.75 / 0.95 | ~$100k | $100-300k | 0.3-1x |

Key points from the arithmetic:
- Specificity matters because a false "hot" costs the whole $150k carry. Sensitivity matters because masking (Argenta) hides the prize.
- Tests run in series multiply: two independent cheap tests at s = 0.6, q = 0.85 each give, under an "either positive then hole" rule, a combined sensitivity near 0.84 for a few thousand dollars. This is the case for a **multi-modal** probe that reads temperature, conductivity and chemistry on one visit.
- At a 0.5% prior (an average cell) every VOI falls about 10x and false positives dominate. So **VOI is only high after the regional model has concentrated the prior.** The model and the sensors are complements.
- Cheap rights flip the order. Locking a 640-acre ranch parcel at $1-2/ac costs under $1.3k, less than most measurements. So the bank should **lock first, then measure**, and use VOI to decide what to carry, not what to lease. The exception is competitive BLM auction tracts, where VOI before bidding matters (my analysis).

### F8. Two kinds of value per measurement
- Local value: the parcel decision above.
- Global value: each honest label (especially a cold one) updates the shared occupancy model (M15) and the reliability tables for every other cell. Classic VOI ignores this. Active learning captures it as expected information gain on model parameters. With only 10-20 blind discoveries since 2008 (M15), the global value of the first few hundred prospective labels is large (my analysis). Zanskar has 27,000 samples but its test set is hot springs (M13), so it has the same gap on blind-system likelihoods.

## Datasets

| Dataset | Access | Coverage | Value for blind detection |
|---|---|---|---|
| Trainor-Guitton 2014 synthetic MT posteriors + spreadsheet | GDR submission 426, public | Synthetic clay caps | Template likelihood for MT throat detection; method to copy |
| Granite Springs TGH, 2 m and 3D model data (INGENIOUS / PFA) | GDR, partly public | ~280 km² NV | A real explore/exploit test bed to benchmark our acquisition rule |
| Darajat MT-steam flow pairs | Not public (Chevron/Star Energy) | 1 volcanic field | Only empirical MT reliability matrix published; method only |
| NREL open-source VOI app | Open source (repo link unverified) | Generic | Drop-in binary VOI with uploaded labels |
| Zanskar published base rates (1/550 holes, 49 blind systems) | Papers, summary only | 11 western states | Prior for p in VOI |
| INGENIOUS favorability with 1,200 MC realizations | GDR public | Great Basin | Prior p and its spread per cell |
| Our own probe, chemistry and MT reads at known systems and cold controls | Ours (to build) | Target 20 blind + 40 cold sites | The missing reliability matrix; the input every VOI needs |

## What dominates uncertainty (in VOI terms)

1. **The reliability matrix of each cheap measurement against blind systems.** Never published for 2 m probes, ranch-well logs, E-field MT or water chemistry. A sensitivity of 0.3 versus 0.7 changes VOI by more than 2x.
2. **The local prior p.** VOI scales almost linearly with p at low priors. The occupancy model (M15) and size-biased discovery correction set it.
3. **Hydrologic masking.** It cuts the sensitivity of every shallow method (Argenta Rise: 139 probes and 10 TG wells, no anomaly). It is the main reason a shallow negative is weak evidence.
4. **Payoff V.** What a confirmed blind prospect sells for, which sets the scale of every VOI. Few public comps (B07, R04).
5. **Correlation between measurements.** If probe and chemistry fail together (same masking aquifer), stacking them adds less than the independent-test arithmetic says.

## What a sensor could fill

- **A calibration campaign, not just a sensor.** Run the full kit (drop probe, chemistry, 2 m grid, E-field carpet) across about 20 known blind or near-blind Nevada systems and about 40 cold controls from Zanskar-style cold-hole lists and published dry gradient holes. Output: measured s and q per modality, and their correlation. Cost is a few hundred thousand dollars at our unit costs. This turns VOI from opinion into data and is a saleable artifact.
- **Multi-modal ranch-well probe.** Temperature gradient plus conductivity plus an in-situ ion or sampling module (Si, Li, B, Na/K). Different physics, so partly independent errors, so combined sensitivity rises under masking.
- **Deeper-looking cheap channel.** E-field MT nodes left for days see 0.5-2 km, below the masking aquifer. Lower specificity, but a different failure mode from shallow temperature, which is exactly what stacking needs.
- **Telemetry and a tablet that runs the VOI loop in the field**, so the crew decides the next station by expected information gain the same day (re-planning, as in the POMDP).

## Implications for a better model

1. **Make it a decision model, not a map.** Output for each parcel: P(blind system), posterior MWe, V_prior of carry, and the VOI of each available measurement. Rank actions by VOI per dollar.
2. **Use a two-part acquisition score:** local decision VOI + lambda x expected information gain on global model parameters (occupancy rate, size distribution, reliability tables). Early on set lambda high to buy labels; later lower it to exploit.
3. **Learn the likelihoods as model parameters.** Put sensitivity and specificity of each modality inside the hierarchical Bayesian model (M15 occupancy-detection) with priors, and update them from the calibration campaign and every later hole.
4. **Re-plan after each measurement (POMDP / sequential Bayesian design)** with a falsification check (a max-entropy null model), following Mern et al. Expect about 2x fewer holes per decision.
5. **Use surrogates for speed.** BEL or neural-operator surrogates (M13) to compute VOI over thousands of parcels nightly.
6. **Lock first, then learn.** Because rights cost less than most measurements, VOI should gate carry spend, not lease spend, except at competitive auctions.
7. **Benchmark on Granite Springs and Argenta.** Replay history: would our acquisition rule have picked the holes that were drilled, and would it have stopped at Argenta sooner? This is a cheap, public test of the loop.
8. **Sell the VOI.** A buyer (Ormat, Fervo) pays for de-risked prospects. A data room that shows calibrated likelihoods and the VOI log behind each carry decision is more credible than a favorability score.

## Sources
- LLNL VOI deck (Darajat): https://www.energy.gov/sites/default/files/2015/06/f23/19-Information%20Evaluation_LLNL.pdf
- Trainor-Guitton et al. 2014, Geophysics: https://www.osti.gov/biblio/1148896 ; data https://gdr.openei.org/submissions/426
- Trainor-Guitton publications: https://people.mines.edu/wtrainor ; NREL profile https://nrel.gov/research/staff/whitney-trainor-guitton.html
- LLNL-PROC-668598: https://www.osti.gov/biblio/1245716
- Trainor-Guitton, Siler, Ayling 2023 (SGW): https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2023/Trainorguitton.pdf
- NREL open-source VOI app (GRC 2025): https://research-hub.nrel.gov/en/publications/open-source-value-of-information-app-insight-from-three-geotherma/
- Athens and Caers 2019: https://ideas.repec.org/a/eee/appene/v256y2019ics0306261919316198.html
- Mern et al. 2024, Intelligent Prospector v2.0: https://arxiv.org/pdf/2410.10610
- Siegel, Degen, Cacace, EGU26-11172: https://meetingorganizer.copernicus.org/EGU26/EGU26-11172.html
- Niederau et al. EGC 2025: https://europeangeothermalcongress.eu/wp-content/uploads/2025/11/Jan-Niederau-et-al-2.pdf
- Reykjavik University VoI seismic project: https://en.ru.is/ise/research/research-projects/voi-geothermal-seismic-value-of-seismic-survey-in-geothermal-assessment
- NREL exploration decision-making review: https://www.energy.gov/sites/prod/files/2015/06/f23/3-Exploration%20Decision%20Making_NREL_1.pdf
