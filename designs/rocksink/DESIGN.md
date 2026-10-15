# ROCKSINK: bedrock as the passive ultimate heat sink for a shaft-sited SMR

A complete soft design, sized and evaluated with a first-principles model, for rejecting
the decay heat of a 250 MWth integral pressurised-water SMR module into the bedrock around
its own shaft, through an array of sealed gravity thermosyphons, with no pool, no cooling
tower, no valves, no pumps, no power and no surface structure. The design gives an
unlimited grace period in every case run, including poor rock.

Files: `model.py` (physics), `final.py` (base case), `sweep.py` (variants), `field.py` (rock
temperature field), `plots.py` (figures), `runs/` (results as JSON and npz), `figures/`.

---

## 1. The idea in one paragraph

Every passive decay-heat system today ends in one of three sinks: a pool of water that
boils away (NuScale, BWRX-300 isolation condensers, AP1000's tank), an air chimney (RVACS on
sodium reactors, RCCS on gas reactors), or the containment shell radiating to air. Pools give
3 to 30 days and need make-up water; chimneys and shells are large surface structures that
are exposed to aircraft, tornado missiles and attack. Bedrock has effectively unlimited
heat capacity, sits under every plant, and is protected by geometry. The obstacle has been
heat transport: rock conducts poorly, so a reactor cannot simply be buried in it, and heat
cannot be moved downward passively. ROCKSINK solves both at once. The module sits at the
bottom of a 100 m shaft, so the rock beside the shaft is *above* the reactor and gravity
thermosyphons can carry heat into it. A bundle of 128 sealed thermosyphons fans out from a
ring drift around the shaft into 7.3 km of grouted boreholes, turning the low conductivity
of rock into a non-problem by spreading the heat over a large surface. A closed water jacket
around the steel containment collects the module's decay heat and delivers it to the
thermosyphon evaporators as steam. A nitrogen gas charge in each thermosyphon makes it a
thermal switch that is off in normal operation and opens by itself when the jacket warms.

## 2. Novelty and prior art

Searched on 2026-09-28 (patent full text, journals, vendor documents). Closest prior art:

| Prior art | What it is | How ROCKSINK differs |
|---|---|---|
| GE-Hitachi patent US 11,482,345 (2022), "geothermal passive cooling" | For an underground PRISM sodium reactor, a single-phase natural-circulation coolant loop buried 1 to 20 ft in soil, with fins and a damper, for up to 20 MW of decay heat | ROCKSINK is for a light-water module, uses 128 independent sealed two-phase thermosyphons rather than one loop, condenses in deep grouted upholes in bedrock rather than a shallow soil conduit, and switches itself with a gas charge instead of a damper |
| Deep Fission "Gravity Reactor" white papers (NRC ML24172A286, ML26112A159) and patent US 12,469,612 | A 15 MWe PWR at the bottom of a 1 mile borehole; decay heat conducts from the borehole water through the casing into the rock, and a heat exchanger in a second borehole receives heat through the rock | Deep Fission uses the rock directly next to the reactor, which limits it to a small core in a very deep hole. ROCKSINK spreads the heat over thousands of metres of borehole away from the module so a 250 MWth module in a 100 m shaft works |
| Two-phase thermosyphon PRHR concepts (e.g. Applied Thermal Engineering 2024, KAERI mercury thermosyphon SFR) | Thermosyphons carrying decay heat to a pool or to air | Same component, different sink: none use bedrock |
| Thermal-energy-storage decay-heat sinks (patent on LiCl phase-change blocks) | A manufactured store absorbs decay heat | ROCKSINK uses the site itself as the store, at zero material cost and without a temperature limit set by a phase-change material |
| Permafrost thermosyphons (124,000 units on the Trans-Alaska Pipeline since 1977) | Sealed gravity thermosyphons moving heat *out* of the ground into winter air | Same device class and the source of the reliability record; ROCKSINK runs them in the opposite direction, ground as sink |
| Borehole thermal energy storage (Drake Landing and others) | Seasonal storage of solar heat in a borehole field with pumped water | Same conduction physics and design method (finite line source superposition); ROCKSINK is pumpless, two-phase and transient |

No source found combines: a shaft-sited LWR module, a closed containment jacket as steam
generator, a torus manifold in a ring drift, sealed gas-loaded thermosyphons, and fanned
upholes in bedrock as the ultimate heat sink. Nobody has implemented any ground-sink decay
heat system at all; the GE patent and Deep Fission are paper designs. The claim made here is
novelty of the assembly and of the evaluated sizing, not of any component.

## 3. Design description

### 3.1 Module and shaft

- Reactor: a 250 MWth integral PWR module in a 4.6 m OD x 23 m steel containment vessel
  (the envelope of a NuScale-class module). The module's internals, emergency core cooling
  valves and decay-heat-removal steam-generator loops are unchanged; the only difference
  seen by the module is that its containment sits in a water jacket instead of a pool.
- Shaft: 10 m internal diameter, 100 m deep, raise-bored or conventionally sunk in
  competent rock, concrete lined. Containment bottom at 98 m depth, top at 75 m.
- Ring drift: a 3 m x 3 m tunnel at 73 to 76 m depth on a 15 m radius around the shaft
  axis (94 m long), leaving a 7 m rock pillar between shaft and drift. The drift carries
  the steam torus and the thermosyphon collars.

### 3.2 Containment jacket

- A closed steel vessel forming a 0.3 m water annulus around the containment, with a
  steam drum ring at the top. Water inventory 120 t; thermally coupled steel about 400 t.
  Design pressure 0.5 MPa absolute (150 °C saturation). The 0.5 MPa cap keeps the external
  pressure on the containment shell within a factor of four of its elastic buckling
  pressure even if the inside of containment were unpressurised.
- Normal operation: a small non-safety chilled-water loop holds the jacket at 25 °C and
  removes the module's normal heat loss (order 100 to 300 kW). Rock near the boreholes is
  at 14 °C, so the thermosyphons, which are switched off below 45 °C anyway, carry nothing.
- Accident: with all AC, DC and the chiller lost, the jacket water heats, boils at the
  drum, and its steam flows by pressure difference through two DN400 lines into the torus.
  Condensate returns by gravity along the same sloped lines.

### 3.3 Steam torus and thermosyphon evaporators

- A 0.8 m diameter toroidal pressure vessel in the ring drift, rated with the jacket.
- 128 thermosyphon evaporators, each a 4 m horizontal length of the thermosyphon tube,
  pass through the torus. Jacket steam condenses on their outside (film coefficient of
  order 8 kW/m²K) and the water inside boils (5 kW/m²K). Evaporator resistance is
  1.8e-4 K/W per unit: at 90 kW per unit the evaporator drop is 16 K.

### 3.4 Thermosyphons and upholes

- 128 sealed two-phase closed thermosyphons, working fluid demineralised water in
  stainless steel (316L or duplex), 125 mm ID, 141 mm OD. Each rises from the torus
  through an 8 m insulated riser, then a 57 m condenser section grouted in a 165 mm
  uphole, and ends in a 3 m gas reservoir at 8 m below grade.
- Upholes are drilled upward from the drift crown, alternating 0°, 10°, 20° and 30°
  outward tilt around the ring. Collar spacing is 0.74 m, but the tilt fan opens the
  spacing to 3 m between vertical neighbours and up to 30 m at the toe, and the insulated
  riser keeps the crowded collar zone from overheating.
- Totals: 7,296 m of condenser, 8,704 m of drilled hole.
- Borehole thermal resistance (film + wall + thermally enhanced grout, k = 2.0 W/mK):
  0.014 m·K/W, a third of a typical geothermal U-tube because the tube fills the hole.
- Gas loading: each unit carries a measured nitrogen charge sized so that the gas fills
  the entire condenser when the vapour is at or below 45 °C and fits entirely in the
  reservoir at 95 °C (flat-front model; pressure ratio 8.8). Between those temperatures
  the open condenser length is continuous, so the array throttles itself. Gas-loaded
  variable-conductance heat pipes are a mature spacecraft component. The reservoir sits in
  cold rock, which is the standard cold-reservoir configuration.
- Every unit is a factory-sealed, individually tested part. A single leak loses one unit
  (0.8 % of capacity). No valve, no damper, no instrument is needed for it to work.

### 3.5 Heat path

core → reactor vessel → steam in containment → containment wall → boiling jacket → torus
→ evaporators → vapour up the upholes → condensate film → tube wall → grout → bedrock →
(over months) ground surface. Every step is driven by gravity, pressure difference or
conduction.

## 4. Physics model

`model.py`, about 350 lines, no proprietary code.

1. **Decay heat**: the Glasstone-Sesonske / Todreas-Kazimi fission-product fit
   0.066 [t^-0.2 − (t + T)^-0.2] with T = 3 y, multiplied by 1.15 for actinides and fit
   uncertainty. Plus 140 GJ of stored primary-system heat (metal and water cooling from
   320 °C to 170 °C) released with a 2 h time constant. Peak load at scram is 25.6 MW.
2. **Jacket**: lumped capacitance of 0.70 GJ/K, implicit time stepping, coupled to the
   containment by a 300 kW/K conductance (wall conduction plus the module's decay-heat
   condensers) used only to estimate the containment inner-wall temperature.
3. **Thermosyphons**: isothermal vapour, evaporator and condenser film resistances,
   flat-front gas loading; per-unit load checked against the counter-current flooding
   limit (Faghri's correlation) and the sonic limit; design cap 50 % of flooding.
4. **Rock**: three-dimensional transient conduction. Every one of the 768 condenser
   segments (128 holes x 6 segments) is a finite line source; the ground surface is held
   at 14 °C by the method of images. Line integrals are done in the diffusion-scaled
   coordinate with the 1/distance singularity integrated analytically and the smooth
   remainder by 40-point Gauss-Legendre, so the response is accurate from 10 s to 3 y.
   Loads are piecewise constant in time and superposed. At each step the per-segment
   loads are solved from the isothermal-condenser condition (each open segment sees the
   same vapour temperature), so heat automatically shifts to cooler rock.
5. **Validation**: the numeric finite line source reproduces the analytic infinite line
   source to four significant figures at the borehole wall, 1 m and 5 m, at 1 h, 1 d and
   30 d (`python3 model.py` prints the comparison). Rock: granite, k = 3.0 W/mK,
   volumetric heat capacity 2.3 MJ/m³K, undisturbed 14 °C.

## 5. Results, base case (granite)

Scenario: scram from full power, simultaneous loss of all AC and DC power, chiller and
all water supplies, no operator action, ever.

| Time after scram | Heat into jacket | Heat into rock | Jacket | Vapour | Hottest borehole wall | Condenser open |
|---|---|---|---|---|---|---|
| 2.3 h (peak) | 9.5 MW | 7.8 MW | **94.7 °C** | 78 °C | 62 °C | 100 % |
| 12 h | 1.79 MW | 2.00 MW | 65 °C | 62 °C | 57 °C | 68 % |
| 1 d | 1.46 MW | 1.50 MW | 60 °C | 58 °C | 53 °C | 56 % |
| 7 d | 0.84 MW | 0.84 MW | 56 °C | 55 °C | 52 °C | 48 % |
| 30 d | 0.51 MW | 0.51 MW | 53 °C | 52 °C | 51 °C | 38 % |
| 1 y | 0.14 MW | 0.14 MW | 56 °C | 56 °C | 56 °C | 49 % |
| 3 y | 0.06 MW | 0.06 MW | 52 °C | 52 °C | 52 °C | 37 % |

- Peak jacket pressure 0.08 MPa gauge (94.7 °C), against a 0.5 MPa absolute rating.
- Peak borehole-wall temperature 70 °C at 3.7 h, against a 90 °C limit chosen to keep
  groundwater in the grout and fractures below boiling.
- Most-loaded thermosyphon: 90 kW, 48 % of its flooding limit at that moment, 13 % of
  its sonic limit.
- Energy absorbed by rock: 288 GJ in day 1, 834 GJ in week 1, 2.1 TJ in month 1, 9.2 TJ
  in year 1. The jacket's own sensible heat (49 GJ from 25 to 95 °C) buffers the first
  two hours while the decay heat falls from 25 MW to 4 MW.
- Grace period: unlimited. From day 3 on, heat into rock equals heat generated, the gas
  front throttles the array to hold the jacket in the 50 to 60 °C band, and the rock
  field never approaches saturation (the 1 y load of 0.14 MW is 2 % of what the array
  moved on day 1).

Figures: `figures/fig1_timeseries.png` (loads, temperatures, capacity margin),
`figures/fig2_rockfield.png` (rock temperature on a vertical section and a plan at 36 m
depth at days 1, 7, 30 and 365; after day 1 the gas front closes the upper condensers
and the load concentrates on the lower 40 m; by a year the ring volume is a uniform
50 to 58 °C and the warm zone reaches about 40 m from the axis), `figures/schematic.svg`.

## 6. Sensitivity

`figures/fig3_sensitivity.png`; each row is a full re-run.

| Case | Peak jacket °C (limit 150) | Peak wall °C (limit 90) | Load / flooding (cap 0.50) | Jacket at 30 d | Jacket at 1 y |
|---|---|---|---|---|---|
| Granite k = 3.0 (base) | 95 | 70 | 0.48 | 53 °C | 56 °C |
| Limestone or sandstone k = 2.0 | 99 | 80 | 0.50 | 60 °C | 59 °C |
| Shale k = 1.5 | 106 | 90 | 0.50 | 59 °C | 57 °C |
| 96 units instead of 128 | 109 | 81 | 0.52 (over cap) | 59 °C | 56 °C |
| 160 units | 86 | 64 | 0.44 | 56 °C | 55 °C |
| Poor grout k = 1.0 | 104 | 68 | 0.37 | 54 °C | 55 °C |
| Half-size jacket (60 t water) | 104 | 76 | 0.61 (over cap) | 53 °C | 56 °C |
| Warm rock 20 °C | 98 | 74 | 0.46 | 56 °C | 58 °C |
| 45 m condensers | 104 | 79 | 0.42 | 60 °C | 56 °C |


Every temperature limit holds in every case. The design passes in shale, which is close
to the worst rock a plant would be sited in, with the wall temperature at its limit; in
shale one would add a fifth tilt family or lengthen the condensers. Two cases exceed the
self-imposed 50 % flooding cap and show what it protects: dropping to 96 units, or halving
the jacket water (which lets the jacket heat faster in the first hours and pushes 117 kW
through each unit). Neither breaches a physical limit, but both erode the margin against
the one correlation in the model that is least certain for this geometry, since the
flooding correlation is for straight vertical tubes and these units have an L-bend. The
count of 128 and the 120 t jacket were chosen so that the flooding margin, not the rock,
is the binding constraint in granite.

## 7. Failure modes and defence in depth

| Failure | Consequence | Why it is tolerable |
|---|---|---|
| Loss of all power and water | None: the design case | Fully passive |
| One thermosyphon leaks its charge to rock | Loses 0.8 % of capacity | 128 independent units; grouted hole contains the water |
| Several units in one sector fail | Load shifts to neighbours through the torus | Isothermal torus; per-unit margin of 2 on flooding |
| Jacket-to-torus steam line breaks in the drift | Jacket steam vents into the sealed drift; second line still connects | Two lines; drift is a sealed rock space at 73 m depth; jacket inventory stays in the shaft |
| Jacket vessel leaks into the shaft | Water collects in the shaft sump around the containment base | The containment then radiates to the shaft liner and the lower jacket; shaft holds the full inventory below the containment top |
| Gas charge wrong (too much nitrogen) | Unit opens late or not at all | Each unit is hot-tested at the factory and can be re-tested in service by heating the torus with the chiller loop in reverse |
| Non-condensable gas generated over life (hydrogen from water and steel) | Adds to the deliberate charge and shifts the switch temperature up | Stainless steel, degassed fill, 3 m cold reservoir sized for the 60-year hydrogen inventory; periodic torus heat-up test verifies the switch point |
| Chiller fails in normal operation | Jacket warms to about 60 °C, thermosyphons open partially and hold it there, rock absorbs a few hundred kW until the chiller is fixed | Self-limiting; weeks of margin |
| Seismic event | Shaft-sited module; thermosyphons are flexible tubes in grouted rock | Same argument used for all below-grade SMRs |
| Aircraft impact, tornado, flood, attack on the heat sink | Nothing to hit: no surface structure above the sink | The point of the design |
| Groundwater flow through the rock | Advection removes heat faster | Only helps |

What the design does *not* do: it is a transient sink, not a steady one. Continuous
loads such as spent-fuel pool cooling must not be put on it, because a steady 2 MW would
warm the field by over 100 K within years. The chiller and the gas switch enforce this.

## 8. Construction and cost

Everything uses mining and geothermal methods that are routine at this scale.

| Item | Quantity | Method | Cost, rough |
|---|---|---|---|
| Ring drift | 94 m, 3 x 3 m | Roadheader or drill-and-blast | $1.5 M |
| Upholes | 8,704 m, 165 mm | Long-hole in-the-hole drilling rig from the drift | $1.5 to 2.5 M |
| Thermosyphons | 128, stainless, gas-loaded, tested | Fabricated in 12 m sections, welded in the drift, filled and sealed on site | $3 to 4 M |
| Grouting | 8,704 m | Thermally enhanced grout | $0.5 M |
| Torus, steam lines, jacket vessel, drum | 1 set | Pressure-vessel shop | $8 to 12 M |
| Chiller plant | 0.5 MW | Off the shelf | $1 M |
| Extra shaft depth beyond a conventional below-grade module | 40 to 60 m | Raise boring | $3 to 6 M |
| **Total incremental** | | | **$18 to 28 M per module** |

Against: the reactor pool of a NuScale-class plant (a seismic category I reinforced
concrete structure holding thousands of tonnes of water with its own cooling, make-up and
boil-off management), or the cooling towers and safety-class ultimate-heat-sink water
system of a conventional SMR. The heat sink here also carries no water consumption, no
make-up requirement and no siting constraint on a river or coast.

## 9. Safety and licensing argument

- Meets the intent of the 72 h passive coping requirement with an unlimited coping time
  and no consumable.
- The heat sink is below grade and distributed: it removes the ultimate-heat-sink
  external-hazard analysis (tornado, aircraft, flood, ice, biofouling, freezing) almost
  entirely.
- No active component and no valve in the safety path. The passive-system reliability
  question reduces to two physical facts: does the jacket boil, and do gravity
  thermosyphons condense in cold rock. Both are testable at full scale before fuel load by
  heating the jacket with the chiller loop reversed and watching the rock respond.
- Every temperature stays in the range of ordinary materials: jacket under 100 °C in the
  base case, rock under 70 °C, containment wall under 140 °C.
- The rock response is measurable by fibre-optic distributed temperature sensing in a few
  monitoring holes, giving an inspectable ultimate heat sink for the first time.

## 10. Open questions and the test programme

1. Flooding and start-up of an L-shaped 68 m water thermosyphon with a 4 m horizontal
   evaporator: build one full-scale unit in a vertical test rig and measure capacity
   against vapour temperature from 45 to 150 °C.
2. Gas-front behaviour with a 3 m reservoir in cold rock over years: confirm the
   switch temperatures and the hydrogen allowance.
3. Rock characterisation: conductivity, groundwater, fracture state, and whether the
   90 °C wall criterion is the right one at the site.
4. Whether the jacket external pressure should be limited by a relief line into the
   shaft sump rather than by rating; and containment external-pressure qualification.
5. Drift and torus layout for multi-module plants: modules at 60 m spacing keep the
   fields independent for the first year; closer spacing needs a joint run of the model.
6. The decay-heat curve should be replaced with an ANS-5.1-2014 calculation for the
   actual fuel cycle; the 1.15 factor is a placeholder for that.

## 11. Reproducing the results

```
pip install numpy scipy matplotlib iapws
python3 model.py                 # validation + base case, ~40 s
python3 final.py                 # writes runs/final.json and runs/final_series.npz
python3 sweep.py F_k2 '{"k_rock":2.0,"rhoc_rock":2.2e6}'   # any variant
python3 field.py                 # rock field, ~10 min
python3 plots.py                 # figures
```
