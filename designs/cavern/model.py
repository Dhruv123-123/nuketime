"""
CAVERN: two lined rock caverns of pressurised hot water as a daily peaking store for a
light-water reactor.

  charge   : extraction steam from the main turbine heats water from the warm cavern to the
             hot cavern in a cascade of closed feed heaters (each stage draws steam at the
             lowest pressure that can do its job), plus heating of make-up water.
  store    : two caverns at constant temperature (hot T_h, warm T_w); only levels move, so
             the liners see steady pressure and steady temperature.
  discharge: hot water flashes in M stages; the steam from each stage enters a dedicated
             peaking turbine at that pressure. Residual water returns to the warm cavern.

Everything is computed from IAPWS-97 steam properties. SI unless noted.
"""
from __future__ import annotations
import json, math, sys
import numpy as np
from iapws import IAPWS97

P_COND = 0.005          # condenser pressure, MPa
ETA_HP, ETA_LP = 0.85, 0.88
P_MSR = 1.1             # moisture separator / crossover pressure, MPa
T_RH = 250.0            # reheat temperature after MSR, C (heated by live steam)

def sat(P=None, T=None, x=0.0):
    return IAPWS97(P=P, x=x) if P is not None else IAPWS97(T=T + 273.15, x=x)

def expand(h1, s1, P1, P2, eta):
    """Expand from (h1,s1) at P1 to P2 with isentropic efficiency; returns (h2, state)."""
    st_s = IAPWS97(P=P2, s=s1)
    h2 = h1 - eta * (h1 - st_s.h)
    return h2, IAPWS97(P=P2, h=h2)

# --------------------------------------------------------------------------- main turbine
class MainCycle:
    """Saturated-steam PWR turbine: HP to P_MSR, moisture separation, live-steam reheat to T_RH,
    LP to condenser. Gives the work lost when steam is taken from the expansion line."""
    def __init__(self, P_main=6.9):
        self.P_main = P_main
        live = sat(P=P_main, x=1.0)
        self.h_live, self.s_live = live.h, live.s
        # HP expansion
        h_hp, st_hp = expand(live.h, live.s, P_main, P_MSR, ETA_HP)
        self.h_hp_out, self.x_hp_out = h_hp, st_hp.x
        # moisture separation: liquid drained (returned to feed train), vapour reheated
        vap = sat(P=P_MSR, x=1.0)
        rh = IAPWS97(P=P_MSR, T=T_RH + 273.15)
        self.q_reheat_per_kg_vap = rh.h - vap.h
        self.h_rh, self.s_rh = rh.h, rh.s
        # reheat steam: live steam condensing at P_main -> drains at saturation
        self.h_fg_live = live.h - sat(P=P_main, x=0.0).h
        # LP expansion
        h_lp, st_lp = expand(rh.h, rh.s, P_MSR, P_COND, ETA_LP)
        self.h_lp_out, self.x_lp_out = h_lp, st_lp.x
        # work per kg live steam admitted at the throttle (net of reheat steam consumption)
        self.w_lp_per_kg_rh = rh.h - h_lp
        self.w_hp_per_kg = live.h - h_hp
        # 1 kg live -> HP -> x_hp kg vapour -> reheat needs m_r = x_hp q_rh / h_fg_live kg live steam
        # which itself would have produced W_live (recursive). Solve W_live = w_hp + x w_lp - m_r W_live.
        m_r = self.x_hp_out * self.q_reheat_per_kg_vap / self.h_fg_live
        self.W_live = (self.w_hp_per_kg + self.x_hp_out * self.w_lp_per_kg_rh) / (1 + m_r)
        self.m_reheat_per_kg_live = m_r
        self.eta_cycle_est = None

    def state_on_line(self, P):
        """Enthalpy and entropy of steam on the main expansion line at pressure P (MPa)."""
        if P >= self.P_main:
            return self.h_live, self.s_live
        if P > P_MSR:
            h, st = expand(self.h_live, self.s_live, self.P_main, P, ETA_HP)
            return h, st.s
        h, st = expand(self.h_rh, self.s_rh, P_MSR, P, ETA_LP)
        return h, st.s

    def work_remaining(self, P):
        """Work (kJ/kg) that 1 kg of steam on the expansion line at P would still produce."""
        if P >= self.P_main:
            return self.W_live
        if P > P_MSR:
            h, s = self.state_on_line(P)
            h2, st2 = expand(h, s, P, P_MSR, ETA_HP)
            x = st2.x
            m_r = x * self.q_reheat_per_kg_vap / self.h_fg_live
            return (h - h2) + x * self.w_lp_per_kg_rh - m_r * self.W_live
        h, s = self.state_on_line(P)
        h2, _ = expand(h, s, P, P_COND, ETA_LP)
        return h - h2

# --------------------------------------------------------------------------- peaking turbine
def peaker_work(P_adm, eta=0.85, P_sep=1.0):
    """Work (kJ/kg) of saturated steam admitted at P_adm to a wet-steam peaking turbine with a
    moisture separator at P_sep (no reheat) and exhaust at P_COND."""
    v = sat(P=P_adm, x=1.0)
    if P_adm > P_sep:
        h2, st2 = expand(v.h, v.s, P_adm, P_sep, eta)
        x = st2.x
        v2 = sat(P=P_sep, x=1.0)
        h3, _ = expand(v2.h, v2.s, P_sep, P_COND, eta)
        return (v.h - h2) + x * (v2.h - h3)
    h2, _ = expand(v.h, v.s, P_adm, P_COND, eta)
    return v.h - h2

# --------------------------------------------------------------------------- store
class Store:
    def __init__(self, T_h=250.0, T_w=160.0, n_charge=4, n_flash=3, dT_pinch=5.0,
                 T_feed=33.0, P_main=6.9, T_makeup_src=33.0):
        self.T_h, self.T_w, self.n_charge, self.n_flash, self.dT_pinch = T_h, T_w, n_charge, n_flash, dT_pinch
        self.mc = MainCycle(P_main)
        self.P_h, self.P_w = sat(T=T_h).P, sat(T=T_w).P
        self.h_h, self.h_w = sat(T=T_h).h, sat(T=T_w).h
        self.rho_h, self.rho_w = sat(T=T_h).rho, sat(T=T_w).rho
        self.T_feed = T_feed
        self.h_feed = IAPWS97(P=self.P_w + 0.5, T=T_feed + 273.15).h
        self._charge(); self._discharge()

    # charge: heat 1 kg of store water T_w -> T_h in n stages with extraction steam
    def _charge(self):
        Ts = np.linspace(self.T_w, self.T_h, self.n_charge + 1)
        self.charge_stages, W_lost, Q = [], 0.0, 0.0
        for a, b in zip(Ts[:-1], Ts[1:]):
            P_ext = sat(T=b + self.dT_pinch).P
            P_ext = min(P_ext, self.mc.P_main)
            h_ext, _ = self.mc.state_on_line(P_ext)
            h_drain = sat(P=P_ext, x=0.0).h
            q = sat(T=b).h - sat(T=a).h
            m = q / (h_ext - h_drain)
            w = m * self.mc.work_remaining(P_ext)
            self.charge_stages.append(dict(T_in=a, T_out=b, P_ext=P_ext, m_steam=m, w_lost=w, q=q))
            W_lost += w; Q += q
        self.Q_charge_per_kg, self.W_lost_per_kg = Q, W_lost       # kJ per kg of store water
        # make-up: the water flashed off during discharge must be replaced; heat it T_feed -> T_w
        # at charge time with the same cascade.
        Ts = np.linspace(self.T_feed, self.T_w, self.n_charge + 1)
        Wm, Qm = 0.0, 0.0
        for a, b in zip(Ts[:-1], Ts[1:]):
            P_ext = min(sat(T=b + self.dT_pinch).P, self.mc.P_main)
            P_ext = max(P_ext, 0.006)
            h_ext, _ = self.mc.state_on_line(P_ext)
            h_drain = sat(P=P_ext, x=0.0).h
            q = sat(T=b).h - (sat(T=a).h if a > 34 else self.h_feed)
            m = q / (h_ext - h_drain)
            Wm += m * self.mc.work_remaining(P_ext); Qm += q
        self.W_lost_makeup_per_kg, self.Q_makeup_per_kg = Wm, Qm    # per kg of make-up water

    # discharge: flash 1 kg of hot water in n_flash stages down to T_w
    def _discharge(self):
        Ts = np.linspace(self.T_h, self.T_w, self.n_flash + 1)[1:]
        m_liq, W, self.flash_stages = 1.0, 0.0, []
        for T in Ts:
            P = sat(T=T).P
            hf, hg = sat(P=P, x=0.0).h, sat(P=P, x=1.0).h
            h_in = sat(T=self.flash_stages[-1]["T"]).h if self.flash_stages else self.h_h
            x = (h_in - hf) / (hg - hf)
            m_s = m_liq * x
            w = m_s * peaker_work(P)
            self.flash_stages.append(dict(T=T, P=P, m_steam=m_s, w=w))
            W += w; m_liq -= m_s
        self.W_peak_per_kg = W                    # kJ_e per kg of hot water
        self.m_flashed_per_kg = 1.0 - m_liq       # kg steam per kg hot water (needs make-up)
        self.Q_discharge_per_kg = self.h_h - m_liq * self.h_w - self.m_flashed_per_kg * self.h_feed  # not used

    def round_trip(self):
        W_in = self.W_lost_per_kg + self.m_flashed_per_kg * self.W_lost_makeup_per_kg
        return self.W_peak_per_kg / W_in, W_in, self.W_peak_per_kg

# --------------------------------------------------------------------------- rock
class Rock:
    def __init__(self, k=3.0, rhoc=2.3e6, T0=14.0, alpha_th=8e-6, E=40e9):
        self.k, self.rhoc, self.T0, self.alpha_th, self.E = k, rhoc, T0, alpha_th, E
        self.alpha = k / rhoc

    def sphere_loss(self, R, T_s, t):
        """Heat loss (W) from a sphere of radius R held at T_s in infinite rock at time t (s)."""
        dT = T_s - self.T0
        return 4 * math.pi * self.k * R * dT * (1 + R / math.sqrt(math.pi * self.alpha * t))

    def sphere_energy_loss(self, R, T_s, t):
        """Cumulative energy (J) lost to the rock by time t."""
        dT = T_s - self.T0
        return 4 * math.pi * self.k * R * dT * (t + 2 * R * math.sqrt(t / (math.pi * self.alpha)))

    def sphere_profile(self, R, T_s, t, r):
        from scipy.special import erfc
        r = np.asarray(r, dtype=float)
        dT = (T_s - self.T0) * (R / np.maximum(r, R)) * erfc((np.maximum(r, R) - R) / math.sqrt(4 * self.alpha * t))
        return self.T0 + dT

    def heave(self, R, T_s, t, depth_c):
        """Surface heave (m) above the cavern centre: vertical strain integral of the thermal
        expansion (free-expansion estimate, upper bound) along the axis above the sphere."""
        z = np.linspace(R, depth_c, 400)      # distance from centre up to the surface
        dT = self.sphere_profile(R, T_s, t, z) - self.T0
        return float(self.alpha_th * np.trapezoid(dT, z))

    def wall_temperature(self, R, T_s, t, R_ins):
        """Rock-wall temperature for a sphere at T_s behind an insulating layer of areal resistance
        R_ins (m2K/W): equates conduction through the layer with the sphere's transient rock conductance."""
        A = 4 * math.pi * R ** 2
        G_rock = 4 * math.pi * self.k * R * (1 + R / math.sqrt(math.pi * self.alpha * t))   # W/K
        G_ins = A / R_ins if R_ins > 0 else float("inf")
        return self.T0 + (T_s - self.T0) * G_rock ** -1 / (G_rock ** -1 + G_ins ** -1) if R_ins > 0 else T_s

    def thermal_stress(self, dT):
        """Free-thermal-expansion hoop stress estimate at a heated wall, MPa (upper bound)."""
        return self.alpha_th * self.E * dT / 1e6

    def uplift_sf(self, P, R, depth_top, rho=2700.0, half_angle_deg=30.0):
        """Safety factor against uplift of the rock cone above a cavern of radius R whose crown is
        at depth_top, internal pressure P (Pa). Simple rigid-cone check used in LRC screening."""
        H = depth_top
        r2 = R + H * math.tan(math.radians(half_angle_deg))
        V = math.pi * H / 3 * (R ** 2 + R * r2 + r2 ** 2)
        return V * rho * 9.81 / (P * math.pi * R ** 2)

# --------------------------------------------------------------------------- plant sizing
def size_plant(store: Store, P_th=3400e6, eta_plant=0.34, frac_charge=0.30, h_charge=6.0, h_discharge=4.0,
               cavern_D=30.0, days=330, price_mid=15.0, price_peak=160.0, capex_inputs=None):
    """Size caverns and peaker for a plant diverting frac_charge of its thermal power for h_charge
    hours per day; discharge over h_discharge hours."""
    mc = store.mc
    # steam-side energy diverted per day (thermal, kJ)
    Q_day = P_th * frac_charge * h_charge * 3600 / 1e3
    # store water mass cycled per day: charge heat per kg incl. make-up heating
    q_per_kg = store.Q_charge_per_kg + store.m_flashed_per_kg * store.Q_makeup_per_kg
    m_cycle = Q_day / q_per_kg                                  # kg of hot water made per day
    # electricity forgone during charge, produced at peak
    E_forgone = m_cycle * (store.W_lost_per_kg + store.m_flashed_per_kg * store.W_lost_makeup_per_kg) / 3.6e6  # MWh
    E_peak = m_cycle * store.W_peak_per_kg / 3.6e6                                                         # MWh
    P_peak = E_peak / h_discharge                                                                           # MW
    P_charge_drop = E_forgone / h_charge
    # cavern volumes (10 % ullage for steam cushion and level swing)
    V_hot = m_cycle / store.rho_h * 1.10
    V_warm = m_cycle * (1 - store.m_flashed_per_kg) / store.rho_w * 1.10 + m_cycle * store.m_flashed_per_kg / store.rho_w * 1.10
    H_hot = V_hot / (math.pi * (cavern_D / 2) ** 2)
    H_warm = V_warm / (math.pi * (cavern_D / 2) ** 2)
    # economics
    ci = dict(excavation=120.0, concrete_m3=800.0, concrete_t=1.5, liner_kg=12.0, liner_t=0.015, steel_rho=7850.0,
              insulation_m2=400.0, drainage_access=40e6, peaker_kw=450.0, bop_frac=0.25, contingency=0.30)
    if capex_inputs:
        ci.update(capex_inputs)
    def cavern_cost(V, H):
        A_wall = math.pi * cavern_D * H + 2 * math.pi * (cavern_D / 2) ** 2
        return (V * ci["excavation"] + A_wall * ci["concrete_t"] * ci["concrete_m3"]
                + A_wall * ci["liner_t"] * ci["steel_rho"] * ci["liner_kg"] + A_wall * ci["insulation_m2"])
    C_cav = cavern_cost(V_hot, H_hot) + cavern_cost(V_warm, H_warm) + ci["drainage_access"]
    C_peaker = P_peak * 1e3 * ci["peaker_kw"]
    C_direct = (C_cav + C_peaker) * (1 + ci["bop_frac"])
    C_total = C_direct * (1 + ci["contingency"])
    rev_day = E_peak * price_peak - E_forgone * price_mid
    rev_year = rev_day * days
    return dict(Q_day_MWh_th=Q_day / 3.6e6, m_cycle_t=m_cycle / 1e3, E_forgone_MWh=E_forgone, E_peak_MWh=E_peak,
                P_peak_MW=P_peak, P_charge_drop_MW=P_charge_drop, V_hot_m3=V_hot, V_warm_m3=V_warm,
                H_hot_m=H_hot, H_warm_m=H_warm, capex_caverns_M=C_cav / 1e6, capex_peaker_M=C_peaker / 1e6,
                capex_total_M=C_total / 1e6, capex_per_kWh_e=C_total / (E_peak * 1e3), capex_per_kW_peak=C_total / (P_peak * 1e3),
                revenue_M_per_yr=rev_year / 1e6, payback_yr=C_total / rev_year if rev_year > 0 else None)


if __name__ == "__main__":
    mc = MainCycle()
    print(f"Main cycle: W_live={mc.W_live:.1f} kJ/kg, x_hp_out={mc.x_hp_out:.3f}, x_lp_out={mc.x_lp_out:.3f}, reheat live steam {mc.m_reheat_per_kg_live:.3f} kg/kg")
    print("work remaining on line at P:", {P: round(mc.work_remaining(P), 1) for P in (6.9, 4.0, 3.0, 2.0, 1.5, 1.1, 0.8, 0.5, 0.2, 0.05)})
    print("peaker work sat steam at P:", {P: round(peaker_work(P), 1) for P in (4.0, 3.0, 2.0, 1.5, 1.0, 0.6, 0.3)})
    print("\nRound trip vs temperatures (n_charge=4, n_flash=3):")
    for Th in (200, 220, 240, 250, 260, 270, 280):
        row = []
        for Tw in (120, 140, 160, 180):
            if Tw >= Th - 30: row.append("   -  "); continue
            s = Store(T_h=Th, T_w=Tw)
            rt, win, wout = s.round_trip()
            row.append(f"{rt*100:5.1f}%")
        print(f"  T_h={Th}: " + "  ".join(row) + "   (T_w = 120,140,160,180)")
    s = Store(T_h=250, T_w=160)
    rt, win, wout = s.round_trip()
    print(f"\nDesign point T_h=250 T_w=160: RT={rt*100:.1f}%  W_in={win:.1f} kJ_e/kg  W_out={wout:.1f} kJ_e/kg  flashed={s.m_flashed_per_kg:.3f} kg/kg  Q_charge={s.Q_charge_per_kg:.0f} kJ/kg")
    print("charge stages:", [(round(c['T_out']), round(c['P_ext'], 2), round(c['m_steam'], 4)) for c in s.charge_stages])
    print("flash stages:", [(round(f['T']), round(f['P'], 2), round(f['m_steam'], 4)) for f in s.flash_stages])
    print("\nstages sensitivity (n_charge, n_flash):", {(nc, nf): round(Store(250, 160, nc, nf).round_trip()[0] * 100, 1) for nc in (1, 2, 4, 8) for nf in (1, 2, 3, 5)})
    # ---- design scan: pick T_h, T_w, stages, discharge hours by payback
    print("\nDesign scan (1,100 MWe PWR, 30% of thermal power for 6 h; payback years / RT / capex $M / peaker MW):")
    best = None
    for Th in (220, 235, 250, 265, 280):
        for Tw in (140, 160, 180):
            st = Store(T_h=Th, T_w=Tw, n_charge=6, n_flash=4)
            for hd in (4.0, 5.0, 6.0):
                pl = size_plant(st, h_discharge=hd)
                rt = st.round_trip()[0]
                if best is None or pl["payback_yr"] < best[0]:
                    best = (pl["payback_yr"], Th, Tw, hd)
                print(f"  T_h={Th} T_w={Tw} h_dis={hd:.0f}: payback {pl['payback_yr']:.2f} y  RT {rt*100:.1f}%  capex ${pl['capex_total_M']:.0f}M  peaker {pl['P_peak_MW']:.0f} MW  V_hot {pl['V_hot_m3']/1e3:.0f} km3e-3")
    print("best:", best)
    Th, Tw, hd = 235, 160, 5.0
    s = Store(T_h=Th, T_w=Tw, n_charge=6, n_flash=4)
    rt, win, wout = s.round_trip()
    plant = size_plant(s, h_discharge=hd)
    print(f"\nDESIGN POINT T_h={Th} T_w={Tw}, 6 charge stages, 4 flash stages, {hd:.0f} h discharge: RT={rt*100:.1f}%")
    print("charge stages:", [(round(c['T_out']), round(float(c['P_ext']), 2), round(float(c['m_steam']), 4)) for c in s.charge_stages])
    print("flash stages:", [(round(f['T']), round(float(f['P']), 2), round(float(f['m_steam']), 4)) for f in s.flash_stages])
    print(json.dumps({k: (round(float(v), 3) if v is not None else None) for k, v in plant.items()}, indent=1))
    rock = Rock()
    R_eq = (3 * plant["V_hot_m3"] / (4 * math.pi)) ** (1 / 3)
    yr = 365.25 * 86400
    out = dict(design=dict(T_h=Th, T_w=Tw, P_h=float(s.P_h), P_w=float(s.P_w), n_charge=6, n_flash=4, h_discharge=hd, RT=rt,
                           W_in_kJ_per_kg=win, W_out_kJ_per_kg=wout, m_flashed=s.m_flashed_per_kg, Q_charge_kJ_per_kg=s.Q_charge_per_kg,
                           charge_stages=[{k: float(v) for k, v in c.items()} for c in s.charge_stages],
                           flash_stages=[{k: float(v) for k, v in f.items()} for f in s.flash_stages]),
               plant={k: (float(v) if v is not None else None) for k, v in plant.items()}, rock={})
    for label, R_ins in (("no insulation", 0.0), ("0.5 m foam concrete k=0.3", 0.5 / 0.3), ("1.0 m k=0.15", 1.0 / 0.15)):
        tw = {t: rock.wall_temperature(R_eq, Th, t * yr, R_ins) for t in (1, 5, 30)}
        print(f"Rock wall temperature ({label}): " + ", ".join(f"{t} y: {v:.0f} C" for t, v in tw.items()) + f"; stress at 30 y {rock.thermal_stress(tw[30]-rock.T0):.0f} MPa")
        out["rock"][label] = {str(t): float(v) for t, v in tw.items()}
    out["rock"]["loss_MW_1y_10y_30y"] = [rock.sphere_loss(R_eq, Th, t * yr) / 1e6 for t in (1, 10, 30)]
    out["rock"]["loss_30y_GWh_th"] = rock.sphere_energy_loss(R_eq, Th, 30 * yr) / 3.6e12
    out["rock"]["throughput_30y_GWh_th"] = plant["Q_day_MWh_th"] * 330 * 30 / 1e3
    out["rock"]["heave_cm_30y"] = rock.heave(R_eq, Th, 30 * yr, 200) * 100
    out["rock"]["uplift_sf_hot"] = rock.uplift_sf(s.P_h * 1e6, 15, 150)
    out["rock"]["R_eq_m"] = R_eq
    print(f"Rock: R_eq={R_eq:.1f} m; loss 1/10/30 y = {out['rock']['loss_MW_1y_10y_30y']} MW; 30-y loss {out['rock']['loss_30y_GWh_th']:.0f} GWh_th of {out['rock']['throughput_30y_GWh_th']:.0f} GWh_th throughput; heave {out['rock']['heave_cm_30y']:.1f} cm; uplift SF {out['rock']['uplift_sf_hot']:.1f}")
    # price sensitivity
    out["price_sens"] = {}
    for pm, pp in ((15, 160), (15, 100), (15, 200), (30, 160), (0, 160), (-20, 160)):
        pl = size_plant(s, h_discharge=hd, price_mid=pm, price_peak=pp)
        out["price_sens"][f"mid{pm}_peak{pp}"] = dict(revenue_M=pl["revenue_M_per_yr"], payback=pl["payback_yr"])
        print(f"  prices mid ${pm} peak ${pp}: revenue ${pl['revenue_M_per_yr']:.0f}M/yr payback {pl['payback_yr']:.1f} y")
    # RT table for figure
    out["rt_table"] = {f"{Th}_{Tw}": Store(T_h=Th, T_w=Tw, n_charge=6, n_flash=4).round_trip()[0] for Th in range(200, 290, 10) for Tw in (120, 140, 160, 180) if Tw <= Th - 30}
    out["stage_table"] = {f"{nc}_{nf}": Store(Th, Tw, nc, nf).round_trip()[0] for nc in (1, 2, 4, 6, 8) for nf in (1, 2, 3, 4, 6)}
    json.dump(out, open("runs/design.json", "w"), indent=1)
