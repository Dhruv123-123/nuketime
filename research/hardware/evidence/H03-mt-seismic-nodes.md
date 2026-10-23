# H03: Low-cost MT and passive seismic nodes for geothermal

Note on method: about 20 web searches and 12 page fetches. The shared fetch budget ran out partway through, so several vendor prices below come from general knowledge and are marked "(unverified)".

## Summary
- MT is the standard geothermal step before drilling, because it maps the conductive smectite clay cap above hot reservoirs. It is sold as a contractor service at roughly $400 to $2,300 per station. Surveys stay sparse, usually 50 to 300 stations on a 0.5 to 1 km grid.
- The cost is in the magnetic sensors and the crew, not the electronics. A commercial 5-channel station (Phoenix MTU-5C or Metronix ADU-08e plus 3 induction coils) costs about $50k to $100k (unverified). The 24-bit ADC, GNSS and logger inside it cost under $200 in parts.
- The literature already shows a way to cut cost 10x. Use dense, cheap electric-field-only "telluric" nodes plus a few full magnetic reference stations, since magnetic fields barely change over a few km. Münster's EDE logger and the NRIAG/Münster LPTR are both low-cost 24-bit, GPS-timed telluric loggers that matched an ADU07 MT system.
- Dense passive seismic is already cheap and proven. SmartSolo nodes run about 30 days at 250 Hz. Arrays of 450 to 500 nodes have imaged Hengill (Iceland) and Cornwall (UK) geothermal systems. Zanskar hires for "large-N seismic arrays", so seismic is not a moat for us. Dense MT is the open gap.
- Candidate play: "Dense-EM heat-rights bank". Run our own months-long, ultra-dense telluric/MT carpets (100 m spacing, 1,000+ nodes) over ranch and state land we can option cheaply. Invert the data in 3D, and then drill temperature-gradient holes only where the clay cap and the upflow line up. Own the rights and the data cube.

## Key facts (numbers and sources)
- **What MT resolves.** It maps the smectite clay ring and cap around a geothermal system. Low-temperature clay alteration (conductive) gives way to resistive high-temperature alteration below. Depth range runs from tens of meters to tens of km. It also senses faults, fracture zones, porosity and fluid type ([OpenEI MT](https://en.openei.org/wiki/Magnetotellurics)).
- **Contractor cost per station.** OpenEI gives about $522 low, $1,739 median and $2,298 high per station, and 1.7 to 7.5 crew-days per 10 stations. Its currency-year is not stated ([OpenEI MT](https://en.openei.org/wiki/Magnetotellurics)). A Quantec MT survey in BC invoiced $122,071 for a program logging 321 sites, about $380 to $400 per site. This was a dense mining grid, so the per-site figure is rough ([BC ARIS 39168](https://apps.nrs.gov.bc.ca/pub/aris/Report/39168.pdf/)). Western US geothermal broadband MT from Quantec, Zonge or Enthalpion is commonly $1,500 to $4,000 per station with mobilization (unverified). A recent example is NREL's NV22 MT report by contractor Enthalpion ([GDR 1514](https://gdr.openei.org/files/1514/)).
- **Instrument kit.** A Phoenix 5-channel station is a 24-bit 2E+3H receiver, 3 broadband induction coils (6 kg each), 5 porous-pot electrodes, GPS and SD cards ([IIT ISM tender](https://people.iitism.ac.in/~download/tender/Purchase/AGP-PRJ-338-2018-19_1548153672.pdf); [NERC GEF MTU-5C](https://gef.nerc.ac.uk/equipment/mtu5c/)). Approximate prices (all unverified):
  - Phoenix MTU-5C with 3 coils: $60k to $90k.
  - Metronix ADU-08e with MFS coils: $80k to $120k.
  - LEMI-417 long-period with fluxgate: $20k to $35k.
  - A single broadband induction coil: $8k to $15k.
- **Low-cost telluric loggers exist.** The LPTR uses a 24-bit ADC, 2 E channels, GPS timing to about 1 ms and Cu-CuSO4 electrodes. It ran 2 to 4 months autonomous in Egyptian desert. Its impedances matched an ADU07-e from 5 s periods and reached periods of 42,000 s ([EGU21-16275](https://meetingorganizer.copernicus.org/EGU21/EGU21-16275.html)). Münster's EDE is a "low-cost, low-power" 2-component E logger for dense E arrays beside sparse 5-component stations, with 10 units fielded in parallel ([Uni Münster EDE](https://www.uni-muenster.de/Physik.GP/applied_geophysics/projects/ede.html)).
- **Seismic nodes.** SmartSolo IGU-16HR 3C (5 Hz) gets about 30 days at 250 Hz with GPS on, or about 60 days recording nights only, and logs about 3 GB per month ([AuScope/AusPass SmartSolo](https://auspass.edu.au/xwiki/bin/view/Instrumentation/SmartSolo%20Nodes)). Price is about $1.5k to $2.5k per node, and Fairfield ZLand nodes are similar or more, mostly leased (unverified).
- **Large-N geothermal seismic.**
  - Hengill: 498 nodes, about 20 km aperture, under 500 m spacing, about 2 months. Ambient noise imaged low-velocity zones in the top 500 m and a 3 to 5 km intrusion body ([Wu et al. 2024, JGR](https://escholarship.org/content/qt5mj7r09n/qt5mj7r09n.pdf)).
  - Cornwall: 450 nodes resolved fracture orientation and stress, and the results agreed with well logs ([Hudson et al. 2024, Seismic Record](https://ora.ox.ac.uk/objects/uuid:9a5713b8-cfed-4ad9-baed-9ff3af6ba6bf)).
  - Short-observation dense 3C ambient noise imaging works in days ([ESS Open Archive](https://essopenarchive.org/users/527791/articles/598744-high-resolution-ambient-noise-imaging-of-geothermal-reservoir-using-3c-dense-seismic-nodal-array-and-ultra-short-observation)).
- **Zanskar.** It advertised for a seismologist to process "large-N seismic arrays" across geothermal fields ([IRIS job post 2022](https://ds.iris.edu/message-center/thread/8021/)). In December 2025 it announced "Big Blind", a blind system in western Nevada found with AI plus its own field data ([ThinkGeoEnergy](https://www.thinkgeoenergy.com/zanskar-announces-discovery-of-big-blind-geothermal-site-in-western-nevada-usa/)). Its exact sensor mix was not confirmed.

## Hardware design sketch
**Architecture: dense telluric carpet plus sparse MT reference.**
- **E-node (about 90% of stations).** Two orthogonal 50 to 100 m dipoles and 4 Pb-PbCl2 electrodes, which are buried and so need no coils. Electronics are a 24 to 32-bit delta-sigma ADC (ADS1282 or ADS131M class), a low-power MCU and a u-blox GNSS with PPS for timing better than 1 µs. Storage is a 128 GB SD card. Power is a LiFePO4 pack plus a 10 W panel, with sampling cycled between 4 Hz continuous and 1 to 2 kHz bursts. Target: 3 to 6 months autonomous.
  - BOM (unverified, distributor list prices): electronics $120, GNSS $40, electrodes $120, cable $80, battery and solar $90, enclosure $30. **About $500 prototype, about $250 to $300 at 1,000 units.**
- **H-reference (1 per 5 to 10 km², plus 1 remote).** 2 or 3 in-house induction coils (mu-metal or amorphous core, about 20k turns, chopper preamp) on the same logger. Coil BOM is about $400 to $800 each if we wind our own (unverified). The noise target is 0.1 pT/√Hz at 1 Hz, about one order worse than Metronix, which is fine with long stacking time. **About $2.5k per reference station.**
- **Optional co-located seismic.** Add a $30 to $60 3C 4.5 Hz geophone channel to every E-node so one deployment yields ambient-noise tomography as well.
- **Cost and spacing math.** A 25 km² prospect at 100 m spacing is about 2,500 sites, which is unrealistic for one go. At 250 m spacing it is 400 sites. Hardware for 400 E-nodes plus 4 H-refs is about $130k, reusable over 10+ prospects. Field crew: 2 people place about 25 to 40 E-nodes a day (unverified), so 400 sites take about 2 weeks, roughly $30k to $50k with vehicles. **Cost is about $150 to $250 per site versus $1,500 to $4,000 contracted, or about $3k to $8k per km² at 250 m spacing.**
- **Time to prototype.** 3 to 4 months for a 10-unit E-node batch and 2 coils. 6 to 9 months to a field-proven 200-unit fleet.

## What data it unlocks and why incumbents do not have it
- Incumbents (Quantec, Zonge, Phoenix-as-contractor, Enthalpion, Metronix users) sell crew-days. Their revenue scales with stations times rate, and their kit costs $60k+ per station. That kit cannot be left out for months or by the thousand, and clients pay by the station, so nobody buys a dense carpet. Phoenix and Metronix sell to universities and governments at low volume, so a $300 node would cannibalize them.
- Dense, long-duration E data gives four things. First, a 3D clay-cap and conductor model at 100 to 250 m resolution rather than 0.5 to 1 km. Second, good data in the 0.1 to 10 Hz "dead band" from weeks of stacking. Third, time-lapse resistivity. Fourth, a joint inversion with co-located ambient-noise velocity.
- None of this is in public archives. Public MT in the western US is sparse: USArray stations are about 70 km apart, and DOE project grids are small.
- Every survey, especially once matched to our own gradient-hole temperatures, becomes labeled training data (resistivity to temperature at depth). Only we would hold those labels.

## How it compounds into owned assets
- **Rights bought.** Private and ranch geothermal leases and options at $1 to $10/ac, state first-file at about $1/ac/yr, and leftover BLM noncompetitive leases. The carpet costs less than the option fee on many tracts, so survey first and buy only the parcels over upflow.
- **Step-up.** A tract with a 3D clay cap plus 2 to 3 hot gradient holes is a drill-ready prospect. Buyers (Ormat, Fervo, Invenergy, Cyrq, Zanskar itself) usually pay for exactly this de-risking, by commissioning MT and then TG holes. We would sell it as a carry or override.
- **Ladder.** Fleet hardware is reused, and each new prospect improves the model that converts resistivity into temperature. Later we could license the node or use it for lithium brine, hydrogen and critical-mineral EM, but keep owning rights first.

## Risks and kill conditions
- **Physics.** E-only stations depend on a laterally smooth H field. Strong 3D near-surface distortion (static shift) or cultural noise (powerlines, pipelines, cathodic protection) may degrade the impedances. Kill: the telluric-derived tensor at more than 20% of sites deviates more than 10% (or 5 degrees in phase) from a co-located commercial MT station.
- **Ambiguity.** Clay caps also occur over fossil (cooled) systems. MT alone does not prove heat, so we still need TG holes. Kill: in a blind test on 3 known fields, dense-MT targeting does not beat the public-map F1 baseline.
- **Copyability.** Competitors can build the same node in about a year. The moat is the labeled data and the rights, not the electronics.
- **Permits.** BLM casual-use limits apply, and E-nodes are minimal-disturbance. Ranchers must allow months of deployment.
- **Inversion compute.** 3D inversion of 400 to 2,500 sites is heavy. ModEM, SimPEG and MARE2DEM can handle it on cloud GPUs and CPUs, at roughly $1k to $10k per inversion (unverified).

## Cheapest first test
- **Cost:** about $15k.
- **Time:** about 60 days.
- **Setup:** build 10 E-nodes and borrow or rent 1 commercial MT station (university or GEF loan, or a Zonge day rate). Deploy on a known Nevada field with public MT, such as Brady, Dixie Valley or the San Emidio fringe, for 3 weeks.
- **Pass:** the E-node apparent resistivity and phase, computed with the commercial H as reference, are within 10% and 3 to 5 degrees of the commercial station from 0.01 to 100 s. Nodes also run more than 21 days unattended.
- **Fail:** worse than 20% or 10 degrees agreement, or under 7 days of autonomy.

## Sources
- https://en.openei.org/wiki/Magnetotellurics
- https://apps.nrs.gov.bc.ca/pub/aris/Report/39168.pdf/
- https://gdr.openei.org/files/1514/ (NV22 MT Enthalpion for NREL)
- https://people.iitism.ac.in/~download/tender/Purchase/AGP-PRJ-338-2018-19_1548153672.pdf
- https://gef.nerc.ac.uk/equipment/mtu5c/
- https://meetingorganizer.copernicus.org/EGU21/EGU21-16275.html
- https://www.uni-muenster.de/Physik.GP/applied_geophysics/projects/ede.html
- https://auspass.edu.au/xwiki/bin/view/Instrumentation/SmartSolo%20Nodes
- https://escholarship.org/content/qt5mj7r09n/qt5mj7r09n.pdf
- https://ora.ox.ac.uk/objects/uuid:9a5713b8-cfed-4ad9-baed-9ff3af6ba6bf
- https://essopenarchive.org/users/527791/articles/598744-high-resolution-ambient-noise-imaging-of-geothermal-reservoir-using-3c-dense-seismic-nodal-array-and-ultra-short-observation
- https://ds.iris.edu/message-center/thread/8021/
- https://www.thinkgeoenergy.com/zanskar-announces-discovery-of-big-blind-geothermal-site-in-western-nevada-usa/
- https://www1.eere.energy.gov/geothermal/pdfs/wannamaker_peer2013.pdf
