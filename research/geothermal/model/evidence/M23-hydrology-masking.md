# M23: Hydrologic masking. Why systems are blind, how far the heat travels, and where to put sensors

Date: 23 Oct 2026. Slice M23, model track. This builds on `../../evidence/L02-blind-systems.md` (blind shares: ~39% of known Great Basin systems blind, ~75% of all resources blind; Coolbaugh 2006 already used water-table depth in its "degree of exploration" model), `M06` (water-well temperatures, Zanskar's "water wells found >1/3 of blind systems"), `M18` (historic finds were shallow outflow plumes; Big Blind is the deep kind), and `M21` (2 m probe physics: noise ~1.2 C, seasonal ±5 C, needs >0.5-1 W/m2 leak). It does not repeat them. New here: (1) a simple classification of the four hydrologic masks with primary-source numbers (Cascades rain curtain, Snake River Plain cold aquifer, Eureka Low carbonate sweep, lateral outflow); (2) back-of-envelope physics (marked "calc") for how far an outflow plume carries heat, and how small a vertical water flux a temperature log can see; (3) a sensor placement rule for each mask. Method note: 7 web searches and 4 page reads. The shared WebFetch budget then ran out, so some numbers below come from my own knowledge of the literature and are marked (unverified).

## Bottom line

Most blind systems are not "no heat reaches the surface". They are "the heat reaches the surface somewhere else, or gets carried away by moving water". Four masks do this. (1) **Rain curtain**: in the Cascades, cold recharge sweeps the top 0.5 to 1 km, and heat leaves through springs in deep valleys, often 10-20 km from the source. The whole US Cascade arc discharges only about 1,050 MW of advective heat, and only ~240 MW through hot springs (Ingebritsen and Mariner 2010). (2) **Cold aquifer lid**: on the eastern Snake River Plain the Kimama hole is near-isothermal (4.5 C/km) down to ~950 m, then the gradient jumps to 72-75 C/km, with 132 mW/m2 heat flow and 125-140 C geothermometers below (Lachmar et al. 2017). A surface probe or a shallow well sees nothing. (3) **Regional carbonate sweep**: the "Eureka Low" of central-eastern Nevada has low surface heat flow because deep interbasin groundwater carries heat away (Sass et al. 1971; Lachenbruch and Sass 1977). (4) **Lateral outflow**: in the Great Basin and calderas, upflow on a fault feeds a tongue of hot water that runs downhill along a permeable layer. At Long Valley, temperature reversals (hot water over cooler rock) were found in almost every thermal well before 1988 (Sorey et al. 1991). My physics estimate is that such a plume carries a usable signal 3 to 30 km before it fades, depending on flow speed. This tells us where to put sensors. Do not sample on a grid. Sample where the water goes: valley floors, springs and stream confluences downstream (to detect), then walk upgradient along structure (to locate the upflow). Log full temperature-depth profiles in wells, not one bottom reading, because the shape of the profile (reversal, isothermal, convex) says which mask is present. For a better model, each cell needs a "hydrologic transfer" term. It maps a heat source at depth to where and how strongly it shows up at the surface and in shallow wells, using water-table depth, recharge, topography and aquifer type. Without it, the model counts swept and lidded ground as "explored and empty" when it is really "not yet observable". That one fix probably moves the most hidden-resource uncertainty per dollar.

## Findings

### F1. The four masks and how big each is
| Mask | Where | Key number | Source |
|---|---|---|---|
| Rain curtain (high recharge through young volcanics) | Cascades, Oregon High Cascades, Newberry, Lassen, Medicine Lake | US Cascades total advective heat 1,050 MW: thermal springs ~240 MW (Cl flux x geothermometer T), slightly thermal springs ~660 MW, fumaroles ~160 MW. ~1.7 MW per km of arc south of 45°15'N, only ~0.1 MW/km north of it | Ingebritsen & Mariner 2010, https://pubs.usgs.gov/publication/70037638 |
| Same, Oregon detail | North-central Oregon Cascades | Groundwater removes heat from rocks younger than ~6 Ma; the deep anomaly is confined to the <2 Ma arc; intrusion rate 9-33 km3 per km of arc per Myr fits the heat budget | Ingebritsen, Sherrod & Mariner 1989, Science 243:1458, https://pubs.usgs.gov/publication/70015370 ; PP 1044-L https://pubs.usgs.gov/publication/pp1044L |
| Cold aquifer lid | Eastern Snake River Plain | Aquifer base ~860-970 m. Gradient 4.5 C/km above ~950 m, 72-75 C/km from ~970-1,440 m. 16.3 C at 951 m, ~94 C extrapolated at 1,912 m. Heat flow 132 ± 26 mW/m2. Geothermometers 125-140 C. Smectite clay seal begins at ~950-1,020 m | Lachmar et al. 2017, Geothermal Energy 5:28, https://link.springer.com/10.1186/s40517-017-0086-8 ; Project Hotspot report https://gdr.openei.org/files/1442/EE0002848_%20Final_Report_Shervais.pdf |
| Regional carbonate sweep | Eastern and central Nevada, western Utah (Eureka Low) | Heat flow below ~60 mW/m2 versus ~85+ regional and >100 in the Battle Mountain High (unverified exact values). Explained by deep interbasin flow in Paleozoic carbonates | Sass et al. 1971, https://data.nbmg.unr.edu/public/Geothermal/GreyLiterature/Sass_HtFlow_WesternUS_1971.pdf ; Lachenbruch & Sass 1977 (via USGS OFR 82-973 https://pubs.usgs.gov/of/1982/0973/report.pdf) |
| Lateral outflow | Calderas, Great Basin range-front faults | Long Valley: reservoir 202-214 C in west moat, outflow east and southeast toward Casa Diablo and Hot Creek; "temperature reversals in virtually every thermal well" before 1988 | Sorey et al. 1991 (OpenEI summary), https://openei.org/wiki/Conceptual_Model_At_Long_Valley_Caldera_Geothermal_Area_(Sorey,_Et_Al.,_1991) |
| Lateral outflow, volcanic | Lassen | Steam and steam-heated features high in the park. High-chloride liquid comes out at lower elevation outside the park (Morgan and Growler springs, roughly 8-12 km away, unverified distance), fed by the same upflow | Sorey & Ingebritsen 1984, WRI 84-4278, https://pubs.usgs.gov/publication/wri844278 |

Plain reading: in the Cascades the heat is real, but the shallow ground is scrubbed. Ingebritsen's work suggests the hot-spring heat is only part of the total anomaly (unverified share). That leaves a large unseen deep resource under the arc, and the only cheap surface handle on it is the chemistry and heat of the water leaving it.

### F2. A dry, deep vadose zone is not the main mask. Moving water below it is (calc and inference)
- Heat crossing a dry, still vadose zone moves by conduction. Dry alluvium has low conductivity (~1-1.5 W/m/K versus ~2-3 for wet rock, typical textbook values). So the same heat flux gives a *steeper* gradient and a *larger* 2 m anomaly. A deep water table by itself amplifies the shallow signal, as long as the upflow reaches the water table.
- The masking happens when (a) the upflow stalls and spreads at an aquifer, or (b) the aquifer carries the heat sideways. Great Basin water tables are often 50-300 m deep under fans and benches (more than 500 m at Yucca Mountain; unverified general range). So a 2 m reading only sees the heat that is *left over* after the aquifer has done its sweep.
- Model consequence: water-table depth should not be a plain penalty. The model should use aquifer transmissivity and hydraulic gradient (sweep strength) together with water-table depth (lid thickness).

### F3. How far an outflow plume carries a signal (calc)
- Picture a hot aquifer layer of thickness b, Darcy speed v, at depth d below the surface. Heat leaks upward by conduction at about λ·ΔT/d per m2. The plume's heat content per unit width is ρc·v·b·ΔT. So the signal decays over a length of about **L = ρc·v·b·d / λ**.
- With ρc = 4.2 MJ/m3/K, b = 100 m, d = 50 m, λ = 2 W/m/K:
  - v = 10 m/yr: L ≈ 3 km.
  - v = 100 m/yr: L ≈ 33 km.
- This fits the field cases: a few km in Great Basin alluvium, 10-20 km in caldera fill and young volcanics (Long Valley, Lassen, the Western Cascades springs).
- The same aquifer can also hide an upflow. A 0.5 W/m2 anomaly 2 km wide, under an aquifer with v = 10 m/yr and b = 100 m, warms that aquifer by only about **7.5 C** (calc). That is easy to miss in a single well and invisible at 2 m.
- Conductive halo for comparison: a buried heat source spreads sideways by about √(κt). That is ~0.6 km after 10,000 years and ~1.8 km after 100,000 years (κ = 1e-6 m2/s). So without water, the surface footprint is about as wide as the source is deep (1-2 km). With water, the footprint is shifted and stretched downstream by 3-30 km.

### F4. What depth can see what (calc, building on M21)
- In a temperature-depth log, vertical water flow bends the profile (Bredehoeft and Papadopulos 1965 method). Over a 100 m interval, a Péclet number of 0.1 is about the smallest bend you can resolve. That equals a vertical flux of **~5e-10 m/s, or about 1.5 cm/yr** (calc). So a good log in a water well can detect slow upflow or downflow that no surface sensor can see.
- Signature shapes in logs (standard interpretation):
  - **Reversal** (temperature peaks, then falls with depth): lateral outflow at the peak depth. The upflow is up the hydraulic gradient, usually toward the range-front fault.
  - **Isothermal top, then a sharp kink**: a cold aquifer or rain-curtain lid (Kimama at ~950 m). Look below the kink.
  - **Convex-up** (gradient grows upward): upflow at this spot.
  - **Concave-up**: recharge or downflow (a "cold" reading, not a true negative).
- Seasonal noise is gone below ~10-15 m (M21). So any water well deeper than ~30 m gives a usable profile shape, if the log is dense (1 m or less) and the well has rested.

### F5. Water chemistry travels further than heat
- Chloride, boron, lithium and dissolved helium are not lost to conduction the way heat is. Ingebritsen and Mariner used **chloride flux in streams times geothermometer temperature** to measure hidden hot-spring heat for the whole Cascade arc (F1). This is a proven way to "weigh" a hidden system from a stream gauge.
- Mixed, cooled outflow water still carries geothermometer information. The Kimama 1,070 m sample gave 125-140 C even though the measured T was far lower (Lachmar et al. 2017).
- In carbonate sweep areas, warm regional springs (for example Ash Meadows and the White River springs, unverified temperatures) are the outlet of the sweep. Heat and chemistry budgets for them set an upper bound on the hidden heat upstream.

### F6. Today's labels are biased toward one mask
- M18 found that nearly every historic blind find hit 100 C shallower than ~300 m. Those are mostly outflow tongues that reached shallow wells. Upflows under cold aquifers (SRP), rain curtains (Cascades) or strong sweep (Eureka Low) are almost absent from the labels.
- So a model trained on known systems learns "outflow-visible" settings and gives low scores to masked ones. USGS 2008 favorability and the high-favorability-but-few-systems areas (southern Idaho, eastern Oregon, western Utah) match where these masks are strongest (inference from L02 and the sources above).

## Datasets

| Dataset | Access | Coverage | Value for blind detection |
|---|---|---|---|
| USGS NWIS groundwater levels and water-quality (temp, specific conductance) | https://waterdata.usgs.gov | US, millions of records | Water-table depth, hydraulic gradient direction, warm wells |
| Water Quality Portal (WQP) | https://www.waterqualitydata.us | Multi-agency | Cl, B, Li, temperature at springs and wells (M06 counts ~54,000 western groundwater-temp sites) |
| USGS stream gauges with continuous specific conductance and temperature | https://waterdata.usgs.gov (parameter 00095, 00010) | Hundreds of western gauges (unverified count) | Chloride-flux proxy. Detects hidden thermal input to a watershed |
| Zell & Sanford 2020 CONUS groundwater model outputs (water-table depth, recharge, flow) | USGS ScienceBase, Water Resources Research 2020 (unverified exact link) | CONUS, 1 km | Lid thickness and sweep strength per cell |
| Fan et al. 2013 global water-table depth | Science 339:940; data via authors (unverified link) | Global, ~1 km | Same, also for outside US |
| Reitz & Sanford recharge maps | USGS ScienceBase (unverified link) | CONUS | Rain-curtain strength proxy |
| PRISM precipitation | https://prism.oregonstate.edu | CONUS, 800 m | Recharge proxy, rain curtain |
| Principal aquifers map (carbonate, basalt, basin fill) | https://www.usgs.gov/mission-areas/water-resources/science/principal-aquifers-united-states | CONUS | Which mask type applies |
| Cascades heat-discharge site data (Ingebritsen & Mariner) | USGS publications above | Cascade arc | Labels for advective heat per spring |
| SMU / NGDS heat flow and temperature-depth logs | https://geothermal.smu.edu ; https://gdr.openei.org | Western US | Profile shapes (reversals, isothermal tops) as features and labels |
| Nevada NDWR driller reports | https://water.nv.gov | 146,235 reports, 14,278 with temperature (M06) | First-water temperature, depth, static level |

## What dominates the uncertainty

1. **Which way and how fast shallow-to-mid groundwater moves** in each basin (transmissivity times gradient). This sets the 3-30 km range for plume travel, and whether a blank area is truly blank.
2. **How much heat is swept away at depth** in the Eureka Low and the Snake River Plain. We know these areas have low surface heat flow, but not how much deep upflow is hidden below them.
3. **The share of the Cascade heat anomaly that never surfaces**. Only ~240 MW reaches hot springs, and the deep resource under the arc is barely drilled.
4. **Profile data are rare**. Most well temperatures are a single number (M06), so we cannot tell outflow from upflow from sweep.
5. **Label bias**. Known blind systems over-sample the outflow-visible type (F6), so priors for masked settings are weak.

## What a sensor could fill

- **Full-profile drop probe (upgrade to the existing hardware pick)**: log temperature every 0.5-1 m on the way down, plus conductivity, and later a rested repeat. It is the same ranch visit, but the output is a profile shape: reversal, kink or convex. That one change turns each well into a mask classifier and a 1.5 cm/yr flux meter (F4).
- **Stream and spring chemistry loggers ("watershed tree")**: cheap conductivity and temperature loggers with a stage sensor, plus monthly grab samples for Cl, B, Li and helium. Put them at stream confluences in a nested tree, like stream-sediment sampling in mineral exploration. A jump in chloride flux between two nodes pins the hidden inflow to one sub-basin. This is best in the Cascades and other rain-curtain areas, where no surface probe works. No permit is needed for loggers at public crossings on casual-use terms (unverified for each state).
- **Spring heat budget kit**: a flow meter (flume or salt dilution) with temperature and conductivity, at warm springs at the outlet of carbonate sweeps. Advected heat equals flow times ρc times ΔT. This gives an upper bound on the hidden heat upstream.
- **Thermistor chains left in open wells for days**: to catch reversals and the slow flow inside the well.
- **E-field MT nodes (existing pick)**: under a cold lid, the smectite clay cap (Kimama: ~950-1,020 m) is a strong conductor. MT is the cheapest way to see under the lid without drilling.
- **Placement rule**:
  - Detect downstream: valley floors, springs, confluences, the lowest wells in a basin.
  - Locate upstream: walk up the hydraulic gradient toward the nearest range-front fault, step-over or accommodation zone.
  - Under a lid: skip 2 m probes. Use deep wells, MT and chemistry.
  - In dry basins with slow flow: 2 m arrays still work, because a dry lid amplifies the signal.

## Implications for a better model

1. **Add a hydrologic transfer layer.** For each cell, route a hypothetical deep heat source through a simple groundwater model (Zell & Sanford flow field, aquifer type, recharge) to predict where its signal appears at 2 m, in wells, and in springs and streams. Then compare predictions with observations. This is a forward model inside the likelihood, not an extra feature.
2. **Use a detection probability per cell and per sensor**, conditioned on mask type. A blank 2 m survey under a rain curtain or cold aquifer should barely lower the posterior. A blank one in a dry, slow basin should lower it a lot (extends M21).
3. **Treat warm water as evidence of a source upgradient, not on the spot.** The likelihood for a warm well or spring should spread over the upgradient catchment, weighted by the plume decay length L (F3).
4. **Use temperature-profile shape as a feature and as a label.** Reversal = outflow nearby. Isothermal-then-kink = lid. These come from SMU/NGDS logs now, and from our own probe later.
5. **Add a chloride/heat budget constraint.** The total advected heat out of a watershed (springs plus stream chloride flux) caps the hidden upstream resource. This gives hard bounds for the hidden-resource total in the Cascades and carbonate regions.
6. **Fix label bias** by weighting training labels by mask type, or by training separate sub-models for outflow-visible, lidded and swept settings. Then the hidden-resource total for masked ground is not inherited from outflow-type priors.
7. **Business angle**: masked ground (southern Idaho, eastern Oregon, Cascades flanks, Eureka Low margins) is where competitors' surface-data ML is weakest. If our physics transfer layer plus chemistry loggers can see through the mask, that is where cheap rights are most mispriced (inference).
