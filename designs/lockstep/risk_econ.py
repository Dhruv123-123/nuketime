"""
LOCKSTEP sub-model C: station-blackout risk with (a) islanding onto the data centre and (b) the
data centre's backup fleet as a diverse AC source to the plant's safety buses; plus the economics
of the whole arrangement.

Risk numbers are generic-fleet order-of-magnitude values in the style of NUREG/CR-6890
(2005) and are labelled as such; a plant-specific PRA would replace them.
"""
import json

# LOOP initiating-event frequency per reactor-critical-year, by category (approximate industry values)
LOOP = dict(plant_centered=0.0025, switchyard_centered=0.0100, grid_related=0.0190, weather_related=0.0043)
# probability that offsite power is NOT recovered within the plant's SBO coping time (~4 h), by category
NONREC_4H = dict(plant_centered=0.05, switchyard_centered=0.08, grid_related=0.10, weather_related=0.40)
# emergency AC: two diesel trains, per-train unavailability incl. fail-to-start and fail-to-run over the mission, with common cause
EDG_TRAIN = 0.02
EDG_CCF_BETA = 0.05
P_EDG_ALL = EDG_TRAIN ** 2 + EDG_CCF_BETA * EDG_TRAIN
# conditional core damage given SBO not recovered within coping time (turbine-driven AFW, batteries, FLEX)
P_CD_GIVEN_SBO = 0.5

def sbo_cdf(islanding=False, dc_ac=False, p_island_success=0.9, p_dc_ac_fail=0.02, p_dc_ac_fail_weather=0.05):
    total = 0.0; detail = {}
    for cat, f in LOOP.items():
        f_eff = f
        if islanding:
            # an external-grid or weather LOOP that the unit rides through is not a plant LOOP at all
            if cat in ("grid_related", "weather_related"):
                f_eff = f * (1 - p_island_success)
            elif cat == "switchyard_centered":
                f_eff = f * (1 - 0.5 * p_island_success)     # tie is on the generator bus; half of switchyard faults still isolate it
        p_ac_fail = P_EDG_ALL
        if dc_ac:
            p_ac_fail *= (p_dc_ac_fail_weather if cat == "weather_related" else p_dc_ac_fail)
        cdf = f_eff * p_ac_fail * NONREC_4H[cat] * P_CD_GIVEN_SBO
        detail[cat] = dict(f_loop=f, f_eff=f_eff, p_ac_fail=p_ac_fail, cdf=cdf)
        total += cdf
    return total, detail

def economics(dc_mw=500.0, plant_loss_mw_avg=2.0, price=80.0, dc_cooling_capex_per_kw=250.0, dc_cooling_energy_frac=0.04,
              hx_piping_capex=40e6, tie_capex=35e6, islanding_upgrade_capex=15e6, trips_avoided_per_yr=0.07, trip_cost=3e6):
    hours = 8760
    plant_loss = plant_loss_mw_avg * hours * price
    dc_energy_saved = dc_mw * dc_cooling_energy_frac * hours * price
    dc_capex_saved = dc_mw * 1e3 * dc_cooling_capex_per_kw
    capex = hx_piping_capex + tie_capex + islanding_upgrade_capex
    trips = trips_avoided_per_yr * trip_cost
    return dict(plant_output_loss_M_per_yr=plant_loss / 1e6, dc_cooling_energy_saved_M_per_yr=dc_energy_saved / 1e6,
                dc_cooling_capex_avoided_M=dc_capex_saved / 1e6, system_capex_M=capex / 1e6, avoided_trips_M_per_yr=trips / 1e6,
                net_annual_M=(dc_energy_saved + trips - plant_loss) / 1e6, net_capex_M=(dc_capex_saved - capex) / 1e6)

if __name__ == "__main__":
    base, dbase = sbo_cdf()
    isl, disl = sbo_cdf(islanding=True)
    dca, ddca = sbo_cdf(dc_ac=True)
    both, dboth = sbo_cdf(islanding=True, dc_ac=True)
    out = dict(cdf=dict(baseline=base, islanding=isl, dc_ac=dca, both=both), detail=dict(baseline=dbase, islanding=disl, dc_ac=ddca, both=dboth),
               inputs=dict(LOOP=LOOP, NONREC_4H=NONREC_4H, EDG_TRAIN=EDG_TRAIN, EDG_CCF_BETA=EDG_CCF_BETA, P_EDG_ALL=P_EDG_ALL, P_CD_GIVEN_SBO=P_CD_GIVEN_SBO))
    print(f"SBO core-damage frequency per reactor-year: baseline {base:.2e}; islanding {isl:.2e} (x{isl/base:.2f}); DC AC source {dca:.2e} (x{dca/base:.3f}); both {both:.2e} (x{both/base:.4f})")
    try:
        tw = json.load(open("runs/tower.json"))["cases"]
        loss = tw["scale1.0_dc500"]["MW_avg_lost"]
    except Exception:
        loss = 2.0
    econ = economics(plant_loss_mw_avg=loss)
    out["economics"] = econ
    for k, v in econ.items():
        print(f"  {k}: {v:.1f}")
    json.dump(out, open("runs/risk_econ.json", "w"), indent=1)
