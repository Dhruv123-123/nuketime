# M33: How big is a hidden hydrothermal system before anyone drills it, and how many are left?

Slice M33, model track. Date: 23 Oct 2026. This builds on `M01-usgs-assessment-methods.md` (count-times-size frame, Rg 0.08-0.25, the shared 11.6x band), `M15-uq-methods.md` (Wilmarth and Stimac 53-field power density, Cumming's area x power density, Garg and Combs on Silver Peak, Libbey and Murphy's 40 Ormat analogs with Rg 4-53%, Kaufman size-biased discovery), `M13` (Zanskar's flat 30 MWe per discovery), `M18`/`L02` (blind case studies) and `D06` (mining-hole discoveries). It does not repeat those. What is new here: (1) a first size-frequency fit of the Nevada producing fields, (2) a test of whether Nevada discovery looks like an oil-style "creaming curve" (it does not), (3) a toy discovery-process simulation that shows how much the borrowed size distribution could be biased, and (4) how to turn all of this into a per-cell "MWe if it exists" prior.

**Search notes.** The shared web-search budget for this run was already spent when this slice started, so no new searches or fetches ran. Everything below comes from prior repo files (cited by file), primary sources I know by name (marked "from memory", with the best URL I know), and my own arithmetic on an approximate Nevada plant list (marked unverified). The fit script is at `/home/user/nuketime/research/geothermal/model/evidence/M33_fit_sizes.py`. The plant list should be replaced with EIA-860 nameplate data before anyone relies on the numbers.

## Bottom line

Before drilling, the industry sizes a system in one of two ways. **Stored heat** (USGS, Muffler and Cataldi lineage) multiplies a hot rock volume by a recovery factor. **Power density** (Wilmarth, Cumming) multiplies an area by MW per km². Both are honest skeletons, but both have a 7-13x spread at the exploration stage, and neither has ever been hindcast on blind systems. What matters more for a heat-rights bank is the **size distribution of the population**, because it sets how many leases are worth more than the "too small" line. My rough fit of 18 Nevada producing fields gives a **lognormal with median about 29 MW and sigma about 0.95** (mean about 45 MW), and a **heavy tail (power-law index about 1.1 above 15 MW)**. The top 3 fields hold 44% of the MW. So a lease portfolio is a power-law bet, like mineral royalties: a few fields carry the book. Two results matter most. First, **Nevada has no creaming curve.** The largest field (McGinness Hills, about 160 MW) came online in 2012, 25+ years after the first plants, and size versus discovery order has a rank correlation of about 0.03. In oil, big fields are found first. In Nevada geothermal they are not, because discovery was driven by surface leakage, not size. That means the remaining pool is **not obviously depleted of big systems**, and blind fields are, if anything, larger (blind median about 45 MW versus 20 MW for spring-marked fields in this sample, which is partly a "developers only build big blind fields" effect). Second, if discovery *were* size-biased, the borrowed USGS size distribution would overstate hidden-system size by up to 2x (my simulation). The data say that bias is weak. So the best model is: **count from an occupancy-detection model (M15), times a size prior that is lognormal (median about 25-30 MW, sigma about 1), shifted by local temperature and structural setting, and updated by our own sensors.** Rough check: 100-150 undiscovered Nevada systems (Coolbaugh 2006 says 157) at a 30-45 MW mean gives 3-7 GW, which brackets the USGS Nevada mean of 4.4 GW. The sensor that most narrows *size* (not existence) is one that measures **reservoir temperature and upflow area** before drilling: a geothermometer-grade fluid sampler on the drop probe, plus a dense 2 m temperature grid and E-field MT to outline the upflow.

## Findings

### F1. The two standard size methods, and what is new about them for blind Great Basin plays
- **Stored heat (volumetric).** MWe = (rho*c*V*(T_res - T_ref)) x Rg x conversion efficiency / (plant factor x 30 yr). Origin: Muffler and Cataldi 1978, Geothermics 7, "Methods for regional assessment of geothermal resources" (from memory, https://doi.org/10.1016/0375-6505(78)90002-0). The USGS 2008 version is in OFR 2008-1296 (M01). Known faults: it is linear in Rg and volume, and both are guesses before drilling. Grant (2014, "Stored-heat assessments: a review in the light of field experience", Geothermal Energy Science 2:49-54, from memory, https://doi.org/10.5194/gtes-2-49-2014) compared stored-heat estimates with what fields actually produced and found they **overestimated in most cases** (my memory of the paper is that the bias is large and systematic; exact ratios unverified). Garg and Combs (SGW 2010, in M15) showed the P90 moves 5x with input choices.
- **Power density (area x MW/km²).** Wilmarth and Stimac 2014 (53 fields >200 °C, in M15). Wilmarth, Stimac and Ganefianto (WGC 2015, "Power density in geothermal fields", from memory, https://www.geothermal-energy.org/pdf/IGAstandard/WGC/2015/16020.pdf) extended it and grouped by setting. The repo already has their summary: 80% of fields fall between 5.6 and 38.5 MW/km², and **seven fields below 150 °C span 0.2-20 MW/km²**. Power density rises about 2 MW/km² per 10 °C.
- **What is new for us.** Blind Great Basin systems are mostly 120-180 °C binary plays. At 150 °C the Wilmarth trend predicts about 5-10 MW/km² (my extrapolation). A typical Nevada binary field (25-50 MW) therefore needs about 3-8 km² of productive area. That is **2,000-5,000 acres**, which is a few BLM lease blocks or a handful of ranch sections. At $1-2/acre, locking the whole upflow footprint of a median system costs about **$2,000-10,000**. This is the core asymmetry: the right to a median 29 MW system costs four orders of magnitude less than its value (at roughly $2-5M per MW of plant value, or $60-150M; unverified, see B07).
- **Plant size is not resource size.** Ormat builds in phases: McGinness Hills went 72 -> 138 -> about 160 MW (repo D06/L02). So nameplate understates the resource early, and the first estimate is usually low. Any fit on nameplate is a lower bound on resource size.

### F2. Size-frequency of Nevada producing fields (my fit, approximate data)
Approximate nameplate MW for 18 Nevada fields (from repo files and memory; unverified, replace with EIA-860): McGinness 160, Steamboat complex 100, Dixie Valley 65, Blue Mountain 49.5, Patua 48, Brady + Desert Peak 48, Stillwater 47, Don A. Campbell 42, Tungsten Mountain 26, North Valley 25, Soda Lake 23, Salt Wells 23, Jersey Valley 22, Tuscarora 18, Beowawe 17, San Emidio 14, Dixie Meadows 12, Wabuska 2. Total about 740 MW, consistent with the "under 600-800 MW in the Great Basin" figures in L05 (definitions differ).

| Statistic | Value |
|---|---|
| Median | 25.5 MW (lognormal fit median 28.8) |
| Mean | 41 MW (lognormal mean 45) |
| Lognormal sigma (natural log) | 0.95 |
| Top 3 share of total MW | 44% |
| Power-law (Hill) index above 15 MW | 1.07 (a Zipf-like tail) |
| P(size >= 10 / 20 / 30 / 50 / 100 MW) from the fit | 0.87 / 0.65 / 0.48 / 0.28 / 0.10 |
| Blind-field median vs spring-marked median | 44.5 vs 20.5 MW (n = 8 vs 10) |

- Meaning: **Zanskar's flat 30 MWe per discovery (M13) is close to the median, but it throws away the tail.** With sigma about 1, the mean is about 1.6x the median, and one field in ten is above 100 MW. For a royalty or carry business, the expected value lives in that tail.
- A power-law index near 1 means the total MW of a region is set by its few biggest systems. Region totals will have wide bands no matter how good the count is. This explains part of the USGS 11.6x band (M01).
- The sample is censored at the low end. Systems under about 10 MW are rarely built in Nevada (economic floor). So the true population of systems is more numerous and smaller than the producing set. A model must keep "population of systems" and "population of buildable systems" apart.

### F3. No creaming curve in Nevada: big fields were not found first
- Oil and gas discovery-process models assume that discovery probability rises with size (Arps and Roberts 1958, AAPG Bull. 42; Kaufman, Balcer and Kruyt 1975, "A probabilistic model of oil and gas discovery", AAPG Studies in Geology 1; Barouch and Kaufman 1977; Drew, Schuenemeyer and Bawiec 1982, USGS Prof. Paper 1252, https://pubs.usgs.gov/publication/pp1252; all from memory). This produces the "creaming curve": cumulative volume against number of wildcats rises fast, then flattens. The flattening tells you how much is left.
- In my Nevada list, the rank correlation between first-power year and size is **0.03**, that is, none. Cumulative MW grew in two steps: about 316 MW from 1984-1989 (mostly spring-marked fields plus Desert Peak and Stillwater), then about 425 MW from 2009-2024, led by blind fields found through mining holes (McGinness, Blue Mountain, Don A. Campbell, Tungsten Mountain; D06). The curve is **not flattening**. The second step was driven by new data (mining holes) and new policy (2005 Energy Policy Act leasing, ITC), not by depletion.
- Meaning: geothermal discovery is biased by **leakiness** (hot springs, sinter, steam), not size (M15 F3). Leakiness is only weakly tied to MW. So the classic oil-style "big ones are gone" argument does not apply. Big blind systems can still be out there. This is optimistic for us, and it is a testable claim.

### F4. How much could size bias distort the hidden-resource number? (toy discovery-process simulation)
I drew N systems from the fitted lognormal and "discovered" 18 of them with probability proportional to size^beta, without replacement (Kaufman style). Mean over 2,000 runs:

| beta (size bias) | N total = 30 | N = 60 | N = 120 |
|---|---|---|---|
| 0 (no bias) | found 30 / left 31 MW median | 30 / 29 | 30 / 29 |
| 0.5 | 39 / 21 | 43 / 25 | 46 / 27 |
| 1.0 (oil-like) | 44 / 17 | 56 / 23 | 64 / 26 |

- If discovery were oil-like (beta = 1), the found fields would be about 2x the parent median and the left-over systems would be about 0.6-0.9x it. USGS borrowed the identified size distribution unchanged (M01 F1), so under beta = 1 it would overstate hidden size by up to 2x.
- F3 says beta is near 0 for Nevada. Then **hidden systems are about the same size as known ones**, and the USGS borrowing is roughly fair. The repo's blind examples (Big Blind, about 121 °C with >100 MWe analogs claimed by Zanskar; McGinness 160 MW) support this.
- A proper Bayesian discovery-process model can fit beta, N and the lognormal jointly from discovery order plus exploration effort. With about 20-30 Nevada fields and the USGS 205-system inventory (M01 F4) this is feasible, but the band on N will stay wide unless effort is measured (M15 F4).

### F5. How many systems remain: three independent anchors agree on "about 2-3x the known count"
- Coolbaugh et al. 2006 (in M01): **157 undiscovered Nevada systems at >=100 °C against 69 known (3.2x).**
- Faulds and Hinz 2015 and Coolbaugh 2007 (in L05): about 39% of known systems are blind, and about 75% of all Great Basin resources are estimated to be blind.
- USGS 2008: undiscovered mean is 3.3x identified nationally, and Nevada undiscovered mean is 4,364 MWe against 1,391 MWe identified (3.1x) (L05).
- Check by count x size: 100-157 undiscovered Nevada systems x P(buildable >= 10 MW) 0.87 x mean about 45 MW gives **about 4-6 GW**. This sits on the USGS Nevada mean. So the three anchors are consistent with one another. They are all built on similar data, though, so they are not truly independent.
- The 2026 USGS inventory adds 99 "probable" systems to 106 known electric-grade ones (M01 F4). If most of the 99 are real, the known count roughly doubles, and the undiscovered count from favorability conditioning also rises.

### F6. The "too small" line, in numbers
- At the fitted distribution, about 13% of systems are under 10 MW and about 35% are under 20 MW. Those mostly fail as stand-alone binary plants in Nevada (transmission, drilling cost; unverified threshold, see B03/B07).
- So for a portfolio of, say, 100 locked cells with real systems, expect about 65 at >=20 MW, about 28 at >=50 MW and about 10 at >=100 MW. If the override is about $1-3/MWh (B07) on about 8,000 MWh per MW-year, a 50 MW field pays about $0.4-1.2M per year (my arithmetic). The 10 tail fields would carry most of the book. Size is not the killer; existence and buyer appetite are.

## Datasets

| Dataset | Access | Coverage | Value for blind detection and sizing |
|---|---|---|---|
| EIA-860 generator nameplate and EIA-923 generation | Free, https://www.eia.gov/electricity/data/eia860/ ; https://www.eia.gov/electricity/data/eia923/ | All US plants >1 MW | Replace my approximate list; fit the size distribution on actual MW and capacity factor |
| Wilmarth and Stimac 2014 / WGC 2015 power-density tables | Free, https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2014/Wilmarth.pdf | Global, mostly >200 °C, plus 7 fields <150 °C | Power density prior, MW/km² vs temperature and setting |
| BLM MLRS geothermal leases, units and well locations | Free, https://mlrs.blm.gov | Federal land | Productive area per field, to build a low-T power-density curve |
| NBMG Nevada geothermal well and plant database | Free, https://nbmg.unr.edu | Nevada | Discovery dates, first-hole year, discovery channel for the discovery-process model |
| USGS 2008 identified-system table (OFR 2008-1296 appendix, FS 2008-3082) | Free, https://pubs.usgs.gov/of/2008/1296 | 13 western states | Per-system volume, temperature and MWe triangles; the "borrowed" size set |
| USGS 2026 Great Basin 205-system inventory with capacity and uncertainty | Free data release (DOI not retrieved, unverified) | Great Basin | Known plus probable systems with capacity; the main fitting set |
| Libbey and Murphy 2026 40 analogs (Rg back-solved) | Free, https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Libbey.pdf | Ormat analog fields | Recovery-factor prior by permeability regime |
| Global geothermal field list (IGA/ThinkGeoEnergy plant lists, Bertani country updates) | Free, WGC country updates, https://www.geothermal-energy.org | World | A larger N (about 200 fields) to fit the tail index and check Nevada against other extensional provinces |

## What dominates uncertainty (per this slice)
1. **Size-tail shape.** A power-law index near 1 means one large field moves a regional total more than dozens of small ones. With only about 20 Nevada fields, the tail index is poorly fixed (my rough 95% range about 0.6-1.6, unverified).
2. **Low-temperature power density.** The public calibration is above 200 °C. Our targets are 120-180 °C. The MW/km² at 150 °C is an extrapolation, likely good to about 2-3x.
3. **Productive area before drilling.** Area enters linearly. MT outlines run several times too large (Cumming, M15). The upflow area is the single input a sensor could pin best.
4. **Discovery bias (beta).** My evidence says it is weak in Nevada, but that rests on about 18 points and on nameplate, not resource size.
5. **Censoring and phasing.** Small systems are not built, and big ones are built in phases. Both distort any fit on plant data.
6. **Recovery factor / permeability.** Still the largest physical term (M15: Rg 4-53%). Sensors cannot fix it before a flow test.

## What a sensor could fill
- **Reservoir temperature before drilling (sets power density).** Add a fluid sampler to the ranch drop probe (already the prior hardware pick): a sealed bottle for silica and Na-K-Ca geothermometers, plus in-situ conductivity and pH. A 20 °C shift in reservoir temperature moves power density by about 4 MW/km² (Wilmarth trend), so this is a direct size input. Cost per sample is a lab fee of roughly $100-300 (unverified).
- **Upflow footprint (sets area).** A dense 2 m temperature grid (50-100 probes at 200-500 m spacing) over an anomaly outlines the shallow thermal plume. Combined with E-field MT conductance, it gives an area estimate with real error bars, not the over-large MT contour. This is the cheapest way to cut the area term, which is linear in MW.
- **Heat output of the outflow (a direct "natural-state MW" proxy).** Where a blind system has a subsurface outflow plume in an aquifer, water-well gradients plus flow give a natural convective heat flux (MWth). Natural heat flow is a known lower bound on sustainable output (a classic NZ-style check; from memory). A grid of logged water wells turns into a heat-flux map, so this sensor sizes systems, not just finds them.
- **Discovery-effort log.** Every probe visit is recorded as effort, which the discovery-process model needs to fit N and beta.
- Not fillable cheaply: permeability and Rg. Keep them as priced priors and pass that risk to the buyer.

## Implications for a better model
1. **Use a two-level size prior, not a flat 30 MWe.** Level 1: a population lognormal (median about 25-30 MW, sigma about 1) fitted to EIA-860 plus the USGS 205 inventory, with left-censoring below about 10 MW and a phasing correction. Level 2: shift each cell's size prior by predicted reservoir temperature (via power density per 10 °C) and structural setting (step-over, accommodation zone, fault tip; M11). Report P(MWe >= 20) and P(MWe >= 50) per cell, not a point.
2. **Fit a Bayesian discovery-process model for Nevada.** Unknowns: N (total systems), lognormal parameters, size-bias beta, leakiness-bias, and discovery rate per unit effort. Data: discovery order and channel (springs, gradient hole, mining hole, ag well), exploration effort per cell, and the 205-system inventory. Do it in NumPyro or Stan. It will give the first honest posterior on "how many are left" for any geothermal province. Then run it for other provinces (Utah, Oregon, Idaho, New Mexico), where effort is lower and the posterior on N is wider: that is where the land alpha is.
3. **Build the low-temperature power-density curve.** For each US binary field: EIA-923 average MW over the last 10 years, divided by the area of a 500 m buffer around production wells (BLM/NBMG well maps). This is public, nobody has published it (M15), and it is the weakest input for blind Great Basin plays.
4. **Treat the portfolio as a power-law book.** Value lease portfolios by simulation from the fitted tail, not by the mean. The top decile of locked systems will carry most of the value. Spend sensor money where P(MWe >= 100) is highest, not where P(exists) is highest.
5. **Check against hindcasts.** Freeze the size model as of 2008 data, then score it on fields built 2009-2024 (Blue Mountain, McGinness, Don A. Campbell, Tungsten Mountain, North Valley, Dixie Meadows). This is a clean, publishable validation buyers will trust.
6. **Track the creaming curve live.** Plot cumulative discovered MW against cumulative exploration effort for each province every year. A flat curve after real effort means the province is mined out. A curve that steps up when a new data type arrives (as with mining holes in 2009-2017) means the new data type is the edge. Our own sensors should make the next step.

## Sources
- Muffler and Cataldi 1978, Geothermics 7 (from memory): https://doi.org/10.1016/0375-6505(78)90002-0
- Williams, Reed and Mariner 2008, USGS OFR 2008-1296: https://pubs.usgs.gov/of/2008/1296
- Williams et al. 2008, USGS FS 2008-3082: https://pubs.usgs.gov/fs/2008/3082
- Grant 2014, Geothermal Energy Science 2 (from memory): https://doi.org/10.5194/gtes-2-49-2014
- Wilmarth and Stimac 2014, SGW: https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2014/Wilmarth.pdf
- Wilmarth, Stimac and Ganefianto 2015, WGC (from memory): https://www.geothermal-energy.org/pdf/IGAstandard/WGC/2015/16020.pdf
- Cumming 2016, SGW: https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2016/Cumming.pdf
- Garg and Combs 2010, SGW: https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2010/garg.pdf
- Libbey and Murphy 2026, SGW: https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Libbey.pdf
- Coolbaugh et al. 2006: https://www.usgs.gov/publications/prediction-and-discovery-new-geothermal-resources-great-basin-multiple-evidence-a
- Drew, Schuenemeyer and Bawiec 1982, USGS PP 1252 (from memory): https://pubs.usgs.gov/publication/pp1252
- Arps and Roberts 1958; Kaufman, Balcer and Kruyt 1975; Barouch and Kaufman 1977 (from memory, no URL checked)
- Kaufman and Schuenemeyer 2007, AAPG abstract: https://www.searchanddiscovery.com/abstracts/html/2007/annual/abstracts/lbKaufman.htm
- Ormat McGinness Hills expansion: https://investor.ormat.com/news-events/news/news-details/2021/Ormat-Completes-McGinness-Hills-Complex-Expansion/default.aspx
- Plant MW list: repo files D06, L02, Z08 and memory (unverified; replace with EIA-860)
