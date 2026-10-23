# M34 toy economics: temperature/depth/flow -> LCOE -> $/acre. Inputs marked in M34 file; many are (unverified).
import numpy as np, math
T0=15.0  # surface/dead state C
def exergy_kJkg(T):  # liquid water, dead state 10 C
    Tk,T0k=T+273.15,283.15; cp=4.2+0.001*(T-100)
    return cp*((Tk-T0k)-T0k*math.log(Tk/T0k))
def util_eff(T):  # binary second-law utilisation, ~0.30 at 110C to ~0.45 at 200C (DiPippo-style, unverified)
    return float(np.clip(0.30+0.15*(T-110)/90,0.25,0.47))
def net_kW_per_kgs(T,parasitic=0.15):
    return exergy_kJkg(T)*util_eff(T)*(1-parasitic)
def well_cost_M(z_km):  # large-diameter production well; anchors ~1.8/1km,3.5/2km,6/3km,16.4/5km (Lowry 2017 5km baseline; others unverified)
    zs=[0.5,1,2,3,4,5]; cs=[1.2,1.8,3.5,6.0,10.0,16.4]
    return float(np.interp(z_km,zs,cs))
def plant_kW(T):  # binary surface plant $/kW incl. gathering; ~2600 at 200C to ~4500 at 120C (unverified)
    return float(np.interp(T,[110,120,150,175,200],[5200,4500,3400,2900,2600]))
def lcoe(T,z,flow=60,succ=0.7,inj_ratio=0.6,expl_M_per_MW=0.3,itc=0.3,crf=0.0888,om=160,cf=0.92):
    pw=net_kW_per_kgs(T)*flow/1000  # MW per producer
    wells_per_MW=(1+inj_ratio)/pw/succ
    capex_kW=wells_per_MW*well_cost_M(z)*1e6/1000 + plant_kW(T) + expl_M_per_MW*1000 + 300  # +300 transmission/intertie
    capex_kW*=(1-itc)
    return (capex_kW*crf+om)/(8.76*cf), capex_kW/(1-itc), pw
print("T  MW/(kg/s) per-producer MW@60kg/s")
for T in [120,140,150,175,200]: print(T, round(net_kW_per_kgs(T)/1000,4), round(net_kW_per_kgs(T)*60/1000,1))
print("\nLCOE $/MWh (flow 60 kg/s), rows T, cols depth km 0.5,1,1.5,2,3,4")
ds=[0.5,1,1.5,2,3,4]
for T in [120,135,150,165,180,200]:
    print(T,[round(lcoe(T,z)[0]) for z in ds])
print("\nflow sensitivity at 150C, 1.5 km: ", {f:round(lcoe(150,1.5,flow=f)[0]) for f in [20,40,60,90,120]})
print("capex $/kW at 150C 1.5km:",round(lcoe(150,1.5)[1]))
# minimal temperature to hit LCOE<=P at each depth
for P in [80,100,115]:
    row=[]
    for z in ds:
        Ts=[T for T in range(100,251) if lcoe(T,z)[0]<=P]
        row.append(Ts[0] if Ts else None)
    print("min T for LCOE<=",P,":",dict(zip(ds,row)))
# depth to 150C for gradients (conductive)
for g in [30,40,60,80,120]: print("grad",g,"C/km -> depth to 150C km",round((150-T0)/g,2),"to 120C",round((120-T0)/g,2))
# value to developer per MW: PV of (P-LCOE) margin over 30 yr @8%
def dev_value_M_per_MW(T,z,P=100,flow=60):
    l=lcoe(T,z,flow=flow)[0]; mwh=8.76*0.92*1000
    return max(P-l,0)*mwh/0.0888/1e6
print("\ndeveloper surplus $M/MW at P=100:", {(T,z):round(dev_value_M_per_MW(T,z),2) for T in [135,150,175] for z in [1,2,3]})
# expected $/acre to bank
def ev_acre(p_exist,mw_km2,capture_M_per_MW,p_build=0.4,delay_yr=8,r=0.12,p_in_footprint=0.5):
    return p_exist*p_in_footprint*mw_km2*capture_M_per_MW*1e6*p_build/(1+r)**delay_yr/247.1
print("\nEV $/acre examples:")
for p in [0.005,0.02,0.05,0.2]:
    print("p",p, "override 0.4M/MW, 6 MW/km2:",round(ev_acre(p,6,0.4)), " sale-at-confirm 0.1M/MW, delay 4:",round(ev_acre(p,6,0.1,p_build=1,delay_yr=4)))
