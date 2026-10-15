"""Design-basis impact engine, prototype.

Reads a calculation-of-record index (plantx_calcs.txt: synthetic, in the header format of real
nuclear calcs), builds the parameter -> calculation graph, and answers the two questions an uprate
team spends its first months on by hand:

1. Trace: if licensed power (and the calorimetric uncertainty) change, which calculations of record
   are affected, and through which chain of inputs?
2. Margin map: for every acceptance limit, how much power the plant has before that limit binds,
   what a modern analysis method recovers, and which limits need hardware (with lead time).

In the real product step 0 is the hard part: extracting these headers from thousands of scanned
calcs, vendor reports and UFSAR tables (LLM extraction plus engineer review), and keeping the graph
current as calcs are revised. This prototype starts from already-extracted headers.

Run: python3 engine.py [uprate_percent] [new_cal_unc_percent]
     python3 engine.py trace PARAM      (which calcs a change to one parameter reaches)
"""
import re
import sys
from collections import defaultdict, deque

NUM = r"([-+]?\d+(?:\.\d+)?(?:e[-+]?\d+)?)"


def parse(path):
    calcs, cur = {}, None
    for raw in open(path):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        key, _, rest = line.partition(":")
        rest = rest.strip()
        if key == "CALC":
            cid, title = rest.split(None, 1)
            cur = calcs[cid] = dict(id=cid, title=title, inputs=[], outputs={}, sens={},
                                    result=None, limit=None, recover=None, hardware=None)
        elif key == "INPUT":
            m = re.match(r"(\w+)(?:\s*=\s*" + NUM + r")?.*?\((.+)\)", rest)
            cur["inputs"].append(dict(param=m.group(1), value=m.group(2), source=m.group(3)))
        elif key == "OUTPUT":
            m = re.match(r"(\w+)\s*=\s*" + NUM + r"\s*(.*)", rest)
            cur["outputs"][m.group(1)] = (float(m.group(2)), m.group(3))
        elif key == "RESULT":
            m = re.match(r"(\w+)\s*=\s*" + NUM + r"\s*(.*)", rest)
            cur["result"] = (m.group(1), float(m.group(2)), m.group(3))
        elif key == "LIMIT":
            m = re.match(r"(\w+)\s*(<=|>=)\s*" + NUM + r"\s*(.*)", rest)
            cur["limit"] = (m.group(2), float(m.group(3)), m.group(4))
        elif key == "SENS":
            m = re.match(r"(\w+)\s+" + NUM, rest)
            cur["sens"][m.group(1)] = float(m.group(2))
        elif key == "RECOVER":
            m = re.match(r"(.*?)recovers\s+" + NUM + r"\s*(.*)", rest)
            cur["recover"] = (m.group(1).strip(), float(m.group(2)), m.group(3))
        elif key == "HARDWARE":
            cur["hardware"] = rest
    return calcs


def graph(calcs):
    producer, consumers = {}, defaultdict(list)
    for c in calcs.values():
        for p in c["outputs"]:
            producer[p] = c["id"]
        for i in c["inputs"]:
            consumers[i["param"]].append(c["id"])
    # root parameters are those given a value in an INPUT line
    for c in calcs.values():
        for i in c["inputs"]:
            if i["value"] is not None:
                producer.setdefault(i["param"], c["id"])
    return producer, consumers


def trace(calcs, changed):
    """Breadth-first: calc -> the chain of parameters that makes it affected."""
    producer, consumers = graph(calcs)
    why, seen, q = {}, set(), deque((p, [p]) for p in changed)
    while q:
        param, chain = q.popleft()
        for cid in consumers[param]:
            if cid not in why:
                why[cid] = chain
            for out in calcs[cid]["outputs"]:
                if (cid, out) not in seen:
                    seen.add((cid, out))
                    q.append((out, chain + [f"{cid}", out]))
    return why


def depends_on(calcs, cid, root, memo=None):
    """True if calc cid uses root directly or through another calc's OUTPUT (not a shared root)."""
    memo = {} if memo is None else memo
    if (cid, root) in memo:
        return memo[(cid, root)]
    out_of = {p: c["id"] for c in calcs.values() for p in c["outputs"]}
    hit = False
    for i in calcs[cid]["inputs"]:
        if i["param"] == root:
            hit = True
        elif i["param"] in out_of and out_of[i["param"]] != cid:
            hit = hit or depends_on(calcs, out_of[i["param"]], root, memo)
    memo[(cid, root)] = hit
    return hit


def margin_map(calcs, old_unc=2.0, new_unc=2.0):
    """Headroom in % of licensed power for each acceptance limit.

    Safety analyses that carry the calorimetric uncertainty are run at RTP x (1 + unc); cutting the
    uncertainty (an ultrasonic feedwater flow meter: the 'MUR' uprate) returns that difference to
    them. Balance-of-plant equipment sees real power, so it gets nothing back."""
    rows = []
    for c in calcs.values():
        if not c["limit"]:
            continue
        name, val, unit = c["result"]
        op, lim, basis = c["limit"]
        s = c["sens"][name]
        room = (lim - val) / s if op == "<=" else (val - lim) / -s   # % power to the limit
        credit = (old_unc - new_unc) if depends_on(calcs, c["id"], "CAL_UNC") else 0.0
        rec = c["recover"][1] / abs(s) if c["recover"] else 0.0
        rows.append(dict(calc=c["id"], title=c["title"], result=f"{val:g} {unit}".strip(),
                         limit=f"{op} {lim:g} ({basis})", headroom=room + credit,
                         with_methods=room + credit + rec,
                         method=c["recover"][0] if c["recover"] else "",
                         hardware=c["hardware"] or ""))
    return sorted(rows, key=lambda r: r["headroom"])


def report(path, uprate, new_unc):
    calcs = parse(path)
    changed = ["RTP"] + (["CAL_UNC"] if new_unc != 2.0 else [])
    why = trace(calcs, changed)
    rows = margin_map(calcs, 2.0, new_unc)
    out = [f"# Impact report: +{uprate:g}% licensed power, calorimetric uncertainty {new_unc:g}%", ""]
    out.append(f"{len(why)} of {len(calcs)} calculations of record are affected.\n")
    out.append("| Calc | Title | Affected through |")
    out.append("|---|---|---|")
    for cid in calcs:
        if cid in why:
            out.append(f"| {cid} | {calcs[cid]['title']} | {' -> '.join(why[cid])} |")
    out.append("")
    out.append("## Margin map (headroom in % of licensed power before each limit binds)")
    out.append("")
    out.append("| Calc | Limit | Headroom % | With modern method % | Status at this uprate | Fix |")
    out.append("|---|---|---|---|---|---|")
    for r in rows:
        if r["headroom"] >= uprate:
            status, fix = "OK", ""
        elif r["with_methods"] >= uprate:
            status, fix = "re-analyse", r["method"]
        else:
            status, fix = "EXCEEDED", r["hardware"] or "needs new analysis basis or hardware"
        h = lambda x: f"{x:.1f}" if x < 100 else ">100"
        out.append(f"| {r['calc']} | {r['limit']} | {h(r['headroom'])} | {h(r['with_methods'])} | "
                   f"{status} | {fix} |")
    analysis_only = min(r["headroom"] for r in rows)
    methods = min(r["with_methods"] for r in rows if not r["hardware"])
    bop = [r for r in rows if r["hardware"]]
    out.append("")
    out.append(f"Uprate available with no new analysis methods or hardware: {analysis_only:.1f}% "
               f"(binding: {rows[0]['calc']}).")
    out.append(f"Safety-analysis ceiling with modern methods: {methods:.1f}%. "
               f"Hardware needed beyond: " + ", ".join(f"{r['calc']} at {r['headroom']:.1f}%" for r in bop) + ".")
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "trace":
        calcs = parse("plantx_calcs.txt")
        why = trace(calcs, [sys.argv[2]])
        print(f"{sys.argv[2]} reaches {len(why)} of {len(calcs)} calcs:")
        for cid, chain in why.items():
            print(f"  {cid:10s} {calcs[cid]['title']}  [{' -> '.join(chain)}]")
        sys.exit()
    up = float(sys.argv[1]) if len(sys.argv) > 1 else 5.0
    unc = float(sys.argv[2]) if len(sys.argv) > 2 else 2.0
    print(report("plantx_calcs.txt", up, unc))
