"""Generate NUCLEAR_VERTICAL_ML_MAP.md and vertical_map.html from vertical_map_data.py."""
import html as H
from vertical_map_data import STAGES, STEPS, TOP, THESES, FOR_PROSPECTOR

VLABEL = {"10x": "Exponential", "3x": "Strong", "1.3x": "Incremental", "done": "Already commercial"}
VSHORT = {"10x": "10x", "3x": "3x", "1.3x": "1.3x", "done": "done"}
by_id = {s["id"]: s for s in STEPS}
counts = {k: sum(1 for s in STEPS if s["verdict"] == k) for k in VLABEL}

# ------------------------------------------------------------------ markdown
md = ["# The nuclear vertical, step by step: where models and software change the outcome",
      "",
      "Fifty-nine steps from regional targeting to decommissioning and safeguards, each with what happens today, the real",
      "bottleneck, what data exist, who is already applying software or machine learning, the gap that remains, the size",
      "of the prize, and a verdict. Built from six parallel research streams (about 300 sources, listed in",
      "`vertical_map_sources.md`) on 2026-09-29, then synthesised. Verdicts: **Exponential** means a model could change",
      "the outcome by ten times or more (cost, time, recovery, risk); **Strong** three times; **Incremental** under two;",
      "**Already commercial** means products exist and the remaining value is as a feed into other steps.",
      "",
      f"Count: {counts['10x']} exponential, {counts['3x']} strong, {counts['1.3x']} incremental, {counts['done']} already commercial.",
      "", "## Six theses that fall out of the map", ""]
for t, body in THESES:
    md += [f"**{t}.** {body}", ""]
md += ["## The twenty opportunities, ranked", "",
       "Ranked by the product of prize, data availability and the absence of anyone already doing it, tempered by difficulty.", ""]
for rank, ids, title, why, buyer in TOP:
    md += [f"{rank}. **{title}** ({', '.join(ids)}). {why} Buyers: {buyer}.", ""]
md += ["## The map", ""]
for code, sname in STAGES:
    md += [f"### {code}. {sname}", ""]
    for s in [x for x in STEPS if x["stage"] == code]:
        md += [f"#### {s['id']} {s['name']}  —  {VLABEL[s['verdict']]} · data {s['data']} · difficulty {s['difficulty']}", "",
               f"- **Today.** {s['today']}",
               f"- **Bottleneck.** {s['bottleneck']}",
               f"- **Data.** {s['data_note']}",
               f"- **Who is on it.** {s['players']}",
               f"- **Gap.** {s['gap']}",
               f"- **Prize.** {s['prize']}",
               f"- **Verdict.** {s['why']}", ""]
md += ["## For a company that already does ML prospecting", ""]
for t, body in FOR_PROSPECTOR:
    md += [f"**{t}.** {body}", ""]
md += ["## Method and limits", "",
       "Six research agents each covered one stage group with web searches (September 2026), returning per-step findings with sources;",
       "the synthesis, verdicts, ranking and theses are the author's. Prize figures are order-of-magnitude and come from the cited",
       "public numbers (NEI cost data, DOE liabilities, project overruns, market sizes). Anything inside enrichment plants, fuel",
       "fabrication lines and plant historians is inferred from the outside, because those data are closed. The map is a starting",
       "point for diligence, not a substitute for it.", ""]
open("NUCLEAR_VERTICAL_ML_MAP.md", "w").write("\n".join(md))

# ------------------------------------------------------------------ html
def e(x): return H.escape(str(x))
badge = {"10x": "b10", "3x": "b3", "1.3x": "b1", "done": "bd"}
dbadge = {"open": "d-open", "mixed": "d-mixed", "closed": "d-closed"}
rows = []
for code, sname in STAGES:
    rows.append(f'<tr class="stagehead"><th colspan="7">{code}. {e(sname)}</th></tr>')
    for s in [x for x in STEPS if x["stage"] == code]:
        rows.append(
            f'<tr class="step" data-v="{s["verdict"]}" id="{s["id"]}">'
            f'<td class="id"><b>{s["id"]}</b><br><span class="nm">{e(s["name"])}</span></td>'
            f'<td>{e(s["today"])}</td>'
            f'<td>{e(s["bottleneck"])}<div class="sub">Data: <span class="db {dbadge[s["data"]]}">{s["data"]}</span> {e(s["data_note"])}</div></td>'
            f'<td>{e(s["players"])}</td>'
            f'<td>{e(s["gap"])}</td>'
            f'<td>{e(s["prize"])}</td>'
            f'<td class="vcell"><span class="badge {badge[s["verdict"]]}">{VLABEL[s["verdict"]]}</span><div class="sub">difficulty {s["difficulty"]}</div><div class="sub why">{e(s["why"])}</div></td>'
            f'</tr>')
table = "\n".join(rows)
def links(ids):
    return ", ".join('<a href="#%s">%s</a>' % (i, i) for i in ids)
top_cards = "".join(
    '<div class="card"><div class="rank">%d</div><div><h3>%s</h3><p>%s</p><p class="meta">Steps %s · Buyers: %s</p></div></div>' % (rank, e(title), e(why), links(ids), e(buyer))
    for rank, ids, title, why, buyer in TOP)
theses = "".join(f'<div class="thesis"><h3>{e(t)}</h3><p>{e(b)}</p></div>' for t, b in THESES)
prosp = "".join(f'<li><b>{e(t)}</b> {e(b)}</li>' for t, b in FOR_PROSPECTOR)

page = f"""<title>Nuclear Vertical Atlas</title>
<meta name="description" content="Every step of the nuclear vertical, from targeting to decommissioning, with where models and software change the outcome">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Condensed:wght@500;600;700&family=IBM+Plex+Sans:ital,wght@0,400;0,500;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root {{ --paper:#f3f4f1; --paper-2:#e9ebe6; --ink:#12161a; --ink-2:#4b545c; --ink-3:#7c858d; --rule:#cfd4cd; --accent:#1c5cab; --accent-soft:#dbe7f7; --heat:#c9501f; --heat-soft:#f8dccd; --ok:#1e7a3c; --ok-soft:#dcefe0; --warn:#a8600c; --warn-soft:#f6e7cf;
  --mono:"IBM Plex Mono", ui-monospace, Menlo, monospace; --sans:"IBM Plex Sans", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; --disp:"IBM Plex Sans Condensed", "Arial Narrow", system-ui, sans-serif; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ color-scheme:dark; --paper:#15181b; --paper-2:#1d2124; --ink:#eef0ee; --ink-2:#b4bbc1; --ink-3:#8b939b; --rule:#343a3f; --accent:#5598e7; --accent-soft:#1d2f47; --heat:#f08a5e; --heat-soft:#3d2216; --ok:#5dc27c; --ok-soft:#1c3a26; --warn:#e0a24a; --warn-soft:#3d2e14; }} }}
:root[data-theme="dark"] {{ color-scheme:dark; --paper:#15181b; --paper-2:#1d2124; --ink:#eef0ee; --ink-2:#b4bbc1; --ink-3:#8b939b; --rule:#343a3f; --accent:#5598e7; --accent-soft:#1d2f47; --heat:#f08a5e; --heat-soft:#3d2216; --ok:#5dc27c; --ok-soft:#1c3a26; --warn:#e0a24a; --warn-soft:#3d2e14; }}
body {{ background:var(--paper); color:var(--ink); font-family:var(--sans); font-size:15.5px; line-height:1.5; padding-inline:clamp(16px, 3vw, 32px); padding-block:24px 64px; }}
.wrap {{ max-width:1400px; margin:0 auto; }}
header.tb {{ border:1.5px solid var(--ink); display:grid; grid-template-columns:2fr 1fr; }} header.tb > div {{ padding:14px 18px; }} header.tb .name {{ border-right:1.5px solid var(--ink); }}
h1 {{ font-family:var(--disp); font-weight:700; font-size:clamp(28px, 5vw, 44px); line-height:1.02; margin:0 0 8px; }} .sub {{ color:var(--ink-2); font-size:13px; }}
header .lead {{ color:var(--ink-2); font-size:17px; max-width:70ch; margin:0; }}
.meta {{ font-family:var(--mono); font-size:12px; color:var(--ink-2); display:grid; grid-template-columns:auto 1fr; gap:4px 12px; align-content:start; }} .meta b {{ color:var(--ink); font-weight:500; }}
@media (max-width:640px) {{ header.tb {{ grid-template-columns:1fr; }} header.tb .name {{ border-right:0; border-bottom:1.5px solid var(--ink); }} }}
h2 {{ font-family:var(--disp); font-weight:600; font-size:26px; margin:44px 0 12px; padding-top:14px; border-top:1.5px solid var(--ink); }} h2 .num {{ font-family:var(--mono); font-weight:400; font-size:14px; color:var(--ink-3); margin-right:10px; }}
h3 {{ font-family:var(--disp); font-weight:600; font-size:18px; margin:0 0 4px; }}
p {{ max-width:75ch; margin:0 0 12px; }}
.theses {{ display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:18px 28px; }} .thesis p {{ font-size:14.5px; color:var(--ink-2); }}
.cards {{ display:grid; grid-template-columns:repeat(auto-fit, minmax(340px, 1fr)); gap:14px; }}
.card {{ display:grid; grid-template-columns:44px 1fr; gap:10px; border:1px solid var(--rule); padding:12px 14px; background:var(--paper-2); }}
.card .rank {{ font-family:var(--mono); font-size:26px; color:var(--accent); line-height:1; }} .card p {{ font-size:14px; color:var(--ink-2); margin:0 0 6px; }} .card p.meta {{ display:block; font-size:12.5px; }}
.filters {{ display:flex; flex-wrap:wrap; gap:8px; margin:10px 0 14px; }}
.filters button {{ font:inherit; font-size:13.5px; padding:6px 12px; border:1px solid var(--rule); background:var(--paper-2); color:var(--ink); cursor:pointer; border-radius:3px; }}
.filters button[aria-pressed="true"] {{ background:var(--accent); color:#fff; border-color:var(--accent); }} .filters button:focus-visible {{ outline:2px solid var(--accent); outline-offset:2px; }}
.tablewrap {{ overflow-x:auto; border:1px solid var(--rule); }}
table {{ border-collapse:collapse; width:100%; min-width:1240px; font-size:13px; }}
th, td {{ text-align:left; padding:8px 9px; border-bottom:1px solid var(--rule); vertical-align:top; }}
thead th {{ font-family:var(--disp); font-weight:600; font-size:13px; letter-spacing:0.02em; color:var(--ink-2); border-bottom:1.5px solid var(--ink); position:sticky; top:0; background:var(--paper); }}
tr.stagehead th {{ font-family:var(--disp); font-weight:700; font-size:15px; color:var(--ink); background:var(--paper-2); padding:10px 9px; }}
td.id {{ min-width:150px; }} td.id .nm {{ font-family:var(--disp); font-weight:600; font-size:13.5px; }}
td.vcell {{ min-width:170px; }}
.badge {{ display:inline-block; font-family:var(--disp); font-weight:600; font-size:12px; padding:2px 8px; border-radius:3px; }}
.b10 {{ background:var(--heat-soft); color:var(--heat); }} .b3 {{ background:var(--accent-soft); color:var(--accent); }} .b1 {{ background:var(--paper-2); color:var(--ink-2); border:1px solid var(--rule); }} .bd {{ background:var(--ok-soft); color:var(--ok); }}
.db {{ font-family:var(--mono); font-size:11.5px; padding:1px 6px; border-radius:3px; }} .d-open {{ background:var(--ok-soft); color:var(--ok); }} .d-mixed {{ background:var(--warn-soft); color:var(--warn); }} .d-closed {{ background:var(--heat-soft); color:var(--heat); }}
.why {{ font-style:italic; }}
tr.step[hidden] {{ display:none; }}
ol.pro li {{ margin-bottom:10px; max-width:80ch; }}
footer {{ margin-top:56px; padding-top:14px; border-top:1px solid var(--rule); color:var(--ink-3); font-size:13px; }} a {{ color:var(--accent); }}
</style>
<div class="wrap">
<header class="tb">
  <div class="name"><h1>Nuclear Vertical Atlas</h1><p class="lead">Every step from regional targeting to decommissioning and safeguards, with what happens today, where it actually binds, what data exist, who is already on it, and where a model changes the outcome by ten times.</p></div>
  <div class="meta"><span>Steps</span><b>{len(STEPS)} across 6 stages</b><span>Verdicts</span><b>{counts['10x']} exponential · {counts['3x']} strong · {counts['1.3x']} incremental · {counts['done']} commercial</b><span>Sources</span><b>about 300, dated 2026-09-29</b><span>Repo</span><b>research/NUCLEAR_VERTICAL_ML_MAP.md</b></div>
</header>

<h2><span class="num">01</span>Six theses that fall out of the map</h2>
<div class="theses">{theses}</div>

<h2><span class="num">02</span>The twenty opportunities, ranked</h2>
<p>Ranked by prize times data availability times the absence of anyone already doing it, tempered by difficulty. Each card links to its rows in the map.</p>
<div class="cards">{top_cards}</div>

<h2><span class="num">03</span>The map</h2>
<p>Filter by verdict. Rows keep their stage headings so the sequence of the vertical stays visible.</p>
<div class="filters" role="group" aria-label="Filter by verdict">
  <button type="button" data-f="all" aria-pressed="true" id="f-all">All {len(STEPS)}</button>
  <button type="button" data-f="10x" aria-pressed="false" id="f-10x">Exponential {counts['10x']}</button>
  <button type="button" data-f="3x" aria-pressed="false" id="f-3x">Strong {counts['3x']}</button>
  <button type="button" data-f="1.3x" aria-pressed="false" id="f-1x">Incremental {counts['1.3x']}</button>
  <button type="button" data-f="done" aria-pressed="false" id="f-done">Already commercial {counts['done']}</button>
</div>
<div class="tablewrap"><table>
<thead><tr><th>Step</th><th>What happens today</th><th>Bottleneck and data</th><th>Who is already on it</th><th>The gap</th><th>Prize</th><th>Verdict</th></tr></thead>
<tbody>{table}</tbody></table></div>

<h2><span class="num">04</span>For a company that already does ML prospecting</h2>
<ol class="pro">{prosp}</ol>

<h2><span class="num">05</span>Method and limits</h2>
<p>Six research agents each covered one stage group with web searches on 2026-09-29 and returned per-step findings with sources; the synthesis, verdicts, ranking and theses are the author's. Prize figures are order-of-magnitude and come from cited public numbers (NEI cost data, DOE liabilities, project overruns, market sizes). Anything inside enrichment plants, fuel fabrication lines and plant historians is inferred from outside, because those data are closed. The full source list is in the repository next to the map.</p>
<footer>Nuclear Vertical Atlas, 2026-09-29. Data and generator: <code>research/vertical_map_data.py</code>, <code>research/build_map.py</code>.</footer>
</div>
<script>
(function(){{
  var btns = document.querySelectorAll('.filters button');
  var rows = document.querySelectorAll('tr.step');
  function apply(f){{
    rows.forEach(function(r){{ r.hidden = !(f === 'all' || r.dataset.v === f); }});
    btns.forEach(function(b){{ b.setAttribute('aria-pressed', b.dataset.f === f ? 'true' : 'false'); }});
    try {{ localStorage.setItem('nva-filter', f); }} catch(e) {{}}
  }}
  btns.forEach(function(b){{ b.addEventListener('click', function(){{ apply(b.dataset.f); }}); }});
  var saved = null; try {{ saved = localStorage.getItem('nva-filter'); }} catch(e) {{}}
  if (saved) apply(saved);
}})();
</script>
"""
open("vertical_map.html", "w").write(page)
print("wrote NUCLEAR_VERTICAL_ML_MAP.md (%d KB) and vertical_map.html (%d KB); verdicts %s" % (len("\n".join(md))//1024, len(page)//1024, counts))
