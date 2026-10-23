# H06: Logger as landman (water-well temperature and chemistry in exchange for heat-rights options)

Research note: the shared web search and fetch budgets ran out partway through this slice. Facts marked (unverified) come from background knowledge and need a primary-source check before anyone relies on them.

## Summary
- The western states hold a very large number of private wells with public logs. Each log gives location, depth and static water level, but almost never a temperature profile or full chemistry. We could log thousands of these holes for the cost of driving to them.
- History supports the idea. Several Basin and Range resources were first found when a ranch or irrigation well hit hot water: Raft River ID (irrigation wells in the 1950s), Lightning Dock NM (a stock well around 1948, now a Cyrq plant) and Newcastle UT (an irrigation well) (all unverified). Most early USGS Basin and Range heat-flow data also came from water wells.
- The deal is a free well-health check for the rancher: water level, pump drawdown, a lab test for arsenic, nitrate and TDS, and a temperature log. In return the rancher signs a 5 to 10 year option on the ranch's geothermal rights at roughly $0.5 to $2 per acre per year. The same water sample gives us geothermometers (SiO2, Na-K-Ca, B, Li, Cl) at no extra cost.
- Private heat is cheap. Raser paid $25k cash plus 25k shares for about 11,600 fee acres in Nevada, around $2 per acre up front (SEC exhibit). Texas SB 785 (2023) gives the surface owner the geothermal rights on split estates, which makes "ask the rancher" a clean title path there.
- Split estate is the main trap. On Stock-Raising Homestead Act (SRHA) patents the United States kept "all coal and other minerals", and US v. Union Oil (9th Cir. 1977) held that this includes geothermal. On that land the rancher cannot option the heat. It goes to BLM leasing, with the rancher holding only surface-damage rights. Railroad-checkerboard minerals along I-80 are a second trap (unverified).

## Key facts
- **Nevada.** NDWR runs a public online well log database. It records owner, driller, depth to water and total depth (https://www.recordcourier.com/news/2026/mar/21/county-seeks-more-information-on-wells/). It "generally contains logs for wells drilled since 1984" (https://catalog.data.gov/dataset/irrigation-wells-from-the-nevada-division-of-water-resources-well-log-database). The total count is probably above 100,000 logs (unverified). USGS documented the structure in OFR 95-460 (https://pubs.usgs.gov/publication/ofr95460).
- **Utah.** Division of Water Rights publishes yearly lists of wells drilled for 2002 to 2026 (https://waterrights.utah.gov/wellinfo/stats2k/). Roughly 2,000 to 3,000 wells are drilled a year, with over 100k in total (unverified).
- **Oregon.** OWRD has a well-report database with a map viewer (https://apps.wrd.state.or.us/apps/gw/well_log/well_log_faq.aspx). It holds roughly 400k+ reports (unverified).
- **Idaho and New Mexico.** IDWR and the NM OSE keep similar databases (unverified counts, likely 100k+ each).
- **Typical depths (unverified).** Domestic and stock wells run 30 to 150 m, irrigation wells 100 to 400 m, and the water table sits 10 to 100 m down. That leaves a usable logged water column of about 50 to 300 m. This matches the "about 500 ft" depth of the Play Fairway gradient holes that found blind systems at Gabbs Valley (124 C at 500 ft) and Granite Springs (95 C) (https://www.unr.edu/nevada-today/news/2019/geothermal-success).
- **Blind discoveries are rare and valuable.** Zanskar's "Big Blind" was billed as the first new US blind system in about 30 years (https://www.thinkgeoenergy.com/zanskar-announces-discovery-of-big-blind-geothermal-site-in-western-nevada-usa/ ; https://www.technologyreview.com/2025/12/04/1128763/ai-geothermal-zanskar/).
- **Existing well-temperature archives.** USGS published industry temperature profiles for the Great Basin (https://pubs.usgs.gov/publication/ofr99425). USGS PP 1044-B covers 1 m temperature surveys (https://app.ingemmet.gob.pe/biblioteca/pdf/USGS-PP-1044-B.pdf). Neither covers repeat logs in private water wells.
- **Private lease terms (Raser and Truckee River Ranch, 2006).** About 11,600 fee acres. $25k first-year rent, 25k shares, a $50k royalty advance and a 50-year term. The lease also carried rights on about 3M acres of lessor mineral interests with no rent due (https://www.sec.gov/Archives/edgar/containers/fix061/1103078/000119312507059509/dex1033.htm). The brief's "4,444 NV acres for $5k" figure is probably in the Raser 10-Ks (https://www.sec.gov/Archives/edgar/data/0001103078/000119312509056940/d10k.htm). Not re-verified here.
- **Federal comparison.** Raser paid about $40 per acre ($620k for 15,325 acres) at a competitive BLM sale (https://www.renewableenergyworld.com/?p=186578). Private options at $1 to $2 per acre are a 20 to 40x discount to a contested federal auction.
- **Texas SB 785.** Geothermal energy belongs to the owner of the surface estate. Effective 18 June 2023 (https://capitol.texas.gov/tlodocs/88R/billtext/html/SB00785F.htm ; https://www.thinkgeoenergy.com/new-texas-legislation-defines-ownership-of-geothermal-energy/).
- **SRHA.** US v. Union Oil, 549 F.2d 1271 (9th Cir. 1977): geothermal is a reserved mineral (https://m.openjurist.org/549/f2d/1271). About 70M acres were patented under SRHA (unverified; https://en.wikipedia.org/wiki/Stock-Raising_Homestead_Act ; https://blm.gov/programs/energy-and-minerals/mining-and-minerals/split-estate). The patent type is public in the BLM GLO records, so we can screen it before a visit.
- **Logger prices.** Off-the-shelf level/temperature/conductivity loggers (Solinst Levelogger 5 LTC, In-Situ Level TROLL) sell for roughly $1k to $3k (https://fondriest.com/solinst-levelogger-5-ltc-water-level-conductivity-loggers.htm ; unverified price). A contractor wireline temperature log typically costs $1k to $3k per well with mobilization (unverified).

## Hardware design sketch
**A. Slimline drop logger ("the landman probe").**
- **Probe.** 16 mm OD, so it fits a 3/4" or 1" sounding tube beside a submersible pump without pulling the pump. That is the key design constraint.
- **Sensors.** Glass-bead thermistor (resolution 0.001 C, accuracy 0.02 C), a pressure sensor for depth, and a conductivity cell.
- **Logging.** On-board logging at 2 Hz, with the probe lowered at 3 to 5 m per minute.
- **Winch.** A 300 m Kevlar or steel line on a battery winch with a depth encoder. Data goes to a phone app over Bluetooth.
- **Field kit.** A sample bottle kit for the lab panel: major ions, SiO2, B, Li, As, NO3.
- **BOM.** Probe about $400, winch and reel about $1,200, rugged tablet $500, sample kit $20. That is roughly $2k per kit at prototype and about $800 at scale (unverified estimates).
- **Per-well cost.** About 45 minutes of logging plus a $150 to $250 lab panel (unverified).

**B. Permanent IoT well-health probe (the retention hook).**
- **Hardware.** A thermistor and pressure transducer at a fixed depth, plus a pump-current clamp. A cellular or LoRa/satellite modem with a solar node.
- **Rancher value.** Alerts on low water level and pump failure. Ranch tank and well monitors already sell at $300 to $1,000 (unverified).
- **Our value.** A long temperature time series. It separates seasonal and pumping noise from a steady heat anomaly, and it keeps us on the property for the life of the option.
- **Cost.** BOM about $150 to $250 at scale, plus about $3 to $5 per month for data (unverified).

**Prototype time.** 6 to 10 weeks with an off-the-shelf thermistor and a 3D-printed or machined housing, for about $10k to $15k, including two kits and one calibration bath.

## What data it unlocks that is not public
- **Temperature profiles and chemistry in thousands of private holes.** State logs carry lithology and water level only. Driller-noted temperatures are rare and crude.
- **Geothermometer chemistry from private wells.** Public NBMG and USGS thermal-water data cover springs and known thermal wells. Ordinary 18 to 30 C "barely warm" wells are mostly unsampled. Those are where the outflow plumes of blind systems show up (the Basin and Range "hidden outflow" pattern; unverified).
- **Repeat and continuous series.** No one has these.
- **Access.** Incumbents (Zanskar, Ormat, Fervo) drill their own gradient holes on BLM land, at roughly $100k to $300k per hole (unverified). None of them runs a rancher-facing service, and their gradient holes sit only on land they already control.
- **A data moat that compounds.** Each logged well becomes a labeled point for the ML (heat flow plus chemistry plus water level). Each point arrives already attached to an option on the land around it.

## How it compounds into owned assets
1. Screen out SRHA and railroad-severed tracts using GLO patents and county records. Target fee-simple ranches where the surface owner holds the heat. In Utah, statute ties geothermal ownership to the surface owner (Utah Code 73-22, unverified). Texas SB 785 does the same.
2. Run the free check. Sign an option at signing for $500 to $2,000 total or about $1 per acre per year. It converts to a lease at a 10% gross royalty plus rent if exercised (unverified market terms).
3. Anomalous ranches get our own gradient holes or a farm-in. The rest of the acreage stays as cheap optionality.
4. **The step-up.** We sell a confirmed-anomaly package to Ormat, Fervo or Zanskar for a carry or a $/MWh override, using the bank model from prior work. A ranch-heat block also gives a buyer something BLM cannot: no NEPA wait for leasing and fewer bid competitors.

**Acres per field team.** A team of 2 can log 2 to 3 wells a day across 180 field days, which is 400 to 500 wells or 120 to 200 ranches. A 30 to 50% sign rate at an average of 2,000 to 5,000 deeded acres gives about **100k to 400k optioned acres per team per year** (unverified). All-in cost is about $350k for labor, truck and lab, plus option payments, or roughly $1 to $3 per acre.

## Risks and kill conditions
- **Access.** Most wells have a pump and no sounding tube. If fewer than 30% are loggable without pulling the pump, the cost per point rises 5x.
- **Groundwater flow.** Cold recharge masks heat in alluvial aquifers. If logged gradients do not predict known resources better than the public maps, kill the idea.
- **Title.** If more than 50% of target ranch acreage is SRHA or mineral-severed, the cheap right shrinks to BLM leasing.
- **Trust and law.** A free check tied to an option may look predatory. The option terms need plain disclosure and a fair price. Some states treat geothermal fluid as water and require a water right.
- **Copyability.** A competitor can copy the service. The first ranch signatures plus the dataset are the moat, so speed matters.

## Cheapest first test
- **Setup.** About $8k and 21 days. Buy one off-the-shelf thermistor drop logger, pull NDWR logs and GLO patents in two valleys (one with a known blind or KGRA system nearby, one control), and cold-call 30 ranchers.
- **Pass bar.** At least 15 wells logged, with at least 60% accessible without pulling the pump. The anomaly must show up in the known valley (gradient over 60 C/km or a geothermometer over 120 C) and not in the control. At least 3 ranchers must agree in writing to a $1 per acre option.

## Sources
- https://www.recordcourier.com/news/2026/mar/21/county-seeks-more-information-on-wells/
- https://catalog.data.gov/dataset/irrigation-wells-from-the-nevada-division-of-water-resources-well-log-database
- https://pubs.usgs.gov/publication/ofr95460
- https://waterrights.utah.gov/wellinfo/stats2k/
- https://apps.wrd.state.or.us/apps/gw/well_log/well_log_faq.aspx
- https://www.unr.edu/nevada-today/news/2019/geothermal-success
- https://www.thinkgeoenergy.com/zanskar-announces-discovery-of-big-blind-geothermal-site-in-western-nevada-usa/
- https://www.technologyreview.com/2025/12/04/1128763/ai-geothermal-zanskar/
- https://pubs.usgs.gov/publication/ofr99425
- https://app.ingemmet.gob.pe/biblioteca/pdf/USGS-PP-1044-B.pdf
- https://www.sec.gov/Archives/edgar/containers/fix061/1103078/000119312507059509/dex1033.htm
- https://www.sec.gov/Archives/edgar/data/0001103078/000119312509056940/d10k.htm
- https://www.renewableenergyworld.com/?p=186578
- https://capitol.texas.gov/tlodocs/88R/billtext/html/SB00785F.htm
- https://www.thinkgeoenergy.com/new-texas-legislation-defines-ownership-of-geothermal-energy/
- https://m.openjurist.org/549/f2d/1271
- https://en.wikipedia.org/wiki/Stock-Raising_Homestead_Act
- https://blm.gov/programs/energy-and-minerals/mining-and-minerals/split-estate
- https://fondriest.com/solinst-levelogger-5-ltc-water-level-conductivity-loggers.htm
