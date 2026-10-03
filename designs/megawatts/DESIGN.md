# MEGAWATTS: is monitoring for lost output a company?

A reduced-order model of a 3,411 MWt PWR secondary cycle, built to test one candidate for the
second pick: software that finds the megawatts a running reactor quietly loses to drifting
instruments and degrading equipment. The answer from the model is that better detection is worth
about 1 MWe per unit over what a plant's own engineers already catch, and the people who sell that
detection today already own the market. It is a negative result, kept so the idea is not reopened.

## The model

- `plant.py`: daily simulation over two years. Four slow faults may each appear (probability 0.6,
  onset day 100 to 600):
  - feedwater venturi fouling, so indicated flow reads high and the reactor runs below its licence
    (0.1 to 2.6 % in the literature, average about 1 %);
  - cycle-isolation leakage of main steam to the condenser;
  - condenser fouling (lower UA, higher back-pressure, about 2 % output per inHg);
  - feedwater heater degradation (lower final feedwater temperature).
  The plant has the sensors a plant has: indicated flow, temperatures, back-pressure, gross output,
  cooling-water inlet temperature, with noise, slow drift, a seasonal correction error and an AR(1)
  unexplained output variation (sd 0.25 %, 60-day memory) that sets realistic alarm thresholds.
- `monitor.py`: three detectors.
  - *Conventional*: 30-day KPIs a performance engineer already trends (corrected output,
    cleanliness factor, final feedwater temperature).
  - *Model-based*: weighted least squares of the signature vector through the plant's sensitivity
    matrix, 30-day window. This is a stand-in for data validation and reconciliation (DVR).
  - *Combined*: either one alarming.
  `operate()` runs the repair loop: an alarm opens an investigation (30 or 90 or 180 days busy),
  the fault is fixed 30 days after it is confirmed, and alarms re-arm.
- `calibrate.py`: thresholds at a 5 % false-alarm rate over 200 fault-free plants.
- `compare.py`: 200 plants per setting.

## Results (average MWe lost over two years, 200 plants)

| Detector | Investigation 30 d | 90 d | 180 d |
|---|---|---|---|
| No repairs | 9.63 | 9.63 | 9.63 |
| Conventional KPIs | 2.53 | 3.07 | 3.71 |
| Model-based (DVR-like) | 2.10 | 2.10 | 2.10 |
| Combined | 1.88 | 1.95 | 1.99 |
| Oracle (fixed on day one) | 0.31 | 0.31 | 0.31 |

Combined over conventional is +0.65, +1.12 and +1.72 MWe per unit, which is $0.49M, $0.84M and
$1.28M per unit-year at $85/MWh. Model-based detection finds venturi bias much sooner (98 days
against 171 to 305) but catches fewer leaks (60 of 195 against 111 to 121). False alarms are about
0.05 to 0.08 per plant-year.

## What the market already has

- Measurement-uncertainty recapture uprates are done: 57 approved, and ultrasonic flow meters
  (LEFM) are installed on more than 90 reactors, which removes the venturi fault this model scores
  highest on.
- DVR is NRC-accepted (EPRI 3002018337, August 2023); Salem uses it to defend its existing 1.4 %
  uprate. Bruce Power recovered 39.7 MWe across eight units with it.
- Belsim (sold by GSE, 30+ US units), BTB Jansky (70+), Curtiss-Wright PEPSE and EtaPRO are
  installed incumbents.

## Verdict

At about 1 MWe and $0.5M to $1.3M per unit-year, 94 US units cap the software at roughly $25M to
$50M a year even at full share, against installed incumbents and a buyer (the utility performance
engineer) who already trends the same signals. Not the pick. Like the wellfield model, it says that
software optimising a competently run asset is worth single-digit percent.
