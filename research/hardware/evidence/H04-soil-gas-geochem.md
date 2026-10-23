# H04. Soil-gas and fluid geochemistry sensing over blind geothermal systems

Research note: the shared web search and fetch budgets ran out partway through this slice (about 15 searches and fetches done). Numbers I could not confirm against a source are marked (unverified).

## Summary

- Helium isotopes are the strongest geochemical signal for hidden deep permeability in the Great Basin. LBNL (Kennedy and van Soest) found that "anomalously high ratios map zones of higher than average permeability" and that the method can gauge deep permeability "without drilling" ([LBNL](https://www2.lbl.gov/Science-Articles/Archive/ESD-geothermal-energy.html)). The catch is that 3He/4He still needs a lab noble-gas mass spectrometer. No field instrument resolves 3He.
- Soil CO2 flux works over known systems but is weak over blind ones. At Dixie Valley the background was about 7 g/m2/day and the peak 570 g/m2/day, but only next to fumaroles ([USGS, Bergfeld et al. 2001](https://pubs.usgs.gov/publication/70023687)). Over the blind Kumiva target, the CO2 anomalies were "weak" and only "suggestive" ([DOE/U of Utah](https://www.energy.gov/sites/prod/files/2015/06/f23/9-Magnetotellurics_Soil%20Gas%20Geochemistry_U%20of%20U.pdf)). Biological CO2 noise is the main obstacle ([LBNL, Lewicki and Oldenburg](https://www.osti.gov/biblio/840238)).
- A portable mass spectrometer exists. The miniRUEDI weighs 13 kg, draws 50 W, gives total He, Ar, Kr, N2, O2, CO2 and CH4 in under a minute at 1 to 3% precision, and has run autonomously for weeks ([Eawag](https://www.eawag.ch/en/info/portal/news/news-detail/portable-mass-spectrometer-allows-on-site-gas-analysis/); [Brennwald et al. 2024](https://gi.copernicus.org/articles/13/1/2024/gi-13-1-2024.pdf)). The price is not public; it sells through the Gasometrix spin-off, one custom build at a time ([startup.ch](https://www.startup.ch/gasometrix)).
- Public soil-gas data over Great Basin geothermal targets is thin. It amounts to a few DOE GDR sets (Utah FORGE soil He R/Ra and CO2, Hot Pot mercury) and 1970s to 1980s USGS helium and mercury surveys ([GDR search](https://gdr.openei.org/search?q=Soil%20Gas); [Hinkle, Roosevelt HS](https://digitalcommons.usu.edu/govdocs/47/)). A systematic regional survey would be new.
- Best play: a truck-borne probe-and-bottle system. It runs a field total-He, CO2 and H2 screen every 200 to 500 m along ranch roads. Anomalies go to the lab for 3He/4He. Private ranch and stock wells, which the Water Quality Portal largely lacks, get sampled on the same visit where we offer to lease the heat right.

## Key facts

- Helium: mantle helium has R/Ra around 8, crustal helium around 0.02 (standard values, unverified here). Great Basin fluids run from low ratios in the east to high in the west. The highest Dixie Valley ratios sit on the Stillwater range-front fault ([LBNL](https://www2.lbl.gov/Science-Articles/Archive/ESD-geothermal-energy.html)). McGinness Hills, a blind system with no surface manifestation that Ormat now runs at about 190 MW, has production fluid R/Ra of 0.35 to 0.57, or about 5 to 10% mantle helium ([DOE/U of Utah](https://www.energy.gov/sites/prod/files/2015/06/f23/9-Magnetotellurics_Soil%20Gas%20Geochemistry_U%20of%20U.pdf)). The plant size is unverified.
- CO2: Dixie Valley's anomalous flux tracked shallow temperature anomalies. Output was 7.5 t/day from 0.14 km2 near the Stillwater fault ([USGS](https://pubs.usgs.gov/publication/70023687)). LBNL modeling shows geothermal CO2 can build up to high concentrations at shallow depth even from a low flux, but wind quickly disperses it at the surface ([OSTI 840238](https://www.osti.gov/biblio/840238)). So measure soil gas at depth rather than sniffing air.
- 14C helps separate deep CO2 from plant CO2. At Kumiva, two samples had depleted 14C, which points to an older, deeper source ([DOE/U of Utah](https://www.energy.gov/sites/prod/files/2015/06/f23/9-Magnetotellurics_Soil%20Gas%20Geochemistry_U%20of%20U.pdf)).
- Mobile helium: USGS ran a vehicle-mounted mobile helium detector and a portable helium sniffer for uranium exploration in the 1970s and 1980s ([USGS mobile He](https://pubs.usgs.gov/publication/70012488); [portable sniffer](https://pubs.usgs.gov/publication/70042909)). The concept has been proven once, then dropped.
- Lab helium isotopes: commercial and academic price lists exist at GNS NZ, WHOI, Utah and USGS ([GNS 2026-27](https://www.gns.cri.nz/assets/Laboratory-files/Noble-gas/NGTL-Price-List-2026-27-B.pdf); [Utah](https://facilities.cmes.utah.edu/noble-gas-lab/lab_documents/price_oncampus.pdf)). The typical cost is about $300 to $700 per sample (unverified, as the PDFs were not read).
- Instrument costs (all unverified): LI-COR LI-7810 CO2/CH4 analyzer about $40k to $50k; West Systems accumulation-chamber fluxmeter about $20k to $35k; a miniRUEDI-class mass spectrometer about $60k to $100k; NDIR CO2 sensor $50 to $250; electrochemical H2 and H2S cells $50 to $300 each; Lumex-type mercury vapor analyzer about $25k to $40k.
- H2 and radon: soil-gas H2 surveys across faults are now routine in natural-hydrogen exploration, and junior companies report "anomalous" values from cheap probes ([DGGV Bavaria](https://www.dggv.de/e-publikationen/natural-hydrogen-emanations-in-northern-bavaria-soil-gas-surveys-across-three-fault-systems/)). Radon and thoron mark open faults, but they track shallow fracturing, not heat (unverified).

## Hardware design sketch

**Unit A: probe truck (the "sniffer").** This is a 4x4 pickup with a hydraulic or hammer drive that pushes a 1 m hollow probe. A pump pulls soil gas past:
- NDIR CO2 at about $200 (unverified)
- electrochemical H2 and H2S at about $500 (unverified)
- a radon/thoron alpha cell such as a RAD7-class unit at about $8k (unverified)
- a quadrupole total-He channel, either a miniRUEDI or a home-built RGA with a getter at about $15k to $25k (unverified)

Each stop fills a copper-tube or Isotainer bottle for later 3He/4He work. GPS, a soil-temperature thermistor at 1 m, and logging come to about $1k. The truck reaches about 100 stops a day at 3 to 5 minutes each (unverified). Prototype BOM is about $60k to $120k plus the truck. Unit cost at scale is about $40k if we build our own RGA channel (unverified).

**Coverage.** A 2 km grid with tighter lines across range-front faults needs about 0.3 stops per km2, so one truck covers about 300 km2 a day. Ten trucks over a 120-day field season could screen about 100,000 km2 (unverified, but it follows from the stop rate). At about $1,500 per truck-day all-in, the field screen costs about $5 per km2. Lab isotopes on the top 5% of stops add roughly $3 to $5 per km2.

**Unit B: static node (optional).** A buried solar node with an NDIR CO2 sensor at 1 m depth, H2 and temperature sensors, and an LTE-M or satellite modem, at about $300 to $600 BOM (unverified). Weeks of logging strip out the diurnal and biological CO2 swings that ruin one-shot surveys. Deploy 20 to 50 nodes per target, not regionally.

**Unit C: spring and well sampler.** This is a van kit, not a robot. It holds a miniRUEDI on a membrane contactor for dissolved He, Ne, Ar and CO2, a downhole temperature logger for open stock wells, and bottles for major ions, Li, B, SiO2 (for geothermometers), δ18O/δD and lab 3He/4He. Autonomous "robots" add little, because access to the wells is the bottleneck, not labor.

Time to prototype: 3 to 4 months if we buy a miniRUEDI, or 6 to 9 months if we build our own He channel (unverified).

## What data it unlocks that is not public

- **Regional total-He and R/Ra in soil gas and groundwater.** Today this exists only as points at known fields plus the LBNL regional springs set. Nobody has a dense regional grid.
- **Private stock and domestic wells.** The Water Quality Portal holds USGS NWIS and state samples: mostly major ions, some temperatures, many decades old, and almost no dissolved noble gases or 3He/4He (unverified, as the WQP check was not completed). Ranch wells are mostly unsampled. Every well we log gives three readings: temperature, a geothermometer and helium.
- **Time-series soil gas** that separates the deep signal from biological noise.
- **Why incumbents lack it:** Zanskar and Enverus are software-first and use public data. Ormat explores near its own fields. Academic groups sample tens of sites per grant, not thousands. Labs measure what is sent to them.

## How it compounds into owned assets

The sampling visit is also the land deal. To sample a ranch well we need the landowner's permission. At the same visit we offer about $1 to $10 per acre for an option on the heat right. Helium and temperature anomalies then decide which options we exercise, and they steer state first-file and BLM noncompetitive filings next door. The proprietary layer of He, R/Ra and well temperatures feeds the favorability model, and only we can retrain on it. Buyers (Ormat, Fervo, Invenergy) pay for drill-ready targets. A mantle-helium anomaly plus a hot well plus a fault turns a lease into a "prospect" and raises it from about $5/ac to perhaps $100 to $500/ac or an override (unverified). The step-up is still weak until a temperature-gradient hole confirms it.

## Risks and kill conditions

- Soil gas over blind Great Basin systems may be too weak. The Kumiva CO2 was only suggestive, and the helium upflow may stay inside the reservoir under clay caps. Kill if a blind-field test line (McGinness Hills, Blue Mountain or Tungsten Mountain) shows no total-He or R/Ra contrast above the 2-sigma background.
- R/Ra marks deep permeability, not temperature. A high value with a cold reservoir is still a dry hole.
- Field total-He at ppm-level excess may sit in the noise of the 5.24 ppm air background unless the probe is deep and purged.
- Landowners may refuse access to their wells.
- The data is copyable in kind: anyone with $150k and a truck can do it. The moat is the head start on rights, not the instrument.

## Cheapest first test

Rent or borrow a miniRUEDI and a soil-gas probe (from a university or Gasometrix). Run two 10 km transects across the McGinness Hills range-front fault and one across a matched barren valley, with a stop every 250 m. Bottle 30 samples for lab 3He/4He, and sample 10 nearby stock wells.
- Cost: about $25k to $40k, including about $15k for lab isotopes.
- Time: about 10 field days plus about 6 weeks of lab work.
- Pass: the excess He or R/Ra over the known upflow is at least 3 times the barren-line spread, and it lands within 1 km of the producing faults without being told where they are.

## Sources

- https://www2.lbl.gov/Science-Articles/Archive/ESD-geothermal-energy.html
- https://openei.org/wiki/Isotopic_Analysis-_Fluid_At_Dixie_Valley_Geothermal_Area_(Kennedy_%26_Soest,_2005)
- https://pubs.usgs.gov/publication/70023687
- https://www.osti.gov/biblio/840238
- https://www.energy.gov/sites/prod/files/2015/06/f23/9-Magnetotellurics_Soil%20Gas%20Geochemistry_U%20of%20U.pdf
- https://www.eawag.ch/en/info/portal/news/news-detail/portable-mass-spectrometer-allows-on-site-gas-analysis/
- https://gi.copernicus.org/articles/13/1/2024/gi-13-1-2024.pdf
- https://www.startup.ch/gasometrix
- https://gdr.openei.org/search?q=Soil%20Gas
- https://gdr.openei.org/submissions/1024
- https://digitalcommons.usu.edu/govdocs/47/
- https://pubs.usgs.gov/publication/70012488
- https://pubs.usgs.gov/publication/70042909
- https://www.gns.cri.nz/assets/Laboratory-files/Noble-gas/NGTL-Price-List-2026-27-B.pdf
- https://facilities.cmes.utah.edu/noble-gas-lab/lab_documents/price_oncampus.pdf
- https://www.dggv.de/e-publikationen/natural-hydrogen-emanations-in-northern-bavaria-soil-gas-surveys-across-three-fault-systems/
- https://licor.com/env/products/trace-gas/LI-7810
