"""P15 PACKSACK-CORE calcs. Plain physics, textbook constants (unverified where noted)."""
import numpy as np
rng = np.random.default_rng(15)
yr = 3.156e7

# 1. Helium loss from a freshly cut core (cylinder, early-time diffusion)
#    F ~ (4/sqrt(pi)) * sqrt(Dp t / r^2), Dp = pore diffusivity = D_water / tortuosity
D_He, D_Ne = 7.2e-9, 4.2e-9      # m2/s in water at 25 C (textbook, unverified)
tau = 3.0                         # tortuosity factor (assumed)
print("1. Fraction of pore He lost before sealing")
for name, rcore in [("AQ (27 mm core)", 0.0135), ("BQ (36.5 mm core)", 0.01825)]:
    for tmin in (2, 5, 10, 20, 40):
        t = tmin*60
        F_he = min(1, 4/np.sqrt(np.pi)*np.sqrt(D_He/tau*t/rcore**2))
        F_ne = min(1, 4/np.sqrt(np.pi)*np.sqrt(D_Ne/tau*t/rcore**2))
        print(f"  {name:18s} {tmin:3d} min: He lost {F_he:5.1%}, Ne lost {F_ne:5.1%}, He/Ne bias {(1-F_he)/(1-F_ne)-1:+.1%}")

# 2. Width of the diffusive pore-water He halo around an active fault conduit
De = 1e-10   # m2/s effective matrix diffusivity in fractured volcanic/carbonate rock (assumed)
print("\n2. He halo half-width sqrt(De t) around a conduit")
for ky in (1, 10, 100, 500):
    print(f"  {ky:4d} kyr: {np.sqrt(De*ky*1e3*yr):6.1f} m")

# 3. What a 150-200 m bedrock hole sees above a Big Blind-type reservoir (121 C at 823 m)
Ts, g0 = 15.0, 0.030   # surface C, background gradient C/m in bedrock (k~2.5)
print("\n3. Excess T at hole depth, conductive cap above a reservoir top")
for top, Tres in [(823, 121), (760, 138), (500, 130)]:
    g = (Tres-Ts)/top
    for z in (100, 150, 200):
        print(f"  top {top} m, {Tres} C: z={z} m T={Ts+g*z:5.1f} C bg={Ts+g0*z:5.1f} excess={(g-g0)*z:5.1f} C")

# 4. Extrapolation error to 1 km: gradient from a 150 m equilibrium log + needle k vs a single ranch-well reading
N = 20000
def T1km(n_int, sig_T, k_err, lid_frac):
    g_true = rng.uniform(0.04, 0.15, N)
    # gradient fit error from n points along 100 m interval
    z = np.linspace(50, 150, n_int)
    se_g = sig_T/np.sqrt(np.sum((z-z.mean())**2))
    g_hat = g_true + rng.normal(0, se_g, N)
    # conductivity contrast with depth (unknown lithology below hole), reduced by core k
    kr = np.exp(rng.normal(0, k_err, N))
    # chance a deeper advective change bends the curve (lid / outflow) -> extra error
    adv = rng.random(N) < lid_frac
    extra = np.where(adv, rng.normal(0, 25, N), 0)
    err = (g_hat*kr - g_true)*850 + extra
    return np.std(err)
print("\n4. Sd of predicted T at 1 km (C)")
print(f"  ranch well, 1 reading, k unknown : {T1km(2, 1.0, 0.35, 0.45):5.1f}")
print(f"  P14 push 60 m tube               : {T1km(20, 0.02, 0.15, 0.35):5.1f}")
print(f"  P15 core 150 m relog + core k    : {T1km(200, 0.01, 0.10, 0.20):5.1f}")

# 5. Cost per hole and per located upflow (unverified unit costs)
print("\n5. Cost per 150 m hole (USD, low-high)")
items = {"crew 3 x 6-8 d": (6500, 13000), "bits/reamers/shells": (1500, 4500),
         "rod/barrel wear": (600, 1500), "water, mud additives, grout, 1in tube": (800, 2000),
         "fuel + UTV/truck": (400, 1200), "He lab 4-6 canisters": (2000, 4200),
         "XRD 4-6 + tritium/water chem": (600, 1500), "kit amortisation ($150k/4yr/30 holes)": (1000, 1500),
         "permit/bond/clearance share": (500, 4000)}
lo = sum(v[0] for v in items.values()); hi = sum(v[1] for v in items.values())
for k_, v in items.items(): print(f"  {k_:40s} {v[0]:6d}-{v[1]:6d}")
print(f"  {'TOTAL':40s} {lo:6d}-{hi:6d}   (+ helicopter 3-8k/hole if no track)")
for hit in (0.15, 0.25, 0.4):
    for holes in (3, 5):
        print(f"  hit rate {hit:.0%}, {holes} holes/prospect: $/located upflow = {holes*(lo+hi)/2/hit/1e3:6.0f}k")
