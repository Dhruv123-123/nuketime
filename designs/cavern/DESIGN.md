# CAVERN: two lined rock caverns of pressurised hot water as a daily peaking store for a light-water reactor

A complete soft design, sized and evaluated with a steam-table model, that turns a
1,100 MWe pressurised-water reactor's midday output, which is nearly worthless on a
solar-heavy grid, into 315 MW of extra output for five evening hours, every day, at a
74.6 % electric round trip, using two lined rock caverns instead of steel vessels.

Files: `model.py` (thermodynamics, rock, sizing, economics), `plots.py`, `runs/design.json`,
`figures/`.

---

## 1. What it yields

| Quantity | Value |
|---|---|
| Extra output at the evening peak | 315 MW for 5 h, 1,574 MWh per day |
| Output given up at midday | 352 MW for 6 h, 2,111 MWh per day |
| Electric round trip | 74.6 % |
| Reactor duty | 100 % all day, no manoeuvring |
| Cavern volumes | 70,000 m³ hot, 63,000 m³ warm (30 m diameter, about 100 m tall) |
| Heat lost to rock | under 0.2 % of throughput over 30 years |
| Capex, retrofit with a new peaking turbine | about $420 M ($268 per kWh delivered per day, $1,340 per kW of peak) |
| Capex, new build with an oversized main turbine | about $320 M |
| Revenue on a stylised duck curve (midday $15, peak $160 per MWh) | $73 M per year, 5.8-year payback (4.4 years for new build) |

Compared with a 4-hour lithium battery at $1,300 to 1,800 per kW: similar capital per kW
of peak, a longer discharge, no degradation, a 50-year civil asset, and the reactor
runs flat out all day. Compared with a gas peaker: no fuel, no emissions, and the
"fuel" is nuclear electricity bought from itself at the midday price.

## 2. Lineage and what is new

This is not a new idea at the level of the concept. Peter Margen filed a Swedish patent in
1958 for a large accumulator in an underground insulated rock cavern connected in
parallel with a nuclear plant's steam generator, and his 1979 to 1985 US patents
(4,174,009; 4,399,656; 4,526,005) describe long-period hot-water accumulators in unlined
or foil-lined caverns and submerged tanks, discharged by preheating feedwater over weeks
to months. Sweden built a 15,000 m³ unlined test cavern at Avesta in the early 1980s at
115 °C and the 100,000 m³ Lyckebo solar cavern at 90 °C. Steel Ruths accumulators have
served peaking turbines since the 1920s (Charlottenburg). Idaho National Laboratory
studied steam accumulators for SMRs and rejected them on volume. Nothing at nuclear steam
conditions has ever been built underground.

What this design adds:

1. **Lined rock cavern method.** The rock mass carries the pressure and a thin steel liner
   only seals, as in the Skallen lined rock cavern for natural gas (Sweden, 2004, 20 MPa,
   115 m deep). Margen assumed unlined rock or water-balanced foil, which limits the
   temperature to about 115 °C. Lining makes 235 °C and 3.1 MPa possible, which is what
   makes flash discharge to a turbine worthwhile.
2. **Two caverns at constant temperature.** Hot and warm water are kept apart, like the
   two tanks of a molten-salt plant. Each liner sees a steady temperature and a steady
   pressure for its whole life; only the water level moves. A single Ruths accumulator
   cycles both, which is what makes large hot liners fail.
3. **Daily cycle, staged both ways.** Charging uses six extraction points of the existing
   turbine as a cascade of closed heaters, so each kilojoule is bought with the cheapest
   steam that can do the job. Discharge is a four-stage flash into a dedicated wet-steam
   peaking turbine. Staging is worth 20 points of round trip against a single stage
   (54.4 % with one stage each, 74.6 % with six and four).
4. **Evaluated sizing** with steam tables, rock conduction, uplift and heave checks and an
   economic scan, none of which exist for the cavern variant in the public record.

## 3. Design

### 3.1 Plant and duty

- Host: a 3,400 MWth, 1,156 MWe PWR with 6.9 MPa saturated main steam, a moisture
  separator at 1.1 MPa and live-steam reheat to 250 °C. The model's main cycle gives
  838 kJ of net work per kg of throttle steam.
- Charge: 09:00 to 15:00, 30 % of thermal power (1,020 MWth) diverted as extraction
  steam. Output falls by 352 MW. Reactor stays at 100 %.
- Discharge: 17:00 to 22:00, 315 MW from the peaking turbine on top of the plant's normal
  1,156 MW.

### 3.2 Caverns

- Two vertical cylindrical lined rock caverns, 30 m diameter, crowns at 150 m depth,
  60 m apart, in competent crystalline rock with a drainage gallery, as in gas storage
  practice. Hot cavern 70,000 m³ (98 m tall) at 235 °C and 3.1 MPa; warm cavern
  63,000 m³ (89 m tall) at 160 °C and 0.62 MPa. Each has a steam cushion at its own
  saturation pressure, so no gas blanket is needed.
- Wall, inside to rock: 15 mm carbon-steel liner, bitumen sliding layer, 1.5 m refractory
  (calcium-aluminate) concrete, 1 m insulating castable (k = 0.15 W/m·K, compressive
  strength above 10 MPa), drained bedrock.
- Uplift: the rigid-cone check gives a safety factor of 23 for the hot cavern at 3.1 MPa
  with the crown at 150 m; the criterion that set Skallen's depth is met with a wide
  margin, so the caverns could be shallower.
- Water chemistry: demineralised, deoxygenated, alkaline, on the secondary side of the
  plant; it never touches the primary circuit.

### 3.3 Charge train

Warm water is pumped from the warm cavern through six closed feed heaters in series and
into the hot cavern. Each heater takes steam from the main turbine's expansion line at the
lowest pressure that can heat its stage with a 5 K pinch:

| Stage outlet, °C | 172 | 185 | 198 | 210 | 222 | 235 |
|---|---|---|---|---|---|---|
| Extraction pressure, MPa | 0.95 | 1.26 | 1.64 | 2.11 | 2.67 | 3.35 |
| Steam per kg of store water, kg | 0.025 | 0.032 | 0.033 | 0.034 | 0.035 | 0.036 |

Drains cascade back to the plant's feed train. The make-up water that replaces what is
flashed off during discharge (16.0 % of the hot mass) is heated from 33 °C to 160 °C at
charge time by the same method, so no extraction steam is spent during the peak. Charging
costs 146 kJ of electricity per kg of hot water made, make-up included.

### 3.4 Discharge

Hot water flashes in four vessels at 2.16, 1.48, 0.97 and 0.62 MPa (216, 198, 179 and
160 °C). The steam from each enters the peaking turbine at that pressure; the residual
water at 160 °C goes to the warm cavern. Per kg of hot water, 0.160 kg of steam yields
109 kJ of electricity in a wet-steam turbine with 85 % stage efficiency, a moisture
separator at 1 MPa and a 5 kPa condenser. Round trip: 109 / 146 = 74.6 %.

### 3.5 Peaking turbine

A 315 MW saturated-steam turbine with four admission pressures, its own condenser and
cooling, and a generator on the plant's switchyard. For a new plant the same steam can go
to an oversized main turbine instead, at about $250 per kW of added capacity instead of
$450.

## 4. Model

`model.py`, IAPWS-97 steam tables throughout.

- Main cycle: HP expansion (85 % isentropic) to 1.1 MPa, moisture separation, live-steam
  reheat to 250 °C (its steam consumption is charged against the cycle self-consistently),
  LP expansion (88 %) to 5 kPa. The work that a kilogram of steam taken from the line at
  any pressure would still have produced is what charging forgoes.
- Charge train: cascade of closed heaters as above; make-up heating included.
- Discharge: multi-stage flash with mass and energy balance per stage; peaking turbine
  work per admission pressure.
- Rock: transient conduction from a sphere of equal volume held at constant temperature,
  with an insulating layer solved against the rock's transient conductance; heat loss,
  wall temperature, temperature profile, free-expansion heave along the axis, rigid-cone
  uplift.
- Economics: component costs (excavation $120/m³, 1.5 m concrete at $800/m³, 15 mm liner
  at $12/kg installed, insulation $400/m², $40 M for shafts, drainage and access, peaking
  turbine $450/kW, balance of plant 25 %, contingency 30 %) and a stylised price day.
  These are order-of-magnitude figures, not quotes.

## 5. Results

Figures: `fig1_dispatch.png` (one day), `fig2_roundtrip.png` (round trip against cavern
temperatures and against stage counts), `fig3_economics.png` (payback against discharge
duration and cases), `fig4_rock.png` (rock wall temperature over decades and the profile
into the rock), `schematic.svg`.

- Round trip rises as the hot cavern gets cooler and the warm cavern gets hotter, because
  less exergy is destroyed heating water with steam and flashing it back. It falls from
  78 % at 200/180 °C to 67 % at 280/120 °C. Volume moves the other way. The design point
  235/160 °C balances round trip, cavern size and liner conditions.
- Economics favour a longer discharge (the peaking turbine is the biggest cost) and a
  hotter store (smaller caverns). Payback at 5 h ranges from 5.1 years (280 °C) to
  6.2 years (220 °C). The 235 °C point costs a year of payback for a liner that stays
  below the temperatures at which ordinary concrete degrades.
- Rock: with 1 m of insulating castable the rock wall reaches 76 °C after a year and
  119 °C after 30 years; the warm zone extends about 60 m from the wall after 30 years.
  Surface heave above the hot cavern after 30 years is 3.8 cm (free-expansion upper
  bound). Heat lost to rock is 0.69 MW in year one falling to 0.30 MW, 102 GWh over
  30 years against 60,600 GWh of throughput.
- Price sensitivity: at a $100 peak the payback is 10 years; at $200, 4.5 years; with
  negative midday prices (−$20), 4.3 years.

## 6. Failure modes and limits

| Item | Assessment |
|---|---|
| Liner leak | Water enters the drained rock zone and the drainage gallery; detected by flow; cavern taken out of service, plant unaffected |
| Concrete at 235 °C | Calcium-aluminate refractory concrete is rated far above this; ordinary Portland concrete would not be used |
| Liner thermal fatigue | None by design: temperature and pressure are constant; level changes only |
| Rock thermal stress | 34 MPa free-expansion estimate at a 119 °C wall, within the strength of sound granite; without insulation it would be 71 MPa, which is why the insulating layer is there |
| Groundwater | Drained rock zone as in gas LRC practice; site in low-permeability rock |
| Steam cushion collapse on fast withdrawal | Withdrawal rate limited by the flash vessels; cushion volume 10 % |
| Water carry-over into the peaking turbine | Four flash vessels with separators; standard wet-steam turbine practice |
| Radioactivity | Secondary-side water only |

What it does not do: it does not raise the plant's thermal efficiency, and the 25 % of
energy lost per cycle is real. It does not help a grid with a flat price. It needs
competent rock within about 200 m of the surface.

## 7. Construction

Lined rock cavern construction is an established method: Skallen (40,000 m³, 20 MPa)
took about three years. Two 70,000 m³ caverns are within the range of civil caverns built
for hydro plants. The peaking turbine, flash vessels and heater train are conventional
power-plant equipment. Nothing needs a first-of-a-kind material; the one item to qualify
is the liner and concrete system at 235 °C and 3.1 MPa, which can be tested at small scale
in a shaft before the caverns are excavated.

## 8. Open questions

1. Liner and refractory-concrete behaviour at 235 °C over decades, including the sliding
   layer.
2. Whether the rock temperature ceiling should be lower than 119 °C at a wet site.
3. Real price series rather than a stylised day; capacity-market revenue is not counted.
4. Whether part of the store should serve as a reactor-trip ride-through supply for a
   co-located load, which it can do at reduced power for a day.
5. Detailed turbine design for four admission pressures versus two admissions with
   throttling.

## 9. Reproducing the results

```
pip install numpy scipy matplotlib iapws
python3 model.py      # cycle validation, round-trip table, design scan, writes runs/design.json
python3 plots.py      # figures
```
