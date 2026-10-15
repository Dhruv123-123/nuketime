"""Two ways to watch the same plant for lost megawatts.

Conventional: the thermal-performance KPIs a plant trends today. Generator output
corrected to design back-pressure, condenser cleanliness, and final feedwater
temperature, as 30-day means against a clean reference, each with an alarm
threshold. A corrected-output alarm starts an investigation (walkdowns, then heater
checks, then a calorimetric check), after which every cause present is found.

Model-based: five physics residuals (flow ratio, condenser heat balance, condenser
cleanliness, feedwater temperature, corrected output) inverted every day through
the plant model's sensitivity matrix into four separate fault magnitudes with
uncertainty, so each fault is named and sized on its own and sent straight to repair.

Both see the same sensors, learn their references from the same 90 clean days, and
have alarm thresholds tuned to the same false-alarm rate.
"""
import numpy as np
from plant import Scenario, LICENSE_MWT, GEN_LOSS, BP_SENS, P_DESIGN, DAYS, psat_kpa

CAL = 90
FAULTS = ("venturi", "leak", "foul", "heater")


def tsat(P):
    # invert Antoine
    return 1730.63 / (8.07131 - np.log10(P / 0.133322)) - 233.426


def signatures(se):
    gen, Pc = se["gen"], se["Pc"]
    dT = se["Tout"] - se["Tin"]
    qrej_ind = LICENSE_MWT - gen / GEN_LOSS
    Ts = tsat(Pc)
    lmtd = dT / np.log(np.maximum(Ts - se["Tin"], 1e-3) / np.maximum(Ts - se["Tout"], 1e-3))
    raw = dict(
        ratio=se["venturi"] / se["p1"],
        rej=dT / qrej_ind,
        clean=qrej_ind / lmtd,
        tfw=se["Tfw"],
        cgen=gen / (1 - BP_SENS * (Pc - P_DESIGN)),
    )
    S = {}
    for k, v in raw.items():
        ref = v[:CAL].mean()
        S[k] = (ref - v) if k == "tfw" else (v / ref - 1)
    return S


SIG = ("ratio", "rej", "clean", "tfw", "cgen")
UNIT = dict(venturi=0.01, leak=0.005, foul=0.2, heater=3.0)


def sensitivity():
    """Signature response to each fault alone, from the noise-free plant model."""
    G = np.zeros((len(SIG), len(FAULTS)))
    base = Scenario(12345, faults=())
    for v in base.noise.values():
        v[:] = 0
    base.cal = dict(p1=0.0, cond=0.0); base.p1_drift[:] = 0
    for j, f in enumerate(FAULTS):
        sc = Scenario.__new__(Scenario); sc.__dict__ = dict(base.__dict__)
        arr = np.zeros(len(base.t)); arr[CAL:] = UNIT[f]
        sc.b, sc.leak, sc.foul, sc.dTh = [arr if f == g else np.zeros(len(base.t)) for g in FAULTS]
        _, se = sc.simulate({})
        S = signatures(se)
        for i, k in enumerate(SIG):
            G[i, j] = S[k][CAL:].mean() / UNIT[f]
    return G


G = sensitivity()


def rolling(x, w):
    c = np.cumsum(np.insert(x, 0, 0))
    out = np.full(len(x), np.nan)
    out[w - 1:] = (c[w:] - c[:-w]) / w
    return out


def edges(stat, h, persist=7):
    """Days on which an alarm raises: the statistic has stayed above h for `persist`
    days. The alarm re-arms once the statistic drops back below h."""
    above = np.nan_to_num(stat, nan=-np.inf) > h
    out, run, armed = [], 0, True
    for d in range(CAL, DAYS):
        run = run + 1 if above[d] else 0
        if not above[d]:
            armed = True
        if armed and run >= persist:
            out.append(d); armed = False
    return out


class ModelBased:
    name = "Model-based"
    window = 30

    def __init__(self, thresholds, noise_sd):
        self.h = thresholds
        self.W = np.diag(1 / np.asarray(noise_sd))

    def estimate(self, se):
        S = signatures(se)
        Y = np.array([rolling(S[k], self.window) for k in SIG])      # 5 x days
        A = self.W @ G
        X = np.linalg.lstsq(A, self.W @ np.nan_to_num(Y), rcond=None)[0]   # 4 x days
        X[:, :self.window - 1] = 0
        return {f: X[j] for j, f in enumerate(FAULTS)}

    def alarms(self, se):
        X = self.estimate(se)
        return {f: edges(X[f], self.h[f]) for f in FAULTS}


class Conventional:
    name = "Conventional"
    window = 30

    def __init__(self, thresholds):
        self.h = thresholds

    def kpis(self, se):
        S = signatures(se)
        return dict(cgen=-rolling(S["cgen"], self.window),
                    clean=-rolling(S["clean"], self.window),
                    tfw=rolling(S["tfw"], self.window))

    def alarms(self, se):
        K = self.kpis(se)
        return {k: edges(K[k], self.h[k]) for k in K}


class Combined:
    """Model-based fault alarms plus the conventional corrected-output investigation
    for whatever the fault models do not name."""
    name = "Combined"

    def __init__(self, mb, cv):
        self.mb, self.cv = mb, cv

    def alarms(self, se):
        a = self.mb.alarms(se)
        a.update({"cgen": self.cv.alarms(se)["cgen"]})
        return a


def _first_after(days, t0):
    for d in days:
        if d >= t0:
            return d
    return None


def operate(sc, policy, d_fix=30, d_inv=90):
    """Run to a fixed point: alarms trigger repairs, repairs change later data.
    Returns (true series, repair days, number of false alarms)."""
    fixed = {}
    onset = {f: v[0] for f, v in sc.truth.items()}
    for _ in range(12):
        tr, se = sc.simulate(fixed)
        al = policy.alarms(se)
        new = {}
        false = 0
        if isinstance(policy, (ModelBased, Combined)):
            for f in FAULTS:
                if f in onset:
                    d = _first_after(al[f], onset[f])
                    if d is not None:
                        new[f] = d + d_fix
                    false += sum(1 for x in al[f] if x < onset[f])
                else:
                    false += len(al[f])
            if isinstance(policy, Combined):
                busy_until = -1
                for d in al["cgen"]:
                    if d < busy_until:
                        continue
                    end = d + d_inv
                    busy_until = end
                    for f in ("venturi", "leak", "heater"):
                        if f in onset and onset[f] < end:
                            new[f] = min(new.get(f, np.inf), max(end, onset[f]) + d_fix)
        else:
            # a corrected-output alarm opens an investigation that finds every
            # venturi, leak or heater cause present by the time it closes
            busy_until = -1
            for d in al["cgen"]:
                if d < busy_until:
                    continue
                end = d + d_inv
                busy_until = end
                found = False
                for f in ("venturi", "leak", "heater"):
                    if f in onset and onset[f] < end and f not in new:
                        new[f] = max(end, onset[f]) + d_fix
                        found = True
                false += 0 if found else 1
            for k, f in (("clean", "foul"), ("tfw", "heater")):
                if f in onset:
                    d = _first_after(al[k], onset[f])
                    if d is not None:
                        new[f] = min(new.get(f, np.inf), d + d_fix)
                    false += sum(1 for x in al[k] if x < onset[f])
                else:
                    false += len(al[k])
        if new == fixed:
            break
        fixed = new
    tr, se = sc.simulate(fixed)
    return tr, fixed, false
