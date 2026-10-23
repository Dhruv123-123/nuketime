# M34: Depth to economic heat, drilling cost, binary plant economics, and the dollar target a rights bank should predict

Slice M34, model track. Date: 23 Oct 2026. This builds on `../../evidence/L21-cost-learning.md` (Lowry 2017 well-cost curves, Fervo drilling learning, ATB 2024 capex), `../../evidence/L13-exploration-risk.md` (IFC and Wall-Dobson success rates), `../../evidence/B03-ppa-prices.md` (PPA above $100/MWh), `../../evidence/B07-royalty-model.md` (royalty comps, $5/MWh Centaurus override, about $0.1M/MW for confirmed-no-PPA), `M16-temperature-at-depth.md` (column model), `M17-value-of-information.md` (VOI frame) and `M33-resource-size-models.md` (lognormal size prior, power density). It does not repeat them. What is new: (1) a single physics-plus-cost chain from temperature, depth and flow to cost of power, (2) the "minimum economic temperature by depth" curve, (3) the gap between what a confirmed resource is worth to a builder and what it sells for, and (4) a precise definition of the target variable the model should predict.

**Search notes.** The shared web-search budget for this run was used up before this slice started. Both searches I tried were refused, and no fetches ran. Everything below comes from prior repo files (cited by file), primary sources I know by name (marked "from memory", with the best URL I know), and my own arithmetic in `/home/user/nuketime/research/geothermal/model/evidence/M34_econ.py` (marked "calc"). Inputs in that script that are not from a fetched source are marked (unverified) and should be replaced with GETEM and ATB 2024 numbers before anyone relies on them.

## Bottom line

A rights bank should not ask its model "is there heat here?". It should ask **"what is the risked dollar value of holding the right to this acre?"** That value is built from three physical numbers and one business number. The physical numbers are **temperature at depth, depth, and flow per well**. The business number is **how many dollars per MW the bank can capture** (a sale at confirmation, a carry, or a $/MWh override). My cost chain (calc, using Lowry 2017 well costs, ATB-style plant costs and a 30% ITC) gives a clear rule. At $100/MWh, a binary plant pays at about **110 °C at 1 km, 120 °C at 1.5 km, 130 °C at 2 km, 150 °C at 3 km and 180 °C at 4 km**, if each producer flows about 60 kg/s. So the economic target is not a fixed "150 °C" line. It is a **sloped surface in temperature-depth space**, and shallow-but-moderate heat beats deep-but-hot heat. Flow matters as much as temperature: at 150 °C and 1.5 km, cost of power goes from about $118/MWh at 20 kg/s to $73/MWh at 60 kg/s (calc). Conductive background gradients in the Great Basin (30-40 °C/km) put 150 °C at 3.4-4.5 km, which is uneconomic for hydrothermal. Only a convective upflow, which puts 150 °C above about 2 km, makes money. That is why blind upflows are the asset. The second result is a big gap. A 150 °C resource at 1-2 km is worth about **$1.8-3.1M per MW** of surplus to a builder at $100/MWh (calc), but a confirmed resource without a PPA sells for about **$0.1M/MW** (B07). The 20-30x gap is the bank's alpha. It is captured by carrying assets to PPA and interconnection, or by keeping an override (about $0.4M/MW PV at $5/MWh). Risked value per acre (calc) is about **$4/acre for an average cell (0.5% prior), $40/acre for a top-decile cell (5%), and $150/acre after a positive probe (20%)**, against a cost of $1-2/acre. So the target variable should be **risked net present value per acre (RNPV/acre)**. The model predicts calibrated distributions of T(z) and flow class. A fixed, auditable economics layer turns those into dollars. The sensor that most cuts the uncertainty on this target is one that measures **flow capacity (permeability)** and **temperature at depth** together. Neither is in public data for blind cells.

## Findings

### F1. The cost chain: temperature, depth, flow -> MW per well -> $/kW -> $/MWh
- **Power per kg/s rises steeply with temperature.** The usable work in hot water (exergy) goes up much faster than temperature. A binary plant turns about 30-45% of that exergy into power (DiPippo, *Geothermal Power Plants*, 4th ed. 2016, from memory; the 30-45% band is (unverified)). My calc gives net power after 15% parasitic load of about **19 kW per kg/s at 120 °C, 35 at 150 °C, 52 at 175 °C and 73 at 200 °C**. So one 60 kg/s producer gives about 1.2 MW at 120 °C and 4.4 MW at 200 °C. A 200 °C well is worth about 3.7 producers at 120 °C.
- **Cross-check.** Fervo's Cape producer gave 107 kg/s and "more than 10 MW gross" at about 190 °C (repo L21/L08), about 95 kW gross per kg/s. My net 65-70 kW/(kg/s) at 190 °C after parasitics fits. The Meikle mine reference in the repo (166 °C, about 1,750 gpm wells, 20 MW air-cooled binary) also fits the shape (D06/A05).
- **Well cost by depth.** Lowry et al. 2017 (Sandia SAND2017-9977, https://www.osti.gov/servlets/purl/1394062) give the baseline 5 km large-diameter well at **$16.4M**. Materials are 78% of cost, and doubling drilling speed saves only 10-14%. Shallower points in my curve ($1.2M at 0.5 km, $1.8M at 1 km, $3.5M at 2 km, $6M at 3 km) follow the GETEM-style quadratic shape but are (unverified). The NREL 2025 drilling cost curve update (Akindipe and Witter, from memory, unverified) is the right replacement. Geothermal wells cost 2-5x oil and gas wells at the same depth (Augustine et al. 2006, via L21).
- **Field capex.** At 150 °C, 1.5 km and 60 kg/s, with 70% well success, 0.6 injectors per producer, $0.3M/MW exploration and $300/kW for the line, the calc gives **about $6,900/kW**. ATB 2024 gives **$9,483/kW** for binary hydrothermal on average (https://atb.nrel.gov/electricity/2024/geothermal, via L21). ATB 2022 ranged from **about $4,156/kW at ≥200 °C to about $17,060/kW below 135 °C** (via L21, bin mapping unverified). My number sits inside that band.
- **Cost of power.** Using an 8% / 30-year capital charge (8.9%), $160/kW-yr O&M (Fervo 424B4), 92% capacity factor and a 30% ITC (48E stays at 100% for projects that start building by end-2033, B03), the calc table is:

| Temp \ depth | 0.5 km | 1 km | 1.5 km | 2 km | 3 km | 4 km |
|---|---|---|---|---|---|---|
| 120 °C | $77 | $86 | $99 | $112 | $150 | $211 |
| 135 °C | $68 | $75 | $84 | $94 | $122 | $166 |
| 150 °C | $61 | $66 | $73 | $80 | $101 | $135 |
| 165 °C | $56 | $60 | $66 | $71 | $88 | $114 |
| 180 °C | $53 | $56 | $60 | $65 | $78 | $99 |
| 200 °C | $49 | $52 | $55 | $59 | $69 | $85 |

(calc, $/MWh, 60 kg/s per producer. Absolute levels carry about ±30%; the slopes are the useful part.)

### F2. The minimum economic temperature is a sloped line, not a number
- At a **$100/MWh** price (new Ormat and Fervo PPAs clear above $100, B03), the calc minimum temperature is about **100 °C at 0.5 km, 109 °C at 1 km, 120 °C at 1.5 km, 130 °C at 2 km, 152 °C at 3 km and 179 °C at 4 km**.
- At **$80/MWh** (a downside case if EGS pushes prices back, L21), the line moves up about 20-30 °C: 128 °C at 1 km, 151 °C at 2 km, 177 °C at 3 km.
- Each extra km of depth needs roughly **+10 °C at 1-2 km and +25-30 °C at 3-4 km** to break even, because well cost rises faster than linearly with depth.
- **Meaning for the model:** a cell with 130 °C at 1 km is worth more than a cell with 170 °C at 3.5 km. A map of "temperature at 3 km" (SMU, Stanford, USGS) ranks them the wrong way round. The model must predict the whole column T(z) from 0 to 3 km, not one depth slice.

### F3. Only convection makes Great Basin heat economic
- Depth to 150 °C under a conductive gradient (surface 15 °C): **4.5 km at 30 °C/km, 3.4 km at 40, 2.25 km at 60, 1.7 km at 80, 1.1 km at 120 °C/km** (calc).
- Great Basin background is about 30-40 °C/km (SMU and USGS maps, M16). That puts 150 °C at 3.4-4.5 km, where the calc cost is $120-180/MWh. Not economic for hydrothermal.
- Zanskar's blind finds sit at about **137 °C at 2,500 ft (0.76 km) at Pumpernickel and 121 °C at 2,668 ft (0.81 km) at Big Blind** (Z02). Both lie well inside the economic zone on the F1 table. That is what a convective upflow does: it lifts the 120-150 °C isotherm from 3-4 km to under 1 km.
- **Meaning for the model:** the target is "shallow economic heat from upflow". A national conductive map is a prior on the background. The thing we sell is the deviation from it (M16).

### F4. Flow (permeability) is as big a lever as temperature, and it is the one nobody can map
- At 150 °C and 1.5 km, the calc cost of power is **$118/MWh at 20 kg/s, $84 at 40, $73 at 60, $66 at 90 and $62 at 120 kg/s**.
- Going from 20 to 60 kg/s saves as much as going from 120 °C to 150 °C.
- Sanyal (2004-2005 Stanford/WGC papers on the cost of geothermal power, from memory) found well productivity to be the single largest driver of geothermal power cost. The same message holds here (unverified quote).
- Wall and Dobson (2016, via L13) found that exploration led to full-size development wells **less than one-third of the time**. Most failures in hot ground are flow failures, not heat failures (unverified share).
- **Meaning for the model:** the target must include a flow term. A heat-only probability overstates value. Predict a flow class (for example under 20, 20-60, over 60 kg/s per well) with its own probability.

### F5. The builder-to-seller gap: about $2-3M/MW of surplus, about $0.1M/MW of price
- Builder surplus at $100/MWh, 30 years, 8% (calc): **$3.1M/MW at 150 °C and 1 km, $1.8M/MW at 150 °C and 2 km, $2.3M/MW at 135 °C and 1 km, $3.0M/MW at 175 °C and 2 km**, and zero at 150 °C and 3 km.
- Market prices for the same thing: confirmed resource without PPA about **$0.1M/MW** (USG 2017 review, B07). Operating plants trade at **$4.3-5.6M/MW**, about replacement cost (B07). Override precedent: **$5/MWh (Centaurus on Fervo Cape)**, about **$0.4M/MW PV** (B07).
- So the bank captures 3-20% of the builder surplus, depending on how far it carries the asset. The step up comes at **PPA plus interconnection**, not at the flow test (B07, MEMO).
- **Meaning for the model:** "capture dollars per MW" is not a constant. It depends on the stage the bank reaches, so the economics layer must take a stage argument.

### F6. Risked value per acre: the arithmetic that sets the bank's buy rule
- Formula (calc): **RNPV/acre = P(system in cell) x P(acre in productive footprint | system) x power density (MW/km²) x capture ($/MW) x P(someone builds) x discount(delay) / 247 acres per km²** - holding costs.
- With 6 MW/km² (150 °C trend, M33), footprint share 0.5, override capture $0.4M/MW, P(build) 0.4 and 8 years at 12%:
  - average cell, P = 0.5%: **about $4/acre**;
  - good cell, P = 2%: **about $16/acre**;
  - top-decile fault cell, P = 5%: **about $39/acre**;
  - after a positive probe, P = 20%: **about $157/acre**.
- A sale at confirmation ($0.1M/MW, 4 years, P(build) 1) gives almost the same numbers. So the two exit routes are worth about the same today, and the override is the one that grows with price.
- Cost to hold: $1-2/acre/yr (ranch heat, leftover BLM) plus BLM's diligence spend (about $40/acre in the repo's reading, B07). **Even an average cell roughly pays for its lease. A top-decile cell is 20-40x its cost.** The buy rule is simple: lock anything with RNPV/acre above about 3x the 10-year holding cost, then spend sensor money where VOI (M17) is highest.
- Note the size tail (M33): a few fields carry the book. RNPV/acre should use the mean of the lognormal size, not the median, because the bank owns the whole portfolio.

### F7. Taxes, royalties and price are second-order but not zero
- Federal royalty on BLM leases is **1.75% of gross proceeds for the first 10 years, then 3.5%** (43 CFR 3211.17, https://www.law.cornell.edu/cfr/text/43/3211.17). Ormat reports 1.0-2.5% in early years (B07). This adds about $2-4/MWh to the builder's cost.
- Private ranch royalty is typically **2-5%** (Ormat 10-K, via B07). On $100/MWh that is $2-5/MWh, or about **$0.15-0.4M/MW PV** to the bank if it holds the fee right directly. That is as big as a negotiated override.
- Losing the 30% ITC adds about $20-30/MWh at 150 °C and 1.5 km (calc). That moves the economic line up about 15-20 °C at every depth.

## Datasets

| Dataset | Access | Coverage | Value for blind detection |
|---|---|---|---|
| GETEM (DOE Geothermal Electricity Technology Evaluation Model) | Free, https://www.energy.gov/eere/geothermal/geothermal-electricity-technology-evaluation-model | US, binary and flash | Official cost and power curves to replace my calc inputs |
| NREL ATB 2024 geothermal | Free, https://atb.nrel.gov/electricity/2024/geothermal | US, by resource class | Capex by temperature bin, learning rates, CF |
| Lowry et al. 2017 well-cost curves (SAND2017-9977) | Free, https://www.osti.gov/servlets/purl/1394062 | Generic well designs to 7 km | Well cost vs depth |
| NREL 2025 drilling cost curves update (Akindipe and Witter) | Free NREL report (from memory, unverified) | Generic, updated with recent wells | Newer, lower well costs |
| EIA-860 and EIA-923 | Free, https://www.eia.gov/electricity/data/eia860/ and /eia923/ | Every US plant, monthly MWh | Real capacity factors, MW per field, size labels |
| ONRR geothermal production and royalty data | Free, https://revenuedata.doi.gov/ | Federal leases | Real $ per lease, a dollar label for producing federal parcels |
| Nevada Division of Minerals geothermal well files | Free after 5-year confidentiality (D03, D05) | 938 NV wells | Depth, temperature and flow per well, the flow-class label |
| SMU / Stanford InterPIGNN / USGS Great Basin temperature models | Free (M16) | US | Conductive background T(z) prior |
| HIFLD transmission lines and substations | Free, https://hifld-geoplatform.hub.arcgis.com/ | US | Line cost and P(build) term |
| BLM MLRS lease records | Free, https://mlrs.blm.gov/ | Federal land | Holding cost and lease status per acre |

## What dominates uncertainty about blind resources, per this slice

1. **Flow per well (permeability).** It swings cost of power by about 2x (20 vs 60 kg/s). No public layer measures it in a blind cell. INGENIOUS fault layers are a weak proxy.
2. **Temperature at 0.5-2 km, not at 3 km.** The economic line slopes about 10 °C per km at shallow depth, so a ±20 °C error is a ±1.5-2 km error in where the money is.
3. **Capture per MW.** It ranges from $0.1M/MW (confirmed, no PPA) to $0.4M/MW (override) to several $M/MW (carried to PPA). This depends on business execution, not geology, but it scales every acre equally.
4. **Well cost below 1 km.** The shallow end of the cost curve has the least public data and matters most for blind upflows.
5. **Probability someone builds (transmission, PPA queue).** It is a multiplier of 0.2-0.8 (unverified) and is independent of the rock.
6. **Policy (ITC).** Moves the economic line by 15-20 °C.

## What a sensor could fill

- **Flow capacity before a full well.** A drop probe that runs a short pump or slug test in a ranch well and logs pressure recovery gives transmissivity of the shallow aquifer. A temperature-and-pressure tool in a gradient hole can run a small injection test. Even a crude 3-class flow label per cell is new data nobody has.
- **The shape of T(z) in the top 0.5-1 km.** Dense, high-precision profiles (0.01 °C) in existing wells show convective curvature (Bredehoeft-Papadopulos) and let the column model push the curve down to 1-2 km with an error bar (M16).
- **Reservoir temperature from fluid chemistry.** A sealed sample bottle for silica and Na-K-Ca geothermometers puts a cap on the deep temperature (M33). This is the cheapest way to tell 130 °C from 180 °C before drilling.
- **Rock thermal conductivity.** A needle probe on cuttings or core turns gradient into heat flow and cuts the extrapolation error (M16).
- **Upflow area.** 2 m probe grids and E-field MT outline the footprint, which sets MW per system and the footprint share term.
- **Ranking for this slice:** the most valuable new sensor is a **combined T-P logger plus slug or pump-test module on the ranch-well drop probe**. It adds the flow term to the prior pick at small extra cost. Flow is the biggest unmeasured term in the dollar target.

## Implications for a better model

1. **Define the target as RNPV per acre**, with the parts kept separate so each can be checked:
   RNPV/acre = Σ over depth bins z ≤ 3 km and flow classes f of P(T(z) ≥ T_min(z, f, price) and flow = f) x E[MW/km² | T, f] x capture(stage) x P(build) x discount / 247 - holding cost.
2. **Predict physics, then apply economics as a fixed layer.** The ML model should output calibrated joint distributions of T at 0.5, 1, 1.5, 2 and 3 km and a flow class. A deterministic GETEM-based layer converts them to dollars. Do not train ML on dollars: there are too few dollar labels, and the economics change with price and policy. This also lets the bank re-price the whole map in seconds when PPA prices or the ITC change.
3. **Report "probability of economic heat" (PEH), not "probability of heat".** PEH = P(the T(z) curve crosses the sloped T_min line above 3 km with flow ≥ 40 kg/s). This is the honest label for a well outcome too. Old wells should be re-labelled by where their measured T(z) and flow sit against the line, not by a fixed 150 °C cut.
4. **Make price and capture stage inputs.** Run the map at $80, $100 and $115/MWh, and at sale, carry and override capture. The spread is part of the uncertainty a buyer sees.
5. **Use the mean of the size distribution for portfolio value, and P(MW ≥ 20) for go/no-go.** The "too small" line (about 10-20 MW, M33) is an economic cut, so it belongs in the economics layer.
6. **Add flow labels from public well files.** Nevada geothermal well files rolling off confidentiality (D03, D05) carry flow and productivity data. They give the first training set for the flow term.
7. **Rank sensor spending by VOI on RNPV/acre (M17), with flow as a first-class output.** A sensor that resolves flow class in a top-decile cell moves RNPV/acre more than one that sharpens temperature by 10 °C.
