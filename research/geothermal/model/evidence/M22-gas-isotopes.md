# M22. Gas and isotope tracers of blind upflow: helium isotopes, soil CO2 flux, mercury, radon, hydrogen

**Builds on:** H04 (soil-gas truck, miniRUEDI, Kumiva and Dixie Valley CO2), H09 (H2/He seeps), M07 (Kennedy and van Soest values, Snake River Plain He, Banerjee 2011, helium as a high-weight channel), L15. This file does not repeat those. It adds: the 2024 USGS western-US gas chemistry release, the full list of GDR helium and soil-gas sets, the Long Valley and Los Humeros soil-gas numbers, the Hawaii blind-resource noble-gas test, how each gas behaves over a *buried* system, the main false-positive traps (tritium, air, biology), costs per sample, and how to put these gases into the model.

**Research note:** the shared web-fetch budget ran out partway (about 7 searches and 6 fetches done; the GNS price list and the UGS FORGE soil-gas paper could not be read). Numbers I could not check against a source are marked (unverified).

## Bottom line

Helium isotopes (3He/4He, written R/Ra) are the only gas tracer that reliably sees *through* a cold cap to deep permeability, and they do it in ordinary water wells, not just at hot springs. They are the gas layer worth building the model around. The public data are scattered but bigger than we assumed: a 2024 USGS release has 313 gas and 1,867 water samples from western wells and springs with 3He/4He, about a dozen DOE GDR sets add more, and California's groundwater-dating programs probably hold thousands of well He-isotope analyses (unverified count). Soil CO2 flux, mercury, radon and hydrogen are cheap and fast, but over truly blind Great Basin systems they give weak or ambiguous signals. Their job is to map which *fault segment* is open, at 10 to 200 m scale, after helium and temperature have picked the area. The best sensor play is not a better soil sniffer. It is (1) cheap passive noble-gas diffusion samplers dropped into hundreds of ranch and stock wells on the same visit as the heat-option signing, mailed to a lab, plus (2) a truck-portable He/Ne quadrupole that screens excess 4He in real time so only good wells get the $300 to $700 isotope run. A long shot worth funding: a field instrument that reads 3He/4He directly.

## Findings

### 1. Helium isotopes: the one gas that sees blind permeability

1. **Physics.** Air has R/Ra = 1 by definition and 5.24 ppm He. Crustal helium (from U and Th decay) is about 0.01 to 0.05 Ra. Mantle helium is about 8 Ra (MORB), up to 15 to 30 in plumes (standard values, unverified here). Any well water above about 0.1 to 0.2 Ra in the eastern Great Basin, or above about 1 Ra anywhere, carries a deep-fluid component that has to have come up a permeable path. Helium is inert. It does not react with clay caps or get eaten by microbes, which is why it survives where CO2 and H2 do not.
2. **It maps open faults, not heat.** Banerjee et al. (2011) model the signal as deep meteoric water circulating along faults with permeability of 10^-12 to 10^-15 m2, with a tiny mantle flux (M07). So high R/Ra is a *permeability* label. It must be paired with a temperature signal (well temperature, geothermometer, heat flow) to mean "hot and open". https://www.usgs.gov/publications/deep-permeable-fault-controlled-helium-transport-and-limited-mantle-flux-two
3. **Blind systems carry measurable mantle helium.** McGinness Hills, a blind system, has production fluids at 0.35 to 0.57 Ra, and Dixie Valley is at 0.70 to 0.76 Ra (H04, M07). Kennedy and van Soest (2005) call helium possibly "the best, and perhaps only" deep-permeability indicator under cool shallow reservoirs. https://escholarship.org/content/qt67p1z91d/qt67p1z91d.pdf
4. **It works in ordinary wells away from the system.** In Hawaii (DOE EE0006729), 66 well targets were picked and 23 sampled. R/Ra ran from 15 to 16 on Kilauea's lower east rift to 0.37 on Lanai. Anomalies appeared on every island and tracked rift zones and calderas. The authors note that R/Ra is "minimally affected by dilution and transport", so a well not directly over a system can still flag it. https://gdr.openei.org/submissions/1410 ; raw data https://gdr.openei.org/submissions/1373
5. **Snake River Plain did the same with regional wells.** About 20 new analyses, 7 above 1.5 Rc/Ra, clustered in 3 zones (M07). https://www.energy.gov/sites/default/files/2015/06/f23/Track2_Hydrothermal_4.2_Dobson_He_isotopes.pdf
6. **Soil-gas helium works only roughly.** At Long Valley (Hinkle and Kilburn 1980, USGS OFR 80-612), 269 regional samples at about one per 2 km2 and 282 traverse samples at 200 m spacing gave soil He of 830 to 20,000 ppb above air, with reproducibility of only about plus or minus 30%. Helium was high on the Hilton Creek fault outside the caldera. It was *low* over surface alteration, where mercury was high (a seal effect). It did not correlate with geophysics. The authors said helium in water reflected very local conditions and needed many more samples. https://pubs.usgs.gov/of/1980/0612/report.pdf . So total soil He is a noisy fault-finder. Dissolved He in wells, corrected with neon, is the better carrier.

### 2. Soil CO2 flux: strong over leaky systems, weak over blind ones

7. **A large modern survey shows the scale.** At Los Humeros, Mexico (Jentsch et al. 2020), 2,823 CO2 flux points on a 25 x 200 m grid over 6 x 4 km, plus about 800 infill points, found a background threshold of 20.7 g/m2/day, with about 90% of points in background and a maximum of 1,464 g/m2/day. Total output was about 87 t/day over 13.7 km2, of which about 26 t/day was above background. Six vent samples gave 2.31 to 4.88 Ra (up to about 65% mantle He). The high-flux corridors were read as hidden NNW faults, but this was not checked by drilling. https://arxiv.org/pdf/2002.11515
8. **The lesson for blind targets.** Los Humeros is a leaky volcanic field. Even there, 90% of points are background, and the anomalies sit in a few narrow corridors. Over a capped Great Basin system the signal is far weaker (Kumiva "weak" and "suggestive"; Dixie Valley anomalies only near fumaroles, H04). CO2 needs δ13C-CO2 (hydrothermal near -3 to -6 per mil versus plant CO2 near -20 to -27 per mil) and ideally 14C to tell deep from biological gas. Los Humeros δ13C spanned -23.2 to -1.2 per mil.

### 3. Mercury: an old, cheap, ambiguous tracer

9. **Hg is a cap-and-outflow tracer.** Mercury is volatile above about 200 C and condenses in the cool clay cap and soils above upflow. 1970s to 1980s USGS and industry surveys used soil Hg at Long Valley (Matlick and Buseck 1975), Roosevelt Hot Springs (Hinkle) and elsewhere, and OpenEI lists it as a standard method. https://openei.org/wiki/Geothermal_Exploration_Using_Surface_Mercury_Geochemistry ; https://digitalcommons.usu.edu/govdocs/47/
10. **Hg and He can be anti-correlated.** At Long Valley high Hg and low He went together over altered ground (finding 6). That makes the pair useful: high Hg plus low He suggests a sealed cap; high He plus modest Hg suggests an open fault. Hg also has mining-district noise (old Hg and Au mines, mill tailings) across Nevada, which can swamp a geothermal signal (unverified, but well known).

### 4. Radon and thoron: open-fracture finders, not heat finders

11. **Half-life sets the reach.** Rn-222 lives 3.8 days. Without a carrier gas it moves only metres. A high Rn-222 with a low Rn-220 (thoron, 55 s half-life) ratio means gas is being *pushed* up from depth along an open fracture by CO2 or steam. A high thoron reading means only local shallow soil. That ratio is the useful number, and it is commonly used to map active faults in geothermal fields (e.g., Rajabasa, Indonesia) (unverified details). Radon says "open crack with gas flow", which is a good fault-segment selector, but it is strongly driven by soil uranium, moisture and barometric pumping.

### 5. Hydrogen: fast fault-segment mapper, noisy and reactive

12. **H2 in soil gas marks active, deep-rooted faults,** and natural-hydrogen exploration has made cheap electrochemical H2 probes common (H04, H09). Geothermal fluids carry H2 (it is part of the Giggenbach H2-Ar geothermometer). But H2 is eaten by soil microbes and made by drilling-steel corrosion and by serpentinization unrelated to heat. Treat H2 as a secondary segment selector, never as a primary label (inference).

### 6. Traps that make gas data lie

13. **Tritiogenic 3He.** Young groundwater carries tritium from 1950s to 1960s bomb tests, which decays to 3He. That raises R/Ra in shallow, young wells and can mimic a mantle signal. Every helium isotope sample needs a tritium analysis or a neon-based check, or a known old water age (standard practice in 3H/3He dating, unverified here as a source).
14. **Air and excess air.** Bubbles and pumping add air helium. Neon (pure air tracer) is used to subtract it. A total-He-only field reading is ambiguous without Ne. This argues for an He plus Ne field instrument.
15. **Crustal 4He in old water.** Very old basin water accumulates crustal 4He and pushes R/Ra down. A well can be over a real upflow and still read low if it pulls mostly old cold water. The model must use He concentration, R/Ra and Ne together, not R/Ra alone.

### 7. Costs per sample (mostly unverified)

| Measurement | Cost per sample | Field rate | Notes |
|---|---|---|---|
| 3He/4He + He, Ne (lab, copper tube or diffusion sampler) | $300 to $700 (GNS, Utah, WHOI, LBNL lists; not read) | 5 to 15 wells/day/crew | The core value point. Copper tubes about $30 to $60 each. |
| Tritium (for 3He correction) | $150 to $400 (unverified) | same visit | Needed on young or shallow wells. |
| Field total He + Ne (miniRUEDI-class) | under $1 marginal after a $60k to $100k instrument (unverified) | about 1 minute per reading | Screens wells before lab spend. |
| Soil CO2 flux (accumulation chamber) | under $5 marginal; $20k to $35k instrument | 100 to 200 points/day/person (unverified) | Los Humeros did 2,823 points in one campaign. |
| δ13C-CO2 (lab or field CRDS) | $30 to $60 (unverified) | | Needed to reject plant CO2. |
| 14C of soil CO2 | $400 to $600 (unverified) | | Only on top anomalies. |
| Soil Hg (lab cold-vapour AA) or field Lumex | $15 to $40 lab; $25k to $40k field unit (unverified) | 50 to 150/day | Cheap, ambiguous, mining noise. |
| Radon/thoron (RAD7-class) | under $5 marginal; about $8k instrument (unverified) | 20 to 40/day | Ratio maps open cracks. |
| Soil H2 (electrochemical) | under $1 marginal; $50 to $300 sensor | 100+/day | Reactive, noisy. |

## Datasets

| Dataset | Access | Coverage | Value for blind detection |
|---|---|---|---|
| USGS, Gregoire, Peek and Hurwitz (2024), "Water and gas chemistry data from wells and hot springs in the Western USA, 1930-2006" | Free, https://doi.org/10.5066/P96Q13U3 (catalog https://data.usgs.gov/datacatalog/data/USGS:64cc2213d34e2d58db2fa9a6) | 1,867 water and 313 gas samples, mainly CA, OR, WA, some MT, ID, NV, UT, AZ, NM; 3He/4He and air-corrected 3He/4He | First clean digital He-isotope table for the West. Mostly known systems, so it is a positive-label and calibration set. |
| Kennedy and van Soest Great Basin He survey (2005 LBNL report; Science 2007) | Paper and report tables, https://escholarship.org/content/qt67p1z91d/qt67p1z91d.pdf | Springs and wells across NV and neighbours, roughly a few hundred points (unverified) | Regional mantle-He gradient plus fault-scale highs. The key regional prior. |
| Utah FORGE soil He R/Ra (GDR 1024), soil CO2 (GDR 1025), cold groundwater and produced fluid geochem (GDR 1629), MM West fault report (GDR 1150), topical report (GDR 1038) | Free, https://gdr.openei.org/submissions/1024 , /1025 , /1629 , /1150 , /1038 | Roosevelt HS / Milford, UT | Only public dense soil-He R/Ra grid over a US field. Use as a test of how far soil He sees from the upflow. |
| Play Fairway CA-NV-OR geochemistry (GDR 671) and 2 km grid (GDR 673); Eastern Great Basin PFA (GDR 1090) | Free, https://gdr.openei.org/submissions/671 , /673 , /1090 | NW Great Basin; eastern NV and W UT | Helium already used as a play-fairway layer; reuse and extend. |
| Western USA high-value materials in geothermal and produced fluids (GDR 1126, 1266) | Free, https://gdr.openei.org/submissions/1126 , /1266 | ID, NV, NM, OR, UT produced fluids | Extra He-isotope points in producing fields and oil-field brines. |
| Snake River Plain FORGE site data (GDR 793) and LBNL/INL SRP He study | Free, https://gdr.openei.org/submissions/793 | Eastern Snake River Plain | Regional well He showing blind-zone clusters. |
| Hawaii PFA noble gas raw data (GDR 1373) and blind-resource study (GDR 1410) | Free, https://gdr.openei.org/submissions/1373 , /1410 | 23 to 66 wells, Hawaii | Best worked example of "noble gases in ordinary wells find blind heat". Method template. |
| USGS soil helium and mercury surveys, 1970s to 1980s (e.g., OFR 80-612 Long Valley, OFR 80-613, OFR 78-246, Roosevelt HS) | Scanned PDFs, https://pubs.usgs.gov/of/1980/0612/report.pdf , https://pubs.usgs.gov/of/1980/0613/report.pdf , https://pubs.usgs.gov/of/1978/0246/report.pdf | Selected known fields | Digitise as weak labels and noise models. |
| California GAMA / LLNL groundwater noble-gas and tritium-helium ages | Public via GAMA GeoTracker (unverified link and count) | Likely thousands of CA wells (unverified) | Largest untapped well He-isotope set in the West; R/Ra highs outside known fields are free blind-upflow candidates. Check first. |
| USGS / BLM natural-gas helium analyses | Public (USGS DS / BLM helium program; unverified link) | Tens of thousands of gas wells, mostly He %, few isotopes | Total 4He in sedimentary basins; weak for heat but a crustal-He baseline. |
| USGS Data Series 169 (noble gas / isotope related) | https://pubs.usgs.gov/ds/2005/169/ (contents not read) | unverified | Check for extra He data. |

## What dominates uncertainty

1. **Sparsity, not quality.** Each He-isotope point is very informative, but there are only hundreds in the Great Basin outside known fields. Between points the helium layer is almost pure prior. Doubling coverage matters more than anything else.
2. **Mixing and dilution.** A well's R/Ra depends on what fraction of deep fluid it pulls, how old its cold water is (crustal 4He), and how young it is (tritiogenic 3He). Without Ne, tritium and an age proxy, a low reading cannot tell "no upflow" from "upflow diluted".
3. **Groundwater flow path.** The signal is displaced down-gradient from the fault. Without a flow model, a helium high is placed kilometres from its source.
4. **Permeability is not temperature.** High R/Ra on a cold fault (or an amagmatic deep circulation that never got hot) gives false positives. Helium must be fused with thermal data.
5. **For soil gases, biology and weather.** CO2, H2 and radon vary with season, moisture, barometric pressure and soil type by factors comparable to the geothermal anomaly. One-shot surveys over blind systems are close to noise.
6. **Selection bias in labels.** Almost all public He data were collected at hot springs and known fields. A model trained on them learns "near a spring" unless negatives from ordinary wells are added.

## What a sensor could fill

1. **Passive noble-gas diffusion samplers for ranch wells (top pick).** A small copper or silicone-membrane diffusion cell hung in a stock or domestic well equilibrates with dissolved gas in about a day, then is crimped and mailed to a lab (method used in hydrogeology; unverified detail). BOM perhaps $20 to $60 each. It fits the existing ranch-probe visit: drop the T/P/conductivity probe, leave a sampler, sign the heat option, pick it up next pass. This turns each landowner visit into a He, Ne, R/Ra point. 1,000 wells at about $500 all-in is $0.5M for a layer no competitor has.
2. **Truck-portable He plus Ne quadrupole (miniRUEDI-class) with a membrane contactor.** Real-time excess-4He and air-corrected He in well water and soil gas. It decides which samples earn a lab isotope run, cutting cost per *useful* R/Ra point by 3 to 10 times (assumed).
3. **Moonshot: field 3He/4He.** No field instrument resolves 3He today. A compact magnetic-sector or laser-spectroscopy (metastable-He) 3He/4He analyzer good to about 0.05 Ra would make helium as cheap as temperature and is the single biggest data unlock in this slice (assume it can work; development cost and timeline unverified).
4. **Buried multi-gas nodes on candidate faults.** CO2 (NDIR) plus δ13C proxy, Rn/Tn alpha cell, H2, temperature, soil moisture, barometer, logging for weeks. Time series removes biology and barometric pumping, so a fault segment can be called open or closed. Use at 20 to 50 nodes per target, not regionally (as in H04).
5. **Low-cost soil-Hg + Rn/Tn probe on the 2 m temperature-probe rig.** The no-permit 2 m probes are already being pushed. Adding a gas port at the tip gives CO2, Rn/Tn and Hg vapour at the same hole for almost no added field time.

## Implications for a better model

1. **Make helium a physics channel, not a raster.** Model each well's He, Ne, 3He/4He and tritium with a simple mixing forward model: air-saturated water + excess air + crustal 4He (age-dependent) + tritiogenic 3He + deep-fluid fraction f with end-member R/Ra. Infer f and its uncertainty per well. Feed f, not raw R/Ra, to the favorability model.
2. **Back-project along groundwater flow.** Place the inferred deep-fluid source up-gradient using water-table gradients (NWIS heads), so helium highs light up the right fault, not the downstream well.
3. **Use helium as a permeability label and temperature data as a heat label,** and model the probability of "hot AND open" as a product of two linked latent fields. Helium then fixes the main weakness of temperature-only models: picking hot but tight ground.
4. **Spatial model on the fault network.** Interpolate deep-fluid fraction along mapped Quaternary faults (a graph or anisotropic Gaussian process along strike), not in isotropic space. Banerjee's result says the signal lives on faults.
5. **Soil gases as segment-scale likelihoods.** CO2 flux (with δ13C), Rn/Tn ratio, Hg and H2 enter only at target scale, as evidence on which 100 m to 1 km fault segment is open. Keep them out of the regional model, where they are mostly noise.
6. **Fix label bias with negatives.** Add ordinary-well He results with low f as explicit negatives, and down-weight spring-only positives.
7. **Value of information drives sampling.** Use the model's posterior to choose which ranch wells to sample next (highest expected reduction in MWe-weighted uncertainty per $500 sample). Helium is the cheapest per-point update to the "hidden but open" question, so it should get most of the early field budget after temperature.
8. **Check California GAMA first.** If it holds thousands of well He-isotope analyses, it is a free, large, mostly non-geothermal-biased training set and a direct blind-candidate list.

## Sources

- https://doi.org/10.5066/P96Q13U3 and https://data.usgs.gov/datacatalog/data/USGS:64cc2213d34e2d58db2fa9a6 (Gregoire, Peek, Hurwitz 2024)
- https://escholarship.org/content/qt67p1z91d/qt67p1z91d.pdf (Kennedy and van Soest 2005)
- https://www.usgs.gov/publications/deep-permeable-fault-controlled-helium-transport-and-limited-mantle-flux-two (Banerjee et al. 2011)
- https://gdr.openei.org/submissions/1410 and https://gdr.openei.org/submissions/1373 (Hawaii noble gases)
- https://www.energy.gov/sites/default/files/2015/06/f23/Track2_Hydrothermal_4.2_Dobson_He_isotopes.pdf (Snake River Plain He)
- https://pubs.usgs.gov/of/1980/0612/report.pdf (Hinkle and Kilburn 1980, Long Valley soil He)
- https://pubs.usgs.gov/of/1980/0613/report.pdf ; https://pubs.usgs.gov/of/1978/0246/report.pdf (other USGS soil-gas reports, not read)
- https://arxiv.org/pdf/2002.11515 (Jentsch et al., Los Humeros CO2 and He)
- https://gdr.openei.org/search?q=helium (GDR helium listing: 1024, 1025, 1629, 1150, 1038, 671, 673, 1090, 1126, 1266, 793)
- https://openei.org/wiki/Geothermal_Exploration_Using_Surface_Mercury_Geochemistry
- https://digitalcommons.usu.edu/govdocs/47/ (Hinkle, Roosevelt HS soil He and Hg)
- https://pubs.usgs.gov/ds/2005/169/ (not read)
- Blocked, not read: https://www.gns.cri.nz/assets/Laboratory-files/Noble-gas/NGTL-Price-List-2026-27-B.pdf ; https://ugspub.nr.utah.gov/publications/misc_pubs/mp-169/mp-169-i.pdf ; https://www.eti-geochemistry.com/co2-paper/helium/index.html
