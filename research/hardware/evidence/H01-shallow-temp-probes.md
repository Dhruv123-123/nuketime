# H01: Shallow temperature probes and a "heat carpet" for blind geothermal discovery

Note on method: about 17 web searches and 7 page reads. The WebFetch budget ran out partway through, so several numbers (modern gradient-hole cost, component prices, crew rate) come from memory and are marked "(unverified)".

## Summary

- The UNR/DRI/USGS "2 m probe" method (Coolbaugh, Sladek, Zehner, Kratt, from about 2006) works. It found blind systems with no surface springs at Teels Marsh (2008), Emerson Pass, Columbus Salt Marsh, Hawthorne, and Gabbs Valley. Gabbs Valley was later confirmed by gradient wells at about 120 C at 150 m.
- It is cheap: OpenEI lists $200 to $500 per station (median $300) and 1.5 to 3 hours per station. A one-time 2 m reading costs roughly 1/30 to 1/500 of a temperature-gradient hole.
- The weak spot is noise. One-shot readings carry several degrees of error from the seasonal wave and from albedo, and the anomaly-to-background contrast changes through the year. Months of logging at three depths per probe largely removes this. Nobody does it at scale today.
- **New regulatory tailwind (31 Aug 2026):** BLM IM 2026-024 now treats direct-push temperature probing with rods under 2 inches, and temporary battery sensors in small holes, as casual use. That needs only a Notice of Intent and a 15-day answer, with no permit. A mass probe carpet on BLM land is now legal by default.
- Candidate play, the "heat carpet": a robot-emplaced grid of $50 to $80 logging probes with LoRa and satellite backhaul. It costs about $1.5k to $3k per km2 and turns a whole basin into a proprietary heat-flux map. We take options on ranch and state heat rights first, then carpet, then nominate or file. This is the cheapest compounding "own holes" dataset we have found.

## Key facts with numbers

- **Method.** A steel tube is driven to 2 m and a high-precision RTD is left in place for at least an hour. Solar and seasonal effects are "mostly damped out" below 1 m. Cost is $200 / $300 / $500 per station (low / median / high), and time is 1.5 / 2 / 3 hours per station. OpenEI lists 8 activities across 5 areas, citing Coolbaugh et al. 2007, Kratt et al. 2009, Sladek et al. 2009 and Skord et al. 2011. https://openei.org/wiki/2-M_Probe_Survey
- **Field rate.** Using a portable gas rock drill, crews install about 10 probe holes per 8-hour day. Multi-depth sensors at 1, 1.5 and 2 m give a shallow gradient. https://openei.org/wiki/Improvements_in_Shallow_(Two-Meter)_Temperature_Measurements_and_Data_Interpretation In soft alluvium, a rotary hammer and 2-person crew reportedly manages 30 to 40 per day (unverified).
- **Seasonal science.** Albedo differences shift 2 m temperatures by "up to several degrees C". The UNR team corrects this with ASTER albedo. Long-term monitoring showed anomaly contrast is smallest about two months after the coldest air temperatures (February to March). (Same source.)
- **First-principles check.** The annual damping depth is d = sqrt(2 kappa / omega). Dry alluvium has kappa of about 0.5e-6 m2/s, which gives d of about 2.2 m. At 2 m the surface annual swing (±12 to 15 C in Nevada) is cut to about 40%, which is still ±5 C, with a phase lag of about 50 days (unverified calculation). A single snapshot cannot cleanly separate a +3 C anomaly from that swing. A 6 to 12 month record at 3 depths can fit amplitude and phase per probe and leave the steady geothermal residual. This is the core physics case for logging probes.
- **Salt Wells.** Winter surveys ran at a 3 to 10 C background, 24-hour stability was ±0.1 C, and the anomaly threshold was 12 C. https://openei.org/wiki/2-M_Probe_Survey_At_Salt_Wells_Area_(Coolbaugh,_Et_Al.,_2006)
- **Hit rate in practice ("Boom and Bust" paper).** About 11 areas were surveyed. Roughly 7 anomalies were found, including a new system at Emerson Pass, a blind anomaly at Columbus Salt Marsh, and 3 at Hawthorne (one new). Dead Horse Wells exceeded 37 C over more than 1.5 km. Six valleys came back blank, each with more than 20 probes at about 1 km spacing. Astor Pass got more than 100 points. https://openei.org/wiki/Boom_And_Bust_With_The_Latest_2M_Temperature_Surveys-_Dead_Horse_Wells,_Hawthorne_Army_Depot,_Terraced_Hills,_And_Other_Areas_In_Nevada
- **Teels Marsh.** This was the first blind find by 2 m mapping in a basin with no known springs or wells. Two hot zones run along a fault for a little over 2 miles combined. https://www.unr.edu/nevada-today/news/2008/researchers-make-geothermal-discovery-in-mineral-county
- **Gabbs Valley (2018).** A 2 m anomaly plus gradient wells at about 120 C at 150 m confirmed a blind system and validated play fairway analysis. https://www.usgs.gov/publications/discovery-blind-geothermal-system-southern-gabbs-valley-western-nevada-through
- **Count of blind systems found.** No source gives a single total. From the papers read, at least 5 to 8 blind or previously unknown systems were first flagged or confirmed by 2 m surveys (my count, unverified). Public 2 m data exist as one-time snapshots in the Nevada Play Fairway and INGENIOUS compilations and on the GDR. https://gdr.openei.org/submissions/1086
- **Gradient hole cost.** OpenEI lists $5 / $16.50 / $50 per ft (low / median / high), for holes usually under 500 ft, so about $8k median for 500 ft (dated figures). https://openei.org/wiki/Thermal_Gradient_Holes Modern 1,000 to 2,000 ft gradient wells in Nevada run about $150k to $500k each including permitting and bonding (unverified). Permitting is the real cost and takes months (unverified).
- **BLM casual use (IM 2026-024, effective 31 Aug 2026, expires 30 Sep 2029).** The following now count as casual use: "shallow probing for ground temperature... hand-held or OHV-mounted direct-push probes with rods under 2 inches", "temporary placement of battery-operated sensors in small holes", and near-surface installations under 10 ft. A Notice of Intent goes to the field office, which must answer within 15 days. There is no numeric cap on sites and no stated maximum sensor duration. Truck-mounted or mechanized drilling and earth-moving are excluded, and off-road travel must follow the travel plan. https://www.blm.gov/policy/im-2026-024 and https://www.thinkgeoenergy.com/blm-to-no-longer-requires-permits-for-casual-use-geothermal-exploration-activities/
- **Competitor signal.** Zanskar announced "Big Blind" in western Nevada (Dec 2025), found through AI plus its own drilling. https://www.axios.com/2025/12/04/nevada-energy-ai-models-discovery-research

## Hardware design sketch: the "heat carpet"

**Probe (one unit):**
- 2.0 m by 16 to 19 mm OD rod, either a disposable steel drive point or a fiberglass sleeve left in the ground. Under the 2-inch BLM rule.
- 3 digital sensors at 1.0, 1.5 and 2.0 m (TMP117 class, ±0.1 C, about $3 each). Plus a surface air and albedo sensor in the cap.
- STM32WL LoRa SoC, about $6. One Li-SOCl2 D cell (19 Ah, about $15) gives 2+ years at hourly samples and 4 uplinks a day.
- Potted cap, about $5.
- Rod $8 to $15.

| Item | Prototype BOM | At 10k units |
|---|---|---|
| Probe (rod, sensors, LoRa, battery, cap) | ~$150 | **$45 to $70** (unverified) |
| Gateway (solar, LoRa, Starlink Mini or Iridium) | ~$1,500 | ~$800 |

One gateway covers about 10 to 15 km of open basin line of sight (unverified).

**Emplacement:**
- **Option A, crew.** UTV with a hydraulic direct-push or rotary hammer and 2 people. About 40 probes a day, so about $40 per probe in labor (unverified).
- **Option B, robot.** An autonomous UTV or tracked rover with a GPS waypoint list and a percussion arm. About 6 minutes per push gives 80 to 120 a day, running unattended at night with remote supervision. It can also pull probes on recovery.
- **Drones** cannot drive a 2 m rod, because the impulse needed is far beyond a drone's thrust. A drone could drop 0.3 to 0.5 m darts. That depth sees the full seasonal wave and needs a heavier model, but it could work as a coarse first-pass "sparse carpet" in the logging regime. The best split: drones scout and deliver, rovers push.
- Thousands of probes is realistic. 2,000 probes is about 20 rover-days.

**Deployment cost:**
- Spacing of 250 m gives 16 probes per km2, about $1,500 to $2,500 per km2 for hardware plus install, before any probe recovery or reuse.
- A 1 km reconnaissance grid costs about $150 per km2.
- A 100 km2 basin at 250 m spacing comes to about $200k, roughly one modern gradient well. It returns a 12-month heat map of the whole basin instead of one point.

**Software:**
- Fit each probe's annual and diurnal harmonics, using the three depths to estimate local diffusivity.
- Remove albedo and elevation effects.
- Invert the residual to shallow conductive heat flux, then join it with structure maps for ML.

**Time to prototype:** 6 to 8 weeks for 20 units and 1 gateway. A robot pusher retrofit is about 4 to 6 months (unverified).

## What data it unlocks that is not public

- **Time series instead of snapshots.** Public 2 m data are single readings taken in different seasons, with ±several C noise. Year-long, 3-depth records give corrected heat flux at each point. That would be the first labelled, dense, low-noise shallow heat dataset at basin scale.
- **Density.** Public surveys use tens to hundreds of points per area. A carpet uses thousands. Spatial ML on fault intersections can then train against real heat, not the sparse labels that cap public models at F1 below 0.10.
- **Negatives.** Blank basins carpeted to a known detection limit are just as valuable. Nobody publishes clean negatives.
- **Why incumbents skip this.** Operators like Ormat drill near known fields. Zanskar optimizes ML on public data plus its own gradient wells. Academic groups lack the capex for thousands of loggers. And until August 2026, mass probing on BLM land carried permit risk.

## How it compounds into owned assets

1. Pick target basins with the public ML plus the Chevron and Phillips archive.
2. On private ranch land, sign heat-rights options ($1 to $10 per acre) before probing. On state land, first-file. On BLM land, carpet under the casual-use NOI, then nominate parcels for lease or take leftover noncompetitive leases at $1 per acre per year.
3. The carpet turns "cheap acreage" into a "drill-ready shallow anomaly". One gradient well funded by a partner then converts it to a confirmed resource.
4. Sell or farm out to Ormat, Fervo or Invenergy for a carry or a $/MWh override. The step-up per prospect is probably $1M to $5M at the drill-ready stage (unverified).
5. Every basin carpeted, hit or miss, retrains the model. Hit rates rise and cost per discovery falls.

## Risks and kill conditions

- **Depth blindness.** 2 m only sees systems whose heat reaches the near surface. Deep systems under cold aquifer sweep look blank. Kill if more than half of known Great Basin producing fields show no 2 m anomaly on a carpet test (unverified threshold).
- **Signal leakage.** A filed NOI tells the BLM, and maybe FOIA requesters, where we are looking. Mitigate by optioning private and state land first, or by filing broad NOIs.
- **Field office variability.** Offices can still decide a project is "significant disturbance". The IM expires in 2029.
- **Hardware attrition** from cattle, flash floods and theft. Kill if more than 20% of probes are lost per year.
- **Copyability.** The method is public, so the moat is speed, volume and land already optioned, not secret physics.

## Cheapest first test

- **What:** 40 logging probes (about $6k BOM plus 1 gateway) across a known blind anomaly, such as Teels Marsh or Dead Horse Wells, and its background. Use private land or a casual-use NOI.
- **Time:** 2 weeks to build, 2 days to install, 90 days of logging.
- **Cost:** about $15k all in.
- **Pass:** after seasonal fitting, the corrected residual separates anomaly from background with SNR of 3 or better, and the residual noise is under 0.3 C. Also, a 0.5 m dart subset tracks the 2 m result well enough (r of 0.8 or better) to justify drone darts.

## Sources

- https://openei.org/wiki/2-M_Probe_Survey
- https://openei.org/wiki/Improvements_in_Shallow_(Two-Meter)_Temperature_Measurements_and_Data_Interpretation
- https://openei.org/wiki/2-M_Probe_Survey_At_Salt_Wells_Area_(Coolbaugh,_Et_Al.,_2006)
- https://openei.org/wiki/Boom_And_Bust_With_The_Latest_2M_Temperature_Surveys-_Dead_Horse_Wells,_Hawthorne_Army_Depot,_Terraced_Hills,_And_Other_Areas_In_Nevada
- https://www.unr.edu/nevada-today/news/2008/researchers-make-geothermal-discovery-in-mineral-county
- https://www.usgs.gov/publications/discovery-blind-geothermal-system-southern-gabbs-valley-western-nevada-through
- https://openei.org/wiki/Thermal_Gradient_Holes
- https://www.blm.gov/policy/im-2026-024
- https://www.thinkgeoenergy.com/blm-to-no-longer-requires-permits-for-casual-use-geothermal-exploration-activities/
- https://gdr.openei.org/submissions/1086
- https://www.axios.com/2025/12/04/nevada-energy-ai-models-discovery-research
