# M27: Fibre optics for blind geothermal exploration (DTS strings in existing wells, DAS on dark telecom fibre)

Date: 23 Oct 2026. This file builds on `M12-seismology.md` (F5 covers the Brawley dark-fibre basics, the interrogator rent guess and the Zanskar DAS-intern role), `M16-temperature-at-depth.md` (repeat logging), `M20-tg-and-mining-holes.md` (re-entry logger), `M21-shallow-temperature.md` (the "deep dart"), and `../../../hardware/evidence/H02, H11, H12` (DTS costs, DTS-lined gradient holes, Fervo's fibre). It does not repeat them. It asks: **can fibre (a) read temperature in many existing holes cheaply and (b) turn existing telecom routes into regional seismic lines across target valleys, and how does that enter the model and the kit?**

Web budget: the shared search and fetch budgets ran out after 2 searches and 5 fetches. Everything not tied to a URL below is from memory and marked (unverified).

## Bottom line

Fibre is two different tools, and both are worth having. **DAS on existing buried telecom fibre** is the cheapest way anyone has found to get a 2D shear-velocity (Vs) section to about 3 km depth along tens of km at once, with no permit and no field crew. At Brawley, 28 km of Zayo dark fibre and **two days** of ambient noise imaged a high-Vs, low-Vp/Vs body under a blind field (Cheng et al. 2023, JGR). A 12 km Reno dark-fibre line gave bedrock depth that matched regional studies (BSSA). So DAS reliably gives **basin depth and buried fault offsets**, which are the biggest errors in our conductive temperature-at-depth model. It is still a structure tool, not a heat detector, and every published geothermal result is retrospective (M12). The real moat is **access**: the western US has long buried routes that cross hot valleys at right angles (US-395 "Digital 395" from Barstow to Reno through Coso and Long Valley, I-80, US-50, US-95, the railways, unverified detail), and nobody has a map of which strands are dark, buried and reachable from an amplifier hut. **DTS** (Raman fibre thermometry) is the other tool. It gives a full temperature profile every 0.25-1 m at about 0.01-0.1 °C, and it can be left in a hole for weeks to show equilibrium and flow zones. For us it is best used as a **shared, rotating interrogator feeding cheap sacrificial fibre left in ranch water wells, old TG holes and our own shallow pushes**, not as a service-company job at $50-150k a well. The build: (1) a "fibre-route atlas" plus a carrier DAS-rental program that screens 10-30 valleys a year at about $10-30k each; (2) a portable DTS box that serves 10-20 cheap fibre-lined holes at once. Both feed the model directly: DAS gives a basin-depth and fault-offset layer with real uncertainty; DTS turns single-shot logs into equilibrium gradients with flow-zone flags.

## Findings

### F1. Published geothermal DAS results on telecom or surface fibre
- **Brawley, Imperial Valley CA (Cheng, Ajo-Franklin, Nayak, Rodríguez Tribaldos, Mellors, Dobson et al., JGR Solid Earth 2023, doi 10.1029/2022JB025240, CC-BY).** About 28 km of Zayo fibre from Calipatria to Imperial. Two days of passive DAS from early Nov 2020. S-wave velocity to 3 km depth. A high-Vs, low-Vp/Vs feature under Brawley, read as hydrothermal mineralization and lower porosity (https://escholarship.org/uc/item/1gg2w5qf). Access was simple in principle: reach a point of presence (amplifier hut), plug in an interrogator, no new sensors and no permitting (https://www.thinkgeoenergy.com/research-explores-the-use-of-telecom-fiber-for-geothermal-seismic-sensing/). Data are public on data.gov (M12). Brawley had already been found by oil and gas wells.
- **Downtown Reno NV (BSSA; NSF awards 1832109, 2243961-3).** 12 km of dark fibre. Ambient-noise interferometry on strain-rate DAS, dispersion inversion for near-surface Vs. Average depth to bedrock and lateral velocity changes agree with earlier regional studies. The authors check how the conduit around the fibre affects the inversion (https://par.nsf.gov/biblio/10502387-subsurface-imaging-using-interferometry-distributed-acoustic-sensing-ambient-noise-measurement-along-dark-fiber-line-case-study-downtown-reno-nevada). **Lesson:** conduit fibre in a noisy city still gives usable bedrock depth. Rural fibre has less traffic noise. That means less signal for interferometry too, so more days are needed (unverified).
- **Brady NV, PoroTomo (2016).** 8.6 km of trenched surface DAS plus about 400 m of borehole DAS and DTS in a known field. It gave shallow Vp maps and showed DAS can track pumping-driven strain (Feigl et al., unverified detail; data on GDR, see M12).
- **Reykjanes, Iceland (Jousset et al., Nature Communications 2018, unverified detail).** About 15 km of existing telecom fibre on a geothermal peninsula. DAS mapped known and unknown faults and small earthquakes at metre scale. This is the cleanest case of "telecom fibre finds buried faults in a geothermal area".
- **Long Valley caldera CA (Caltech, Zhan group, about 2020-2023, unverified detail).** About 100 km of fibre along US-395 (reported as the CENIC / Digital 395 network) recorded earthquakes and noise across the caldera that hosts the Casa Diablo plants. Results imaged shallow structure and the top of the magma system. **Lesson:** a state middle-mile network on a geothermal corridor has already been lent to scientists for DAS.
- **Ridgecrest and Sacramento-area DAS (Caltech, LBNL, Stanford, 2019-2021, unverified detail).** Repeat demonstrations that 10-50 km of existing fibre gives earthquake catalogs and near-surface Vs. Not geothermal, but they prove carrier cooperation is routine for research.
- **Development use (H12).** Fervo Project Red and Utah FORGE used DAS and DTS in wells to watch stimulation. That is after the lease. It is not exploration.
- **Zanskar** has a DAS-processing intern role (M12). No public DAS result from Zanskar was found.

### F2. What DAS can and cannot see (physics for the model)
- **Measures:** axial strain rate along the fibre every 1-10 m, gauge length about 5-20 m, frequency roughly 0.01 Hz to kHz (unverified generic spec).
- **Good at:** surface-wave dispersion from traffic, rail and ocean noise, giving 1D Vs at each segment and a 2D section. Depth reach scales with the longest usable wavelength. Brawley reached 3 km with overtones. Also good at local earthquakes for Vp/Vs and fault location, if events happen during the record.
- **Weak at:** broadside waves (single component), and areas away from the line. Fibre hung on poles (aerial) or on power lines (OPGW) is wind-noisy and poorly coupled. Buried conduit is fine (Reno).
- **Heat:** DAS does not see temperature at depth. Very low-frequency DAS does respond to tiny temperature changes in the fibre itself (mK level), which is useful in wells, not along roads (unverified).
- **Blind signatures DAS can add:** basin-fill thickness, buried range-front fault position and throw, step-overs, and odd fast or slow bodies (sealed caps like Brawley, or altered clay zones). These are the structural "where could upflow be" inputs, at the depth that matters (0.3-3 km).

### F3. Access to fibre routes: the real bottleneck and the moat
- **Who owns buried long-haul in the Great Basin (unverified, from memory):** Zayo, Lumen (ex-Level 3 / Qwest), AT&T, Verizon, Crown Castle, regional middle-mile builders, rural telephone and electric co-ops, state DOTs (NDOT and UDOT have fibre along interstates for traffic systems), and fibre in railroad rights-of-way (Union Pacific routes across Nevada carry several carriers' fibre).
- **Corridors over hot ground (unverified):** US-395 (Coso, Long Valley, Mono Basin, Steamboat, Carson Valley), I-80 (Humboldt valley, Brady, Desert Peak, Beowawe, Winnemucca), US-50 (Dixie Valley edge, Fallon, Austin), US-95 (Hawthorne, Tonopah, Walker Lane), I-15 and US-6 in Utah (Cove Fort, Roosevelt, Milford). These roads mostly cross valleys at right angles to range fronts, which is the best geometry for a 2D fault section.
- **New fibre is coming.** NTIA middle-mile grants and BEAD money are funding new rural routes in Nevada and Utah from 2024 on (unverified detail). New builds often lay spare strands. A state-funded strand may be easier to borrow than a commercial one.
- **Route maps are not public.** The FCC broadband map shows service, not routes. Commercial route databases (for example FiberLocator) sell maps (unverified pricing, likely $10-50k/yr). Carriers will share a route under NDA to a research partner. **A curated atlas of "buried, dark-capable, crosses a target valley, reachable hut" segments is itself proprietary data.**
- **Cost of a DAS week (unverified):** interrogator rent $5-15k/week (M12) or buy $100-300k; carrier strand access free for research partners (Zayo-LBNL) or a short-term lease of perhaps $1-5k per segment-week; one tech; data is 1-10 TB per week per 30 km at full rate, much less after downsampling to noise-band. Total per valley line: about **$10-30k**, versus $150k+ for one TG hole and $50-200k for a nodal carpet.
- **Partner route:** UNR Nevada Seismological Laboratory (Reno fibre), LBNL (Imperial Valley), Caltech (Long Valley, Ridgecrest) and Rice have the carrier relationships. A paid research contract with one of them is the fastest way to get strands (unverified).

### F4. DTS in existing wells
- **Specs.** Raman DTS: about 1 m (newer units 0.25-0.5 m) sampling, up to about 20 km range, fibre usable to about 300 °C with suitable coating (https://www.fiercesensors.com/components/distributed-temperature-sensing-dts-geothermal-energy-applications). Temperature resolution about 0.01-0.1 °C with long averaging (unverified). Hydrogen darkening at high temperature drifts the reading unless double-ended or carbon-coated fibre is used (unverified).
- **Deep-well use.** Wireline DTS was run in geothermal wells as early as the 2000s (GFZ, WGC 2005; https://gfzpublic.gfz-potsdam.de/pubman/item/item_232868_1/component/file_232867/Wireline%20Distributed%20Temperature-WGC2005.pdf). A permanent DTS in a Munich production well (installed 2019) was inverted for which reservoir zones give flow (Felix et al., Advances in Geosciences 2023; https://www.cee.ed.tum.de/hydro/news/article/new-paper-published-about-geothermal-reservoir-characterization-with-fiber-optics/). Fervo holds a patent on DTS and DAS methods for geothermal well planning (https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12662904, assignee unverified).
- **Why DTS matters for blind exploration.** A single probe log in a well that was just pumped is disturbed. A fibre left for 1-4 weeks gives the equilibrium profile, shows lateral outflow (a warm aquifer with a temperature reversal below), shows up- or down-flow in the borehole, and shows how fast it is changing. These are exactly the "is this warm water a leak from a hidden upflow" signals (M16, M23).
- **Cheap version.** The expensive part is the interrogator ($20-80k, H11; $50-150k, H02). The fibre itself is cheap: a loose-tube gel-filled cable is about $1-5/m (unverified). So one interrogator on a trailer can multiplex 4-16 channels, or be driven between wells, reading 10-20 cheap fibres left hanging in ranch wells, old TG holes (M20) and our 10-30 m pushes (M21). Each well costs a few hundred dollars of fibre. Fibre has no electronics downhole, so it survives hot water and does not corrode like thermistor strings.
- **Distributed thermal response test.** Heating a copper wire inside a hybrid cable and watching DTS gives thermal conductivity along the hole (used for ground-source heat pumps, unverified detail). That turns gradient into heat flow in-situ, without core.

### F5. What it adds versus our existing kit
- DAS is the only tool that gives **regional lines to 3 km depth with no permit, no land access and no node deployment**. It fills the gap between free catalogs (M12 F3) and the MT/geophone carpet (H03).
- DTS turns the drop-probe visit into a **monitored well**. It upgrades our private ranch-well temperatures from one-shot to research-grade.

## Datasets

| Dataset | Access | Coverage | Value for blind detection |
|---|---|---|---|
| Imperial Valley Dark Fiber continuous DAS (DOE GTO) | data.gov / GDR, open | 28 km, Calipatria-Imperial, months from Nov 2020 | Benchmark to build and test our DAS-to-Vs pipeline. Has the one published blind-field DAS signature. |
| Cheng et al. 2023 Vs model | JGR, CC-BY (escholarship 1gg2w5qf) | 28 km section to 3 km | Label: "sealed cap = high Vs, low Vp/Vs" in a hot basin. |
| Reno dark fibre DAS (UNR, NSF) | Ask UNR; paper in BSSA | 12 km, Truckee Meadows | Test of conduit fibre and bedrock depth near the Steamboat / Moana systems. |
| PoroTomo Brady DAS + DTS | GDR, open | 8.6 km surface + borehole | Field-scale DAS beside wells with known temperature. |
| Long Valley / Ridgecrest DAS (Caltech) | Caltech data, partly via EarthScope (unverified) | Up to about 100 km on US-395 | Shows Digital 395 access and a DAS record over a geothermal caldera. |
| FORGE and Fervo DTS/DAS | GDR (FORGE open); Fervo private | Single wells | Calibrates DTS behaviour at 200+ °C. |
| Commercial fibre route maps (FiberLocator etc.) | Paid (unverified) | US | Input to the route atlas. |
| NTIA middle-mile and state broadband route filings | Public grant documents (unverified detail) | NV, UT, OR, ID | Free hints of new buried routes and spare strands. |

## What dominates uncertainty (this slice)
1. **Fibre access and coupling.** Which strands are dark, buried (not aerial) and reachable, and whether carriers will lend them for a week at a fair price. This sets how many valleys DAS can screen. It is unknown until we ask.
2. **Retrospective-only record.** As in M12, no DAS line has found an undrilled field. The likelihood ratio of a DAS anomaly for "hot and permeable" is unknown (guess 1.5-5).
3. **Sign of the signature.** Brawley's blind field showed as *fast* (sealed), not slow. A model that hard-codes "slow = hot" will be wrong in some settings.
4. **Depth reach in quiet rural noise.** Brawley had farm and road noise. A remote Nevada route may need 1-4 weeks for good long-period data (unverified).
5. **DTS drift and well disturbance.** Hydrogen darkening and calibration drift at high temperature, and pumping by the rancher, can bias gradients unless double-ended and logged with pump records.

## What a sensor could fill
- **Basin depth and buried fault offset along every fibre-crossed valley**, as a 2D line to 1-3 km. This is the main error in the conductive model.
- **Local microseismicity below the network threshold** along the line during the record (DAS sees M<0 events within a few km, unverified).
- **Equilibrium temperature profiles and flow zones** in ranch wells and old TG holes over weeks, not one shot.
- **In-situ thermal conductivity** (heated DTS) so gradients become heat flow.

## Implications for a better model
1. **Add a "basin depth and fault-offset" layer with per-cell uncertainty.** Prior from gravity and free catalogs; update with DAS lines where we have them. Feed it into the conductive temperature-at-depth model. Valleys crossed by a DAS line get a much narrower basin-depth posterior.
2. **Treat DAS velocity anomalies as a signed, setting-dependent likelihood.** Learn "fast cap" versus "slow altered zone" separately by setting (sedimentary basin vs Basin-and-Range fault), using Brawley and Brady as the first labels.
3. **Value-of-information targeting.** Pick valleys for DAS where heat evidence is positive but structure is unknown (high posterior entropy, M12, M17). Only then option land and carpet.
4. **Use DTS records as time series, not points.** Model equilibrium temperature with the drift as a feature. Flag reversals as lateral outflow and use them to point up-gradient toward the hidden upflow.
5. **Make the fibre-route atlas a model input.** It sets where cheap structural data can be had, which changes the expected cost of confirming each cell, and therefore which land to lock first.

## Physical things to build (alpha)
- **"Fibre scout" trailer.** A rented or owned DAS interrogator in a ruggedized trailer with solar and Starlink, edge processing that writes only noise cross-correlations (GB not TB). Plugs into an amplifier hut for 1-2 weeks per valley. Goal: 10-30 valley lines a year at $10-30k each.
- **Fibre-route atlas.** Not a sensor but a data asset: carrier NDAs, NTIA filings, DOT and railroad fibre, scored for burial, darkness, hut access and valley crossing.
- **Shared DTS box plus sacrificial fibre.** One multi-channel Raman DTS on a truck serving 10-20 wells and pushes, each with $200-500 of fibre left in place with the owner's consent and our heat option signed. Optional heated hybrid cable for conductivity.
- **Later:** lay our own cheap fibre in a plough trench along a ranch road across a top target (km for a few $k, on private land we already option). That gives a permanent DAS and DTS line we own.

## Sources
- https://escholarship.org/uc/item/1gg2w5qf (Cheng et al. 2023, Brawley DAS)
- https://www.thinkgeoenergy.com/research-explores-the-use-of-telecom-fiber-for-geothermal-seismic-sensing/
- https://essopenarchive.org/users/527791/articles/596714-using-dark-fiber-and-distributed-acoustic-sensing-to-characterize-a-geothermal-system-in-the-imperial-valley-southern-california
- https://par.nsf.gov/biblio/10502387-subsurface-imaging-using-interferometry-distributed-acoustic-sensing-ambient-noise-measurement-along-dark-fiber-line-case-study-downtown-reno-nevada (Reno 12 km)
- https://www.cee.ed.tum.de/hydro/news/article/new-paper-published-about-geothermal-reservoir-characterization-with-fiber-optics/ (Munich DTS flow zones)
- https://gfzpublic.gfz-potsdam.de/pubman/item/item_232868_1/component/file_232867/Wireline%20Distributed%20Temperature-WGC2005.pdf (wireline DTS)
- https://www.fiercesensors.com/components/distributed-temperature-sensing-dts-geothermal-energy-applications (DTS specs)
- https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12662904 (DTS/DAS geothermal well-planning patent)
- Related repo files: M12 (Imperial Valley data.gov link, Brady GDR 1070, interrogator costs), H02, H11, H12.
