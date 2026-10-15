"""Buying simulation: at T=2016, among open contaminated sites within reach of a high-voltage substation,
which portfolio would a buyer have ended up with if they ranked by the full model, by the structured model,
by the buyer's lookup, or at random?  Reports realised closure within 5 years and time to closure.

Inputs: work/pred_temporal.pkl (from backtest.py), data/ca_substations.csv (CEC/HIFLD, Max_Voltage in kV).
Writes results/buy_sim.json and results/buy_sim.md, plus results/top_sites_2016.csv.
"""
import json
import os

import numpy as np
import pandas as pd
from sklearn.neighbors import BallTree

from common import DATA, RESULTS, WORK, log

pred = pd.read_pickle(os.path.join(WORK, "pred_temporal.pkl"))
T = 2016 if (pred["T"] == 2016).any() else int(pred["T"].min())
p = pred[pred["T"] == T].dropna(subset=["lat", "lon"]).copy()
p = p[p.lat.between(32, 42.5) & p.lon.between(-125, -114)]
sub = pd.read_csv(os.path.join(DATA, "ca_substations.csv"), encoding="utf-8-sig")
sub = sub[(sub.Type.astype(str).str.upper() == "SUBSTATION") & sub.Max_Voltage.notna()]
log(f"T={T}: {len(p):,} open sites with coordinates; {len(sub):,} substations")

out = {"T": T, "n_open_sites": int(len(p)), "base_closure_rate": round(float(p.y.mean()), 3)}
for kv in (115, 230):
    s = sub[sub.Max_Voltage >= kv]
    tree = BallTree(np.radians(s[["Lat", "Lon"]].to_numpy()), metric="haversine")
    d, i = tree.query(np.radians(p[["lat", "lon"]].to_numpy()), k=1)
    p[f"dist_km_{kv}"] = d[:, 0] * 6371.0
    p[f"sub_name_{kv}"] = s.Name.to_numpy()[i[:, 0]]
    p[f"sub_kv_{kv}"] = s.Max_Voltage.to_numpy()[i[:, 0]]
    for radius in (1.5, 3.0):
        pool = p[p[f"dist_km_{kv}"] <= radius]
        key = f"ge{kv}kV_within{radius}km"
        r = {"pool": int(len(pool)), "pool_closure_rate": round(float(pool.y.mean()), 3) if len(pool) else None,
             "pool_by_county_top10": pool.county.value_counts().head(10).to_dict()}
        rng = np.random.default_rng(0)
        for k in (50, 100, 300):
            if len(pool) < k * 2:
                continue
            row = {}
            for sc in ("F", "S", "L2", "L1"):
                top = pool.sort_values(f"p_{sc}", ascending=False).head(k)
                row[sc] = {"closed_5y": round(float(top.y.mean()), 3), "median_ttc": round(float(top.ttc.median()), 2) if top.y.sum() else None}
            rand = [pool.sample(k, random_state=int(rng.integers(1e9))).y.mean() for _ in range(200)]
            row["random"] = {"closed_5y": round(float(np.mean(rand)), 3), "sd": round(float(np.std(rand)), 3)}
            row["F_minus_L2_closed_5y"] = round(row["F"]["closed_5y"] - row["L2"]["closed_5y"], 3)
            r[f"top{k}"] = row
        out[key] = r

pool = p[p.dist_km_115 <= 3.0].sort_values("p_F", ascending=False)
cols = ["gid", "county", "case_type", "status_at_T", "years_open", "p_F", "p_S", "p_L2", "y", "ttc", "dist_km_115", "sub_name_115", "sub_kv_115", "lat", "lon"]
pool.head(300)[cols].to_csv(os.path.join(RESULTS, f"top_sites_{T}.csv"), index=False)
json.dump(out, open(os.path.join(RESULTS, "buy_sim.json"), "w"), indent=2, default=str)

L = [f"# Buying simulation at T={T}\n", f"Open sites with coordinates: {out['n_open_sites']:,}; base 5-year closure rate {out['base_closure_rate']}.\n"]
for key, r in out.items():
    if not isinstance(r, dict):
        continue
    L.append(f"\n## {key}: pool {r['pool']:,} sites, pool closure rate {r['pool_closure_rate']}\n")
    L.append("| top k | model F | structured S | lookup L2 | lookup L1 | random | F - L2 |\n|---|---|---|---|---|---|---|")
    for k in (50, 100, 300):
        if f"top{k}" in r:
            w = r[f"top{k}"]
            L.append(f"| {k} | {w['F']['closed_5y']} (ttc {w['F']['median_ttc']}) | {w['S']['closed_5y']} | {w['L2']['closed_5y']} | {w['L1']['closed_5y']} | {w['random']['closed_5y']} ± {w['random']['sd']} | {w['F_minus_L2_closed_5y']} |")
    L.append(f"\nPool by county: {r['pool_by_county_top10']}")
open(os.path.join(RESULTS, "buy_sim.md"), "w").write("\n".join(L))
log("\n".join(L))
