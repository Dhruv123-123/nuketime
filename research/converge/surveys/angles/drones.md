## Findings: drones as a replacement for helicopter surveys (Athabasca uranium)

**Bottom line:** Drones have made magnetics cheaper for small, tight-spaced blocks, and radiometrics too. They have **not** cut the cost of the deep EM that matters for Athabasca uranium. Fully airborne drone TEM systems carry about 150–3,000x less transmitter moment than helicopter TDEM, and their published depth reach is tens to about 100 m. Uranium targets sit 480–1,000 m deep. The only drone routes that might reach that depth are semi-airborne EM (transmitter on the ground, receiver on the drone) and passive natural-field EM (Expert Geophysics' drone MobileMT, called MobileMTd). Both are still prototypes or research and are not yet commercial. That gap is the open opportunity.

### 1. Cost per line-km: drone vs helicopter (real numbers)
| Item | Figure | Source |
|---|---|---|
| Drone magnetics, invoiced (Pioneer, Ontario 2022, 56.7 line-km) | C$6,190 survey = **C$109/line-km** acquisition, plus **C$2,500 mob/demob**, so **C$153/line-km all-in** | Ontario assessment report 20000020702 |
| Drone magnetics, vendor guide 2026 | US$150–600/line-km all-in (typically $200–400). Over 5,000 line-km: $120–180. Mob $5k–25k vs $50k–150k for crewed aircraft. Minimum practical job 50–100 line-km for drone vs 1,000–5,000 for crewed. Drone 50–300 line-km/day vs crewed 1,000–2,000/day | skymineral.com (vendor content, low reliability) |
| Helicopter EM + mag, invoiced (AeroTEM, Berg BC, 2010, 754 line-km at 100 m spacing) | C$99,894 total = **C$132/line-km, EM included** | BC ARIS 32307 |
| AEM cost ceiling used 2014–2020 | US$500/line-km maximum target | Nebraska AEM guidelines |
| Academic model (assumptions only) | Multirotor $1.38/km and $500/day; Bell 206 helicopter $10/km and $12,000/day; aircraft $20k vs $2.1M | arXiv 2402.11797 |

**Key insight:** per line-km, drone magnetics alone (about C$110–150) costs **about the same as helicopter EM plus magnetics** (about C$130). Drones win on mobilisation, small jobs (under 300 line-km), tight spacing (20–50 m) and low flying height. They do not win on cost per km at the scale of a uranium property. The founder's figure of about US$100k matches roughly 500–1,000 line-km of helicopter TDEM (estimate). Typical Athabasca helicopter TDEM jobs:
- Corvo: 1,380–1,670 line-km
- Grease River: 1,290 line-km
- Reynolds: 1,100 line-km
- McKenzie Lake: 365 line-km
- Dutton: 263 line-km
- 914W: 136 line-km

Most use 100–200 m line spacing and 1,000 m tie lines, and Axiom's Xcite system is the main contractor setup.

### 2. Depth of investigation: why drones fail for deep uranium EM
- **Helicopter moments:** SkyTEM 306HP and 312HP reach about 500,000 and 1,000,000 Am². VTEM-Max reaches about 400 m depth vs about 200 m for VTEM-ET. Xcite uses a 20 m inflatable transmitter loop towed about 30 m below the helicopter.
- **Fully airborne drone TEM systems** (comparison table, egusphere-2026-4378):

| System | Transmitter moment | Weight |
|---|---|---|
| SkyTEM21HR | 3,480 Am² | 150 kg (needs a 300 kg heavy-lift drone; Denmark tests 2023) |
| Jilin TEM-31 | 360 Am² | 8 kg |
| Chinese Academy of Sciences UAV-HTEM-5M | 2,250 Am² | 14.94 kg; targets within **50 m** depth |
| Chongqing Wukong | 80,000 Am² | single component, used for mine-void detection |

  SkyTEM's Diamond system (4 m frame, carried by helicopter or drone) is aimed at near-surface work.
- **Athabasca target depths:** Cigar Lake 480 m, McArthur River 530 m, Cosa's Ursa unconformity 850–1,000 m. Even helicopter TDEM is sometimes blocked by conductive cover in the sandstone (Grease River), which led the operator to fly a follow-up MobileMT survey.
- **Semi-airborne EM (ground transmitter, drone receiver):**
  - The DESMEX project targets about 1,000 m, but its drone versions have "shallower penetration than helicopter-towed" systems.
  - A 2025 *Geophysics* paper imaged a sulfide body to more than 300 m.
  - With a ground loop the reach is about 100 m; with a bipole source about 200 m (JpGU 2023).
  - Radai's Louhi system (Finland) is frequency-domain (2.3/4.6/9.2 kHz) with a 100 m ground loop, used in GTK's DroneSOM project.
  - Laying ground transmitters in roadless northern Saskatchewan needs crews and probably helicopter support anyway (estimate).
- **Passive drone EM (MobileMTd):** natural-field MT, so no transmitter moment is needed. It claims 1–2 km or more of depth and its lowest frequency is the lowest of any airborne system. It was in prototype in 2023–24, with a 2026 conference abstract showing Western Australia field examples. Expert Geophysics calls the Athabasca "particularly active". There is no public pricing or commercial launch. **This is the most credible drone path to deep uranium conductors.**
- **Industry vendor claim:** Rosor says its drone EM reaches 1,000 m and offers up to 75 kg payload, 315–500 line-km/day magnetics and a 4,000 line-km Gull River job. The EM system type is not disclosed and the claims are unverified.
- **Drone radiometrics** (Medusa MS-350/MS-1000 on a DJI M350) see only the top ~50 cm of ground. Altomaxx flew one at a Labrador uranium deposit at about 2 m/s, a vendor case study without costs. Usefulness is low under Athabasca glacial cover and sandstone.

### 3. Adoption numbers
- **Drone magnetics is mainstream:**
  - Apex flew 20,000+ line-km in 2025 (Türkiye and Africa).
  - Pioneer's largest contract was 3,000+ line-km for Géophysique TMC in 2018.
  - Puma Exploration flew 2,800 line-km in 2026.
- **Athabasca drone magnetics:**
  - Skyharbour Moore, 402 line-km at 20 m spacing (Pioneer, 2019).
  - Codrus Jasper Wedge, 224 line-km at 100 m spacing, flown by Axiom on a DJI M300 with a GEM GSMP-35U magnetometer (2024).
- **Drone EM is rare:** 5 of 59 studies in a 2025 *Drones* review. No commercial drone EM survey in the Athabasca was found.
- **Small business scale:** Global UAV, Pioneer's parent, had quarterly revenue of C$537k (Q2 2018), and its market cap was under C$20M.
- **Market size:** drone magnetometer market estimated at US$0.3–0.4B (2025) growing to $0.7–1.1B (2034). These come from a vendor research site, so treat as low reliability.

### 4. BVLOS regulation
- **Transport Canada:** the Phase 1 certificates opened 1 Apr 2025; the rules took effect **4 Nov 2025**.
  - Lower-risk BVLOS no longer needs a Special Flight Operations Certificate (SFOC) for small drones and medium drones (25–150 kg).
  - Conditions: uncontrolled airspace, below 122 m, away from aerodromes. Medium drones must stay at least 1 km from a populated area (over 5 people/km²).
  - Pilots need a Level 1 Complex certificate: 20 h ground school, a C$50 exam, a flight review and a C$125 certificate. Operators need an RPAS Operator Certificate (RPOC), C$125.
  - Drones over 150 kg still need an SFOC.
  - Northern Saskatchewan mostly qualifies, so this is favourable for drones there.
- **FAA Part 108:** the final rule has been at OIRA (the White House review office) since 10 July 2026 and was still unpublished as of September 2026. The open dispute is right-of-way over crewed aircraft. Part 107 waivers are still required today.
- **CASA (Australia):** a trial under TMI 2025-03 started 15 Oct 2025. It offers four broad-area BVLOS pathways for drones up to 25 kg, only for holders of a ReOC (remote pilot operator certificate), with 12-month approvals.

### 5. Implications for a new venture
- Drone magnetics is commoditised, low-margin services work, already priced near helicopter EM per km. **Do not build there.**
- The unsolved problem is **deep (300–1,000 m) conductor mapping without a helicopter**. Candidate routes:
  - Passive MT/AFMAG on drones, where MobileMTd is the incumbent prototype.
  - Semi-airborne EM with drone-deployed or autonomous ground transmitters, plus swarms of receiver drones.
  - Heavy-lift drone TDEM with much larger moments, constrained by battery power and the 150 kg SFOC line.
- Canada's Nov 2025 BVLOS rules make northern Saskatchewan one of the friendliest places to fly them.
- The physics limit is moment: depth grows only weakly with moment (estimate). A drone would need over 100,000 Am² to match helicopter depth, which is impractical on battery power today (estimate).

### Sources
- https://prd-0420-geoontario-0000-blob-cge0eud7azhvfsf7.z01.azurefd.net/lrc-geology-documents/assessment/20000020702/20000020702_01.pdf
- https://aris.empr.gov.bc.ca/ArisReports/32307.PDF (BC ARIS 32307, Berg AeroTEM)
- https://skymineral.com/knowledge/how_much_does_a_drone_magnetometer_survey_cost_per_km_in_2026.php
- https://snr.unl.edu/csd/download/geology/geocloud/guidelines/NGC_Guidelines_v1_0.pdf
- https://arxiv.org/pdf/2402.11797
- https://egusphere.copernicus.org/preprints/2026/egusphere-2026-4378/egusphere-2026-4378.pdf
- https://www.earthdoc.org/content/papers/10.3997/2214-4609.202640046
- https://www.earthdoc.org/content/papers/10.3997/2214-4609.202220036
- https://www.earthdoc.org/content/papers/10.3997/2214-4609.201702155
- https://www.earthdoc.org/content/papers/10.3997/2214-4609.202640078
- https://www.earthdoc.org/content/papers/10.3997/2214-4609.202640008
- https://www.earthdoc.org/content/papers/10.3997/2214-4609.202640006
- https://www.earthdoc.org/content/papers/10.3997/2214-4609.202420098
- https://meetingorganizer.copernicus.org/EGU23/EGU23-11469.html
- https://bgr.bund.de/EN/Themen/GG_Geophysik/Aerogeophysik/Projekte/laufend/DESMEX-II/DESMEX-II_en.html
- https://www.gtk.fi/en/research-project/dronesom/
- https://pubs.geoscienceworld.org/seg/geophysics/article/90/3/WA261/653824/Semi-airborne-electromagnetic-exploration-of-deep
- https://confit.atlas.jp/guide/event/jpgu2023/subject/STT40-P02/tables
- https://www.mdpi.com/2504-446X/9/5/383
- https://www.azomining.com/Article.aspx?ArticleID=1972
- https://projects.gbreports.com/ontario-mining-2024/expert-geophysics-and-axiom-exploration-interviews
- https://rosor.ca/
- https://www.sphengineering.com/news/drone-radiometric-survey-uranium-exploration
- https://www.maverickdrone.com/products/medusa-ms-1000-gamma-ray-spectrometer
- https://maverickdrone.com/products/geometrics-magarrow-mk2-magnetometer
- https://www.newsfilecorp.com/release/155503
- https://www.newsfilecorp.com/release/212643
- https://www.newsfilecorp.com/release/244386
- https://www.newsfilecorp.com/release/185898
- https://www.broomead.com.au/business/bulls-n-bears/infini-finds-major-uranium-indicators-in-canadas-athabasca-basin-c-19461442
- https://www.nasdaq.com/press-release/greenridge-exploration-identifies-uranium-targets-airborne-electromagnetic-survey
- https://resourceworld.com/mustang-energy-runs-airborne-geophysics-over-dutton-project-saskatchewan/
- https://kalkine.com.au/news/stocks/mustang-energy-corp-announces-results-of-tdem-survey-over-the-914w-property
- https://announcements.asx.com.au/asxpdf/20240916/pdf/067xhdnvrnf2fh.pdf
- https://www.miningstockeducation.com/2019/07/skyharbour-announces-uav-mag-airborne-geophysics-surveying-on-its-high-grade-moore-uranium-project/
- https://www.newsfilecorp.com/release/33687/Global-UAVs-Survey-Division-Secures-Largest-UAVMAGTM-Contract-to-Date
- https://www.newsfilecorp.com/release/35616/Global-UAV-Announces-Q2-Revenue-for-2018
- https://blog.thecse.com/tag/global-uav/
- https://www.webull.com/news/15463375309521920
- https://gh.linkedin.com/in/nicholas-agbo-40012674
- https://marketintelo.com/report/drone-magnetometer-survey-market
- https://tc.canada.ca/en/aviation/drone-safety/2025-summary-changes-canada-drone-regulations
- https://www.unmannedairspace.info/?p=32272
- https://pickdrones.com/faa-part-108-bvlos-rule-delayed-oira-2026/
- https://lowaltitudeeconomy.aero/en/aam-events/faa-part-108-oira-review
- https://www.casa.gov.au/about-us/news-media-releases-and-speeches/new-trial-pathways-bvlos-approvals
