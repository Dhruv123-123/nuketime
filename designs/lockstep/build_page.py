"""Assemble the LOCKSTEP design report as a single HTML page with embedded figures."""
import base64, json
def b64(p): return "data:image/png;base64," + base64.b64encode(open(p, "rb").read()).decode()
svg = open("figures/schematic.svg").read(); svg = svg[svg.index("<svg"):]
f1, f2, f3, f4, f5 = (b64(f"figures/{n}") for n in ("fig1_island.png", "fig2_threshold.png", "fig3_island24h.png", "fig4_tower.png", "fig5_risk.png"))
S = json.load(open("runs/island.json")); T = json.load(open("runs/tower.json"))["cases"]; R = json.load(open("runs/risk_econ.json"))
i5 = S["island_520"]; ih = S["island_house_only"]; t5 = T["scale1.0_dc500"]; e = R["economics"]; c = R["cdf"]
def row(name, label):
    s = S[name]; flags = ", ".join(k.replace("_", " ") for k, v in s["trips"].items() if v) or "none"
    return f"<tr><td>{label}</td><td class=n>{s['freq_max']:.2f}</td><td class=n>{s['Tavg_max']:.1f}</td><td class=n>{s['P_pz_max']:.2f}</td><td class=n>{s['p_sg_max']:.2f}</td><td class=n>{s['otdt_margin_K']:.1f}</td><td>{'no' if not s['any_trip'] else 'yes'}: {flags}</td></tr>"
rows = "".join(row(n, l) for n, l in [("island_700", "data centre 700 MW (59 %)"), ("island_600", "600 MW (51 %)"), ("island_520", "520 MW (44 %), design case"), ("island_450", "450 MW (38 %)"),
                                       ("island_400", "400 MW (34 %)"), ("island_400_dump50", "400 MW with 50 % steam dump"), ("island_300", "300 MW (25 %)"), ("island_house_only", "house load only (5 %), today's plant"),
                                       ("island_520_step_plus100", "520 MW then +100 MW job start"), ("island_520_step_minus200", "520 MW then −200 MW job kill"), ("island_520_slow_valving", "520 MW, slow valving"), ("island_520_dump60", "520 MW with 60 % steam dump")])
trow = "".join(f"<tr><td>{dc} MW</td><td class=n>{T[f'scale1.0_dc{dc}']['MW_avg_lost']:.1f}</td><td class=n>{T[f'scale1.0_dc{dc}']['MWh_lost_vs_base']/1e3:.0f}</td><td class=n>{T[f'scale1.0_dc{dc}']['Tcold_max']:.1f}</td><td class=n>{T[f'scale1.0_dc{dc}']['dc_supply_p99']:.1f}</td><td class=n>{T[f'scale1.25_dc{dc}']['MW_avg_lost']:.1f}</td></tr>" for dc in (250, 500, 750))

html = f"""<title>Lockstep</title>
<meta name="description" content="A PWR and a data centre engineered as one island: ride-through, shared cooling, shared backup">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Condensed:wght@500;600;700&family=IBM+Plex+Sans:ital,wght@0,400;0,500;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root {{ --paper:#f3f4f1; --paper-2:#e9ebe6; --ink:#12161a; --ink-2:#4b545c; --ink-3:#7c858d; --rule:#cfd4cd; --accent:#1c5cab; --accent-soft:#dbe7f7; --heat:#c9501f; --heat-soft:#f8dccd;
  --mono:"IBM Plex Mono", ui-monospace, Menlo, monospace; --sans:"IBM Plex Sans", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; --disp:"IBM Plex Sans Condensed", "Arial Narrow", system-ui, sans-serif; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ color-scheme:dark; --paper:#15181b; --paper-2:#1d2124; --ink:#eef0ee; --ink-2:#b4bbc1; --ink-3:#8b939b; --rule:#343a3f; --accent:#5598e7; --accent-soft:#1d2f47; --heat:#f08a5e; --heat-soft:#3d2216; }} }}
:root[data-theme="dark"] {{ color-scheme:dark; --paper:#15181b; --paper-2:#1d2124; --ink:#eef0ee; --ink-2:#b4bbc1; --ink-3:#8b939b; --rule:#343a3f; --accent:#5598e7; --accent-soft:#1d2f47; --heat:#f08a5e; --heat-soft:#3d2216; }}
body {{ background:var(--paper); color:var(--ink); font-family:var(--sans); font-size:16px; line-height:1.55; padding-inline:clamp(16px, 4vw, 40px); padding-block:24px 64px; }}
.wrap {{ max-width:1040px; margin:0 auto; }}
.titleblock {{ border:1.5px solid var(--ink); display:grid; grid-template-columns:2fr 1fr; }} .titleblock > div {{ padding:14px 18px; }} .titleblock .name {{ border-right:1.5px solid var(--ink); }}
.titleblock h1 {{ font-family:var(--disp); font-weight:700; font-size:clamp(28px, 5vw, 44px); line-height:1.02; margin:0 0 8px; letter-spacing:-0.01em; }} .titleblock .sub {{ color:var(--ink-2); font-size:17px; max-width:62ch; margin:0; }}
.meta {{ font-family:var(--mono); font-size:12px; color:var(--ink-2); display:grid; grid-template-columns:auto 1fr; gap:4px 12px; align-content:start; }} .meta b {{ color:var(--ink); font-weight:500; }}
@media (max-width:640px) {{ .titleblock {{ grid-template-columns:1fr; }} .titleblock .name {{ border-right:0; border-bottom:1.5px solid var(--ink); }} }}
.kpis {{ display:grid; grid-template-columns:repeat(auto-fit, minmax(150px, 1fr)); gap:1px; background:var(--rule); border:1px solid var(--rule); margin:22px 0 34px; }} .kpi {{ background:var(--paper-2); padding:12px 14px; }}
.kpi .v {{ font-family:var(--mono); font-size:26px; font-weight:500; line-height:1.1; font-variant-numeric:tabular-nums; }} .kpi .v small {{ font-size:14px; color:var(--ink-2); margin-left:3px; }} .kpi .l {{ font-size:12.5px; color:var(--ink-2); margin-top:4px; }}
h2 {{ font-family:var(--disp); font-weight:600; font-size:26px; margin:44px 0 12px; padding-top:14px; border-top:1.5px solid var(--ink); }} h2 .num {{ font-family:var(--mono); font-weight:400; font-size:14px; color:var(--ink-3); margin-right:10px; vertical-align:middle; }}
h3 {{ font-family:var(--disp); font-weight:600; font-size:19px; margin:26px 0 6px; }} p, li {{ max-width:70ch; }} p {{ margin:0 0 12px; }} ul, ol {{ padding-left:22px; margin:0 0 12px; }} li {{ margin-bottom:5px; }}
.lead {{ font-size:18px; max-width:66ch; }} .callout {{ border-left:3px solid var(--accent); background:var(--accent-soft); padding:12px 16px; margin:16px 0 20px; max-width:80ch; }} .callout.heat {{ border-color:var(--heat); background:var(--heat-soft); }}
figure {{ margin:22px 0 28px; }} figure img, figure svg {{ width:100%; height:auto; display:block; border:1px solid var(--rule); background:#fcfcfb; }} figcaption {{ font-size:13.5px; color:var(--ink-2); margin-top:8px; max-width:90ch; }}
.tablewrap {{ overflow-x:auto; margin:14px 0 22px; }} table {{ border-collapse:collapse; width:100%; font-size:14.5px; }} th, td {{ text-align:left; padding:8px 10px; border-bottom:1px solid var(--rule); vertical-align:top; }}
th {{ font-family:var(--disp); font-weight:600; font-size:14px; letter-spacing:0.02em; color:var(--ink-2); border-bottom:1.5px solid var(--ink); }} td.n, th.n {{ text-align:right; font-family:var(--mono); font-variant-numeric:tabular-nums; white-space:nowrap; }}
code, pre {{ font-family:var(--mono); font-size:13.5px; }} pre {{ background:var(--paper-2); padding:12px 14px; overflow-x:auto; border:1px solid var(--rule); }}
.grid2 {{ display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:18px 32px; }} .spec dt {{ font-family:var(--disp); font-weight:600; margin-top:10px; }} .spec dd {{ margin:2px 0 0; color:var(--ink-2); font-size:15px; }}
footer {{ margin-top:56px; padding-top:14px; border-top:1px solid var(--rule); color:var(--ink-3); font-size:13px; }} a {{ color:var(--accent); }}
</style>
<div class="wrap">
<header class="titleblock">
  <div class="name"><h1>Lockstep</h1><p class="sub">A pressurised-water reactor and a data centre engineered as one island: the plant rides through grid loss on the data-centre load, the two share one cooling tower, and the data centre's backup fleet backs the plant's safety buses.</p></div>
  <div class="meta"><span>Drawing</span><b>LS-001 rev A</b><span>Date</span><b>2026-09-28</b><span>Plant</span><b>3,400 MWth / 1,180 MWe PWR</b><span>Load</span><b>520 MW liquid-cooled data centre</b><span>Models</span><b>island.py · tower.py · risk_econ.py</b></div>
</header>
<div class="kpis">
  <div class="kpi"><div class="v">0</div><div class="l">reactor trips on grid loss with the data centre on the island (today: trip)</div></div>
  <div class="kpi"><div class="v">÷190</div><div class="l">station-blackout core-damage frequency with both provisions</div></div>
  <div class="kpi"><div class="v">{t5['MW_avg_lost']:.1f}<small>MW</small></div><div class="l">plant output given up to reject the data centre's 500 MW of heat</div></div>
  <div class="kpi"><div class="v">{e['dc_cooling_capex_avoided_M']:.0f}<small>M USD</small></div><div class="l">data-centre cooling plant not built</div></div>
  <div class="kpi"><div class="v">≥40<small>%</small></div><div class="l">of plant rating: the data-centre load that makes islanding clean</div></div>
</div>
<p class="lead">Every nuclear-plus-data-centre deal so far connects a seller and a buyer with a wire. Physically the two are complements. The plant owns the largest heat-rejection system on the site next to a data centre that builds its own; the data centre owns hundreds of megawatts of tested generators and batteries next to a plant whose worst accident is losing 20 MW of AC; and a data centre of about half the plant's output is exactly the load that lets a PWR ride through a grid loss without tripping.</p>
<figure>{svg}<figcaption>Electrical one-line (top) and heat rejection (bottom). The data-centre feeder hangs on the generator bus so the island survives the switchyard opening; the diverse-AC tie is normally open and sync-checked; data-centre heat enters the circulating water downstream of the condenser.</figcaption></figure>

<h2><span class="num">01</span>What it yields</h2>
<div class="tablewrap"><table>
<tr><th>Quantity</th><th>Value</th></tr>
<tr><td>Grid-loss ride-through</td><td>No reactor trip with a data-centre load ≥ 40 % of rating (40 % steam dump) or ≥ 34 % (50 % dump); design case 44 % with {i5['otdt_margin_K']:.1f} K over-temperature ΔT margin and no safety-valve lift</td></tr>
<tr><td>Station-blackout core-damage frequency (generic fleet inputs)</td><td>{c['baseline']:.1e} per reactor-year baseline; {c['islanding']:.1e} with islanding; {c['dc_ac']:.1e} with the backup-fleet tie; {c['both']:.1e} with both</td></tr>
<tr><td>Plant output given up for shared cooling, 500 MW data centre</td><td>{t5['MW_avg_lost']:.1f} MW annual average ({t5['MW_avg_lost']/1224*100:.1f} %), {t5['MWh_lost_vs_base']/1e3:.0f} GWh per year</td></tr>
<tr><td>Data-centre cooling energy avoided</td><td>about 20 MW (4 % of IT), 175 GWh per year</td></tr>
<tr><td>Data-centre cooling plant not built</td><td>about {e['dc_cooling_capex_avoided_M']:.0f} M USD (dry coolers, towers, evaporative plant at 250 USD per kW; heat exchangers and CDUs remain)</td></tr>
<tr><td>System capital</td><td>about {e['system_capex_M']:.0f} M USD: heat exchangers and piping 40, safety-bus tie 35, islanding controls and testing 15</td></tr>
<tr><td>Net</td><td>+{e['net_annual_M']:.0f} M USD per year in energy, +{e['net_capex_M']:.0f} M USD in capital, plus the safety and reliability outcomes</td></tr>
<tr><td>Water the data centre receives</td><td>26 to 35 °C; 99th percentile {t5['dc_supply_p99']:.1f} °C; never above the ASHRAE W40 liquid-cooling class</td></tr>
</table></div>
<p>The money is positive but modest. The point is the two things money does not capture: the plant becomes materially safer, and the data centre gets power that survives the grid rather than power that depends on it.</p>

<h2><span class="num">02</span>Lineage and what is new</h2>
<p>House-load operation, running back to the plant's own auxiliaries on grid loss, is an established capability in German, French and Korean plants and the subject of a GE patent (US 9,620,252); Korean safety assessments credit it. Most US plants are not designed for it, and full rejection to a 5 % house load is the hardest load-rejection transient there is, which is why many cannot do it. Loss of offsite power and station blackout are the largest contributors to core-damage frequency at many PWRs (NUREG/CR-6890). Data centres co-located with nuclear plants buy power across the switchyard and build their own cooling, batteries and generators.</p>
<p>Lockstep adds three things, none implemented and none found engineered together: the data-centre load as the island load, which turns the hardest load rejection into an ordinary 50 % one; the data centre's backup fleet credited as a diverse AC source in the plant's blackout defence; and one heat-rejection system for both.</p>

<h2><span class="num">03</span>Design</h2>
<div class="grid2">
<dl class="spec">
<dt>Generator-bus feeder</dt><dd>600 MVA, 24/34.5 kV transformer on the generator side of the generator circuit breaker. On a grid fault the switchyard opens; generator, unit auxiliary transformer and data-centre feeder remain one island.</dd>
<dt>Island control</dt><dd>Governor switches to frequency control (4 % droop with slow restoration); fast valving (full stroke in 0.3 s) armed by the breaker-open signal; steam dump load-rejection controller opens on power mismatch; rods run back at full speed until reactor power meets the island load. Standard Westinghouse-class functions; the change is setpoints and a tested procedure.</dd>
<dt>Data centre as load</dt><dd>Constant-power electronic load with 520 MW / 10 min of UPS batteries that ride through the first second and give fast frequency response on the island. Training jobs pause, so load can be shed in blocks if the island needs it.</dd>
</dl>
<dl class="spec">
<dt>Diverse-AC tie</dt><dd>34.5/4.16 kV transformer from the data centre's generator bus to each safety bus through a normally open, sync-checked, seismically qualified breaker. The N+1 generator fleet (560 MW) and batteries are credited like FLEX equipment, but permanently connected and automatically started.</dd>
<dt>Shared heat rejection</dt><dd>12 m³/s tapped from the tower basin (28 % of the 43,400 kg/s circulating flow) through plate heat exchangers with a 2 K pinch; warmed water rejoins the hot return downstream of the condenser, so the condenser's range is unchanged and the only plant penalty is the 0.6 K rise in tower cold water at the design day. Closed treated loop on the data-centre side with a 12 K rise.</dd>
<dt>Not changed</dt><dd>The reactor, its safety systems and its accident licensing basis. The tie is an addition on the supply side of the safety buses, behind isolation devices, where a FLEX connection sits today.</dd>
</dl>
</div>

<h2><span class="num">04</span>Results: islanding</h2>
<figure><img src="{f1}" alt="Six panels of the islanding transient: frequency, reactor power with steam and dump, coolant temperature, pressuriser pressure, steam generator pressure and rod reactivity, for the island case and the house-load-only case"><figcaption>Loss of grid at full power. With the 520 MW data centre on the island the plant settles at 49 % power in two minutes with every limit intact; the same plant rejecting to house load alone exceeds the pressuriser trip setpoint and lifts the steam-generator safety valves within the first minute.</figcaption></figure>
<div class="tablewrap"><table>
<tr><th>Case</th><th class="n">peak Hz</th><th class="n">peak Tavg °C</th><th class="n">peak pressuriser MPa</th><th class="n">peak SG MPa</th><th class="n">OTΔT margin K</th><th>trip</th></tr>
{rows}
</table></div>
<figure><img src="{f2}" alt="Peak pressuriser pressure, steam generator pressure and coolant temperature versus data-centre load for several steam-dump capacities"><figcaption>The minimum island load. With a typical 40 % steam dump the plant needs the data centre at 40 % of rating or more; a 50 % dump lowers that to 34 %; a 60 % dump avoids even the relief-valve lift at the design point.</figcaption></figure>
<figure><img src="{f3}" alt="Reactor power, xenon and rod reactivity over 24 hours on the island"><figcaption>Twenty-four hours on the island: the xenon transient after the power drop is compensated by rod withdrawal within the model's rod worth.</figcaption></figure>

<h2><span class="num">05</span>Results: shared cooling</h2>
<div class="tablewrap"><table>
<tr><th>Data-centre load</th><th class="n">plant loss, MW avg</th><th class="n">GWh per year</th><th class="n">max tower cold water °C</th><th class="n">DC supply p99 °C</th><th class="n">loss with 25 % more tower cells, MW</th></tr>
{trow}
</table></div>
<figure><img src="{f4}" alt="Plant output lost versus data-centre load and the cooling energy the data centre avoids; histogram of the wet-bulb year with the data-centre supply water temperature marked"><figcaption>The plant gives up a fifth of what the data centre saves in fan power. More tower cells barely help because the condenser range and terminal difference, not the tower approach, set the plant's back pressure at this water flow.</figcaption></figure>

<h2><span class="num">06</span>Results: blackout risk</h2>
<figure><img src="{f5}" alt="Stacked bars of station-blackout core-damage frequency by loss-of-offsite-power category for the baseline and the three Lockstep configurations, log scale"><figcaption>Order-of-magnitude PRA with generic fleet inputs. Grid- and weather-related events dominate the baseline and are exactly the ones islanding removes; the backup-fleet tie multiplies what remains by the probability that a second, diverse fleet also fails.</figcaption></figure>

<h2><span class="num">07</span>Failure modes and limits</h2>
<div class="tablewrap"><table>
<tr><th>Item</th><th>Assessment</th></tr>
<tr><td>Islanding fails (valve, dump or control fault)</td><td>The plant trips as it would today; the PRA credit rests on the island function's reliability, taken as 90 %</td></tr>
<tr><td>Data centre trips off during the island</td><td>A second 45 % load loss from 50 % power; the plant runs back toward house load and will likely trip. Batteries and staged load shedding are the mitigation</td></tr>
<tr><td>Safety-bus tie misoperation</td><td>Normally open; sync-check and interlocks against paralleling onto a faulted bus; qualified breaker; single-failure criteria unchanged because the tie is additional</td></tr>
<tr><td>Common-cause loss of both fleets (flood, seismic)</td><td>Qualified tie; diverse generator types and locations; weather correlation included in the risk model</td></tr>
<tr><td>Heat-exchanger leak</td><td>Conductivity monitoring and isolation; the data centre reverts to reduced load</td></tr>
<tr><td>Hot summer at full data-centre load</td><td>Cold water peaks at {t5['Tcold_max']:.1f} °C, supply {t5['dc_supply_max']:.1f} °C, within W40</td></tr>
<tr><td>Regulatory</td><td>Behind-the-meter load on the generator bus and a diverse AC tie both need NRC and grid-operator review; the interconnection dispute over Susquehanna shows that side is not trivial</td></tr>
</table></div>
<div class="callout heat"><b>What it does not do.</b> It does not raise the plant's efficiency, and the money is modest. A reactor trip still hands the data centre to its own batteries and generators, as today.</div>

<h2><span class="num">08</span>Open questions</h2>
<ol>
<li>Plant-specific load-rejection capability: the model is a generic four-loop PWR; designs with smaller dumps or slower rods need the 50 % dump case.</li>
<li>Island frequency and voltage control with a large constant-power electronic load; UPS inverter response and grid-forming capability need a hardware-in-the-loop test.</li>
<li>PRA credit for a non-safety AC source: the FLEX precedent and the tie's qualification.</li>
<li>Real climate data and the plant's actual circulating-water flow for the tower penalty.</li>
<li>Boron dilution over a longer island; the 24 h case relies on rod worth.</li>
</ol>
<h2><span class="num">09</span>Reproducing the results</h2>
<pre>pip install numpy scipy matplotlib iapws
python3 island.py      # transient cases
python3 tower.py       # hourly year, about 2.5 min
python3 risk_econ.py   # blackout risk and economics
python3 plots.py       # figures</pre>
<footer>Lockstep design study, 2026-09-28. Models, runs and figures live in <code>designs/lockstep/</code> of the nuketime repository. Risk inputs are generic order-of-magnitude values; prior-art statements reflect searches made on that date and are not a legal opinion.</footer>
</div>
"""
open("lockstep.html", "w").write(html)
print("wrote lockstep.html", len(html) // 1024, "KB")
