"""Rock temperature field on two planes at selected times, from the final run's load history.
Near segments (< 25 m from a field point) use the exact finite-line integral, evaluated pairwise;
far segments use an equivalent point source. Both include the image above the ground surface."""
import numpy as np, math, time
from scipy.special import erfc, erf
from model import Design

d = Design()
z = np.load("runs/final_series.npz")
t, q_hist, L_seg = z["t"], z["q_hist"], float(z["L_seg"])
src_P0, src_U, src_rep = z["src_P0"], z["src_U"], z["src_rep"]
mid = src_P0 + 0.5 * L_seg * src_U
mid_img = mid * np.array([1, 1, -1])
_xg, _wg = np.polynomial.legendre.leggauss(40)


def pair_response(P, P0, U, L, lag):
    """Exact finite-line response (K per W/m) for matched pairs P[i] <- segment (P0[i], U[i]), with image."""
    s = math.sqrt(4 * d.alpha * lag)
    tot = np.zeros(len(P))
    for sign, zflip in ((1.0, 1.0), (-1.0, -1.0)):
        P0m = P0 * np.array([1, 1, zflip]); Um = U * np.array([1, 1, zflip])
        w = P - P0m
        l0 = np.einsum("nk,nk->n", w, Um)
        rho = np.sqrt(np.maximum(np.einsum("nk,nk->n", w, w) - l0 ** 2, 1e-10))
        c = rho / s
        a = np.maximum(-l0 / s, -6.0); b = np.minimum((L - l0) / s, 6.0)
        ok = b > a
        a = np.where(ok, a, 0.0); b = np.where(ok, b, 0.0)
        I_sing = np.arcsinh(b / c) - np.arcsinh(a / c)
        u = 0.5 * (b - a)[:, None] * _xg + 0.5 * (a + b)[:, None]
        D = np.sqrt(u ** 2 + c[:, None] ** 2)
        I_smooth = (erf(D) / D) @ _wg * 0.5 * (b - a)
        tot += sign * np.where(ok, I_sing - I_smooth, 0.0)
    return tot / (4 * math.pi * d.k_rock)


def blocks(t_eval, nb=18):
    edges = np.unique(np.concatenate([[0.0], np.logspace(1, math.log10(t_eval), nb)]))
    edges = edges[edges <= t_eval]; edges[-1] = t_eval
    out = []
    for a, b in zip(edges[:-1], edges[1:]):
        m = (t > a) & (t <= b)
        qb = q_hist[m].mean(axis=0) if m.any() else q_hist[np.searchsorted(t, b)]
        out.append((a, qb))
    return out


def field(pts, t_eval, near=25.0):
    T = np.zeros(len(pts))
    dist = np.linalg.norm(pts[:, None, :] - mid[None, :, :], axis=2)
    dist_img = np.linalg.norm(pts[:, None, :] - mid_img[None, :, :], axis=2)
    near_mask = dist < near
    ii, jj = np.nonzero(near_mask)
    q_prev = np.zeros(q_hist.shape[1])
    for a, qb in blocks(t_eval):
        dq = (qb - q_prev)[src_rep]; q_prev = qb
        lag = t_eval - a
        if lag <= 0:
            continue
        s = math.sqrt(4 * d.alpha * lag)
        far = L_seg / (4 * math.pi * d.k_rock) * (erfc(dist / s) / dist - erfc(dist_img / s) / dist_img)
        resp = np.where(near_mask, 0.0, far)
        resp[ii, jj] = pair_response(pts[ii], src_P0[jj], src_U[jj], L_seg, lag)
        T += resp @ dq
    return d.T0 + T


if __name__ == "__main__":
    n = 72
    xs = np.linspace(-45, 45, n); zs = np.linspace(0.5, 100, n)
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
