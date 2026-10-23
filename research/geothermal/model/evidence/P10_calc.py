"""P10 back-of-envelope: crew time per well, cost per well, and how paired
equilibrium logs shrink the hierarchical BHT cold-bias term (rank 5).
All inputs are estimates (unverified). Run: python3 -I P10_calc.py"""
import math

# ---- crew time for one well (hours) ----
def well_hours(depth_m, log_speed=9.0, pooh_speed=60.0, sampler=True):
    rig_up, rig_down = 1.5, 1.0
    log_in = depth_m / log_speed / 60          # continuous down-log, gauge leading
    pull = depth_m / pooh_speed / 60
    repeat = 0.5                               # 200 m repeat section at TD
    samp = (depth_m / 40 / 60) * 2 + 0.75 if sampler else 0  # run in/out fast + dwell
    return rig_up + log_in + pull + repeat + samp + rig_down

for d in (1000, 2000, 3000):
    print(f"{d} m: log only {well_hours(d, sampler=False):.1f} h, log+sampler {well_hours(d):.1f} h")

# ---- marginal cost per well ----
crew_day = 2 * 550 + 2 * 180 + 250 + 150     # 2 techs, per diem, fuel, consumables
lab = 550 + 150 + 200                         # noble gas, water chem, gas comp
for wells_per_day in (1.0, 1.5):
    print(f"{wells_per_day} wells/day: field ${crew_day/wells_per_day:,.0f} + lab ${lab} per well")

# ---- BHT cold-bias calibration (normal-normal) ----
# Basin-era bias mu_b ~ N(m, tau0^2); each paired well gives bias residual with sd sig.
tau0, sig = 8.0, 6.0   # C: prior sd of a basin's bias; per-pair scatter (BHT noise vs log)
for n in (0, 5, 10, 20, 40):
    post = 1 / math.sqrt(1 / tau0**2 + n / sig**2)
    # predictive sd of a single corrected BHT = sqrt(bias_sd^2 + random scatter 8 C)
    pred = math.sqrt(post**2 + 8.0**2)
    print(f"n={n:2d} pairs: bias sd {post:4.1f} C, single-BHT predictive sd {pred:4.1f} C")

# ---- T at 1.5 km in a cell: wildcat-only vs own log ----
print("cell with own equilibrium log at 1.5 km: sd ~0.5-1 C (log) vs ~11-13 C (BHT, uncalibrated)")
