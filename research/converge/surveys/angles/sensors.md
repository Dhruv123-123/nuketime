## Airborne survey cost: can a new sensor make it 10x cheaper?

### Short answer
- **No single new sensor gets airborne survey cost down 10x.** Magnetics and radiometrics are already cheap. The expensive part is the helicopter EM, and most of that money goes to the helicopter, mobilisation and standby, not the sensor.
- **The most plausible route is drone-borne passive EM plus drone mag/radiometrics, possibly with several small surveys sharing one mobilisation.** That could be roughly 3x to 10x cheaper for the small claim blocks juniors usually fly (about 150–500 line-km). For large blocks over 1,500 line-km it is closer to 1.5x to 2x. All of these multiples are my estimates.
- **The other methods on the list don't replace the airborne survey.** Ambient-noise seismic, muon tomography, SQUID receivers and quantum magnetometers are either follow-up tools that cost more per km², or they don't change what drives the cost.

### 1. What the current survey costs (sourced figures)
| Survey | Size | Cost | Per line-km |
|---|---|---|---|
| Aeroquest AeroTEM helicopter TEM + mag, BC, about 2006 | 1,070 line-km | C$173,400 total | C$125/km, plus C$17,000 mobilisation and C$2,000/day standby; about C$162/km all-in |
| Geotech VTEM, Melkior, Ontario, 2010 | 1,765 line-km | about C$300,000 | about C$170/km |
| ZTEM (passive), Babine BC, 2010 | 484 line-km | C$97,255 | C$200.94/km |
| ZTEM, Goose 1 BC, 2016 (added onto a larger job, so no mobilisation) | 41 line-km | C$5,945 + C$1,000 report | C$145/km |
| MobileMT (passive), Orestone, 2026 | 157 line-km, 26 km², 200 m line spacing | about C$112,000 (estimated) | **about C$713/km, because fixed costs dominate a small survey** |
| AEM guideline, Nebraska groundwater, 2014–2020 | n/a | n/a | US$500/line-km used as the maximum all-in target (includes processing and interpretation) |
| Crewed aeromagnetics, large blocks (vendor claim) | 1,000–5,000 line-km minimum | mobilisation US$50–150k | US$30–80/km |
| Drone magnetometer (vendor claim) | 50–300 line-km/day | mobilisation US$5–25k | US$150–600/km |
| NeoCore uranium project, 13,012 ha, 2026 technical-report budget | n/a | airborne mag C$200k, ground EM C$200k, ground gravity C$150k | n/a |

- **Modern helicopter TEM rate:** probably C$180–300/km plus C$20–50k mobilisation (estimate). This is the 2006–2010 rates of C$125–170/km adjusted for inflation; I found no published 2023–2026 rate.
- **Coverage per km²:** at 200 m line spacing a survey flies about 5.4 line-km per km². F4's Wales Lake VTEM is an example: 1,031 line-km over 191 km². That puts helicopter TEM at roughly C$1,000–1,600/km² (estimate).
- **The founder's figure of about US$100k matches a typical small junior survey:** roughly 300–500 line-km at C$200–300/km including mobilisation (estimate).
- **Typical Athabasca survey sizes (helicopter TEM):** 136, 365, 916, 1,031, 1,421, 1,670 and 5,200 line-km.
- **Typical sizes for the alternatives:**
  - MobileMT: 771, 1,097, 1,536, 1,781, 2,900 and about 5,000 line-km.
  - ZTEM: 618 and 1,487 line-km, at 400 m spacing.
  - Fixed-wing gravity gradiometry (Falcon): 1,838 and 2,843 line-km.
- **Where the cost sits:** fixed costs (mobilisation, standby, minimum charges) dominate small surveys. Orestone paid about C$713/km for 157 km, against about C$170/km for 1,765 km of VTEM. That gap, not the sensor, is the main problem.
- **Market size:** Saskatchewan uranium exploration spending was C$149M in 2022 and about C$200M expected for 2024. All Saskatchewan exploration was C$357M in 2023 and over C$410M intended for 2024. Airborne geophysics is probably 5–15% of that (estimate). The addressable market in Saskatchewan alone is therefore only about C$10–30M a year (estimate), so a venture would need to sell globally.

### 2. Each method assessed
| Method | Depth for Athabasca targets | Cost against helicopter TEM | Could it be 10x cheaper? |
|---|---|---|---|
| **Passive / natural-field EM (ZTEM, AFMAG, MobileMT)** | ZTEM was tested over conductors at about 450–800 m. MobileMT claims 1–2 km (Foremost release). Many new targets sit under more than 500 m of sandstone, where helicopter TEM loses resolution. A 2015 AGU abstract judged AFMAG the better airborne option | Per km about the same: C$145–201/km for ZTEM. It can fly 400 m spacing instead of 200 m, so about 2x cheaper per km². Still towed by a helicopter | **No, about 2x.** It is the right physics for depth, but it doesn't remove the helicopter |
| **Drone-borne passive EM (MobileMT drone)** | Founder claims the lowest frequency of any airborne system, so the deepest. A prototype flew in 2023, and A.I.S. Resources' 2026 budget (about C$300k) covers drone MobileMT plus IP | Mobilisation could fall from C$20–150k to C$5–20k (estimate). No helicopter fuel or standby | **The best candidate. About 3–10x on small blocks** (estimate; no published price yet) |
| Drone TEM (ground transmitter, drone-towed receiver; SibGIS, AIRCAS) | 50–300 m in published trials, including a uranium paleovalley target | Low hardware cost | **No for the Athabasca.** It can't see deep enough under 500 m or more of cover |
| Quantum / optically pumped / diamond magnetometers (SBQuantum, GEM potassium) | Magnetics only | Magnetics already cost US$30–80/km crewed | **No.** It doesn't touch the EM cost |
| SQUID B-field receivers | Ground SQUID TEM is the standard for deep Athabasca follow-up. In airborne trials (BHP/CSIRO, 2001) SQUIDs were "comparable with, but not superior to" induction coils | Adds cryogenics | **No** |
| Lighter EM transmitters | Depth scales with transmitter moment, so lighter means shallower | Small savings | **No** |
| Airborne gravity gradiometry (Falcon) | Detects low-density alteration (clay) zones; used at Geikie and South Falcon Point | Price not published. Covers more than 2,000 km² a week from a fixed-wing aircraft | Complements EM rather than replacing it |
| Satellite / hyperspectral / InSAR | The deposits lie under hundreds of metres of sandstone and glacial till. Only structure and boulder trains show at the surface (my assessment; not sourced) | Very cheap | **No.** Useful for screening only |
| Ambient-noise seismic (Fleet Space ExoSphere) | 1.2 km at IsoEnergy's Hurricane over about 34 km² (June–Sept 2023). Fleet claims 2.5–4 km. Drilling confirmed the alteration it imaged | Standard Uranium paid C$525k in shares for its partnership; Astute paid A$400k in shares. That works out to roughly C$5–15k/km² (estimate), about 10x **more** than airborne per km² | **No.** It is a follow-up step before drilling. Fleet raised US$100M (Series D) at a US$525M valuation and has run more than 250 surveys |
| Muon tomography (Ideon) | About 1 km, but detectors must go down boreholes or underground. Trialled at Orano's McClean Lake, 200 m target | Needs an existing drill hole | **No.** It comes after drilling. Series A was US$16M (2022) |

### 3. Venture implications
- **A 10x cut needs three things together:**
  - A drone platform, which removes the helicopter, the pilot and standby.
  - A passive natural-field receiver, which removes the heavy transmitter and reaches 1–2 km.
  - Pooled campaigns, where many small claim blocks share one mobilisation, so cost per km approaches large-survey rates.
- **What it might look like:** C$50–150/km all-in for a 300 km block, about C$15–45k total, against about C$100–200k by helicopter TEM. That is 3–10x, and it is an estimate.
- **Who is already moving:** Expert Geophysics, which owns MobileMT, has the drone prototype and has flown more than 70,000 line-km across more than 70 projects since 2018.
- **Risks:**
  - The incumbent may simply commercialise the drone version first.
  - Passive EM resolves thin, steep graphitic conductors less sharply than TEM, so it might add a ground-EM step instead of replacing one (my assessment).
  - Regulator approval for drones flown beyond visual line of sight in northern Saskatchewan (not researched).
  - Natural-field signal is weak in winter at high latitudes (my assessment; not sourced).

### Gaps
- I found no published modern (2023–2026) helicopter TEM rate per line-km and no ExoSphere price per km². Both are inferred and marked as estimates.
- The shared search quota ran out before I could look into ZTEM Athabasca depth results, SkyTEM/Xcite rates, or the Saskatchewan assessment-file invoices. A follow-up pass could fill these in.

### Sources
- https://apps.nrs.gov.bc.ca/pub/aris/Report/28538.pdf/ (AeroTEM C$125/km, C$17k mobilisation, C$2k/day standby)
- https://apps.nrs.gov.bc.ca/pub/aris/Report/32356a.pdf/ (ZTEM 484 km at C$200.94/km)
- https://apps.nrs.gov.bc.ca/pub/aris/Report/37100.pdf/ (ZTEM C$145/km, 2016)
- https://geotech.ca/melkior-completes-vtem-survey-at-ring-of-fire/ (1,765 km about C$300k)
- https://www.streetwisereports.com/article/2026/06/17/orestone-mining-advances-captain-project-with-mobilemt-survey-amid-rising-gold-prices.html (MobileMT 157 km, C$112k)
- https://middleeastnewscenter.com/article/896832859-a-i-s-resources-corporate-update (drone MobileMT + IP, about C$300k budget)
- https://snr.unl.edu/csd/download/geology/geocloud/guidelines/NGC_Guidelines_v1_0.pdf (US$500/line-km maximum)
- https://skymineral.com/knowledge/how_much_does_a_drone_magnetometer_survey_cost_per_km_in_2026.php
- https://newsfile.moomoo.com/public/NN-PersistNoticeAttachment/7781/20260620/SEDAR_PLUS/CSA_SEDAR_PLUS_NOTICE_RECORD_ID_2438449.pdf (NeoCore budget)
- https://f4uranium.com/wp-content/uploads/2026/05/F4-MDA-Q2-2026-FINAL.pdf (VTEM 1,031 km / 191 km²; MobileMT 1,097 km)
- https://greenridge-exploration.com/greenridge-exploration-identifies-uranium-targets-from-airborne-electromagnetic-survey-at-the-mckenzie-lake-uranium-project-in-northern-saskatchewan/
- https://www.globenewswire.com/news-release/2023/05/10/2665484/0/en/Traction-Uranium-and-Forum-Energy-Metals-Commence-Airborne-Geophysical-Survey-on-the-Grease-River-Project-Athabasca-Basin.html
- https://www.juniorminingnetwork.com/junior-miner-news/press-releases/895-tsx-venture/cvv/162853-canalaska-starts-airborne-surveys-at-frontier-project-in-northeastern-athabasca-basin.html
- https://stallionuranium.com/stallion-discoveries-highlights-uranium-target-areas-from-airborne-vtem-data-outlines-exploration-plan-in-the-western-athabasca-basin/
- https://www.globenewswire.com/news-release/2025/07/07/3111087/0/en/Foremost-Clean-Energy-to-Deploy-District-Scale-MobileMT-Survey-Over-its-GR-and-Blackwing-Uranium-Properties.html
- https://www.newsfilecorp.com/release/212643/Forum-Energy-Metals-and-Traction-Uranium-Commence-Airborne-MobileMT-Survey-on-the-Grease-River-Project-Athabasca-Basin
- https://www.globenewswire.com/news-release/2025/04/30/3071257/0/en/greenridge-exploration-completes-airborne-mobilemt-survey-at-the-sabre-uranium-project-in-athabasca-basin-saskatchewan.html
- https://www.globenewswire.com/news-release/2025/09/17/3151582/0/en/Global-Uranium-Corp-Reports-Results-of-Airborne-ZTEM-Survey-at-Astro-Project-Athabasca-Basin.html
- https://publish.csiro.au/ex/ASEG2009AB054 (ZTEM uranium tests)
- https://agu.confex.com/agu/seg15/webprogram/Paper37925.html (Athabasca EM evolution; AFMAG vs SQUID)
- https://www.seequent.com/introducing-next-level-airborne-survey-technology-using-the-latest-in-geophysics-innovation/
- https://projects.gbreports.com/ontario-mining-2024/expert-geophysics-and-axiom-exploration-interviews
- https://www.mdpi.com/2075-163X/15/6/630 (drone TEM, uranium paleovalley)
- https://english.aircas.ac.cn/newsroom/focus/202607/t20260720_1178679.html
- https://publish.csiro.au/eg/EG01009 (SQUID airborne TEM)
- https://metaltechnews.com/story/2024/03/06/mining-tech/quantum-leap-for-mineral-exploration/1655.html (SBQuantum drone)
- https://www.gemsys.ca/uavs-pathway-to-the-future/
- https://canalaska.com/canalaska-reports-large-gravity-targets-identified-at-geikie-project-in-athabasca-basin/
- https://www.jotup.co/node/1936472 (South Falcon Point gravity gradiometry)
- https://www.globenewswire.com/en/news-release/2015/06/03/1631666/0/en/CGG-CGG-launches-lowest-noise-FALCON-Plus-airborne-gravity-gradiometry-technology.html
- https://www.standarduranium.ca/_resources/news/2025/nr_20250618.pdf (Fleet Space C$525k)
- https://www.fleetspace.com/resources/imaging-alteration-in-the-athabasca-basin-with-ambient-noise-tomography
- https://www.fleetspace.com/fermiexploration
- https://mining.com.au/astute-and-fleet-space-launch-exosphere-ant-survey-at-georgina/
- https://otpp.com/en-ca/about-us/news-and-insights/2024/fleet-space-closes-usd-100m-series-d-with-usd-525m-valuation/
- https://smallcaps.com.au/article/ideon-technologies-muon-tomography-global-transition-low-cost-mining
- https://techcrunch.com/2022/09/19/ideon-technologies-digs-up-16m-series-a-to-use-particle-physics-to-find-critical-minerals
- https://www.saskatchewan.ca/government/news-and-media/2024/december/03/53rd-geological-open-house-highlights-saskatchewans-leadership-in-critical-minerals
- https://publications.saskatchewan.ca/api/v1/products/81262/formats/93218/download
- https://pipelineonline.ca/saskatchewan-funding-aero-magnetic-survey-in-southwest-sask-to-drive-further-critical-mineral-development/
