# M28: Commercial and proprietary subsurface data for blind-hydrothermal ML (well data, seismic, MT, gravity, legacy operator archives, data deals)

Slice M28, model track. Date: 23 Oct 2026. This file builds on `../../evidence/D08-commercial-data.md` (Enverus bought the TGS A2D log library on 8 July 2026 for USD 100M + 15M earn-out; A2D revenue USD 27M in 2025; >8M raster logs, >5M logs not in public sources, "basin temperature models"), `../../evidence/D05-confidentiality.md` (release clocks: NV geothermal 5 yr, OR 4 yr, UT/BC 2 yr, BLM indefinite), `M20-tg-and-mining-holes.md` (NBMG 2,002 scanned logs, AMAX/Chevron/Getty TG holes; EGI archive of ~500 reports and 180+ holes), `M08-magnetotellurics.md` and `M09-gravity-magnetics.md` (public MT, gravity, Earth MRI). It does not repeat them.

**Method note.** The shared WebSearch budget for this run (200 calls per turn) was used up before this agent's first query, so no new web searches ran. Everything below comes from (a) primary URLs already fetched and cited by sibling files, and (b) my own background knowledge of the industry. Every claim not backed by a cited URL is marked (unverified). Prices in particular are industry rules of thumb, not quotes. A follow-up turn with fresh search budget should check the items in the "verify next" list at the end.

## Bottom line

For blind hydrothermal in the Great Basin, the commercial data market is mostly the wrong shape. The big vendors (Enverus, which now owns A2D; S&P Global, ex-IHS; Seismic Exchange; Geophysical Pursuit; EDCON-PRJ; Getech/Xcalibur) are built around oil-and-gas basins. They are rich in the Permian, Gulf Coast, Rockies and Williston, and thin in the Basin and Range, where only a few hundred oil wildcats and some 1970s-80s 2D seismic lines exist. The data that actually decides a blind-system label (temperature-gradient holes, MT around producing fields, geothermal well tests, failed-prospect files) is not for sale from any vendor. It sits in four places: (1) operator archives (Ormat, Cyrq, Calpine/Constellation, Terra-Gen, BHE/CalEnergy, Navy Geothermal Program Office, Zanskar, Fervo); (2) orphaned legacy archives of the 1970s-80s explorers (Unocal → Chevron, Phillips, AMAX, Getty, Sunoco, Republic, Hunt), part of which already sits scanned at EGI (Utah) and NBMG (Nevada); (3) contractor files (Zonge, Quantec, GeothermEx → SLB), which contractors cannot resell because clients own the data; and (4) mining-company geophysics and drill logs, which leak into public Canadian NI 43-101 reports. So the edge is not "buy a licence". It is: **buy a narrow oil-and-gas licence where it is cheap and helps (deep BHT/DST in sedimentary and Utah/Nevada basins, legacy 2D seismic across buried range fronts); trade for operator data inside farm-out and option deals; buy or rescue orphaned archives from bankruptcies and retiring geologists; and mine the free-but-illegible state and NI 43-101 files with document AI.** Labels, not features, dominate uncertainty, and our own sensors (drop probe in ranch wells, 2 m probes) make the labels no vendor sells.

## Findings

### F1. Well data with BHT: Enverus and S&P cover the wrong basins for blind hydrothermal, but help in the margins
- Enverus now holds A2D (>8M raster logs, >1.9M LAS, >2M tops/interpretations and "basin temperature models") plus its own Drillinginfo well database and the PDS exchange (D08; https://www.prnewswire.com/news-releases/enverus-acquires-a2d-well-log-library-from-tgs-connecting-subsurface-data-to-energy-decision-workflows-302820900.html).
- S&P Global (IHS Markit merged into S&P in 2022) sells the US well database descended from Petroleum Information, with header BHTs, DST temperatures and recoveries (unverified counts; often quoted as about 4-5M US wells).
- Coverage in Nevada is small. Nevada has produced oil only from Railroad Valley and Pine Valley, and has well under 1,000 oil and gas wells statewide (unverified count; NDOM). Western Utah (Sevier, Black Rock Desert, Great Salt Lake Desert) has a few hundred deep wildcats (unverified). These are high value per well: Pavant Butte 1 had a corrected BHT of 230 +/- 10 C (M04, UGS NGDS summary https://geology.utah.gov/docs/geothermal/ngds/supplemental/summary_report/NGDS_data_summary.pdf). But almost all of them are already in state files and the SMU/NGDS node for free (M04, M05).
- Where the vendors add real value: (a) DST temperatures and recoveries (fluid type, flow, salinity) give permeability and fluid labels, which the free BHT sets mostly lack; (b) digital LAS curves for porosity and lithology; (c) tops; (d) lease and ownership records (Enverus cites 350M+ courthouse records, D08). These matter most for the sedimentary/oil-patch and Utah-basin targets, less for Nevada range-front blind systems.
- Prices (unverified): Enverus and S&P platforms are seat-based subscriptions, roughly USD 20k-100k+ per seat per year, with enterprise deals to seven figures; single LAS curves have historically sold for roughly USD 10-50 each with volume discounts; raster images a few dollars to USD 10 (BEG charges USD 10 per scan, D01/D07). A narrow, field-of-use licence for "all wells deeper than 1,500 m in NV, UT, ID, OR, NM, AZ" would be a few thousand wells, so likely low six figures or less (unverified estimate).

### F2. Seismic libraries: thin in the Great Basin, but legacy 2D across buried range fronts is the cheapest buried-fault data you can buy
- TGS keeps its global seismic library; Geophysical Pursuit Inc. (GPI) and Seitel shoot and license onshore multi-client 3D, almost all in Gulf Coast, Permian, Mid-Continent and Canada (unverified; GPI/Seitel catalogues not fetched). No Great Basin multi-client 3D is known.
- Legacy 2D does exist. Oil companies shot 2D lines in the 1970s-80s across Railroad Valley, Pine Valley, Dixie Valley, the Carson Sink, Sevier Desert and the Utah "hingeline" (unverified line-km). Dixie Valley reflection lines (Southland Royalty era) were reprocessed and used to image the range-front fault and its step-overs (Honjas et al. 1997, unverified citation). INGENIOUS-era work at Gabbs Valley and Granite Springs used seismic reflection among inputs (M02).
- These lines are usually brokered by Seismic Exchange Inc. (SEI) and similar brokers, or still held by successor companies (unverified). A transfer licence for legacy onshore 2D is commonly quoted around USD 1,000-5,000 per line-mile, with reprocessing at a similar cost (unverified rule of thumb). A 50-mile package over one buried basin margin would be roughly USD 50k-250k all in (unverified).
- Model value: reflection seismic is the only data that maps the dip, offset, and step-over geometry of a fault buried under 0.5-2 km of basin fill. That is exactly what INGENIOUS and play-fairway models proxy with gravity gradients. One reprocessed line can turn a fuzzy "fault density" feature into a hard fault trace with a depth.

### F3. MT libraries: there is no commercial MT library to buy; the data belongs to the clients
- Zonge International (Tucson, contractor since 1972) and Quantec Geoscience (Toronto; Titan-24 DC/IP/MT and Spartan MT systems) are acquisition contractors, not multi-client vendors (unverified for Quantec's current offering). Their geothermal and mining surveys belong to the clients who paid for them. They cannot resell them without consent (standard contractor terms; unverified).
- The MT that matters for labels therefore sits in operator files (Ormat, Cyrq, Calpine, Navy GPO, Zanskar, Fervo) and in mining companies' files. M08 already flags "Operator / contractor MT (Ormat, Cyrq, Quantec, Zonge archives)" as proprietary and high value.
- Leak path: Canadian-listed juniors exploring in Nevada (gold, lithium, copper) must file NI 43-101 technical reports on SEDAR+. These reports often show MT/CSAMT/IP sections, gravity and magnetics maps, and drill-hole logs, sometimes with notes of hot water or hot holes (unverified frequency). They are free to read but are scanned PDFs, so they are illegible to most people. The same is true of US SK-1300 technical report summaries filed with the SEC (unverified for geophysics content).
- Contractors as partners: Zonge and Quantec can be hired to acquire. More usefully, a contractor that is paid partly in a carry on prospects could share its knowledge of which surveyed areas were warm (unverified whether either would do this).

### F4. Gravity and magnetics: commercial libraries add little over free USGS + Earth MRI in the Great Basin
- EDCON-PRJ (Denver) is the best-known US commercial land-gravity and magnetics library, built from oil-industry and its own surveys, and sold under non-exclusive licences (unverified size and pricing). Getech sells global gravity/magnetic compilations. CGG's multi-physics airborne business moved to Xcalibur Multiphysics around 2021-22 (unverified); Xcalibur flies airborne gravity gradiometry and had an exclusive airborne mapping partnership in natural hydrogen (A06).
- In Nevada, the free base is already strong: about 71,000 gravity stations statewide and Earth MRI re-flown magnetics and radiometrics over large parts of the Great Basin since 2021 (M09). Earth MRI was boosted by the 2021 Bipartisan Infrastructure Law (about USD 320M over five years, unverified amount) and released 11,079 line-km of HELITEM airborne EM plus magnetics in Sep 2025 (DOI 10.5066/P1UKDJSM; M08).
- The same law funded the National Geological and Geophysical Data Preservation Program (NGGDPP, about USD 23.7M, unverified), which pays state surveys to rescue and scan logs, cores and maps. This keeps pushing more legacy data into free state portals.
- Commercial airborne gravity gradiometry (Xcalibur FALCON-type or Bell Geospace) resolves basin-margin faults better than ground gravity at 2 km spacing. A custom survey costs roughly USD 100-200 per line-km (unverified). It is a "buy acquisition" decision, not a "buy library" one.

### F5. The proprietary geothermal datasets that matter, who holds them, and how they leak

| Holder | What they likely hold | How to get at it | Notes |
|---|---|---|---|
| Ormat (about 20+ NV/CA/UT fields; largest BLM lessee) | Decades of TG holes, MT, gravity, slim holes, failed prospects, production data | Farm-out data rooms; JV where we bring land; state releases after 5 yr (NV) | Ormat is a buyer for us; data is a deal currency (inference) |
| Cyrq Energy | Patua, Soda Lake, Thermo 1, Hudson Ranch; Lightning Dock (sold to Zanskar 2024); Blue Mountain (sold to Ormat 2025 for USD 88.7M) (Z08) | Asset sales carry data rooms; Cyrq is a seller of mid-size assets (Z08) | Data travels with asset sales |
| Calpine (now Constellation, closing reported early 2026, unverified) | The Geysers: thousands of wells, decades of microseismicity | Much is public: CalGEM well files; LBNL Geysers seismic network via NCEDC | Not a blind target, but the best labelled vapour-dominated analogue |
| BHE / CalEnergy (Salton Sea, Coso partner) | Salton Sea wells; inherited Magma Power and some Phillips-era data (unverified) | Lithium-brine partnerships, CalGEM | Phillips/CalEnergy files flagged as "unreleased" in M20 |
| Unocal → Chevron (2005) | Unocal was the largest US geothermal explorer of the 1970s-80s (Geysers, Salton Sea, Valles/Baca, many Basin and Range prospects). Chevron sold its Indonesia and Philippines geothermal in 2016-17 (unverified) | Some Unocal/Union data was donated to UURI/EGI or released through DOE programs (unverified). The rest may sit in Chevron archives | NBMG already lists 187 Chevron logs (M20). A request to Chevron's archive or a university donation is a realistic ask |
| Phillips, AMAX, Getty, Sunoco, Republic, Hunt (1970s-80s explorers) | Phillips 623 TG holes and Chevron 83 across 82 prospects (L16/M20) | Partly scanned at EGI (~500 reports, 180+ holes) and NBMG (773 logs on 442 industry TG boreholes, 0 LAS) | Free but illegible: document AI is the unlock |
| Navy Geothermal Program Office (China Lake) | Coso; exploration on DoD lands (NAS Fallon, Hawthorne, Mountain Home etc.) | Much published to GDR and GRC papers (unverified extent) | Good labelled data around military land |
| GeothermEx (acquired by Schlumberger, now SLB, 2008, unverified) and other consultants (Thermochem, Black Mountain Technology) | Client reports worldwide, decades | Client-owned; not saleable; knowledge transfer via hiring retired staff | Retired consultants' personal files are a real, informal source (inference) |
| Zanskar, Fervo, Open Mountain Energy | 2021-2026 TG holes, MT, wells | NV 534A.031 opens them 5 yr after filing, about 2026-2031 (D05); DOE-funded parts go to GDR | Calendar-driven, free |
| Bankrupt or exited developers (Raser Technologies 2011; Nevada Geothermal Power; Gradient Resources; Magma Energy/Alterra; US Geothermal, bought by Ormat 2018) (unverified details) | Prospect files, TG holes, leases | Bankruptcy asset sales, liquidators, ex-staff | Data is often abandoned or sold cheaply (inference) |

### F6. Data-sharing deals and public-good channels
- DOE GTO-funded work must deposit data in the Geothermal Data Repository (GDR: 1,423 datasets, 146 providers, 764 TB; https://gdr.openei.org/). This is how INGENIOUS, Play Fairway, FORGE and some Zanskar/Fervo DOE grant data become public. It is the biggest free channel for industry-quality data.
- The DOE Industry-Coupled Program (1977-82, 14 NV/UT sites) required release for unrestricted use; it is scanned on OSTI/UNT (L16, M20).
- State release clocks (NV 5 yr, OR 4 yr, UT/BC 2 yr) open each operator's filings on a schedule (D05). This is a free, predictable, rolling "data deal".
- Zanskar open-sourced GeoCore (LightGBM on INGENIOUS layers), but not its proprietary labels (M13). Its moat is its own wells and its large-N compilation, not features.
- Project InnerSpace GeoMap is free with 150+ layers; it commoditises regional temperature but does not include operator labels (D08).
- Farm-out data rooms are the standard industry trade: a developer shows TG and MT data to a farm-in partner under NDA. A land bank that offers its acreage can ask to see the counterparty's nearby data as part of the deal (common practice in oil and gas; for geothermal, inference).

### F7. What this means in money terms
- A2D, the biggest North American log library, earned about USD 27M per year and sold for about USD 100-115M (D08). Selling data is a small business. Buying it is cheap relative to drilling: a 300 m TG hole costs roughly USD 150k-500k (L16/M20 ranges, unverified), so a licence for a few thousand western deep wells plus a few legacy 2D packages, at well under USD 1M total, is the price of two or three TG holes.
- The best label data (operator TG holes and failed prospects) cannot be bought at any price today; it is reached by deals, by state release clocks, or by our own sensors.

## Datasets table

| Dataset | Access and price | Coverage | Value for blind detection |
|---|---|---|---|
| Enverus (incl. A2D since July 2026): headers, BHT, DST, LAS, tops, basin temperature models, land/ownership | Subscription, ~USD 20k-100k+/seat/yr; per-curve LAS (unverified) | All US producing basins; thin in NV/West UT | Medium in Utah basins and oil-patch sedimentary plays; low for NV range fronts. DST fluid/flow labels are the unique part |
| S&P Global (ex-IHS / Petroleum Information) US well data | Enterprise licence, six to seven figures for large users (unverified) | US and international | Same as Enverus; strong international coverage for the "and beyond" plan |
| MJ Logs, Neuralog, BEG scans | Per image/curve; BEG USD 10/scan (D01, D07) | 3M wells (MJ), Texas (BEG) | Oil-patch heat; marginal for Great Basin |
| Legacy 2D seismic via Seismic Exchange Inc. and successor holders | Transfer licence ~USD 1k-5k/line-mile + reprocessing (unverified) | Railroad Valley, Dixie Valley, Carson Sink, Sevier Desert, Utah hingeline (unverified line-km) | High per dollar: hard buried-fault geometry and basin depth at specific targets |
| GPI / Seitel / TGS onshore multi-client 3D | Licence per km2 (unverified) | Gulf Coast, Permian, Mid-Con | None for Great Basin; useful only for sedimentary EGS plays |
| EDCON-PRJ gravity/mag library | Non-exclusive licence (unverified) | US, oil-basin heavy | Low to medium; free NV gravity + Earth MRI mostly covers it |
| Getech global potential fields; Xcalibur (ex-CGG) airborne | Licence / custom survey ~USD 100-200/line-km (unverified) | Global | Medium for "and beyond"; custom AGG over targets is high value |
| Earth MRI mag, radiometrics, AEM, lidar, hyperspectral | Free (USGS) | Large and growing parts of NV, OR, CA, UT | High; the cheapest new feature layers (M08, M09) |
| NGGDPP-funded state scans (NBMG, UGS, others) | Free | Growing state archives | High once read with document AI |
| EGI/UURI archive (Unocal/Phillips-era) | Free/visit; scanned | Utah and beyond; ~500 reports, 180+ holes | Very high labels |
| NBMG WellLog service | Free, PDF | 2,002 logs; 773 on 442 industry TG holes | Very high labels (M20) |
| Operator archives (Ormat, Cyrq, Calpine, BHE, Navy GPO, Zanskar, Fervo) | Not for sale; farm-out NDA, asset sale, state release clock | Field-level | Highest: true positives, true negatives, size |
| Contractor archives (Zonge, Quantec, GeothermEx/SLB) | Client-owned; not resaleable | Many fields | Indirect only (knowledge, hiring) |
| NI 43-101 (SEDAR+) and SK-1300 (SEC) mining technical reports | Free, scanned PDFs | Hundreds of NV/UT/AZ projects (unverified count) | Medium-high: MT/IP/gravity sections and drill notes over unexplored ground |
| Bankrupt/exited geothermal company files | Bankruptcy sale or ex-staff (inference) | Dozens of prospects | High, cheap when found |

## What dominates uncertainty (from this slice)
1. **Labels, not features.** Commercial data mostly sells features (logs, seismic, gravity). Blind-system uncertainty is dominated by the shortage and bias of labels: deep temperature and permeability truth at known-negative and known-positive places. The best labels are in operator and legacy archives that are not for sale.
2. **Missing-not-at-random negatives.** Failed prospects (Phillips/Chevron/AMAX grids that "were not hot enough") are under-reported. Without them the model over-predicts near faults.
3. **Buried fault geometry.** Gravity gradients blur fault dip, step-overs and terminations. Legacy 2D seismic exists on only a few basin margins.
4. **Unknown size of hidden archives.** We do not know how much Unocal/Chevron, Phillips/CalEnergy or bankrupt-company data survives (unverified); that unknown is itself a large part of the uncertainty about what is "blind" versus "known to someone".
5. **Leakage of private knowledge.** Some "blind" cells in our model are already known to Ormat or Zanskar. Their lease and drilling footprints (BLM LR2000/MLRS, NDOM permits) are the only public shadow of that knowledge.

## What a sensor could fill
- **Labels where no archive exists.** The ranch water-well drop probe (T, P, conductivity) and the 2 m temperature probes create cheap temperature labels on private land between the public TG-hole clusters. They are the substitute for the operator TG data we cannot buy.
- **Negatives.** Systematic probe surveys of "model says hot" cells that come back cold create the honest negative set that commercial and public data lack.
- **Ground truth for licensed features.** A drop-probe log in a ranch well next to a licensed oil wildcat BHT calibrates the BHT correction locally (M04).
- **MT where none can be bought.** E-field-only MT nodes give the clay-cap / conductor picture that sits unsold in Zonge/Quantec client files.
- **Fault geometry without seismic.** Dense passive seismic nodes (ambient noise, M12) or drone magnetics can map buried faults where no legacy 2D exists, at lower cost than new reflection lines.
- **A new idea: a document-AI "sensor".** A scanning and extraction pipeline over EGI, NBMG, NI 43-101 and bankrupt-company paper is the cheapest "instrument" for labels. A rugged portable scanner rig (sheet-fed plus large-format, with on-device OCR) that a field person carries into county offices, university archives and retired geologists' garages turns paper into labels on the spot. It is a physical thing that can be built (inference).

## Implications for a better model
1. **Buy features narrowly, chase labels hard.** Licence only (a) all deep wells in NV, UT, ID, OR, AZ, NM with DST and BHT from Enverus or S&P, and (b) legacy 2D seismic across the top 10-20 buried range-front targets. Budget under about USD 1M (unverified prices). Spend the real effort on labels.
2. **Add a "data provenance" feature and a leakage mask.** Mark each cell by whether an operator is known to have drilled or leased nearby (MLRS, NDOM permits, CalGEM). Treat those cells as "known to someone" and down-weight their value as blind bets.
3. **Make DST data first-class labels.** DST recoveries (water, flow rate, salinity, temperature) are permeability-plus-temperature labels. Encode them as censored observations next to TG holes (M20 approach).
4. **Use legacy 2D seismic to replace fault-density proxies at the top targets.** Interpreted fault planes with dip and depth become explicit inputs to the fault-scenario prior (M13, M15).
5. **Build a rolling ingestion queue.** Track NV/OR/UT/BC release dates (D05), new GDR submissions, Earth MRI releases, NGGDPP scans and new NI 43-101 filings. Re-score cells as new labels arrive. Be first to read each release.
6. **Trade data in deals.** Every option or farm-out with Ormat, Cyrq or others should include a data-access clause for nearby TG/MT data. Over time this builds a private label set like Zanskar's, without drilling every hole ourselves.
7. **Buy dead archives.** Watch bankruptcy dockets and retiring-consultant estates for geothermal and mining exploration files. Price is usually low (inference); value as labels is high.
8. **Do not build a data-selling business.** A2D shows selling logs caps out near USD 27M/yr revenue (D08). Data is an input and a deal currency, not the product.

## Verify next (needs fresh search budget)
- Enverus and S&P actual pricing for a geothermal field-of-use licence; whether Enverus has launched a geothermal or "subsurface heat" module since July 2026.
- Seismic Exchange / successor holdings of Great Basin 2D lines, with line-km by basin.
- Whether Quantec or Zonge offer any multi-client or data-licensing product.
- Current owner of CGG's multi-physics library (Xcalibur) and EDCON-PRJ library size.
- Fate of Unocal geothermal exploration files after Chevron (2005) and the 2016-17 asset sales.
- Earth MRI and NGGDPP funding after FY2026.

## Sources
- Enverus acquisition of A2D: https://www.prnewswire.com/news-releases/enverus-acquires-a2d-well-log-library-from-tgs-connecting-subsurface-data-to-energy-decision-workflows-302820900.html
- TGS sale release: https://www.tgs.com/press-releases/tgs-sells-north-american-well-data-products-business-to-enverus ; https://www.tgs.com/well-data
- DOE Geothermal Data Repository: https://gdr.openei.org/
- UGS NGDS data summary (Pavant Butte 1, wells of opportunity): https://geology.utah.gov/docs/geothermal/ngds/supplemental/summary_report/NGDS_data_summary.pdf
- NBMG WellLog NGDS service: https://web2.nbmg.unr.edu/arcgis/rest/services/NV_Data/NVWellLogs/MapServer/0
- Earth MRI AEM Basin and Range (DOI 10.5066/P1UKDJSM): https://www.usgs.gov/index.php/data/regional-airborne-electromagnetic-and-magnetic-surveys-basin-and-range-province-nevada-oregon
- DOE Industry-Coupled era report (UNT): https://digital.library.unt.edu/ark:/67531/metadc1055320/m2/1/high_res_d/5053058.pdf
- Project InnerSpace GeoMap: https://geomap.projectinnerspace.org/
- Cyrq Energy: https://www.cyrqenergy.com/
- Sibling evidence (same repo): D01, D05, D07, D08, L16, Z08, A06, M02, M04, M05, M08, M09, M12, M13, M20.
- All vendor pricing, Seismic Exchange / GPI / Seitel / EDCON-PRJ / Getech / Xcalibur / Zonge / Quantec / GeothermEx / Unocal-Chevron archive statements are from background knowledge and are (unverified).
