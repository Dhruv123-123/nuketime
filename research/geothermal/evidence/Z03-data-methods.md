# Z03: Zanskar, data and methods

*Research note, 2026-10-21.*

*Method: the shared WebSearch budget for this workflow (200 calls) ran out before this agent's first query, so I could not run open searches. Everything below comes from direct WebFetch of primary sources: Zanskar's site and Substack, the GitHub organisation, the OSTI API and records, the GDR, and press coverage (MIT Technology Review, TechCrunch, Heatmap, Latitude Media). The Stanford geothermal server (pangea.stanford.edu) returned HTTP 503 every time. Google Patents, Justia and FreePatentsOnline returned 403 or rendered empty, so the patent search is incomplete, not negative. Where a GeoCore paper detail comes only from the sibling file L03, it is labelled that way. Anything without a source is marked (unverified).*

---

## 1. What Zanskar says it uses (datasets)

Zanskar's public disclosures name the categories of data but list almost no specific datasets.

| Data class | What Zanskar or press says | Source |
|---|---|---|
| Legacy analog archives | The founders "acquired long-forgotten analog subsurface data sets and digitized them for their AI model," covering regions never developed. | Heatmap, Sep 2025 |
| Old oil, gas and federal exploration wells | At Pumpernickel, oil and gas companies and the federal government drilled exploratory wells intermittently from the 1970s, but none reached commercial temperatures. Zanskar's models still indicated hot reservoirs, and the models set surface location, drilling angle and direction. | Heatmap |
| Known geothermal systems as labels | Regional AI models are trained on known hot spots and on simulations the team generates. TechCrunch: past *accidental* discoveries are the training labels for supervised ML. | MIT TR, Dec 2025; TechCrunch, Jan 2026 |
| Geology, faults, satellite and remote sensing | "Geological data, satellite data," fault-line information, and "newer satellite and remote sensing databases." | MIT TR; Heatmap |
| Heat flow | Big Blind was flagged in late 2023 as an "above background heat flow" anomaly. | Zanskar Substack (Big Blind proof-up) |
| Proprietary field data | An in-house data-collection team was launched about 3 years before Sep 2025. Field crews drilled shallow temperature holes over about **100 sq mi** at Big Blind. Zanskar also collected "several high-resolution geo datasets" after winning the lease. | Heatmap; MIT TR; Zanskar Substack |
| Seismology | A DOE Cyclotron Road CRADA with LBNL used large-n arrays of low-cost seismometers, micro-earthquake tomography and ambient fracture-seismic emissions to map faults and fluid flow. The results "guided well siting" and served as priors for reservoir models. | OSTI 3015294 (Jan 2026) |
| MT, gravity, passive seismic | Co-author Ian Warren (Zanskar) worked on passive-seismic-emission tomography with cooperative MT and gravity inversion for 3D permeability at San Emidio and Crescent Valley, NV (with Ormat and LBNL). | OSTI 1986084 |
| Wellbore and seismic fracture data | A DOE SBIR Phase II (contract SC0022427) produced a "Workflow for 1D & 2D Fracture Prediction from Wellbore & Seismic Data" using ML. The full text is **embargoed until 11 Feb 2042**. | OSTI 2339574 (Mar 2023) |
| Production data | Lightning Dock plant SCADA. One year of well 44-7 data is published. | Zanskar Substack (Jul 2026) |

What Zanskar does **not** disclose: bottom-hole temperature (BHT) correction methods, geochemistry or geothermometers, mining assessment files, and any named commercial or state data purchases. In the posts I retrieved, the words "BHT" and "geochemistry" never appear. **Inference (unverified):** the Pumpernickel story shows they use legacy O&G and federal wells, but the archive-recovery layer is not something they publicise.

## 2. Published methods and papers by Zanskar staff

### 2.1 GeoCore: open-source geospatial ML framework
- **Paper:** Grujic, O., Hossler, T., Lipscomb, J., Morrison, R.A., Smith, C.M. (2025), "An efficient and scalable framework to optimize geospatial machine learning," 50th Stanford Geothermal Workshop, SGP-TR-229 (cited in the repo README). I could not fetch the PDF (503).
  - Per the sibling file L03 (not re-verified here): about **4 million H3 grid cells run on an M1-Max laptop**, and **no prospect-level performance metrics**.
- **Code:** github.com/zanskar-geothermal/GeoCore, Python, under Apache-2.0 (the README says MIT, which conflicts), last updated May 2025.
- **Stack:** features, labels and predictions live in **Snowflake** on an **H3 hex grid**. Experiments are YAML-configured and tracked in **MLflow**. Built with Poetry and Docker.
- **Example experiment** (`lightgbm_gbdt_model_ingenious.yaml`), which shows the *public* feature set Zanskar demonstrates on:
  - **Features:** Ingenious geodetic layers, CBA gravity HGM, earthquake density, MT conductance layers, RTP magnetic HGM, distance to Quaternary volcanics, fault layers.
  - **Labels:** INGENIOUS well temperatures, with positive and negative well-depth thresholds of 10 and 150.
  - **Held-out test set:** INGENIOUS hot springs.
  - **Model:** LightGBM binary GBDT with 30-iteration hyperparameter search scored on ROC-AUC.
  - **Cross-validation:** **spatial block CV** (4x2 blocks, 8 folds, buffer 10, clustering distance 50).
- **Takeaway:** the open model is a standard gradient-boosted favourability classifier on the public INGENIOUS Great Basin stack, which is also offered as a Snowflake Marketplace dataset. **The algorithm is not the moat.** The proprietary edge must sit in data, labels, simulations and field acquisition.

### 2.2 Bayesian evidential learning and stochastic reservoir modelling
- TechCrunch reports Zanskar uses **"Bayesian evidential learning" (BEL)** for development planning: existing data become priors, models test hypotheses, and the output is probabilities. An in-house **geothermal simulator fills in missing data**.
  - BEL is the Stanford (Caers group) decision-focused framework. The link to Zanskar staff training is (unverified).
- Hoiland (Heatmap): the models "create a probability distribution that allows you to make decisions with more confidence." The MIT TR article quotes him as saying neural nets can learn "if there's something learnable in the earth."
- **Big Blind** (Substack): stochastic models explore a wide range of conceptual models consistent with the data. End-member models targeted the *exploration* wells. Regional models and "full-physics simulations" suggest more than 10x more generation at depth.
- **Lightning Dock** (Substack): 6 months of reservoir modelling after the June 2024 acquisition, combining modern geophysical imaging with stochastic modelling of "thousands of plausible subsurface realizations." The hypothesis was that fractures stay open with depth.
  - Result: well 44-7 drilled to about 8,000 ft (3-4x the legacy wells), producing **>4,000 GPM** at a **PI of about 50 GPM/psi**, with inlet temperature about 60 °F higher than the legacy wells.
  - **No measurable thermal decline over 12 months**; about **75,000 MWh** delivered, over 44,000 MWh more than the legacy wells would have produced.
- In short: supervised ML for regional screening, then Bayesian/stochastic physics-based modelling for targeting and value of information. This is a decision-analytic stack, not a single model. Whitney Trainor-Guitton, a value-of-information specialist now at NREL/NLR, co-taught Zanskar's 2022 GRC workshop.

### 2.3 Other staff outputs
- **GRC 2022 student workshop repo** (Connor M. Smith with W. Trainor-Guitton): introductory Python, geospatial modelling and kriging notebooks.
- **Staff come from the UNR/USGS Nevada ML pipeline:** Connor Smith, earlier listed as Connor Macrossie-Smith, was first author of the Smith et al. 2023 Nevada ML paper, per L03. Ian Warren came from NREL (San Emidio geomechanics and microseismicity: JGR 2023, OSTI 2205394; Geothermics 2023, OSTI 1960949).
- **Peer-reviewed performance disclosure: none found.** Zanskar's validation is drilling it reports itself, described as "three of three" by Edwards in TechCrunch.

### 2.4 Patents
- I could not run a patent search (403 or blank responses from Google Patents, Justia and FreePatentsOnline).
- No Zanskar patent is cited in any company post retrieved. Status: **unknown (unverified)**.
- Given the open-sourced GeoCore code and the "AI-native platform" framing, the IP strategy appears to be trade-secret data plus speed, not patents (inference).

## 3. Outcomes linked to the methods (company-reported)

- **Big Blind, western NV:** no surface manifestation and no prior wells.
  - Sequence: heat-flow anomaly in late 2023, then **BLM lease won at auction**, then high-resolution data collection, then 2 intermediate wells in Jul-Aug 2025.
  - Result: TD 2,668.5 ft, max equilibrated temperature about 250 °F, total lost circulation, and a gradient of about **100 °C/km** in the overlying 300 ft.
  - Discovery cost claim: **< $15k/MW**, against more than $100k/MW for early-1980s explorers.
- **Pumpernickel, northern NV:** an overlooked site with old O&G and federal wells. A 20 MW plant is targeted for 2028 (Heatmap).
- **Portfolio:**
  - More than 700 MW of sites under full or partial control (CFO, Latitude Media).
  - Six 20 MW plants planned, sized for small-generator interconnection.
  - A 100 MW NV Energy PPA.
  - $180M total equity, including a $115M Series C in Jan 2026, plus $40M of development capital scaling to $100M.
  - The CC Power GEODE agreement extends prospecting to CAISO.
  - Two DOE awards (Sep 2026, in negotiation): a horizontal stimulated injector at Lightning Dock, and deep directional confirmation drilling in NV with near-real-time model updating.
- Zanskar says test wells have been drilled in only about **5%** of prospective western US area (Heatmap). TechCrunch: about 95% of systems are blind, and Hoiland claims about 1 TW of potential against the DOE's 60 GW by 2050.

## 4. Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **The ML layer is commoditised. Zanskar open-sourced its own.** GeoCore runs LightGBM on public INGENIOUS layers with spatial CV. A newcomer starts at Zanskar's *public* baseline on day one. Differentiation therefore has to come from what Zanskar does not open-source: **data and rights**. This matches the Terranox thesis exactly.

2. **Zanskar's data emphasis points to the gap.** Its public story is heat flow, satellite, geophysics, seismology, physics simulation and its own field crews (new data acquisition, which is capital-intensive). It does not publicise a systematic **text and scan recovery** of illegible public archives:
   - state O&G well files and BHT headers;
   - mining assessment and drill-log filings (the Nevada NBMG files, claim-holder holes);
   - USGS and state temperature-gradient-hole open files;
   - BLM well files.

   Archive recovery is the Saskatchewan Mineral Assessment Database playbook. It is also the feature and label bottleneck the literature names: each digitised BHT is both a new feature and a new label. Whether Zanskar already does this internally is (unverified). Heatmap says they digitised "analog data sets," so assume partial overlap and compete on breadth and speed.

3. **Business-model gap.** Zanskar turns every discovery into a developer and IPP project: it bought Lightning Dock, holds a PPA, plans 20 MW plants and project-finances them. Its capital and attention concentrate on a handful of sites, about 10 to confirm next. Edwards: "We have dozens of sites that look just like this." That implies more prospects than one developer can build. The Terranox shape is a **land bank and prospect-generator** (the EMX/Franco-Nevada model):
   - rank hundreds of cells;
   - take BLM, state and private rights cheaply;
   - de-risk to a "TG-confirmed anomaly" or "slimhole-confirmed" state;
   - sell, JV or royalty the proven state to Ormat, Fervo, Cyrq, utilities, data-centre offtakers, or Zanskar itself.

4. **Geography and resource-type gap.** Zanskar's published work and discoveries are Great Basin and Rio Grande-rift hydrothermal. Sedimentary basins with dense legacy O&G BHTs, where the Terranox archive skill transfers most directly, are not in its public footprint:
   - the Williston, including Saskatchewan's own well archive;
   - the Uinta, Permian, DJ and Gulf Coast;
   - the Alberta and BC foothills.

   Their EGS and sedimentary-geothermal value is rising with Fervo-style development and data-centre demand.

5. **Validation is equal-footing.** Zanskar has no peer-reviewed prospective performance numbers. Its validation is 3/3 company-reported. Under the standing rules, untested ML lift does not kill a Terranox shape either. The credibility plan is a published held-out back-test plus a cheap TG-hole program on owned leases. Big Blind shows the step-up happens at about 800 m (2,700 ft) confirmation wells, so budget for slimholes on the best few.

6. **Watch-outs.**
   - Zanskar has the capital ($180M equity) and the people to copy an archive-recovery wedge.
   - BLM auctions are visible, so a pre-proof edge on federal land depends on knowing which parcels to nominate before others do.
   - Exclusive data deals (mining claim holders, O&G operators) and private and state rights are the more defensible channels.

## Sources
- https://www.zanskar.com/ ; https://www.zanskar.com/about/
- https://github.com/zanskar-geothermal ; https://github.com/zanskar-geothermal/GeoCore ; https://raw.githubusercontent.com/zanskar-geothermal/GeoCore/main/experiment_configs/lightgbm_gbdt_model_ingenious.yaml ; https://github.com/zanskar-geothermal/GRC_2022_Workshop_Zanskar
- https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Grujic.pdf (GeoCore paper, fetch failed with 503; cited via the repo README and L03)
- https://zanskargeothermal.substack.com/p/zanskar-proves-first-blind-geothermal
- https://zanskargeothermal.substack.com/p/zanskar-reveals-big-blind-the-discovery
- https://zanskargeothermal.substack.com/p/using-custom-built-artificial-intelligence
- https://zanskargeothermal.substack.com/p/one-year-at-lightning-dock
- https://zanskargeothermal.substack.com/p/zanskar-raises-115m-series-c-following
- https://zanskargeothermal.substack.com/p/zanskar-and-cc-power-sign-geode-agreement
- https://zanskargeothermal.substack.com/p/zanskar-selected-for-two-us-department
- https://www.osti.gov/biblio/3015294 (LBNL-Zanskar CRADA, seismology)
- https://www.osti.gov/biblio/2339574 (Zanskar SBIR fracture-prediction workflow, embargoed to 2042)
- https://www.osti.gov/biblio/1986084 (PST/MT permeability mapping, Warren)
- https://www.osti.gov/biblio/2205394 ; https://www.osti.gov/biblio/1960949 (Warren, San Emidio)
- https://gdr.openei.org/submissions/1391 (INGENIOUS Great Basin compilation)
- https://www.heatmap.news/climate-tech/ai-geothermal-discovery
- https://www.technologyreview.com/2025/12/04/1128763/ai-geothermal-zanskar
- https://techcrunch.com/2026/01/21/zanskar-thinks-1-tw-of-geothermal-power-is-being-overlooked/
- https://www.latitudemedia.com/news/armed-with-115-million-geothermal-startup-zanskar-gets-ready-to-build/
