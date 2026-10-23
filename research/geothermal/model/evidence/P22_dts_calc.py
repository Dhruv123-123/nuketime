"""P22: what a year of Brillouin DTS on buried telecom fibre (~1 m) can detect.
Simple harmonic-fit Monte Carlo. All inputs are assumptions (unverified)."""
import numpy as np
rng = np.random.default_rng(0)
kappa = 0.5e-6                     # m2/s, dry alluvium diffusivity
P = 365.25*86400
d = np.sqrt(kappa*P/np.pi)         # annual damping depth
k = 1.0; h = 15.0                  # W/m/K conductivity, W/m2/K surface exchange
hours = np.arange(0, 365*24, 6)    # 4 reads a day
t = hours*3600.0
A0 = 12.0                          # surface annual amplitude C
def fit(z, sig_read):
    w = 2*np.pi/P
    T = A0*np.exp(-z/d)*np.cos(w*t - z/d) + rng.normal(0, sig_read, t.size)
    X = np.c_[np.ones_like(t), np.cos(w*t), np.sin(w*t)]
    b, *_ = np.linalg.lstsq(X, T, rcond=None)
    amp = np.hypot(b[1], b[2]); lag = np.arctan2(b[2], b[1])
    return b[0], amp, lag
print(f"damping depth d = {d:.2f} m; amplitude at 1 m = {A0*np.exp(-1/d):.1f} C")
for sig in (0.5, 1.0, 2.0):
    res = np.array([fit(1.0, sig) for _ in range(300)])
    zhat = res[:,2]*d                       # depth from phase lag (air phase known)
    print(f"read noise {sig} C: mean-T SD {res[:,0].std():.3f} C, depth-from-lag SD {zhat.std()*100:.1f} cm")
# offset per W/m2 at z, including surface warming
for z in (0.8, 1.0, 1.2):
    print(f"z={z} m: offset per W/m2 = {z/k + 1/h:.2f} C")
# detection threshold with background (MAGST) scatter after along-line detrend
for bg in (0.2, 0.4, 0.8):
    thr = 3*bg; dq = thr/(1.0/k + 1/h)
    print(f"MAGST residual SD {bg} C -> 3-sigma {thr:.1f} C -> dq ~ {dq:.2f} W/m2 (~{dq/0.08:.0f}x background flux)")
# depth-error term: gradient of seasonal-mean profile is small; but z error matters for flux only via z/k
print("1 m conductive offset of normal 0.08 W/m2 flux:", 0.08*1/k, "C (invisible; only anomalies count)")
