# Z07: Other AI- and data-driven geothermal exploration players, and who is land-first

*Research note, 2026-10-21.*

**Method.** The workflow's shared WebSearch budget (200 calls) was already used up when this agent started, so I ran no open web searches. The facts below come from two places:

- direct WebFetch of company sites: Teverra, Cyrq, Open Mountain Energy, Baseload Capital, XGS, Mazama, Gradient Geothermal, Rodatherm, Sage, Quaise and Project InnerSpace;
- facts already sourced with URLs in sibling evidence files (Z04 BLM bid records, L-series files).

Several names in the brief could not be checked:

- **Hephae** and **Geologica**: the domains are parked or for sale.
- **TLS Geothermics**: the domain did not resolve.
- **GeoFrame, Quantum, Avalon**: there was no URL to fetch without search.

These are marked (unverified). A follow-up turn with fresh search budget should close those gaps.

---

## 1. Bottom line

1. **Almost nobody else does "ML exploration + buy the right + own the asset" for blind hydrothermal.** Zanskar is the only venture-backed company with a public, sourced record of doing all three (Z01/Z04). The other "AI geothermal" names split into three groups:
   - **(a) Services and software:** Teverra, SLB/Baker Hughes, Seequent-style tools.
   - **(b) Technology-first EGS/closed-loop/superhot developers** that buy land to deploy a drilling or loop technology: Fervo, Mazama, Quaise, Sage, XGS, Eavor, Rodatherm.
   - **(c) Conventional owner-operators** that use "modern data" on brownfield assets: Ormat, Cyrq, Open Mountain, Baseload.
2. **The land-first players are mostly anonymous LLCs and incumbents, not AI startups.** In BLM Nevada and Utah auctions, the parcel counts are dominated by:
   - **Buffalo River Minerals** (28 Nevada wins in 2024);
   - **Invenergy** (17);
   - **Ormat** (12 in 2022);
   - **Aspect Holdings** (13 in 2022);
   - **Baseload Power** (10 in 2022);
   - **TLS Geothermics** (8 in 2023, the largest that year);
   - Percheron, Umbrella Renewables, Cordillera, Skyladder Capital, Lithos48 and Navram Resources.

   Several of these have no public operating identity. They look like land-banking or nominee vehicles (Z04, from BLM all-bids PDFs). **Land-banking ahead of discovery already exists. Data-driven land banking with a published discovery engine does not.**
3. **The data moat is thinning at the regional-screening layer.** Public XGBoost favourability maps from USGS, NREL and UNR, plus Project InnerSpace's free **GeoMap**, give anyone a first-pass Great Basin and North America screen (L03, L10). The edge moves to illegible legacy records and to speed of acquiring the right.

---

## 2. Player-by-player

### A. Exploration and data services: tool shape, scores low as a business model but matters as competition

- **Teverra (Denver).** Its geothermal offerings are:
  - play-fairway analysis and resource assessment;
  - EGS engineering and hydro-thermo-mechanical modelling;
  - "physics-informed machine learning", signal processing and AI;
  - GeoDeck (subsurface visualisation), ConvertDeck (oil and gas well-to-geothermal conversion) and MMARCT (EGS fracture monitoring).

  It reports "multi-million-dollar" DOE and NSF SBIR grants since 2019, and a 5-year DoD geothermal development project at Ft Wainwright, AK, where it ranked top 3 of 68 applicants. Its site shows **no owned assets or leases**. TLS Geothermics appears as a client testimonial. A sibling file notes that Petrolern is "now Teverra", which fits a services lineage. (https://teverra.com/)
- **SLB, Baker Hughes and Halliburton.** They supply drilling, logging, reservoir modelling and some geothermal digital tooling. Baker Hughes is an owner of Baseload Capital (logo on https://www.baseloadcap.com/) and a partner in XGS's DOE New Mexico drilling project (https://xgsenergy.com/). None of them is a known land-first explorer (unverified for SLB; the Ormat news fetch returned empty).
- **Project InnerSpace (nonprofit).** It offers GeoMap, a free geothermal prospecting tool, launched in beta and then for North America (ThinkGeoEnergy coverage: https://www.thinkgeoenergy.com/project-innerspace-launches-geomap-geothermal-prospecting-tool-for-north-america/ ; https://projectinnerspace.org/). It is philanthropy-funded and builds on oil-and-gas data and expertise. **Implication: a free, public screening layer now exists, especially for sedimentary basins.** That lowers barriers to entry and makes regional screening a commodity.

### B. Technology-first developers that are land-holders by necessity

| Company | Shape | Land / site | Capital and offtake (sourced) |
|---|---|---|---|
| **Fervo** | Horizontal-well EGS IPP | About **596k acres** assembled 2019–21 at about **$4/acre** (S-1). Cape Station, UT: **33 MW net COD on 30 Sep 2026** | IPO in 2026 (~$1.9B reported). Google 3 GW framework; >1 GW of PPAs. Uses an AI/ML subsurface partnership with Google (2021). https://www.sec.gov/Archives/edgar/data/1853868/000162828026025821/fervoenergy-sx1.htm ; https://www.esgtoday.com/geothermal-developer-fervo-energy-raises-1-9-billion-in-upsized-ipo/ ; https://blog.google/outreach-initiatives/sustainability/google-fervo-geothermal-energy-partnership/ |
| **Mazama** | Superhot EGS (Newberry, OR) | Pilot reached **629 °F at ~10,200 ft** (2025). Taurus plant: **200 MW**, first power 2029; "at least 5 GW" site claim. Says it has "secured land" elsewhere in the West | Khosla-backed; DOE support for the 15 MW Ceres project. Raised $135M (Sep 2026, reported). https://www.mazamaenergy.com/ ; https://www.renewableenergymagazine.com/geothermal/mazama-energy-raises-135-million-to-scale-20260918 |
| **Quaise** | Millimetre-wave superhot drilling | Project Obsidian, central OR: **50 MW** first phase, +200 MW expansion, COD 2030 | **$180M Series B**, including $35M from Nabors. https://www.quaise.com/ |
| **Sage Geosystems** | Hot-dry-rock EGS + storage (TX) | Next commercial EGS sited at **Ormat's Blue Mountain** plant. 3 MW storage at SMECI | Meta PPA up to 150 MW (2024). Investors include Ormat, Nabors, Meta and Carbon Direct. https://www.sagegeosystems.com/ |
| **XGS Energy** | "Solid-state" closed loop with conductive materials, independent of permeability | New Mexico; DOE-selected drilling with Baker Hughes, NM Tech and Sandia | Meta up to **150 MW in NM** (Jun 2025); about $56.7M raised (sibling file). https://xgsenergy.com/ ; https://www.businesswire.com/news/home/20250612778008/en/XGS-Energy-and-Meta-to-Partner-on-150-MW-Advanced-Geothermal-Project |
| **Eavor** | Multilateral closed loop | Geretsried, Germany | About **$529M** raised 2021–Jun 2025 (sibling file, L-series) |
| **Rodatherm** | Waterless closed loop with refrigerant; pads under 5 acres, sited near load | Not disclosed | Not shown on the site. https://www.rodatherm.com/ |

**Read-across.** These companies sell *technology-enabled MW*. Several closed-loop shapes (XGS, Eavor, Rodatherm) say performance does not depend on permeability. That **lowers the scarcity value of a specific right**: any hot rock near load works. For permeability-dependent EGS (Fervo, Sage, Mazama), parcel quality (temperature at depth, stress, transmission) still dominates. Those companies are **buyers of de-risked land**, not competitors for blind discovery.

### C. Owner-operators and brownfield consolidators

- **Ormat.** The incumbent vertically integrated player and a heavy BLM bidder (12 Nevada wins in 2022). Historically it discovered blind systems through mineral-exploration holes: McGinness Hills (lease taken in 2007, about 160 MW) and Tungsten Mountain (24 MW). It is a technology partner and investor in Sage. (https://investor.ormat.com/news-events/news/news-details/2021/Ormat-Completes-McGinness-Hills-Complex-Expansion/default.aspx)
- **Cyrq Energy (Salt Lake City / Reno).** Plants: Hudson Ranch (Salton Sea), Patua and Soda Lake (NV), Thermo 1 (UT). It sold Lightning Dock (NM), widely reported as the seller to Zanskar (unverified). It pitches "smarter geothermal exploration and plant optimization through modern data and technology", with no ML specifics. (https://www.cyrqenergy.com/)
- **Open Mountain Energy (Reno).** It acquires, develops, owns and operates plants:
  - **~23,477 leased acres + ~4,203 fee acres**, 64 wells (34 full-size);
  - **57.5 MW** of guaranteed PPA capacity, about $767.7M of total PPA value, 95.8 MW of contracted interconnection;
  - bought Bottle Rock Power (Feb 2023) and holds StarPeak (NV).

  It is brownfield-first, not data-first. (https://www.openmountainenergy.com/)
- **Baseload Capital (Sweden).** An investment platform with four "Baseload Power" subsidiaries (US, Iceland, Taiwan, Japan) building small binary plants. Owners include **Baker Hughes, Google, Chevron, Ingka and Breakthrough Energy**. Chevron joined its $25M round in 2021. It won 10 Nevada BLM parcels in 2022. An Aug 2026 strategy update says it "sharpens focus". (https://www.baseloadcap.com/)
- **Gradient Geothermal (Denver).** Modular ORC units on co-produced oilfield fluids, sold on a **rental or subscription model**. Pilots with Grant Canyon (NV, 2022) and Chord Energy (ND). This is service/equipment, not land. (https://www.gradientgeothermal.com/)
- **Invenergy.** A large IPP that entered geothermal through land. It was the second-largest Nevada winner in 2024 (17 parcels), outbid Zanskar $112 to $111/acre on a Lander parcel, and bid up to $327/acre in Utah in 2025 (Z04, BLM PDFs).

### D. Land-first actors visible in BLM records (Z04)

| Bidder | Evidence | Identity |
|---|---|---|
| Buffalo River Minerals | 28 Nevada parcels (Oct 2024); $344/acre, $1.35M parcel in Utah (Apr 2025) | No public operating identity (unverified). Likely a land bank or nominee |
| Lithos48 Inc | Took the Pumpernickel step-out at **$232/acre** (~$408k) over Zanskar's $231, one month after Zanskar's discovery announcement | Unknown. The name hints at a lithium or minerals angle |
| TLS Geothermics | 8 parcels, the largest by count, Nov 2023 NV sale; Teverra client | French geothermal developer (unverified; domain unreachable) |
| Aspect Holdings, Percheron, Umbrella Renewables, Cordillera, Skyladder Capital, Navram | Repeat 2022–2025 bidders in NV and UT | Unknown |

The step-up is visible in these records:

- Zanskar's Pumpernickel step-out acreage cost **$2/acre** in Nov 2023. Adjacent acreage cleared at **$232/acre** in Oct 2025.
- Land near Fervo cleared at up to **$344/acre**.
- **Fast followers already exploit disclosure.** Nobody demonstrably exploits *pre-disclosure, data-driven* selection at portfolio scale apart from Zanskar, and Zanskar's 2025 additions fell to 872 acres.

### E. Europe and Asia (thin evidence)

- **Europe:** Eavor (Germany); Vulcan Energy (Upper Rhine geothermal-lithium, ~€2.2B Lionheart financing per sibling L12; site unreachable); Innargi (Danish district heat, unverified). Rights there are state-granted exploration licences, so the US-style "buy cheap at auction, flip" arbitrage is weaker.
- **Indonesia, Kenya, Japan:** geothermal is dominated by state or quasi-state players (Pertamina Geothermal Energy, KenGen, JOGMEC programmes). No AI land-first startup was found (unverified; no search was possible). Baseload operates in Japan and Taiwan.
- **Unverified names from the brief:** GeoFrame, "Quantum" geothermal, Avalon, Hephae, Snowcap, Bedrock Energy. Bedrock Energy is a shallow geoexchange heat-pump driller and is irrelevant here (unverified). Dandelion and Zap are explicitly out of scope.

---

## 3. Competitive map: who owns what

| Shape | Examples | ML or data claim | Owns rights before proof? | Sells the proven state? |
|---|---|---|---|---|
| Blind-hydrothermal AI developer | **Zanskar** | Strong, public | Yes (~50k acres in NV auctions) | No: builds and operates (100 MW NVE PPA) |
| Next-gen EGS / superhot / closed loop | Fervo, Mazama, Quaise, Sage, XGS, Eavor, Rodatherm | Moderate (Fervo–Google) | Yes, as a means to an end (Fervo 596k acres) | No |
| Integrated incumbents | Ormat, Cyrq, Open Mountain, Baseload, Invenergy | Low or generic | Yes (auctions, acquisitions) | Rarely |
| Services and software | Teverra, SLB, Baker Hughes, Gradient | Strong (PIML, SBIR) | No | n/a |
| Anonymous land banks | Buffalo River, Lithos48, Percheron, Skyladder | None visible | Yes | Presumably, by flipping (unverified) |
| Free public screening | Project InnerSpace GeoMap; USGS, NREL, UNR maps | Public | n/a | n/a |

---

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **The empty quadrant is "data-driven rights bank / prospect generator".** It means buying rights cheaply before proof, proving them up with cheap temperature-gradient and slim holes, and selling, farming out or royaltying the proven state. Every sourced player sits elsewhere:
   - Zanskar and the EGS companies build plants;
   - the services firms own nothing;
   - the land banks have no visible discovery engine.

   This is the mining prospect-generator model (and Terranox's uranium model) applied to geothermal. None of the named geothermal startups runs it publicly.
2. **There are many natural buyers, and they are capitalised and short of sites:**
   - Fervo: IPO in 2026; Google 3 GW framework;
   - Mazama: 200 MW Taurus; $135M raised;
   - Quaise: $180M Series B;
   - Sage and XGS: Meta, 150 MW each;
   - Ormat, Invenergy, Open Mountain and Cyrq.

   A neutral seller can serve all of them. Zanskar cannot easily sell to Ormat or Invenergy, its direct competitors in auctions and for PPAs.
3. **Gap versus Zanskar:**
   - **Geography.** Zanskar won nothing outside Nevada at auction. Open ground includes Utah, Oregon and Idaho, New Mexico state land, the Texas surface estate (SB 785) and BHT-rich sedimentary basins, where GeoMap and oil-and-gas logs exist but rights are fragmented.
   - **Channel.** Noncompetitive day-after filings: in NV-2025 only 1 of 27 leftover parcels drew an offer, so about 92k nominated acres went unclaimed. Also private fee rights and split estate.
   - **Product.** Selling de-risked parcels to permeability-dependent EGS and to hyperscalers that want sites, not electrons.
4. **Threats to price in:**
   - **(i) Disclosure leakage.** Fast-follower land banks reprice neighbouring acreage about 100x within weeks (Lithos48 at $232/acre). The company must lock up whole fairways before drilling or press.
   - **(ii) Free public screening layers** (GeoMap, USGS/NREL ML maps) commoditise the regional model. The edge must come from digitising illegible legacy records and acquiring faster.
   - **(iii) Permeability-independent closed loops** (XGS, Eavor, Rodatherm) reduce the scarcity premium for some land. Target permeability-dependent hydrothermal and EGS-grade parcels, where site quality still sets value.
5. **It is not too small.** BLM manages geothermal leasing on about 245M acres. Nevada auctions alone put 190–280k bid acres per year on offer, Fervo's pipeline is 38–50 GW, and hot ground clears at $100–410/acre against a $2 floor on blind ground. That is a recurring, cheap inventory with a visible resale market.

---

## Sources

- Teverra: https://teverra.com/
- Cyrq Energy: https://www.cyrqenergy.com/
- Open Mountain Energy: https://www.openmountainenergy.com/ ; https://www.openmountainenergy.com/news
- Baseload Capital: https://www.baseloadcap.com/ ; https://www.thinkgeoenergy.com/chevron-and-baseload-capital-to-collaborate-on-u-s-geothermal-projects/
- Gradient Geothermal: https://www.gradientgeothermal.com/
- XGS Energy: https://xgsenergy.com/ ; https://www.businesswire.com/news/home/20250612778008/en/XGS-Energy-and-Meta-to-Partner-on-150-MW-Advanced-Geothermal-Project
- Mazama Energy: https://www.mazamaenergy.com/ ; https://www.renewableenergymagazine.com/geothermal/mazama-energy-raises-135-million-to-scale-20260918
- Quaise: https://www.quaise.com/ ; https://www.quaise.com/news/a-first-look-at-project-obsidian
- Sage Geosystems: https://www.sagegeosystems.com/
- Rodatherm: https://www.rodatherm.com/
- Fervo S-1: https://www.sec.gov/Archives/edgar/data/1853868/000162828026025821/fervoenergy-sx1.htm ; IPO: https://www.esgtoday.com/geothermal-developer-fervo-energy-raises-1-9-billion-in-upsized-ipo/ ; COD: https://www.renewableenergymagazine.com/geothermal/fervo-energy-declares-commercial-operation-at-cape-20261002 ; Google partnership: https://blog.google/outreach-initiatives/sustainability/google-fervo-geothermal-energy-partnership/
- Ormat McGinness Hills: https://investor.ormat.com/news-events/news/news-details/2021/Ormat-Completes-McGinness-Hills-Complex-Expansion/default.aspx ; Tungsten Mountain: https://investor.ormat.com/news-events/news/news-details/2017/24-MW-Tungsten-Mountain-Geothermal-Power-Plant-in-Nevada-Begins-Commercial-Operation/default.aspx
- Project InnerSpace / GeoMap: https://projectinnerspace.org/ ; https://www.thinkgeoenergy.com/project-innerspace-launches-geomap-geothermal-prospecting-tool-for-north-america/
- BLM NV bids (land-bank bidders, step-up): https://www.blm.gov/sites/default/files/docs/2024-10/GEONV-2024-Q4-All%20Bids.pdf ; https://www.blm.gov/sites/default/files/docs/2025-10/NV_Geot_20251021_Bidding_Results.pdf ; https://www.blm.gov/sites/default/files/docs/2022-08/NV_Geot_20220830_Bidding_Results.pdf ; https://www.blm.gov/sites/default/files/docs/2023-11/NV_Geot_20231114_Bidding_Results.pdf ; UT 2025: https://www.blm.gov/sites/default/files/docs/2025-05/BLM-UT-Geothermal-Lease-Sale-Results-04-08-2025.pdf
- Zanskar: https://www.zanskar.com/ ; https://zanskargeothermal.substack.com/p/zanskar-raises-115m-series-c-following
- Sibling evidence files (same directory): Z04-land.md, Z05-business.md, L03-ml-geothermal.md, L10-sedimentary.md, L12-lithium-brines.md
