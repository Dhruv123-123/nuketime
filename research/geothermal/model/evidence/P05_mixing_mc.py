import numpy as np
rng=np.random.default_rng(1)
def Sq(T): # quartz no steam loss, Fournier 1977: T=1309/(5.19-log10 S)-273.15
    return 10**(5.19-1309/(T+273.15))
def Tq(S): return 1309/(5.19-np.log10(S))-273.15
Td,Tc=150.,15.; Sd=Sq(Td); Sc=30.; Cld,Clc=500.,20.
print("Sd",Sd)
Tgrid=np.linspace(40,300,5000)
def solve(slope_ST, Sc_, Tc_):
    # line S = Sc + slope*(T-Tc) (temperature as enthalpy proxy, cp const); intersect quartz curve
    f=Sq(Tgrid)-(Sc_+slope_ST*(Tgrid-Tc_))
    idx=np.where(np.diff(np.sign(f))!=0)[0]
    return Tgrid[idx[-1]] if len(idx) else np.nan
def sim(xs,cold_sd_S=1.5,cold_known=False,nrep=2000,sS=0.02,sT=0.05,sCl=0.02,cool=0.0):
    out=[]
    for r in range(nrep):
        n=len(xs)
        # cold endmember varies sample to sample (zone mixing) 
        Sc_i=Sc+rng.normal(0,cold_sd_S,n); Clc_i=Clc*(1+rng.normal(0,0.05,n)); Tc_i=Tc+rng.normal(0,0.3,n)
        S=xs*Sd+(1-xs)*Sc_i; Cl=xs*Cld+(1-xs)*Clc_i; T=xs*Td*(1-cool)+(1-xs)*Tc_i + xs*Td*cool*0  # cool: fraction of excess heat lost
        T=xs*(Tc+(Td-Tc)*(1-cool))+(1-xs)*Tc_i
        S=S*(1+rng.normal(0,sS,n)); Cl=Cl*(1+rng.normal(0,sCl,n)); T=T+rng.normal(0,sT,n)
        if n>=3 and np.ptp(xs)>0:
            # regress S on T and T,S on Cl ; slope S/T from ratio of Cl-slopes (errors-in-variables robust)
            bS=np.polyfit(Cl,S,1)[0]; bT=np.polyfit(Cl,T,1)[0]
            slope=bS/bT
            # cold point = intercept at Cl=Clc (cold Cl from regional cold well, sd 5%)
            Sc_e=np.polyval(np.polyfit(Cl,S,1),Clc); Tc_e=np.polyval(np.polyfit(Cl,T,1),Clc)
        else:
            # single/flat: average mixed point plus separately sampled cold well (one sample, with cold variability)
            Sm,Tm=S.mean(),T.mean()
            Sc_e=Sc+rng.normal(0,cold_sd_S); Tc_e=Tc+rng.normal(0,0.3)
            slope=(Sm-Sc_e)/(Tm-Tc_e)
        out.append(solve(slope,Sc_e,Tc_e))
    o=np.array(out); o=o[np.isfinite(o)]
    return np.median(o), np.percentile(o,16), np.percentile(o,84), len(o)/nrep
for lab,xs in [("single x=.075",np.array([.075])),("flat 30 x=.075",np.full(30,.075)),
               ("vary 30 x .05-.10",np.linspace(.05,.10,30)),("vary 30 x .05-.20",np.linspace(.05,.20,30)),
               ("vary 30 x .02-.05",np.linspace(.02,.05,30))]:
    print(lab, ["%.1f"%v for v in sim(xs)])
print("with 30% conductive heat loss:")
for lab,xs in [("single",np.array([.075])),("vary .05-.20",np.linspace(.05,.20,30))]:
    print(lab, ["%.1f"%v for v in sim(xs,cool=0.3)])
# Cl-only check of signal
x=0.05; print("Cl at 5%:",x*Cld+(1-x)*Clc,"B",x*5+(1-x)*0.1,"Li",x*1+(1-x)*0.02,"SiO2",x*Sd+(1-x)*Sc,"T",x*Td+(1-x)*Tc)
# naive chalcedony single-sample T at 7.5%
S=0.075*Sd+0.925*Sc; print("naive chalcedony T", 1032/(4.69-np.log10(S))-273.15, "quartz",Tq(S))
