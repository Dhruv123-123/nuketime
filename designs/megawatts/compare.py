"""Lost megawatt-hours over two years, conventional vs model-based monitoring."""
import json, sys, numpy as np
from multiprocessing import Pool
from plant import Scenario, DAYS
from monitor import ModelBased, Conventional, Combined, operate, CAL, SIG, FAULTS

TH = json.load(open("runs/thresholds.json"))
D_INV = float(sys.argv[2]) if len(sys.argv) > 2 else 90


def one(seed):
    sc = Scenario(seed)
    ideal = sc.ideal_gen()
    out = dict(seed=seed, truth={k: list(v) for k, v in sc.truth.items()})
    tr, _ = sc.simulate({})
    out["none"] = float(((ideal - tr["gen"])[CAL:]).sum() * 24)
    fixed = {f: v[0] + 30 for f, v in sc.truth.items()}
    tr, _ = sc.simulate(fixed)
    out["oracle"] = float(((ideal - tr["gen"])[CAL:]).sum() * 24)
    cv = Conventional(TH["conv"]); mb = ModelBased(TH["model"], [TH["noise_sd"][k] for k in SIG])
    for pol in (cv, mb, Combined(mb, cv)):
        tr, fx, nf = operate(sc, pol, d_fix=30, d_inv=D_INV)
        out[pol.name] = float(((ideal - tr["gen"])[CAL:]).sum() * 24)
        out[pol.name + "_fixed"] = {k: float(v) for k, v in fx.items()}
        out[pol.name + "_false"] = nf
    return out


if __name__ == "__main__":
    n = int(sys.argv[1])
    with Pool(4) as p:
        res = p.map(one, range(n))
    json.dump(res, open(f"runs/compare_inv{int(D_INV)}.json", "w"))
    hrs = (DAYS - CAL) * 24
    for k in ("none", "Conventional", "Model-based", "Combined", "oracle"):
        v = np.array([r[k] for r in res])
        print(f"{k:13s} mean lost {v.mean()/hrs:6.2f} MW avg  ({v.mean()/1e3:7.1f} GWh over 640 days)")
    c = np.array([r["Conventional"] for r in res]); m = np.array([r["Model-based"] for r in res])
    nn = np.array([r["none"] for r in res])
    cb = np.array([r["Combined"] for r in res])
    print("combined recovers vs conventional: %.2f MW avg, $%.2fM/yr at $85/MWh" % ((c - cb).mean() / hrs, (c - cb).mean() / hrs * 8760 * 85 / 1e6))
    print("model-based recovers vs conventional: %.2f MW avg, $%.2fM/yr at $85/MWh" % ((c - m).mean() / hrs, (c - m).mean() / hrs * 8760 * 85 / 1e6))
    print("share of avoidable loss avoided: conv %.0f%%, model %.0f%%" % (100 * (1 - c.sum() / nn.sum()), 100 * (1 - m.sum() / nn.sum())))
    for pol in ("Conventional", "Model-based"):
        print(f"  false alarms per plant-year, {pol}: {np.mean([r[pol + '_false'] for r in res]) / 1.75:.2f}")
    for f in FAULTS:
        has = [r for r in res if f in r["truth"]]
        for pol in ("Conventional", "Model-based"):
            det = [r for r in has if f in r[pol + "_fixed"]]
            lag = [r[pol + "_fixed"][f] - r["truth"][f][0] - 30 for r in det]
            print(f"  {f:8s} {pol:13s} found {len(det)}/{len(has)}  median detection lag {np.median(lag) if lag else float('nan'):.0f} d")
