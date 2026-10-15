"""Assemble the ROCKSINK design report as a single HTML page with embedded figures."""
import base64, json, os
def b64(path):
    return "data:image/png;base64," + base64.b64encode(open(path, "rb").read()).decode()
svg = open("figures/schematic.svg").read()
svg = svg[svg.index("<svg"):]
fig1, fig3 = b64("figures/fig1_timeseries.png"), b64("figures/fig3_sensitivity.png")
fig2 = b64("figures/fig2_rockfield.png") if os.path.exists("figures/fig2_rockfield.png") else ""
F = json.load(open("runs/final.json"))
sens = {k: json.load(open(f"runs/F_{k}.json")) for k in ["k3", "k2", "k15", "N96", "N160", "grout1", "smalljacket", "T0_20", "L45"]}
names = {"k3": "Granite, k = 3.0 W/m·K (base)", "k2": "Limestone or sandstone, k = 2.0", "k15": "Shale, k = 1.5", "N96": "96 units instead of 128",
         "N160": "160 units", "grout1": "Poor grout, k = 1.0", "smalljacket": "Half-size jacket, 60 t water", "T0_20": "Warm rock, 20 °C", "L45": "45 m condensers"}
sens_rows = "".join(
    f"<tr><td>{names[k]}</td><td class=n>{s['Tj_peak']:.0f}</td><td class=n>{s['Tw_peak']:.0f}</td>"
    f"<td class=n>{s['flood_ratio_max']:.2f}{' <span class=flag>over cap</span>' if s['flood_ratio_max'] > 0.505 else ''}</td>"
    f"<td class=n>{s['day30']['Tj']:.0f}</td><td class=n>{s['day365']['Tj']:.0f}</td></tr>" for k, s in sens.items())
d = F
res_rows = [("2.3 h (peak)", "9.5", "7.8", f"{d['Tj_peak']:.1f}", "78", "62", "100"),
            ("12 h", "1.79", "2.00", "65", "62", "57", "68"), ("1 d", "1.46", "1.50", "60", "58", "53", "56"),
            ("7 d", "0.84", "0.84", "56", "55", "52", "48"), ("30 d", "0.51", "0.51", "53", "52", "51", "38"),
            ("1 y", "0.14", "0.14", "56", "56", "56", "49"), ("3 y", "0.06", "0.06", "52", "52", "52", "37")]
res_html = "".join("<tr>" + "".join(f"<td class='{'n' if i else ''}'>{c}</td>" for i, c in enumerate(r)) + "</tr>" for r in res_rows)

html = f"""<title>Rocksink</title>
<meta name="description" content="Bedrock as the passive ultimate heat sink for a shaft-sited SMR">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Condensed:wght@500;600;700&family=IBM+Plex+Sans:ital,wght@0,400;0,500;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root {{
  --paper:#f3f4f1; --paper-2:#e9ebe6; --ink:#12161a; --ink-2:#4b545c; --ink-3:#7c858d; --rule:#cfd4cd;
  --accent:#1c5cab; --accent-soft:#dbe7f7; --heat:#c9501f; --heat-soft:#f8dccd; --ok:#1e7a3c; --warn:#a8600c;
  --mono:"IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  --sans:"IBM Plex Sans", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --disp:"IBM Plex Sans Condensed", "Arial Narrow", system-ui, sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ color-scheme:dark;
  --paper:#15181b; --paper-2:#1d2124; --ink:#eef0ee; --ink-2:#b4bbc1; --ink-3:#8b939b; --rule:#343a3f;
  --accent:#5598e7; --accent-soft:#1d2f47; --heat:#f08a5e; --heat-soft:#3d2216; --ok:#5dc27c; --warn:#e0a24a; }} }}
:root[data-theme="dark"] {{ color-scheme:dark;
  --paper:#15181b; --paper-2:#1d2124; --ink:#eef0ee; --ink-2:#b4bbc1; --ink-3:#8b939b; --rule:#343a3f;
  --accent:#5598e7; --accent-soft:#1d2f47; --heat:#f08a5e; --heat-soft:#3d2216; --ok:#5dc27c; --warn:#e0a24a; }}
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
.kpi .l {{ font-size:12.5px; color:var(--ink-2); margin-top:4px; letter-spacing:0.01em; }}
h2 {{ font-family:var(--disp); font-weight:600; font-size:26px; margin:44px 0 12px; padding-top:14px; border-top:1.5px solid var(--ink); text-wrap:balance; }}
h2 .num {{ font-family:var(--mono); font-weight:400; font-size:14px; color:var(--ink-3); margin-right:10px; vertical-align:middle; }}
h3 {{ font-family:var(--disp); font-weight:600; font-size:19px; margin:26px 0 6px; }}
p, li {{ max-width:70ch; }}
p {{ margin:0 0 12px; }}
ul, ol {{ padding-left:22px; margin:0 0 12px; }}
li {{ margin-bottom:5px; }}
.lead {{ font-size:18px; color:var(--ink); max-width:66ch; }}
.callout {{ border-left:3px solid var(--accent); background:var(--accent-soft); padding:12px 16px; margin:16px 0 20px; max-width:80ch; }}
.callout.heat {{ border-color:var(--heat); background:var(--heat-soft); }}
figure {{ margin:22px 0 28px; }}
figure img, figure svg {{ width:100%; height:auto; display:block; border:1px solid var(--rule); background:#fcfcfb; }}
figcaption {{ font-size:13.5px; color:var(--ink-2); margin-top:8px; max-width:90ch; }}
.tablewrap {{ overflow-x:auto; margin:14px 0 22px; }}
table {{ border-collapse:collapse; width:100%; font-size:14.5px; }}
th, td {{ text-align:left; padding:8px 10px; border-bottom:1px solid var(--rule); vertical-align:top; }}
th {{ font-family:var(--disp); font-weight:600; font-size:14px; letter-spacing:0.02em; color:var(--ink-2); border-bottom:1.5px solid var(--ink); }}
td.n, th.n {{ text-align:right; font-family:var(--mono); font-variant-numeric:tabular-nums; white-space:nowrap; }}
.flag {{ font-family:var(--sans); font-size:11.5px; color:var(--warn); border:1px solid var(--warn); border-radius:3px; padding:0 5px; margin-left:4px; white-space:nowrap; }}
code, pre {{ font-family:var(--mono); font-size:13.5px; }}
pre {{ background:var(--paper-2); padding:12px 14px; overflow-x:auto; border:1px solid var(--rule); }}
.path {{ font-family:var(--mono); font-size:13.5px; color:var(--ink-2); line-height:1.7; max-width:90ch; }}
.path span {{ color:var(--accent); }}
.grid2 {{ display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:18px 32px; }}
.spec dt {{ font-family:var(--disp); font-weight:600; margin-top:10px; }}
.spec dd {{ margin:2px 0 0; color:var(--ink-2); font-size:15px; }}
footer {{ margin-top:56px; padding-top:14px; border-top:1px solid var(--rule); color:var(--ink-3); font-size:13px; }}
a {{ color:var(--accent); }}
</style>
<div class="wrap">
<header class="titleblock">
  <div class="name">
    <h1>Rocksink</h1>
    <p class="sub">Bedrock as the passive ultimate heat sink for a shaft-sited small modular reactor. A complete soft design, sized and evaluated with a first-principles model.</p>
  </div>
  <div class="meta">
    <span>Drawing</span><b>RS-001 rev A</b>
    <span>Date</span><b>2026-09-28</b>
    <span>Module</span><b>250 MWth integral PWR</b>
    <span>Sink</span><b>7,296 m condenser in bedrock</b>
    <span>Units</span><b>128 gas-loaded thermosyphons</b>
    <span>Status</span><b>Concept, evaluated</b>
    <span>Model</span><b>designs/rocksink/model.py</b>
  </div>
</header>

<div class="kpis">
  <div class="kpi"><div class="v">{d['Tj_peak']:.0f}<small>°C</small></div><div class="l">peak containment jacket, limit 150 °C</div></div>
  <div class="kpi"><div class="v">{d['Tw_peak']:.0f}<small>°C</small></div><div class="l">hottest borehole wall, limit 90 °C</div></div>
  <div class="kpi"><div class="v">{d['flood_ratio_max']*100:.0f}<small>%</small></div><div class="l">of thermosyphon flooding limit, cap 50 %</div></div>
  <div class="kpi"><div class="v">∞</div><div class="l">grace period: no water, power or action, ever</div></div>
  <div class="kpi"><div class="v">0</div><div class="l">valves, pumps, dampers or surface structures in the safety path</div></div>
</div>

<p class="lead">Every passive decay-heat system today ends in a pool that boils away, an air chimney, or a containment shell radiating to the sky. Pools give three to thirty days and need make-up water. Chimneys and shells are large surface structures exposed to aircraft, tornado missiles and attack. Bedrock has effectively unlimited heat capacity, sits under every plant, and is protected by geometry. The obstacle has always been transport: rock conducts poorly, and heat cannot be moved downward passively. Rocksink solves both at once.</p>
<p>The module sits at the bottom of a 100 m shaft, so the rock beside the shaft is <em>above</em> the reactor and gravity thermosyphons can carry heat into it. A bundle of 128 sealed thermosyphons fans out from a ring drift around the shaft into 7.3 km of grouted boreholes, which turns the low conductivity of rock into a non-problem by spreading the heat over a large surface. A closed water jacket around the steel containment collects the module's decay heat and delivers it to the thermosyphon evaporators as steam. A nitrogen charge in each thermosyphon makes it a thermal switch that is off in normal operation and opens by itself when the jacket warms.</p>

<figure>{svg}<figcaption>Vertical section through the shaft, drawn to scale (5.5 px per metre). Blue: thermosyphon condensers in fanned upholes; grey: insulated risers; orange: jacket steam drum, steam lines and the torus in the ring drift; arrows: heat into rock.</figcaption></figure>

<h2><span class="num">01</span>What is new</h2>
<p>Searched on 2026-09-28 across patent full text, journals and vendor filings. Nobody has built any ground-sink decay-heat system. Two paper designs come close and both differ in physics and scale.</p>
<div class="tablewrap"><table>
<tr><th>Prior art</th><th>What it is</th><th>How Rocksink differs</th></tr>
<tr><td>GE-Hitachi patent US 11,482,345 (2022), geothermal passive cooling</td><td>For an underground PRISM sodium reactor: one single-phase natural-circulation loop buried 1 to 20 ft in soil, with fins and a damper, for up to 20 MW of decay heat.</td><td>Light-water module; 128 independent sealed two-phase thermosyphons instead of one loop; deep grouted upholes in bedrock instead of a shallow soil conduit; a gas charge instead of a damper.</td></tr>
<tr><td>Deep Fission Gravity Reactor (NRC ML24172A286, ML26112A159; patent US 12,469,612)</td><td>A 15 MWe PWR at the bottom of a one-mile borehole. Decay heat conducts from the borehole water through the casing into the rock next to the reactor; a heat exchanger in a second borehole receives heat through the rock.</td><td>Using the rock next to the reactor limits Deep Fission to a small core in a very deep hole. Rocksink spreads the heat over thousands of metres of borehole away from the module, so a 250 MWth module in a 100 m shaft works.</td></tr>
<tr><td>Two-phase thermosyphon PRHR concepts (Applied Thermal Engineering 2024; KAERI mercury thermosyphon for sodium reactors)</td><td>Thermosyphons carrying decay heat to a pool or to air.</td><td>Same component, different sink.</td></tr>
<tr><td>Thermal-energy-storage decay-heat sinks (patented LiCl phase-change block store)</td><td>A manufactured store absorbs decay heat.</td><td>The site itself is the store, at zero material cost, with no temperature limit set by a phase-change material.</td></tr>
<tr><td>Permafrost thermosyphons (124,000 units on the Trans-Alaska Pipeline since 1977)</td><td>Sealed gravity thermosyphons moving heat out of the ground into winter air.</td><td>Same device class and the source of the reliability record; run in the opposite direction.</td></tr>
<tr><td>Borehole thermal energy storage (Drake Landing and others)</td><td>Seasonal storage of solar heat in a pumped borehole field.</td><td>Same conduction physics and design method; Rocksink is pumpless, two-phase and transient.</td></tr>
</table></div>
<p>The claim is novelty of the assembly and of the evaluated sizing: a shaft-sited LWR module, a closed containment jacket acting as a steam generator, a torus manifold in a ring drift, sealed gas-loaded thermosyphons, and fanned upholes in bedrock as the ultimate heat sink. No component is new.</p>

<h2><span class="num">02</span>The design</h2>
<div class="grid2">
<dl class="spec">
<dt>Module and shaft</dt><dd>250 MWth integral PWR in a 4.6 m OD × 23 m steel containment (a NuScale-class envelope). Internals, emergency core cooling valves and decay-heat steam-generator loops unchanged. Shaft 10 m ID, 100 m deep, raise-bored, concrete lined. Containment from 75 to 98 m depth.</dd>
<dt>Ring drift</dt><dd>3 × 3 m tunnel at 73 to 76 m depth on a 15 m radius (94 m long), 7 m rock pillar to the shaft. Holds the torus and the 128 collars.</dd>
<dt>Containment jacket</dt><dd>Closed steel vessel forming a 0.3 m water annulus with a steam-drum ring. 120 t water, about 400 t coupled steel. Rated 0.5 MPa absolute (150 °C), which keeps the external pressure on the containment within a factor of four of its buckling pressure. A small chiller holds it at 25 °C in normal operation.</dd>
<dt>Steam torus and evaporators</dt><dd>0.8 m torus in the drift, fed by two DN400 lines that also return condensate by slope. 128 evaporators of 4 m pass through it; jacket steam condenses on them (8 kW/m²K) while the water inside boils (5 kW/m²K). Evaporator resistance 1.8 × 10⁻⁴ K/W per unit.</dd>
</dl>
<dl class="spec">
<dt>Thermosyphons</dt><dd>Sealed, water in 316L or duplex stainless, 125 mm ID, 141 mm OD. From the torus: 8 m insulated riser, 57 m condenser grouted in a 165 mm uphole, 3 m gas reservoir ending 8 m below grade.</dd>
<dt>Uphole fan</dt><dd>Drilled upward from the drift crown, alternating 0°, 10°, 20° and 30° outward tilt. Collar spacing 0.74 m; the fan opens it to 3 m between vertical neighbours and 30 m at the toe. Totals 7,296 m of condenser, 8,704 m drilled. Borehole resistance 0.014 m·K/W with thermally enhanced grout.</dd>
<dt>Gas loading</dt><dd>A measured nitrogen charge fills the whole condenser at or below 45 °C vapour and fits in the reservoir at 95 °C (flat-front model, pressure ratio 8.8). Between them the open length is continuous, so the array throttles itself. Gas-loaded variable-conductance heat pipes are a mature spacecraft component; the reservoir sits in cold rock, the standard configuration.</dd>
<dt>Independence</dt><dd>Each unit is a factory-sealed, individually tested part. One leak loses 0.8 % of capacity. No valve, damper or instrument is needed for it to work.</dd>
</dl>
</div>
<p class="path" style="margin-top:18px"><span>Heat path:</span> core → reactor vessel → steam in containment → containment wall → boiling jacket → torus → evaporators → vapour up the upholes → condensate film → tube wall → grout → bedrock → (over months) ground surface. Every step is driven by gravity, pressure difference or conduction.</p>

<h2><span class="num">03</span>Physics model</h2>
<p><code>model.py</code>, about 350 lines, no proprietary code, validated against the analytic line source.</p>
<ol>
<li><b>Decay heat.</b> The Glasstone-Sesonske / Todreas-Kazimi fission-product fit 0.066 [t<sup>−0.2</sup> − (t + T)<sup>−0.2</sup>] with T = 3 y, times 1.15 for actinides and fit uncertainty, plus 140 GJ of stored primary-system heat released with a 2 h time constant. Peak load at scram 25.6 MW.</li>
<li><b>Jacket.</b> Lumped capacitance of 0.70 GJ/K, implicit time stepping, coupled to the containment by a 300 kW/K conductance used only to estimate the containment inner-wall temperature.</li>
<li><b>Thermosyphons.</b> Isothermal vapour, evaporator and condenser film resistances, flat-front gas loading. Per-unit load checked against Faghri's counter-current flooding limit and the sonic limit; design cap 50 % of flooding.</li>
<li><b>Rock.</b> Three-dimensional transient conduction. Each of the 768 condenser segments (128 holes × 6) is a finite line source; the ground surface is held at 14 °C by the method of images. Line integrals are taken in the diffusion-scaled coordinate with the 1/distance singularity integrated analytically and the smooth remainder by 40-point Gauss-Legendre, so the response is accurate from 10 s to 3 y. Loads are piecewise constant and superposed in time. At each step the per-segment loads are solved from the isothermal-condenser condition, so heat shifts automatically to cooler rock.</li>
<li><b>Validation.</b> The numeric finite line source reproduces the analytic infinite line source to four significant figures at the borehole wall, 1 m and 5 m, at 1 h, 1 d and 30 d. Rock: granite, k = 3.0 W/m·K, 2.3 MJ/m³K, undisturbed 14 °C.</li>
</ol>

<h2><span class="num">04</span>Results, base case in granite</h2>
<div class="callout heat"><b>Scenario.</b> Scram from full power with simultaneous loss of all AC and DC power, the chiller and every water supply, and no operator action, ever.</div>
<div class="tablewrap"><table>
<tr><th>Time after scram</th><th class="n">Heat into jacket, MW</th><th class="n">Heat into rock, MW</th><th class="n">Jacket, °C</th><th class="n">Vapour, °C</th><th class="n">Hottest wall, °C</th><th class="n">Condenser open, %</th></tr>
{res_html}
</table></div>
<ul>
<li>Peak jacket pressure 0.08 MPa gauge at {d['Tj_peak']:.1f} °C, against a 0.5 MPa absolute rating.</li>
<li>Peak borehole-wall temperature {d['Tw_peak']:.0f} °C at 3.7 h, against a 90 °C limit chosen to keep groundwater in the grout and fractures below boiling.</li>
<li>Most-loaded thermosyphon {d['Q_unit_max_kW']:.0f} kW, {d['flood_ratio_max']*100:.0f} % of its flooding limit at that moment and 13 % of its sonic limit.</li>
<li>Energy into rock: 288 GJ in day 1, 834 GJ in week 1, 2.1 TJ in month 1, 9.2 TJ in year 1. The jacket's own sensible heat (49 GJ from 25 to 95 °C) buffers the first two hours while the load falls from 25 MW to 4 MW.</li>
<li>From day 3 on, heat into rock equals heat generated. The gas front throttles the array to hold the jacket in the 50 to 60 °C band, and the field never approaches saturation: the year-1 load of 0.14 MW is 2 % of what the array moved on day 1.</li>
</ul>
<figure><img src="{fig1}" alt="Three panels: heat flows, temperatures, and thermosyphon capacity margin versus time after scram on a log axis from minutes to three years"><figcaption>Loads, temperatures and capacity margin from scram to three years. The rock line in the top panel starts when the gas front opens at 45 °C; from about day 3 it tracks the decay curve exactly.</figcaption></figure>
{'<figure><img src="' + fig2 + '" alt="Rock temperature maps on a vertical section and a horizontal plan at days 1, 7, 30 and 365"><figcaption>Rock temperature on a vertical section through the shaft axis (top) and a plan at 36 m depth (bottom). Dashed: the shaft; solid: the containment jacket. After day 1 the gas front closes the upper condensers and the load concentrates on the lower 40 m; by a year the ring volume is a uniform 50 to 58 °C and the warm zone reaches about 40 m from the axis. The field uses a coarsened load history, accurate to about 3 K.</figcaption></figure>' if fig2 else ''}

<h2><span class="num">05</span>Sensitivity</h2>
<div class="tablewrap"><table>
<tr><th>Case</th><th class="n">Peak jacket °C (limit 150)</th><th class="n">Peak wall °C (limit 90)</th><th class="n">Load / flooding (cap 0.50)</th><th class="n">Jacket at 30 d</th><th class="n">Jacket at 1 y</th></tr>
{sens_rows}
</table></div>
<figure><img src="{fig3}" alt="Dot plot of peak jacket temperature, peak wall temperature and flooding ratio for nine design and site variants"><figcaption>Each row is a full re-run. Temperature limits hold in every case; the two red marks exceed the self-imposed flooding cap, not a physical limit.</figcaption></figure>
<p>The design passes in shale, close to the worst rock a plant would be sited in, with the wall at its limit; there one would add a fifth tilt family or lengthen the condensers. Dropping to 96 units, or halving the jacket water (which lets the jacket heat faster in the first hours and pushes 117 kW through each unit), erodes the margin against the one correlation in the model that is least certain for this geometry: the flooding correlation is for straight vertical tubes and these units have an L-bend. The count of 128 and the 120 t jacket were chosen so that the flooding margin, not the rock, is the binding constraint in granite.</p>

<h2><span class="num">06</span>Failure modes</h2>
<div class="tablewrap"><table>
<tr><th>Failure</th><th>Consequence</th><th>Why it is tolerable</th></tr>
<tr><td>Loss of all power and water</td><td>None: the design case</td><td>Fully passive</td></tr>
<tr><td>One thermosyphon leaks to rock</td><td>Loses 0.8 % of capacity</td><td>128 independent units; the grouted hole contains the water</td></tr>
<tr><td>Several units in one sector fail</td><td>Load shifts to neighbours through the torus</td><td>Isothermal torus; per-unit margin of two on flooding</td></tr>
<tr><td>A jacket-to-torus steam line breaks</td><td>Steam vents into the sealed drift; the second line still connects</td><td>Two lines; the drift is a sealed rock space at 73 m; jacket inventory stays in the shaft</td></tr>
<tr><td>Jacket vessel leaks into the shaft</td><td>Water collects in the shaft sump around the containment base</td><td>Containment then radiates to the shaft liner and the lower jacket; the shaft holds the full inventory below the containment top</td></tr>
<tr><td>Wrong gas charge</td><td>Unit opens late or not at all</td><td>Each unit is hot-tested at the factory and re-testable in service by heating the torus with the chiller loop reversed</td></tr>
<tr><td>Hydrogen generated over life</td><td>Adds to the deliberate charge, shifts the switch point up</td><td>Stainless steel, degassed fill, 3 m cold reservoir sized for the 60-year inventory; the periodic torus test verifies the switch point</td></tr>
<tr><td>Chiller fails in normal operation</td><td>Jacket warms to about 60 °C, units open partly and hold it there</td><td>Self-limiting; weeks of margin before rock warming matters</td></tr>
<tr><td>Seismic event</td><td>Shaft-sited module; flexible tubes in grouted rock</td><td>Same argument as every below-grade SMR</td></tr>
<tr><td>Aircraft, tornado, flood, attack on the sink</td><td>Nothing to hit</td><td>The point of the design</td></tr>
<tr><td>Groundwater flow</td><td>Advection removes heat faster</td><td>Only helps</td></tr>
</table></div>
<div class="callout"><b>What it does not do.</b> This is a transient sink, not a steady one. Continuous loads such as spent-fuel pool cooling must never be put on it: a steady 2 MW would warm the field by over 100 K within years. The chiller and the gas switch enforce that in normal operation.</div>

<h2><span class="num">07</span>Construction and cost</h2>
<p>Everything uses mining and geothermal methods that are routine at this scale.</p>
<div class="tablewrap"><table>
<tr><th>Item</th><th>Quantity</th><th>Method</th><th class="n">Cost, rough</th></tr>
<tr><td>Ring drift</td><td>94 m, 3 × 3 m</td><td>Roadheader or drill-and-blast</td><td class="n">$1.5 M</td></tr>
<tr><td>Upholes</td><td>8,704 m, 165 mm</td><td>Long-hole in-the-hole rig from the drift</td><td class="n">$1.5 to 2.5 M</td></tr>
<tr><td>Thermosyphons</td><td>128, stainless, gas-loaded, tested</td><td>12 m sections welded in the drift, filled and sealed on site</td><td class="n">$3 to 4 M</td></tr>
<tr><td>Grouting</td><td>8,704 m</td><td>Thermally enhanced grout</td><td class="n">$0.5 M</td></tr>
<tr><td>Torus, steam lines, jacket vessel, drum</td><td>1 set</td><td>Pressure-vessel shop</td><td class="n">$8 to 12 M</td></tr>
<tr><td>Chiller plant</td><td>0.5 MW</td><td>Off the shelf</td><td class="n">$1 M</td></tr>
<tr><td>Extra shaft depth beyond a conventional below-grade module</td><td>40 to 60 m</td><td>Raise boring</td><td class="n">$3 to 6 M</td></tr>
<tr><th>Total incremental</th><th></th><th></th><th class="n">$18 to 28 M per module</th></tr>
</table></div>
<p>Compare with the reactor pool of a NuScale-class plant, a seismic category I reinforced concrete structure holding thousands of tonnes of water with its own cooling, make-up and boil-off management, or with the cooling towers and safety-class ultimate-heat-sink water system of a conventional SMR. The sink here consumes no water, needs no make-up and imposes no river or coast on the site.</p>

<h2><span class="num">08</span>Safety argument</h2>
<ul>
<li>Meets the intent of the 72 h passive coping requirement with an unlimited coping time and no consumable.</li>
<li>The heat sink is below grade and distributed, which removes almost all of the external-hazard analysis for the ultimate heat sink: tornado, aircraft, flood, ice, biofouling, freezing.</li>
<li>No active component and no valve in the safety path. Passive-system reliability reduces to two physical facts, that the jacket boils and that gravity thermosyphons condense in cold rock, and both can be tested at full scale before fuel load by running the chiller loop in reverse and watching the rock respond.</li>
<li>Every temperature stays in the range of ordinary materials: jacket under 100 °C, rock under 70 °C, containment wall under 140 °C in the base case.</li>
<li>Fibre-optic distributed temperature sensing in a few monitoring holes makes this the first inspectable ultimate heat sink.</li>
</ul>

<h2><span class="num">09</span>Open questions and test programme</h2>
<ol>
<li>Flooding and start-up of an L-shaped 68 m water thermosyphon with a 4 m horizontal evaporator: build one full-scale unit in a vertical rig and measure capacity against vapour temperature from 45 to 150 °C.</li>
<li>Gas-front behaviour with a 3 m reservoir in cold rock over years: confirm the switch temperatures and the hydrogen allowance.</li>
<li>Rock characterisation at the site: conductivity, groundwater, fracture state, and whether 90 °C is the right wall criterion.</li>
<li>Whether jacket external pressure should be limited by a relief line into the shaft sump rather than by rating; containment external-pressure qualification.</li>
<li>Drift and torus layout for multi-module plants: 60 m module spacing keeps the fields independent for the first year; closer spacing needs a joint run.</li>
<li>Replace the decay-heat fit with an ANS-5.1-2014 calculation for the real fuel cycle; the 1.15 factor is a placeholder for that.</li>
</ol>

<h2><span class="num">10</span>Reproducing the results</h2>
<pre>pip install numpy scipy matplotlib iapws
python3 model.py        # validation + base case, about 40 s
python3 final.py        # runs/final.json and runs/final_series.npz
python3 sweep.py F_k2 '{{"k_rock":2.0,"rhoc_rock":2.2e6}}'
python3 field.py        # rock temperature field
python3 plots.py        # figures</pre>
<footer>Rocksink design study, 2026-09-28. Model, runs and figures live in <code>designs/rocksink/</code> of the nuketime repository. Prior-art statements reflect searches made on that date and are not a legal opinion.</footer>
</div>
"""
open("rocksink.html", "w").write(html)
print("wrote rocksink.html", len(html) // 1024, "KB", "fig2" if fig2 else "no fig2")
