# H05: Quantum and novel sensors for subsurface heat and structure

Note: the web-fetch budget ran out partway through this slice. Many vendor prices are not published ("quote only"). Those are marked (unverified) and come from general industry knowledge.

## Summary
- No novel sensor here measures heat at depth directly. Gravity, magnetics, muons, InSAR and hyperspectral imaging see structure (basin depth, faults, alteration, clay caps). They never see temperature. Thermal IR from space sees the top few cm of soil, and only over strong anomalies.
- Quantum gravimeters and gradiometers are real but still early and expensive. Ground absolute units sell (Exail AQG). Mobile gradiometers are TRL 4-6: the UWA/Lockheed TAIPAN field test had about 20 Eotvos error against a 50-200 E signal. Infleqtion's mineral field test is only planned for 2027. We cannot own these cheaply, and they mostly add basin depth and fault offsets.
- Drone magnetics (OPM/cesium, about 1 kg, for example Geometrics MagArrow) and satellite TIR and InSAR (ECOSTRESS 70 m, TRISHNA 57 m, SBG-TIR) are commodity. Anyone can buy or download them, so they add no moat.
- Airborne hyperspectral imaging has already found a blind Nevada system: at Columbus Salt Marsh, mapped borates and sulfates guided about 100 two-metre temperature probes to a 4.1 x 1.7 km anomaly. But the instruments are rented from contractors, and NASA/USGS AVIRIS coverage of Nevada is public.
- The cheap, ownable, proprietary layer is **shallow ground temperature at scale**. A 2 m probe today costs $200-500 per station and takes about 2 hours (OpenEI). A robotic direct-push heat probe at under $30 per station, with satellite and hyperspectral imaging used only to pick targets, is the one sensor play that creates data nobody else has.

## Key facts
- **Exail (formerly Muquans) AQG**: a commercial cold-atom absolute gravimeter that ran in a year-long field campaign on Etna ([Exail](https://www.exail.com/product/quantum-gravimeters), [Etna story](https://www.exail.com/resources/customer-stories/a-year-long-field-campaign-on-mount-etna-to-prove-the-absolute-quantum-gravimeter-value-for-volcanology)). Price is not published. Likely about EUR 400-600k (unverified). It works at fixed stations (stop and measure), not as a survey tool.
- **TAIPAN gradiometer** (UWA with Lockheed Martin): towed on a trolley, 60 stations at 50 m spacing over 3 km. Field error was about 23 E from orientation plus about 20 E from extrapolation, against predicted signals of 50-200 E. The sensor heated from 19.6 to 37.5 C. The data are "not well quantified". The borehole version is on hold while the lab moves to New Zealand as GRADIOLAB ([arXiv 2411.15461](https://arxiv.org/pdf/2411.15461)). TRL about 4-5.
- **Infleqtion**: quantum gravity gradiometry (QGG) field test for critical minerals in Colorado, planned for 2027. No sensitivity figures are given. It is tied to H.R. 9646, the Quantum-Enhanced Critical Minerals Mapping Act of 2026, which would add QGG to USGS Earth MRI ([IntelligentCIO](https://www.intelligentcio.com/north-america/2026/08/19/infleqtion-to-test-quantum-sensing-in-colorado-to-advance-us-critical-minerals-security/)). If the bill passes, USGS would make QGG data public.
- **Q-CTRL**: a A$4.3M (about US$2.8M) grant for airborne quantum sensors for resources ([QCR](https://quantumcomputingreport.com/q-ctrl-and-partners-win-4-3-million-aus-2-8m-usd-grant-to-develop-airborne-quantum-sensors-for-resources-and-environmental-monitoring/amp)). Its demonstrated focus is gravimetric navigation at sea ([FierceSensors](https://www.fiercesensors.com/sensors/q-ctrls-quantum-gravimeter-tackles-gps-denied-navigation-sea)).
- **SandboxAQ AQNav**: magnetic-anomaly navigation for aircraft with Acubed/Airbus and DIU ([SandboxAQ](https://www.sandboxaq.com/post/sandboxaq-and-acubed-achieve-remarkable-progress-in-magnetic-navigation)). This is navigation, not exploration. It uses existing magnetic maps and does not create new ones.
- **AOSense**: sells cold-atom gravimeters, mainly to defense customers (unverified, no source fetched).
- **ANU MiniGrav**: a drone-deployable absolute gravimeter, 5 cm in size, TRL 3. It has shown 1e-5 m/s2 (about 1000 mGal), against a goal of 1e-8 (1 mGal) ([ANU](https://research.anu.edu.au/partner-with-us/technology-marketplace/minigrav-drone-deployable-miniturised-absolute-gravimeter)). Drone gravity today means MEMS IMUs with about 20 mGal bias instability ([MDPI Sensors 23:7060](https://www.mdpi.com/1424-8220/23/16/7060)). That is too coarse for geothermal faults, which need about 0.1-1 mGal.
- **Ground relative gravimeter**: the Scintrex CG-6 is the standard tool ([Scintrex](https://scintrexltd.com/product/cg-6-autograv-gravity-meter/)). Cost is about $100-130k (unverified). Ground gravity at 0.01 mGal already maps Basin and Range depth to basement well.
- **Drone magnetometer**: the Geometrics MagArrow weighs 1 kg and samples every 1 cm at up to 10 m/s. Price is quote-only ([Maverick](https://maverickdrone.com/products/geometrics-magarrow-mk2-magnetometer)), likely about $25-40k (unverified). Drone magnetics maps demagnetized altered zones on volcanoes ([EGU23-12771](https://meetingorganizer.copernicus.org/EGU23/EGU23-12771.html)).
- **2 m temperature probe**: $200-500 per station (median $300), 1.5-3 h per station, 1-2 m deep. It fails where cold aquifers mask the signal and in rocky soil. Federal permitting is usually a categorical exclusion ([OpenEI](https://openei.org/wiki/2-M_Probe_Survey)).
- **Hyperspectral**: a ProSpecTIR VS2 survey covered 380 km2 at 4 m resolution. It guided about 100 two-metre probes to a 4.1 x 1.7 km blind anomaly at Columbus Salt Marsh, NV, with geothermometers of 115-137 C ([GIS Resources](https://gisresources.com/?p=15985)). Contractor surveys cost about $20-60 per km2 (unverified). EMIT and EnMAP data are free.
- **Thermal IR**: TRISHNA has 57 m resolution, a 3-day revisit, NEdT 0.15 K and 4 TIR bands ([eoPortal](https://www.eoportal.org/satellite-missions/trishna)). Launch was set for 2025 and has likely slipped (unverified). SBG-TIR (NASA/ASI, Vega-C) has about 60 m resolution with launch about 2028-29 ([SBG](https://sbg.jpl.nasa.gov/downloads/documents/1_4_SBG-TIR_webinar20230921_Overview_Hook.pdf)). ECOSTRESS hotspot work exists ([U Twente](https://research.utwente.nl/en/publications/geothermal-hotspot-detection-with-ecostress-data-geohot-2/)). All of this is free and global, so it is a commodity.
- **InSAR**: Sentinel-1 plus NISAR show production subsidence and fault-bounded deformation at operating fields such as Brady ([GDR 941](https://gdr.openei.org/submissions/941)). It mainly sees fields that are already producing, which makes it a competitor-intel tool rather than a discovery tool.
- **Muon tomography**: proposed for low-cost reservoir density monitoring ([PNNL](https://www.pnnl.gov/publications/muon-tomography-deep-reservoirs)), with borehole detectors in development ([Utah](https://collections.lib.utah.edu/details?id=197735)). The muon flux limits it to the top few hundred metres to about 1 km. It is a monitoring tool, TRL about 4 for this use.

## What each sees for geothermal
| Sensor | Basin depth | Faults | Alteration / clay cap | Heat | Own cheaply? | Commodity? |
|---|---|---|---|---|---|---|
| Quantum gravimeter/gradiometer | Yes | Yes (offsets) | Weak (density loss) | No | No | Not yet |
| Drone mag (OPM/Cs) | Weak | Yes | Yes (demagnetized zones) | No | Yes (about $40k) | Yes |
| SQUID / drone TEM | Partly | Partly | Yes (conductive smectite cap) | Indirect | Medium | Mostly contractor |
| Satellite TIR | No | No | No | Surface only, strong anomalies | Free | Yes |
| InSAR | No | Active faults | No | No | Free | Yes |
| Hyperspectral | No | Via sinter/alignments | Yes (best) | No | Rent | Yes |
| Muon | Shallow only | Shallow | Density | No | No | No (TRL low) |
| **Shallow temperature probe** | No | Via anomaly shape | No | **Yes, direct** | **Yes** | Manual method is old, scaled data is not |

## Hardware design sketch
**Build: a robotic heat-probe rig.** A hydraulic direct-push rod rig (Geoprobe-class, or a custom unit on a UTV or tracked carrier) drives 2-6 m steel probes. Each probe carries a sealed thermistor string (5 sensors), a LoRa or satellite logger, and solar. It can be left in place 3-14 days to remove frictional heating and daily cycles. Optional add-ons: a soil-gas CO2/He sniffer, and a thermal-conductivity needle for real heat-flow estimates.
- BOM: carrier and push head about $60-90k (used units are cheaper). 200 probe and logger kits at about $150 each, so about $30k. Total prototype about **$120k** (unverified).
- Throughput target: 40-60 stations per day per 2-person crew, against about 4 per day manually. Marginal cost **under $30 per station**, against $300 today.
- Density: 1 station per 4-25 ha gives about $120-750 per km2 of proprietary heat data.
- Time to prototype: 8-12 weeks.
- Targeting layer (commodity, used cheaply): free EMIT/ECOSTRESS/TRISHNA data, USGS AVIRIS, and our own drone magnetics ($40k) over each block.
- Skip quantum gravity for now. Revisit when Exail, Infleqtion or Q-CTRL rent airborne gradiometer time, or when the USGS publishes QGG data.

## What data it unlocks that is not public
- A dense, repeatable map of shallow temperature and heat flow over large Basin and Range blocks. Public 2 m surveys number in the low thousands of stations, done in small university and DOE patches ([GDR 344](https://gdr.openei.org/submissions/344)).
- Labels. Every probe gives a true or false heat label under a public feature stack. That fixes the "F1 under 0.10, input-limited" problem only for us.
- Incumbents do not have it. Developers drill $1-3M slim holes on a handful of prospects. Zanskar and the play-fairway models buy no dense ground truth at scale (unverified for Zanskar). Satellites cannot see below the top few cm.

## How it compounds into owned assets
- Probe first on cheap ground: state first-file leases, leftover BLM noncompetitive land, and private ranch heat rights at $1-10/ac. A positive anomaly leads to buying or leasing that right before anyone else sees the signal.
- Step-up: an anomaly backed by 100+ stations plus geothermometry is a better package than a desktop prospect. That drives a higher carry or override from Ormat, Fervo or Invenergy (exact uplift unverified, but still below a confirmed resource at about $0.1M/MW).
- Every survey trains the model. Better priors mean fewer probes per discovery, which lowers cost per prospect over time.

## Risks and kill conditions
- Cold-aquifer masking hides deep systems. If more than 50% of known blind Nevada fields show no 2 m anomaly, kill or go deeper (10-30 m push or sonic holes).
- BLM land: probing before holding the lease may need a Notice or permit, and first-file rights are race-based.
- Copyable: a well-funded rival (Zanskar) can buy the same rig. The moat is the head start plus the accumulated labels, not the hardware itself.
- Quantum sensors: if an airborne QGG drops to commodity prices and USGS publishes it, structure becomes free. That is good for us as an input but no edge.

## Cheapest first test
Rent a manual 2 m probe kit or a Geoprobe and run 60 stations over 2 known blind fields (for example around Salt Wells or Columbus Marsh) and 1 cold control. Cost about $15k, 10 days. Pass: the anomaly is detected at both known fields with more than 2 C contrast over background, the control stays flat, and the cost per station is under $100 using the rig.

## Sources
- https://www.exail.com/product/quantum-gravimeters
- https://www.exail.com/resources/customer-stories/a-year-long-field-campaign-on-mount-etna-to-prove-the-absolute-quantum-gravimeter-value-for-volcanology
- https://arxiv.org/pdf/2411.15461
- https://www.intelligentcio.com/north-america/2026/08/19/infleqtion-to-test-quantum-sensing-in-colorado-to-advance-us-critical-minerals-security/
- https://quantumcomputingreport.com/q-ctrl-and-partners-win-4-3-million-aus-2-8m-usd-grant-to-develop-airborne-quantum-sensors-for-resources-and-environmental-monitoring/amp
- https://www.fiercesensors.com/sensors/q-ctrls-quantum-gravimeter-tackles-gps-denied-navigation-sea
- https://www.sandboxaq.com/post/sandboxaq-and-acubed-achieve-remarkable-progress-in-magnetic-navigation
- https://research.anu.edu.au/partner-with-us/technology-marketplace/minigrav-drone-deployable-miniturised-absolute-gravimeter
- https://www.mdpi.com/1424-8220/23/16/7060
- https://scintrexltd.com/product/cg-6-autograv-gravity-meter/
- https://maverickdrone.com/products/geometrics-magarrow-mk2-magnetometer
- https://meetingorganizer.copernicus.org/EGU23/EGU23-12771.html
- https://openei.org/wiki/2-M_Probe_Survey
- https://gdr.openei.org/submissions/344
- https://gisresources.com/?p=15985
- https://www.eoportal.org/satellite-missions/trishna
- https://sbg.jpl.nasa.gov/downloads/documents/1_4_SBG-TIR_webinar20230921_Overview_Hook.pdf
- https://research.utwente.nl/en/publications/geothermal-hotspot-detection-with-ecostress-data-geohot-2/
- https://gdr.openei.org/submissions/941
- https://www.pnnl.gov/publications/muon-tomography-deep-reservoirs
- https://collections.lib.utah.edu/details?id=197735
