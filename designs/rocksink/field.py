"""Rock temperature field on two planes at selected times, from the final run's load history."""
import numpy as np, math, time
from model import Design
d = Design()
z = np.load("runs/final_series.npz")
t, q_hist, L_seg, src_P0, src_U, src_rep = z["t"], z["q_hist"], float(z["L_seg"]), z["src_P0"], z["src_U"], z["src_rep"]
# coarsen the load history into piecewise-constant blocks on a log grid
def blocks(t_eval, nb=28):
    edges = np.unique(np.concatenate([[0.0], np.logspace(1, math.log10(t_eval), nb)]))
    edges = edges[edges <= t_eval]; edges[-1] = t_eval
    out = []
    for a, b in zip(edges[:-1], edges[1:]):
        m = (t > a) & (t <= b)
        qb = q_hist[m].mean(axis=0) if m.any() else q_hist[np.searchsorted(t, b)]
        out.append((a, qb))
    return out
def field(pts, t_eval):
    T = np.zeros(len(pts))
    bl = blocks(t_eval)
    q_prev = np.zeros(q_hist.shape[1])
    for a, qb in bl:
        dq = qb - q_prev; q_prev = qb
        lag = t_eval - a
        if lag <= 0: continue
        dq_src = dq[src_rep]
        for c0 in range(0, len(pts), 400):
            resp = d._segment_response(pts[c0:c0+400], src_P0, src_U, L_seg, np.array([lag]))[0]
            T[c0:c0+400] += resp @ dq_src
    return d.T0 + T
n = 90
xs = np.linspace(-45, 45, n); zs = np.linspace(0, 100, n)
X, Z = np.meshgrid(xs, zs); pv = np.column_stack([X.ravel(), np.zeros(X.size), Z.ravel()])
ys = np.linspace(-45, 45, n); X2, Y2 = np.meshgrid(xs, ys)
zmid = d.z_collar - d.L_adiab - 0.5 * d.L_cond
ph = np.column_stack([X2.ravel(), Y2.ravel(), np.full(X2.size, zmid)])
out = {"xs": xs, "zs": zs, "ys": ys, "zmid": zmid}
for day in (1, 7, 30, 365):
    t0 = time.time()
    out[f"vert_{day}"] = field(pv, day * 86400).reshape(n, n)
    out[f"horiz_{day}"] = field(ph, day * 86400).reshape(n, n)
    print(f"day {day}: vert max {out[f'vert_{day}'].max():.1f} C, horiz max {out[f'horiz_{day}'].max():.1f} C  ({time.time()-t0:.0f}s)", flush=True)
np.savez("runs/field.npz", **out)
