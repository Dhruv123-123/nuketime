# Z01: Zanskar company overview

*Research note, 2026-10-21. Method: the shared WebSearch budget ran out on the first call of this task, so everything below comes from direct WebFetch of primary sources (Zanskar's site, its Substack and press releases) plus trade and press coverage. Anything not tied to a URL is marked (unverified).*

## 1. Identity and founding

- **What it is:** a geothermal discovery and development company based in Salt Lake City, UT. Its tagline is "Building a world model for the subsurface." Mission: make geothermal "the most cost effective, reliable, and clean form of power on the planet." (https://www.zanskar.com/ ; https://www.zanskar.com/about)
- **Founded:** 2019 by **Carl Hoiland (co-founder, CEO)** and **Joel Edwards (co-founder, CTO)**. Both are geologists by training. (https://www.latitudemedia.com/news/armed-with-115-million-geothermal-startup-zanskar-gets-ready-to-build/ ; https://heatmap.news/climate-tech/ai-geothermal-discovery)
  - Detailed CVs, such as university and previous employers, were not retrieved (unverified).
- **Origin of the data moat:** the founders "acquired long-forgotten analog subsurface data sets and digitized them for their AI model." About three years before Sept 2025 they also launched an in-house field data-collection team. (https://heatmap.news/climate-tech/ai-geothermal-discovery)
  - This is the same "illegible archive, then ML" move Terranox makes. Zanskar already does it for geothermal.
- **Other named executives:**
  - Ryan McGraw, Chief Development Officer
  - Diego D'Sola, Head of Finance / CFO
  - (https://zanskargeothermal.substack.com/p/zanskar-inks-100-mw-power-purchase ; https://zanskargeothermal.substack.com/p/zanskar-closes-40m-in-novel-development)
- **Headcount:** not disclosed in any source retrieved.
  - The careers page (Oct 2026) lists 10 open roles: drilling, finance, G&A including in-house counsel, a paralegal and project finance, an O&M technician at Lightning Dock (Animas, NM), partnerships, and R&D software. (https://www.zanskar.com/careers)
  - Estimate: roughly 50 to 100 staff (unverified). This is inferred from the breadth of functions and the field and drilling operations.

## 2. Funding history

| Round | Date | Amount | Lead(s) | Source |
|---|---|---|---|---|
| Seed / early | ~2019–2022 | not found | not found | (unverified) |
| Series A | not found | not found | **Union Square Ventures + Lowercarbon Capital** (co-leads) | Series C release |
| Series B | ~2024 (less than 2 years before Jan 2026) | **$30M** | **Obvious Ventures** | Latitude Media; Series C release |
| Series C | Jan 21, 2026 | **$115M** (oversubscribed, capped to limit dilution) | **Spring Lane Capital** | Series C release; TechCrunch; Latitude |
| Series C extension | ~Apr 2026 | undisclosed | **Just Climate** (Generation IM) | $40M facility release |
| Development Capital Facility | closed Apr 16, 2026 | **$40M**, non-recourse revolving, structured to scale to **$100M** | Just Climate + Spring Lane (co-leads) | $40M facility release |

- **Total equity raised to date: $180M.** This is the figure at the Series C (https://zanskargeothermal.substack.com/p/zanskar-raises-115m-series-c-following).
  - Implied seed plus Series A plus grants: about $35M. This is derived as 180 − 115 − 30 (unverified split).
- **Series C participants:**
  - Obvious Ventures, USV, Lowercarbon
  - Munich Re Ventures
  - Susquehanna Sustainable Investments, Clearvision Ventures, Orion Industrial Ventures
  - Safar Partners, Imperative Ventures, StepStone Group, University Growth Fund
  - Cross Creek, GVP Climate, Tranquillion, Carica Sustainable Investments
  - UP.Partners, All Aboard Fund
  - Prime Impact Fund also appears on the homepage investor list (https://www.zanskar.com/).
- **Capital strategy:**
  - The company was "100% venture-backed since inception."
  - The Jan 2026 plan was to move to non-dilutive development and project-level debt (Latitude Media). The $40M facility covers pre-construction costs and bridges projects to bank project finance.
  - Spring Lane's Jason Scott: the key is "financing project capital needs off balance sheet."
  - D'Sola: the goal is a cost-of-capital path that brings geothermal "in line with mature energy asset classes." (https://zanskargeothermal.substack.com/p/zanskar-closes-40m-in-novel-development)
- **Non-dilutive public money:** in Sept 2026 Zanskar was selected for two DOE projects (amounts undisclosed; awards still under negotiation). It is one of only two companies selected under both programs. (https://zanskargeothermal.substack.com/p/zanskar-selected-for-two-us-department)
  - **Field-scale demonstration:** a short horizontal injection well, stimulated, at Lightning Dock. This is a hydrothermal-plus-EGS hybrid.
  - **Exploration and discovery:** deep directional wells at an undrilled Nevada site, with near-real-time model updating.

## 3. Business model: "geothermal developer that uses AI," not a software vendor

- **Self-description:** Zanskar discovers resources, then "develops and operates the power plants." It sells firm power. (https://www.zanskar.com/about)
- **Series C use of funds** (https://zanskargeothermal.substack.com/p/zanskar-raises-115m-series-c-following):
  - Advance a gigawatt-scale pipeline.
  - Begin building plants, with several in the Western U.S. delivering power before 2030.
  - Expand the AI platform and exploration drilling.
  - "Build, own, and operate high-grade geothermal assets," with hyperscaler and data-centre demand named as a target.
- **Explicitly avoids technology risk.** Edwards: "We're avoiding the first-of-a-kind risk label, so that we can access cheaper capital sooner."
  - Plants are planned in **20 MW increments** so they qualify for small-generator interconnection in the West.
  - Edwards calls interconnection the main bottleneck. (https://www.latitudemedia.com/news/armed-with-115-million-geothermal-startup-zanskar-gets-ready-to-build/)
- **Operator thesis.** Hoiland: "The only way to test and prove out those ideas is to be an operator of those assets." (https://magazine.asme.org/issues/may-2026/news-hidden-geothermal-goldmines)
- **Exit-to-utility element.** The NV Energy PPA covers "multiple projects that Zanskar will build and operate, then sell as a portfolio to NV Energy." So Zanskar already monetises a step-up by selling built assets. (https://zanskargeothermal.substack.com/p/zanskar-inks-100-mw-power-purchase)
- **Methods:**
  - Supervised ML trained on known systems, including accidental discoveries, plus simulations.
  - "Bayesian evidential learning" priors.
  - A proprietary geothermal simulator.
  - Inputs from satellite, airborne and ground surveys, plus faults.
  - Field crews survey roughly 100 sq mi per flagged anomaly and drill shallow temperature-gradient holes.
  - (https://techcrunch.com/2026/01/21/zanskar-thinks-1-tw-of-geothermal-power-is-being-overlooked/ ; https://www.technologyreview.com/2025/12/04/1128763/ai-geothermal-zanskar/ ; ASME)
  - Zanskar claims its discovery cost per MW is "an order of magnitude lower" than that of the last major greenfield explorers, inflation-adjusted. (https://zanskargeothermal.substack.com/p/using-custom-built-artificial-intelligence)

## 4. Assets and track record

- **Lightning Dock, NM (acquisition):**
  - Bought around May or June 2024. The plant was ~15 MW gross, designed for ~310 °F, and had sagged to ~255 °F. The prior operator had put it up for sale. Seller and price are undisclosed.
  - New well 44-7 to ~8,000 ft: >4,000 GPM, PI ~50 GPM/psi, inlet temperature ~60 °F higher.
  - First-year output was ~75,000 MWh, more than 140% above what the legacy wells would have produced. Production was "tripled" in May 2025.
  - (https://zanskargeothermal.substack.com/p/one-year-at-lightning-dock ; Latitude)
  - This is a buy-distressed-then-re-model play: a Terranox-like step-up captured on an operating asset.
- **Pumpernickel, NV (Sept 2025):**
  - ~280 °F (137 °C) at ~2,500 ft. Phase 1 is 20 MWe, targeting ~2028.
  - Oil and gas companies and the federal government had drilled the site intermittently since the 1970s without finding commercial temperatures.
  - (https://www.thinkgeoenergy.com/zanskar-validates-ai-based-discovery-method-with-drilling-at-pumpernickel-geothermal-site-nevada/ ; https://heatmap.news/climate-tech/ai-geothermal-discovery)
- **Big Blind, NV (Dec 2025):**
  - ~250 °F at ~2,700 ft. Zanskar calls it the first blind system confirmed commercial by industry in over 30 years. It had no prior wells.
  - **Zanskar bought a federal (BLM) lease** on the strength of its prospecting data, then drilled two wells in July and August 2025.
  - Comparable systems are claimed at more than 100 MWe each.
  - (https://zanskargeothermal.substack.com/p/zanskar-reveals-big-blind-the-discovery ; https://www.technologyreview.com/2025/12/04/1128763/ai-geothermal-zanskar/)
- **Portfolio:**
  - "Full or partial control" of sites with more than **700 MW** of potential (D'Sola, Jan 2026).
  - **Six 20 MW plants** in the pipeline, with commercial operation in 3–4 years.
  - Pipeline claimed to support at least 1 GW. Zanskar wants at least **10 confirmed sites** to attract project finance.
  - Edwards: "dozens of sites that look just like this."
  - The exploration campaign spans "millions of acres" in the western US.
  - (Latitude; TechCrunch; MIT Tech Review; https://www.zanskar.com/about)
- **Offtake:**
  - **100 MW, 20-year PPA with NV Energy** (May 2026) running through 2050, for delivery by 2030. It is subject to PUCN approval of the 2026 IRP and covers Pumpernickel, Big Blind and other sites.
  - **GEODE agreement** with **CC Power**, a joint powers authority of nine California CCAs representing about 12% of CAISO load. Zanskar prospects in CAISO and CC Power can support development and buy the power. Financial terms are undisclosed.
  - (https://zanskargeothermal.substack.com/p/zanskar-and-cc-power-sign-geode-agreement)

## 5. Stated targets

- **"Multi-gigawatt" pipeline** and "gigawatts" of firm power.
- Hoiland calls conventional hydrothermal a **"terawatt-scale opportunity."** He argues DOE's 60 GW-by-2050 figure is too low and that undiscovered systems are underestimated "by an order of magnitude or more."
- About 95% of systems lack surface expression, and only about 5% of the prospective western US has had test wells.
- Zanskar describes US geothermal as poised for "more than 25x growth."
- (TechCrunch; Heatmap; https://zanskargeothermal.substack.com/p/using-custom-built-artificial-intelligence)

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **Zanskar already runs the front half of the Terranox loop.** It digitises forgotten archives, uses ML to rank prospects, buys the BLM lease before proof (Big Blind), and buys a distressed asset cheaply and re-models it (Lightning Dock).
   - A Terranox-shape entrant is therefore not novel on method in the Great Basin hydrothermal play. Zanskar has a 6-year head start, $180M of equity, a $40–100M development facility, its own drill program and DOE backing.
   - Competing head-on for Nevada BLM lease sales against Zanskar, Ormat and Fervo is the weakest version of the idea.
2. **The structural gap is the asset-light "rights bank."** Zanskar is deliberately becoming a capital-heavy IPP: it builds 20 MW plants, takes project finance and needs 10 or more confirmed sites. Each discovery ties up hundreds of millions of capex and a multi-year interconnection queue, which caps how many rights it can hold and work.
   - It also **cannot easily sell proven parcels to competitors** (Fervo, Ormat, data-centre developers) without undercutting its own pipeline.
   - A Terranox-shape company that only aggregates rights, de-risks to "drill-ready / temperature-confirmed," then sells or farms out for a carry or royalty is a different shape, closer to a mineral-royalty or land-bank model. Zanskar is not pursuing it.
3. **Zanskar's own evidence validates the step-up economics.**
   - A lease bought cheaply, followed by two intermediate wells, became a site that may support more than 100 MWe (Big Blind).
   - A plant sold as underperforming tripled production after one deeper well.
   - A 100 MW PPA was structured as build-then-sell-to-utility.
   - These are the price points a rights-bank would sell into.
4. **Gaps in geography and data that Zanskar does not visibly occupy** (unverified as to its private land book):
   - Private and state geothermal rights, and fee land, outside BLM lease sales.
   - Sedimentary and oilfield basins using oil and gas BHT and well-log archives. Zanskar's stated inputs are surface, airborne and satellite geophysics, plus TG holes.
   - Hard-rock mining assessment files.
   - Canada (Alberta, BC, Saskatchewan). Terranox already knows the Saskatchewan assessment-file regime.
   - Low-temperature direct-use and data-centre-heat parcels.
   - Rights for EGS developers who need hot, shallow, interconnectable rock near load rather than convective systems.
5. **Risks to flag:**
   - Zanskar could open a "partner prospects" arm. GEODE with CC Power already looks like prospect-for-offtaker.
   - Lease competition rises as Zanskar's ML pulls more nominations into BLM sales.
   - Zanskar's real moat is permeability prediction plus drilling, which a pure land bank lacks. So a rights-bank must pick plays where temperature-at-depth, which public archives can map, drives most of the value, or partner for drilling.
6. **Scoring view:** this is plausible and not "too small." 700 MW of controlled potential is already being valued by Spring Lane and Just Climate. But the entrant must avoid Zanskar's home turf and differentiate on asset type, data source, geography and the asset-light model, not on "AI finds blind hydrothermal."

## Sources

- https://www.zanskar.com/
- https://www.zanskar.com/about
- https://www.zanskar.com/news
- https://www.zanskar.com/careers
- https://zanskargeothermal.substack.com/p/zanskar-raises-115m-series-c-following
- https://zanskargeothermal.substack.com/p/zanskar-closes-40m-in-novel-development
- https://zanskargeothermal.substack.com/p/zanskar-inks-100-mw-power-purchase
- https://zanskargeothermal.substack.com/p/zanskar-and-cc-power-sign-geode-agreement
- https://zanskargeothermal.substack.com/p/zanskar-reveals-big-blind-the-discovery
- https://zanskargeothermal.substack.com/p/using-custom-built-artificial-intelligence
- https://zanskargeothermal.substack.com/p/one-year-at-lightning-dock
- https://zanskargeothermal.substack.com/p/zanskar-selected-for-two-us-department
- https://techcrunch.com/2026/01/21/zanskar-thinks-1-tw-of-geothermal-power-is-being-overlooked/
- https://www.latitudemedia.com/news/armed-with-115-million-geothermal-startup-zanskar-gets-ready-to-build/
- https://www.technologyreview.com/2025/12/04/1128763/ai-geothermal-zanskar/
- https://heatmap.news/climate-tech/ai-geothermal-discovery
- https://www.thinkgeoenergy.com/zanskar-validates-ai-based-discovery-method-with-drilling-at-pumpernickel-geothermal-site-nevada/
- https://magazine.asme.org/issues/may-2026/news-hidden-geothermal-goldmines
