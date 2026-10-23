# P13: 1 m drone-dart noise check, reusing the P02 1D conduction forward model.
# Usage: python3 P13_dart1m_sim.py 0 20
# Compares, for a PAIR of darts under the same weather, (a) the 12-month harmonic-fit
# steady offset at 1.0 m, (b) the gradient over 0.3-1.0 m times k, against the 2 m and 3 m cases.
# Adds a site surface-mean offset (albedo/aspect/shrub) of sd 0.7 C per site (unverified prior),
# which the harmonic fit cannot remove, and penetration-depth error of the 1 m sensor (+/-5 cm, accel log).
import sys, numpy as np
sys.path.insert(0, __file__.rsplit('/',1)[0])
from P02_dart_sim import run
yr=365.25*86400; w=2*np.pi/yr
def harm(t,y):
    A=np.vstack([np.ones_like(t),np.cos(w*t),np.sin(w*t),np.cos(2*w*t),np.sin(2*w*t)]).T
    c,*_=np.linalg.lstsq(A,y,rcond=None); return c
r=np.random.default_rng(11)
deps=(0.3,0.65,1.0,2.0,3.0)
res={"off1m":[],"off1m_nosurf":[],"grad1m_q":[],"off2m":[],"q3m_pair":[],"kappa_err":[]}
for sd in range(int(sys.argv[1]),int(sys.argv[2])):
    kA=1.0; kB=float(np.clip(np.exp(r.normal(0,0.3)),0.4,1.8))
    CB=float(2.0e6*np.exp(r.normal(0,0.15)))
    dA,t,oA,_=run(q=0.08,k0=kA,C=2.0e6,kamp=0.3*r.uniform(),seed=sd,depths=deps,years_spin=3)
    dB,t,oB,_=run(q=0.08,k0=kB,C=CB,kamp=0.3*r.uniform(),seed=sd,depths=deps,years_spin=3)
    t=t-t[0]
    sA,sB=r.normal(0,0.7,2)  # site surface-mean offsets (do not decay with depth at steady state)
    cA=harm(t,oA[:,2]); cB=harm(t,oB[:,2])
    res["off1m_nosurf"].append(cA[0]-cB[0]); res["off1m"].append(cA[0]+sA-cB[0]-sB)
    res["off2m"].append(oA[:,3].mean()+sA-oB[:,3].mean()-sB)
    def g(o,i,j,dz): return (harm(t,o[:,j])[0]-harm(t,o[:,i])[0])/dz
    dz=0.35*(1+0.0)
    gA=g(oA,0,2,0.7+r.normal(0,0.05)); gB=g(oB,0,2,0.7+r.normal(0,0.05))
    kAh=kA*(1+0.15*r.normal()); kBh=kB*(1+0.15*r.normal())   # k from kappa(wave) x assumed C: ~15%
    res["grad1m_q"].append(kAh*gA-kBh*gB)
    gA3=(oA[:,4].mean()-oA[:,3].mean()); gB3=(oB[:,4].mean()-oB[:,3].mean())
    res["q3m_pair"].append(kAh*gA3-kBh*gB3)
    # kappa from amplitude ratio 0.3->1.0 m
    a0=np.hypot(*harm(t,oA[:,0])[1:3]); a1=np.hypot(*harm(t,oA[:,2])[1:3])
    d=0.7/np.log(a0/a1); kap=d*d*w/2; res["kappa_err"].append(kap/(kA/2.0e6)-1)
for k,v in res.items():
    v=np.array(v); s=1000 if k.endswith("_q") or k=="q3m_pair" else 1
    print(f"{k}: bias {v.mean()*s:+.3f} sd {v.std()*s:.3f}", "(mW/m2)" if s==1000 else "(C or frac)")
