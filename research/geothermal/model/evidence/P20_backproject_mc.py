"""P20: Monte Carlo of upflow back-projection from a mapped conductive tongue (rank 6).
Tongue: apex (upflow) at origin, axis bearing theta, width grows linearly W = w0 + k*x (km).
We observe crossings at transects spaced dx along the axis, from x_near to x_far (the part we can drive).
Each crossing gives the centre (sd = c_sd) and width (sd = w_sd); fit axis line and width line, extrapolate
to W = w0 (apex). Report 1-sigma search-ellipse area vs the 'ranch wells only' baseline sector.
"""
import numpy as np
rng = np.random.default_rng(1)
def run(dx, x_near, x_far, c_sd, w_sd, n=4000):
    xs = np.arange(x_near, x_far+1e-9, dx)
    along, across = [], []
    for _ in range(n):
        th = rng.uniform(-0.15, 0.15)              # tongue curves a bit (rad)
        k = rng.uniform(0.15, 0.5); w0 = rng.uniform(0.2, 0.6)
        W = w0 + k*xs + rng.normal(0, w_sd, xs.size)
        yc = np.tan(th)*xs + rng.normal(0, c_sd, xs.size)
        A = np.vstack([np.ones_like(xs), xs]).T
        (b0, b1), *_ = np.linalg.lstsq(A, W, rcond=None)
        (c0, c1), *_ = np.linalg.lstsq(A, yc, rcond=None)
        w0_prior = 0.4                               # apex width prior (km)
        xa = (w0_prior - b0)/b1 if b1 > 0.02 else -5.0
        xa = np.clip(xa, -6, x_near)
        along.append(xa - 0.0); across.append(c0 + c1*xa)
    a, c = np.array(along), np.array(across)
    return np.std(a), np.std(c), np.pi*np.std(a)*np.std(c)
print("Baseline: ranch wells only. Bearing +-50 deg, distance 1-8 km unknown -> sector area ~",
      round(0.5*np.deg2rad(100)*(8**2-1**2), 1), "km2")
for label, dx, xn, xf, csd, wsd in [
    ("field mode, 150 m lines, 1-5 km reach", 0.15, 1.0, 5.0, 0.05, 0.08),
    ("field mode, 150 m lines, 2-4 km reach", 0.15, 2.0, 4.0, 0.05, 0.08),
    ("road mode, ~0.8 km transects, 1-6 km", 0.8, 1.0, 6.0, 0.12, 0.2),
    ("road mode, 1.5 km transects, 2-8 km", 1.5, 2.0, 8.0, 0.2, 0.3),
    ("AEM-like, 2 km lines, 1-9 km", 2.0, 1.0, 9.0, 0.15, 0.25)]:
    sa, sc, area = run(dx, xn, xf, csd, wsd)
    print(f"{label:42s} sd_along {sa:4.2f} km  sd_across {sc:4.2f} km  1-sigma ellipse {area:5.2f} km2")
