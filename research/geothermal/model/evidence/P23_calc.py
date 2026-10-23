"""P23 back-of-envelope calcs (all inputs are assumptions, unverified)."""
import math
# 1) Detection: local magnitude scale (Hutton & Boore 1987, S. California form)
def ML(A_mm, R_km):  # A = Wood-Anderson amplitude in mm
    return math.log10(A_mm) + 1.11*math.log10(R_km) + 0.00189*R_km - 2.09
# Wood-Anderson-equivalent noise floor at a quiet Basin & Range rock site, as pick threshold.
# Assume pick needs WA-equivalent amplitude ~ 0.005 mm (quiet) and 0.02 mm (noisy ranch/road)
for A in (0.005, 0.02):
    print("pick-threshold A=%.3f mm" % A)
    for R in (3, 5, 8, 15, 30, 60):
        print("   R=%3d km  M_min=%.2f" % (R, ML(A, R)))
# NOTE: these are ideal physical limits. Real surface networks reach Mc about -0.5 to 0.5 (wind, cattle, pumps, 4-pick rule). Design uses Mc 0 +/- 0.3.
# Mc needs >=4 stations; for a cluster of 5 at ~8 km aperture, 4th-nearest distance ~6-8 km at the centre
# 2) Gutenberg-Richter gain, b = 1.0
for Mc_old in (1.5, 2.0, 2.5):
    for Mc_new in (0.0, 0.3):
        print("Mc %.1f -> %.1f : x%.0f more events" % (Mc_old, Mc_new, 10**(Mc_old-Mc_new)))
# expected events in a 300 km2 cluster footprint per year, rate of M>=2 per 1000 km2/yr
for r2 in (0.2, 0.5, 2.0):
    n0 = r2*0.3*10**(2-0.0)
    print("rate M>=2 %.1f /1000km2/yr -> M>=0 per year in 300 km2: %.0f" % (r2, n0))
# 3) HVSR f0 vs fill thickness with power-law Vs(z)=Vs0*(1+z/z0)^x ; quarter-wavelength approx
def f0(H, Vs0=300.0, z0=20.0, x=0.35, n=2000):
    dz = H/n; tt = sum(dz/(Vs0*(1+((i+0.5)*dz)/z0)**x) for i in range(n))
    return 1.0/(4*tt)
for H in (50, 100, 200, 400, 700, 1000, 1500, 2000):
    f = f0(H)
    # SESAME: window >= 10/f0, >=10 windows, >200 cycles -> record time
    t_min = max(10*10/f, 200/f)/60*3   # x3 for windows rejected for transients
    print("H=%5d m  f0=%.3f Hz  min record ~%.0f min" % (H, f, t_min))
# 4) Temperature error from basin-depth error (sediment k=1.3, bedrock k=2.8 W/mK, q=90 mW/m2)
q=0.090; ks=1.3; kb=2.8
def T15(Hfill, z=1500.0, T0=15.0):
    if Hfill>=z: return T0+q/ks*z
    return T0+q/ks*Hfill+q/kb*(z-Hfill)
for H, dH in ((800, 300), (800, 150), (800, 100)):
    print("fill %d m, depth err +-%d m -> T(1.5km) err +-%.1f C" % (H, dH, (T15(H+dH)-T15(H-dH))/2))
# 5) s/q precision from 20 blind / 40 cold
for s in (0.3, 0.5):
    print("s=%.1f n=20 sd=%.3f" % (s, math.sqrt(s*(1-s)/20)))
for qq in (0.1, 0.2):
    print("q=%.1f n=40 sd=%.3f" % (qq, math.sqrt(qq*(1-qq)/40)))
