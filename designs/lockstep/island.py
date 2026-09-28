"""
LOCKSTEP sub-model B: a PWR riding through loss of the grid by islanding onto the co-located
data centre plus its own house load, with no reactor trip.

Reduced-order plant model of the kind used for load-rejection screening:
  - point kinetics, 6 delayed groups, Doppler and moderator feedback, control rods, Xe-135/I-135
  - lumped fuel, core coolant (hot leg), SG primary node, cold leg; SG secondary saturated node
  - pressuriser as a compressible volume with spray, PORV and heaters
  - turbine (HP prompt, LP through reheater lag), generator swing equation
  - governor: droop plus slow frequency restoration in island; fast valving on load rejection
  - steam dump on power mismatch and on Tavg error; rod control on Tavg - Tref(load) with runback
  - loads: grid (infinite bus) or island = data centre (constant power) + house load
  - trip checks: overspeed, under-frequency, pressuriser high/low, SG safety-valve lift,
    over-temperature proxy, overpower
"""
from __future__ import annotations
import json
import numpy as np
from scipy.integrate import solve_ivp
from iapws import IAPWS97

BETA = np.array([0.000215, 0.001424, 0.001274, 0.002568, 0.000748, 0.000273])
LAM = np.array([0.0124, 0.0305, 0.111, 0.301, 1.14, 3.01])
BETA_T = BETA.sum()
LAMBDA = 2.0e-5
ALPHA_F = -2.8e-5              # Δk/k per K fuel
ALPHA_M = -3.5e-4              # Δk/k per K coolant
ROD_MAX = 8.0e-5               # Δk/k per s
P0 = 3400.0                    # MWth
C_F = 20.0e6                   # J/K
UA_FC = P0 * 1e6 / 500.0       # W/K  (fuel average ~ 500 K above coolant at full power)
C_C = 60.0e6                   # J/K core coolant
M_DOT_CP = 17000.0 * 5500.0    # W/K
C_SGP = 60.0e6                 # J/K SG primary node
C_COLD = 60.0e6                # J/K cold leg node
T_SAT_D = 275.0                # C
UA_SG = P0 * 1e6 / 35.0        # W/K  (primary average 310 C vs 275 C)
C_SGS = 320.0e6                # J/K secondary water + metal, 4 SGs
H_FW = 977e3                   # J/kg feedwater 227 C
P_PZ0 = 15.5
K_PZ = 0.12                    # MPa per K Tavg
P_SPRAY, P_PORV, P_HI_TRIP, P_LO_TRIP = 15.7, 16.2, 16.7, 13.0
H = 5.5; S_BASE = 1300.0; P_E_RATED = 1180.0
TAU_RH = 8.0; F_HP = 0.35; HOUSE = 60.0; DUMP_CAP = 0.40
GAMMA_I, GAMMA_X, LAM_I, LAM_X, SIG_PHI0 = 0.0639, 0.00237, 2.87e-5, 2.09e-5, 8.0e-5
XE_WORTH = -0.028
I0 = GAMMA_I / LAM_I
X0 = (GAMMA_X + LAM_I * I0) / (LAM_X + SIG_PHI0)

_psat_cache = {}
def psat(T):
    k = round(T, 3)
    if k not in _psat_cache:
        _psat_cache[k] = IAPWS97(T=T + 273.15, x=0.0).P
    return _psat_cache[k]
_hg_cache = {}
def hg(P):
    k = round(P, 4)
    if k not in _hg_cache:
        _hg_cache[k] = IAPWS97(P=P, x=1.0).h * 1e3
    return _hg_cache[k]
PSAT_D = psat(T_SAT_D)

class Case:
    def __init__(self, mode="island", dc_load=520.0, t_event=10.0, dc_step=None, runback=True, dump_cap=DUMP_CAP,
                 fast_valve=True, t_end=1800.0, max_step=0.5):
        self.__dict__.update(locals()); del self.__dict__["self"]

def tref(P_frac):
    return 292.0 + 16.0 * P_frac

def rhs(t, y, c: Case, ref):
    n = y[0]; C = y[1:7]; Tf, Th, Tc, Tsgp, Tsgs, P_pz, rho_rod, omega, P_lp, valve, dump, I_n, X_n = y[7:20]
    islanded = (c.mode == "island") and t >= c.t_event
    dc = c.dc_load + (c.dc_step[1] if (c.dc_step and t >= c.dc_step[0]) else 0.0)
    P_e = dc + HOUSE                                    # island load, MWe (constant power)
    # steam and turbine
    p_sg = psat(Tsgs)
    m_frac = valve * p_sg / PSAT_D
    P_t = P_E_RATED * m_frac
    P_mech = F_HP * P_t + P_lp
    dP_lp = ((1 - F_HP) * P_t - P_lp) / TAU_RH
    m_dump = dump * p_sg / PSAT_D
    # generator
    domega = (P_mech - P_e) / (2 * H * S_BASE) if islanded else 0.0
    # governor
    if islanded:
        target = P_e / P_E_RATED - (omega - 1.0) / 0.04
        rate = 3.0 if c.fast_valve else 0.3
        dvalve = float(np.clip((target - valve) * 20.0 - (omega - 1.0) * 5.0, -rate, rate))
    else:
        dvalve = 0.0
    # thermal
    P_th = n * P0
    Tavg = 0.5 * (Th + Tc)
    Q_fc = UA_FC * (Tf - Tavg)
    dTf = (P_th * 1e6 - Q_fc) / C_F
    dTh = (Q_fc - M_DOT_CP * (Th - Tc)) / C_C
    Q_sg = UA_SG * (0.5 * (Th + Tsgp) - Tsgs)
    dTsgp = (M_DOT_CP * (Th - Tsgp) - Q_sg) / C_SGP
    dTc = M_DOT_CP * (Tsgp - Tc) / C_COLD
    hs = hg(p_sg)
    m_steam = (m_frac + m_dump) * P0 * 1e6 / (hs - H_FW)
    dTsgs = (Q_sg - m_steam * (hs - H_FW)) / C_SGS
    # pressuriser
    dP = K_PZ * 0.5 * (dTh + dTc)
    if P_pz > P_SPRAY: dP -= 0.05 * (P_pz - P_SPRAY)
    if P_pz > P_PORV: dP -= 0.5 * (P_pz - P_PORV)
    if P_pz < P_PZ0 - 0.2: dP += 0.02 * (P_PZ0 - 0.2 - P_pz)
    # rods
    err = Tavg - tref(m_frac)
    rod_rate = 0.0 if abs(err) < 0.8 else -np.sign(err) * min(ROD_MAX, ROD_MAX * (abs(err) - 0.8) / 2.0)
    if islanded and c.runback and (t - c.t_event) < 150.0 and n > (P_e / P_E_RATED) * 1.05:
        rod_rate = -ROD_MAX
    # steam dump: power mismatch (load-rejection controller) and Tavg error
    if islanded:
        dump_target = max(np.clip(n - m_frac - 0.02, 0.0, 1.0), np.clip((err - 2.0) / 8.0, 0.0, 1.0)) * c.dump_cap
    else:
        dump_target = 0.0
    ddump = float(np.clip((dump_target - dump) * 2.0, -2.0, 2.0))
    # xenon (normalised)
    dI_n = LAM_I * (n - I_n)
    dX_n = (GAMMA_X * n + LAM_I * I0 * I_n - LAM_X * X0 * X_n - SIG_PHI0 * n * X0 * X_n) / X0
    rho_xe = XE_WORTH * (X_n - 1.0)
    rho = rho_rod + ALPHA_F * (Tf - ref["Tf0"]) + ALPHA_M * (Tavg - ref["Tavg0"]) + rho_xe
    dn = (rho - BETA_T) / LAMBDA * n + float(np.sum(LAM * C))
    dC = BETA / LAMBDA * n - LAM * C
    return [dn, *dC, dTf, dTh, dTc, dTsgp, dTsgs, dP, rod_rate, domega, dP_lp, dvalve, ddump, dI_n, dX_n]

def initial_state():
    n = 1.0
    C = BETA / (LAMBDA * LAM) * n
    Tsgs = T_SAT_D
    # steady state: Tc = Tsgp; Th = Tc + P0/mcp; Q_sg = UA (0.5(Th+Tsgp) - Tsgs) = P0
    dT_loop = P0 * 1e6 / M_DOT_CP
    Tsgp = Tsgs + P0 * 1e6 / UA_SG - 0.5 * dT_loop
    Tc = Tsgp; Th = Tc + dT_loop
    Tavg = 0.5 * (Th + Tc)
    Tf = Tavg + P0 * 1e6 / UA_FC
    y0 = [n, *C, Tf, Th, Tc, Tsgp, Tsgs, P_PZ0, 0.0, 1.0, (1 - F_HP) * P_E_RATED, 1.0, 0.0, 1.0, 1.0]
    return y0, dict(Tf0=Tf, Tavg0=Tavg, Th0=Th, Tc0=Tc)

def simulate(c: Case):
    y0, ref = initial_state()
    sol = solve_ivp(lambda t, y: rhs(t, y, c, ref), [0, c.t_end], y0, method="BDF", max_step=c.max_step, rtol=1e-6, atol=1e-9)
    return sol, ref

def diagnostics(sol):
    t, y = sol.t, sol.y
    n = y[0]; Tf = y[7]; Th = y[8]; Tc = y[9]; Tsgs = y[11]; P_pz = y[12]; rho_rod = y[13]; omega = y[14]; P_lp = y[15]; valve = y[16]; dump = y[17]; X = y[19]
    Tavg = 0.5 * (Th + Tc)
    p_sg = np.array([psat(T) for T in Tsgs])
    m_frac = valve * p_sg / PSAT_D
    P_mech = F_HP * P_E_RATED * m_frac + P_lp
    freq = 60.0 * omega
    # Over-temperature and over-power ΔT trips (Westinghouse form): core ΔT vs setpoint depending on Tavg and pressure
    dT0 = P0 * 1e6 / M_DOT_CP
    dT_core = Th - Tc
    otdt_set = dT0 * (1.18 - 0.022 * (Tavg - 310.0) + 0.10 * (P_pz - P_PZ0))
    opdt_set = dT0 * (1.08 - 0.002 * np.maximum(Tavg - 310.0, 0.0))
    trips = dict(overspeed_66Hz=bool(np.any(freq > 66.0)), underfreq_57Hz=bool(np.any(freq < 57.0)),
                 pressuriser_high_16_7=bool(np.any(P_pz > P_HI_TRIP)), pressuriser_low_13_0=bool(np.any(P_pz < P_LO_TRIP)),
                 SG_safety_valves_8_3MPa=bool(np.any(p_sg > 8.3)), OTdT=bool(np.any(dT_core > otdt_set)), OPdT=bool(np.any(dT_core > opdt_set)),
                 overpower_118=bool(np.any(n > 1.18)))
    otdt_margin = float(np.min(otdt_set - dT_core))
    return dict(t=t, n=n, Tf=Tf, Tavg=Tavg, Th=Th, Tc=Tc, Tsgs=Tsgs, p_sg=p_sg, P_pz=P_pz, rho_rod=rho_rod, freq=freq, P_mech=P_mech, valve=valve, dump=dump, X=X, m_frac=m_frac,
                trips=trips, any_trip=any(trips.values()), freq_max=float(freq.max()), freq_min=float(freq.min()), Tavg_max=float(Tavg.max()), Tavg_min=float(Tavg.min()),
                P_pz_max=float(P_pz.max()), P_pz_min=float(P_pz.min()), p_sg_max=float(p_sg.max()), n_min=float(n.min()), n_end=float(n[-1]), dump_max=float(dump.max()), otdt_margin_K=otdt_margin, PORV_lift=bool(np.any(P_pz > P_PORV)))

CASES = {
    "island_520": Case(dc_load=520.0),
    "island_520_step_plus100": Case(dc_load=520.0, dc_step=(600.0, 100.0)),
    "island_520_step_minus200": Case(dc_load=520.0, dc_step=(600.0, -200.0)),
    "island_300": Case(dc_load=300.0),
    "island_150": Case(dc_load=150.0),
    "island_house_only": Case(dc_load=0.0),
    "island_520_slow_valving": Case(dc_load=520.0, fast_valve=False),
    "island_520_dump_25pct": Case(dc_load=520.0, dump_cap=0.25),
    "island_520_no_runback": Case(dc_load=520.0, runback=False),
    "island_520_24h": Case(dc_load=520.0, t_end=24 * 3600.0, max_step=5.0),
    "island_350": Case(dc_load=350.0),
    "island_400": Case(dc_load=400.0),
    "island_450": Case(dc_load=450.0),
    "island_600": Case(dc_load=600.0),
    "island_700": Case(dc_load=700.0),
    "island_520_dump50": Case(dc_load=520.0, dump_cap=0.50),
    "island_400_dump50": Case(dc_load=400.0, dump_cap=0.50),
    "island_300_dump50": Case(dc_load=300.0, dump_cap=0.50),
    "island_520_dump60": Case(dc_load=520.0, dump_cap=0.60),
}

if __name__ == "__main__":
    summary = {}
    for name, c in CASES.items():
        sol, ref = simulate(c)
        d = diagnostics(sol)
        summary[name] = {k: v for k, v in d.items() if not isinstance(v, np.ndarray)}
        flags = ", ".join(k for k, v in d["trips"].items() if v)
        print(f"{name:28s} trip={str(d['any_trip']):5} f[{d['freq_min']:.2f},{d['freq_max']:.2f}]Hz Tavg[{d['Tavg_min']:.1f},{d['Tavg_max']:.1f}] P_pz[{d['P_pz_min']:.2f},{d['P_pz_max']:.2f}] p_sg_max {d['p_sg_max']:.2f} n_min {d['n_min']:.3f} n_end {d['n_end']:.3f} OTdT margin {d['otdt_margin_K']:.1f} K PORV {d['PORV_lift']}  {flags}", flush=True)
        np.savez(f"runs/island_{name}.npz", **{k: v for k, v in d.items() if isinstance(v, np.ndarray)})
    json.dump(summary, open("runs/island.json", "w"), indent=1)
