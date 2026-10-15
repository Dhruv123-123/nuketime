# Margin: design-basis impact engine and uprate models

Supports `research/converge/PICK6.md`.

| File | What it is | Run |
|---|---|---|
| `plantx_calcs.txt` | Synthetic calculation-of-record index (23 calcs) for a 3,411 MWt four-loop PWR, in the header format of real calcs. Values are illustrative, not from any plant. | data |
| `engine.py` | Prototype impact engine: parses the index, builds the parameter-to-calc graph, traces what a change reaches and maps headroom to every limit (with the calorimetric-uncertainty credit a flow-meter recapture earns). | `python3 engine.py 7 0.4`, `python3 engine.py trace DECAY_HEAT` |
| `report_mur.md`, `report_stretch7.md` | Engine output for a 1.6 % recapture and a 7 % uprate | |
| `impact.py` | Monte Carlo of a 31-node extended-uprate analysis graph, today vs an impact engine vs a weak engine, gated by refuelling outages, NRC review and hardware lead time | `python3 impact.py > results.json` |
| `firm.py` | Addressable engineering pool and revenue scenarios for an AI-native nuclear engineering firm | `python3 firm.py > firm_results.json` |

All assumptions are labelled in the code. The two that drive the value (12 % of analyses missed in
today's scoping; drafting speed factors by owner) are tested first in PICK6's eight-week plan using
NRC's public record of uprate licence amendments and their requests for additional information.
