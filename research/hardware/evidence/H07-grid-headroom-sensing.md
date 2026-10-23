# H07: Our own sensors to find hidden grid headroom, then own powered land

Note on method: the shared web-fetch budget and then the web-search budget ran out partway through. About 20 searches and 6 page reads got done. Figures I could not open a page to confirm are marked (unverified).

## Summary
- **Power is what sets the price of data-centre land.** Powered land in Northern Virginia sells for at least ~$6M/acre. Entitled land there without power sells for ~$4M/acre. In weak markets, land worth ~$10k/acre without a power path can reach six figures per acre once it has one. US data-centre land purchases were ~$6B in H1 2026, up 79% on a year earlier.
- **Someone has already sensed line flows from the roadside and sold the data.** Genscape put magnetic and electric field monitors within ~60-200 ft of transmission lines to estimate power-plant output, then sold the data to traders. Verisk bought Genscape for £300M in 2019. The core patent expired around 2019.
- **The public picture of grid capacity is incomplete.** Hosting-capacity maps cover distribution feeders (a few MW each) and go stale. Large-load queues are huge and mostly speculative: ERCOT ~445 GW and PJM ~95 GW of data-centre requests. The planning models (FERC 715 power-flow cases) are restricted as CEII (critical energy infrastructure information).
- **Big gap: line loading is not the same as interconnection headroom.** What a utility will grant depends on N-1 contingency studies, stability and transformer limits, not only on today's flow on one line. Our sensors can see real flows and spare thermal margin. They cannot see the contingency answer. So the data is a strong prior, not proof.
- **Candidate play: "Powered-site bank".** Roadside EMF stations plus drone thermal give a proprietary loading map. ML ranks substations that probably have spare capacity. We option the land nearby at farmland prices, file the load request and buy the will-serve letter, then sell to Tract, Cloverleaf, hyperscalers or Digital Realty. It pairs with the geothermal bank: the same map scores export headroom for geothermal rights.

## Key facts
- Powered vs unpowered land in Northern Virginia: ~$6M vs ~$4M per acre. Elsewhere, ~$10k/acre rises to six figures. Rule of thumb: 0.5-1 acre per MW. Loudoun deal: $615M for 97 acres (~$6.3M/acre). [DCK/Avison Young](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)
- Plug Power sold its Graham, TX site to Stream: $50M plus up to $26.5M more tied to final load. That is ~164 MW on 66 acres, about $0.3-0.47M per MW for land plus load rights. Inputs were small: a $6.5M Oncor deposit and a $7.75M ERCOT letter of credit. [same source](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)
- Altus (80 deals): sites on 230/500 kV lines trade at ~2.4x those on ≤138 kV. Sites within half a mile of a substation sell for ~2x those 2-5 miles away. Markets with little committed load have a median of ~$28k/acre. [Altus](https://www.altusgroup.com/insights/where-value-is-created-in-data-center-land/)
- ERCOT has ~445 GW of large-load requests by 2033. A realistic wait for a 500 MW transmission connection is 4-6 years, against the 18-24 months buyers want. The proposed security is ~$50k/MW. [CES](https://ces-ltd.com/resources/byline-articles/ercot-large-load-integration-strategies-and-forecast-part-two-of-two/)
- PJM has 3,500 data-centre applications totalling 95 GW. [datacentres.com](https://www.datacentres.com/news/power-grid-constraints-pjm-interconnection). Dominion's Loudoun connections have been paused and constrained. [DCF](https://www.datacenterfrontier.com/energy/article/11436951/dominion-resumes-new-connections-but-loudoun-faces-lengthy-power-constraints)
- Genscape patent US7088090 (priority 1999): coil or Hall sensors read the magnetic field, and an E-field sensor gives the phase reference. Together they give current, direction and real and reactive power. Placement is ~60-100 ft from the line. The stated aim was to work "without... equipment in utility right-of-ways". The patent has expired, and there was IPR litigation over it. [patent](https://patents.google.com/patent/US7088090)
- Verisk bought Genscape for £300M in 2019. It called itself "the world's largest private network of in-field monitors" and had 1,300 customers. [ABN](https://aberdeenbusinessnews.co.uk/wood-mackenzie-parent-buys-data-analytics-provider-for-300m/)
- Academic work has rebuilt line current and sag from ground magnetic fields. [NJIT](https://web.njit.edu/~wp24/manuscripts/Magnetic%20field%20sensing%20based%20approach%20current%20reconstruction%20sag%20detection.pdf)
- Sensors that sit on the line itself, such as dynamic line rating (DLR) units, need the utility to install them. Heimdall raised $25M (Series B). Great River Energy saw +25% average line capacity, +42.8% on one line. [REW](https://www.renewableenergyworld.com/power-grid/transmission/startup-behind-magic-ball-for-boosting-transmission-capacity-raises-25-million/). LineVision (non-contact, mounted on towers) raised a $12.5M Series B. [Utility Dive](https://www.utilitydive.com/press-release/20210407-linevision-secures-125-million-in-series-b-financing-to-scale-grid-enhanc/). Sentient MM3 clamps onto distribution lines and is sold to utilities. [Sentient](https://sentientenergy.com/products/mm3-overhead-fault-indicator/). None of these is a third-party ownership play.
- Comps for the "powered land" asset: Cloverleaf Infrastructure raised $300M for "energy-first" data-centre sites. [DCD](https://www.datacenterdynamics.com/en/news/cloverleaf-infrastructure-secures-300m-for-clean-energy-data-center-campuses/). Tract assembles multi-GW parks (1,515 acres in Caldwell County TX for ~2 GW; Reno 2,200 acres). [GlobeNewswire](https://www.globenewswire.com/de/news-release/2025/05/07/3076274/0/en/TRACT-CLOSES-ACQUISITION-OF-1-515-ACRES-IN-CALDWELL-COUNTY-TEXAS-FOR-MULTI-GIGAWATT-DATA-CENTER-TECHNOLOGY-PARK.html)
- Public data: EIA-930 gives hourly load only at the level of whole balancing areas. FERC 714 is annual. [EIA](https://www.eia.gov/electricity/930-content/about.html). Line-by-line flows and contingency limits are not public (unverified in detail; CEII rules).
- Zanskar is hiring a Head of Interconnection & Transmission. [Lever](https://jobs.lever.co/Zanskar/6fa6846f-7628-4199-be04-d205774de0de). That supports the "interconnection is our bottleneck" quote (I could not find the exact quote).

## Hardware design sketch
**Station ("Pylon Ear").** It has a 3-axis search-coil or fluxgate magnetometer array, which uses spatial gradients to separate the three phases and cancel nearby lines. It also has an E-field plate for the voltage phase, GPS-disciplined timing so many stations stay in sync (like a poor man's PMU, the synchronised meters utilities use), a small solar panel and battery, LTE, and an edge MCU (a small processor that cleans the signal on the box). It sits 20-60 m from a 69-500 kV line, on public road right of way where the line crosses a road, or on a ranch fence line under a small paid easement.
- BOM: ~$600-1,500 per station. Prototype run of 10: ~$25k with engineering time. (unverified estimates)
- Unit cost at scale: ~$400. Install: ~$300 (a staked post, no permit on private land). Data: ~$10/month.
- Coverage: 2-4 stations per substation corridor, one per line leaving it. A 100-substation region needs ~300 stations, about $250k installed.
- **Add-on: drone thermal and acoustic passes.** We fly substation transformers from public land, keeping to FAA Part 107 rules and staying off restricted airspace. Fan state and radiator temperature show how heavily a transformer is loaded. Cost ~$200 per site visit. Satellite thermal is too coarse at 30-100 m (unverified).
- Prototype time: 8-12 weeks to the first calibrated station.

**ML layer.** Inputs: station flows, public line and conductor data (HIFLD, OpenStreetMap, conductor guessed from imagery), weather for ampacity (how much current a line can carry before it overheats), EIA-930, ISO nodal prices (congestion shows up in the price), and queue filings. Output: P(substation can serve X MW by date Y), plus a rebuilt power-flow model. Over time we train against ground truth: will-serve letters and study results we and others get back.

## What data it unlocks and why incumbents lack it
- **Hourly flows and real thermal margin on lines.** Today only the utility has them. Developers see only stale distribution maps and a queue padded with phantom load.
- **A labelled loop.** Each load request we file returns a utility answer, and that becomes a training label. A queue position plus a flow history is a dataset nobody else assembles.
- **Why nobody does this:** Genscape-style networks were sold for trading generation, not for land. Utilities own the full picture but are regulated and cannot speculate on land. Tract and Cloverleaf use relationships and deposits, not measurement (unverified on their methods).

## How it compounds into owned assets
1. The map flags a substation with probable spare capacity, say 150-300 MW.
2. We option 200-500 acres within half a mile at farmland or ranch prices. Typical inputs (unverified): ~$3-10k/acre to buy, ~1-3% a year for the option.
3. We file the large-load request and post security (~$50k/MW in ERCOT) to get a study or will-serve letter. This is the proving step.
4. Step-up: land rises from ~$10-30k/acre to six figures or more per acre. The Plug-Stream deal shows ~$0.3-0.47M/MW. On 200 MW that is ~$60-90M for perhaps $5-15M in. We sell to Tract, Cloverleaf, Stream, QTS/Blackstone, Digital Realty or straight to hyperscalers, often keeping an earn-out tied to delivered MW, the way Plug did.
5. **Geothermal pairing.** The same map scores generation export headroom. Geothermal rights near headroom with spare capacity are worth more. A firm 24/7 geothermal-plus-data-centre campus behind the meter avoids the queue. We could hold both the heat right and the powered site, then sell the bundle to Fervo/Google-type buyers.

Size: 5-10 GW of sites at ~$0.3M/MW is $1.5-3B in gross step-up. Today's land market already runs ~$12B a year.

## Risks and kill conditions
- **Physics gap:** contingency, short-circuit and transformer limits decide what gets granted. If loading-based scores do not predict will-serve outcomes better than "near a big substation", kill it.
- **The utility queue is first come, first served.** Holding land does not reserve capacity. Security deposits (~$50k/MW) and the new ERCOT and PJM speculative-load filters raise the cost of each test.
- **Legal:** passive field sensing from public right of way looks legal by analogy with Genscape (unverified). But road ROW encroachment permits, CEII rules, NERC CIP sensitivities and state critical-infrastructure trespass laws (drones near substations) could bite. We would need a legal opinion first.
- **Competition:** Tract, Cloverleaf and others hold capital and utility relationships. Utilities increasingly publish large-load maps.
- **Market:** if AI capex cools, powered land loses its premium fast.

## Cheapest first test
- **Cost and time:** ~$15k and ~45 days. Build 3 stations from off-the-shelf magnetometers.
- **Calibration:** place them at 3 lines whose flows are known, such as a line next to a generator that reports to EIA. Accuracy pass bar: within 10% of known flow, hourly.
- **Backtest:** in parallel, take 30 substations with known will-serve outcomes (from news and filings). Check whether public data plus a loading proxy beats distance to a substation. Pass bar: AUC >0.7.

## Sources
- https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise
- https://www.altusgroup.com/insights/where-value-is-created-in-data-center-land/
- https://ces-ltd.com/resources/byline-articles/ercot-large-load-integration-strategies-and-forecast-part-two-of-two/
- https://www.datacentres.com/news/power-grid-constraints-pjm-interconnection
- https://www.datacenterfrontier.com/energy/article/11436951/dominion-resumes-new-connections-but-loudoun-faces-lengthy-power-constraints
- https://patents.google.com/patent/US7088090
- https://aberdeenbusinessnews.co.uk/wood-mackenzie-parent-buys-data-analytics-provider-for-300m/
- https://web.njit.edu/~wp24/manuscripts/Magnetic%20field%20sensing%20based%20approach%20current%20reconstruction%20sag%20detection.pdf
- https://www.renewableenergyworld.com/power-grid/transmission/startup-behind-magic-ball-for-boosting-transmission-capacity-raises-25-million/
- https://www.utilitydive.com/press-release/20210407-linevision-secures-125-million-in-series-b-financing-to-scale-grid-enhanc/
- https://sentientenergy.com/products/mm3-overhead-fault-indicator/
- https://www.datacenterdynamics.com/en/news/cloverleaf-infrastructure-secures-300m-for-clean-energy-data-center-campuses/
- https://www.globenewswire.com/de/news-release/2025/05/07/3076274/0/en/TRACT-CLOSES-ACQUISITION-OF-1-515-ACRES-IN-CALDWELL-COUNTY-TEXAS-FOR-MULTI-GIGAWATT-DATA-CENTER-TECHNOLOGY-PARK.html
- https://www.eia.gov/electricity/930-content/about.html
- https://jobs.lever.co/Zanskar/6fa6846f-7628-4199-be04-d205774de0de
- https://www.stantec.com/en/ideas/content/blog/2025/go-slow-to-go-fast-how-to-improve-hosting-loading-capacity-maps-for-interconnection
