# P09 back-of-envelope physics: pipe magnetic anomaly, in-pipe convection stability,
# Peclet detection limit, and search-area survey time. Textbook formulas, own arithmetic.
import math
mu0 = 4e-7*math.pi
B_earth = 50e-6  # T, Nevada total field approx
print("== Vertical steel pipe as a magnetic monopole at its top ==")
for name, od, wall in [("3/4in sch40", 26.7e-3, 2.87e-3), ("1in sch40", 33.4e-3, 3.38e-3), ("1.25in sch40", 42.2e-3, 3.56e-3)]:
    A = math.pi/4*(od**2-(od-2*wall)**2)  # steel cross-section m2
    for label, M in [("induced only (mu_r~100)", 100*B_earth/mu0), ("induced+remanent x10", 10*100*B_earth/mu0)]:
        p = M*A  # pole strength A*m
        vals = [1e9*mu0*p/(4*math.pi*r**2) for r in (1, 2, 3, 5, 10, 20)]
        print(f"{name:12s} A={A*1e4:4.2f} cm2 {label:26s} nT at r=1,2,3,5,10,20 m:", " ".join(f"{v:7.2f}" for v in vals))
print()
print("== Onset of free convection in a water-filled pipe (Ra_c = 216, long vertical tube) ==")
g, kappa, nu = 9.81, 1.4e-7, 1.0e-6
for alpha, T in [(0.9e-4, 10), (2.1e-4, 20), (3.0e-4, 30), (4.6e-4, 50)]:
    for name, idd in [("3/4in", 20.9e-3), ("1in", 26.6e-3), ("2in", 52.5e-3), ("4in", 102e-3)]:
        r = idd/2
        beta_c = 216*kappa*nu/(g*alpha*r**4)
        print(f"T={T:2d}C pipe {name:5s} ID {idd*1e3:5.1f} mm: critical gradient {beta_c*1000:9.1f} C/km")
print()
print("== Smallest vertical Darcy flux seen from profile curvature (Bredehoeft-Papadopulos) ==")
rho_c, lam = 4.18e6, 2.0
for L in (50, 100, 200, 300):
    for Pe in (0.05, 0.1, 0.2):
        v = Pe*lam/(rho_c*L)
        print(f"L={L:3d} m Pe={Pe:4.2f}: q = {v:.2e} m/s = {v*3.156e7*100:5.2f} cm/yr")
print()
print("== Diffusion depth of post-1980 surface warming ==")
for yrs in (40, 46):
    t = yrs*3.156e7
    print(yrs, "yr: sqrt(kappa t) =", round(math.sqrt(1e-6*t), 1), "m; 2*sqrt =", round(2*math.sqrt(1e-6*t), 1), "m")
print()
print("== Drone mag survey time for a TRS search box ==")
for box, side in [("quarter-quarter 400 m", 400), ("quarter 800 m", 800), ("section 1600 m", 1600), ("pad-cued 60 m", 60)]:
    for spacing in (3, 5):
        km = side*side/spacing/1000
        hrs = km*1000/6/3600*1.3  # 6 m/s, 30% turns
        print(f"{box:22s} spacing {spacing} m: {km:7.1f} line-km, {hrs:6.2f} flight h")
