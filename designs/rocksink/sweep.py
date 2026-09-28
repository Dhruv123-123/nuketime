import json, sys
from model import Design
name = sys.argv[1]
kw = json.loads(sys.argv[2])
d = Design(**kw)
s = d.run(verbose=False)
s["kw"] = kw
json.dump(s, open(f"runs/{name}.json", "w"), indent=1)
print(name, "Tj_peak=%.1f Tw_peak=%.1f flood=%.2f Qunit=%.0f kW  day30 Tj=%.1f  day365 Tj=%.1f" % (s["Tj_peak"], s["Tw_peak"], s["flood_ratio_max"], s["Q_unit_max_kW"], s["day30"]["Tj"], s["day365"]["Tj"]))
