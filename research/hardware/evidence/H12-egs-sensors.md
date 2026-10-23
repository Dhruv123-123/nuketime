# H12. Sensors for the EGS / superhot size ladder

Note on method: the shared web search and fetch budget ran out after about 12 searches and 7 fetches. Facts with a URL were checked. Everything marked (unverified) comes from background knowledge and needs a check before anyone relies on it.

## Summary

- EGS land is now priced like oil land. A 2025 BLM Utah sale next to Fervo's Cape Station averaged about $111/acre over 50,000+ acres. An August 2026 Millard/Beaver sale took $24.7M, with a top bid of $1,207/acre. Fervo's first leases were roughly $4/acre (brief figure, unverified here). Whoever ranks a block before the auction captures the step-up.
- Five things decide an EGS block: temperature at 3-5 km (175-250C+), rock type (crystalline or tight, with sediment cover under about 1 km), stress regime (normal faulting is best), natural fracture orientation, and seismic and social risk. At FORGE: 199C at 2,297 m in granite under 780 m of fill, with Shmin 0.62, SHmax 0.77 and Sv 1.13 psi/ft (normal faulting).
- Today the stress and fracture inputs come only from deep wells: image logs, breakouts and DFITs. Those cost millions of dollars per data point because you need the hole. Nobody measures stress cheaply before leasing. Temperature is mapped from shallow holes, but the logs are often read before the hole has settled thermally, and few people correct for groundwater.
- Ordinary silicon electronics fail at about 175C. SOI works to about 225-250C. SiC has been shown at 300C for 1,000 hours. Fibre DTS and DAS works at 250-300C+. So a sensor *at* depth is solved but expensive. The cheap lever is at the surface and in shallow holes, plus ML that ties those readings to the deep result.
- Best play: a heat-flow-plus-stress "block rating kit". It has three parts. A long-dwell thermistor string with on-site rock conductivity in 150-300 m bedrock holes. A 30-60 node passive seismic patch that maps shear-wave splitting, which shows the stress direction. And MT/gravity to find depth to basement. The output is a proprietary EGS grade per section. We use it to nominate and win leases, or option private land, ahead of the developers.

## Key facts

- Lease price ladder. Utah BLM 2025 sale: 50,000+ acres, $5.5M+, about $111/acre, the highest per-acre price in recent Utah history (https://www.sltrib.com/news/environment/2025/04/11/utah-renewable-energy-blm-sale). August 2026 Millard/Beaver sale: $24.7M high bids, 32 of 37 parcels bid, $4.16M top parcel, $1,207/acre top bid (https://www.thinkgeoenergy.com/blm-receives-record-breaking-24m-in-winning-bids-in-utah-geothermal-lease-sale/). August 2026 Utah sale records: winners not yet named (https://energynews.pro/en/blm-sells-geothermal-leases-in-utah-records-reported-by-trade-press). Fervo's roughly $4/acre original cost (brief, unverified).
- FORGE baseline. Well 58-32 reached 2,297 m and about 199C. Granite top at 780 m. Stress gradients Shmin 0.62, SHmax 0.77 and Sv 1.13 psi/ft from the 2017 minifrac and DFIT. About 2,000 fractures picked on the FMI image log. Core covered only about 6 m (https://gdr.openei.org/files/1209/ARMA2019_JMoore-FORGE.pdf). Minifrac data for 16B(78)-32 is public (https://gdr.openei.org/submissions/1570).
- How stress is measured today. Breakouts and drilling-induced tensile fractures on image logs give the SHmax direction. A DFIT or minifrac gives Shmin size. Both need an open deep hole (https://www.weatherford.com/documents/papers/2019/increasing-reliability-of-stress-characterization-through-optimum-design-and-sensitivity-analysis-of/). Typical cost: an image log run is $50-200k and a DFIT is $100-300k, both on top of a $5-10M deep well (unverified).
- Shallow thermal holes. They are usually under 500 ft deep. Cost runs $5 to $50/ft, median $16.50/ft. OpenEI says they "do not have the accuracy of predicting reservoir temperatures or depths" (https://openei.org/wiki/Thermal_Gradient_Holes). Groundwater flow in Basin and Range basins can hide or fake a gradient. The fix is to log below the water table in bedrock and wait days to weeks for the hole to settle (unverified).
- Electronics limits. Silicon CMOS leakage becomes a problem near 250C. A SiC op-amp ran at 300C, and passives passed 1,000 h at 300C. The GE/DOE program cost $2M (https://www.energy.gov/sites/prod/files/2014/02/f7/high_tilak_electronics_platform.pdf). Sandia built dewarless high-temperature logging tools (https://sandia.gov/research/publications/details/dewarless-logging-tool-1st-generation-2000-08-01). Most commercial tools are rated 175C, or 200-260C in a vacuum flask for hours (unverified).
- Fibre. Fervo's Project Red used DAS and DTS fibre in the horizontal pair to place wells and watch stimulation. It was the first commercial horizontal EGS proof (https://egi.utah.edu/wp-content/uploads/2023/09/09.45-Emma-McConville-Fervo_EGI_Sept-19-2023.pdf; https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2025/Titov.pdf). That fibre is a development tool. It is used after the lease is won, not to rank land.

## What decides EGS quality, and the cheap proxy for each

| Parameter | Today (deep, after the lease) | Cheap proxy (before the lease) | How well it predicts |
|---|---|---|---|
| T at 3-5 km | Deep well log | Heat flow in a 200 m bedrock hole times modelled conductivity and heat production | About ±20-40C at 4 km in conductive crust (unverified). Poor where groundwater flows. |
| Depth to basement / rock type | Deep well, seismic reflection | Gravity + MT + mining and water-well logs | Good to ±200 m (unverified) |
| Stress direction | Breakouts on image logs | Shear-wave splitting of local microquakes on a node array. World Stress Map. Quaternary fault trends | Fast-shear direction tracks SHmax in the upper crust (unverified) |
| Stress regime / size | DFIT | Earthquake focal mechanisms. Fault slip tendency | Regime yes. Size only roughly. |
| Natural fractures | Image log, core | Outcrop and lidar fracture mapping. MT anisotropy | Weak |
| Seismic risk | Traffic-light plan after drilling | Background microseismicity from the same nodes | Good, and needed for permits anyway |

## Hardware design sketch

1. **Long-dwell heat-flow probe.** A string of 20-40 calibrated thermistors (±5 mK) with a logger and cellular or satellite uplink. It sits 2-6 weeks in a 150-300 m bedrock hole, so the drilling disturbance dies away. We add a needle or optical-scan conductivity reading on cuttings or core, plus a gamma reading for heat production. BOM is about $3-6k per string. Logger and comms are about $1k (unverified). The hole is the cost: at $16.50-50/ft, a 650 ft hole is $11-33k, or $40-80k with hard-rock mobilisation (unverified). Strings can be reused.
2. **Stress patch.** 30-60 three-component seismic nodes, spaced 1-2 km, left 1-3 months. They catch microquakes and ambient noise. We process shear-wave splitting, focal mechanisms and background rate. Nodes cost about $2-5k each to buy or are cheap to rent (unverified). Deployment is about $50-150k per 100 km2 (unverified).
3. **MT + gravity.** Contracted at first, about $1-3k per MT station (unverified). The only build is the ML stack that combines all of it.
4. **Later (superhot rung):** a SiC/SOI memory tool, or a fibre we leave in other people's holes (mining, water, abandoned O&G) to read temperature and breakouts at 175-300C. A first prototype is $0.5-2M and 12-24 months (unverified).

Prototype for parts 1-2: about $150-300k and 4-6 months. Fully deployed cost per block (100 km2): about $0.3-0.6M with 4-6 holes plus the patch (unverified).

## What data it unlocks that is not public

- Thermally settled heat flow in bedrock under basin cover, with matching measured conductivity. Public gradient archives such as the Chevron/Phillips data are mostly single logs taken during or soon after drilling, often in alluvium.
- Stress direction and regime *before* any deep well. No public pre-drill stress map exists at section scale. The World Stress Map is sparse in the Great Basin outside fields.
- Background seismicity at magnitudes below what regional networks detect. This has permit value and ML value.
- Incumbents skip this. Developers like Fervo spend their money on wells and fibre once they hold the land. Zanskar mines public data and large-n seismology. Enverus/A2D sells logs. Nobody is paid to measure stress cheaply across land they do not yet own.

## How it compounds into owned assets

- **Right bought:** BLM lease nominations, where the nominator sets the timing but still faces an auction. State first-file. And, most valuable, options on private ranch heat rights at $1-10/acre, where no auction exists.
- **Step-up:** the 2025-26 Utah sales show ranked EGS land clears at $111-1,207/acre against about $1-4 unranked. That is 30-300x on land alone, before any MW override.
- **Buyer:** Fervo, Ormat, Quaise and Sage, plus hyperscaler-backed developers (Google with Fervo, Meta with Sage). They pay for land already graded and permit-ready.
- **Compounding:** each hole and patch becomes a labelled pair, shallow reading against later deep truth from buyers' wells. That pair sharpens the model only for us. The superhot rung (above 300C) extends the same kit to Cascades and Newberry-type crust.

## Risks and kill conditions

- Auctions bid away the edge once a block is nominated. The private-land share must be big enough. Kill if under about 20% of top-graded acreage is private or state.
- Kill if shallow heat flow cannot predict 4 km temperature to within ±25C against FORGE and Cape well data in blind tests.
- Kill if shear-wave splitting fast directions do not match the FORGE/Cape image-log SHmax within about 20 degrees.
- The 2026 auction records may show a passing hype peak. Buyers may keep sourcing their own land.
- Drilling holes on BLM land needs a notice or permit. That takes 30-90 days (unverified).

## Cheapest first test

Desk test, $0-20k, 14-21 days. Take public FORGE data (well logs, gradient holes, the University of Utah seismic network catalogue) and Cape/Milford gradient holes. Predict 3-4 km temperature using only the shallow holes, and predict SHmax using only the surface seismic data. Pass bar: temperature within ±25C at 3 km and SHmax within 20 degrees of the FORGE image-log result. If it passes, field-test one long-dwell string in an existing Milford hole plus a 30-node patch, at about $60-100k for 60 days.

## Sources

- https://www.sltrib.com/news/environment/2025/04/11/utah-renewable-energy-blm-sale
- https://www.thinkgeoenergy.com/blm-receives-record-breaking-24m-in-winning-bids-in-utah-geothermal-lease-sale/
- https://energynews.pro/en/blm-sells-geothermal-leases-in-utah-records-reported-by-trade-press
- https://www.utilitydive.com/news/cape-station-enhanced-geothermal-utah-fervo-blm-lease/726796/
- https://gdr.openei.org/files/1209/ARMA2019_JMoore-FORGE.pdf
- https://gdr.openei.org/submissions/1570
- https://openei.org/wiki/Thermal_Gradient_Holes
- https://www.energy.gov/sites/prod/files/2014/02/f7/high_tilak_electronics_platform.pdf
- https://sandia.gov/research/publications/details/dewarless-logging-tool-1st-generation-2000-08-01
- https://egi.utah.edu/wp-content/uploads/2023/09/09.45-Emma-McConville-Fervo_EGI_Sept-19-2023.pdf
- https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2025/Titov.pdf
- https://www.weatherford.com/documents/papers/2019/increasing-reliability-of-stress-characterization-through-optimum-design-and-sensitivity-analysis-of/
