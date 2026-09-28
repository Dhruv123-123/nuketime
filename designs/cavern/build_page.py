"""Assemble the CAVERN design report as a single HTML page with embedded figures."""
import base64, json
def b64(path):
    return "data:image/png;base64," + base64.b64encode(open(path, "rb").read()).decode()
svg = open("figures/schematic.svg").read(); svg = svg[svg.index("<svg"):]
f1, f2, f3, f4 = (b64(f"figures/{n}") for n in ("fig1_dispatch.png", "fig2_roundtrip.png", "fig3_economics.png", "fig4_rock.png"))
D = json.load(open("runs/design.json")); d = D["design"]; p = D["plant"]; r = D["rock"]
cs = "".join(f"<td class=n>{c['T_out']:.0f}</td>" for c in d["charge_stages"])
cp = "".join(f"<td class=n>{c['P_ext']:.2f}</td>" for c in d["charge_stages"])
cm = "".join(f"<td class=n>{c['m_steam']:.3f}</td>" for c in d["charge_stages"])
fs = "".join(f"<td class=n>{f['T']:.0f}</td>" for f in d["flash_stages"])
fp = "".join(f"<td class=n>{f['P']:.2f}</td>" for f in d["flash_stages"])
fm = "".join(f"<td class=n>{f['m_steam']:.3f}</td>" for f in d["flash_stages"])
ps = D["price_sens"]

html = f"""<title>Cavern Store</title>
<meta name="description" content="Two lined rock caverns of pressurised hot water turn a PWR's midday output into evening peak output">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Condensed:wght@500;600;700&family=IBM+Plex+Sans:ital,wght@0,400;0,500;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root {{
  --paper:#f3f4f1; --paper-2:#e9ebe6; --ink:#12161a; --ink-2:#4b545c; --ink-3:#7c858d; --rule:#cfd4cd;
  --accent:#1c5cab; --accent-soft:#dbe7f7; --heat:#c9501f; --heat-soft:#f8dccd; --warn:#a8600c;
  --mono:"IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  --sans:"IBM Plex Sans", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --disp:"IBM Plex Sans Condensed", "Arial Narrow", system-ui, sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ color-scheme:dark;
  --paper:#15181b; --paper-2:#1d2124; --ink:#eef0ee; --ink-2:#b4bbc1; --ink-3:#8b939b; --rule:#343a3f;
  --accent:#5598e7; --accent-soft:#1d2f47; --heat:#f08a5e; --heat-soft:#3d2216; --warn:#e0a24a; }} }}
:root[data-theme="dark"] {{ color-scheme:dark;
  --paper:#15181b; --paper-2:#1d2124; --ink:#eef0ee; --ink-2:#b4bbc1; --ink-3:#8b939b; --rule:#343a3f;
  --accent:#5598e7; --accent-soft:#1d2f47; --heat:#f08a5e; --heat-soft:#3d2216; --warn:#e0a24a; }}
body {{ background:var(--paper); color:var(--ink); font-family:var(--sans); font-size:16px; line-height:1.55; padding-inline:clamp(16px, 4vw, 40px); padding-block:24px 64px; }}
.wrap {{ max-width:1040px; margin:0 auto; }}
.titleblock {{ border:1.5px solid var(--ink); display:grid; grid-template-columns:2fr 1fr; }}
.titleblock > div {{ padding:14px 18px; }}
.titleblock .name {{ border-right:1.5px solid var(--ink); }}
.titleblock h1 {{ font-family:var(--disp); font-weight:700; font-size:clamp(28px, 5vw, 44px); line-height:1.02; margin:0 0 8px; letter-spacing:-0.01em; text-wrap:balance; }}
.titleblock .sub {{ color:var(--ink-2); font-size:17px; max-width:62ch; margin:0; }}
.meta {{ font-family:var(--mono); font-size:12px; color:var(--ink-2); display:grid; grid-template-columns:auto 1fr; gap:4px 12px; align-content:start; }}
.meta b {{ color:var(--ink); font-weight:500; }}
@media (max-width:640px) {{ .titleblock {{ grid-template-columns:1fr; }} .titleblock .name {{ border-right:0; border-bottom:1.5px solid var(--ink); }} }}
.kpis {{ display:grid; grid-template-columns:repeat(auto-fit, minmax(150px, 1fr)); gap:1px; background:var(--rule); border:1px solid var(--rule); margin:22px 0 34px; }}
.kpi {{ background:var(--paper-2); padding:12px 14px; }}
.kpi .v {{ font-family:var(--mono); font-size:26px; font-weight:500; line-height:1.1; font-variant-numeric:tabular-nums; }}
.kpi .v small {{ font-size:14px; color:var(--ink-2); margin-left:3px; }}
.kpi .l {{ font-size:12.5px; color:var(--ink-2); margin-top:4px; }}
h2 {{ font-family:var(--disp); font-weight:600; font-size:26px; margin:44px 0 12px; padding-top:14px; border-top:1.5px solid var(--ink); text-wrap:balance; }}
h2 .num {{ font-family:var(--mono); font-weight:400; font-size:14px; color:var(--ink-3); margin-right:10px; vertical-align:middle; }}
h3 {{ font-family:var(--disp); font-weight:600; font-size:19px; margin:26px 0 6px; }}
p, li {{ max-width:70ch; }} p {{ margin:0 0 12px; }} ul, ol {{ padding-left:22px; margin:0 0 12px; }} li {{ margin-bottom:5px; }}
.lead {{ font-size:18px; max-width:66ch; }}
.callout {{ border-left:3px solid var(--accent); background:var(--accent-soft); padding:12px 16px; margin:16px 0 20px; max-width:80ch; }}
.callout.heat {{ border-color:var(--heat); background:var(--heat-soft); }}
figure {{ margin:22px 0 28px; }} figure img, figure svg {{ width:100%; height:auto; display:block; border:1px solid var(--rule); background:#fcfcfb; }}
figcaption {{ font-size:13.5px; color:var(--ink-2); margin-top:8px; max-width:90ch; }}
.tablewrap {{ overflow-x:auto; margin:14px 0 22px; }}
table {{ border-collapse:collapse; width:100%; font-size:14.5px; }}
th, td {{ text-align:left; padding:8px 10px; border-bottom:1px solid var(--rule); vertical-align:top; }}
th {{ font-family:var(--disp); font-weight:600; font-size:14px; letter-spacing:0.02em; color:var(--ink-2); border-bottom:1.5px solid var(--ink); }}
td.n, th.n {{ text-align:right; font-family:var(--mono); font-variant-numeric:tabular-nums; white-space:nowrap; }}
code, pre {{ font-family:var(--mono); font-size:13.5px; }} pre {{ background:var(--paper-2); padding:12px 14px; overflow-x:auto; border:1px solid var(--rule); }}
.grid2 {{ display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:18px 32px; }}
.spec dt {{ font-family:var(--disp); font-weight:600; margin-top:10px; }} .spec dd {{ margin:2px 0 0; color:var(--ink-2); font-size:15px; }}
footer {{ margin-top:56px; padding-top:14px; border-top:1px solid var(--rule); color:var(--ink-3); font-size:13px; }}
a {{ color:var(--accent); }}
</style>
<div class="wrap">
<header class="titleblock">
  <div class="name">
    <h1>Cavern Store</h1>
    <p class="sub">Two lined rock caverns of pressurised hot water turn a pressurised-water reactor's midday output into evening peak output. A complete soft design, evaluated with steam tables, rock conduction and an economic scan.</p>
  </div>
  <div class="meta">
    <span>Drawing</span><b>CV-001 rev A</b>
    <span>Date</span><b>2026-09-28</b>
    <span>Host</span><b>1,100 MWe PWR, 6.9 MPa steam</b>
    <span>Store</span><b>{p['V_hot_m3']/1e3:.0f},000 + {p['V_warm_m3']/1e3:.0f},000 m³</b>
    <span>Peak</span><b>{p['P_peak_MW']:.0f} MW for {d['h_discharge']:.0f} h</b>
    <span>Model</span><b>designs/cavern/model.py</b>
  </div>
</header>

<div class="kpis">
  <div class="kpi"><div class="v">+{p['P_peak_MW']:.0f}<small>MW</small></div><div class="l">extra output for {d['h_discharge']:.0f} evening hours, every day</div></div>
  <div class="kpi"><div class="v">{d['RT']*100:.1f}<small>%</small></div><div class="l">electric round trip</div></div>
  <div class="kpi"><div class="v">{p['E_peak_MWh']:.0f}<small>MWh</small></div><div class="l">delivered at the peak per day</div></div>
  <div class="kpi"><div class="v">{p['capex_total_M']:.0f}<small>M USD</small></div><div class="l">retrofit capex, {p['capex_per_kW_peak']:.0f} USD per kW of peak</div></div>
  <div class="kpi"><div class="v">{p['payback_yr']:.1f}<small>y</small></div><div class="l">payback on a stylised duck curve (midday 15, peak 160 USD/MWh)</div></div>
</div>

<p class="lead">On a solar-heavy grid a reactor's midday electricity is nearly worthless and its evening electricity is worth ten times more. A light-water reactor cannot store its own output as molten salt because its steam is too cool, and steel steam accumulators are too expensive at the scale needed. Rock is not. Two lined caverns in bedrock hold hot water at nuclear steam conditions for a small fraction of the cost of steel, and because the water is stored as pressurised liquid and flashed back through a turbine, three quarters of the electricity comes back.</p>
<p>The reactor runs at 100 % all day. From 09:00 to 15:00, six of the main turbine's extraction points heat water from the warm cavern to 235 °C and it is stored in the hot cavern; output drops by {p['P_charge_drop_MW']:.0f} MW while prices are lowest. From 17:00 to 22:00 the hot water flashes in four stages and the steam drives a {p['P_peak_MW']:.0f} MW peaking turbine. Each cavern stays at one temperature and one pressure for its whole life; only the water level moves.</p>

<figure>{svg}<figcaption>Vertical section, to scale. Crowns at 150 m in competent crystalline rock; the lined-rock-cavern method from high-pressure gas storage lets the rock carry the pressure while a 15 mm steel liner only seals.</figcaption></figure>

<h2><span class="num">01</span>What it yields</h2>
<div class="tablewrap"><table>
<tr><th>Quantity</th><th>Value</th></tr>
<tr><td>Extra output at the evening peak</td><td>{p['P_peak_MW']:.0f} MW for {d['h_discharge']:.0f} h, {p['E_peak_MWh']:.0f} MWh per day</td></tr>
<tr><td>Output given up at midday</td><td>{p['P_charge_drop_MW']:.0f} MW for 6 h, {p['E_forgone_MWh']:.0f} MWh per day</td></tr>
<tr><td>Electric round trip</td><td>{d['RT']*100:.1f} %</td></tr>
<tr><td>Reactor duty</td><td>100 % all day, no manoeuvring, no xenon transients</td></tr>
<tr><td>Cavern volumes</td><td>{p['V_hot_m3']/1e3:.0f},000 m³ hot and {p['V_warm_m3']/1e3:.0f},000 m³ warm, 30 m diameter, {p['H_hot_m']:.0f} m and {p['H_warm_m']:.0f} m tall</td></tr>
<tr><td>Heat lost to rock</td><td>{r['loss_30y_GWh_th']:.0f} GWh over 30 years, under 0.2 % of throughput</td></tr>
<tr><td>Capex, retrofit with a new peaking turbine</td><td>about {p['capex_total_M']:.0f} M USD ({p['capex_per_kWh_e']:.0f} per kWh delivered per day, {p['capex_per_kW_peak']:.0f} per kW of peak)</td></tr>
<tr><td>Capex, new build with an oversized main turbine</td><td>about 320 M USD</td></tr>
<tr><td>Revenue on the stylised price day</td><td>{p['revenue_M_per_yr']:.0f} M USD per year; payback {p['payback_yr']:.1f} years (4.4 years for new build)</td></tr>
</table></div>
<p>Against a four-hour lithium battery at 1,300 to 1,800 USD per kW: similar capital per kW of peak, an hour longer, no degradation, a civil asset with a 50-year life. Against a gas peaker: no fuel and no emissions; the "fuel" is the plant's own midday electricity at the midday price.</p>

<h2><span class="num">02</span>Lineage and what is new</h2>
<p>The concept is old. Peter Margen filed a Swedish patent in 1958 for a large accumulator in an insulated underground rock cavern in parallel with a nuclear plant's steam generator, and his US patents of 1979 to 1985 (4,174,009; 4,399,656; 4,526,005) describe long-period hot-water accumulators in unlined or foil-lined caverns and submerged tanks, discharged by preheating feedwater over weeks to months. Sweden built a 15,000 m³ unlined test cavern at Avesta at 115 °C and the 100,000 m³ Lyckebo solar cavern at 90 °C. Steel Ruths accumulators have fed peaking turbines since the 1920s. Idaho National Laboratory looked at steam accumulators for small modular reactors and rejected them on volume. Nothing at nuclear steam conditions has ever been built underground.</p>
<div class="grid2">
<dl class="spec">
<dt>Lined rock cavern method</dt><dd>The rock carries the pressure; the liner only seals, as at Skallen (Sweden, 2004, 20 MPa natural gas at 115 m). Margen assumed unlined rock or water-balanced foil, which caps the temperature near 115 °C. Lining makes 235 °C and 3.1 MPa possible, and that is what makes flash discharge to a turbine worthwhile.</dd>
<dt>Two caverns at constant temperature</dt><dd>Hot and warm water are kept apart, like the two tanks of a molten-salt plant. Each liner sees one temperature and one pressure for life. A single accumulator cycles both, which is what makes large hot liners fail.</dd>
</dl>
<dl class="spec">
<dt>Daily cycle, staged both ways</dt><dd>Charging uses six extraction points of the existing turbine as a cascade, so each kilojoule is bought with the cheapest steam that can do the job. Discharge is a four-stage flash. Staging is worth twenty points of round trip against one stage each way (54 % versus {d['RT']*100:.0f} %).</dd>
<dt>Evaluated sizing</dt><dd>Steam-table thermodynamics, rock conduction, uplift and heave checks and an economic scan, none of which exist for the cavern variant in the public record.</dd>
</dl>
</div>

<h2><span class="num">03</span>Design</h2>
<div class="grid2">
<dl class="spec">
<dt>Host plant and duty</dt><dd>3,400 MWth, 1,156 MWe PWR with 6.9 MPa saturated steam, moisture separator at 1.1 MPa, live-steam reheat to 250 °C; 838 kJ of net work per kg of throttle steam in the model. Charge 09:00 to 15:00 with 30 % of thermal power; discharge 17:00 to 22:00.</dd>
<dt>Caverns</dt><dd>Two vertical cylinders, 30 m diameter, crowns at 150 m, 60 m apart, in competent crystalline rock with a drainage gallery. Hot: {p['V_hot_m3']/1e3:.0f},000 m³ at {d['T_h']:.0f} °C and {d['P_h']:.2f} MPa. Warm: {p['V_warm_m3']/1e3:.0f},000 m³ at {d['T_w']:.0f} °C and {d['P_w']:.2f} MPa. Steam cushion at each cavern's own saturation pressure, no gas blanket. Rigid-cone uplift safety factor {r['uplift_sf_hot']:.0f} for the hot cavern.</dd>
<dt>Wall, inside to rock</dt><dd>15 mm carbon-steel liner, bitumen sliding layer, 1.5 m calcium-aluminate refractory concrete, 1 m insulating castable (k = 0.15 W/m·K, strength above 10 MPa), drained bedrock.</dd>
</dl>
<dl class="spec">
<dt>Charge train</dt><dd>Warm water pumped through six closed feed heaters in series into the hot cavern. Make-up for the water flashed off during discharge ({d['m_flashed']*100:.1f} % of the hot mass) is heated from 33 to 160 °C at charge time by the same method, so no steam is spent at the peak. Cost: {d['W_in_kJ_per_kg']:.0f} kJ of electricity per kg of hot water made.</dd>
<dt>Discharge</dt><dd>Four flash vessels; the steam from each enters the peaking turbine at its own pressure; residual water at 160 °C returns to the warm cavern. Yield: {d['W_out_kJ_per_kg']:.0f} kJ of electricity per kg of hot water in a wet-steam turbine with 85 % stage efficiency, a separator at 1 MPa and a 5 kPa condenser.</dd>
<dt>Peaking turbine</dt><dd>{p['P_peak_MW']:.0f} MW saturated-steam machine with four admission pressures, its own condenser and generator on the plant switchyard. A new plant would oversize its main turbine instead at about 250 USD per kW of added capacity.</dd>
</dl>
</div>
<div class="tablewrap"><table>
<tr><th>Charge stage outlet, °C</th>{cs}</tr>
<tr><th>Extraction pressure, MPa</th>{cp}</tr>
<tr><th>Steam per kg of store water, kg</th>{cm}</tr>
</table></div>
<div class="tablewrap"><table>
<tr><th>Flash stage, °C</th>{fs}</tr>
<tr><th>Pressure, MPa</th>{fp}</tr>
<tr><th>Steam per kg of hot water, kg</th>{fm}</tr>
</table></div>

<h2><span class="num">04</span>Model</h2>
<ol>
<li><b>Main cycle.</b> HP expansion at 85 % isentropic efficiency to 1.1 MPa, moisture separation, live-steam reheat (its steam consumption charged self-consistently), LP expansion at 88 % to 5 kPa. The work a kilogram of steam taken from the line at any pressure would still have produced is what charging forgoes.</li>
<li><b>Charge and discharge.</b> Closed-heater cascade with a 5 K pinch; multi-stage flash with mass and energy balances; peaking turbine work per admission pressure. IAPWS-97 properties throughout.</li>
<li><b>Rock.</b> Transient conduction from a sphere of equal volume at constant temperature; insulating layer solved against the rock's transient conductance; heat loss, wall temperature, profile, free-expansion heave, rigid-cone uplift.</li>
<li><b>Economics.</b> Excavation 120 USD/m³, 1.5 m concrete at 800 USD/m³, 15 mm liner at 12 USD/kg installed, insulation 400 USD/m², 40 M USD for shafts and drainage, peaking turbine 450 USD/kW, 25 % balance of plant, 30 % contingency, and a stylised price day. Order-of-magnitude figures, not quotes.</li>
</ol>

<h2><span class="num">05</span>Results</h2>
<figure><img src="{f1}" alt="Plant output over one day with the store, and a stylised price curve"><figcaption>One day. The reactor never moves; the grid sees {p['P_charge_drop_MW']:.0f} MW less at midday and {p['P_peak_MW']:.0f} MW more in the evening.</figcaption></figure>
<figure><img src="{f2}" alt="Round trip as a function of cavern temperatures, and as a function of the number of charge and flash stages"><figcaption>Round trip rises as the hot cavern gets cooler and the warm cavern hotter, because less exergy is destroyed heating water with steam and flashing it back; volume moves the other way. The design point is marked. Right: staging both ways is worth twenty points.</figcaption></figure>
<figure><img src="{f3}" alt="Payback versus discharge duration and under different cases"><figcaption>The peaking turbine is the largest cost, so a longer discharge pays back faster; a hotter store shrinks the caverns. The 235 °C point costs a year of payback for a liner that stays below the temperatures at which ordinary concrete degrades.</figcaption></figure>
<figure><img src="{f4}" alt="Rock wall temperature over decades for three insulation options, and rock temperature profile"><figcaption>With 1 m of insulating castable the rock wall reaches 76 °C after a year and 119 °C after 30 years; the warm zone reaches about 60 m into the rock. Heave above the hot cavern after 30 years: {r['heave_cm_30y']:.1f} cm (free-expansion upper bound). Heat loss falls from {r['loss_MW_1y_10y_30y'][0]:.2f} MW in year one to {r['loss_MW_1y_10y_30y'][2]:.2f} MW.</figcaption></figure>
<div class="tablewrap"><table>
<tr><th>Price case (USD per MWh)</th><th class="n">Revenue, M USD per year</th><th class="n">Payback, years</th></tr>
<tr><td>Midday 15, peak 160 (base)</td><td class="n">{ps['mid15_peak160']['revenue_M']:.0f}</td><td class="n">{ps['mid15_peak160']['payback']:.1f}</td></tr>
<tr><td>Midday 15, peak 100</td><td class="n">{ps['mid15_peak100']['revenue_M']:.0f}</td><td class="n">{ps['mid15_peak100']['payback']:.1f}</td></tr>
<tr><td>Midday 15, peak 200</td><td class="n">{ps['mid15_peak200']['revenue_M']:.0f}</td><td class="n">{ps['mid15_peak200']['payback']:.1f}</td></tr>
<tr><td>Midday 30, peak 160</td><td class="n">{ps['mid30_peak160']['revenue_M']:.0f}</td><td class="n">{ps['mid30_peak160']['payback']:.1f}</td></tr>
<tr><td>Midday −20, peak 160</td><td class="n">{ps['mid-20_peak160']['revenue_M']:.0f}</td><td class="n">{ps['mid-20_peak160']['payback']:.1f}</td></tr>
</table></div>

<h2><span class="num">06</span>Failure modes and limits</h2>
<div class="tablewrap"><table>
<tr><th>Item</th><th>Assessment</th></tr>
<tr><td>Liner leak</td><td>Water enters the drained rock zone and the drainage gallery; detected by flow; cavern taken out of service, plant unaffected</td></tr>
<tr><td>Concrete at 235 °C</td><td>Calcium-aluminate refractory concrete is rated far above this; ordinary Portland concrete is not used</td></tr>
<tr><td>Liner thermal fatigue</td><td>None by design: temperature and pressure are constant; only the level changes</td></tr>
<tr><td>Rock thermal stress</td><td>34 MPa free-expansion estimate at a 119 °C wall, within the strength of sound granite; without insulation it would be 71 MPa, which is why the insulating layer exists</td></tr>
<tr><td>Groundwater</td><td>Drained rock zone as in gas-storage practice; site in low-permeability rock</td></tr>
<tr><td>Steam cushion collapse on fast withdrawal</td><td>Withdrawal rate limited by the flash vessels; 10 % cushion volume</td></tr>
<tr><td>Water carry-over</td><td>Four flash vessels with separators; standard wet-steam turbine practice</td></tr>
<tr><td>Radioactivity</td><td>Secondary-side water only; never touches the primary circuit</td></tr>
</table></div>
<div class="callout heat"><b>What it does not do.</b> It does not raise the plant's thermal efficiency, and the quarter of the energy lost per cycle is real. It does nothing for a grid with a flat price. It needs competent rock within about 200 m of the surface.</div>

<h2><span class="num">07</span>Construction and open questions</h2>
<p>Lined rock cavern construction is an established method; Skallen (40,000 m³, 20 MPa) took about three years. Two 70,000 m³ caverns are within the range of civil caverns built for hydro plants. The peaking turbine, flash vessels and heater train are conventional power-plant equipment. The one item to qualify is the liner and concrete system at 235 °C and 3.1 MPa, which can be tested at small scale in a shaft before the caverns are excavated.</p>
<ol>
<li>Liner and refractory-concrete behaviour at 235 °C over decades, including the sliding layer.</li>
<li>Whether the rock temperature ceiling should be lower than 119 °C at a wet site.</li>
<li>Real price series rather than a stylised day; capacity-market revenue is not counted.</li>
<li>Whether part of the store should serve as a reactor-trip ride-through supply for a co-located load, which it can do at reduced power for a day.</li>
<li>Turbine design for four admission pressures versus two admissions with throttling.</li>
</ol>

<h2><span class="num">08</span>Reproducing the results</h2>
<pre>pip install numpy scipy matplotlib iapws
python3 model.py      # cycle validation, round-trip table, design scan, writes runs/design.json
python3 plots.py      # figures</pre>
<footer>Cavern Store design study, 2026-09-28. Model, runs and figures live in <code>designs/cavern/</code> of the nuketime repository. Prior-art statements reflect searches made on that date and are not a legal opinion.</footer>
</div>
"""
open("cavern.html", "w").write(html)
print("wrote cavern.html", len(html) // 1024, "KB")
