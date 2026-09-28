"""
ROCKSINK: passive decay-heat rejection from a shaft-sited integral PWR module
into bedrock through an array of gas-loaded gravity thermosyphons.

Physics chain modelled here
  1. Decay heat + stored primary-system heat after scram (bounding fit).
  2. Containment water jacket: lumped thermal capacitance, closed and pressurised,
     which replaces the reactor pool. Its steam space feeds a torus manifold.
  3. N sealed two-phase thermosyphons: evaporator legs in the torus, condenser legs in
     upholes drilled from a ring drift and fanned into the rock above the module.
     Gas-loaded (variable conductance): blanketed below ~45 C, fully open by ~95 C.
     Capacity checked against the counter-current flooding limit (Faghri) and the
     sonic limit.
  4. Rock: 3-D transient conduction, finite line sources with a constant-temperature
     ground surface (method of images), full spatial superposition over every borehole
     segment, temporal superposition of piecewise-constant loads. Per-segment loads
     solved each step from the isothermal-condenser condition.

Everything is SI unless noted. Depth z is positive downward, ground surface z = 0.
"""
from __future__ import annotations
import json, math, sys, time
import numpy as np
from scipy.special import erf, erfc, exp1
from iapws import IAPWS97

# --------------------------------------------------------------------------- water
_Tgrid = np.linspace(5.0, 220.0, 216)
_props = {k: np.zeros_like(_Tgrid) for k in ("P", "rho_l", "rho_v", "hfg", "sigma")}
for i, Tc in enumerate(_Tgrid):
    T = Tc + 273.15
    l, v = IAPWS97(T=T, x=0.0), IAPWS97(T=T, x=1.0)
    _props["P"][i] = l.P * 1e6
    _props["rho_l"][i] = l.rho
    _props["rho_v"][i] = v.rho
    _props["hfg"][i] = (v.h - l.h) * 1e3
    _props["sigma"][i] = l.sigma

def wprop(name: str, Tc):
    return np.interp(Tc, _Tgrid, _props[name])

def psat(Tc):
    return wprop("P", Tc)

# --------------------------------------------------------------------------- loads
def decay_fraction(t: np.ndarray | float, T_irr: float = 3 * 365.25 * 86400, factor: float = 1.15):
    """Fission-product decay power / P0 (Glasstone-Sesonske / Todreas-Kazimi form),
    times a bounding factor for actinides and fit uncertainty. Valid t >= 10 s."""
    t = np.maximum(np.asarray(t, dtype=float), 10.0)
    return factor * 0.066 * (t ** -0.2 - (t + T_irr) ** -0.2)

# --------------------------------------------------------------------------- design
class Design:
    def __init__(self, **kw):
        # reactor / module
        self.P0 = 250e6                # thermal power, W
        self.E_stored = 140e9          # primary-system stored heat released after scram, J
        self.tau_stored = 2 * 3600.0   # release time constant, s
        self.UA_cnv = 300e3            # containment wall + DHRS condensers conductance to jacket, W/K
        # jacket (annulus + steam drum, closed, pressurised)
        self.m_water = 120e3           # kg
        self.m_steel = 400e3           # kg of steel thermally coupled (CNV shell, jacket vessel)
        self.T_j0 = 25.0               # normal-ops jacket temperature, C (chilled loop)
        self.T_j_limit = 150.0         # design limit: 0.48 MPa abs, CNV external-pressure margin
        # thermosyphons
        self.N = 128
        self.D_i = 0.125               # tube ID, m
        self.D_o = 0.141
        self.D_hole = 0.165
        self.k_tube = 16.0             # stainless steel
        self.k_grout = 2.0             # thermally enhanced grout
        self.h_film = 5000.0           # condenser film coefficient, W/m2K
        self.L_evap = 4.0              # evaporator length in torus, m
        self.h_evap_out = 8000.0       # steam condensing on evaporator OD
        self.h_evap_in = 5000.0        # pool boiling inside evaporator
        self.T_gas_off = 45.0          # gas front fills whole condenser at/below this vapour T
        self.T_gas_on = 95.0           # condenser fully open at/above this vapour T
        # geometry (depths positive down)
        self.z_collar = 73.0           # drift crown / uphole collar depth, m
        self.R_drift = 15.0            # ring drift radius from shaft axis, m
        self.L_adiab = 8.0             # insulated riser above collar, m
        self.L_cond = 57.0             # condenser length, m
        self.n_seg = 6
        self.tilts_deg = (0.0, 10.0, 20.0, 30.0)   # outward tilt from vertical, alternating
        # rock
        self.k_rock = 3.0
        self.rhoc_rock = 2.3e6
        self.T0 = 14.0
        # time grid
        self.t_end = 3 * 365.25 * 86400
        self.n_steps = 600
        for k, v in kw.items():
            if not hasattr(self, k):
                raise KeyError(k)
            setattr(self, k, v)
        self.alpha = self.k_rock / self.rhoc_rock
        self.r_b = self.D_hole / 2
        self.C_j = self.m_water * 4180 + self.m_steel * 500
        # per-metre condenser resistance: film + tube wall + grout
        self.Rb_m = (1 / (self.h_film * math.pi * self.D_i)
                     + math.log(self.D_o / self.D_i) / (2 * math.pi * self.k_tube)
                     + math.log(self.D_hole / self.D_o) / (2 * math.pi * self.k_grout))
        A_e = math.pi * self.D_o * self.L_evap
        self.R_evap = 1 / (self.h_evap_out * A_e) + 1 / (self.h_evap_in * A_e)
        self._build_geometry()

    # ---------------------------------------------------------------- geometry
    def _build_geometry(self):
        N, nf = self.N, len(self.tilts_deg)
        assert N % nf == 0
        self.n_per_family = N // nf
        seg_edges = self.L_adiab + np.linspace(0, self.L_cond, self.n_seg + 1)
        self.L_seg = float(self.L_cond / self.n_seg)
        # every borehole segment as a source: start point, unit direction, length
        P0, U, fam, segid = [], [], [], []
        for i in range(N):
            th = 2 * math.pi * i / N
            phi = math.radians(self.tilts_deg[i % nf])
            collar = np.array([self.R_drift * math.cos(th), self.R_drift * math.sin(th), self.z_collar])
            u = np.array([math.sin(phi) * math.cos(th), math.sin(phi) * math.sin(th), -math.cos(phi)])
            for s in range(self.n_seg):
                P0.append(collar + u * seg_edges[s]); U.append(u); fam.append(i % nf); segid.append(s)
        self.src_P0, self.src_U = np.array(P0), np.array(U)
        self.src_fam, self.src_seg = np.array(fam), np.array(segid)
        self.S = nf * self.n_seg                     # representative (family, segment) unknowns
        self.src_rep = self.src_fam * self.n_seg + self.src_seg   # index of unknown for each source
        # representative targets: hole i = family index (first hole of each family), wall points
        self.tgt_pts, self.tgt_rep = [], []
        ng = 8
        xg, wg = np.polynomial.legendre.leggauss(ng)
        for f in range(nf):
            i = f                                     # hole index of first member of family f
            th = 2 * math.pi * i / N
            tang = np.array([-math.sin(th), math.cos(th), 0.0])
            phi = math.radians(self.tilts_deg[f])
            collar = np.array([self.R_drift * math.cos(th), self.R_drift * math.sin(th), self.z_collar])
            u = np.array([math.sin(phi) * math.cos(th), math.sin(phi) * math.sin(th), -math.cos(phi)])
            for s in range(self.n_seg):
                a, b = seg_edges[s], seg_edges[s + 1]
                l = 0.5 * (b - a) * xg + 0.5 * (a + b)
                pts = collar[None, :] + u[None, :] * l[:, None] + self.r_b * tang[None, :]
                self.tgt_pts.append(pts); self.tgt_rep.append(f * self.n_seg + s)
        self.tgt_w = wg / 2.0
        # geometry summary
        self.total_cond_length = N * self.L_cond
        self.total_hole_length = N * (self.L_adiab + self.L_cond + 3.0)

    # ---------------------------------------------------------------- rock response
    def _segment_response(self, pts, P0, U, L, t, mirror=True):
        """Temperature rise per unit q' (K per W/m) at points pts (m,3) due to finite line
        sources (n,3)/(n,3)/scalar L at times t, incl. image sources above z=0.
        For each point/source pair the line integral of erfc(d/s)/d (s = sqrt(4 alpha t)) is
        taken in the scaled coordinate u = (l - l0)/s over the window |u| <= 6 where erfc is
        non-zero, with the 1/D singularity (D = sqrt(u^2 + (rho/s)^2)) integrated analytically
        and the smooth remainder erf(D)/D by Gauss-Legendre."""
        ng = 40
        xg, wg = np.polynomial.legendre.leggauss(ng)
        out = np.zeros((len(t), pts.shape[0], P0.shape[0]))
        for sign, zflip in ((1.0, 1.0), (-1.0, -1.0)) if mirror else ((1.0, 1.0),):
            P0m = P0 * np.array([1, 1, zflip]); Um = U * np.array([1, 1, zflip])
            w = pts[:, None, :] - P0m[None, :, :]                 # (m,n,3)
            l0 = np.einsum("mnk,nk->mn", w, Um)
            rho = np.sqrt(np.maximum(np.einsum("mnk,mnk->mn", w, w) - l0 ** 2, 1e-10))
            for it, tt in enumerate(t):
                s = math.sqrt(4 * self.alpha * tt)
                c = rho / s
                a = np.maximum(-l0 / s, -6.0); b = np.minimum((L - l0) / s, 6.0)
                ok = b > a
                a = np.where(ok, a, 0.0); b = np.where(ok, b, 0.0)
                I_sing = np.arcsinh(b / c) - np.arcsinh(a / c)
                u = 0.5 * (b - a)[..., None] * xg + 0.5 * (a + b)[..., None]
                D = np.sqrt(u ** 2 + c[..., None] ** 2)
                I_smooth = np.einsum("mng,g->mn", erf(D) / D, wg) * 0.5 * (b - a)
                out[it] += sign * np.where(ok, I_sing - I_smooth, 0.0)
        return out / (4 * math.pi * self.k_rock)

    def build_gfunctions(self, lags):
        """G[it, s, s'] = wall-temperature rise of representative segment s per unit q' applied
        to every borehole segment of type s' (all holes), at lag lags[it]."""
        t0 = time.time()
        G = np.zeros((len(lags), self.S, self.S))
        for s, pts in enumerate(self.tgt_pts):
            resp = self._segment_response(pts, self.src_P0, self.src_U, self.L_seg, lags)  # (nt, ng, nsrc)
            resp = np.einsum("g,tgn->tn", self.tgt_w, resp)                                 # (nt, nsrc)
            for sp in range(self.S):
                G[:, s, sp] = resp[:, self.src_rep == sp].sum(axis=1)
        self.lags, self.G = np.asarray(lags), G
        self._gtime = time.time() - t0
        return G

    def g_at(self, dt):
        """Interpolate G in log-time."""
        x = math.log(max(dt, self.lags[0]))
        return np.array([[np.interp(x, np.log(self.lags), self.G[:, s, sp]) for sp in range(self.S)] for s in range(self.S)])

    # ---------------------------------------------------------------- thermosyphon limits
    def q_flooding(self, Tv):
        """Counter-current flooding limit of a closed two-phase thermosyphon (Faghri), W."""
        rl, rv, hfg, sig = wprop("rho_l", Tv), wprop("rho_v", Tv), wprop("hfg", Tv), wprop("sigma", Tv)
        Bo = self.D_i * math.sqrt(9.81 * (rl - rv) / sig)
        K = (rl / rv) ** 0.14 * math.tanh(Bo ** 0.25) ** 2
        A = math.pi * self.D_i ** 2 / 4
        return K * hfg * math.sqrt(rv) * (sig * 9.81 * (rl - rv)) ** 0.25 * A

    def q_sonic(self, Tv):
        rv, hfg, P = wprop("rho_v", Tv), wprop("hfg", Tv), psat(Tv)
        A = math.pi * self.D_i ** 2 / 4
        return 0.474 * hfg * math.sqrt(rv * P) * A

    def active_fraction(self, Tv):
        """Flat-front gas-loaded condenser: fraction of condenser length open to vapour."""
        Pg = psat(self.T0)                      # vapour partial pressure in the cold gas region
        P_off, P_on, P = psat(self.T_gas_off) - Pg, psat(self.T_gas_on) - Pg, psat(Tv) - Pg
        if P <= P_off:
            return 0.0
        if P >= P_on:
            return 1.0
        # gas volume ~ 1/P; reservoir sized so V_gas(P_on) = V_res, V_gas(P_off) = V_res + V_cond
        # gas volume scales as 1/P; V_gas(P_on) = V_res and V_gas(P_off) = V_res + V_cond
        return float(np.clip(1 - (P_on / P - 1) / (P_on / P_off - 1), 0, 1))

    # ---------------------------------------------------------------- transient
    def run(self, verbose=True):
        S, nf = self.S, len(self.tilts_deg)
        t = np.concatenate([[0.0], np.logspace(1, math.log10(self.t_end), self.n_steps)])
        lags = np.logspace(1, math.log10(self.t_end) + 0.05, 90)
        if not hasattr(self, "G"):
            self.build_gfunctions(lags)
        G_cache = {}
        w_len = np.repeat(self.n_per_family, S) * self.L_seg     # W per (W/m) for each unknown
        seg_of = np.tile(np.arange(self.n_seg), nf)              # segment index of each unknown
        q_hist = np.zeros((len(t), S))
        Tj, Tv_hist, Qrock, Qin, Tw_hist, act_hist = np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t)), np.zeros((len(t), S)), np.zeros(len(t))
        Tj[0] = self.T_j0; Tw_hist[0] = self.T0
        act = 0.0
        for n in range(1, len(t)):
            dt = t[n] - t[n - 1]
            # history from all previous load increments
            hist = np.zeros(S)
            for k in range(1, n):
                lag = t[n] - t[k - 1]
                key = round(math.log(lag), 3)
                if key not in G_cache:
                    G_cache[key] = self.g_at(lag)
                hist += G_cache[key] @ (q_hist[k] - q_hist[k - 1])
            Gdt = self.g_at(dt)
            Q_dec = self.P0 * float(decay_fraction(t[n]))
            Q_sto = self.E_stored / self.tau_stored * math.exp(-t[n] / self.tau_stored)
            Q_in = Q_dec + Q_sto
            Tj_prev = Tj[n - 1]
            # fixed-point iteration on gas-front activity (depends on Tv) and implicit jacket balance
            for _ in range(8):
                active = np.array([1.0 if seg_of[s] < act * self.n_seg - 1e-9 else 0.0 for s in range(S)])
                # partial segment at the front
                for s in range(S):
                    fpos = act * self.n_seg
                    if seg_of[s] < fpos < seg_of[s] + 1:
                        active[s] = fpos - seg_of[s]
                if active.sum() == 0:
                    q = np.zeros(S); Q_r = 0.0
                    Tj_new = Tj_prev + dt * Q_in / self.C_j
                    Tv = Tj_new
                    Tw = self.T0 + hist + Gdt @ (q - q_hist[n - 1])
                    act_new = self.active_fraction(Tv)
                    if abs(act_new - act) < 1e-3:
                        act = act_new
                        break
                    act = 0.5 * (act + act_new)
                    continue
                # q_s = active_s (Tv - Tw_s)/Rb ;  Tw = T0 + hist + Gdt (q - q_prev)
                # -> (Rb I + diag(active) Gdt) q = active*(Tv - T0 - hist + Gdt q_prev)
                Aact = np.diag(active)
                M = self.Rb_m * np.eye(S) + Aact @ Gdt
                rhs0 = active * (-self.T0 - hist + Gdt @ q_hist[n - 1])
                Minv = np.linalg.inv(M)
                a_vec, b_vec = Minv @ rhs0, Minv @ active
                # Tv = Tj - (Q_r/N) R_evap, Q_r = w.(a + b Tv)
                wa, wb = w_len @ a_vec, w_len @ b_vec
                c = self.R_evap / self.N
                # Tv = (Tj - c wa)/(1 + c wb);  Q_r = wa + wb Tv = alpha + beta Tj
                beta = wb / (1 + c * wb)
                alpha = wa + wb * (-c * wa) / (1 + c * wb)
                # implicit jacket: C (Tj_new - Tj_prev)/dt = Q_in - alpha - beta Tj_new
                Tj_new = (self.C_j / dt * Tj_prev + Q_in - alpha) / (self.C_j / dt + beta)
                Tv = (Tj_new - c * wa) / (1 + c * wb)
                q = a_vec + b_vec * Tv
                Q_r = float(w_len @ q)
                Tw = self.T0 + hist + Gdt @ (q - q_hist[n - 1])
                act_new = self.active_fraction(Tv)
                if abs(act_new - act) < 1e-3:
                    act = act_new
                    break
                act = 0.5 * (act + act_new)
            q_hist[n], Tj[n], Tv_hist[n], Qrock[n], Qin[n], Tw_hist[n], act_hist[n] = q, Tj_new, Tv, Q_r, Q_in, Tw, act
            if verbose and n % 100 == 0:
                print(f"  t={t[n]/86400:9.3f} d  Tj={Tj_new:6.1f} C  Tv={Tv:6.1f}  Qin={Q_in/1e6:6.3f} MW  Qrock={Q_r/1e6:6.3f} MW  Twmax={Tw.max():6.1f}  act={act:.2f}", flush=True)
        self.t, self.Tj, self.Tv, self.Qrock, self.Qin, self.q_hist, self.Tw, self.act = t, Tj, Tv_hist, Qrock, Qin, q_hist, Tw_hist, act_hist
        # per-unit loads by family and limits
        self.Q_unit = np.zeros((len(t), nf))
        for f in range(nf):
            self.Q_unit[:, f] = q_hist[:, f * self.n_seg:(f + 1) * self.n_seg].sum(axis=1) * self.L_seg
        self.q_flood = np.array([self.q_flooding(max(Tv, 20.0)) for Tv in Tv_hist])
        self.q_son = np.array([self.q_sonic(max(Tv, 20.0)) for Tv in Tv_hist])
        self.T_cnv = Tj + Qin / self.UA_cnv
        return self.summary()

    def summary(self):
        t = self.t
        def at(day):
            i = np.searchsorted(t, day * 86400)
            return i
        i_peak = int(np.argmax(self.Tj))
        i_tw = int(np.argmax(self.Tw.max(axis=1)))
        with np.errstate(divide="ignore", invalid="ignore"):
            margin = np.where(self.q_flood > 0, self.Q_unit.max(axis=1) / self.q_flood, 0)
        s = dict(
            N=self.N, R_drift=self.R_drift, L_cond=self.L_cond, k_rock=self.k_rock, T0=self.T0,
            total_condenser_m=self.total_cond_length, total_drilled_m=self.total_hole_length,
            Rb_mK_per_W=self.Rb_m, R_evap_K_per_W=self.R_evap, C_jacket_GJ_per_K=self.C_j / 1e9,
            Tj_peak=float(self.Tj[i_peak]), t_Tj_peak_h=float(t[i_peak] / 3600),
            P_jacket_peak_MPa=float(psat(self.Tj[i_peak]) / 1e6),
            T_cnv_peak=float(self.T_cnv.max()),
            Tw_peak=float(self.Tw.max()), t_Tw_peak_d=float(t[i_tw] / 86400),
            flood_ratio_max=float(np.nanmax(margin)),
            Q_unit_max_kW=float(self.Q_unit.max() / 1e3),
            gfunction_build_s=getattr(self, "_gtime", None),
        )
        for d in (1, 3, 7, 30, 90, 180, 365, 730, 1095):
            i = min(at(d), len(t) - 1)
            s[f"day{d}"] = dict(Tj=float(self.Tj[i]), Tv=float(self.Tv[i]), Qin_MW=float(self.Qin[i] / 1e6),
                                Qrock_MW=float(self.Qrock[i] / 1e6), Tw_max=float(self.Tw[i].max()), act=float(self.act[i]))
        return s


# --------------------------------------------------------------------------- checks
def validate_fls():
    """Numeric finite-line-source vs analytic infinite-line-source (long line, no mirror)."""
    d = Design(n_steps=10)
    L = 2000.0
    P0 = np.array([[0.0, 0.0, -1000.0]]); U = np.array([[0.0, 0.0, 1.0]])
    pts = np.array([[d.r_b, 0.0, 0.0], [1.0, 0.0, 0.0], [5.0, 0.0, 0.0]])
    ts = np.array([3600.0, 86400.0, 30 * 86400.0])
    num = d._segment_response(pts, P0, U, L, ts, mirror=False)[:, :, 0]
    r = pts[:, 0]
    ana = np.array([exp1(r ** 2 / (4 * d.alpha * tt)) / (4 * math.pi * d.k_rock) for tt in ts])
    return num, ana


if __name__ == "__main__":
    num, ana = validate_fls()
    print("FLS validation (numeric vs ILS analytic), K per W/m:")
    print(np.round(num, 5)); print(np.round(ana, 5))
    kw = {}
    for arg in sys.argv[1:]:
        k, v = arg.split("=")
        kw[k] = float(v) if k not in ("tilts_deg",) else tuple(float(x) for x in v.split(","))
        if k in ("N", "n_seg", "n_steps"):
            kw[k] = int(kw[k])
    d = Design(**kw)
    print(f"Design: N={d.N} R_drift={d.R_drift} L_cond={d.L_cond} k_rock={d.k_rock}  Rb'={d.Rb_m:.4f} mK/W  R_evap={d.R_evap:.2e} K/W")
    s = d.run()
    print(json.dumps(s, indent=1))
