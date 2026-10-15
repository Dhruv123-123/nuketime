"""A plant fed by a sequence of header houses, run by two operating policies.

The plant has a fixed flow capacity. A new header house (16 five-spot patterns) comes
online every few months as wellfield development completes. Each month the operator
sets every producer's rate. Both policies see the same data: monthly flow and head
grade per producer, plus a delineation-drilling estimate of each pattern's pounds.
"""
import numpy as np
from field import Wellfield, GPM, LB_PER_KG

PRICE = 90.0        # $/lb U3O8 (Cameco long-term indicator ~$96.5, spot ~$90, Aug 2026)
VAR_COST = 0.60     # $/m3 pumped: power, lixiviant, restoration-water treatment (assumed)
DISC = 0.08         # per year


def new_header_house(rng):
    return Wellfield(rng,
                     K_mean=float(np.exp(rng.normal(np.log(4.0), 0.4))),
                     sig_lnK=float(rng.uniform(0.6, 1.2)),
                     grade_mean=float(np.exp(rng.normal(np.log(0.08), 0.35))),
                     k_u=float(np.exp(rng.normal(np.log(0.004), 0.35))),
                     k_g=float(np.exp(rng.normal(np.log(0.03), 0.5))))


class Scenario:
    def __init__(self, seed, n_hh=6, cadence=5, months=36, plant_gpm=1200,
                 design_gpm=40, max_gpm=60, est_sd=0.35):
        self.seed, self.n_hh, self.cadence, self.months = seed, n_hh, cadence, months
        self.plant = plant_gpm * GPM
        self.design = design_gpm * GPM
        self.qmax = max_gpm * GPM
        self.est_sd = est_sd

    def fields(self):
        rng = np.random.default_rng(self.seed)
        hhs = [new_header_house(np.random.default_rng(rng.integers(1 << 31)))
               for _ in range(self.n_hh)]
        # delineation estimate of pounds in each pattern (drill-hole grade x thickness)
        est = [hh.inplace_kg * np.exp(rng.normal(0, self.est_sd, 16)) for hh in hhs]
        return hhs, est


def run(scn, policy):
    hhs, est = scn.fields()
    online = lambda m: [k for k in range(scn.n_hh) if m >= k * scn.cadence]
    hist = {(k, j): [] for k in range(scn.n_hh) for j in range(16)}   # (vol, kg) per month
    tot_kg = tot_vol = npv = 0.0
    monthly = []
    policy.reset(scn, est)
    for m in range(scn.months):
        on = online(m)
        q = policy.rates(m, on, hist)                     # dict (k, j) -> m3/day
        assert sum(q.values()) <= scn.plant * 1.0001
        kg_m = vol_m = 0.0
        for k in on:
            qk = np.array([q.get((k, j), 0.0) for j in range(16)])
            vol, kg, _ = hhs[k].step_month(qk)
            for j in range(16):
                hist[(k, j)].append((vol[j], kg[j]))
            kg_m += kg.sum(); vol_m += vol.sum()
        cash = kg_m * LB_PER_KG * PRICE - vol_m * VAR_COST
        npv += cash / (1 + DISC) ** ((m + 0.5) / 12)
        tot_kg += kg_m; tot_vol += vol_m
        monthly.append((kg_m * LB_PER_KG, vol_m))
    inplace = sum(hh.total_kg for hh in hhs)
    return dict(lb=tot_kg * LB_PER_KG, vol=tot_vol, npv=npv, rec=tot_kg / inplace,
                lb_per_kgal=tot_kg * LB_PER_KG / (tot_vol / 3.785), monthly=monthly)


class Conventional:
    """Standard practice: keep the plant at nameplate by splitting flow equally over
    every producing pattern (up to the per-well limit), and shut a pattern in once its
    head grade falls below the cut-off. The default cut-off is the direct-cost
    break-even; a higher cut-off can be passed to model a tuned operator."""
    name = "Conventional"

    def __init__(self, cutoff_mgL=None, name=None):
        self.cutoff = cutoff_mgL if cutoff_mgL is not None else VAR_COST / (PRICE * LB_PER_KG) * 1e3
        if name:
            self.name = name

    def reset(self, scn, est):
        self.scn = scn
        self.shut = set()

    def rates(self, m, on, hist):
        act = []
        for k in on:
            for j in range(16):
                h = hist[(k, j)]
                if (k, j) in self.shut:
                    continue
                if len(h) > 2 and h[-1][0] > 0 and h[-1][1] / h[-1][0] * 1e3 < self.cutoff:
                    self.shut.add((k, j))
                    continue
                act.append((k, j))
        if not act:
            return {}
        r = min(self.scn.qmax, self.scn.plant / len(act))
        return {key: r for key in act}


class ClosedLoop:
    """Calibrated pattern models plus marginal allocation of plant flow.

    Each pattern is a first-order tank: a month that pumps v m3 recovers
    (M - P) * (1 - exp(-a v)) kg, where M is recoverable kg, P cumulative production
    and a the sweep efficiency per m3. M starts from the delineation estimate and a
    from header houses already run; both are re-fitted every month from that
    pattern's own flow and head-grade history (a Bayesian MAP fit). Plant flow then
    goes wherever the next m3 recovers the most uranium net of cost: equalising
    marginal value across patterns, subject to the plant cap and per-well limits."""
    name = "Closed loop"

    def __init__(self, rec_prior=0.80, a_prior=None, sd_M=0.35, sd_a=0.5, lag=1):
        self.rec_prior, self.sd_M, self.sd_a, self.lag = rec_prior, sd_M, sd_a, lag
        self.a_prior = a_prior

    def reset(self, scn, est):
        self.scn = scn
        self.M0 = {(k, j): est[k][j] * self.rec_prior for k in range(scn.n_hh) for j in range(16)}
        if self.a_prior is None:
            # one pattern pore volume is 30 x 30 x 5 x 0.3 m3; ~ 1/(6 PV) per m3
            self.a_prior = 1.0 / (6 * 1350.0)
        self.par = {}

    def _fit(self, key, h):
        M0, a0 = self.M0[key], self.a_prior
        if len(h) <= self.lag:
            return M0, a0
        v = np.array([x[0] for x in h]); y = np.array([x[1] for x in h])
        best, bp = np.inf, (M0, a0)
        # coarse-to-fine grid MAP (2 parameters, cheap and robust)
        lM = np.log(M0 + 1e-9); la = np.log(a0)
        for span, nn in ((1.2, 25), (0.25, 21)):
            Ms = np.exp(np.linspace(lM - span * 2, lM + span * 2, nn))
            As = np.exp(np.linspace(la - span * 2.5, la + span * 2.5, nn))
            for Mi in Ms:
                P = np.concatenate([[0], np.cumsum(y)[:-1]])
                pred = np.maximum(Mi - P, 0)[None, :] * (1 - np.exp(-As[:, None] * v[None, :]))
                # skip the first month (lixiviant arrival lag)
                r = (pred[:, self.lag:] - y[self.lag:]) / (0.1 * y[self.lag:].mean() + 1e-6 + 0.1 * pred[:, self.lag:])
                obj = (r ** 2).sum(1) + ((np.log(Mi) - np.log(M0)) / self.sd_M) ** 2 \
                    + ((np.log(As) - np.log(a0)) / self.sd_a) ** 2
                i = int(np.argmin(obj))
                if obj[i] < best:
                    best, bp = obj[i], (Mi, As[i])
            lM, la = np.log(bp[0]), np.log(bp[1])
        return bp

    def rates(self, m, on, hist):
        days = 30.0
        keys, R, A = [], [], []
        for k in on:
            for j in range(16):
                key = (k, j)
                h = hist[key]
                M, a = self._fit(key, h)
                P = sum(x[1] for x in h)
                keys.append(key); R.append(max(M - P, 0.0)); A.append(a)
        R, A = np.array(R), np.array(A)
        val = PRICE * LB_PER_KG          # $ per kg
        vmax = self.scn.qmax * days
        # monthly volume v_j maximising val*R(1-exp(-a v)) - c v - lam v
        def alloc(lam):
            g = val * R * A                # marginal $ per m3 at v = 0
            v = np.where(g > VAR_COST + lam, np.log(np.maximum(g, 1e-12) / (VAR_COST + lam)) / A, 0.0)
            return np.clip(v, 0, vmax)
        cap = self.scn.plant * days
        v = alloc(0.0)
        if v.sum() > cap:
            lo, hi = 0.0, val * (R * A).max()
            for _ in range(60):
                mid = (lo + hi) / 2
                if alloc(mid).sum() > cap:
                    lo = mid
                else:
                    hi = mid
            v = alloc(hi)
        return {key: vi / days for key, vi in zip(keys, v) if vi > 0}


class GradeRank:
    """Heuristic: give each pattern the per-well maximum in order of last month's head
    grade (new patterns first) until the plant is full; shut in below the cut-off."""
    name = "Grade rank"

    def __init__(self, cutoff_mgL=20.0):
        self.cutoff = cutoff_mgL

    def reset(self, scn, est):
        self.scn = scn

    def rates(self, m, on, hist):
        cand = []
        for k in on:
            for j in range(16):
                h = hist[(k, j)]
                g = 1e9 if len(h) < 2 else h[-1][1] / max(h[-1][0], 1e-9) * 1e3
                if g >= self.cutoff:
                    cand.append((g, (k, j)))
        cand.sort(reverse=True)
        q, left = {}, self.scn.plant
        for g, key in cand:
            r = min(self.scn.qmax, left)
            if r <= 0:
                break
            q[key] = r; left -= r
        return q
