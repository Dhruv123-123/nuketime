# M29: What pre-drill information predicts success in US geothermal wells

Slice M29, model track. This builds on `evidence/L13-exploration-risk.md` (IFC 50% first well, Sanyal & Morrow, Wall & Dobson "<1/3", ESMAP costs, cost of capital), `L01-play-fairway.md`, `L04-ingenious.md`, `L16-gtc-holes.md` and `model/evidence/M01-usgs-assessment-methods.md`. It does not repeat their tables. It covers four things those files leave open: (1) what "success" and "confirmation" actually mean, rung by rung; (2) a cost-per-hole-by-depth ladder; (3) what is and is not known about success *by data package* (MT, gradient, structure); (4) how to turn all of this into labels and a decision model.

**Method note.** The shared WebSearch budget for this workflow was used up before this agent's first search. One fetch worked (the Wall & Dobson 2016 abstract on the Stanford server). The Sandia Lowry et al. 2017 PDF on OSTI timed out on a permission prompt (https://www.osti.gov/servlets/purl/1394062, blocked this run). Everything else comes from the repo's earlier evidence files (which cite their primary sources) and from what I know. Anything I could not check this run is marked (unverified).

## Bottom line

There is **no public US dataset that tabulates geothermal well outcomes against the pre-drill data package**. Nobody has published "wells sited with MT + gradient holes + structural mapping succeeded X%, wells sited without them Y%". The famous numbers measure different things. IFC's **50% first-well success** counts wells of at least 3 MWe in fields that were *later developed*, so it is survivorship-biased. Wall & Dobson's **"under one-third"** counts western-US projects whose exploration drilling went on to full-size development wells. GeoVision's **50% confirmation-well success** is a modelling assumption. The only US data that link a chosen data package to an outcome are small: Play Fairway (2 of 2 drilled sites hot at TG depth), INGENIOUS (Argenta Rise, the top-scored site with gravity, MT, aeromagnetics, 139 two-metre points and 10 TG holes, came back cool), the 1977+ DOE Industry-Coupled program (8 of 14 surface-expressed sites reached power, 57%), 2 m surveys (about 36% of surveyed areas anomalous, at sites chosen because they looked good), and Zanskar's own statements ("three of three" funded sites, yet "we've missed way more than we've hit"). The lesson from Sanyal & Morrow still holds: success moves in *steps* when the conceptual model is revised, not with drilling practice. So the better model should not predict "success" as one label. It should predict an **ordinal ladder of outcomes** (hot TG hole, then convective gradient, then a slimhole at at least 120-150 °C, then a full-size well flowing at least 3 MWe, then a financed project), with an explicit **which-data-came-before** feature and an explicit **masking** term. The best sensor to build is one that cheaply produces the missing middle rung: a **true temperature and convection label at 150-500 m in existing holes and new cheap holes**, plus a fluid sample. That is the ranch drop probe and light gradient rig already picked, now aimed at re-logging and at building the first public-quality "pre-drill package vs outcome" table.

## Findings

### F1. "Success" has at least six meanings, and the headline numbers mix them
| Rung | What counts as success | Who uses it | Typical rate | Source |
|---|---|---|---|---|
| R0 Desk anomaly | Cell in the top band of a favorability map | USGS, INGENIOUS, Zanskar | 26 of 28 producing systems above the 80th percentile; 15 of 28 in the top 1% of area | USGS 2025 map via M01 F3 |
| R1 Shallow thermal anomaly | 2 m temperature or TG gradient well above background (Nevada background about 2-3 °F/100 ft) | NBMG, PFA | About 36% of surveyed areas (sites chosen for promise); PFA 2 of 2; INGENIOUS Argenta 0 of 1 | L01, L04, L16, M02 |
| R2 Electric-grade evidence | A well above **85 °C with evidence of convection** | USGS 2026 inventory | 205 systems listed (28 producing, 78 other known, 99 probable) | DeAngelo, Burns & Mordensky 2026, https://www.usgs.gov/publications/conventional-hydrothermal-power-producing-systems-great-basin-usa (via M01) |
| R3 Slimhole / intermediate well | Reservoir temperature and some permeability at 500-1,500 m | Developers | Not published for the US | Zanskar Big Blind about 121 °C at about 2,700 ft (L13) |
| R4 Productive full-size well | Final capacity of **at least 3 MWe** | IFC 2013 | 50% first well; 59% first five; 74% development; 83% operations | IFC 2013 via Lowry 2017 (L13) |
| R5 Project success | Exploration leads to full-size development wells | Wall & Dobson 2016 | **Under one-third** in the western US | GeoVision p. 37 quoting Wall & Dobson (L13) |
| R6 Bankable confirmation | Enough flow-tested capacity behind the wellhead for project debt | Lenders | Hudson Ranch: debt came once about 75% of capacity was behind the wellhead | Wall, Dobson & Thomas 2017 (L13) |

- The Wall & Dobson 2016 abstract (fetched this run) says plainly that there is "no common definition of exploration success". It says earlier studies defined success loosely as the number of commercially viable wells. The paper looks at **project-level records from western US sites, organised around decision points**. It also counts non-reservoir causes of failure such as financing and land-sale delays, and how exploration methods complement each other. It promises later work on which exploration elements most affect project success. https://pangea.stanford.edu/ERE/db/IGAstandard/record_detail.php?id=26553
- I found no published follow-up that gives success broken down by method (unverified; the search budget was gone). **This gap is the single biggest finding of this slice.**
- So "50%" and "under 33%" do not conflict. One is per well inside fields that worked. The other is per project from the start of drilling. For a blind-system rights bank, the right prior is lower still. Wall & Dobson's projects mostly began at sites with surface signs.

### F2. How "confirmation" is defined in practice (the rung buyers pay for)
- **GEA development phases.** The Geothermal Energy Association's 2010-2011 reporting guide splits projects into Phase I (resource procurement and identification), Phase II (resource exploration and confirmation), Phase III (permitting and initial development) and Phase IV (production and plant construction). As I remember it, a project leaves Phase II once at least one production-size well has been drilled and flow-tested at commercial temperature and rate. GEA's yearly reports then listed "confirmed" against "unconfirmed" MW. (GEA, *New Geothermal Terms and Definitions*, 2010; exact wording and URL unverified.)
- **Reserves codes.** The Australian Geothermal Reporting Code (AGRCC 2008, 2nd ed. 2010) and the Canadian Geothermal Code (CanGEA 2010) borrow the mining JORC ladder: **Inferred, then Indicated, then Measured** resources, and **Probable, then Proven** reserves. "Measured" needs well data, including temperature and flow or permeability tests, that are close enough to support a volume estimate. "Proven" needs that plus the economic and permitting factors. (Recalled from the codes; unverified this run.) No US code is binding. US buyers use their own internal standards.
- **Lenders.** In the ESMAP handbook the test-drilling phase (3-5 wells) exists "to confirm the existence of an exploitable resource". It costs up to 15% of capex while failure risk is still high (L13). Project debt comes only after flow tests. At Hudson Ranch that meant about 75% of capacity behind the wellhead. A common rule is that wells must prove 25-30% or more of planned capacity before construction debt (unverified).
- **What this means for us.** A buyer such as Ormat or Invenergy will pay a modest amount for R1-R2 evidence and much more for R3. The steepest step in price is at R4-R6. The model's output has to be the **probability of reaching each rung**, because that is what sets the price at each sale point.

### F3. Cost per hole by depth: a ladder for the value-of-information model
| Measurement | Typical depth | Cost per point or hole | Source |
|---|---|---|---|
| 2 m temperature probe | 2 m | About $100-200 per site | Hardware MEMO / H files |
| Re-log an existing water, mining or TG hole with a drop probe | 50-300 m | A few hundred dollars per hole | Hardware pick (L22/H files) |
| TG hole, drilling only | Under 500 ft | $5 / **$16.50** / $50 per ft (low / median / high), so about $8k at 500 ft | OpenEI, https://openei.org/wiki/Thermal_Gradient_Holes |
| TG hole, all-in (permit, road, logging, plugging) | 150-300 m | About $100-300k per hole (incumbents) | Repo estimate (unverified) |
| PFA validation TG holes | 150-250 m | About $1.5M for 12 holes at 2 sites, about $125k each | Faulds et al. 2021, OSTI 1724080 (L13) |
| Gradient or intermediate hole | 150-900 m | $0.3-1.5M all-in | Repo brief (unverified) |
| Slimhole (core or rotary) | Up to 1,500 m | $0.5-1.5M (2012 $), about **50%** of a full-size well at the same depth | ESMAP 2012 (L13) |
| Full-size production well | 1.5-3 km | $2-6M (2012 $). About $5-10M today (unverified). About $4.8M quoted for an EGS-style well | ESMAP 2012; repo (L17) |
| Full-size **confirmation** well | 1.5-3 km | **20-50% more** than a production well | GeoVision 2019 (L13) |
| 3-5 well test campaign | | $11-30M (ESMAP 2012) / $20-30M (ESMAP 2016) | L13 |

- Geothermal wells cost **2-5x** oil and gas wells of the same depth. Probabilistic cost studies show variance of more than ±50% (Lowry et al. 2017, via L13). Cost rises faster than linearly with depth. Each extra 0.5 km adds more than $1M (ESMAP 2012).
- Most of the all-in cost of a shallow hole is not the drilling. It is mobilisation, roads, crew, permits, logging and plugging. The drilling alone is $16.50/ft. That is why our own light rig and the re-logging of existing holes make the biggest change to the ladder.
- Over 2022-2025, Fervo reports about 70% lower cost per foot and about 75% less drilling time (repo, Fervo S-1). Deep-rung costs are falling. That makes the *middle* rungs (R2-R3) the relative bottleneck.

### F4. What we actually know about success by data package
- **Structure is close to necessary.** About 90% of known Great Basin systems sit in favorable structural settings (Faulds and Hinz). INGENIOUS mapped more than 1,430 such settings. But the settings cover a large area, so structure alone gives a hit rate of perhaps 0.2-0.25 systems per setting (M02 estimate, unverified). Structure is necessary, not sufficient.
- **Structure + favorability + 2 m + MT + gravity can still miss.** Argenta Rise had the highest PF score, a confirmed pull-apart, MT conductors and magnetic lows. Yet 139 two-metre points and 10 TG holes to about 244 m gave no clear anomaly. The likely cause is a cold aquifer masking the heat; MT conductors sit at about 1.5 km (Faulds et al. 2025, GRC 48; Jacinto et al. 2026, SGW 51; https://pubs.usgs.gov/publication/70271419).
- **Structure + favorability + a few TG holes found two blind systems.** Play Fairway Phase 3: Gabbs Valley about 124 °C at 152 m and Granite Springs about 96 °C at about 250 m. Neither has proven capacity (Faulds et al. 2021, OSTI 1724080). Craig (2018): 6 TG holes, 2 above boiling, a system of at least 130 °C (OSTI 1724116).
- **Surface-expressed sites with cost-shared deep drilling.** The DOE Industry-Coupled Program (from 1977) drilled 14 sites; 8 were producing by 1995 (57%), with 137 MW (Fortuna 1995, OSTI 860716, via L16). That is the best US "package to outcome" number, but it is for *known* systems with springs.
- **Mining holes as an accidental data package.** McGinness Hills, Don A. Campbell and Blue Mountain were all found from mineral-hole temperatures, and all became plants (NREL Mining G.O.L.D. 2022, via L16). Conditional on a hot mining hole being reported, the hit rate to a plant is high, but the sample is tiny and selected.
- **The base rate is tiny when you use no targeting.** About 49 blind systems from about 27,000 drill samples, or 0.18% per sample (repo M13 figure; source in M13).
- **Conceptual models, not drilling skill.** Sanyal & Morrow (2012): in 19 liquid-dominated fields, well capacity changes in steps that follow revisions of the conceptual model. Success rates stabilise only after about 40 wells (via L13). In volcanic fields, the MT clay cap is the main input to the conceptual model. Cumming warns that MT uncertainty that is not carried into the model causes targeting failures (repo L14). In the Basin and Range the clay cap is often thin or missing. There, structure plus gradient holes do the work MT does in volcanic fields (inference).
- **Zanskar's own record.** It has tested more than 5 million acres, but says "we've missed way more than we've hit" and that its models beat expert explorers only in the last year or two. Its funded sites were "three of three" (Volts 2025; TechCrunch 2026; via repo). No numbers are published.
- **What predicts a productive full-size well once heat is known?** Mainly permeability, meaning an open fracture zone at the right depth. Slimhole tests help here. Garg and Combs showed in the 1990s that slimhole injectivity and productivity indices, scaled for diameter, predict large-diameter well output at liquid-feedzone fields (Steamboat Hills and several Japanese fields; Sandia slimhole program; recalled, unverified). Temperature alone does not predict R4.

### F5. A rough value-of-information calculation (my arithmetic)
- Cost per confirmed discovery with a $6M confirmation well: $18M at 33% success, $12M at 50%, $10M at 60%, $8M at 75%.
- With a funnel, start at a desk prior of 20% per prospect. Spend $0.45M on 3 TG holes and drill a well only if they come back positive.
  - Test with 70% sensitivity and 80% specificity: P(positive) = 0.30 and the posterior = 0.47. Cost per confirmed discovery is about **$16M**. Drilling blind costs about **$30M**.
  - Test with 85% sensitivity and 90% specificity: posterior 0.68, cost about **$11.5M**.
  - At a 5% prior even the good test only reaches a 0.31 posterior. Cheap rungs must be stacked before a well.
- So the money is in **sensitivity under masking** and in **specificity**. A false "hot" costs a $6M well. A masked "cold" (Argenta) throws away a real system.

## Datasets
| Name | Access | Coverage | Value for blind detection |
|---|---|---|---|
| IFC 2013 *Success of Geothermal Wells* | Public PDF (the IFC link loops; read via Lowry 2017) | 2,613 wells, 57 fields, 14 countries | Learning curve by well order; survivorship-biased; no blind or US split |
| Wall & Dobson 2016 project records | Paper (SGW 41); underlying table not released (unverified) | Western US projects, by decision point | The only US project-level outcomes; ask LBNL for the table |
| USGS 2026 Great Basin inventory (205 systems, confidence-ranked) | USGS data release (companion) | Great Basin | Ordinal R2 labels: producing, known, probable |
| USGS heat-flow residual labels (DeAngelo 2022/2023) | ScienceBase doi:10.5066/P9BZPVUC | Great Basin wells | Convective vs conductive labels; per-well residual |
| Sass et al. 1999 industry TG holes (OFR 99-425) | Public spreadsheet | 786 holes, 82 prospects (NV, UT, OR) | Gradient per hole; can be joined to later development outcomes = a historical "package vs outcome" table |
| PFA and INGENIOUS validation holes, GeoRePORTs | GDR 756, 1276, 1391 | About 17 PFA holes + 10 Argenta TG holes | Rare cases where a map made a prediction and a hole tested it |
| Nevada Division of Minerals geothermal permits | Public web (NRS 534A) | All NV TG and production well permits | Who drilled where and when; follow-on permits signal success |
| BLM lease, unit and well records; GEA / NREL project status lists | Public, scattered | US | Project-level outcomes through time (R4-R6) |
| DOE Industry-Coupled Program reports (1977+) | OSTI, unrestricted by design | 14 NV/UT sites | Data package + deep wells + outcome |
| OpenEI TG hole cost page; ESMAP; GeoVision; NREL drilling cost curves | Public | Costs | Cost side of the VOI model |

## What dominates uncertainty
1. **Label definition and survivorship.** The rates come from different rungs and from fields that were already successful. True failures (abandoned prospects, dry wells on dropped leases) are mostly unreported.
2. **No package-to-outcome table.** We cannot yet say how much MT, gradient holes or structure each add to P(success). Today's priors are expert judgement plus about 20 public test cases.
3. **Masking by cold groundwater.** This is the main false-negative mechanism at shallow rungs (Argenta, the Hawaii and Washington "rain curtain").
4. **Permeability at reservoir depth.** It separates R3 (hot) from R4 (productive). No surface method measures it well.
5. **Small samples and streakiness.** Success stabilises only after about 40 wells per field (Sanyal). Zanskar calls its own hit rate "streaky".
6. **Cost variance of more than ±50% per well**, and falling deep-drilling costs, both of which shift the best stopping rung.

## What a sensor could fill
- **The missing middle rung (R2-R3 labels).** A drop probe that logs temperature, pressure and conductivity in existing water, mining and old TG holes to 300-500 m, plus a light rig for new 300-500 m holes. Each log produces a convective vs conductive label below the masking aquifer. That fills exactly the gap between 2 m data and a $1M slimhole.
- **A fluid sampler on the same probe.** Silica and Na-K-Ca geothermometers, B, Li, Cl and 3He/4He. These can see through a cold aquifer, which is the Argenta failure mode.
- **Dense E-field MT nodes across the structural setting and down hydraulic gradient.** They map conductors at 0.5-2 km under the masking layer. They also turn "MT used or not" into a numeric feature for the success model.
- **A cheap permeability proxy in our own holes.** Spinner or heat-pulse flowmeter plus repeat temperature logs (showing inflow zones) and an injection fall-off test in 300-500 m holes. This is a first step toward predicting R4 rather than only heat (unverified that it scales to depth).
- **Above all, the data product.** Every hole we log becomes a row: what data existed before, what the model predicted, what the hole found, and later what the buyer's well found. That is the first proprietary "package vs outcome" table in US geothermal. It is also the actuarial base that ESMAP says the market has never had (L13).

## Implications for a better model
1. **Predict an ordinal ladder, not a yes or no.** Fit P(reach rung k | features, rungs reached) with an ordinal or sequential (continuation-ratio) model. Price each prospect at every sale point, from desk anomaly to bankable.
2. **Make "what data existed before drilling" a feature.** Use indicators for MT, TG holes, 2 m surveys, structural mapping, geochemistry and mining holes, and for the order they came in. Fit it on a hand-built historical table: Sass 1999 holes, DOE Industry-Coupled sites, PFA, INGENIOUS, USGS 205 systems, Nevada permits and BLM records. This gives a first estimate of the value of each method.
3. **Correct for survivorship.** Treat abandoned prospects and unreported dry holes as censored or missing-not-at-random. Weight IFC-style rates down for blind targets. A reasonable blind prior per first deep well is about 20-35%, not 50% (my estimate).
4. **Carry a masking latent variable** (thickness and flow of the cold aquifer), so a cold shallow reading over a thick fast aquifer counts as weak evidence.
5. **Split heat from permeability.** Use two heads: temperature at depth (well constrained by our probes) and productivity (weak). Report both, because buyers price both.
6. **Pick the next measurement by value of information.** Use the cost ladder in F3, and stop at the rung where a buyer's price per unit of probability gained is highest. That is usually R2-R3 for us. Carry only the best 10-20% to a confirmation well (L13).
7. **Calibrate publicly.** Track whether each new hole falls inside the predicted range (Zanskar does this privately). A record of calibrated hits is itself what we sell to Ormat, Fervo and Invenergy.

## Sources
- Wall, A.M. & Dobson, P.F. (2016), Refining the Definition of a Geothermal Exploration Success Rate, SGW 41 (abstract fetched): https://pangea.stanford.edu/ERE/db/IGAstandard/record_detail.php?id=26553
- Lowry et al. (2017), SAND2017-9977 (blocked this run; content via L13): https://www.osti.gov/servlets/purl/1394062
- DOE GeoVision (2019): https://www.energy.gov/sites/prod/files/2019/06/f63/GeoVision-full-report-opt.pdf
- ESMAP Geothermal Handbook (2012): https://openknowledge.worldbank.org/handle/10986/23712 ; ESMAP (2016): https://openknowledge.worldbank.org/handle/10986/24277
- Wall, Dobson & Thomas (2017), GRC Trans 41: https://publications.mygeoenergynow.org/grc/1033704.pdf
- Faulds et al. (2021), Nevada PFA, OSTI 1724080: https://www.osti.gov/biblio/1724080 ; Craig (2018), OSTI 1724116: https://www.osti.gov/biblio/1724116
- Fortuna (1995), DOE cost-shared R&D, OSTI 860716: https://www.osti.gov/biblio/860716
- Sass et al. (1999), USGS OFR 99-425: https://pubs.usgs.gov/of/1999/of99-425/webmaps/home.html
- DeAngelo, Burns & Mordensky (2026), USGS: https://www.usgs.gov/publications/conventional-hydrothermal-power-producing-systems-great-basin-usa
- USGS heat-flow data, doi:10.5066/P9BZPVUC: https://www.sciencebase.gov/catalog/item/6297d2fad34ec53d276c5b28
- Argenta Rise, USGS: https://pubs.usgs.gov/publication/70271419
- OpenEI, Thermal Gradient Holes: https://openei.org/wiki/Thermal_Gradient_Holes
- NREL Mining G.O.L.D. (2022): https://docs.nlr.gov/docs/fy22osti/81946.pdf
- GDR PFA portal: https://gdr.openei.org/pfa ; INGENIOUS GDR 1391: https://gdr.openei.org/submissions/1391
- Zanskar on the Volts podcast (2025): https://www.volts.wtf/p/is-there-way-more-conventional-geothermal
- Recalled, not fetched (unverified): GEA (2010) *New Geothermal Terms and Definitions*; AGRCC (2010) Australian Geothermal Reporting Code; CanGEA (2010) Canadian Geothermal Code; Garg & Combs, slimhole-to-big-hole productivity (Geothermics, 1990s); Finger & Blankenship (2010), Sandia *Handbook of Best Practices for Geothermal Drilling*.
