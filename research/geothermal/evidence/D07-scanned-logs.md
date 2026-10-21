# D07: Scanned and raster well logs in North America (scale, digitisation cost, AI tools, and whether a startup can read millions cheaply)

*Method note: the shared WebSearch budget (200 calls per turn) ran out before this agent's first query, so open searches were impossible. Everything below comes from **direct WebFetch of primary pages** (TGS, MJ Logs, Neuralog, BEG, KGS, Google AI pricing docs, arXiv) and from numbers that sibling evidence files (D01, D02, L09, Z03) had already sourced; their URLs are repeated here. The academic literature on automated raster-log digitisation (2023–2026) could **not** be surveyed directly, so this file names no papers in that area rather than guessing citations. A follow-up pass with search budget should fill that gap.*

## 1. How many raster logs exist

There is no single census. The fragments below are the best sourced numbers.

| Holder | Holdings | Format / access | Source |
|---|---|---|---|
| **MJ Logs** (formerly MJ Systems, founded 1971; Englewood CO and Calgary) | **"7 million raster logs and LAS"** covering **~3 million wells**, plus **21 million LAS curves** digitised from the rasters. Microfiche at first, rasters from the 1990s, LAS from 2016 | Commercial. Free search; LAS sold "by the curve"; volume discounts; perpetual licence; "raster rental" for play evaluation. No public prices | https://www.mjlogs.com/ ; https://www.mjlogs.com/about ; https://www.mjlogs.com/pricing-orders |
| **TGS / A2D North American well log library** | Size not disclosed on the sale page. TGS sold the business to **Enverus on 8 Jul 2026 for USD 100M at close + USD 15M earn-out**. **2025 revenue USD 27M** (2.9% of TGS multi-client revenue). TGS keeps an internal-use licence | Commercial, now consolidated into Enverus | https://www.tgs.com/well-data |
| **S&P Global (ex-IHS / Petroleum Information)** | Count not retrieved (page returned 403) (unverified) | Commercial | — |
| **Texas BEG Geophysical Log Facility** | **~1.5 million logs**, **TIFF raster only; "LAS files are not currently offered"**. **$10.00 per log**, ordered by email. Some Austin and Midland holdings are not catalogued | Public institution, pay per scan | https://www.beg.utexas.edu/about/facilities/geophysical-log-facility |
| **Texas RRC** (logs from 2004 onward) | Header and log images held as TIFF; no temperature field in structured tables (D01) | Free to view; bulk at public-information pricing | D01; https://www.rrc.texas.gov/media/cx2i4xrm/wba091_well-bore-database.pdf |
| **Kansas Geological Survey** | **367,768 scanned log records across 148,969 wells** (parsed from bulk index `ks_elog_scans.zip`, D02). Only **21,780 LAS wells** (12/31/2024), with yearly archives summing to ~28,908 LAS files. A hand-keyed BHT field covers **74,299 wells / 212,089 readings** | Free bulk index; TIFF scans online; copies for purchase | https://www.kgs.ku.edu/Magellan/Elog/scan.html ; https://www.kgs.ku.edu/Magellan/Logs/index.html ; https://www.kgs.ku.edu/PRS/Scans/Log_Summary/index.html |
| **NGDS (2014)** | **~650,000 well logs, ~530,000 borehole temperature measurements, ~1.7M well headers** (O&G, water and geothermal) | Federated; now partly retired and moved to GDR/Zenodo (D04) | https://www.petroleumnews.com/story/2014/06/08/news/state-contributes-geothermal-data/26622.html |
| **Stanford InterPIGNN (2024)** | Merged **400,134 unique BHTs** from nine sources (per L09). MAE 4.8 °C | Public model | https://arxiv.org/abs/2403.09961 |

**What the numbers say together:**
- The digitisation gap is wide. Kansas, one of the best-digitised states, has ~368k scanned log records but only ~22–29k LAS files, a ratio of **about 13:1 raster to digital** (computed). Its BHTs exist in structured form only because staff keyed them by hand.
- The best national temperature compilation (~400k BHTs) is **below 10% of the US wells drilled** (US total of ~4M+ is unverified). MJ Logs alone lists 3M wells and 7M logs. A North American raster universe of **roughly 10–20 million log images** across MJ, A2D/Enverus, S&P, state surveys and regulators is a reasonable order of magnitude, with heavy overlap between holders (unverified; no holder publishes a deduplicated count).
- In over 95% of wells in national datasets there is only **one** temperature measurement (O'Malley et al. 2026, via L09: https://www.alphaxiv.org/abs/2605.16665). The extra fields that make a BHT correctable (multiple runs, time since circulation, mud type) sit on the raster header and are mostly unextracted.
- The market has put a price on a digitised legacy log library: **~$100–115M for a business earning $27M a year** (TGS→Enverus). That roughly 4x revenue multiple is a floor-value signal for a proprietary digitised corpus, though it is not the business Terranox wants.

## 2. Cost of commercial LAS digitisation

- **Public price points found:** BEG charges **$10 per raster scan**, so the whole 1.5M Texas archive costs **~$15M at list** (computed; the bulk or academic price is unverified). MJ Logs and Enverus/S&P sell LAS **per curve** with volume discounts, but publish no prices.
- **Manual and semi-automatic digitising labour:** The industry has long priced service digitising per curve, or per curve-foot, at levels typically quoted from **a few dollars to tens of dollars per curve per well** (unverified; no public rate card retrieved). Neuralog customer testimonials report **~$100,000** and **~$168,000** saved in scanning and digitising fees by bringing the work in-house (https://www.neuralog.com/). That suggests a mid-size operator spends six figures on outsourced digitisation for one programme.
- **Why LAS is costly:** curves cross grid lines, overlap other curves, include backup scales and wraps, and come from degraded film or paper. A human still QCs the result. That is why Kansas shows only ~7% LAS coverage despite decades of effort.

**Key point for geothermal: you do not need full LAS curves for most of the value.** The highest-value temperature fields are **text on the log header**: BHT or max recorded temperature, depth, time since circulation, mud type and weight, run number, date, and logging company. Reading a header is an OCR or vision-language form-extraction task, not curve tracing. Porosity (density, neutron, sonic) does need curve digitisation, but only over target intervals (for example, deepest 500–1,000 m in candidate sedimentary reservoirs), not the full log.

## 3. AI log digitisation tools, 2023–2026

- **Neuralog: NeuraLog 2026 (published 20 May 2026).** It adds **AILFE**, a neural network that separates curves, grids and background in log images and outputs LAS, plus **AI header capture**, which uses OCR to fill header fields for user verification. No quantified speed or accuracy figures are given. https://www.neuralog.com/neuralog-update-ai-well-log-digitization-software/. The core product already used "neural-network algorithms" for curve tracing, grid models for grid crossings, auto-stop error detection and auto-patching of backup scales. https://www.neuralog.com/well-log-digitizing-software-neuralog/
- **Incumbent posture:** the vendors (MJ, A2D/Enverus, S&P) sell digitised curves per curve. They have every incentive to digitise on demand and to price high, not to release bulk structured header-temperature tables.
- **Generic vision-language models:** frontier and "Flash" class multimodal models now read semi-structured forms well. A log header is a semi-standard form, so it is a tractable target (inference; header-specific benchmarks not retrieved).
- **Academic literature:** there is a body of work on deep-learning curve extraction from raster logs (segmentation and curve-tracing networks), but specific 2023–2026 papers could not be retrieved in this pass (unverified; needs a search follow-up). None is cited here to avoid inventing references.

## 4. Can a startup read millions of raster logs cheaply? (computed estimate)

**Header extraction (temperature): yes, compute cost is close to zero.**
- Gemini API pricing (fetched 2026-10-21): **Gemini 2.5 Flash-Lite batch costs $0.05 per 1M input tokens and $0.20 per 1M output**. Gemini 3.5 Flash-Lite batch costs $0.15 in and $1.25 out. https://ai.google.dev/gemini-api/docs/pricing
- Images cost **258 tokens per 768×768 tile** (rough tiling rule). https://ai.google.dev/gemini-api/docs/image-understanding
- A header crop of about 2000×2600 px is about 4 tiles, so about **1,000 image tokens + ~500 prompt tokens in, and ~300 tokens of JSON out** (computed).
  - With 2.5 Flash-Lite batch, that is **~$0.00014 per header**, or **~$1,400 per 10 million headers** (computed).
  - With 3.5 Flash-Lite batch, it is about $0.0006 per header, or **~$6,000 per 10M** (computed).
  - Even at 10x the tokens, or with a frontier model on a QC subsample, the cost is **tens of thousands of dollars for the whole continent** (computed).
- **The binding cost is access, not compute.** Possible routes:
  - **Free or near-free public archives:** KGS TIFFs, RRC images, OCC and Utah DOGM scanned well files, NDOM/NBMG in Nevada (D01–D03).
  - **Pay-per-scan archives:** BEG at $10 a scan. A targeted subset is much cheaper than the full archive: deep wells filtered by total depth from free well tables, say 100k wells, is about **$1M** (computed).
  - **Commercial licences:** MJ, Enverus, S&P. These are negotiable; a "raster rental" or a geothermal-only field-of-use licence is plausible but its price is unverified.
- **Accuracy and QC:** humans verify a stratified sample, and physics constraints (gradient plausibility, neighbour consistency, depth/TD agreement with state well tables) flag outliers. Header BHTs are noisy anyway. Schölderle et al. (2022) find input errors (shut-in time, rounding) dominate correction-method choice, so better extraction of *metadata* is itself the improvement (L09: https://www.mdpi.com/1996-1073/15/17/6367).

**Curve digitisation (porosity, resistivity, temperature logs): feasible at moderate cost, harder.**
- A full raster log can be tens of thousands to over 100,000 pixels long. A segmentation or curve-tracing network on a GPU at ~$2/hr is plausibly **$0.001–0.01 per log** in compute (computed, unverified throughput).
- The real costs are building training labels and QC. Existing LAS-raster pairs give free supervised training data: MJ's 21M curves digitised *from* rasters, and Kansas's ~22–29k LAS files with matching TIFFs.
- Budget for curve extraction limited to target intervals in about 1M wells: **low six to low seven figures** including human QC (estimate, unverified).

**Verdict:** reading millions of raster headers for temperature is **cheap, near-certain to work at useful accuracy, and fast**: weeks of engineering plus tens of thousands of dollars of inference once images are in hand. Porosity curves over target intervals are also feasible at startup scale. The moat is the **acquired image corpus, the linkage to well locations and depths, and the cleaned, corrected temperature table**, not the OCR model.

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **The Saskatchewan pattern exists at much larger scale.** Records are public by law and illegible in practice:
   - BEG has 1.5M TIFFs and no LAS.
   - Kansas has a 13:1 raster-to-LAS ratio.
   - National BHT compilations cover at most ~400–530k points, with one temperature per well in over 95% of wells.
   - Commercial libraries hold ~7M+ logs over ~3M wells (MJ alone).

   The digitisation step that Terranox runs on assessment reports maps directly onto log headers, mud logs, DSTs and temperature logs.
2. **Unit economics favour the asset-owner model.** Extraction costs ~$0.0001–0.001 per header. Any edge it buys is monetised by **leasing acreage before others see it** (BLM noncompetitive and competitive leases, state trust land, private geothermal rights; see R-files). It is not monetised by selling data. Selling data is the TGS/Enverus model (~$27M a year in revenue), a fallback floor, and a shape that scores low on our rules.
3. **Proprietary edge decays only slowly.** Free national models (InterPIGNN, In-Context Earth, USGS favourability rasters) are built on *already-digitised* BHTs. A company that digitises the rest owns better features *and* more labels, which the ML literature names as the binding constraint (L03, L09). Incumbent data vendors price per curve and have no incentive to build a free continental header-temperature table.
4. **Gap vs Zanskar.**
   - Zanskar's public data story is heat flow, satellite, geophysics, its own seismology (LBNL CRADA) and field crews, all focused on **Great Basin and Rio Grande-rift hydrothermal** systems.
   - Heatmap reports it "acquired long-forgotten analog subsurface data sets and digitized them" (https://heatmap.news/climate-tech/ai-geothermal-discovery). So assume partial overlap, but it does **not publicise systematic mass reading of oil and gas raster-log headers** and does not mention BHT correction at all (Z03).
   - The clearest whitespace is the **sedimentary basins with millions of legacy O&G logs**: Texas/Permian and Gulf Coast, the Anadarko, the Williston, the Denver-Julesburg/Piceance, the Uinta, and Alberta via MJ's Calgary holdings. Here a Terranox-style reader could map temperature at 3–6 km well by well. These are targets for EGS (Fervo-style) and sedimentary-geothermal developers and for data-centre offtakers, and they sit outside Zanskar's footprint.
5. **Risks (not kills).**
   - Licence terms on commercial rasters may restrict derived products, so prefer public archives first and negotiate field-of-use licences.
   - BHTs need correction and remain ±10–16 °C noisy.
   - Many sedimentary targets are mid-temperature (EGS or binary), and private or split-estate geothermal rights in Texas and similar states need title work (R07, R08).

None of these makes the opportunity too small. The corpus is continental.

## Sources
- TGS sale of A2D well data business to Enverus (8 Jul 2026): https://www.tgs.com/well-data
- MJ Logs, holdings and pricing model: https://www.mjlogs.com/ ; https://www.mjlogs.com/about ; https://www.mjlogs.com/pricing-orders
- Texas BEG Geophysical Log Facility (1.5M logs, TIFF only, $10 a log): https://www.beg.utexas.edu/about/facilities/geophysical-log-facility
- Texas RRC wellbore manual (no temperature field): https://www.rrc.texas.gov/media/cx2i4xrm/wba091_well-bore-database.pdf
- KGS scanned logs and bulk index: https://www.kgs.ku.edu/Magellan/Elog/scan.html ; https://www.kgs.ku.edu/PRS/Ora_Archive/ks_elog_scans.zip
- KGS LAS counts: https://www.kgs.ku.edu/Magellan/Logs/index.html ; https://www.kgs.ku.edu/PRS/Scans/Log_Summary/index.html
- NGDS 2014 counts: https://www.petroleumnews.com/story/2014/06/08/news/state-contributes-geothermal-data/26622.html
- Aljubran & Horne 2024, InterPIGNN: https://arxiv.org/abs/2403.09961
- O'Malley et al. 2026, In-Context Earth: https://www.alphaxiv.org/abs/2605.16665
- Schölderle et al. 2022, BHT uncertainty: https://www.mdpi.com/1996-1073/15/17/6367
- Neuralog home, product and 2026 AI release: https://www.neuralog.com/ ; https://www.neuralog.com/well-log-digitizing-software-neuralog/ ; https://www.neuralog.com/neuralog-update-ai-well-log-digitization-software/
- Gemini API pricing and image tokenisation: https://ai.google.dev/gemini-api/docs/pricing ; https://ai.google.dev/gemini-api/docs/image-understanding
- Zanskar data methods (Heatmap): https://heatmap.news/climate-tech/ai-geothermal-discovery
- Sibling evidence files: D01 (Texas RRC), D02 (Oklahoma/Kansas), L09 (temperature at depth), Z03 (Zanskar data methods), all in /home/user/nuketime/research/geothermal/evidence/
