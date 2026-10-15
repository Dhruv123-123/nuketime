# LOCKSTEP: a pressurised-water reactor and a data centre engineered as one island

Every nuclear-plus-data-centre deal announced so far connects a seller and a buyer with a
wire and stops there. This design treats the two as what they physically are: complements.
The plant owns the largest heat-rejection system on the site next to a data centre that
builds its own; the data centre owns hundreds of megawatts of tested backup generation and
batteries next to a plant whose worst accident is losing 20 MW of AC; and a data centre of
about 40 to 50 % of the plant's output is exactly the load that lets a PWR ride through a
grid loss without a reactor trip. Three provisions, each evaluated with its own model:

1. **Island on the data centre.** On loss of the grid the generator breaker opens and the
   unit keeps running, feeding the data centre and its own house load. No reactor trip, no
   xenon dead time, no loss of offsite power as far as the safety buses are concerned.
2. **Share the cooling tower.** The data centre rejects its heat into the plant's
   circulating-water hot return through plate heat exchangers and takes its cooling water
   from the tower basin. No data-centre towers, dry coolers or chillers.
3. **Tie the data centre's backup fleet to the plant's safety buses** through a normally
   open, seismically qualified, sync-checked breaker as a diverse AC source.

Files: `island.py` (plant transient), `tower.py` (Merkel tower, condenser, turbine, hourly
year), `risk_econ.py` (blackout risk, economics), `plots.py`, `runs/`, `figures/`.

---

## 1. What it yields

| Quantity | Value |
|---|---|
| Grid-loss ride-through | No reactor trip with a data-centre load ≥ 40 % of plant rating (40 % steam dump) or ≥ 34 % (50 % dump); demonstrated in the model at 45 % with 6.5 K of over-temperature ΔT margin and no safety-valve lift |
| Station-blackout core-damage frequency (generic fleet numbers) | 3.2 × 10⁻⁶ per reactor-year baseline; ÷ 5 with islanding; ÷ 32 with the backup-fleet tie; ÷ 190 with both |
| Plant output given up for shared cooling (500 MW data centre) | 7.6 MW annual average (0.6 %), 67 GWh per year |
| Data-centre cooling energy avoided | about 20 MW (4 % of IT), 175 GWh per year |
| Data-centre cooling plant not built | about $125 M (dry coolers, towers, evaporative plant at $250 per kW); heat exchangers and CDUs remain |
| System capital | about $90 M (heat exchangers and piping $40 M, safety-bus tie $35 M, islanding controls and testing $15 M) |
| Net | +$9 M per year in energy, +$35 M in capital, plus the safety and reliability outcomes above |
| Water the data centre receives | 26 to 35 °C, 99th percentile 34.5 °C, never above the ASHRAE W40 liquid-cooling class |

The money is positive but modest. The point of the design is the two things money does not
capture: the plant becomes materially safer, and the data centre gets power that survives
the grid rather than power that depends on it.

## 2. Lineage and what is new

- House-load operation (running back to the plant's own auxiliaries on grid loss) is an
  established capability in German, French and Korean plants and is the subject of a GE
  patent (US 9,620,252). Korean probabilistic safety assessments credit it. Most US plants
  are not designed or licensed for it, and full rejection to a 5 % house load is the hardest
  possible load-rejection transient, which is why many cannot.
- Loss-of-offsite-power and station-blackout risk is the largest single contributor to core
  damage frequency at many PWRs (NUREG/CR-6890, 2005).
- Data centres co-located with nuclear plants (Susquehanna and others) buy power across the
  switchyard and build their own cooling, batteries and generators.

What Lockstep adds: the data-centre load is used as the island load, which turns the hardest
load-rejection transient into an ordinary 50 % one; the data centre's backup fleet is
credited as a diverse AC source in the plant's blackout defence; and the two heat-rejection
systems are merged. None of the three has been implemented, and no source found engineers
them together or quantifies them.

## 3. Design

### 3.1 Electrical

- Generator bus tap: a 600 MVA, 24/34.5 kV feeder transformer connected on the generator
  side of the generator circuit breaker feeds the data centre. On a grid fault the generator
  breaker or the switchyard breakers open; the generator, the unit auxiliary transformer and
  the data-centre feeder remain one island.
- Island control: the turbine governor switches from power control to frequency control
  (4 % droop with slow restoration); fast valving (full stroke in 0.3 s) is armed by the
  breaker-open signal; the steam dump load-rejection controller opens on the power
  mismatch. Rod control runs back at maximum speed until reactor power matches the island
  load. These are standard Westinghouse-class functions; the design change is the setpoints
  and the tested procedure.
- Data centre as load: constant-power electronic load with UPS batteries (520 MW for
  10 minutes) that ride through the first second of the frequency swing and, in island
  mode, provide fast frequency response. Training jobs can be paused, so the load can be
  shed in blocks if the island needs it.
- Diverse AC tie: a dedicated 34.5/4.16 kV transformer from the data centre's generator
  bus to each safety bus through a normally open, sync-checked, seismically qualified
  breaker. The data centre's N+1 generator fleet (560 MW) and batteries are not
  safety-class; they are credited as a diverse source in the same way FLEX portable
  equipment is, but permanently connected and automatically started.

### 3.2 Heat rejection

- The plant's circulating-water system (43,400 kg/s, 2,000 MWth to a natural-draft tower
  designed for 25.6 °C wet bulb, 5.4 K approach, 11 K range) tap of 12 m³/s from the tower
  basin feeds plate heat exchangers; the warmed water rejoins the hot return downstream of
  the condenser, so the condenser's own range is unchanged and the only plant penalty is the
  rise in tower cold-water temperature (0.6 K at the design day for 500 MW).
- The data-centre side is a closed treated loop with a 12 K rise; supply temperature is the
  tower cold water plus a 2 K pinch: 26 to 35 °C over a synthetic mid-latitude year, which
  suits liquid-cooled halls (ASHRAE W32 to W40). Air-cooled halls that need 18 to 24 °C
  water would still need chillers and are not part of this design.
- Water: the data centre's evaporation moves to the plant's tower (about 0.2 m³/s for
  500 MW); one intake, one discharge, one consumptive-use permit.

### 3.3 Not changed

The reactor, its safety systems and its licensing basis for accidents are untouched. The
safety-bus tie is an addition on the supply side of the safety buses, behind isolation
devices, in the same place a FLEX connection sits today.

## 4. Models

### 4.1 Islanding transient (`island.py`)

Reduced-order PWR plant model of the kind used for load-rejection screening: six-group point
kinetics with Doppler (−2.8 pcm/K) and moderator (−35 pcm/K) feedback and Xe-135/I-135;
lumped fuel, core coolant, steam-generator primary node and cold leg; saturated
steam-generator secondary; pressuriser as a compressible volume with spray, PORV and
heaters; HP turbine prompt and LP through an 8 s reheater lag; generator swing equation
(H = 5.5 s on 1,300 MVA); governor with droop, restoration and fast valving; steam dump on
power mismatch and Tavg error; rod control on Tavg − Tref(load) with runback. Trip checks:
overspeed 66 Hz, under-frequency 57 Hz, pressuriser 16.7 MPa high and 13.0 MPa low,
steam-generator safety valves 8.3 MPa, over-temperature and over-power ΔT in the
Westinghouse form, overpower 118 %.

### 4.2 Shared tower (`tower.py`)

Merkel counterflow tower sized at the design point (KaV/L = 1.10, L/G = 1.4), off-design
solved for cold-water temperature at fixed water flow with natural-draft airflow scaling
as heat load to the one-third power; surface condenser with NTU from a 3 K terminal
difference; LP-turbine exhaust work from IAPWS-97 steam tables; 8,760-hour synthetic wet-bulb
year (mean 12 °C, seasonal amplitude 11 K, daily 3 K, noise 2 K). Cases: data centre 0, 250,
500, 750 MW; tower with 25 % more cells.

### 4.3 Blackout risk and economics (`risk_econ.py`)

Generic-fleet loss-of-offsite-power frequencies by category (plant-centred 0.0025,
switchyard 0.010, grid 0.019, weather 0.0043 per reactor-year), non-recovery probabilities
at the four-hour coping time, two diesel trains at 0.02 unavailability with 5 % common
cause, and a 0.5 conditional core-damage probability once the coping time is exceeded.
Islanding removes 90 % of grid and weather events and half of switchyard events as plant
LOOPs; the backup-fleet tie multiplies the all-AC-failure probability by 0.02 (0.05 in
weather). These are order-of-magnitude inputs, labelled as such; a plant PRA would replace
them.

## 5. Results

### 5.1 Islanding

Figure `fig1_island.png`: at full power the grid breaker opens. With the 520 MW data centre
on the island, frequency peaks at 61.4 Hz, the turbine valves close to the island load in a
third of a second, the steam dump opens to 40 %, rods run back, reactor power settles at
49 % in about two minutes, average coolant temperature peaks 9 K above program, pressuriser
pressure peaks at 16.4 MPa (the PORV lifts briefly), steam-generator pressure peaks at
7.7 MPa (no safety-valve lift), and the over-temperature ΔT margin never falls below
6.5 K. No trip. The same plant rejecting to house load only sees the pressuriser exceed the
trip setpoint and the steam-generator safety valves lift within the first minute: a trip,
which is what most US plants would do today.

Figure `fig2_threshold.png`: the minimum data-centre load for a clean ride-through is about
40 % of plant rating with a 40 % steam dump and 34 % with a 50 % dump; a 60 % dump avoids
even the PORV lift at 45 %. Load steps of +100 MW and −200 MW on the island are absorbed
without any limit being approached. Slow valving (0.3 s⁻¹ stroke) fails: frequency swings
from 56.6 to 64.9 Hz and the plant trips, so fast valving armed by the breaker signal is a
hard requirement.

Figure `fig3_island24h.png`: over 24 hours on the island the xenon transient after the power
drop is compensated by rod withdrawal within the model's rod worth; the island holds.

### 5.2 Shared cooling

Figure `fig4_tower.png`: the plant loses 4.1, 7.6 and 10.8 MW on average for 250, 500 and
750 MW data centres. Adding 25 % more tower cells recovers only about 1.3 MW because the
plant's condenser range and terminal difference, not the tower approach, dominate at this
water flow; the cheaper remedy is to accept the 0.6 % loss, which is a fifth of what the
data centre saves in fan power. Data-centre supply water stays below 35 °C for all but
about 1 % of hours and never reaches 40 °C.

### 5.3 Risk

Figure `fig5_risk.png`: station-blackout core-damage frequency 3.2 × 10⁻⁶ per reactor-year
baseline, 6.5 × 10⁻⁷ with islanding, 1.0 × 10⁻⁷ with the backup-fleet tie, 1.7 × 10⁻⁸ with
both. Grid- and weather-related events, which dominate the baseline, are the ones islanding
removes.

## 6. Failure modes and limits

| Item | Assessment |
|---|---|
| Islanding fails (valve, dump or control fault) | The plant trips as it would today; nothing is worse than the status quo. Reliability of the island function is what the PRA credit rests on; the model assumes 90 % |
| Data centre trips off during the island | A 45 % load loss on an island: the same transient as the initial event but from 50 % power; the plant runs back to house load and, without the data centre, will likely trip. Batteries and staged load shedding are the mitigation |
| Safety-bus tie misoperation | Normally open, sync-check and interlocks against paralleling non-safety sources onto a faulted bus; qualified breaker; single-failure criteria unchanged because the tie is additional |
| Common-cause loss of both fleets (site-wide flood, seismic) | The tie is qualified; the generator fleet is diverse in type and location from the plant's diesels; weather correlation is included in the risk model (0.05 rather than 0.02) |
| Heat-exchanger leak | Open circulating water into a closed treated loop or vice versa; conductivity monitoring; isolation; the data centre reverts to reduced load |
| Fouling of the plant condenser from the shared loop | Plate exchangers keep the loops separate; the circulating-water chemistry is unchanged |
| Hot summer, data centre at full load | Cold water peaks at 33.8 °C; supply 35.8 °C; within W40 |
| Regulatory | Behind-the-meter load on the generator bus and a diverse AC tie both need NRC and grid-operator review; the FERC dispute over Susquehanna shows the interconnection side is not trivial |

What it does not do: it does not raise the plant's efficiency, and the money is modest. It
does not make the data centre independent of the plant: a reactor trip still hands the data
centre to its own batteries and generators, as today.

## 7. Open questions

1. Plant-specific load-rejection capability: the model is a generic four-loop PWR; some
   designs have smaller steam dumps or slower rods and would need the 50 % dump case.
2. Island frequency and voltage control with a large constant-power electronic load; the
   UPS inverters' response and any grid-forming capability should be tested in a hardware
   loop.
3. PRA credit for a non-safety AC source: the licensing path (FLEX precedent) and the tie's
   qualification.
4. Real climate data and the plant's actual circulating-water flow for the tower penalty.
5. The 24 h island relies on rod worth; boron dilution over a longer island should be
   analysed.

## 8. Reproducing the results

```
pip install numpy scipy matplotlib iapws
python3 island.py      # transient cases, writes runs/island*.npz and runs/island.json
python3 tower.py       # hourly year, writes runs/tower.json (about 2.5 min)
python3 risk_econ.py   # writes runs/risk_econ.json
python3 plots.py       # figures
```
