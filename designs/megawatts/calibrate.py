"""Set every alarm threshold to the same false-alarm budget: in fault-free plants,
no more than 5 % of two-year runs may raise that alarm."""
import json, numpy as np
from multiprocessing import Pool
from plant import Scenario, DAYS
from monitor import signatures, SIG, ModelBased, Conventional, CAL, FAULTS


def persist_stat(x, persist=7):
    x = np.nan_to_num(x[CAL:], nan=-np.inf)
    m = np.lib.stride_tricks.sliding_window_view(x, persist).min(axis=1)
    return m.max()


def clean_run(seed):
    sc = Scenario(seed, faults=())
    _, se = sc.simulate({})
    S = signatures(se)
    return {k: float(np.std(S[k][CAL:])) for k in SIG}, se


if __name__ == "__main__":
    seeds = range(10000, 10200)
    with Pool(4) as p:
        res = p.map(clean_run, seeds)
    sd = {k: float(np.median([r[0][k] for r in res])) for k in SIG}
    mb = ModelBased({f: 0 for f in FAULTS}, [sd[k] for k in SIG])
    cv = Conventional({})
    st_m = {f: [] for f in FAULTS}; st_c = {k: [] for k in ("cgen", "clean", "tfw")}
    for _, se in res:
        X = mb.estimate(se)
        for f in FAULTS:
            st_m[f].append(persist_stat(X[f]))
        K = cv.kpis(se)
        for k in st_c:
            st_c[k].append(persist_stat(K[k]))
    out = dict(noise_sd=sd,
               model={f: float(np.percentile(st_m[f], 95)) for f in FAULTS},
               conv={k: float(np.percentile(st_c[k], 95)) for k in st_c})
    json.dump(out, open("runs/thresholds.json", "w"), indent=1)
    print(json.dumps(out, indent=1))
