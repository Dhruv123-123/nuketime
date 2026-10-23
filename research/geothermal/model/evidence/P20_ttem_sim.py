"""P20 Plume Rover: 1D layered-earth TEM forward model + linearised resolution.
Offset-receiver tTEM-like geometry: Tx dipole (2x4 m loop, moment = I*8 m^2), Rx at 9 m offset,
both 0.4 m above ground. Laplace-domain Hankel integral (damped by source height), Gaver-Stehfest
inversion to time. Output: dBz/dt (V/m^2 per unit Rx area) for step-off.
Noise model (assumption, tuned so a 30 ohm-m halfspace gives DOI ~70-80 m, tTEM-like):
 sigma_d = 3% relative + floor 2e-9 V/m^2 * (t/1e-4 s)^-0.5 at 30 A moment 240 A m^2.
Run: python3 -I P20_ttem_sim.py
"""
import numpy as np
from math import factorial
MU0 = 4e-7*np.pi
R_OFF, H = 9.0, 0.4
MOM = 30.0*8.0                      # 30 A x 8 m^2 single turn
TIMES = np.logspace(np.log10(5e-6), np.log10(1e-3), 24)   # 5 us .. 1 ms gates
LAM = np.logspace(-4, np.log10(40/H), 3000)
from scipy.special import j0
J0 = j0(LAM*R_OFF)

def stehfest_V(N=12):
    V = np.zeros(N)
    for i in range(1, N+1):
        s = 0.0
        for k in range((i+1)//2, min(i, N//2)+1):
            s += k**(N//2)*factorial(2*k)/(factorial(N//2-k)*factorial(k)*factorial(k-1)*factorial(i-k)*factorial(2*k-i))
        V[i-1] = (-1)**(i+N//2)*s
    return V
VS = stehfest_V()

def rte(s, rho, thk):
    sig = 1.0/np.asarray(rho)
    G = [np.sqrt(LAM**2 + s*MU0*sg) for sg in sig]
    Y = G[-1]
    for j in range(len(sig)-2, -1, -1):
        t = np.tanh(G[j]*thk[j])
        Y = G[j]*(Y + G[j]*t)/(G[j] + Y*t)
    return (LAM - Y)/(LAM + Y)

def Hs(s, rho, thk):
    f = rte(s, rho, thk)*np.exp(-2*LAM*H)*LAM**2*J0
    return MOM/(4*np.pi)*np.trapezoid(f, LAM)

def dbdt(rho, thk):
    out = []
    for t in TIMES:
        ln2t = np.log(2)/t
        acc = sum(VS[i]*Hs((i+1)*ln2t, rho, thk) for i in range(len(VS)))
        out.append(abs(MU0*acc*ln2t))
    return np.array(out)

def noise(d):
    return 0.03*d + 2e-9*(TIMES/1e-4)**-0.5

def model(p):
    # p = [log rho1, log rho_plume, top, thickness, log rho_bg]
    r1, rp, z, th, rb = p
    return dbdt([np.exp(r1), np.exp(rp), np.exp(rb)], [z, th])

def post_sd(p, prior_sd):
    d0 = model(p); e = noise(d0)
    J = np.zeros((len(d0), len(p)))
    for k in range(len(p)):
        dp = np.array(p, float); h = 0.02*max(abs(p[k]), 1.0); dp[k] += h
        J[:, k] = (model(dp) - d0)/h/e
    use = d0 > 2*e - 0.03*d0   # gates above floor
    Jm = J[use]
    C = np.linalg.inv(Jm.T@Jm + np.diag(1/np.array(prior_sd)**2))
    return np.sqrt(np.diag(C)), use.sum()

if __name__ == "__main__":
    # sanity: halfspace late-time analytic (central-ish) check
    hs = dbdt([30.0], [])
    s = 1/30.0; t = TIMES[-6]
    ana = MOM*MU0**2.5*s**1.5/(20*np.pi**1.5*t**2.5)*MU0/MU0
    print(f"halfspace 30 ohm-m at t={t*1e6:.0f}us: sim {hs[-6]:.3e}  analytic late-time {ana*1:.3e} (should be same order)")
    # DOI by plume-detectability: cold fresh alluvium 40 ohm-m, bg 40, plume 4 ohm-m 15 m thick
    print("\nPlume detect: 40 ohm-m lid / 4 ohm-m warm Cl plume (15 m) / 40 ohm-m below")
    base = dbdt([40.0], [])
    for z in [5, 10, 20, 30, 45, 60, 80, 100, 130]:
        d = dbdt([40.0, 4.0, 40.0], [z, 15.0])
        snr = np.sqrt(np.sum(((d-base)/noise(base))**2))
        print(f"  top {z:4d} m : max rel diff {np.max(np.abs(d/base-1))*100:6.1f}%   chi-dist {snr:7.1f}")
    print("\nThinner/weaker plume: 8 ohm-m, 10 m thick")
    for z in [10, 30, 50, 70, 90]:
        d = dbdt([40.0, 8.0, 40.0], [z, 10.0])
        snr = np.sqrt(np.sum(((d-base)/noise(base))**2))
        print(f"  top {z:4d} m : chi-dist {snr:7.1f}")
    print("\nLinearised posterior SD (prior sd: logrho 1.0, top 50 m, thk 30 m)")
    for z in [10, 25, 40, 60, 80]:
        p = [np.log(40), np.log(4), z, 15.0, np.log(40)]
        sd, ng = post_sd(p, [1.0, 1.0, 50.0, 30.0, 1.0])
        print(f"  top {z:3d} m: sd(top)={sd[2]:5.1f} m  sd(thk)={sd[3]:5.1f} m  sd(ln rho_p)={sd[1]:.2f}  "
              f"sd(conductance)~{100*np.hypot(sd[1], sd[3]/15):.0f}%  gates={ng}")
    print("\nPlaya case: 3 ohm-m surface clay/brine 0-z, over 40 ohm-m (screening a deeper plume?)")
    for zc in [5, 10, 20]:
        b = dbdt([3.0, 40.0], [zc]); d = dbdt([3.0, 40.0, 4.0, 40.0], [zc, 40.0-zc, 15.0])
        snr = np.sqrt(np.sum(((d-b)/noise(b))**2))
        print(f"  playa {zc:2d} m thick, plume at 40 m: chi-dist {snr:6.1f}")
