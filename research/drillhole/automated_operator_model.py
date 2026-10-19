# per rig-year, CAD, generic Canadian surface diamond core
days=300; shifts=2
rate=180.0
base_m=15000
drill_day=800; help_day=560; sup_day=1040; tech_day=900
def labour(drillers_ps, helpers_ps, sup_ps=0, tech_ps=0, travel=100e3, foreman=150e3, ops=0):
    pd=days*shifts
    return pd*(drillers_ps*drill_day+helpers_ps*help_day+sup_ps*sup_day+tech_ps*tech_day)+travel+foreman+ops
consum_per_m=400e3/base_m
other_fixed=0.35e6+0.10e6+0.15e6  # rig dep+maint, fuel, overhead
def run(name,lab,capex_cad,extra_opex,prod):
    m=base_m*prod
    cost=lab+consum_per_m*m+other_fixed+capex_cad/5+extra_opex
    rev=m*rate
    print(f"{name}: labour {lab/1e6:.2f}M metres {m:.0f} cost {cost/1e6:.2f}M cost/m {cost/m:.0f} rev {rev/1e6:.2f}M EBIT% {100*(rev-cost)/rev:.0f} labour%rev {100*lab/rev:.0f}")
    return cost/m
b=run("Base", labour(1,2), 0,0,1.0)
a=run("A supervised 1:3.5", labour(0,1,1/3.5,0.25,travel=50e3,foreman=75e3,ops=50e3), 0.82e6,0.10e6,1.15)
c=run("B lights-out 1:4", labour(0,0.5,0.25,0.25,travel=30e3,foreman=50e3,ops=80e3), 1.37e6,0.15e6,1.25)
# experienced drillers per rig on site per day
print("driller-days per rig-day base",2,"A",2/3.5,"B",2/4)
