"""Two quick models behind PICK5 (research/converge/PICK5.md).

Part A: how much extra power a bottoming block could add to the behind-the-meter (BTM)
gas fleet being planned for US data centres, and what it is worth.

Part B: a one-second simulation of an islanded AI campus running on gas engines plus a
battery, with and without software that coordinates the compute load with the generators.
It asks how much battery the campus needs to ride through training-load swings, and what
coordination costs in wasted energy and delayed compute.

Every number marked ASSUMPTION is a labelled guess, not a measurement. Run: python3 island.py
"""
import numpy as np

# ---------------------------------------------------------------- Part A: bottoming potential
BTM_PLANNED_GW = 56.0  # Cleanview via Power Engineering, Apr 2026: 46 projects, 56 GW planned BTM

# ASSUMPTION: fleet mix and cycle numbers, typical of published data for these machine classes.
FLEET = {
    #               share, electric eff, exhaust share of fuel, recoverable frac, bottoming eff
    "recip engines": (0.60, 0.45, 0.30, 0.70, 0.20),
    "aero/industrial GT": (0.30, 0.38, 0.58, 0.75, 0.25),
    "fuel cells/other": (0.10, 0.55, 0.0, 0.0, 0.0),  # ignored: little usable exhaust
}
CAPACITY_FACTOR = 0.85  # ASSUMPTION: prime power for a data centre
GAS_PRICE = 4.0  # ASSUMPTION: $/MMBtu delivered
BLOCK_PRICE_PER_KW = 2000.0  # ASSUMPTION: between ORNL 2015 installed SRC/ORC figures for 1-20 MW


def part_a():
    print("Part A: bottoming blocks on the planned BTM data-centre gas fleet")
    total_mw = 0.0
    for name, (share, eff, exh, rec, beff) in FLEET.items():
        gw = BTM_PLANNED_GW * share
        uplift = (1 / eff) * exh * rec * beff  # extra MWe per MWe of prime mover
        add_mw = gw * 1000 * uplift
        total_mw += add_mw
        print(f"  {name:20s} {gw:5.1f} GW  uplift {uplift*100:4.1f}%  -> +{add_mw/1000:4.1f} GW")
    print(f"  total extra output: {total_mw/1000:.1f} GW with no extra fuel or gas supply")
    print(f"  hardware value at ${BLOCK_PRICE_PER_KW:.0f}/kW: ${total_mw*1000*BLOCK_PRICE_PER_KW/1e9:.1f}B")
    # value of one extra MW to an engine-powered campus = fuel it would otherwise burn
    heat_rate = 3.412 / 0.45  # MMBtu/MWh for a 45 % engine
    fuel_per_mw_yr = heat_rate * GAS_PRICE * CAPACITY_FACTOR * 8760
    print(f"  fuel avoided per bottoming MW: ${fuel_per_mw_yr/1e3:.0f}k/yr "
          f"(simple payback on fuel alone {BLOCK_PRICE_PER_KW*1000/fuel_per_mw_yr:.1f} yr)")
    print("  the real value is MW the campus cannot otherwise get: no turbine slot, no new gas "
          "lateral, no new air-permit tonnage\n")
    return total_mw


# ---------------------------------------------------------------- Part B: islanded campus
DT = 1.0  # s
HOURS = 24
N = int(HOURS * 3600 / DT)

JOBS = 4  # training jobs
JOB_MW = 60.0  # ASSUMPTION: power of one training job at full compute
INFER_MW = 60.0  # ASSUMPTION: inference load, mean
ITER_S, DIP_S, DIP_LEVEL = 6, 2, 0.55  # ASSUMPTION: iteration cycle, comm dip length and depth
CKPT_EVERY_S, CKPT_S, CKPT_LEVEL = 1800, 60, 0.30  # ASSUMPTION: checkpoint cadence and power
FAIL_PER_JOB_HR = 1 / 6  # ASSUMPTION: one hard failure every ~6 hours per job
RESTART_S = 420  # ASSUMPTION: idle time before a failed job restarts
IDLE_LEVEL = 0.05
ENGINE_MW = 25.0  # one QPac-style block (VoltaGrid: 25 MW units)
RAMP_FRAC_PER_S = 0.01  # ASSUMPTION: fleet can move 1 % of online capacity per second
GOV_TAU_S = 5.0  # ASSUMPTION: governor/turbocharger lag on top of the ramp limit
SOC_TAU_S = 300.0  # battery state of charge is pulled back to target over ~5 minutes
SHAPE_FRAC = 0.8  # software shapes job ramps to 80 % of the fleet ramp rate
HOLD_S = 30  # on a failure, GPUs burn for up to 30 s, then ramp down
FLOOR = 0.75  # coordinated+floor: GPUs fill comm dips up to 75 % of job power
BATT_COST_PER_KWH = 300.0  # ASSUMPTION: installed short-duration battery
BATT_COST_PER_KW = 150.0  # ASSUMPTION: power-related cost (inverters, interconnect)
FUEL_PER_MWH = 3.412 / 0.45 * 4.0  # $/MWh of gas for a 45 % engine at $4/MMBtu


def job_events(j):
    """Fixed per-job randomness, so every mode sees the same failures."""
    rng = np.random.default_rng(100 + j)
    offset = int(rng.integers(0, ITER_S))
    ck_offset = int(rng.integers(0, CKPT_EVERY_S))
    fails = np.flatnonzero(rng.random(N) < FAIL_PER_JOB_HR / 3600 * DT)
    return offset, ck_offset, fails


def job_trace(j, mode):
    """Power of one training job (MW) each second, split into the slow envelope
    (checkpoints, failures, restarts) and the fast iteration ripple around it."""
    offset, ck_offset, fails = job_events(j)
    if mode != "uncoordinated":  # software staggers checkpoints evenly across jobs
        ck_offset = j * CKPT_EVERY_S // JOBS
    t = np.arange(N)
    env = np.ones(N)
    env[(t + ck_offset) % CKPT_EVERY_S < CKPT_S] = CKPT_LEVEL
    for f in fails:
        env[f:f + RESTART_S] = IDLE_LEVEL
    dip = ((t + offset) % ITER_S < DIP_S) & (env == 1.0)
    depth = 1 - (FLOOR if mode == "coordinated+floor" else DIP_LEVEL)
    ripple = np.where(dip, -depth, 0.0)
    if mode == "coordinated+floor":
        ripple = np.where(dip, -(1 - max(FLOOR, DIP_LEVEL)), 0.0)
    return env * JOB_MW, ripple * JOB_MW


def shape(load, raw_jobs_floor, ramp):
    """Software limits how fast the campus load moves: drops are held up by burning power
    for HOLD_S then ramped down (wasted energy); rises are delayed (deferred compute)."""
    out = np.empty_like(load)
    out[0] = load[0]
    held = 0
    for i in range(1, len(load)):
        d = load[i] - out[i - 1]
        if d < -ramp:
            held += 1
            out[i] = out[i - 1] if held <= HOLD_S else out[i - 1] - ramp
        else:
            held = 0
            out[i] = out[i - 1] + min(d, ramp)
    return out


def run_island(load, online):
    ramp = RAMP_FRAC_PER_S * online * DT
    gen = np.empty_like(load)
    soc = np.empty_like(load)
    gen[0], soc[0] = load[0], 0.0
    for i in range(1, len(load)):
        target = load[i] + soc[i - 1] / SOC_TAU_S * 3600  # MW to restore SOC (MWh)
        g = gen[i - 1] + (target - gen[i - 1]) * DT / GOV_TAU_S
        gen[i] = gen[i - 1] + np.clip(g - gen[i - 1], -ramp, ramp)
        soc[i] = soc[i - 1] + (load[i] - gen[i]) * DT / 3600  # MWh drawn from battery
    p = load - gen
    # also ride through the trip of the largest engine until the rest ramp up
    trip_mw = ENGINE_MW
    trip_mwh = trip_mw * (trip_mw / ramp + GOV_TAU_S) / 2 / 3600
    mw = max(np.abs(p).max(), trip_mw)
    mwh = max(soc.max() - soc.min(), trip_mwh)
    return mw, mwh


def part_b():
    print(f"Part B: islanded campus, {JOBS} training jobs x {JOB_MW:.0f} MW + "
          f"{INFER_MW:.0f} MW inference, {HOURS} h at 1 s")
    peak = JOBS * JOB_MW + INFER_MW * 1.2
    engines = int(np.ceil(peak / ENGINE_MW)) + 1  # N+1
    online = engines * ENGINE_MW
    ramp = RAMP_FRAC_PER_S * online * DT
    rng = np.random.default_rng(1)
    infer = INFER_MW * (1 + 0.1 * np.sin(np.arange(N) / 86400 * 2 * np.pi)) + rng.normal(0, 2, N)
    base_energy = None
    res = {}
    for mode in ("uncoordinated", "coordinated", "coordinated+floor"):
        parts = [job_trace(j, mode) for j in range(JOBS)]
        env = sum(p[0] for p in parts) + infer
        ripple = sum(p[1] for p in parts)
        if mode == "uncoordinated":
            base_env = env
            base_ripple = ripple
            load, wasted, deferred = env + ripple, 0.0, 0.0
            base = load
        else:
            shaped = shape(env, None, SHAPE_FRAC * ramp)
            # waste: holding the envelope up, and burning to fill dips (floor mode)
            wasted = (np.clip(shaped - env, 0, None).sum()
                      + np.clip(ripple - base_ripple, 0, None).sum()) * DT / 3600
            deferred = np.clip(env - shaped, 0, None).sum() * DT / 3600
            load = shaped + ripple
        mw, mwh = run_island(load, online)
        cost = mw * 1000 * BATT_COST_PER_KW + mwh * 1000 * BATT_COST_PER_KWH
        res[mode] = (mw, mwh, cost, wasted, deferred)
        print(f"  {mode:18s} battery {mw:5.1f} MW / {mwh:5.2f} MWh = ${cost/1e6:5.1f}M; "
              f"extra fuel {wasted:5.1f} MWh/day (${wasted*FUEL_PER_MWH*365/1e6:4.2f}M/yr); "
              f"compute deferred {deferred:4.1f} MWh/day")
    print(f"  engines online: {engines} x {ENGINE_MW:.0f} MW (N+1) = {online:.0f} MW, "
          f"fleet ramp {ramp:.1f} MW/s; campus peak {peak:.0f} MW; "
          f"daily energy {base.sum()*DT/3600:,.0f} MWh")
    return res


if __name__ == "__main__":
    part_a()
    part_b()
