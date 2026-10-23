# P02 dart noise simulator (1D conduction, seasonal + weather + interannual forcing, moisture-varying k).
# Usage: python3 P02_dart_sim.py 0 30   -> paired-dart flux-difference error by sensor layout.
# Note: the naive 12-month-mean gradient fit; the single-dart forced inversion tried in scratch was not robust and is not included.
import numpy as np, sys
rng=np.random.default_rng(int(sys.argv[1]) if len(sys.argv)>1 else 0)
def run(q=0.08,kamp=0.2,interann=0.5,k0=1.0,C=2.0e6,years_spin=4,years_rec=1,seed=0,lid_moist=True,depths=(0.5,1,1.5,2,2.5,3.0),noise=0.01,wet_k_top=1.5):
    rng=np.random.default_rng(seed)
    L=12.0; dz=0.1; z=np.arange(0,L+dz/2,dz); n=len(z)
    dt=3600*0.5; yr=365.25*86400; w=2*np.pi/yr
    nsteps=int((years_spin+years_rec)*yr/dt)
    # initial steady
    dd=np.sqrt(2*(k0/C)/w)
    T=16+q/k0*z+13*np.exp(-z/dd)*np.cos(-z/dd-np.pi*0.55)
    # weather: AR1 noise 3C, tau 3 days ; interannual: random yearly mean offset
    a=np.exp(-dt/(3*86400)); wx=0.0
    yoff=rng.normal(0,interann,years_spin+years_rec+1)
    rec=[];tt=[]
    kap_lim=0.5*dz*dz/dt
    for s in range(nsteps):
        t=s*dt
        yi=int(t/yr)
        # smooth interannual offset (linear interp)
        f=t/yr-yi; off=yoff[yi]*(1-f)+yoff[yi+1]*f
        wx=a*wx+np.sqrt(1-a*a)*rng.normal(0,3.0)
        Ts=16+13*np.cos(w*t-np.pi*0.55)+wx+off
        # k(z,t): top 1.5 m varies with moisture: wet in winter/spring (higher k)
        k=np.full(n,k0)
        if kamp>0:
            m=np.cos(w*t-np.pi*0.1)  # wet ~ Feb
            top=z<1.5
            k[top]=k0*(1+kamp*m)
        # explicit FD in flux form
        kh=0.5*(k[1:]+k[:-1])
        flux=-kh*(T[1:]-T[:-1])/dz
        dT=np.zeros(n)
        dT[1:-1]=-(flux[1:]-flux[:-1])/dz
        dT[-1]=-(-q - flux[-1])/dz  # basal flux q upward = -k dT/dz => heat in from below
        # stability
        T=T+dt*dT/C
        T[0]=Ts
        if t>=years_spin*yr:
            rec.append(np.interp(depths,z,T)); tt.append(t)
    rec=np.array(rec); 
    # add sensor noise and fixed offsets
    off_s=rng.normal(0,noise,len(depths))
    obs=rec+off_s+rng.normal(0,noise,rec.shape)
    return np.array(depths),np.array(tt),obs,q/k0
def fitG(d,obs):
    m=obs.mean(0)
    A=np.vstack([np.ones_like(d),d]).T
    c,*_=np.linalg.lstsq(A,m,rcond=None)
    return c[1]
if __name__=="__main__":
    cfg={"2m logged (1,1.5,2)":(1.0,1.5,2.0),"3m dart (0.5..3)":(0.5,1.0,1.5,2.0,2.5,3.0),"3m dart deep3 (2,2.5,3)":(2.0,2.5,3.0)}
    out={k:[] for k in cfg}; out1={k:[] for k in cfg}
    r=np.random.default_rng(7)
    for sd in range(int(sys.argv[1]),int(sys.argv[2])):
        kA=1.0; kB=float(np.clip(1.0*np.exp(r.normal(0,0.3)),0.4,1.8))   # soil k differs ~30%
        CA=2.0e6; CB=float(2.0e6*np.exp(r.normal(0,0.15)))
        kaA=0.3*r.uniform(); kaB=0.3*r.uniform()
        # same weather/interannual seed -> common forcing
        deps=(0.5,1.0,1.5,2.0,2.5,3.0)
        dA,t,oA,GA=run(q=0.08,k0=kA,C=CA,kamp=kaA,interann=0.5,seed=sd,depths=deps)
        dB,t,oB,GB=run(q=0.08,k0=kB,C=CB,kamp=kaB,interann=0.5,seed=sd,depths=deps)
        # heater k estimate with 10% error
        kAh=kA*(1+0.1*r.normal()); kBh=kB*(1+0.1*r.normal())
        for name,dd in cfg.items():
            idx=[deps.index(x) for x in dd]
            gA=fitG(np.array(dd),oA[:,idx]); gB=fitG(np.array(dd),oB[:,idx])
            out[name].append(kAh*gA-kBh*gB)      # with heater k
            out1[name].append(1.0*gA-1.0*gB)     # no k: assume k=1 (flux error from unknown k)
    for name in cfg:
        a=np.array(out[name])*1000; b=np.array(out1[name])*1000
        print(f"{name}: dq with heater k  bias {a.mean():+.0f} sd {a.std():.0f} mW/m2 | without k  bias {b.mean():+.0f} sd {b.std():.0f}",flush=True)
