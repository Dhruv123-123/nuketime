# H02. Equilibrium temperature logging of existing wells we did not drill

Note: the web fetch and search budgets ran out partway through this slice. Facts with a URL were read at the source or seen in a search result. Everything marked (unverified) comes from background knowledge and needs checking.

## Summary
- Oil and gas bottom-hole temperatures (BHTs) are read minutes to hours after the mud stops circulating, so they read cold. The standard Harrison correction adds about 10.7 C at 2 km, 17.2 C at 3 km and up to about 19 C near 3.9 km. SMU then adds up to 11 C more where gradients are above 30 C/km. That puts the total error at about 20 to 30 C, the same size as the "about 22 C cold" figure, and corrected values still only reach 5 to 10% accuracy. Below 3 to 4 km nobody has calibrated a correction.
- There are a lot of open holes we could log. Texas has about 160,000 inactive wells and 8,347 orphans. California has 34,011 idle wells, 15,922 of them idle long term. The USGS has documented 117,672 unplugged orphan wells. The Basin and Range has few: Nevada has 63 orphans and Utah 72.
- The tool is cheap. SMU's e-line temperature tool cost about $5k and reads to 0.1 C. Its 400 C memory tool cost about $45k. What costs money is the slickline truck and crew, not the sensor.
- Texas law is about to push operators. SB 1150 (2025) forces 15-year-idle wells to be plugged or returned to production, with phase-in plans running to 2040 and the requirement starting 1 Sep 2027. That gives operators a reason to say yes to a paid log or a heat-right option on their idle wellbores.
- The best play is a "Thermal Census" fleet: our own trailer winch plus memory probes, logging every open idle or orphan well we can reach before it is plugged. Some wells would also get thermistor strings left in place. Out of that we build the only large set of true equilibrium profiles at 2 to 5 km in Texas, the Gulf and California, and use it to pick which heat rights to buy.

## Key facts
**Why BHTs are wrong**
- The Harrison (1983) correction is Tcf = -16.51 + 0.01827 z - 2.345e-6 z^2 (z in m), calibrated only to about 3 km. SMU adds a second step by gradient: 0 below 20 C/km, minus up to 5 C at 20-26 C/km, plus 2-10 C at 27-31 C/km, and plus 11 C above 30 C/km. The calibrated result is good to about 5-10%, and the method is "not yet established accurately" below 3-4 km. https://smu.edu/dedman/academics/departments/Earth-Sciences/Research/GeothermalLab/DataMaps/GeothermalMapofNorthAmerica/BHTCallibrationPoster
- In the Midcontinent, comparing 33 equilibrium logs against about 500 BHTs each still left a gradient scatter of ±5 C/km after Harrison and ±2 C/km after a second correction. BHTs miss the highest and lowest gradients, and the highest ones are exactly the anomalies we want. https://www.searchanddiscovery.com/abstracts/html/2004/annual/abstracts/Blackwell.htm
- Appalachian (GPFA-AB) BHT corrections explain almost none of the variance (pseudo-R2 0.08-0.5). In some regions the best estimate was no correction at all, and in others the correction was capped at 15-38 C. https://gdr.openei.org/files/682/2_GPFA-AB_BHTCorrections.pdf
- North Dakota already logged temporarily abandoned (TA) oil wells to build static temperature profiles of the Williston Basin, and the program has run since about 2014. That proves operators will let a third party log their TA wells. https://www.dmr.nd.gov/ndgs/documents/newsletter/2019Winter/Williston_Basin_Static_Temperature_Logging_Program_Continues_to_Yield_Results.pdf and https://www.dmr.nd.gov/ndgs/documents/newsletter/Summer%202015/Preliminary%20Results%20of%20the%20Williston%20Basin%20Heat%20Flow%20Study%20Using%20Temporarily%20Abandoned%20Oil%20Wells.pdf (could not open the full text; number of wells and terms of access unverified)

**Tools and cost**
- SMU e-line tool: 0.1 C precision, 0.001 C resolution, logs at 3 m/min, 4,000 m cable, about $5k, rated 150 C. SMU memory tool: 7,600 m slickline on a hydraulic reel (trailer about 1,700 kg), about $45k, rated 400 C for 10 h, with lithium batteries at $150 per 20 h. https://smu.edu/-/media/site/dedman/academics/programs/geothermal-lab/documents/ttool-equipment-techniques.pdf
- Commercial memory gauges rated 150-177 C exist (Weatherford Quantum series). https://www.weatherford.com/drilling-and-evaluation/wireline-products/cased-hole-formation-evaluation/quantum-150c-piezo-memory-gauge/ So do high-temperature geothermal memory gauges (ProbeSensonix, Metrolog). https://probesensonix.com/downhole-memory-gauges
- Hiring a service company costs about $5k-15k per well-day for slickline, and $15k-40k for a full wireline temperature or production log (unverified). A DTS fibre run costs $50k-150k for the interrogator plus $5-15/m of sacrificial fibre and a crew (unverified). DTS is a poor fit for a fleet because the fibre usually stays in the hole.

**Well inventory (documented unplugged orphans, USGS DR1167)**
- Oklahoma 15,971, Texas 5,854, Kansas 5,477, Louisiana 4,484, California 3,338, Wyoming 1,323, New Mexico 652, Colorado 409, Montana 221, Utah 72, Nevada 63. About 90% of orphans with known depth are shallower than 5,000 ft. https://pubs.usgs.gov/publication/dr1167/full
- Texas: 8,347 orphans (Aug 2024). The RRC plugged 1,750 in 2024, but the backlog fell by only 73. https://capitol.texas.gov/tlodocs/89R/analysis/html/SB01150F.htm About 160,000 inactive wells. https://www.yahoo.com/news/politics/articles/texas-lawmakers-grill-railroad-commission-120600374.html
- California: 34,011 idle wells (2023), 15,922 of them long-term idle. CalGEM lists 5,699 likely orphan or deserted wells. https://www.fractracker.org/2024/05/california-must-improve-management-of-idle-wells
- State programs plugged 10,257 orphans with federal money through FY2025. Every one of those was a log we could have taken just before the hole was cemented. https://www.nationalacademies.org/read/29343/chapter/3

**Access and rules**
- The operator of record controls an idle or shut-in well, and the mineral lessee owns the wellbore. Running a slickline log in an open well is routine work and needs no new drilling permit, but the operator has to approve it and carry the liability (unverified, by state).
- Orphan wells are controlled by the state regulator (RRC, CalGEM, OCC). Access would come through a contract or a research agreement with the regulator or its plugging contractor (unverified).
- A fully plugged well has cement plugs in it. Re-entering one means a permit and a workover rig, at about $50k-200k (unverified). That kills plugged wells for a logging fleet. Only open (idle, TA, shut-in or not-yet-plugged orphan) wells count.
- Some states let an orphan or idle well be handed to the landowner as a water well (Texas Rule 3.14, unverified). DOE "Wells of Opportunity" funded the reuse of oil and gas wells for geothermal. https://www.energy.gov/eere/articles/doe-awards-84-million-accessing-geothermal-potential-abandoned-oil-and-gas-wells
- Water wells deep enough to matter (over 300 m) are rare outside a few basins (unverified).

## Hardware design sketch: "drop-in logger fleet"
- **Probe:** a 1.25 to 1.69 inch OD stainless or Inconel housing rated 15k psi. It holds a Pt100 or quartz thermometer (0.01 C), a pressure sensor for depth, an accelerometer, and memory sampling at 1 Hz. A Dewar flask holds the electronics to 200-260 C for 8-12 h. It fits through 2-3/8 inch tubing. BOM is about $3k-8k in prototype and about $1.5k-3k at 500 units (unverified). For comparison, SMU paid $5k for a 150 C tool and $45k for a 400 C one.
- **Delivery:** our own trailer slickline unit with 5-6 km of 0.092 inch wire, a depth encoder, a lubricator and a pressure-control stack for live wells. Used trailer units cost about $60k-150k (unverified). That is the same form factor as SMU's 1,700 kg trailer.
- **Leave-in option:** a 30-60 node digital thermistor string on armoured cable, hung for 1-12 months with a cellular uplink at the wellhead, at about $8k-20k per well (unverified). Each one turns an idle well into a permanent observation well, and the recovery curve also gives thermal conductivity.
- **Cost per well logged:** two techs plus truck and per diem come to about $1.5k-3k per day. At 1-2 wells per day, the marginal cost is about $1k-3k per well, against $5k-40k for a hired service log. A fleet of 5 trailers is about $0.8M capex and could log about 1,500 wells per year.
- **Time to prototype:** 3-4 months, using a commercial 150 C memory gauge on a rented slickline before building our own probe.

## What data this unlocks that is not public
- True equilibrium profiles to 2-5 km in Texas, Gulf, California and Permian wells. Today those places have BHTs carrying 10-30 C of error and almost no deep calibration below 3 km. SMU, USGS and the ND survey have logged only hundreds of wells in total (unverified).
- No incumbent does this. Service companies log for production, not for geothermal, and their logs belong to the operator. Zanskar and Enverus buy BHT archives, which carry the same error. The data that matters is calibration data, and only someone running a fleet produces it.
- It compounds. Every equilibrium log recalibrates the BHT correction for thousands of nearby wells. That improves our ML only, because nobody else has the labels.

## How it compounds into owned assets
- Before logging, we offer the operator either a fee ($500-2k) or a free log plus an option on the wellbore and the heat right. In return we may take over or share the plugging liability, which runs $20k-100k per well in Texas (unverified). SB 1150 deadlines make this offer more attractive after 2027.
- Where a well comes back hot, we buy the geothermal right from the surface owner. Texas assigns geothermal to the surface estate (2023 law, unverified). We would also hold the reusable wellbore for co-produced or sedimentary geothermal.
- Buyers would be Fervo, Sage, Quaise, XGS, Ormat and oil and gas operators moving into geothermal. The step-up comes from a confirmed temperature at depth plus a hole that already exists. It is still pre-PPA, though, so the step-up stays modest.

## Risks and kill conditions
- Western geothermal states have few open wells (Nevada 63 and Utah 72 orphans). The play moves to Texas, Gulf and California sedimentary heat, which is lower grade.
- Operators refuse because of liability or a lost tool. Kill it if fewer than 20% of idle-well operators say yes after 50 asks.
- Wells that were recently shut in or circulated are not at equilibrium. We need 6 months or more since the last disturbance (unverified). Many idle wells are only shallow, under 5,000 ft.
- The data is copyable once sold or disclosed. Keep the logs private until we own the rights.
- Kill it if logged temperatures fall within 5 C of corrected BHTs at most sites. In that case BHT data is good enough and we have no edge.

## Cheapest first test
Rent a slickline unit and a 177 C memory gauge, and partner with one Texas or ND operator holding 10 or more TA wells deeper than 2.5 km. Cost is about $25k-40k over about 30 days. **Pass:** we log 10 or more wells and 3 or more of them differ from Harrison/SMU-corrected BHTs by more than 8 C, plus 1 or more operators sign a heat-right or wellbore option.

## Sources
- https://smu.edu/dedman/academics/departments/Earth-Sciences/Research/GeothermalLab/DataMaps/GeothermalMapofNorthAmerica/BHTCallibrationPoster
- https://www.searchanddiscovery.com/abstracts/html/2004/annual/abstracts/Blackwell.htm
- https://gdr.openei.org/files/682/2_GPFA-AB_BHTCorrections.pdf
- https://smu.edu/-/media/site/dedman/academics/programs/geothermal-lab/documents/ttool-equipment-techniques.pdf
- https://pubs.usgs.gov/publication/dr1167/full
- https://capitol.texas.gov/tlodocs/89R/analysis/html/SB01150F.htm
- https://www.yahoo.com/news/politics/articles/texas-lawmakers-grill-railroad-commission-120600374.html
- https://www.fractracker.org/2024/05/california-must-improve-management-of-idle-wells
- https://www.nationalacademies.org/read/29343/chapter/3
- https://www.dmr.nd.gov/ndgs/documents/newsletter/2019Winter/Williston_Basin_Static_Temperature_Logging_Program_Continues_to_Yield_Results.pdf
- https://www.weatherford.com/drilling-and-evaluation/wireline-products/cased-hole-formation-evaluation/quantum-150c-piezo-memory-gauge/
- https://probesensonix.com/downhole-memory-gauges
- https://www.energy.gov/eere/articles/doe-awards-84-million-accessing-geothermal-potential-abandoned-oil-and-gas-wells
