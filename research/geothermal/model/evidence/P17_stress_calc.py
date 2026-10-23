"""P17 calc: how much does a measured stress state shrink slip-tendency uncertainty?
Normal-faulting Basin and Range column at 2 km. Fault set: strike 20 deg, dip 60 deg (range-front style).
Prior = World Stress Map / Lund Snee-Zoback interpolation. Post = P17 measured at 300-800 m, extrapolated.
All priors are assumptions (unverified), chosen to match M30 notes."""
import numpy as np
rng = np.random.default_rng(17)
N = 200000
z = 2.0  # km
Sv = 25.0 * z            # MPa, 2.5 g/cc
Pp = 9.8 * z             # hydrostatic

def ts(strike, dip, shmax_az, k_h, k_H, mu):
    # principal stresses: Sv vertical, Shmin = k_h*Sv, SHmax between Shmin and Sv (normal) or above (strike-slip)
    Sh = k_h * Sv; SH = k_H * Sv
    # effective
    s = np.stack([SH - Pp, Sh - Pp, np.full_like(Sh, Sv - Pp)], -1)
    # fault normal in N,E,Down frame
    st = np.radians(strike); dp = np.radians(dip)
    n = np.stack([-np.sin(st)*np.sin(dp), np.cos(st)*np.sin(dp), np.cos(dp)*np.ones_like(st)], -1)
    a = np.radians(shmax_az)
    # SHmax direction unit vector, Shmin perpendicular, vertical
    eH = np.stack([np.cos(a), np.sin(a), 0*a], -1)
    eh = np.stack([-np.sin(a), np.cos(a), 0*a], -1)
    l1 = (n*eH).sum(-1); l2 = (n*eh).sum(-1); l3 = n[..., 2]
    sn = s[...,0]*l1**2 + s[...,1]*l2**2 + s[...,2]*l3**2
    t2 = (s[...,0]**2*l1**2 + s[...,1]**2*l2**2 + s[...,2]**2*l3**2) - sn**2
    tau = np.sqrt(np.maximum(t2, 0))
    return tau / sn, mu

def H(p):
    p = np.clip(p, 1e-9, 1-1e-9); return -(p*np.log2(p)+(1-p)*np.log2(1-p))

strike = np.full(N, 20.0); dip = rng.uniform(55, 70, N)
mu = rng.uniform(0.6, 0.85, N)  # friction, same in both cases (P17 does not measure it)
scen = {
 # name: (shmax_az sd, k_h mean, k_h sd, k_H mean, k_H sd)
 'prior_WSM': (25.0, 0.62, 0.07, 0.80, 0.12),
 'post_P17_measured': (8.0, None, 0.03, None, 0.07),
}
# truth draws for preposterior: sample a 'true' local state from the prior, then posterior centred on it
true_az = 110 + rng.normal(0, 25, 4000)   # SHmax ~N20E-ish in Great Basin -> Shmin WNW; use az of SHmax = 20 +- 25 deg
true_az = 20 + rng.normal(0, 25, 4000)
true_kh = np.clip(rng.normal(0.62, 0.07, 4000), 0.45, 0.85)
true_kH = np.clip(true_kh + np.abs(rng.normal(0.18, 0.12, 4000)), 0.5, 1.2)

def pcrit(az_m, az_sd, kh_m, kh_sd, kH_m, kH_sd, n=4000):
    az = az_m + rng.normal(0, az_sd, n)
    kh = np.clip(kh_m + rng.normal(0, kh_sd, n), 0.4, 0.9)
    kH = np.clip(kH_m + rng.normal(0, kH_sd, n), kh, 1.3)
    T, m = ts(np.full(n, 20.0), rng.uniform(55, 70, n), az, kh, kH, rng.uniform(0.6, 0.85, n))
    return (T >= m).mean(), T.mean(), T.std()

p0, T0m, T0s = pcrit(20, 25, 0.62, 0.07, 0.80, 0.12, n=200000)
print(f'Prior P(critically stressed)={p0:.3f}  Ts mean={T0m:.3f} sd={T0s:.3f}  H={H(p0):.3f} bits')
posts = []; sds = []
for i in range(400):
    p, Tm, Ts_ = pcrit(true_az[i], 8, true_kh[i], 0.03, true_kH[i], 0.07)
    posts.append(p); sds.append(Ts_)
posts = np.array(posts)
EH = H(posts).mean()
print(f'Preposterior: mean P={posts.mean():.3f}; share of sites with P<0.2 or >0.8 = {((posts<0.2)|(posts>0.8)).mean():.2f}')
print(f'Expected entropy after = {EH:.3f} bits; info gain = {H(p0)-EH:.3f} bits; Ts sd {T0s:.3f} -> {np.mean(sds):.3f}')
# Shmin only (no SHmax magnitude, direction from televiewer only if breakouts): az sd 12, kH sd 0.12
posts2 = np.array([pcrit(true_az[i], 12, true_kh[i], 0.03, true_kH[i], 0.12)[0] for i in range(400)])
print(f'Shmin + direction only: info gain = {H(p0)-H(posts2).mean():.3f} bits')
# extrapolation stress: shallow ratio measured at 500 m, true at 2 km differs by sd 0.05
posts3 = np.array([pcrit(true_az[i], 8, true_kh[i], 0.05, true_kH[i], 0.09)[0] for i in range(400)])
print(f'With 0.05 extrapolation error to 2 km: info gain = {H(p0)-H(posts3).mean():.3f} bits')
# frictional limit check
for m in (0.6, 0.7, 0.85):
    q = (np.sqrt(m*m+1)+m)**2
    k = (Pp + (Sv-Pp)/q)/Sv
    print(f'mu={m}: frictional-limit Shmin/Sv (hydrostatic) = {k:.3f}')
