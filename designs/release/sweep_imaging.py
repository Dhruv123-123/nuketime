"""Sensitivity of radiographic screening at a fixed 0.1% false-reject rate.

Usage: python3 sweep_imaging.py [n_clean] [n_defect]
Writes runs/imaging.json.
"""
import json, sys
import numpy as np
from multiprocessing import Pool
from imaging import phantom, projections, detector, score

CONFIGS = [(px, ph) for px in (6, 12, 20) for ph in (300, 2000, 10000)]
CASES = [("none", 0)] + [("sic_hole", s) for s in (30, 50, 80, 120, 200)] + \
        [("sic_thin", s) for s in (80, 200)] + [("sic_crack", s) for s in (100, 200)] + [("no_opyc", 0)]


def run(args):
    defect, size, seed = args
    rng = np.random.default_rng(seed)
    P = projections(phantom(rng, defect, size=size))
    out = []
    for px, ph in CONFIGS:
        out.append([score(detector(p, px, ph, px, rng), px) for p in P])
    return out


if __name__ == "__main__":
    n_clean = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    n_def = int(sys.argv[2]) if len(sys.argv) > 2 else 300
    jobs, seed = [], 0
    for d, s in CASES:
        for _ in range(n_clean if d == "none" else n_def):
            jobs.append((d, s, seed)); seed += 1
    with Pool(4) as pool:
        res = pool.map(run, jobs, chunksize=20)
    res = np.array(res)                          # job, config, view
    idx, k = {}, 0
    for d, s in CASES:
        n = n_clean if d == "none" else n_def
        idx[(d, s)] = slice(k, k + n); k += n
    table = []
    for ci, (px, ph) in enumerate(CONFIGS):
        clean = res[idx[("none", 0)], ci]
        for nv in (1, 3):
            thr = np.quantile(clean[:, :nv].max(axis=1), 0.999)
            row = dict(pixel_um=px, photons=ph, views=nv, threshold=round(float(thr), 2))
            for d, s in CASES[1:]:
                sc = res[idx[(d, s)], ci, :nv].max(axis=1)
                row[f"{d}_{s}"] = round(float((sc > thr).mean()), 3)
            table.append(row)
            print(row, flush=True)
    json.dump(dict(n_clean=n_clean, n_defect=n_def, false_reject=1e-3, table=table),
              open("runs/imaging.json", "w"), indent=1)
