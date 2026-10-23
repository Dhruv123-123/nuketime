# P24: Field Gas Lab, a wellhead membrane mass-spec cartridge plus a valley trailer for same-night 3He/4He and geothermometry

Date: 23 Oct 2026. Build candidate P24, model track. This builds on `../MODEL.md` (SENTINEL-COX, the shared latent mask class, ranked uncertainties), `M22-gas-isotopes.md` (why helium is the one gas that sees blind permeability; data sets; the tritium, air and crustal-He traps; lab costs), `../../../hardware/evidence/H04-soil-gas-geochem.md` (miniRUEDI specs: 13 kg, 50 W, He/Ar/Kr/N2/O2/CO2/CH4 in under a minute at 1-3%; McGinness Hills 0.35-0.57 Ra), `P01-ranch-well-sentinel-2-0-a-resident-well-.md` (the resident Sentinel), `P04-wellhead-clamp-fleet-no-entry-discharge-.md` (the gauge-port tee we tap into) and `P05-pump-cycle-mixing-sampler-an-irrigation-.md` (flow cell, copper tubes by hand). It does not repeat them.

**Method note.** The shared web budget for this workflow turn was used up before this agent ran. Both searches I tried were refused, and the one fetch I tried (Brennwald et al. 2024, https://gi.copernicus.org/articles/13/1/2024/gi-13-1-2024.pdf) was blocked. So no new web pages were read. Facts from repo files are cited by file. Facts from standard literature I know are marked (from memory, unverified). All prices are my estimates and are (unverified). Numbers I computed are marked (calc). The Monte Carlo is in `P24_identifiability_mc.py` next to this file.

## Bottom line

Build the cartridge now. Build the trailer second, and start it as a fixed "garage lab" in a valley town before putting a magnetic-sector mass spectrometer on wheels.

1. **The cartridge is the real alpha, and it is cheap.** A home-built miniRUEDI-class unit (membrane contactor, quadrupole RGA, getter, plus one change: a 77 K charcoal trap so neon can be read cleanly) costs about **$25-40k BOM** for v1 and adds about **15-20 minutes** to a Sentinel or Clamp visit. It reads air-corrected excess helium on every well we touch. Helium from a deep fluid is 100-1,000 times richer than air-saturated water, so even 0.1-1% of deep fluid in a cold ranch well shows up (calc below). That turns a "cold blank" into "cold but He-rich", which is exactly the mask-breaking second detector the model needs.
2. **Helium fixes rank 1 better than any other add-on we have priced.** In my Monte Carlo of the shared mask model, temperature alone needs a correction factor of about **x2.4 (5-95%: x1.6 to x4.4)** to go from detected systems to present systems in surveyed cells. Adding an excess-He detector brings it to **x1.4 (x1.2 to x1.9)**. The band ratio drops from **2.7 to 1.6, about 1.7x tighter**, and the median extrapolation falls by 40%. The reason is that helium's failure mode (thick sealed lid) differs from temperature's failure modes (lid, sweep), so the two rarely fail together.
3. **The trailer turns He-rich into "mantle, therefore open and deep".** Excess He alone cannot tell a deep upflow from old cold basin water, which also gathers crustal 4He. Only 3He/4He (R/Ra) splits them. A valley lab with a static-vacuum sector mass spectrometer, an extraction line, an MP-AES and an ion chromatograph gives R/Ra plus solute geothermometers **the same night**, at about **$60-120 marginal per point** (about $150-250 fully loaded) against **$300-700 and 6-12 weeks** at a university lab (M22, H04). Fully built it is **about $450-900k** (unverified).
4. **One honest limit: tritium.** Young water carries bomb-tritium 3He. Its error on R/Ra is small only when the sample has a lot of excess He. My rule (calc below): trust same-night R/Ra when terrigenic He is at least about 10 times air-saturated water. Below that, R/Ra waits for a tritium run (months), and the model uses excess He and Ne only.
5. **Rights edge.** The answer arrives while the rancher is still at the gate (cartridge) or by breakfast (trailer). So the option can carry a pre-agreed step-up that we trigger the next morning, and the adjacent state first-file and BLM noncompetitive filings can go in within 24-48 hours instead of after a 6-12 week lab wait. No samples leave our hands, so no outside lab sees our map.

## 1. Physics: why this detects blind upflow

### 1a. Helium is a loud tracer that survives dilution
- **Air-saturated water (ASW)** at 10-15 C and 1,300 m elevation holds about 4.0-4.5e-8 cm3STP/g He and about 1.6-1.8e-7 cm3STP/g Ne (from memory, unverified; standard solubility tables, e.g. Weiss 1971). He/Ne in ASW is about 0.24-0.27, and in air 0.288.
- **Geothermal and deep fluids** carry about 1e-6 to 1e-4 cm3STP/g He, which is 20 to 2,000 times ASW (from memory, unverified; typical of Great Basin production fluids, e.g. Kennedy and van Soest 2005, https://escholarship.org/content/qt67p1z91d/qt67p1z91d.pdf, cited in M22).
- **Mixing arithmetic (calc).** A ranch well that pulls a fraction f of deep fluid with He_deep = 1e-5 cm3STP/g has excess He = f x 1e-5. Against an ASW of 4.5e-8, f = 0.1% gives +22% excess He. f = 1% gives +220%. A heat signal at the same f is tiny. A 150 C fluid at f = 1% warms a 15 C well by only about 1.4 C, which is inside the 1.5-2.5 C model noise of a single well residual (P04). So helium sees about 10-100 times deeper into the dilution tail than temperature does.
- **Detection limit (calc).** With He at +/-2% and Ne at +/-3% (miniRUEDI-class precision, H04), the excess-air correction gives terrigenic He to about +/-3-5% of ASW, so about +/-2e-9 cm3STP/g. A 3-sigma flag is then about 6e-9, which is f of about 0.06% for a 1e-5 end-member and f of about 0.6% for a weak 1e-6 end-member.
- **Helium crosses lids, but not perfectly.** He is inert and does not react with clay or microbes (M22). It does move with water, so a truly sealed clay cap that stops fluid flow also slows He. Long Valley soil He was low over altered ground (Hinkle and Kilburn 1980, https://pubs.usgs.gov/of/1980/0612/report.pdf, in M22). Dissolved He in wells below or beside a lid does better, because it samples the aquifer, not the soil. I set helium's sensitivity under a "cold lid" mask at about 0.43 (prior mean), against about 0.14 for temperature (judgement, unverified).
- **Helium beats temperature most under "swept" masks.** Cold recharge that sweeps heat away still carries the helium. Dilution lowers the He excess linearly, but it starts 100-1,000 times above background. Heat is also lost to rock along the path. Helium is not. Prior sensitivity 0.67 for He against 0.2 for T under sweep (judgement).

### 1b. The three-way split: air, crust, mantle
- **Air:** neon. Ne has no deep source in groundwater, so Ne above ASW is excess air from bubbles or pumping. He_excess-air = Ne_excess x 0.288.
- **Crust:** 4He from U and Th decay builds up with water age at roughly 1e-11 to 1e-10 cm3STP/g per year in basin aquifers (from memory, unverified). A 10,000-year-old cold carbonate water can reach 1e-7 to 1e-6 cm3STP/g, which looks like a deep fluid on the cartridge. R/Ra of crustal He is about 0.01-0.05.
- **Mantle:** R/Ra about 8 (MORB). Great Basin blind fluids run about 0.3-0.8 Ra (McGinness Hills 0.35-0.57, Dixie Valley 0.70-0.76, H04 and M22). Banerjee et al. (2011) explain this as deep circulation along faults with permeability of 1e-12 to 1e-15 m2 (https://www.usgs.gov/publications/deep-permeable-fault-controlled-helium-transport-and-limited-mantle-flux-two, in M22). So a well above about 0.1-0.2 Ra in the east, or about 0.3 Ra in the west, is a "deep open path" label.
- **That is why the trailer exists.** The cartridge gives "how much non-air He". The trailer's R/Ra gives "how much of it is mantle". Mantle-tagged He is a permeability-to-depth label (rank 2), not just a presence flag.

### 1c. The tritium trap, quantified (calc)
- One tritium unit (TU) decayed fully gives about 2.5e-15 cm3STP/g of 3He (from memory, standard 3H/3He dating constant).
- Water recharged in the 1960s to 1980s can carry tritiogenic 3He of tens to about 100 TU-equivalent (from memory, unverified; typical in US aquifers). Take 100 TU as a bad case: 2.5e-13 cm3STP/g of 3He.
- The R/Ra error is that 3He divided by total He, divided by 1.38e-6 (air 3He/4He).
  - At total He = ASW (4.5e-8): error about 4 Ra. Useless.
  - At He = 4.5e-7 (10x ASW): error about 0.4 Ra. Marginal in the west.
  - At He = 1e-6 (about 20x ASW): error about 0.18 Ra.
  - At He = 1e-5: error about 0.02 Ra. Negligible.
- **Rule for v1:** report same-night R/Ra as "firm" when terrigenic He is above about 10x ASW and the well is deeper than about 100 m or has an old-water hint (low NO3, high Na/Ca, no recent recharge signature). Otherwise mark it "provisional" and send a sealed tritium-ingrowth bottle to a lab for the top 5%. This keeps the likelihood honest. Ne also lets us correct the air 3He properly.

### 1d. Gas ratios and geothermometers
- **N2/Ar** tells air-derived gas (about 38 in ASW, 84 in air) from deep N2. **He/Ar** and **CO2/Ar** are deep-gas fingerprints. **CH4** flags biogenic or basin gas and helps reject petroleum-related He (judgement).
- **H2/Ar and CO2/Ar gas geothermometers** (Giggenbach 1980, Geochim. Cosmochim. Acta 44:2021; Giggenbach 1991, UNITAR/UNDP guide; from memory, unverified) assume gas equilibrated at reservoir temperature and arrived without loss. That holds for hot discharges, bubbling wells and steam. It does **not** hold in a cold, diluted ranch well, where microbes eat H2 and mixing resets ratios. So v1 reports gas geothermometers only for wells above about 35 C or with a free gas phase, and treats them as a likelihood with a wide error (+/-30-50 C). For cold wells, the useful gas outputs are excess He, Ne, N2/Ar and CO2/Ar as fingerprints.
- **Solute geothermometers in the trailer** (quartz and chalcedony silica, Na-K, Na-K-Ca, K-Mg, Li-Mg; Fournier 1977/1981, Giggenbach 1988; from memory) are the main temperature-at-depth read. Diluted water biases them. The new move is to use the helium fraction to un-mix: f from He, Cl and B gives the deep end-member, and the silica-enthalpy mixing model (Fournier and Truesdell 1974; from memory) then gives the reservoir temperature with an error bar. This is how helium also helps rank 5.

### 1e. Noise and failure modes
| Source | Size | Fix |
|---|---|---|
| Pumping and bubble excess air | Ne up to +10-50% over ASW (judgement) | Ne correction; flag Ne over +100% |
| Membrane not equilibrated | He fast (about 1 min), Ar and Kr slower (2-5 min) (judgement from GE-MIMS practice) | Read until the He and Ar trend is flat; 3 repeats |
| 40Ar++ on mass 20, CO2++ on mass 22 | 20Ne unreadable on a plain RGA (from memory) | 77 K charcoal trap removes Ar; getter removes CO2; read 20Ne and 22Ne |
| RGA drift | 1-3% per hour (judgement) | Ambient-air standard through the same membrane each hour; ASW standard daily |
| Old crustal He | Can look like upflow on the cartridge | Trailer R/Ra; water-age proxies |
| Tritiogenic 3He | Up to Ra-scale errors in low-He water | Rule in 1c; tritium lab on top 5% |
| Petroleum basin He | High He, low R/Ra, high CH4 | CH4/He and R/Ra |

## 2. v1 design

### 2a. "Cartridge" (wellhead unit, one per field crew)

Box: Pelican 1610-class case, about 56 x 43 x 27 cm, about 18-22 kg with battery. Runs off a 24 V LiFePO4 pack in the truck.

| Part | Spec | Est. price (unverified) |
|---|---|---|
| Membrane contactor | 3M Liqui-Cel MiniModule 1x5.5 class hollow-fibre polypropylene, water side 0.5-1.5 L/min, gas side to capillary (GE-MIMS layout, Mächler et al. 2012, Environ. Sci. Technol. 46:8288; from memory) | $200-400 (2 spares) |
| Water feed | Quick-fit hose to the P04 gauge-port tee or a sample bib; 12 V submersible purge pump (Monsoon / Proactive class) for idle wells; Sentinel tube wells use the pump on a short purge | $300-700 |
| Flow cell | Shared with P05: T (0.01 C), EC, pH, flow; reads "stable" before gas readings count | (shared) |
| Inlet | Fused-silica capillary, about 0.05 mm ID, 1-2 m, crimped to give about 1e-6 mbar in the analyser | $200 |
| Mass analyser | SRS RGA200 (1-200 amu, Faraday plus electron multiplier) or Pfeiffer PrismaPlus | $6-9k |
| High vacuum | Pfeiffer HiPace 30/80 turbo plus a small diaphragm backing pump | $7-11k |
| Getter plus ion pump | SAES NEXTorr D 100-5 class (NEG plus small ion pump), switched into a second path to strip N2, O2, CO2, H2, CH4 | $5-8k |
| Ar trap | Small activated-charcoal finger held at about 77 K by a Stirling cryocooler (Sunpower CryoTel MT class) or a 1 L LN2 dewar; He and Ne pass, Ar is held | $2-12k (LN2 vs cryocooler) |
| Valves and plumbing | All-metal micro valves, VCR fittings, a 0.5 cc air-standard pipette | $2-4k |
| H2 channel | Electrochemical H2 cell in the contactor headspace (ppm), because mass 2 on a small RGA has high background | $300 |
| Controller | Raspberry Pi CM4 or similar, Python control (miniRUEDI's control software is open source per H04's sources, unverified), tablet UI | $300-600 |
| Power | 24 V 1 kWh LiFePO4 plus 300 W inverter-free DC supply. Draw about 70-120 W (turbo 20-40 W, RGA 20 W, backing 15 W, controller 10 W, cryocooler adds 60-100 W) | $800-1,500 |
| GPS and comms | GNSS puck; LTE plus Iridium SBD fallback; result packet about 2 kB | $300-600 |
| Copper tubes and crimps | Weiss-type 3/8" Cu tubes with two pinch clamps, for the trailer and for lab cross-checks | $30-60 each |
| Bottles | Filtered and acidified cation bottle, raw anion bottle, silica dilution bottle, isotope vial | $10-20 per site |

**BOM v1: about $25-40k per unit** (the high end is the cryocooler). At 5+ units, about $20-30k each.

**Read sequence (about 8-12 minutes of instrument time).**
1. Flow on, purge until T and EC are flat (shared with the Sentinel or Clamp visit).
2. Path A (direct): N2, O2, Ar, CO2, CH4, 4He at about 1 reading per 10 s for 2-3 minutes.
3. Path B (getter plus 77 K trap): 4He, 20Ne, 22Ne for 2-3 minutes.
4. Air standard through the same membrane, 1 minute.
5. Output: excess He (cm3STP/g and as x ASW), excess air from Ne, N2/Ar, CO2/Ar, He/Ar, CH4, H2, a "flag score", and, for hot or gassy wells only, the gas geothermometers.
6. If the flag score is in the top 10-20% (or the model's EVSI says so), take two Cu tubes and the bottle set for the trailer.

**Deployment.** Rides in the Sentinel or Clamp truck. Two-person crew. Crew time added per site: **about 15-20 minutes** (setup 5, readings 8-12 in parallel with the profile and the option talk, tubes 5 if flagged). Field rate stays at about 8-15 Sentinel sites or 20-30 Clamp sites per crew-day (the cartridge is the slower step on Clamp days).

### 2b. "Valley Lab" (trailer, one per active basin cluster)

**Stage A, months 0-9: fixed garage lab in a valley town** (Winnemucca, Elko, Fallon, Delta UT, Burns OR). Crews drive samples in each evening. Same-night or next-morning results. No towing stress on a magnetic sector. This is most of the value at much less risk.

**Stage B, months 9-18: 8.5 x 24 ft enclosed gooseneck trailer**, moved every 2-6 weeks between basins, run from ranch shore power or a 15-20 kVA inverter generator.

| Part | Spec | Est. price (unverified) |
|---|---|---|
| Noble-gas mass spectrometer | Static-vacuum magnetic sector that resolves 3He+ from HD+ (needs M/dM about 600 or better). Options: refurbished MAP 215-50 or VG-era sector ($150-350k used); new Thermo Helix SFT or Nu Noblesse class ($700k-1.2M). v1 assumes a refurbished unit | $150-350k |
| Extraction and clean-up line | Cu-tube crusher and degassing manifold, two SAES getters, cryo-head charcoal trap (about 10-40 K, to separate He from Ne), air-pipette standard, a He standard (HESJ or a lab-made 1 Ra tank), all-metal pneumatic valves (about 20), ion pumps and turbo | $80-150k |
| Data system | Peak-hopping control, faraday plus multiplier, auto-run of 8-14 samples per night | $10-20k |
| MP-AES | Agilent 4210/4300 class, runs on a nitrogen generator from air (no argon deliveries): Na, K, Ca, Mg, Li, B, SiO2, Fe, Mn, As | $70-100k incl. N2 generator |
| Ion chromatograph | Cl, SO4, F, Br, NO3 for Cl-mixing and B/Cl (Metrohm or Thermo compact class) | $30-50k |
| Water isotopes (optional) | Laser analyser for d18O and dD (Picarro L2130-i class): oxygen shift, recharge elevation, mixing | $70-100k |
| Trailer shell | Insulated, HVAC to +/-1 C, vibration-isolated optical-table bench, air-ride suspension, UPS, battery-backed ion-pump supplies so the sector stays under vacuum on the road | $60-120k |
| Prep | Ultrapure water system, balance, pipettes, filtration, fume hood for acids | $15-30k |

**Total: about $450-900k** (Stage A about $350-650k, Stage B adds the shell and road-proofing).

**Throughput.** Noble gases: about 45-75 minutes per water sample incl. extraction and standard, so **8-14 per night** per sector with auto-run (judgement). MP-AES and IC: 40-80 samples per day. That matches the top 10-20% of a 2-crew day of 30-60 cartridge reads.

**Precision targets.** R/Ra +/-1-2% at about 1 Ra for samples above 10x ASW; He and Ne concentrations +/-1-2% (typical sector performance, from memory, unverified). Solute geothermometers: quartz T to about +/-5 C on undiluted water; real error is set by mixing, not by the MP-AES.

**Staff.** One noble-gas technician (night run) plus one geochemistry tech (day). About $220-300k per year loaded (unverified).

**Per-point cost (calc).** Run costs (standards, getters, consumables, power, fuel) about $20-40 per noble-gas point; labour about $40-80 per point at 10 per night over 150 nights. So **$60-120 marginal**. Add amortisation of a $600k lab over 3 years and about 1,500 points per year: plus about $130, so about **$190-250 fully loaded**. That is still below lab price, and it is same-night.

### 2c. Data path into the model
- Each reading enters THERMOS-B as a new per-source likelihood class **"He-cart"** with (excess He, Ne, N2/Ar, flag) and **"He-iso"** with (R/Ra, tritium status firm/provisional, deep-fluid fraction f with error).
- A small forward model per well: ASW(T, elevation, salinity) + excess air (Ne) + crustal 4He (age prior from Cl, Na/Ca, depth) + tritiogenic 3He (prior from depth, NO3) + deep fraction f with end-member He and R/Ra drawn from the Great Basin prior (Kennedy and van Soest field). Infer f and R_deep per well (as M22 proposed). Feed f and R_deep, not raw ratios.
- Sensitivity for He depends on the same latent mask class as T, 2 m, MT and chemistry (MODEL.md section 4). Helium's sensitivities by mask class are new parameters, fitted in the 20/40 calibration campaign.
- f is also back-projected up the head gradient (rank 6). Because He decays only by dilution, its along-flow decay length is longer than heat's. Fitting both gives the distance to source better than either alone.

## 3. How much it shrinks the ranked uncertainties

### Rank 1, detection gap (the main gain)
Monte Carlo (`P24_identifiability_mc.py`, 200,000 draws, priors are my judgement and unverified):
- Mask prevalence in high-lambda, low-P_det cells: Dirichlet(open 2, lid 3, swept 2, tongue 2).
- Temperature sensitivity means: open 0.8, lid 0.14, swept 0.2, tongue 0.67. Helium sensitivity means: open 0.8, lid 0.43, swept 0.67, tongue 0.62. Within-class failure correlation 0.3 (the detectors share plumbing).

| Detector set | Multiplier 1/P_det, median | 5-95% | Band ratio |
|---|---|---|---|
| Temperature only | x2.41 | x1.62 to x4.38 | 2.70 |
| Temperature + excess He | x1.42 | x1.21 to x1.89 | 1.57 |

- **The band on the detection correction shrinks about 1.7x, and the median correction drops about 40%.** Less of N then comes from extrapolating "systems we cannot see".
- The two-detector pattern is also data. A cell with T- and He+ is a direct count of lidded or swept systems. Over 300-800 designed visits this pins the lid and sweep shares of the mask class. The plain Monte Carlo above does not even include that gain.
- A "calibration" variant in the script that only redraws sensitivities around their prior draws shows no extra shrink. That variant is a prior-predictive check, not a real posterior update, so I do not count it.
- **Regional effect (judgement).** Applied to surveyed cells only and then spread by the Cox field, I expect the regional F5/F95 on N to narrow by an extra **about 20-35%** over a Sentinel-only campaign of the same visit count. That moves the buyer metric (F5/F95 below 4x per 100 visits) toward reach.

### Rank 2, permeability class (moderate gain)
- Mantle-tagged He (R/Ra above the local crustal line) is a direct "open path to depth" label (Banerjee et al. 2011). It does not give kg/s. Through a learned transfer with the Sentinel tidal T and specific capacity, I expect **about 10-20% less variance** on permeability class in cells with an R/Ra point (judgement).

### Rank 4, sensor reliability (necessary gain)
- Helium's s and q per mask class become measured numbers after the 20 blind / 40 cold campaign. Same-night R/Ra lets us redo a site the next day if a reading is odd, so the campaign finishes in one season rather than waiting on lab returns.
- **q for excess He alone is poor** (old crustal water fires it). My prior false-positive rate is about 0.25-0.35 in carbonate and deep-basin aquifers. R/Ra cuts it to about 0.05 (judgement). This is the main reason to build the trailer.

### Rank 5, temperature at 0.5-2 km (moderate gain)
- Un-mixing with f from He, Cl and B lets silica and cation geothermometers reach the deep end-member. On wells with f above about 1%, I expect the reservoir-T error to drop from about +/-30-40 C to about +/-15-25 C (judgement).

### Rank 6, upflow location (small to moderate gain)
- Joint fit of He and T decay along the flow line sharpens the source distance. Maybe +/-1-3 km to +/-0.7-2 km in instrumented basins (judgement), on top of P04.

### Rank 3, masking (small direct gain)
- He does not measure lid thickness. But T-low with He-high is the cleanest single signature of a lidded or swept system, so it labels mask class at the cell level.

## 4. Rights edge

- **On the spot.** The cartridge result is ready before the crew leaves. Option template: base $1-2/ac now, plus a pre-agreed step-up (for example to $5-10/ac, or a larger royalty share) that we may trigger within 30 days. The rancher sees we take his well seriously. We pay more only where the gas says so.
- **Same night, file next day.** Trailer R/Ra by morning means the adjacent state first-file and the leftover BLM noncompetitive filings ($1/ac/yr, R02) go in within 24-48 hours, not after a 6-12 week lab cycle during which a neighbour visit or a public auction notice could beat us.
- **Secrecy.** No sample, label or coordinate goes to an outside lab. University noble-gas labs are small, and the same few serve Zanskar, USGS and DOE teams (judgement). Keeping it in-house removes that leak.
- **Data moat.** A dense, dated, GPS-tied He/Ne/R/Ra layer from ordinary ranch wells does not exist in public (M22: only hundreds of He-isotope points outside known fields). After 2-3 seasons we would hold a few thousand points. Zanskar uses LBNL seismology and its own wells (Z files), not a He layer at this density (unverified that they have none).
- **Sales value.** A buyer (Ormat, Fervo) values "hot AND open" more than "hot". A mantle-He anomaly on a fault plus a warm well is a stronger farm-out package than temperature alone (H04).

## 5. Prior art

- **miniRUEDI** (Eawag, Brennwald et al. 2016, Environ. Sci. Technol. 50:13455, from memory; 2024 update in Geosci. Instrum. Method. Data Syst. 13:1, https://gi.copernicus.org/articles/13/1/2024/gi-13-1-2024.pdf, not read). Sold via Gasometrix (https://www.startup.ch/gasometrix, in H04). Total He, Ar, Kr, N2, O2, CO2, CH4. No 3He. Neon is hard on a plain quadrupole (from memory, unverified), which is why v1 adds the 77 K trap.
- **GE-MIMS** (Mächler, Brennwald and Kipfer 2012, Environ. Sci. Technol. 46:8288; from memory): the membrane-contactor gas equilibrium method we copy.
- **USGS mobile and portable He detectors** for uranium in the 1970s-80s (https://pubs.usgs.gov/publication/70012488 ; https://pubs.usgs.gov/publication/70042909 ; in H04). Total He only, soil gas, then dropped.
- **Lab 3He/4He in geothermal exploration:** Kennedy and van Soest (2005, 2007), the Hawaii blind-resource noble-gas test (https://gdr.openei.org/submissions/1410), the Snake River Plain well survey (M22). All lab-based, weeks of turnaround.
- **Field 3He/4He:** no routine field instrument resolves 3He today (H04). A trailer-mounted sector is unusual but not new physics; static-vacuum sectors have been moved between labs under ion-pump vacuum (judgement). I did not find, and could not search for, a mobile noble-gas lab in geothermal use (unverified).
- **Gas geothermometers:** Giggenbach (1980, 1991). **Solute geothermometers and mixing:** Fournier (1977, 1981), Fournier and Truesdell (1974), Giggenbach (1988). All from memory.

## 6. Costs per site and scale

| Item | Cost (unverified) |
|---|---|
| Cartridge reading added to a Sentinel or Clamp visit | $5-15 consumables plus about 15-20 crew-minutes (about $25-40) |
| Trailer R/Ra + solutes on the top 10-20% | $60-120 marginal, $190-250 loaded |
| Average added cost per site (20% sent to trailer) | about $45-90 per site |
| Season (2 crews, about 2,000 cartridge sites, about 300-400 trailer points) | about $0.15-0.25M operating, plus capex |
| Capex | 2-3 cartridges $60-120k; Valley Lab $450-900k |

Per km2: valley wells sit about 1 per 2-10 km2 in irrigated basins (judgement), so about **$5-40 per km2** for the added gas layer in surveyed basins.

## 7. Build plan and time

- **Weeks 0-4:** buy RGA, turbo, getter, contactor; bench test on tap water and an ASW standard.
- **Weeks 4-10:** add the 77 K trap and neon path; air and ASW calibrations; enclosure and battery.
- **Weeks 10-14:** first field test (below). Cartridge v1 done in about **10-14 weeks** with one instrument engineer and one geochemist.
- **Months 3-9:** Stage A garage lab: buy a refurbished sector, build the extraction line, bake and calibrate, cross-check 30 duplicates with a university lab. MP-AES and IC in parallel (off the shelf, about 4-8 weeks to running).
- **Months 9-18:** Stage B trailer, road-proofing, first moves.

## 8. Risks

1. Neon on a small quadrupole may be noisier than +/-3% even with the trap, which weakens the excess-air correction. Fallback: lean on Ar/Kr for excess air with a closed-system equilibration model.
2. Excess He from old crustal water may be common enough in carbonate aquifers that the cartridge flags too many wells before R/Ra (q about 0.3).
3. Truly sealed lids may stop He as well as heat, so helium's lid sensitivity may be nearer 0.2 than 0.43, cutting the rank 1 gain.
4. A magnetic sector in a towed trailer may lose calibration or vacuum on moves. Stage A (fixed garage lab) avoids this.
5. Tritium makes same-night R/Ra provisional on many shallow, young wells.
6. Gas geothermometers do not work in cold diluted wells. They must not be over-sold.
7. Staffing: noble-gas technicians are rare; hiring may set the timeline more than parts.
8. Prices for used sectors, cryocoolers and getters are unverified.

## 9. First test

**Where:** ranch and stock wells in the outflow of a known blind system (McGinness Hills or Dixie Valley range-front wells, Granite Springs if access allows) plus a matched cold control valley with similar aquifers.

**What:** 20 wells in the plume or near the fault, 20 control wells. Cartridge read at each. Two Cu tubes each, one to a university lab (Utah or LBNL) for 3He/4He, He and Ne.

**Pass:**
- Cartridge He within +/-5% and Ne within +/-10% of the lab values on duplicates.
- At least 50% of plume or fault wells show terrigenic He above 3 sigma of the control-valley distribution, including at least some wells with no temperature anomaly (the "cold but He-rich" case).
- Later, for Stage A: lab and garage R/Ra within 3% or 0.03 Ra on 30 duplicates.

**Kill:** fewer than 30% of plume wells exceed control by 2 sigma, or the controls fire as often as the plume wells (q above 0.4 before R/Ra).

**Cost:** about $35-50k (cartridge build plus 40 lab isotope runs at about $400-600 plus field time). About 2 field weeks.

## Sources

- Repo: `M22-gas-isotopes.md`, `../../../hardware/evidence/H04-soil-gas-geochem.md`, `P01`, `P04`, `P05`, `../MODEL.md`.
- https://escholarship.org/content/qt67p1z91d/qt67p1z91d.pdf (Kennedy and van Soest 2005; via M22)
- https://www.usgs.gov/publications/deep-permeable-fault-controlled-helium-transport-and-limited-mantle-flux-two (Banerjee et al. 2011; via M22)
- https://pubs.usgs.gov/of/1980/0612/report.pdf (Hinkle and Kilburn 1980; via M22)
- https://gdr.openei.org/submissions/1410 (Hawaii blind-resource noble gases; via M22)
- https://www.eawag.ch/en/info/portal/news/news-detail/portable-mass-spectrometer-allows-on-site-gas-analysis/ and https://www.startup.ch/gasometrix (miniRUEDI; via H04)
- https://gi.copernicus.org/articles/13/1/2024/gi-13-1-2024.pdf (Brennwald et al. 2024; fetch blocked, not read)
- https://pubs.usgs.gov/publication/70012488 ; https://pubs.usgs.gov/publication/70042909 (USGS mobile He; via H04)
- From memory, unverified: Brennwald et al. 2016 ES&T; Mächler et al. 2012 ES&T; Weiss 1971 He/Ne solubility; Giggenbach 1980, 1988, 1991; Fournier 1977, 1981; Fournier and Truesdell 1974; 3H/3He constants.
