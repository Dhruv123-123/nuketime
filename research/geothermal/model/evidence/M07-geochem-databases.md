# M07: Water chemistry and geothermometers at scale (NWIS, NURE HSSR, Great Basin compilations, helium, CO2)

**Builds on:** L15 (geothermometer physics, Water Quality Portal, GeoThermalCloud NMFk, Kennedy & van Soest 2007), M02 and M03 (ranch-well chemistry as a "see-through-the-cold-aquifer" signal), and hardware H04/H09 plus the prior pick of a ranch water-well drop probe. This file does not repeat those. It adds three things: the NURE HSSR archive, the actual size of the Great Basin compilations, and a concrete way to turn scattered water chemistry into a blind-upflow layer.

**Method note.** I used 9 web searches and 9 fetches. One page (mrdata.usgs.gov/nure/water/) was blocked by a permission timeout, so I could not read the NURE water record count. Facts I could not confirm are marked (unverified).

## Bottom line

Regional water chemistry can flag blind upflow, but not as a raw map of geothermometer temperatures. The usable signal is a leak. Hot deep fluid mixes into cold aquifers and shows up in ordinary wells as excess boron, lithium, chloride, silica, a shifted Na-K-Mg balance and, best of all, mantle helium (³He/⁴He above about 0.8–1.5 Ra against a ~0.1–0.6 Ra background). These leaks are often kilometres down the hydraulic gradient from the upflow. The public data are large but messy:
- about 24,800 western samples in the NBMG/Zehner-Coolbaugh-Shevenell Great Basin compilation, 8,780 of them above 20 °C;
- about 14,300 points in the GeoThermalCloud set;
- hundreds of thousands of NURE HSSR well and spring waters from 1975 to 1980, which carry Na, K, Mg, Li, B, Si and Cl from one lab (Oak Ridge);
- WQP/NWIS on top of all this.

Nobody has merged them, deduplicated them, corrected them for lab bias and mixing, and back-projected them along groundwater flow. Zanskar's GeoCore does not use geochemistry (Z03/MEMO). So this is open, cheap alpha. A 2002 Nevada weights-of-evidence model already found that boron interpolated from NWIS alone gives a contrast of 2.03, and up to about 3.5–4 for high-temperature and power systems. Coverage is the binding gap: points follow towns, roads and wells, and helium isotopes exist at only a few hundred sites. That is exactly what our ranch-well visit fills. Each visit should collect a filtered bottle and a helium sample, not just a temperature log.

## Findings

1. **The Great Basin compilation is about 24,800 samples, not about 14,000.** NBMG's "Great Basin Geochemical Data for Groundwater Concentration Maps" (Zehner, Coolbaugh and Shevenell; published 2006, metadata 2010) holds 24,769 aggregate samples.
   - Temperature: 8,780 report temperatures above 20 °C, and 10,713 report 20 °C or below.
   - Analytes: 14 (As, B, Ba, Ca, Cl, F, Fe, HCO₃, K, Li, Mn, Na, SiO₂, SO₄), plus Sr.
   - States: NV, CA, UT, ID, AZ, OR, WY.
   - Sources: NWIS (2005 pull, including the former USGS GEOTHERM database), the NBMG geothermal database, and the Geo-Heat Center Western Geothermal Database (Reed et al. 1983; Boyd 2002).
   - NURE is NOT included, and no sample dates are given.
   - Source: https://data.nbmg.unr.edu/Public/Geothermal/Data/GeochemicalData/_metadata/HTML_Files/GroundwaterSampleSites.html. A Utah FORGE copy is at https://catalog-beta.data.gov/dataset/utah-forge-great-basin-groundwater-geochemical-database.

2. **Regional groundwater chemistry already works as a predictive layer (Coolbaugh et al. 2002, Nevada GIS).**
   - Method: boron from log-normalized NWIS data, interpolated by inverse distance weighting.
   - Boron contrast: 2.03 (W+ 1.53, W− −0.50, studentized confidence 4.5). For high-temperature systems the contrast is 3.54, and for "power" systems 4.09.
   - The 8 producing systems average 13,700 ppb B.
   - B and Li correlate at r = 0.78 in NWIS.
   - Boron was one of 7 layers in the high-temperature logistic model.
   - Training temperatures used max(measured, mean geothermometer). The SiO₂ and Mg-corrected Na-K-Ca estimates differed by 14% on average.
   - Source: https://data.nbmg.unr.edu/public/Geothermal/GreyLiterature/Coolbaugh_GeothermalGIS_NV_2002.pdf
   - This is a 2002 result using one element and crude interpolation. A modern model that uses all solutes, mixing correction and flow-path awareness should do better (untested, which is not a kill).

3. **NURE HSSR is a large, unused, single-lab water archive.**
   - History: the AEC/DOE program ran from 1975 to about 1983. Systematic sampling started in 1976 on 1°×2° quadrangles.
   - Coverage: 307 of 625 quadrangles were fully sampled and 86 partially.
   - Labs:
     - LLL had AZ, CA, ID, NV, OR, UT and WA: about 38,000 sites sampled, about 30,000 analysed, but only about 13,000 reported.
     - LASL had CO, MT, NM, WY and parts of AZ, ID, TX and UT.
     - SRL took over parts of the western states from 1979, under the "SRL-W" format.
     - ORGDP had the central US.
   - Data problems: originally 894 files in 47 formats, with only 817 converted. Some data exist only on microfiche, and 32 LLL quadrangles may have been analysed but were never published. There are also duplicate SRL analyses, and early samples were analysed for uranium only.
   - Archive: about 500,000 SRL resin water samples went to USGS in 1985 and could, in principle, be re-analysed (unverified whether they still exist and are usable).
   - Source: https://pubs.usgs.gov/of/1997/ofr-97-0492/nurehist.htm

4. **NURE water chemistry contains geothermometer inputs.** Example: the Lemmon quadrangle has 728 waters (626 wells, 102 springs).
   - Method: ORGDP emission spectroscopy for Al, B, Ba, Ca, Fe, K, Li, Mg, Na, Si, Sr and others, plus Cl and SO₄. That is enough for quartz/chalcedony (from Si), Na-K, K-Mg and Na-K-Ca, plus B and Li tracers.
   - Caveats: samples were not filtered or acidified in the field. They were filtered at 0.45 µm in the lab. Silica can drop out before analysis, which would bias silica geothermometers low (a conservative error). Coordinates are about ±70–110 m.
   - Sources: https://pubs.usgs.gov/of/1997/492/quad/q_lemmon.htm. The data portal is http://mrdata.usgs.gov/nure/water/ (blocked here) and https://data.amerigeoss.org/en/dataset/nure-water (CSV, shapefile and dBase). The western-state water record counts are (unverified).
   - Field temperature, pH and conductivity were recorded on many NURE samples (unverified per lab).

5. **Helium isotopes are the strongest direct blind-permeability tracer, and the data are very sparse.** Kennedy and van Soest (2005, LBNL; Science 2007) report these Basin and Range values:
   - west-margin values up to 6–7 Ra;
   - a regional background of about 0.6 Ra, falling to about 0.1 Ra in the east (minimum 0.014 Ra);
   - local "He-spikes" of 0.8–2.1 Ra above the local background;
   - Dixie Valley production fluids at 0.70–0.76 Ra, or about 8–12% mantle helium.

   Not every range-front fault carries the signal, so helium separates deep-permeable faults from dead ones. The authors call it possibly "the best, and perhaps only" indicator of deep permeability under cool shallow reservoirs. Source: https://escholarship.org/content/qt67p1z91d/qt67p1z91d.pdf

6. **Helium works for blind systems outside Nevada as well.** In the Snake River Plain (LBNL/INL/U. Idaho, DOE 2015), about 20 new analyses found 7 samples above 1.5 Rc/Ra, clustered in 3 zones.
   - Six of the seven sit where geothermometers predict 110–172 °C.
   - The highest value was Barron's well at 2.36 Rc/Ra.
   - The team targeted Mountain Home, a hidden system of about 150 °C.

   This is a working example of helium plus geothermometers at regional scale in ordinary wells. Source: https://www.energy.gov/sites/default/files/2015/06/f23/Track2_Hydrothermal_4.2_Dobson_He_isotopes.pdf

7. **What controls the helium anomaly.** Banerjee et al. (2011, Geology, Coso and Beowawe) model helium anomalies as deep meteoric circulation along permeable faults (10⁻¹² to 10⁻¹⁵ m²). In that model the mantle flux itself is negligible. So high ³He/⁴He at the surface maps fault permeability and circulation depth, which is exactly the hidden-upflow target. Source: https://www.usgs.gov/publications/deep-permeable-fault-controlled-helium-transport-and-limited-mantle-flux-two

8. **The unsupervised ML baseline is weak, which leaves room to improve.** GeoThermalCloud NMFk on 14,258 points labels about 36% as "high prospectivity" (L15), which is far too broad to drive leasing. The likely fixes are mixing correction, lab harmonization, flow-path back-projection and supervision against known systems (inference).

9. **State programs still collect fluid geochemistry, but only at single sites.** The 2025 Lund North (Utah) blind-system program lists new fluid geochemistry, and a legacy gradient hole there reads above 220 mW/m². The record does not yet tie geochemistry to a confirmed blind system. Source: https://www.usgs.gov/publications/exploration-blind-geothermal-systems-eastern-great-basin-utah-update-lund-north. Elsewhere, M03 notes that Gabbs Valley irrigation wells at 32 °C gave chalcedony temperatures above 110 °C.

10. **The physics of the false signals is known and can be modelled.**
    - Mixing with cold water: correct with silica-enthalpy and Cl-enthalpy mixing models (Fournier 1977).
    - Re-equilibration in the shallow subsurface: screen with Giggenbach Na-K-Mg maturity, where only "partially equilibrated" or better gives temperatures, while "immature" waters still carry B/Li/Cl excess.
    - Evaporite and playa brines inflate Na-K and B. Separate them using Cl/B, Br/Cl and δ¹⁸O.
    - CO₂-rich waters distort Na-K-Ca. Use a CO₂ correction or K-Mg instead.

    See L15 for citations. These are exactly the steps a model can learn or apply as fixed physics.

11. **CO₂ and soil gas.** Diffuse CO₂ flux and soil-gas He/CO₂ are standard near-field tools (H04, H09). No regional public database exists for the western US, so this layer would have to come from our own sensors (inference, consistent with H04).

## Datasets

| Dataset | Access | Coverage | Value for blind detection |
|---|---|---|---|
| NBMG Great Basin Groundwater Geochemical Database (Zehner, Coolbaugh, Shevenell 2006) | Free; NBMG data server, Utah FORGE/data.gov copy | 24,769 samples; NV, CA, UT, ID, AZ, OR, WY; 14 analytes, including SiO₂, Na, K, Li, B, Cl | High: the ready-made base table. Includes cold wells, which hold the leak signal. |
| USGS NWIS / Water Quality Portal | Free API (waterqualitydata.us) | 290M+ records, 2.7M+ sites nationally (L15) | High after QC: the post-2005 data are not in the NBMG set. Extends coverage beyond the Great Basin. |
| NURE HSSR water (USGS OFR 97-492; mrdata.usgs.gov/nure/water) | Free; CSV/shapefile | 1975–80; 307 full plus 86 partial of 625 quadrangles; western LLL data partly unreported | High and unused: thousands of wells and springs from one lab, with Si, Na, K, Mg, Li, B, Cl. Pre-pumping baseline. |
| NURE archived physical samples (about 500,000 SRL resin waters, about 380,000 sediments) | USGS archive (unverified whether still accessible) | National | Medium: possible re-analysis for B/Li in sediments near springs (speculative). |
| USGS GEOTHERM / Geo-Heat Center Western Geothermal Database | Inside the NBMG set; also NGDS | Thermal springs and wells, western US | Medium: mostly known systems, so a labelled training set. |
| GeoThermalCloud Great Basin set (Ahmmed & Vesselinov 2022) | GitHub/OSTI | 14,258 points, 18 attributes, sparse | Medium: baseline to beat. |
| Helium isotope compilations (LBNL Kennedy & van Soest; Snake River Plain LBNL/INL; Welhan 1989; Unocal/WHOI) | Papers and supplements; partly unpublished | A few hundred sites across the Basin and Range (unverified count) | Very high per point; coverage is the problem. |
| USGS National Produced Waters Geochemical Database | Free (USGS) | About 165k samples, mostly oil and gas basins (unverified, from L15) | Medium for sedimentary plays (L10): Na-K-Mg on deep brines. |
| State thermal-spring and well reports (NBMG, UGS, Oregon DOGAMI, Idaho IGS) | Free PDFs; many need OCR | Patchy | Medium: fills gaps and hand-curated labels. |

## What dominates uncertainty

1. **Sampling coverage and bias.** Points sit on towns, highways, irrigation districts and known springs. Remote basins, which is where the cheap BLM and ranch land is, have little or no chemistry. The model's confidence there falls back to the prior. This is the biggest gap.
2. **Mixing and dilution.** A blind upflow under a big cold aquifer can be diluted until silica and cation geothermometers read cold. Only conservative tracers (B, Li, Cl, ³He) survive. How deep the leak is diluted, and how far it travels downgradient, are unknown site by site.
3. **Offset from source.** Outflow plumes move km to tens of km along the hydraulic gradient. Without groundwater head and flow direction, an anomaly cannot be placed back over its upflow.
4. **Harmonizing labs and eras.** NURE (unfiltered and unacidified until the lab), 1970s USGS and modern ICP-MS data differ in detection limits and silica loss. Duplicates exist across NWIS, GEOTHERM, NBMG and NURE.
5. **Confounders.** Evaporite and playa brines, irrigation return flow, mining, and CO₂-rich waters can all imitate geothermal B/Li/Na-K signals.
6. **Helium sparsity.** The best single tracer exists at too few points to interpolate.
7. **Missing depth context.** Many records lack well depth or screened interval, so shallow and deep waters cannot be separated.

## What a sensor could fill

- **Upgrade the prior ranch-well drop probe into a "wellhead geochem pod" (same visit, same signed heat option).**
  - Inline sensors: in-situ temperature-depth log, conductivity and pH.
  - A 0.45 µm field-filtered, acidified bottle for ICP (SiO₂, Na, K, Mg, Ca, Li, B, Cl, Br). Lab cost is tens to about $100 per sample (unverified).
  - A field silica photometer (molybdate) and a boron photometer (azomethine-H) give same-day triage.
  - A copper-tube or passive diffusion sampler for dissolved He and ³He/⁴He, at a few hundred dollars per noble-gas lab analysis (unverified).
  - Every visit then adds a modern, harmonized, georeferenced point in exactly the remote places where public data are missing.
- **Portable ⁴He sniffer (a leak-detector-class mass spectrometer) for dissolved He and soil gas.** It screens for excess ⁴He in real time, and only anomalous wells get the expensive ³He/⁴He lab run. This cuts isotope cost per useful point (assumed it can work).
- **Soil CO₂ flux chamber plus soil-gas He/CO₂ on 2 m probe traverses** (ties to H01/H04). It fills the missing regional CO₂ layer over candidate upflows flagged by the water-chemistry back-projection.
- **Long-term passive samplers left in stock wells.** These are cheap diffusion samplers or conductivity/temperature loggers, picked up on the next visit. They give time series that separate steady geothermal leakage from seasonal irrigation effects.
- **Water-level loggers in the same wells.** They give the head data needed to back-project anomalies along flow paths.

## Implications for a better model

1. **Build a merged, deduplicated western water-chemistry table.**
   - Inputs: NBMG 24.8k plus post-2005 WQP plus NURE water (all western quadrangles) plus GEOTHERM, Geo-Heat Center and state reports.
   - Steps: lab and era bias terms, a charge-balance filter (CBE <10%), and a well-depth field where available.
   - This is a few weeks of data work and a lasting moat. No competitor has it.
2. **Model each sample as a noisy observation of a mixed fluid, not as a temperature.**
   - The latent variables are deep temperature T_d, hot fraction f and degree of re-equilibration.
   - The observations are silica, Na-K, K-Mg, Na-K-Ca, the Giggenbach maturity index, B, Li, Cl, Br/Cl and δ¹⁸O.
   - A Bayesian mixing or physics-informed model (Fournier 1977 mixing, GeoT-style multicomponent equilibrium) outputs a posterior of "deep hot fluid present upgradient" with credible intervals. This replaces single-ratio geothermometer maps.
3. **Back-project along groundwater flow.**
   - Use regional potentiometric surfaces (USGS RASA / Great Basin carbonate aquifer studies) plus our water-level loggers to trace anomalies upgradient.
   - Convert each leak into a probability footprint over fault intersections, the INGENIOUS structural layers and the M02 permeability proxies.
   - This is how scattered well chemistry becomes a blind-upflow map.
4. **Treat helium as a separate high-weight channel.**
   - Label ³He/⁴He above local background (He-spike above about 0.8 Ra in the central basin) as evidence of deep-permeable faults.
   - Use it to separate live from dead range-front faults in the structural model. Spend sensor budget where the model's posterior on fault permeability is most uncertain (active learning).
5. **Use positive-unlabeled learning against known systems** (DeAngelo/Mordensky labels, M01). Make geochem features "absence-aware": missing data is not negative evidence, which avoids the NMFk "36% everywhere" problem.
6. **Expect lift where structure is ambiguous and chemistry exists.** The 2002 boron-only contrast of 2.0–4.1 suggests geochemistry is one of the stronger single layers. Combined with flow-path back-projection, it should sharpen favorability over basins where heat flow and structure alone cannot separate targets (expected, untested).
7. **Run the business loop.** The model flags basins where chemistry is sparse and the posterior is wide. The ranch-well pod samples them and signs heat options on the same visit. New points shrink uncertainty, and only then do we file state or BLM rights. Chemistry is the cheapest data per km² of confidence we can buy, and it needs no permit.

## Sources
- NBMG Great Basin groundwater geochem metadata: https://data.nbmg.unr.edu/Public/Geothermal/Data/GeochemicalData/_metadata/HTML_Files/GroundwaterSampleSites.html
- Utah FORGE copy: https://catalog-beta.data.gov/dataset/utah-forge-great-basin-groundwater-geochemical-database
- NBMG geochem database page: https://nbmg.unr.edu/Geothermal/GeochemDatabase.html
- Coolbaugh et al. 2002 Nevada geothermal GIS: https://data.nbmg.unr.edu/public/Geothermal/GreyLiterature/Coolbaugh_GeothermalGIS_NV_2002.pdf
- NURE HSSR history (USGS OFR 97-492): https://pubs.usgs.gov/of/1997/ofr-97-0492/nurehist.htm
- NURE Lemmon quadrangle example: https://pubs.usgs.gov/of/1997/492/quad/q_lemmon.htm
- NURE water dataset: https://data.amerigeoss.org/en/dataset/nure-water ; http://mrdata.usgs.gov/nure/water/ (blocked during this run)
- Kennedy & van Soest 2005 (LBNL): https://escholarship.org/content/qt67p1z91d/qt67p1z91d.pdf
- Dobson et al., DOE 2015 Snake River Plain He isotopes: https://www.energy.gov/sites/default/files/2015/06/f23/Track2_Hydrothermal_4.2_Dobson_He_isotopes.pdf
- Banerjee et al. 2011 Geology: https://www.usgs.gov/publications/deep-permeable-fault-controlled-helium-transport-and-limited-mantle-flux-two
- Hardwick et al. 2025 Lund North: https://www.usgs.gov/publications/exploration-blind-geothermal-systems-eastern-great-basin-utah-update-lund-north
- INGENIOUS Great Basin compilation: https://data.amerigeoss.org/dataset/ingenious-great-basin-regional-dataset-compilation-a96d7
- For Fournier, Giggenbach, Spycher GeoT, WQP and GeoThermalCloud, see L15.
