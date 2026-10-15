"""Generate ANALOG_ATLAS.md and analog_atlas.html from analog_atlas_data.py."""
import html as H
from analog_atlas_data import ENTRIES, PATTERNS, GRADES, HIRE_MAP, FINDINGS
from vertical_map_data import TOP

top_by_rank = {t[0]: t for t in TOP}
pat_by_id = {p[0]: p for p in PATTERNS}
E = sorted(ENTRIES, key=lambda x: x["rank"])
gcount = {g: sum(1 for e in E if e["grade"] == g) for g in GRADES}
n_sources = len({u for e in E for u in e["sources"]})
n_precedent = sum(len(e["precedent"]) for e in E)
n_gain = sum(len(e["how"]) for e in E)
DATE = "2026-09-29"

def quality(s):
    tag = s.split(" [")[-1]
    if "unverified" in tag and "[independent" not in s: return "unverified"
    if "unverified" in tag or "corrected" in tag: return "partly verified"
    return "independent" if "[independent" in s else ("vendor" if "[vendor" in s else ("synthetic" if "[synthetic" in s else "mixed"))

def short_analogue(e):
    return "; ".join(a[0] for a in e["analogues"])

# ------------------------------------------------------------------ markdown
md = ["# The Analogue Atlas: who already solved nuclear's twenty software problems, and how the credit was won", "",
      "For each of the twenty ranked opportunities in the nuclear vertical map, the industry that already solved the",
      "structurally identical problem, the method and the measured gain (with an evidence grade), the regulatory document",
      "that let a model or a process be credited, the nuclear rule that could carry the transfer today, what maps one to one,",
      "what breaks, and who to hire. Built from five parallel research streams on %s and synthesised. Every gain figure is" % DATE,
      "tagged independent (regulator, audit office, peer review), vendor (self-reported) or synthetic (benchmark study); a second-round",
      "fact-check verified, corrected or flagged twenty figures, and the flags are carried in the text.", "",
      "Transfer grades: %s" % " ".join("**%s** (%s)." % (v[0], v[1]) for v in GRADES.values()),
      "Count: %d direct, %d adapt, %d partial." % (gcount["direct"], gcount["adapt"], gcount["partial"]), "",
      "## What the atlas says", ""]
for t, body in FINDINGS:
    md += ["**%s.** %s" % (t, body), ""]
md += ["## Ten patterns behind every successful transfer", ""]
for pid, t, body in PATTERNS:
    ex = ", ".join("%d" % e["rank"] for e in E if pid in e["patterns"])
    md += ["**%s. %s.** %s Opportunities: %s." % (pid, t, body, ex or "none"), ""]
md += ["## Scorecard", "",
       "| # | Nuclear opportunity | Solved twin | Best independent gain | Precedent that mattered | Existing nuclear hook | Grade |",
       "|---|---|---|---|---|---|---|"]
for e in E:
    ind = next((h for h in e["how"] if "[independent" in h), e["how"][0])
    ind = ind.split(". [")[0]
    ind = ind if len(ind) < 220 else ind[:217] + "..."
    md.append("| %d | %s | %s | %s | %s | %s | %s |" % (e["rank"], e["title"], short_analogue(e), ind.replace("|", "/"), e["precedent"][0].replace("|", "/"), e["hook"].split(";")[0].replace("|", "/"), GRADES[e["grade"]][0]))
md += ["", "## The twenty, in full", ""]
for e in E:
    md += ["### %d. %s  —  %s" % (e["rank"], e["title"], GRADES[e["grade"]][0]), "",
           "**The nuclear problem.** %s" % e["problem"], "",
           "**The twin.** %s" % e["twin"], "",
           "**Who solved it.**"]
    md += ["- *%s.* %s" % a for a in e["analogues"]]
    md += ["", "**How, and how much.**"]
    md += ["- %s" % h for h in e["how"]]
    md += ["", "**The precedent.**"]
    md += ["- %s" % p for p in e["precedent"]]
    md += ["", "**Existing nuclear hook.** %s" % e["hook"], "", "**What transfers.**"]
    md += ["- %s" % t for t in e["transfers"]]
    md += ["", "**What does not.**"]
    md += ["- %s" % t for t in e["does_not"]]
    md += ["", "**Barriers.** %s" % e["barriers"], "", "**Who to hire.**"]
    md += ["- %s: %s" % h for h in e["hire"]]
    if e["patterns"]:
        md += ["", "Patterns: %s." % ", ".join(e["patterns"])]
    if e.get("note"):
        md += ["", "*Caveat: %s*" % e["note"]]
    md += ["", "Sources: " + " · ".join(e["sources"]), ""]
md += ["## Hiring map", "", "Where the people who did this already work, grouped by skill, with the opportunities each group unlocks.", ""]
for skill, orgs, ranks in HIRE_MAP:
    md += ["- **%s.** %s. Opportunities %s." % (skill, orgs, ", ".join(map(str, ranks)))]
md += ["", "## Method and limits", "",
       "Five research agents each took four opportunities and searched for the analogue industry, its method, its measured",
       "gains and the regulatory instrument, returning sourced reports on %s; the synthesis, grades, patterns and findings" % DATE,
       "are the author's. Opportunity 20 (laser enrichment control) was researched in a second round through OSTI, arXiv and",
       "publisher APIs after the web-search budget was spent. Vendor figures are marked and should be re-verified before external use. Several agents",
       "exhausted their search budget, so a few numbers are from secondary sources; those are flagged in the entries.", ""]
open("ANALOG_ATLAS.md", "w").write("\n".join(md))

# ------------------------------------------------------------------ html
def e_(x): return H.escape(str(x))
gcls = {"direct": "g-direct", "adapt": "g-adapt", "partial": "g-partial"}
qcls = {"independent": "q-ind", "vendor": "q-ven", "synthetic": "q-syn", "mixed": "q-mix", "unverified": "q-unv", "partly verified": "q-unv"}

def how_li(h):
    q = quality(h)
    txt = h.split(" [")[0]
    return '<li>%s <span class="q %s">%s</span></li>' % (e_(txt), qcls[q], q)

findings_html = "".join('<div class="finding"><h3>%s</h3><p>%s</p></div>' % (e_(t), e_(b)) for t, b in FINDINGS)
patterns_html = "".join(
    '<div class="pattern" id="%s"><div class="pid">%s</div><div><h3>%s</h3><p>%s</p><p class="meta">Opportunities: %s</p></div></div>' % (
        pid, pid, e_(t), e_(b), ", ".join('<a href="#op%d">%d</a>' % (e["rank"], e["rank"]) for e in E if pid in e["patterns"]) or "none")
    for pid, t, b in PATTERNS)

rows = []
for e in E:
    ind = next((h for h in e["how"] if "[independent" in h), e["how"][0]).split(". [")[0]
    rows.append('<tr class="op" data-g="%s"><td class="id"><a href="#op%d"><b>%d</b></a><br><span class="nm">%s</span></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td class="gcell"><span class="badge %s">%s</span><div class="sub">%s</div></td></tr>' % (
        e["grade"], e["rank"], e["rank"], e_(e["title"]), e_(short_analogue(e)), e_(ind), e_(e["precedent"][0]), e_(e["hook"].split(";")[0]), gcls[e["grade"]], GRADES[e["grade"]][0], " ".join('<a href="#%s">%s</a>' % (p, p) for p in e["patterns"])))
table = "\n".join(rows)

def lis(items): return "".join("<li>%s</li>" % e_(i) for i in items)
cards = []
for e in E:
    t = top_by_rank[e["rank"]]
    cards.append('''<article class="entry" id="op%d" data-g="%s">
<header><div class="rank">%d</div><div><h3>%s</h3><p class="lede">%s</p></div><span class="badge %s">%s</span></header>
<div class="grid">
<section><h4>The twin</h4><p>%s</p><h4>Who solved it</h4><ul class="who">%s</ul></section>
<section><h4>How, and how much</h4><ul class="how">%s</ul></section>
<section><h4>The precedent</h4><ul>%s</ul><h4>Existing nuclear hook</h4><p>%s</p></section>
<section><h4>What transfers</h4><ul>%s</ul><h4>What does not</h4><ul class="no">%s</ul></section>
<section><h4>Barriers</h4><p>%s</p><h4>Who to hire</h4><ul class="hire">%s</ul>%s</section>
</div>
<footer><span>Patterns: %s</span><details><summary>Sources (%d)</summary><ul>%s</ul></details></footer>
</article>''' % (
        e["rank"], e["grade"], e["rank"], e_(e["title"]), e_(e["problem"]), gcls[e["grade"]], GRADES[e["grade"]][0],
        e_(e["twin"]), "".join("<li><b>%s.</b> %s</li>" % (e_(a), e_(b)) for a, b in e["analogues"]),
        "".join(how_li(h) for h in e["how"]),
        lis(e["precedent"]), e_(e["hook"]),
        lis(e["transfers"]), lis(e["does_not"]),
        e_(e["barriers"]), "".join("<li><b>%s.</b> %s</li>" % (e_(a), e_(b)) for a, b in e["hire"]),
        ('<p class="caveat">Caveat: %s</p>' % e_(e["note"])) if e.get("note") else "",
        " ".join('<a href="#%s">%s</a>' % (p, p) for p in e["patterns"]) or "none", len(e["sources"]),
        "".join('<li><a href="%s">%s</a></li>' % (e_(u), e_(u)) for u in e["sources"])))
entries_html = "\n".join(cards)
hire_html = "".join('<tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>' % (e_(s), e_(o), ", ".join('<a href="#op%d">%d</a>' % (r, r) for r in ranks)) for s, o, ranks in HIRE_MAP)

page = """<title>Nuclear Analogue Atlas</title>
<meta name="description" content="For each of the twenty nuclear software opportunities, the industry that already solved the same problem, the measured gain, the regulatory precedent, and what transfers">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Condensed:wght@500;600;700&family=IBM+Plex+Sans:ital,wght@0,400;0,500;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root { --paper:#f3f4f1; --paper-2:#e9ebe6; --ink:#12161a; --ink-2:#4b545c; --ink-3:#7c858d; --rule:#cfd4cd; --accent:#1c5cab; --accent-soft:#dbe7f7; --heat:#c9501f; --heat-soft:#f8dccd; --ok:#1e7a3c; --ok-soft:#dcefe0; --warn:#a8600c; --warn-soft:#f6e7cf;
  --mono:"IBM Plex Mono", ui-monospace, Menlo, monospace; --sans:"IBM Plex Sans", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; --disp:"IBM Plex Sans Condensed", "Arial Narrow", system-ui, sans-serif; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { color-scheme:dark; --paper:#15181b; --paper-2:#1d2124; --ink:#eef0ee; --ink-2:#b4bbc1; --ink-3:#8b939b; --rule:#343a3f; --accent:#5598e7; --accent-soft:#1d2f47; --heat:#f08a5e; --heat-soft:#3d2216; --ok:#5dc27c; --ok-soft:#1c3a26; --warn:#e0a24a; --warn-soft:#3d2e14; } }
:root[data-theme="dark"] { color-scheme:dark; --paper:#15181b; --paper-2:#1d2124; --ink:#eef0ee; --ink-2:#b4bbc1; --ink-3:#8b939b; --rule:#343a3f; --accent:#5598e7; --accent-soft:#1d2f47; --heat:#f08a5e; --heat-soft:#3d2216; --ok:#5dc27c; --ok-soft:#1c3a26; --warn:#e0a24a; --warn-soft:#3d2e14; }
body { background:var(--paper); color:var(--ink); font-family:var(--sans); font-size:15.5px; line-height:1.5; padding-inline:clamp(16px, 3vw, 32px); padding-block:24px 64px; }
.wrap { max-width:1400px; margin:0 auto; }
header.tb { border:1.5px solid var(--ink); display:grid; grid-template-columns:2fr 1fr; } header.tb > div { padding:14px 18px; } header.tb .name { border-right:1.5px solid var(--ink); }
h1 { font-family:var(--disp); font-weight:700; font-size:clamp(28px, 5vw, 44px); line-height:1.02; margin:0 0 8px; }
header .lead { color:var(--ink-2); font-size:17px; max-width:70ch; margin:0; }
.meta { font-family:var(--mono); font-size:12px; color:var(--ink-2); display:grid; grid-template-columns:auto 1fr; gap:4px 12px; align-content:start; } .meta b { color:var(--ink); font-weight:500; }
@media (max-width:640px) { header.tb { grid-template-columns:1fr; } header.tb .name { border-right:0; border-bottom:1.5px solid var(--ink); } }
h2 { font-family:var(--disp); font-weight:600; font-size:26px; margin:44px 0 12px; padding-top:14px; border-top:1.5px solid var(--ink); } h2 .num { font-family:var(--mono); font-weight:400; font-size:14px; color:var(--ink-3); margin-right:10px; }
h3 { font-family:var(--disp); font-weight:600; font-size:18px; margin:0 0 4px; } h4 { font-family:var(--disp); font-weight:600; font-size:12.5px; letter-spacing:0.05em; text-transform:uppercase; color:var(--ink-3); margin:10px 0 4px; }
p { max-width:75ch; margin:0 0 12px; } a { color:var(--accent); }
.findings { display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:18px 28px; } .finding p { font-size:14.5px; color:var(--ink-2); }
.patterns { display:grid; grid-template-columns:repeat(auto-fit, minmax(380px, 1fr)); gap:14px; }
.pattern { display:grid; grid-template-columns:44px 1fr; gap:10px; border:1px solid var(--rule); padding:12px 14px; background:var(--paper-2); }
.pattern .pid { font-family:var(--mono); font-size:20px; color:var(--accent); line-height:1.2; } .pattern p { font-size:14px; color:var(--ink-2); margin:0 0 6px; } .pattern p.meta { display:block; font-size:12.5px; }
.filters { display:flex; flex-wrap:wrap; gap:8px; margin:10px 0 14px; }
.filters button { font:inherit; font-size:13.5px; padding:6px 12px; border:1px solid var(--rule); background:var(--paper-2); color:var(--ink); cursor:pointer; border-radius:3px; }
.filters button[aria-pressed="true"] { background:var(--accent); color:#fff; border-color:var(--accent); } .filters button:focus-visible { outline:2px solid var(--accent); outline-offset:2px; }
.tablewrap { overflow-x:auto; border:1px solid var(--rule); }
table { border-collapse:collapse; width:100%%; font-size:13px; } table.score { min-width:1100px; }
th, td { text-align:left; padding:8px 9px; border-bottom:1px solid var(--rule); vertical-align:top; }
thead th { font-family:var(--disp); font-weight:600; font-size:13px; letter-spacing:0.02em; color:var(--ink-2); border-bottom:1.5px solid var(--ink); position:sticky; top:0; background:var(--paper); }
td.id { min-width:150px; } td.id .nm { font-family:var(--disp); font-weight:600; font-size:13.5px; } td.gcell { min-width:110px; } .sub { color:var(--ink-2); font-size:12px; }
.badge { display:inline-block; font-family:var(--disp); font-weight:600; font-size:12px; padding:2px 8px; border-radius:3px; white-space:nowrap; }
.g-direct { background:var(--ok-soft); color:var(--ok); } .g-adapt { background:var(--accent-soft); color:var(--accent); } .g-partial { background:var(--warn-soft); color:var(--warn); }
.q { font-family:var(--mono); font-size:11px; padding:1px 6px; border-radius:3px; margin-left:4px; white-space:nowrap; } .q-ind { background:var(--ok-soft); color:var(--ok); } .q-ven { background:var(--heat-soft); color:var(--heat); } .q-syn { background:var(--warn-soft); color:var(--warn); } .q-mix { background:var(--paper-2); color:var(--ink-2); border:1px solid var(--rule); } .q-unv { background:var(--paper-2); color:var(--warn); border:1px solid var(--warn); }
tr.op[hidden], article.entry[hidden] { display:none; }
article.entry { border:1px solid var(--rule); background:var(--paper-2); margin:0 0 18px; padding:14px 16px; }
article.entry > header { display:grid; grid-template-columns:48px 1fr auto; gap:12px; align-items:start; border-bottom:1px solid var(--rule); padding-bottom:10px; margin-bottom:6px; }
article.entry .rank { font-family:var(--mono); font-size:30px; color:var(--accent); line-height:1; } article.entry .lede { color:var(--ink-2); font-size:14.5px; margin:0; max-width:90ch; }
article.entry .grid { display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:6px 24px; font-size:14px; }
article.entry ul { margin:0 0 8px; padding-left:18px; } article.entry li { margin-bottom:5px; } article.entry p { font-size:14px; }
ul.no li { color:var(--ink-2); } .caveat { font-style:italic; color:var(--warn); font-size:13px; }
article.entry > footer { border-top:1px solid var(--rule); margin-top:8px; padding-top:8px; font-size:12.5px; color:var(--ink-2); display:flex; flex-wrap:wrap; gap:8px 24px; align-items:baseline; }
details summary { cursor:pointer; color:var(--accent); } details ul { font-family:var(--mono); font-size:11.5px; padding-left:18px; margin-top:6px; word-break:break-all; }
table.hire td:first-child { min-width:220px; }
footer.page { margin-top:56px; padding-top:14px; border-top:1px solid var(--rule); color:var(--ink-3); font-size:13px; }
</style>
<div class="wrap">
<header class="tb">
  <div class="name"><h1>Nuclear Analogue Atlas</h1><p class="lead">For each of the twenty software opportunities in the nuclear vertical, the industry that already solved the same problem, how much it gained, the document that let a model be credited, the nuclear rule that could carry it today, and who to hire.</p></div>
  <div class="meta"><span>Opportunities</span><b>20, numbered as in the vertical map</b><span>Grades</span><b>%d direct · %d adapt · %d partial</b><span>Evidence</span><b>%d gain bullets, %d precedents, %d sources</b><span>Date</span><b>%s</b><span>Repo</span><b>research/ANALOG_ATLAS.md</b></div>
</header>

<h2><span class="num">01</span>What the atlas says</h2>
<div class="findings">%s</div>

<h2><span class="num">02</span>Ten patterns behind every successful transfer</h2>
<p>Every case in the atlas where a regulator credited a model, a process or an unattended operation fits one of these. They are the forms a nuclear ask should take.</p>
<div class="patterns">%s</div>

<h2><span class="num">03</span>Scorecard</h2>
<p>Filter by transfer grade. <b>Direct</b>: mechanism and nuclear hook both exist. <b>Adapt</b>: mechanism exists, hook must be built. <b>Partial</b>: only pieces transfer.</p>
<div class="filters" role="group" aria-label="Filter by grade">
  <button type="button" data-f="all" aria-pressed="true">All 20</button>
  <button type="button" data-f="direct" aria-pressed="false">Direct %d</button>
  <button type="button" data-f="adapt" aria-pressed="false">Adapt %d</button>
  <button type="button" data-f="partial" aria-pressed="false">Partial %d</button>
</div>
<div class="tablewrap"><table class="score">
<thead><tr><th>Opportunity</th><th>Solved twin</th><th>Best independent gain</th><th>Precedent that mattered</th><th>Existing nuclear hook</th><th>Grade</th></tr></thead>
<tbody>%s</tbody></table></div>

<h2><span class="num">04</span>The twenty, in full</h2>
<p>Each evidence bullet carries a tag: <span class="q q-ind">independent</span> regulator, audit office or peer review; <span class="q q-ven">vendor</span> self-reported; <span class="q q-syn">synthetic</span> benchmark or model study; <span class="q q-unv">partly verified</span> or <span class="q q-unv">unverified</span> where the fact-check round corrected a figure or could not reach the primary source. The filter above applies here too.</p>
%s

<h2><span class="num">05</span>Hiring map</h2>
<p>Where the people who did this already work, grouped by skill, with the opportunities each group unlocks.</p>
<div class="tablewrap"><table class="hire"><thead><tr><th>Skill</th><th>Where it lives</th><th>Unlocks</th></tr></thead><tbody>%s</tbody></table></div>

<h2><span class="num">06</span>Method and limits</h2>
<p>Five research agents each took four opportunities and searched for the analogue industry, its method, its measured gains and the regulatory instrument, returning sourced reports on %s; the synthesis, grades, patterns and findings are the author's. Opportunity 20 (laser enrichment control) was researched in a second round through OSTI, arXiv and publisher APIs after the web-search budget was spent; a fact-check round then verified or corrected twenty flagged figures. Vendor figures are marked and should be re-verified before external use. Several agents exhausted their search budget, so a few numbers come from secondary sources; those are flagged in the entries.</p>
<footer class="page">Nuclear Analogue Atlas, %s. Companion to the <a href="https://claude.ai/artifact/WBHJtS9bU3agH8MvnLynwq">Nuclear Vertical Atlas</a>. Data and generator: <code>research/analog_atlas_data.py</code>, <code>research/build_atlas.py</code>.</footer>
</div>
<script>
(function(){
  var btns = document.querySelectorAll('.filters button');
  var items = document.querySelectorAll('tr.op, article.entry');
  function apply(f){
    items.forEach(function(r){ r.hidden = !(f === 'all' || r.dataset.g === f); });
    btns.forEach(function(b){ b.setAttribute('aria-pressed', b.dataset.f === f ? 'true' : 'false'); });
    try { localStorage.setItem('naa-filter', f); } catch(e) {}
  }
  btns.forEach(function(b){ b.addEventListener('click', function(){ apply(b.dataset.f); }); });
  var saved = null; try { saved = localStorage.getItem('naa-filter'); } catch(e) {}
  if (saved) apply(saved);
})();
</script>
""" % (gcount["direct"], gcount["adapt"], gcount["partial"], n_gain, n_precedent, n_sources, DATE,
       findings_html, patterns_html, gcount["direct"], gcount["adapt"], gcount["partial"], table, entries_html, hire_html, DATE, DATE)
open("analog_atlas.html", "w").write(page)
print("wrote ANALOG_ATLAS.md (%d KB, %d words) and analog_atlas.html (%d KB); grades %s; %d sources" % (len("\n".join(md))//1024, len("\n".join(md).split()), len(page)//1024, gcount, n_sources))
