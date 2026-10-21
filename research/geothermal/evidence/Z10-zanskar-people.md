# Z10: Zanskar people, public statements, hiring, and stated bottlenecks

Research note (2026-10-21). Method limit: the shared WebSearch budget for this run was used up before this agent started, so no search queries went through. Everything below comes from direct WebFetch of Zanskar's own site (zanskar.com), its Lever job board, its Substack newsroom, and one Heatmap article linked from that newsroom. Third-party interviews (Volts, Catalyst, Latitude Media, Canary, LinkedIn profiles, GRC/Stanford talks) could not be retrieved, and are marked (unverified) wherever they are mentioned. A follow-up pass with search budget should fill those in.

## 1. People (from primary pages)

- **Carl Hoiland**, co-founder and CEO. Geology background. Zanskar was founded in 2019 by Hoiland and Edwards ([Heatmap](https://heatmap.news/climate-tech/ai-geothermal-discovery)).
- **Joel Edwards**, co-founder and CTO. Geology background ([Heatmap](https://heatmap.news/climate-tech/ai-geothermal-discovery)).
- **Ryan McGraw**, CDO (Chief Development Officer). Fronts utility and offtake deals: the NV Energy PPA and the CC Power GEODE agreement ([PPA](https://zanskargeothermal.substack.com/p/zanskar-inks-100-mw-power-purchase), [GEODE](https://zanskargeothermal.substack.com/p/zanskar-and-cc-power-sign-geode-agreement)).
- **Diego D'Sola**, Head of Finance ([$40M facility](https://zanskargeothermal.substack.com/p/zanskar-closes-40m-in-novel-development)).
- **Head of Reservoir R&D**. The role exists, and the ML/software engineers report to it (name not given) ([Lever posting](https://jobs.lever.co/Zanskar/fa6e7e75-767f-402f-80de-f8b97b91b292)).
- **Director, Partnerships & Projects**. Runs DOE/DoD grants and partner projects ([Lever](https://jobs.lever.co/Zanskar/a8b80fa9-b706-4ee8-a23b-a695646d77b3)).
- Headquarters is in Salt Lake City, UT. The field crew at Lightning Dock (Animas, NM) was kept on after the acquisition ([Lightning Dock year one](https://zanskargeothermal.substack.com/p/one-year-at-lightning-dock)).

The About page names no leadership team. The Who We Work With page lists Freeport-McMoRan, the U.S. DOE and the U.S. Department of War as partners, and PNM and NV Energy as customers ([who-we-work-with](https://www.zanskar.com/who-we-work-with/)). A Freeport-McMoRan partnership is notable because Freeport is a mining major with large western land and data holdings. The nature of the relationship is not stated (unverified).

## 2. What they hire for (Lever board, fetched 2026-10-21)

There are 10 open roles ([jobs.lever.co/Zanskar](https://jobs.lever.co/Zanskar)):

| Team | Role | Location |
|---|---|---|
| Drilling | Senior Drilling & Completions Engineer | SLC hybrid |
| Finance | Senior Accountant; Project Finance Associate | SLC |
| G&A | In-House Counsel; Paralegal / Contract & Compliance Manager | SLC hybrid |
| Lightning Dock | O&M Technician | Animas, NM |
| Partnerships | Project Manager, Partnerships & Projects | SLC hybrid |
| R&D | Sr Distributed Systems Engineer; Sr/Staff Backend Engineer; Sr/Staff Software Engineer | SLC hybrid |

What the postings show:
- **No landman, land or leasing role is open right now.** A "Land" team does exist. The PM posting lists the teams it coordinates as "Exploration, Drilling, Development, Engineering, Permitting, Land, Finance, Legal" ([PM posting](https://jobs.lever.co/Zanskar/a8b80fa9-b706-4ee8-a23b-a695646d77b3)). So land is an in-house function, but it is not where they are adding people.
- **Drilling has moved from proving resources to building fields.** The drilling engineer will run campaigns that span "temperature gradient wells to full-size production and injection geothermal wells". The work includes ESP design, "completion designs for EGS stimulations", vendor contracts and regulatory filings ([drilling posting](https://jobs.lever.co/Zanskar/1f99b513-5dcd-4016-8ec0-e86b7cb55895)).
- **The ML stack is a "next-generation multi-physics well-targeting engine"** built with "novel software and machine learning modeling". They are hiring distributed-compute engineers to "migrate an existing system to scale", working with geophysicists, geoscientists and seismologists ([R&D posting](https://jobs.lever.co/Zanskar/fa6e7e75-767f-402f-80de-f8b97b91b292)). No open role is labelled "data scientist" or "ML researcher". The current need is scaling the infrastructure, not inventing the models.
- **Half the openings are finance, legal or compliance** (project finance, counsel, paralegal/contracts, accountant), plus a grants PM. This is what a developer/IPP looks like as it moves toward construction and project finance. It is not an exploration startup's hiring pattern.

## 3. How they pick land (their own words)

- **Prospecting toolkit, then auction.** Big Blind: an anomaly with above-background heat flow was "identified in late 2023" with the prospecting toolkit. Then: "After acquiring the BLM leases at auction", geologists used AI prediction tools and stochastic geometry models to choose two drill targets. Wells were spudded in July and August 2025, and the reservoir was hit at ~2,700 ft at ~250°F, with a gradient of ~100 °C/km ([Big Blind technical post](https://zanskargeothermal.substack.com/p/zanskar-proves-first-blind-geothermal)). **About 20 months passed from anomaly to spud.** The lease was won at a public competitive BLM sale, so Zanskar had to bid against anyone else in that sale.
- **No surface signs, no prior data.** "There is nothing geothermally obvious at the surface". The site had "no prior exploration or well data" ([Big Blind reveal](https://zanskargeothermal.substack.com/p/zanskar-reveals-big-blind-the-discovery)).
- **"Dozens more" similar blind anomalies** are in the portfolio. They describe "an exploration campaign spanning millions of acres across the West" ([About](https://www.zanskar.com/about/), [Big Blind technical](https://zanskargeothermal.substack.com/p/zanskar-proves-first-blind-geothermal)). They give no lease count or acreage under lease.
- **Overlooked known sites.** Pumpernickel (Humboldt County, NV; formerly "Hot Springs Ranch"/"Tipton Ranch") had been "written off for not being capable of generating utility-scale power" after "a few explorers" and sparse shallow holes. Zanskar's first hole failed, and the second reached ~280°F at ~2,500 ft MD. They size Phase 1 at about 20 MWe ([Pumpernickel technical](https://zanskargeothermal.substack.com/p/zanskar-strikes-geothermal-steam)), with power by about 2028 ([Heatmap](https://heatmap.news/climate-tech/ai-geothermal-discovery)).
- **Distressed brownfield.** Lightning Dock (~15 MW gross, NM) was bought in June 2024. The prior owner thought the field was depleted: it had cooled ~50°F in 5 years. Zanskar spent 6 months on modelling, then drilled well 44-7 to ~8,000 ft (>4,000 GPM, PI ~50 GPM/psi). First-year output was ~75,000 MWh, more than 44,000 MWh above what the legacy wells would have produced ([Lightning Dock year one](https://zanskargeothermal.substack.com/p/one-year-at-lightning-dock)).
- **Data inputs.** They use "decades-old geological and geophysical datasets", satellite and remote sensing, and "long-forgotten analog datasets mapping undeveloped regions, which the founders tracked down and digitized". An in-house field data-collection team has been running for about 3 years ([Heatmap](https://heatmap.news/climate-tech/ai-geothermal-discovery)). This is very close to the Terranox thesis of illegible public archives.
- **Exclusion screen.** Much of the publicly known pipeline is "off-limits" (conserved lands) or far from interconnection ([Big Blind technical](https://zanskargeothermal.substack.com/p/zanskar-proves-first-blind-geothermal)).

## 4. What they say the bottleneck is

Zanskar has moved the bottleneck it talks about over time:

1. **Exploration risk and cost (the founding thesis).** "if you knew exactly where to drill today, it already would be." "there are millions of possible models, and there's no way humans can model all of those" (Hoiland, [Heatmap](https://heatmap.news/climate-tech/ai-geothermal-discovery)). Test wells have covered only ~5% of the prospective western U.S. They claim discovery cost of **<$15k/MW, against >$100k/MW for the 1970s-80s majors** ([Big Blind technical](https://zanskargeothermal.substack.com/p/zanskar-proves-first-blind-geothermal)), "an order of magnitude" lower ([Pumpernickel PR](https://zanskargeothermal.substack.com/p/using-custom-built-artificial-intelligence)).
2. **Early-stage project finance (2026).** Hoiland: the $40M non-recourse revolving development facility (built to scale to $100M; Just Climate and Spring Lane) "unlocks the critical bottleneck of early-stage project financing" ([$40M](https://zanskargeothermal.substack.com/p/zanskar-closes-40m-in-novel-development)). D'Sola: the industry has lacked "the right financial structures".
3. **Transmission and plant constraints (operational).** At Lightning Dock, winter output is curtailed to stay under the transmission cap, and summer afternoons are curtailed because heat rejection cannot keep up ([Lightning Dock](https://zanskargeothermal.substack.com/p/one-year-at-lightning-dock)).
4. **Not stated as the bottleneck: land/leasing.** None of the fetched releases names leasing, BLM backlog or permitting as the binding constraint. Third-party coverage reportedly has Zanskar and other developers complaining about BLM lease-sale cadence and NEPA timelines (unverified; search budget exhausted).

## 5. Business model as stated

- They own and operate. "We discover these resources, then develop and operate the power plants" ([About](https://www.zanskar.com/about/)). Edwards: "restart that flywheel of developing greenfield geothermal again" ([Heatmap](https://heatmap.news/climate-tech/ai-geothermal-discovery)).
- Offtake: a **100 MW, 20-year PPA with NV Energy through 2050**, delivering by 2030 across multiple Nevada projects, subject to PUCN approval of NV Energy's 2026 IRP ([PPA](https://zanskargeothermal.substack.com/p/zanskar-inks-100-mw-power-purchase)). There is also an exploration+offtake framework (GEODE) with CC Power: 9 CCAs, ~12% of CAISO load, 2.7M customers ([GEODE](https://zanskargeothermal.substack.com/p/zanskar-and-cc-power-sign-geode-agreement)).
- Capital: **$115M Series C (Jan 2026; led by Spring Lane), $180M total equity**. USV and Lowercarbon co-led the Series A, and Obvious led the Series B ([Series C](https://zanskargeothermal.substack.com/p/zanskar-raises-115m-series-c-following)). Two DOE awards (Sep 2026, amounts undisclosed): a horizontal EGS-style injection well at Lightning Dock, and deep directional confirmation at a Nevada discovery ([DOE](https://zanskargeothermal.substack.com/p/zanskar-selected-for-two-us-department)).
- History (unverified): early press described Zanskar as a data/analytics partner to developers before it moved to owning assets. If true, they tried the tool/service shape and abandoned it.

## 6. Talks and podcasts found

- Pushkin "What's Your Problem?": Hoiland, "Drilling Smarter Wells to Unleash Geothermal Energy", Sep 2025 ([Pushkin](https://www.pushkin.fm/podcasts/whats-your-problem/drilling-smarter-wells-to-unleash-geothermal-energy)). No transcript was available.
- Heatmap feature, Sep 2025 (above).
- GRC, Stanford Geothermal Workshop and other conference talks 2023-2026: not retrievable in this pass (unverified).

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **Zanskar already does the Terranox playbook's front half.** It digitises forgotten analog data, runs ML over it, takes leases at BLM auction before drilling, and proves the resource. **The difference is the back half.** Zanskar keeps every asset all the way to an operating plant, which means a 20-year PPA, project finance, a drilling department, O&M technicians and EGS completions. That is about 2 years from anomaly to discovery, a further ~3 years to power, and $180M of equity plus debt facilities. Today it has one ~15 MW plant and a 100 MW PPA due by 2030.
2. **The gap is the step between proof and plant.** Zanskar's "dozens more" anomalies and "millions of acres" campaign are more than it can drill and build in parallel. Its own hiring (no landmen; finance, legal and drilling-heavy) shows the people and capital being pulled into development. A Terranox-shape company could be **the high-throughput land-and-prospect originator.** It would lease far more acreage per dollar and drill only cheap gradient holes. It would then sell or farm out proven or semi-proven leases to Fervo, Ormat, Zanskar itself, utilities or hyperscalers rather than build plants. Capital needs are 10-100x smaller, and step-up value is realised at the lease and TG-hole stage.
3. **Land is not Zanskar's stated bottleneck, and that is both an opening and a warning.** It is an opening because no AI-native player is optimising for land capture at scale (non-BLM private rights, state trust land, nominations and timing of BLM sales). It is a warning because BLM competitive sales are public, and since Big Blind, others will bid up anomalies. The edge has to come from (a) nominating parcels that nobody else knows to value, (b) private and state rights acquired off-auction, and (c) geographies or data Zanskar has not mined: oil and gas BHT archives in sedimentary basins, Canadian provinces, and mining assessment files, where Freeport-type partners hold data.
4. **Zanskar's own numbers support the economics.** Discovery costs <$15k/MW, against a market value of proven geothermal resource that sits far above this (a typical development cost is several $M/MW; unverified for this note). That spread is the step-up a Terranox-shape company would capture without building plants.
5. **Risk to the gap.** Zanskar could start selling surplus prospects itself, and GEODE is already a hint of this: utilities paying for exploration with offtake rights attached. If that happens, the gap narrows to geographies and resource types (sedimentary, co-produced, Canada) that Zanskar does not cover.

## Sources

- https://www.zanskar.com/about/
- https://www.zanskar.com/careers/
- https://www.zanskar.com/who-we-work-with/
- https://jobs.lever.co/Zanskar
- https://jobs.lever.co/Zanskar/1f99b513-5dcd-4016-8ec0-e86b7cb55895
- https://jobs.lever.co/Zanskar/a8b80fa9-b706-4ee8-a23b-a695646d77b3
- https://jobs.lever.co/Zanskar/fa6e7e75-767f-402f-80de-f8b97b91b292
- https://zanskargeothermal.substack.com/archive
- https://zanskargeothermal.substack.com/p/zanskar-proves-first-blind-geothermal
- https://zanskargeothermal.substack.com/p/zanskar-reveals-big-blind-the-discovery
- https://zanskargeothermal.substack.com/p/zanskar-strikes-geothermal-steam
- https://zanskargeothermal.substack.com/p/using-custom-built-artificial-intelligence
- https://zanskargeothermal.substack.com/p/one-year-at-lightning-dock
- https://zanskargeothermal.substack.com/p/zanskar-raises-115m-series-c-following
- https://zanskargeothermal.substack.com/p/zanskar-closes-40m-in-novel-development
- https://zanskargeothermal.substack.com/p/zanskar-inks-100-mw-power-purchase
- https://zanskargeothermal.substack.com/p/zanskar-and-cc-power-sign-geode-agreement
- https://zanskargeothermal.substack.com/p/zanskar-selected-for-two-us-department
- https://zanskargeothermal.substack.com/p/podcast-drilling-smarter-wells-to
- https://www.pushkin.fm/podcasts/whats-your-problem/drilling-smarter-wells-to-unleash-geothermal-energy
- https://heatmap.news/climate-tech/ai-geothermal-discovery
