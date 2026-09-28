"""
LOCKSTEP sub-model A: the plant's cooling tower and condenser carrying the data centre's heat.

Counterflow evaporative cooling tower (Merkel method), surface condenser, LP-turbine exhaust
correction from steam tables, synthetic hourly wet-bulb year. Answers: how much plant output is
lost when the tower also rejects the data centre's heat, what water temperature the data centre
receives, and what extra tower capacity would make the plant whole.
"""
from __future__ import annotations
import json, math
import numpy as np
from scipy.optimize import brentq
from iapws import IAPWS97

CP = 4186.0
P_ATM = 101325.0

# ---------------------------------------------------------------- moist air
def psat_air(T):
    """Saturation pressure of water vapour over liquid, Pa (Magnus)."""
    return 610.94 * math.exp(17.625 * T / (T + 243.04))

def h_sat(T):
    """Enthalpy of saturated air at T (C), J/kg dry air."""
    w = 0.622 * psat_air(T) / (P_ATM - psat_air(T))
    return 1006.0 * T + w * (2501e3 + 1860.0 * T)

def h_wetbulb(T_wb):
    return h_sat(T_wb)

# ---------------------------------------------------------------- Merkel
def merkel(T_cold, T_hot, h_in, LG, n=60):
    """Merkel number KaV/L required for water cooled T_hot -> T_cold against air entering at h_in
    (J/kg) with water/air mass ratio LG. Chebyshev-free simple midpoint quadrature."""
    Ts = np.linspace(T_cold, T_hot, n + 1)
    Tm = 0.5 * (Ts[1:] + Ts[:-1])
    h_air = h_in + CP * (Tm - T_cold) / LG          # air enthalpy along the fill (counterflow)
    hs = np.array([h_sat(t) for t in Tm])
    dT = Ts[1:] - Ts[:-1]
    return float(np.sum(CP * dT / np.maximum(hs - h_air, 1.0)))

class Tower:
    """Natural-draft counterflow tower sized at a design point; off-design solved for cold-water
    temperature with fixed water flow and an airflow that scales weakly with heat load (draft)."""
    def __init__(self, Q_design=2.0e9, T_wb_design=25.6, T_cold_design=31.0, range_design=11.0, LG_design=1.4, n_exp=0.6):
        self.Q_d, self.T_wb_d, self.T_c_d, self.R_d, self.LG_d, self.n = Q_design, T_wb_design, T_cold_design, range_design, LG_design, n_exp
        self.L = Q_design / (CP * range_design)            # water mass flow, kg/s
        self.G_d = self.L / LG_design
        self.Me_d = merkel(T_cold_design, T_cold_design + range_design, h_wetbulb(T_wb_design), LG_design)
        # tower characteristic: KaV/L = c (L/G)^-n
        self.c = self.Me_d * LG_design ** n_exp

    def airflow(self, Q):
        """Natural draft: air mass flow scales with (heat load)^(1/3) around design (buoyancy ~ Q, flow ~ dp^0.5 ~ Q^0.5 with density feedback; 1/3 is a conservative middle)."""
        return self.G_d * (Q / self.Q_d) ** (1.0 / 3.0)

    def cold_water(self, Q, T_wb):
        """Solve cold-water temperature for heat load Q (W) at ambient wet-bulb T_wb."""
        R = Q / (CP * self.L)
        G = self.airflow(Q)
        LG = self.L / G
        Me_avail = self.c * LG ** (-self.n)
        f = lambda Tc: merkel(Tc, Tc + R, h_wetbulb(T_wb), LG) - Me_avail
        return brentq(f, T_wb + 0.3, T_wb + 40.0), R

# ---------------------------------------------------------------- condenser + turbine
class Condenser:
    def __init__(self, Q_design=2.0e9, T_cw_in_design=31.0, range_design=11.0, TTD_design=3.0):
        self.NTU = math.log((range_design + TTD_design) / TTD_design)
        self.Q_d = Q_design
    def T_sat(self, T_in, R):
        return T_in + R / (1 - math.exp(-self.NTU))

def lp_work(p_exh_MPa, eta=0.88, P_in=1.0, T_in=250.0):
    st = IAPWS97(P=P_in, T=T_in + 273.15)
    s_out = IAPWS97(P=p_exh_MPa, s=st.s)
    return eta * (st.h - s_out.h)

class Plant:
    """1,156 MWe PWR: LP exhaust correction and house/DC accounting."""
    def __init__(self, P_gross=1180.0, lp_flow=1050.0, T_cond_design=None):
        self.P_gross, self.lp_flow = P_gross, lp_flow
        self.w_d = None
    def output(self, T_sat):
        p = IAPWS97(T=T_sat + 273.15, x=0.0).P
        w = lp_work(p)
        if self.w_d is None:
            self.w_d = w
        return self.P_gross + self.lp_flow * (w - self.w_d) / 1e3 * 0.98   # MW (generator eff.)

# ---------------------------------------------------------------- climate
def wetbulb_year(mean=12.0, seasonal=11.0, daily=3.0, seed=1):
    rng = np.random.default_rng(seed)
    t = np.arange(8760)
    day = t / 24.0
    T = mean - seasonal * np.cos(2 * math.pi * (day - 20) / 365.25) + daily * np.sin(2 * math.pi * (t % 24 - 9) / 24.0)
    T += rng.normal(0, 2.0, size=8760)
    return np.clip(T, -15, 29)

# ---------------------------------------------------------------- study
def run(dc_loads=(0, 250, 500, 750), tower_scale=(1.0, 1.25), dc_pump_frac=0.02, hx_pinch=2.0):
    Twb = wetbulb_year()
    results = {}
    for scale in tower_scale:
        tw = Tower(Q_design=2.0e9 * scale)
        tw.L = Tower().L                   # same circulating-water flow as the reference plant
        tw.G_d = Tower().G_d * scale       # extra cells add air, fill and plan area
        cond = Condenser()
        pl = Plant()
        # establish the design LP work reference at the design condenser temperature
        Tc0, R0 = Tower().cold_water(2.0e9, 25.6)
        pl.output(cond.T_sat(Tc0, R0))
        print(f"reference condenser saturation at design day: {cond.T_sat(Tc0, R0):.1f} C")
        for dc in dc_loads:
            Q_dc = dc * 1e6 * (1 + dc_pump_frac)
            out = np.zeros(8760); Tcold = np.zeros(8760); Tsat = np.zeros(8760)
            R_plant = 2.0e9 / (CP * tw.L)          # condenser range: plant heat only; DC heat joins the hot return downstream
            for i, twb in enumerate(Twb):
                Q = 2.0e9 + Q_dc
                Tc, R = tw.cold_water(Q, twb)
                Ts = cond.T_sat(Tc, R_plant)
                out[i] = pl.output(Ts); Tcold[i] = Tc; Tsat[i] = Ts
            results[(scale, dc)] = dict(MWe_mean=float(out.mean()), MWe_min=float(out.min()), MWh_year=float(out.sum()),
                                        Tcold_mean=float(Tcold.mean()), Tcold_max=float(Tcold.max()), Tcold_p99=float(np.percentile(Tcold, 99)),
                                        Tsat_max=float(Tsat.max()), dc_supply_max=float(Tcold.max() + hx_pinch), dc_supply_p99=float(np.percentile(Tcold, 99) + hx_pinch),
                                        hours_supply_above_40=int(np.sum(Tcold + hx_pinch > 40.0)), hours_supply_above_35=int(np.sum(Tcold + hx_pinch > 35.0)))
    return results, Twb

if __name__ == "__main__":
    tw = Tower()
    print(f"Tower design: L={tw.L:.0f} kg/s water, G={tw.G_d:.0f} kg/s air, Me_design={tw.Me_d:.3f}")
    for twb in (5, 15, 25.6, 28):
        Tc, R = tw.cold_water(2.0e9, twb)
        print(f"  Q=2.0 GW T_wb={twb:5.1f}: cold water {Tc:5.1f} C, approach {Tc-twb:4.1f} K")
    for Qdc in (0, 250e6, 500e6, 750e6):
        Tc, R = tw.cold_water(2.0e9 + Qdc, 25.6)
        print(f"  design wet-bulb, DC {Qdc/1e6:4.0f} MW: cold water {Tc:5.1f} C, tower range {R:4.1f} K, condenser sat {Condenser().T_sat(Tc, 2.0e9/(CP*tw.L)):5.1f} C")
    res, Twb = run()
    base = res[(1.0, 0)]
    out = {}
    for (scale, dc), r in sorted(res.items()):
        loss = base["MWh_year"] - r["MWh_year"]
        key = f"scale{scale}_dc{dc}"
        out[key] = dict(r, tower_scale=scale, dc_MW=dc, MWh_lost_vs_base=loss, MW_avg_lost=loss / 8760)
        print(f"tower x{scale:.2f}, DC {dc:3d} MW: mean {r['MWe_mean']:.1f} MWe (min {r['MWe_min']:.1f}), lost {loss/8760:6.1f} MW avg, {loss/1e3:7.1f} GWh/yr; cold water max {r['Tcold_max']:.1f} C, DC supply p99 {r['dc_supply_p99']:.1f} C, hours >40 C: {r['hours_supply_above_40']}")
    json.dump(dict(cases=out, Twb_mean=float(Twb.mean()), Twb_max=float(Twb.max())), open("runs/tower.json", "w"), indent=1)
    np.save("runs/Twb.npy", Twb)
