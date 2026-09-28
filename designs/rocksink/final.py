import json, numpy as np
from model import Design, decay_fraction
d = Design()
s = d.run(verbose=False)
json.dump(s, open("runs/final.json", "w"), indent=1)
np.savez("runs/final_series.npz", t=d.t, Tj=d.Tj, Tv=d.Tv, Qrock=d.Qrock, Qin=d.Qin, q_hist=d.q_hist,
         Tw=d.Tw, act=d.act, Q_unit=d.Q_unit, q_flood=d.q_flood, q_son=d.q_son, T_cnv=d.T_cnv,
         Qdec=d.P0 * decay_fraction(d.t), src_P0=d.src_P0, src_U=d.src_U, src_rep=d.src_rep, L_seg=d.L_seg)
print(json.dumps({k: v for k, v in s.items() if not k.startswith("day")}, indent=1))
for k in ("day1", "day7", "day30", "day365", "day1095"):
    print(k, s[k])
