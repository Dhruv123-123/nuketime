# H14: Wildcard sensor-led asset plays (beyond geothermal)

Research budget note: both the shared web-search and web-fetch budgets ran out partway through this slice. The planned 5+ searches per finalist were not all done. Figures from search-result titles are cited to that URL. Anything from memory is marked (unverified).

## Summary
- Best wildcard: **Grid Headroom Bank**. Put our own non-contact magnetometer stations under transmission lines, measure real line flows (Genscape did this and sold to Verisk for $364M), find substations with true spare capacity, option nearby farmland at ~$10k/ac, and sell it as "powered land", which trades at six figures per acre or more.
- Second: **natural hydrogen seep network**. Continuous soil-gas H2 sensors find real seeps that one-off surveys miss. Lease cheap acreage. Sell to Koloma, Fortescue/HyTerra-type buyers. Lease land grab is live (HyTerra about 52,000 ac in Kansas).
- Third: **pore-space bank** for CO2 storage, using our own passive-seismic plus MT nodes. This shares hardware with geothermal. The step-up and size are weaker.
- Rejected or weak: orphan-well reuse (assets are liabilities), water rights (OpenET satellite water use is public, so no data edge), spectrum (FCC buildout data is public and buyers are few), non-powered dams (12 GW total, small sites), used turbines and transformers (we cannot sensor a machine before we own it), aggregates (permitting is the moat, not data).
- The power-land play has the strongest step-up and buyer depth of anything in this slice. Its proof step (a utility load study) is slow and costly, and our sensor data improves the hit rate on it.

## Quick checks: 10 candidates
| # | Play | Our sensor | Right bought | Quick check | Verdict |
|---|---|---|---|---|---|
| 1 | Grid headroom to powered land | Ground magnetometer + E-field under lines | Land options near substations | NoVA $4M/ac unpowered vs $6M+ powered; $10k/ac goes to six figures with power ([DCK](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)) | **Top pick** |
| 2 | Natural H2 seeps | Continuous soil-gas H2 probes | Mineral/gas leases | HyTerra +26,200 ac, to ~52,000 ac Nemaha ([Stockhead](https://stockhead.com.au/energy/hyterra-triples-lease-acreage-at-us-hydrogen-project), [Stockhead](https://stockhead.com.au/energy/hyterra-secures-more-hydrogen-helium-play-types-with-nemaha-project-expansion)); Koloma $394M round 2026 ([EnkiAI](https://enkiai.com/hydrogen/koloma-hydrogen-2026-394m-funding-osaka-gas-deal/)) | **Pick 2** |
| 3 | CO2 pore space | Passive seismic + MT nodes | Pore-space leases | Pore leasing active in Bakken ([JPT](https://jpt.spe.org/pore-space-leasing-insights-from-a-bakken-surface-owners-perspective)); ownership law unsettled ([ABA](https://www.americanbar.org/groups/environment_energy_resources/resources/natural-resources-environment/2024-summer/whose-pore-space-it-carbon-capture-storage-prompts-new-questions-property-law)) | Pick 3 |
| 4 | Non-powered dams | Flow + head sensors | FERC preliminary permit | 12 GW across US NPDs ([POWER](https://www.powermag.com/doe-12-gw-lies-unexploited-in-non-powered-dams-across-u-s/), [OSTI](https://www.osti.gov/biblio/1039957)); Rye sells licenses ([WPXI](https://www.wpxi.com/news/local/rye-development-moves-sell-licenses-three-pittsburgh-area-hydropower-projects/UKR4A5NKNZEKXD76Q42X36ZM7A/)) but FERC denies extensions ([REW](https://www.renewableenergyworld.com/energy-business/new-project-development/ferc-rejects-extensions-for-permits-on-five-hydropower-projects-in-kentucky)) | Too small; USGS gauges already public |
| 5 | Orphan wells reuse | Drone CH4 | Well + lease | Drones already used in PA ([EDF](https://edf.org/paw)); LBNL AI on old maps ([LBNL](https://newscenter.lbl.gov/2024/12/04/ai-helps-researchers-dig-through-old-maps-to-find-lost-oil-and-gas-wells/)) | Plugging liability beats reuse value |
| 6 | Used gas turbines | Vibration/borescope | Machine | Data centers turning to aeroderivatives ([Power Eng](https://www.power-eng.com/gas/data-center-power-crunch-lifts-engines-aeroderivatives-into-larger-role/)) | Real arbitrage, but no pre-purchase sensing access |
| 7 | Used transformers | DGA/acoustic | Machine | Lead times high ([WoodMac](https://woodmac.com/news/opinion/supply-shortages-and-an-inflexible-market-give-rise-to-high-power-transformer-lead-times)), easing per Rystad ([PPD](https://powerpeakdigest.com/global-transformer-supply-constraints-ease-rystad/)) | Shortage is fading; same access issue |
| 8 | Hidden water rights | Airborne thermal ET | Water right | OpenET-style satellite ET is public ([BSPR](https://www.boisestatepublicradio.org/2026-01-12/water-scarce-west-satellite-tool-insight-farm-irrigation)) | No data edge |
| 9 | Unused spectrum | SDR occupancy | FCC license / lease | Academic occupancy work only ([UCSB](https://sites.cs.ucsb.edu/~ravenben/publications/pdf/dsa-imc10.pdf)) | Buildout records public; few buyers |
| 10 | Aggregates near megaprojects | Drone LiDAR/GPR | Quarry land | MLM/VMC M&A pays for reserves ([SEC 425](https://www.sec.gov/Archives/edgar/data/916076/000119312512009342/d281225d425.htm)) | Permitting, not data, is the moat |

## Finalist A: Grid Headroom Bank (deep dive)

### Key facts
- US data center land buys hit about $6B in H1 2026, up 79% YoY (Avison Young via [DCK](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)).
- Northern Virginia: entitled land without power about $4M/ac, powered land at least $6M/ac. In cheaper markets, $10k/ac land without a power path "can reach six figures per acre once power is established" ([DCK](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)).
- Sites tied to 230/500 kV trade at about 2.4x sites tied to 138 kV or lower (Altus via DCK).
- Price is now paid per MW: the Plug Power to Stream Graham, TX sale had $50M base plus up to $26.5M tied to final load capacity on a 164 MW reference (DCK). That is a direct step-up paid for proven power.
- Rule of thumb: 0.5 to 1 acre per MW (DCK). So a 300 MW site is 150 to 300 acres.
- Data center land deals rose 141% in Q1 ([Bisnow](https://www.bisnow.com/news/national/data-center-development/data-center-sites-are-warping-the-market-for-developable-land-134771)).
- Precedent for the sensor: Genscape put non-contact monitors near power plants and lines to infer flows, then sold to Verisk for $364M in 2019 ([Hart Energy](https://hartenergy.com/news/verisk-acquire-genscape-364-million-182282)). Patents cover ground-level measurement of line current from magnetic fields ([US7398168B2](https://patents.google.com/patent/US7398168), [US6771058](https://patents.google.com/patent/US6771058)).
- Public hosting-capacity maps exist but are coarse and stale; practitioners say they need work before they can guide interconnection ([Stantec](https://www.stantec.com/en/ideas/content/blog/2025/go-slow-to-go-fast-how-to-improve-hosting-loading-capacity-maps-for-interconnection), [NREL](https://www.nrel.gov:443/docs/fy22osti/81811.pdf)). Substation capacity matters more than line proximity ([Acres](https://www.acres.com/blog/transmission-line-proximity-vs.-substation-capacity-in-data-center-site-selection)).

### Hardware design sketch
- Station: 3-axis fluxgate or tunnel-magnetoresistance magnetometer array (2 to 3 heights to solve conductor geometry), E-field plate for voltage phase, GPS-disciplined clock for phase angle, LTE modem, solar plus battery, pole or ground mount on a leased easement 20 to 60 m from the right-of-way.
- BOM: about $600 to $1,500 per station (unverified estimate; fluxgates $200 to $800, rest is commodity). At scale about $400.
- Deployment: two stations per line segment near each candidate substation. A 50-substation region needs about 300 stations, about $300k to $500k installed (unverified).
- Prototype: 6 to 10 weeks with off-the-shelf magnetometers.
- ML: invert fields to per-line amps, combine with public line ratings, FERC 715 cases, queue data and weather, and estimate N-1 headroom by hour at each substation.

### What data it unlocks
- Hourly real flows on specific lines. Utilities have this (SCADA) but do not publish it. Traders bought Genscape for the same reason. No land developer has it. Site selectors today use public maps, queue tables and broker talk.
- It compounds: each year of time series sharpens seasonal headroom and load-growth trends. A copycat needs years of station-time to catch up.

### How it compounds into owned assets
- Right bought: 2 to 5 year purchase options on 200 to 500 acre parcels near substations the model flags, at farm price ($5k to $15k/ac) plus option fees of a few percent (unverified).
- Proof step: file a large-load request and get a utility load study or a will-serve letter. This is the expensive, slow, low-hit-rate step our data improves.
- Step-up: land with a will-serve goes to six figures per acre or a per-MW price (Stream deal). Buyers: hyperscalers, Stream, QTS, Vantage, Compass, Digital Realty, and powered-land funds.
- Ladder: land bank, then a per-MW earnout book, then the national map of real headroom (data product for traders and utilities later).

### Risks and kill conditions
- Utilities may ignore measured headroom. Their study model, not physics, decides. Kill if flagged sites do not beat random sites on study outcomes.
- Data center demand could cool, or large-load tariffs (big deposits) could shrink the premium.
- Incumbents (Enverus, Wood Mackenzie, which owns Genscape) could re-point existing monitors at this use.
- Landowners near substations already know about the land rush and are pricing it in.

### Cheapest first test
- About $15k and 30 days. Build 4 stations, place them under two lines with known public ratings near one substation. Pass if inferred amps match a public reference (an ISO flow report or a utility-confirmed value) within 10%. In parallel, back-test: take 20 substations with public will-serve or load-study outcomes and see whether public plus flow features rank winners in the top third.

## Finalist B: Natural hydrogen seep network
- Facts: HyTerra added 26,200 ac and grew Nemaha to about 52,000 ac; Top End Energy holds about 25,000 ac in Kansas ([Stockhead](https://stockhead.com.au/energy/top-end-energy-continues-growing-its-kansas-natural-hydrogen-holdings)); HyTerra spudded wells ([H2 View](https://h2-view.com/story/hyterra-to-drill-first-natural-hydrogen-wells-in-kansas-next-month/2122754.article)); Koloma reported $394M funding in 2026 (EnkiAI). Lease cost is likely $5 to $30/ac bonus (unverified).
- Sensor: buried electrochemical or MOS H2 probes plus CH4/CO2/He at 1 m, logging every 10 minutes. Seeps are thought to vary by day and season, so one-off surveys miss them (unverified). BOM about $300 to $800 per probe (unverified). 100 probes per township.
- Edge: a dense time series of H2 flux nobody else has, plus a training set for ML on public well logs.
- Step-up: lease at cheap rates, prove flux, farm out to Koloma or majors for a carry. The weakness is that commercial H2 production is unproven, so buyers are few and VC-funded.
- First test: about $10k, 21 days, 20 probes over a known Kansas "fairy circle". Pass if H2 is above 100 ppm on repeated readings and differs from background.

## Finalist C: Pore-space bank
- Same passive-seismic plus MT nodes as geothermal, read for seal and reservoir quality. Pore leases are being signed in the Bakken (JPT). Ownership law is unsettled (ABA). Buyers include Oxy/1PointFive, Exxon and Tallgrass (unverified). Weak because buyers do their own Class VI work, value depends on 45Q policy, and seismic data is a known incumbent skill. Best kept as an add-on to the geothermal company.

## Sources
- https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise
- https://www.bisnow.com/news/national/data-center-development/data-center-sites-are-warping-the-market-for-developable-land-134771
- https://hartenergy.com/news/verisk-acquire-genscape-364-million-182282
- https://patents.google.com/patent/US7398168 ; https://patents.google.com/patent/US6771058
- https://www.stantec.com/en/ideas/content/blog/2025/go-slow-to-go-fast-how-to-improve-hosting-loading-capacity-maps-for-interconnection
- https://www.acres.com/blog/transmission-line-proximity-vs.-substation-capacity-in-data-center-site-selection
- https://stockhead.com.au/energy/hyterra-triples-lease-acreage-at-us-hydrogen-project
- https://enkiai.com/hydrogen/koloma-hydrogen-2026-394m-funding-osaka-gas-deal/
- https://www.powermag.com/doe-12-gw-lies-unexploited-in-non-powered-dams-across-u-s/
- https://jpt.spe.org/pore-space-leasing-insights-from-a-bakken-surface-owners-perspective
- https://woodmac.com/news/opinion/supply-shortages-and-an-inflexible-market-give-rise-to-high-power-transformer-lead-times
- https://www.boisestatepublicradio.org/2026-01-12/water-scarce-west-satellite-tool-insight-farm-irrigation
