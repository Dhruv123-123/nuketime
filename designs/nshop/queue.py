"""Lead times for nuclear-qualified parts as reactor builds ramp.

US capacity for safety-related machining, welding and NDE under ASME Section III /
NQA-1 is modelled as c parallel "cells" (a cell = one qualified machine-and-crew line
working a year). Jobs arrive from fleet maintenance plus new builds; each takes a mean
of SERVICE months. Lead time is service, plus the random M/M/c
(Erlang C) wait at the month's utilisation (capped at 0.97), plus the backlog that
builds whenever demand exceeds capacity, worked off at the capacity rate. Simulated
month by month as demand and qualified capacity change.

Every quantity below except the sourced ones is an assumption, labelled as such; the
point is the shape (queues explode near full utilisation) and the leverage of
qualifying new capacity faster, not the exact months.

Sourced:
- N-stamp holders fell from ~500 (1970s-80s) to ~100 (Power Engineering, 2009).
- Getting a stamp took Fluor ~20 months, ~$1M for experienced firms (same source).
- Machining, welding, finishing, inspection and NDE "frequently sit on the critical
  path"; heavy manufacturing often has two to five qualified firms (Nuclear Scaling
  Initiative, March 2026).
- Vogtle 3/4: a 3-6 month delay costing $920M, blamed on "tens of thousands" of
  missing quality documents (E&E News, Feb 2022) -> ~$75M-$155M per unit-month.
"""
import json
import numpy as np
from math import factorial

YEARS = np.arange(2026, 2037)
SERVICE = 3.0              # months per job (assumption)
C0 = 100.0                 # qualified cells in 2026 (assumption)
FLEET = 60.0               # cell-years a year for 94 operating units (assumption, rho0 = 0.6)
CELLS_LARGE = 40.0         # cell-years per large unit, spread over 4 years before start-up (assumption)
CELLS_SMR = 10.0           # cell-years per ~300 MWe SMR, over 3 years (assumption)
ORGANIC = 0.03             # existing holders' capacity growth a year (assumption)
ENTRY_LAG = 2              # years from firm demand to a newly stamped shop (20 months + decision)
ENTRY_SHARE = 0.5          # share of a demand gap that conventional entry fills (assumption)
COST_LARGE = 100e6         # $ per unit-month of critical-path delay (Vogtle range midpoint)
COST_SMR = 15e6            # $ per SMR-month (assumption, scaled by size and interest)
CRIT = 0.25                # share of excess lead time that lands on a project's critical path

SCENARIOS = {
    # starts per year from 2027: (large units, SMRs)
    "low":  dict(large=[0, 0, 1, 1, 1, 1, 1, 1, 1, 1], smr=[1, 2, 2, 3, 3, 4, 4, 4, 4, 4]),
    "base": dict(large=[0, 1, 1, 2, 2, 2, 2, 2, 2, 2], smr=[2, 3, 4, 6, 8, 10, 10, 10, 10, 10]),
    "high": dict(large=[1, 2, 3, 4, 4, 4, 4, 4, 4, 4], smr=[3, 5, 8, 12, 15, 15, 15, 15, 15, 15]),
}


def erlang_wait(rho, c):
    """Mean M/M/c queue wait in units of service time, via the Erlang C formula."""
    c = max(int(round(c)), 1)
    rho = min(rho, 0.97)
    a = rho * c
    logt = [k * np.log(a) - np.sum(np.log(np.arange(1, k + 1))) for k in range(c + 1)]
    m = max(logt)
    t = np.exp(np.array(logt) - m)
    last = t[c] / (1 - rho)
    pw = last / (t[:c].sum() + last)
    return pw / (c * (1 - rho))


def demand(sc):
    """Cell-years demanded each year."""
    d = np.full(len(YEARS), FLEET)
    for i, (nl, ns) in enumerate(zip(sc["large"], sc["smr"])):
        y = i + 1                                   # start year index (2027 = 1)
        for k in range(4):
            if y + k < len(YEARS):
                d[y + k] += nl * CELLS_LARGE / 4
        for k in range(3):
            if y + k < len(YEARS):
                d[y + k] += ns * CELLS_SMR / 3
    return d


def run(sc, network_cells_per_year=0.0, network_start=2028):
    d = demand(sc)
    cap = np.zeros(len(YEARS))
    cap[0] = C0
    backlog = 0.0                                   # cell-months of work waiting beyond normal queueing
    out = []
    for i, yr in enumerate(YEARS):
        if i:
            cap[i] = cap[i - 1] * (1 + ORGANIC)
            j = i - ENTRY_LAG                       # conventional entry answers demand seen ENTRY_LAG years ago
            if j >= 0:
                gap = max(d[j] / 0.8 - cap[j], 0)  # firms enter to bring utilisation toward 80 %
                cap[i] += ENTRY_SHARE * gap / ENTRY_LAG
        net = network_cells_per_year * max(yr - network_start + 1, 0)
        c = cap[i] + net
        leads = []
        for _ in range(12):
            backlog = max(backlog + d[i] / 12 - c / 12, 0.0)    # cell-months
            rho = min(d[i] / c, 0.97)
            leads.append(SERVICE * (1 + erlang_wait(rho, c)) + backlog / (c / 12))
        out.append(dict(year=int(yr), demand=round(float(d[i]), 1), capacity=round(float(c), 1),
                        utilisation=round(float(d[i] / c), 3), lead_months=round(float(np.mean(leads)), 1)))
    return out


def delay_cost(sc, base, alt):
    """$ of critical-path delay avoided. Each unit is delayed by CRIT x the worst excess
    lead time (over the 3-month norm) it meets during its build window; counted once per unit."""
    def excess(run_, i0, n):
        w = [r["lead_months"] - SERVICE for r in run_[i0:i0 + n]]
        return max(w) if w else 0.0
    saved = 0.0
    for i, (nl, ns) in enumerate(zip(sc["large"], sc["smr"])):
        y = i + 1
        saved += nl * COST_LARGE * CRIT * (excess(base, y, 4) - excess(alt, y, 4))
        saved += ns * COST_SMR * CRIT * (excess(base, y, 3) - excess(alt, y, 3))
    return saved


if __name__ == "__main__":
    res = {}
    for name, sc in SCENARIOS.items():
        base = run(sc)
        res[name] = dict(base=base)
        print(f"\n{name}: year util lead(months)")
        for r in base:
            print(r["year"], r["utilisation"], r["lead_months"])
        for k in (5, 10, 20):
            alt = run(sc, network_cells_per_year=k)
            res[name][f"network_{k}"] = alt
            res[name][f"saved_{k}_B"] = round(delay_cost(sc, base, alt) / 1e9, 2)
            peak_b = max(r["lead_months"] for r in base)
            peak_a = max(r["lead_months"] for r in alt)
            print(f"  +{k} cells/yr from 2028: peak lead {peak_b:.1f} -> {peak_a:.1f} months, "
                  f"delay cost avoided 2027-36 ${res[name][f'saved_{k}_B']}B")
    json.dump(res, open("runs/queue.json", "w"), indent=1)


def sensitivity():
    """Base-scenario peak lead time, and +10 cells/yr saving, as key assumptions move."""
    global C0, CELLS_LARGE, CELLS_SMR, ENTRY_LAG
    keep = (C0, CELLS_LARGE, CELLS_SMR, ENTRY_LAG)
    rows = []
    for label, c0, cl, cs, lag in (("as set", 100, 40, 10, 2), ("capacity x1.5", 150, 40, 10, 2),
                                   ("capacity x2", 200, 40, 10, 2), ("work per unit x0.5", 100, 20, 5, 2),
                                   ("work per unit x2", 100, 80, 20, 2), ("entry lag 1 yr", 100, 40, 10, 1),
                                   ("entry lag 3 yr", 100, 40, 10, 3)):
        C0, CELLS_LARGE, CELLS_SMR, ENTRY_LAG = c0, cl, cs, lag
        sc = SCENARIOS["base"]
        b, a = run(sc), run(sc, network_cells_per_year=10)
        rows.append(dict(case=label, peak_lead=max(r["lead_months"] for r in b),
                         peak_lead_net=max(r["lead_months"] for r in a),
                         saved_B=round(delay_cost(sc, b, a) / 1e9, 2)))
        print(rows[-1])
    C0, CELLS_LARGE, CELLS_SMR, ENTRY_LAG = keep
    return rows


if __name__ == "__main__":
    res["sensitivity_base"] = sensitivity()
    json.dump(res, open("runs/queue.json", "w"), indent=1)
