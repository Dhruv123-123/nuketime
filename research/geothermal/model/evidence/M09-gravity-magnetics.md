# M09: Gravity and magnetics as model inputs and as our own sensors

Date: 23 Oct 2026. This file builds on `../../evidence/L14-geophysics.md` (gravity and aeromag rows, Earth MRI outlook), `../../evidence/L22-structural-ml.md` (Gabbs Valley: the target was a concealed fault intersection found from gravity and magnetics), `../../evidence/Z03-data-methods.md` (Zanskar GeoCore already uses CBA gravity HGM and RTP magnetic HGM), `../../../hardware/evidence/H05-quantum-novel-sensors.md` (CG-6, MagArrow, quantum gravity) and `M02`/`M08` (INGENIOUS, MT, Earth MRI AEM). It does not repeat them. It asks one question: **how should gravity and magnetics enter a better "how much hidden hydrothermal is there" model, and what can we build to fill the gaps?** Web budget used: 9 searches and 12 fetches. One fetch (a Stanford 2026 ML paper) was blocked by robots.txt. Physics rules of thumb are textbook knowledge and are marked (unverified).

## Bottom line

Gravity and magnetics never see heat. They see the **plumbing frame**: how deep the basin is, where buried range-front faults step, end or cross, where dikes and intrusions sit, and (for magnetics) where hot fluid has destroyed magnetite. That frame is the single best "where could fluid rise" layer for blind Basin-and-Range systems. Gabbs Valley, Granite Springs, Surprise Valley and Argenta Rise were all framed this way. The public data have three problems. (1) **Gravity is old and patchy.** The Nevada compilation is about 71,000 stations, but parts of NW and NE Nevada have only profiles tens of km apart, against an ideal of one station per 2 to 3 km. The state basement-depth grid is 2 km, from 1990, and it is only good to about ±200 to 300 m above 1.2 km depth. It is unreliable deeper. (2) **Magnetics was 82 mismatched surveys** (1947 to 2004, 400 m to 4.8 km lines) merged to a 500 m grid. That is now changing fast. Earth MRI has flown about **275,000 line-km of 200 to 400 m-spaced magnetics plus radiometrics over Nevada since 2021** (GeoDAWN 149,030 line-km over 51,857 km²; eastern Great Basin about 126,000 line-km over a 170 x 220 km box, released Feb 2026), plus 11,079 line-km of AEM+mag. Very few geothermal studies have used it yet. (3) **Everyone feeds these layers into ML as generic "gradient magnitude" rasters.** This throws away what makes them useful: the 3D geometry (fault dip, basin depth, where the basement steps). A better model should **invert gravity + new magnetics + well picks into a probabilistic 3D basement surface and fault network with uncertainty**. It should then derive physical features from that: depth to the permeable basement contact, fault-termination and step-over geometry, and magnetic-low "alteration holes". It should also carry the basement-depth error into the temperature-at-reservoir estimate. The sensor gap is local and cheap to fill: **dense ground gravity (100 to 250 m station spacing with RTK GNSS) over each candidate fault corner**, plus **drone magnetics at 25 to 50 m line spacing** to find magnetite-destroyed upflow zones the 200 m airborne lines blur. Both run on the same ranch visit as the H06 water-well drop probe. A cheap add-on to that probe (natural gamma + magnetic susceptibility) turns every logged water well into a basin-fill depth and lithology tie point.

## Findings

### F1. The Nevada gravity base is about 71,000 stations, unevenly spread, with a 2 km basement grid from 1990
- Saltus and Jachens (USGS OFR 90-404): "approximately 71,000 point observations" for Nevada. Coverage is "at least every 1-2 km" in the Nevada Test Site and east-central valleys. Parts of northwest and northeast Nevada have only profiles tens of km apart. The stated ideal is one station every 2 to 3 km in covered areas. Calculations used a 2 km grid (https://pubs.usgs.gov/of/1990/0404/report.pdf).
- The basement and cover split used an assumed 2.67 g/cm³ basement density, which the authors call poorly constrained. Cover density follows a depth curve: about 2.02 g/cm³ at the surface, 2.42 at 1.2 km, then held constant. The authors call that constant "undoubtedly in error".
- **Accuracy:** against 225 wells that hit basement above 1.2 km, predicted depth was within ±200 m for about 71% and within ±300 m for about 84%. Agreement was "much poorer" for deeper wells (same source).
- The products are still the statewide layers in use today: "Nevada Isostatic Residual Gravity Over Basement" and "Nevada Thickness of Cenozoic Deposits", on a 2 km grid, last updated 1999 (https://catalog.data.gov/dataset/nevada-isostatic-residual-gravity-over-basement ; https://catalog.data.gov/dataset/nevada-thickness-of-cenozoic-deposits2). NBMG serves an isostatic gravity map service (https://gisweb.unr.edu/nbmg/rest/services/Geology/IsostaticGravity/MapServer).
- National stations are in the PACES / USGS-NGA national gravity compilation. INGENIOUS re-gridded Great Basin complete Bouguer and isostatic gravity and their horizontal gradients (M02). The exact national station count was not checked here (unverified; of order 1 to 2 million US stations).

### F2. Local gravity surveys are where the blind-system work happens, and they are small
- PFA phase 2 collected **237 to 415 new gravity stations per prospect** (L01). Spring/Snake Valley (USGS OFR 2006-1160) added 545 stations to fill sparse Spring Valley and inverted for pre-Cenozoic basement using deep oil and gas wells as ties (https://pubs.usgs.gov/of/2006/1160).
- **Granite Springs Valley (USGS, pubs 70259621):** ground magnetics, gravity, MT and rock-property data, derivative filters to find buried faults, and a depth-to-basement inversion. The results: the basin is deepest on the west, a gravity high marks an intra-basin horst, and a NW magnetic high is an unexposed basement dike swarm. **The geothermal system, the horst, the dike swarm and a terminating normal fault zone all coincide.** It has no clear surface manifestation. Follow-up targets were the horst's west flank and "structural corners" (https://pubs.usgs.gov/publication/70259621).
- **Argenta Rise (USGS, pubs 70271418):** high-resolution gravity + MT + rock density/susceptibility + new GeoDAWN aeromagnetics, with joint 2D gravity-magnetic models on crossing profiles. Key point: **the gravity-derived basement depth matches the base of the shallow conductors.** This suggests the fluids sit in basin fill above basement (https://pubs.usgs.gov/publication/70271418). M02 records that Argenta was a drilling miss/marginal, so this is also a lesson: gravity found the frame, but the frame was not hot enough.
- **Surprise Valley, CA (Glen et al., NASA SIERRA UAS magnetics, 2012):** a buried, faulted mafic dike shows as an intra-basin magnetic high with no surface expression. "All of the major hot springs on the east side of the valley lie along the edge of the high," and they sit where the high steps, bends or breaks (https://www.usgs.gov/publications/correlation-geothermal-springs-sub-surface-fault-terminations-revealed-high-resolution). This is the clearest public evidence that **high-resolution magnetics finds the exact fault-termination points that host upflow**.

### F3. The old statewide magnetics is 82 mismatched surveys on a 500 m grid
- USGS DS 234 (Nevada aeromagnetic compilation, 2006): **82 surveys flown 1947 to 2004**. Line spacing ranges from 400 m or less to 4,800 m for the NURE surveys, which cover the whole state. All are continued to 305 m above ground and merged to a 500 m grid. "The data from these surveys are of varying quality." Much pre-1975 data were digitized from hand-contoured maps. Wide NURE lines create "pearl string" artifacts and false lineations perpendicular to flight lines (https://pubs.usgs.gov/ds/2006/234/nv_desc.htm).
- **Implication:** an RTP-magnetic-gradient raster built from this grid (the INGENIOUS and GeoCore feature, Z03) has fake gradients along old flight lines and misses anything narrower than about 1 km. An ML model can learn artifacts as signal.

### F4. Earth MRI has re-flown a large part of Nevada since 2021, and geothermal has barely used it
| Survey | Line-km | Spacing / height | Area | Dates | DOI |
|---|---|---|---|---|---|
| GeoDAWN mag + radiometrics (W Nevada, Walker Lane; USGS + DOE GTO) | 149,030 | Area 1 (Clayton Valley): 200 m lines, 100-150 m AGL. Area 2 (geothermal focus): 400 m lines, 150-200 m AGL | 51,857 km² | Nov 2021 to Nov 2022 | 10.5066/P93LGLVQ |
| Eastern Great Basin mag + radiometrics (NV) | about 126,000 | 200 m E-W lines, 2 km ties, 100 m AGL | up to 170 x 220 km | Aug 2024 to May 2025, released 19-20 Feb 2026 | 10.5066/P13VSMZ3 |
| Basin and Range AEM + mag (NV/OR) | 11,079 | HELITEM, about 400 m depth of investigation | Clayton Valley, Rhyolite Ridge, McDermitt, Railroad Valley | released Sep 2025 | 10.5066/P1UKDJSM |
| Eastern Oregon Blue Mountains mag + radiometrics (with DOGAMI) | not stated | 200 m lines, 100 m AGL | Baker to Union counties | flights start Oct 2026 | pending |

Sources: https://catalog.data.gov/dataset/geodawn-airborne-magnetic-and-radiometric-surveys-of-the-northwestern-great-basin-nevada-a ; https://www.usgs.gov/data/airborne-magnetic-and-radiometric-survey-over-a-part-eastern-great-basin-nevada-2024-2025 ; https://data.usgs.gov/datacatalog/data/USGS:68c9d8a2d4be0274ff4beaa4 ; https://www.usgs.gov/index.php/data/regional-airborne-electromagnetic-and-magnetic-surveys-basin-and-range-province-nevada-oregon ; https://www.usgs.gov/news/state-news-release/media-alert-low-level-flights-image-geology-over-eastern-oregon
- The eastern Great Basin survey cost about **$4.7 million** in Bipartisan Infrastructure Law money and was designed with NBMG (https://www.usgs.gov/index.php/news/state-news-release/bipartisan-infrastructure-law-helps-remap-nevada-critical-minerals).
- GeoDAWN was explicitly co-led by DOE GTO to rank western Nevada geothermal potential with ML (https://www.thinkgeoenergy.com/multiagency-initiative-starting-work-on-critical-minerals-and-geothermal-energy-in-nevada/). GeoDAWN lidar is also on GDR (e.g. NW Elko County, https://gdr.openei.org/submissions/1526).
- The Oregon release names **"potential geothermal resources"** and geologic hydrogen as purposes. This is the first time an Earth MRI mag release has done so.
- **Rough coverage estimate (unverified):** Nevada is about 286,000 km². GeoDAWN (about 52,000 km²) plus the eastern box (perhaps 30,000 to 37,000 km², at 200 m) means **about 30% of Nevada now has modern 200 to 400 m magnetics**, up from almost none in 2020. North-central Nevada (Humboldt to Elko trend) and the south are mostly still on the 1947 to 2004 patchwork.
- **What 200 to 400 m lines can and cannot see (physics, unverified):** at 100 to 150 m height they resolve bodies about 200 to 400 m across. That is enough for dikes, buried range-front faults and step-overs. It is not quite enough for a 100 to 300 m-wide demagnetized upflow zone over a fault intersection. That needs 25 to 50 m lines at about 30 to 50 m height (drone).

### F5. How gravity and magnetics map to hidden-hydrothermal physics
- **Gravity gradients = buried fault planes.** Steep horizontal gravity gradients sit over basement steps, so their maxima trace concealed range-front faults. Where gradients **end, bend or cross** you have a fault termination, step-over or intersection. These are the Faulds settings that host most Great Basin systems (L02, L22). PFA weighted "intersecting/terminating gravity gradients" directly (L01, L14).
- **Gravity inversion = basin depth = reservoir depth and temperature.** In fault-hosted Basin-and-Range systems the outflow often sits in basin fill, and the upflow sits in fractured basement at the range-front fault. Depth to basement times the local gradient gives the temperature at the basement contact. A ±300 m basement error at 60 °C/km is a ±18 °C error at the target. That is the difference between a 130 °C binary-grade resource and a 112 °C dud (arithmetic on F1 numbers).
- **Magnetic lows = hydrothermal alteration.** Hot acidic fluids turn magnetite to pyrite or clay, so long-lived upflow zones in volcanic or intrusive rock show as local magnetic lows. Gabbs Valley had a magnetic low on its blind target (L22). Drone magnetics maps demagnetized altered zones on volcanoes (H05). In weakly magnetic sediment or carbonate this signal disappears (unverified).
- **Magnetic highs = dikes and intrusions = fault-guiding structures** (Surprise Valley, Granite Springs). They also mark the edges of granitic plutons, which raise heat production in the basement.
- **Radiometrics (flown with the same Earth MRI surveys)** map K, U and Th at the surface. They show potassic alteration and also give upper-crust radiogenic heat production. Both are free side layers (unverified for geothermal use at scale).
- **Potential-field data are non-unique.** A gravity low can be deep basin fill or low-density altered volcanic rock. Joint inversion with well picks, MT (M08) and AEM breaks the ambiguity. Argenta Rise shows the method working: gravity basement depth matched the base of the MT conductors.

### F6. How the current models use these data, and what they throw away
- INGENIOUS and Zanskar's open GeoCore model use **CBA gravity horizontal-gradient magnitude and RTP magnetic horizontal-gradient magnitude** as raster features at about 250 m to 2 km cells (Z03, M02). Faulds PFA used gravity gradients as one of 9 expert-weighted layers (L01).
- A gradient raster says "something steep is here". It does not say which way the fault dips, how deep the basement is, whether two gradients actually intersect at depth, or whether the anomaly is an artifact of an old flight line. The USGS Bayesian neural-net PFA study used "geological and geophysical features related to permeability and heat" with confidence maps, but at the same coarse level (https://pubs.usgs.gov/publication/70241433).
- No public geothermal ML model we found uses (a) the new Earth MRI magnetics statewide, (b) a probabilistic basement surface, or (c) radiometric heat production. This is the "first reader of new public releases" angle from L14, applied to potential fields.

## Datasets

| Dataset | Access | Coverage | Value for blind detection |
|---|---|---|---|
| Nevada gravity, OFR 90-404 / "Isostatic residual gravity over basement" / "Thickness of Cenozoic deposits" | Free, data.gov, NBMG map service | Statewide, about 71k stations, 2 km grid, 1990/1999 | Basin depth prior and regional gradients. Coarse; ±200-300 m above 1.2 km, worse deeper |
| PACES / USGS-NGA national gravity compilation | Free (USGS, UTEP PACES legacy) | National, uneven density | Raw stations to re-grid and re-invert with modern terrain corrections (lidar DEM) |
| INGENIOUS gravity and magnetic layers (CBA, isostatic, HGM, RTP) | Free, GDR DOI 10.15121/1881483 | Great Basin | Baseline features already used by Zanskar. Table stakes |
| Nevada aeromag compilation, USGS DS 234 | Free | Statewide, 82 surveys, 500 m grid | Regional structure. Has flight-line artifacts; misses features under about 1 km |
| GeoDAWN mag + radiometrics | Free, DOI 10.5066/P93LGLVQ | 51,857 km² W Nevada / Walker Lane, 200-400 m lines | High. Buried faults, dikes, alteration lows in the main blind-system belt |
| Eastern Great Basin mag + radiometrics | Free, DOI 10.5066/P13VSMZ3 (Feb 2026) | about 170 x 220 km E Nevada, 200 m lines | High and almost unused for geothermal; covers carbonate-aquifer and deep-basin plays |
| Earth MRI AEM + mag, Basin and Range | Free, DOI 10.5066/P1UKDJSM | 11,079 line-km NV/OR | Clay caps (M08) plus mag on the same lines |
| Eastern Oregon Earth MRI mag (2026) | Pending | Blue Mountains | Names geothermal as a purpose; future layer |
| Local prospect gravity (PFA, USGS OFRs, INGENIOUS sites) | Free, scattered in OFRs and GDR | Dozens of prospects, 200-550 stations each | Labels for "what dense gravity sees" vs regional |
| Oil, gas and water well basement picks (NBMG, NDWR well logs, D03) | Free, needs digitizing | Thousands of wells | Ties for basement inversion; key to cutting depth error |
| Rock density and susceptibility measurements (USGS studies) | Free, in papers | Sparse | Needed to set inversion priors |

## What dominates uncertainty

1. **Depth to basement below about 1.2 km.** The statewide grid is only checked to ±200-300 m above 1.2 km and is "much poorer" deeper. Deep basins are exactly where blind outflow hides and where reservoir temperature depends on depth.
2. **Density of the basin fill.** One assumed density curve for the whole state drives most of the depth error. Altered or welded volcanic fill breaks it.
3. **Station gaps.** Profiles tens of km apart in NW and NE Nevada cannot locate a fault corner. A 1 to 2 km fault step-over is invisible at 5 to 10 km station spacing.
4. **Non-uniqueness.** A magnetic low can be alteration, non-magnetic sediment or a reversed-polarity flow. A gravity low can be deep fill or altered rock. Without well ties or MT the model cannot tell.
5. **Artifacts in old magnetic grids** that ML can learn as signal.
6. **The frame is not the heat.** Argenta Rise had a good gravity/magnetic frame and was not hot enough. Gravity and magnetics raise the odds of permeability; heat must come from other layers (M04-M08).

## What a sensor could fill

- **Dense ground gravity at fault corners (best fit).** A rented or bought relative gravimeter (Scintrex CG-6, about $100-130k to buy, H05; rental perhaps $1-2k per week, unverified) with RTK GNSS for 2-3 cm heights. Read 100 to 250 m spacing along roads and two-tracks across each candidate step-over. A two-person crew does about 40 to 80 stations a day (unverified). 300 stations over one corner is about one week. This turns a 2 km regional guess into a fault map good to about 100 m, and it is casual use (no ground disturbance) under the BLM rules from H13. It is cheaper per target than MT and should be done first, so MT carpets (M08) go only where the fault geometry is right.
- **Drone magnetics at 25 to 50 m line spacing.** MagArrow-class (about 1 kg) on a mid-size drone, about $25-40k (unverified, H05). It resolves the 100 to 300 m demagnetized upflow zone that 200 to 400 m Earth MRI lines blur. One flight day covers a few km² (unverified). Best in volcanic and granitic hosts, weak in carbonate and thick sediment.
- **Add natural gamma + magnetic susceptibility to the H06 water-well drop probe.** Both are small, cheap downhole sensors (unverified cost, low thousands of dollars). In each ranch well they give the depth of the fill-to-bedrock contact (where the well reaches it) and a lithology log. Each one is a free tie point for the basement inversion and a density/susceptibility prior. Hundreds of ranch wells per county could cut the ±300 m basement error sharply where wells are deep enough.
- **Do not build airborne gravity or quantum gradiometers yet.** H05 already found drone gravity drifts about 20 mGal and quantum gradiometers are not field-ready. A Basin-and-Range fault step is about 1 to 10 mGal over a few hundred m (physics, unverified), so ground gravity at 0.01 mGal precision is the right tool now.
- **Hand-held susceptibility and density on outcrop, mine waste and core** (KT-10-class meters, unverified cost about $10k). This sets inversion priors per valley.

## Implications for a better model

1. **Replace gradient rasters with a probabilistic 3D frame.** Jointly invert statewide gravity, the new Earth MRI magnetics, well basement picks and MT/AEM into an ensemble of basement surfaces and fault planes (many plausible versions, not one). Derive features from each version: depth to basement, fault dip, distance to a fault termination or intersection *at depth*, step-over width. Pass the spread of the ensemble to the heat model as an uncertainty term.
2. **Make basement depth a direct input to the temperature-at-reservoir estimate.** Temperature at the permeable basement contact = surface temperature + gradient x depth. Basement depth error then becomes reservoir temperature error, so it shows up in the resource-size (MWe) uncertainty, as the USGS volume method needs (M01).
3. **Use the new magnetics in two ways.** Use it as a structure layer (dikes, buried faults, matching Surprise Valley and Granite Springs) and as an alteration layer (local lows in otherwise magnetic host rock). Mask the alteration term where the host is non-magnetic, using geology maps and radiometrics.
4. **Add radiometric heat production** (K, U, Th from Earth MRI) as a cheap basement heat-source feature.
5. **Clean the old magnetics.** Flag cells where only NURE 4.8 km lines exist so the model does not learn flight-line artifacts. Train and test separately on Earth MRI-covered and old-grid-only areas. That split also measures how much the new data improve ranking.
6. **Value-of-information gravity.** Rank candidate fault corners by how much a 300-station ground gravity survey would change their probability. Spend the cheap gravity there first, then MT, then gradient holes. This is the funnel from L14 with a cheap step added before MT.
7. **Every water well we log becomes a basement tie.** The drop-probe add-on builds a private dataset that sharpens the public gravity inversion. Zanskar cannot get it from public sources.
8. **Scale and optimism.** About 30% of Nevada got modern magnetics in 2021 to 2026, and more is coming (Oregon 2026). Being first to turn each release into a fault-corner map and file on the corners is a repeatable, data-release-driven land play.

## Sources
- https://pubs.usgs.gov/of/1990/0404/report.pdf
- https://catalog.data.gov/dataset/nevada-isostatic-residual-gravity-over-basement
- https://catalog.data.gov/dataset/nevada-thickness-of-cenozoic-deposits2
- https://gisweb.unr.edu/nbmg/rest/services/Geology/IsostaticGravity/MapServer
- https://pubs.usgs.gov/of/2006/1160
- https://pubs.usgs.gov/ds/2006/234/nv_desc.htm
- https://catalog.data.gov/dataset/geodawn-airborne-magnetic-and-radiometric-surveys-of-the-northwestern-great-basin-nevada-a
- https://www.usgs.gov/data/airborne-magnetic-and-radiometric-survey-over-a-part-eastern-great-basin-nevada-2024-2025
- https://data.usgs.gov/datacatalog/data/USGS:68c9d8a2d4be0274ff4beaa4
- https://www.usgs.gov/index.php/news/state-news-release/bipartisan-infrastructure-law-helps-remap-nevada-critical-minerals
- https://www.usgs.gov/index.php/data/regional-airborne-electromagnetic-and-magnetic-surveys-basin-and-range-province-nevada-oregon
- https://www.usgs.gov/news/state-news-release/media-alert-low-level-flights-image-geology-over-eastern-oregon
- https://www.thinkgeoenergy.com/multiagency-initiative-starting-work-on-critical-minerals-and-geothermal-energy-in-nevada/
- https://gdr.openei.org/submissions/1526
- https://pubs.usgs.gov/publication/70259621
- https://pubs.usgs.gov/publication/70271418
- https://www.usgs.gov/publications/correlation-geothermal-springs-sub-surface-fault-terminations-revealed-high-resolution
- https://pubs.usgs.gov/publication/70241433
