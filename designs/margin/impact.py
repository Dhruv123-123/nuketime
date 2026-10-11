"""Uprate engineering as a dependency graph: what an impact engine buys, in megawatt-months.

A power uprate changes one number (licensed core thermal power) and that change ripples through
the plant's design basis: heat balance, NSSS parameters, core design, transient and LOCA analyses,
containment response, equipment qualification, dose, BOP equipment, setpoints, PRA, tech specs,
UFSAR. The graph below is an abridged PWR extended-uprate analysis scope, built from the review
areas an EPU licence amendment must cover (NEI 08-10; NRC's EPU review standard). Durations and
owners are assumptions, labelled; the point is the mechanism, not the exact months.

Two things make the analysis phase long, and an impact engine attacks both:
1. Drafting and checking time on document-heavy work (A/E calcs, UFSAR, tech specs, LAR).
   Vendor code runs and independent verification stay, so vendor tasks shrink much less.
2. Missed impacts. Scoping is done by hand across legacy PDFs; an affected analysis that is not
   scoped up front is found late (during LAR assembly or as an NRC request for additional
   information) and re-enters the schedule then, with rework on everything downstream of it.

The output is converted to energy through the step that actually gates megawatts: modified plant
can only start at a refuelling outage (every 18 months) after both NRC approval and hardware
arrival. So saved months are worth nothing unless they move the project into an earlier outage.

Sourced inputs (see research/converge/ml_software_notes.md):
- Columbia EPU took 18 months of analysis before approval; NRC review target 12 months (EPU),
  9 (stretch), 6 (MUR).
- ~$58k per MW-month of output at $85/MWh and 93% capacity factor (PPA range $70-115/MWh).
"""
import json
import numpy as np

rng = np.random.default_rng(7)

# node: (owner, base months, effort engineer-months, depends on)
# owner V = NSSS/fuel vendor (licensed codes), A = architect-engineer calcs, U = utility licensing
GRAPH = {
    "heat_balance":      ("A", 2.0, 4,  []),
    "nsss_parameters":   ("V", 3.0, 8,  ["heat_balance"]),
    "core_design":       ("V", 4.0, 10, ["nsss_parameters"]),
    "non_loca":          ("V", 6.0, 24, ["nsss_parameters", "core_design"]),
    "loca":              ("V", 6.0, 20, ["nsss_parameters", "core_design"]),
    "cont_mass_energy":  ("V", 3.0, 6,  ["loca"]),
    "containment":       ("A", 3.0, 8,  ["cont_mass_energy"]),
    "helb":              ("A", 3.0, 8,  ["heat_balance"]),
    "eq_profiles":       ("A", 4.0, 14, ["containment", "helb"]),
    "ecc_npsh":          ("A", 2.0, 4,  ["containment"]),
    "dose_ast":          ("A", 4.0, 10, ["core_design", "containment"]),
    "control_room_hab":  ("A", 2.0, 4,  ["dose_ast"]),
    "sg_integrity":      ("V", 3.0, 8,  ["nsss_parameters"]),
    "rcs_structural":    ("V", 5.0, 16, ["nsss_parameters"]),
    "fiv":               ("A", 3.0, 6,  ["heat_balance"]),
    "turbine_gen":       ("A", 3.0, 6,  ["heat_balance"]),
    "fw_condensate":     ("A", 3.0, 8,  ["heat_balance"]),
    "heaters_msr":       ("A", 2.0, 4,  ["heat_balance"]),
    "fac_program":       ("A", 2.0, 4,  ["heat_balance"]),
    "transformer":       ("A", 2.0, 3,  ["turbine_gen"]),
    "grid_study":        ("A", 4.0, 4,  ["turbine_gen"]),
    "heat_sink_ccw_sw":  ("A", 3.0, 8,  ["heat_balance", "core_design"]),
    "spent_fuel_pool":   ("A", 2.0, 3,  ["core_design"]),
    "atws":              ("V", 2.0, 4,  ["non_loca"]),
    "sbo":               ("A", 2.0, 3,  ["heat_balance", "heat_sink_ccw_sw"]),
    "safe_shutdown_fire":("A", 2.0, 4,  ["non_loca"]),
    "setpoints":         ("A", 3.0, 10, ["non_loca", "loca"]),
    "pra_update":        ("A", 4.0, 10, ["non_loca", "loca", "heat_sink_ccw_sw"]),
    "tech_specs":        ("U", 2.0, 4,  ["setpoints", "non_loca", "loca"]),
    "ufsar_markup":      ("U", 3.0, 10, ["non_loca", "loca", "containment", "eq_profiles", "dose_ast",
                                         "heat_sink_ccw_sw", "fw_condensate", "rcs_structural"]),
    "lar_package":       ("U", 3.0, 8,  ["tech_specs", "ufsar_markup", "pra_update", "eq_profiles",
                                         "control_room_hab", "ecc_npsh", "sg_integrity", "atws", "sbo",
                                         "safe_shutdown_fire", "spent_fuel_pool", "fiv", "grid_study",
                                         "transformer", "heaters_msr", "fac_program", "turbine_gen"]),
}
ORDER = list(GRAPH)  # already topological
OVERLAP = 0.6  # analyses run partly in parallel on preliminary inputs; calibrates a clean EPU
               # critical path to ~19 months, near Columbia's 18 months of analysis (assumption)

# Scenario knobs (assumptions)
SCENARIOS = {
    "today": dict(
        speed={"V": 1.00, "A": 1.00, "U": 1.00},   # duration multiplier by owner
        p_miss=0.12,        # share of non-root analyses not scoped up front (assumption)
        late_find=0.6,      # missed items found at this fraction of the way through (LAR assembly / RAI)
        rework=0.5,         # downstream items already done redo this share of their duration
        rai_months=(2, 5),  # extra NRC review months per late-found safety item (uniform)
        sigma=0.30,         # lognormal duration spread
    ),
    "impact_engine": dict(
        speed={"V": 0.85, "A": 0.55, "U": 0.45},   # drafting/checking compressed; codes and IV&V stay
        p_miss=0.02,
        late_find=0.6, rework=0.5, rai_months=(2, 5), sigma=0.25,
    ),
    # Sensitivity: an engine that only half works (assumption)
    "weak_engine": dict(
        speed={"V": 0.95, "A": 0.80, "U": 0.70},
        p_miss=0.06,
        late_find=0.6, rework=0.5, rai_months=(2, 5), sigma=0.28,
    ),
}

SAFETY = {"non_loca", "loca", "containment", "eq_profiles", "dose_ast", "core_design",
          "cont_mass_energy", "rcs_structural", "setpoints", "pra_update", "heat_sink_ccw_sw"}


def descendants(node):
    out, stack = set(), [node]
    while stack:
        n = stack.pop()
        for m, (_, _, _, deps) in GRAPH.items():
            if n in deps and m not in out:
                out.add(m)
                stack.append(m)
    return out


DESC = {n: descendants(n) for n in GRAPH}


def simulate(s, review_target=12.0):
    """One project: returns (analysis months, NRC review months, effort engineer-months)."""
    dur = {n: OVERLAP * GRAPH[n][1] * s["speed"][GRAPH[n][0]] * rng.lognormal(0, s["sigma"]) for n in ORDER}
    missed = {n for n in ORDER[1:] if rng.random() < s["p_miss"]}
    finish = {}
    for n in ORDER:
        start = max([finish[d] for d in GRAPH[n][3]] or [0.0])
        finish[n] = start + dur[n]
    base_end = finish["lar_package"]
    # Late discovery: each missed analysis starts when found, then its downstream redoes work.
    end = base_end
    extra_review = 0.0
    effort = sum(GRAPH[n][2] * s["speed"][GRAPH[n][0]] for n in ORDER)
    for n in missed:
        found = s["late_find"] * base_end
        redo = dur[n] + sum(s["rework"] * dur[m] for m in DESC[n])
        end = max(end, found + redo)
        effort += GRAPH[n][2] * 0.3 + sum(s["rework"] * GRAPH[m][2] for m in DESC[n])
        if n in SAFETY:
            extra_review += rng.uniform(*s["rai_months"])
    review = review_target * rng.lognormal(0, 0.2) + extra_review
    return end, review, effort


def first_outage_after(t, phase, cycle=18.0):
    """Months from analysis start to the first refuelling outage at or after t."""
    k = np.ceil((t - phase) / cycle)
    return phase + max(k, 0) * cycle


def project_value(kind, mw, hardware_lead, n=4000, price=85.0, cf=0.93):
    """Compare scenarios for one uprate. hardware_lead = months from analysis start to hardware
    on site (assumption per kind). Value = MW-months of output pulled earlier, at the PPA price."""
    review = {"EPU": 12.0, "SPU": 9.0, "MUR": 6.0}[kind]
    scale = {"EPU": 1.0, "SPU": 0.6, "MUR": 0.35}[kind]   # MUR/SPU scope is a subset (assumption)
    res = {}
    for name, s in SCENARIOS.items():
        online, analysis, effort = [], [], []
        for _ in range(n):
            a, r, e = simulate(s, review)
            a *= scale
            e *= scale
            phase = rng.uniform(0, 18)           # where the plant sits in its fuel cycle
            ready = max(a + r, hardware_lead)
            online.append(first_outage_after(ready, phase))
            analysis.append(a)
            effort.append(e)
        res[name] = dict(online=np.array(online), analysis=np.array(analysis), effort=np.array(effort))
    # Scenarios are compared by mean and percentiles (independent draws).
    mwh_per_mw_month = 730 * cf
    out = {"kind": kind, "MW": mw, "hardware_lead_months": hardware_lead}
    for name, r in res.items():
        out[name] = {
            "analysis_p50": round(float(np.median(r["analysis"])), 1),
            "analysis_p90": round(float(np.percentile(r["analysis"], 90)), 1),
            "online_p50_months": round(float(np.median(r["online"])), 1),
            "online_mean_months": round(float(r["online"].mean()), 1),
            "effort_eng_months": round(float(r["effort"].mean()), 0),
        }
    for name in ("impact_engine", "weak_engine"):
        gain = res["today"]["online"].mean() - res[name]["online"].mean()
        out[name]["months_earlier_mean"] = round(float(gain), 1)
        out[name]["value_$M"] = round(gain * mw * mwh_per_mw_month * price / 1e6, 1)
        out[name]["effort_saved_share"] = round(
            1 - res[name]["effort"].mean() / res["today"]["effort"].mean(), 2)
    return out


if __name__ == "__main__":
    cases = [
        # (kind, MW, hardware lead months)  -- hardware leads are assumptions
        ("MUR", 17, 12),     # LEFM install: hardware is quick, engineering + review bind
        ("SPU", 40, 18),
        ("EPU", 160, 24),    # pumps, heat exchangers; long-lead but under analysis+review
        ("EPU", 160, 42),    # new HP turbine / generator: hardware binds
    ]
    results = [project_value(*c) for c in cases]
    print(json.dumps(results, indent=1))
