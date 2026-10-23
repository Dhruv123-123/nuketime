# V02: Red team of "Grid Headroom Bank"

Method: 14 searches, 4 page reads. Some sources are cited from search titles only. Memory points are marked (unverified).

## Verdict
**Revised score: 15/25 (was 20-21).** c1 3, c2 2, c3 2, c4 5, c5 3. The buyers are excellent. The data edge and the cheap right are both weak. Worst finding: Wood Mackenzie owns both Genscape, which already runs roadside line-flow sensors, and LandGate, which sells powered-land data.

## (a) Does line flow predict will-serve outcomes?
Mostly no.
- Utilities decide from their own planning model. That model checks N-1 contingency, short-circuit, stability and transformer limits. Above all, it counts the load already ahead of you in the queue. Spare margin on a line today is often already promised to someone else. Stability and ride-through limits bind for large loads ([ESIG](https://www.esig.energy/attachment/serve/session-4a-large-loads-interconnection-planning-and-reliability-considerations-julieta-giraldez-and-ahmed-rashwan-2), [arXiv](https://arxiv.org/pdf/2609.11649)).
- The queue swamps the physics:
  - Texas has more than 400 GW of large-load requests for a grid of about 100 GW.
  - About half of those requests come from "wildcat" land entrepreneurs.
  - Utilities quote 2030 for power, and 2033 is more realistic ([Commercial Observer, Jul 2026](https://commercialobserver.com/2026/07/data-center-development-wildcatters/)).
  - If the answer almost everywhere is "wait for an upgrade", a better reading of today's flow changes nothing.
- What predicts outcomes is mostly public but tedious: queue status and planned upgrades (for example [PJM TEAC](https://www2.pjm.com/-/media/committees-groups/committees/teac/2023/20231205/20231205-item-12---dominion-supplemental-projects.ashx)).
- **Fixable?** Partly. Train on queue and study labels, with flows as a prior. But that model needs no hardware.

## (b) Is the right cheap?
No.
- **The proving step is expensive.** Texas SB6 and the proposed PUCT rules require ([Foley, Mar 2026](https://www.foley.com/insights/publications/2026/03/public-utility-commission-of-texas-issues-proposed-rules-for-large-load-interconn/)):
  - a screening study fee of at least $100k, then $100-300k for the next study;
  - **$50k/MW in security**, with 80% forfeited if you withdraw;
  - a **non-refundable $50k/MW fee** after the study;
  - site control (a deed, a 5-year lease or an option), disclosure of duplicate requests, and investment-grade credit or an LC from an A- bank.
  - A 200 MW test therefore puts about $10M at risk, and $20M all-in. The step-up is about $0.3-0.47M/MW, so the trade still works. But this is a capital-heavy land fund, not a cheap option book.
- **Rules are tightening elsewhere too.** Utilities are raising deposits, and one demanded investment-grade credit (Commercial Observer). AEP Ohio now issues formal load-study letters ([AEP Ohio](https://www.aepohio.com/lib/docs/ratesandtariffs/ohio/AEP-Ohio_DCT_Load_Study_Letter_25.11.7.pdf)). TVA has a new data-centre rate ([LandGate](https://www.landgate.com/news/tva-s-new-data-center-rate-is-a-warning-for-site-selection-teams)). Virginia may move to load cluster studies, which weaken the first-mover edge ([interconnection.fyi](https://newsletter.interconnection.fyi/p/queue-update-load-cluster-studies)).
- **The field is crowded:**
  - Cloverleaf raised $300M and sold a 1.3 GW, 1,900-acre site to Vantage for $200M.
  - Silver Lake started a $400M platform with 3 GW secured ([DCD](https://www.datacenterdynamics.com/en/news/vantage-investor-silver-lake-launches-new-powered-land-firm-targeting-data-center/)).
  - EQT-backed Scale bought Reload ([Baxtel](https://baxtel.com/news/eqt-backed-scale-acquires-powered-land-specialist-reload-to-expand-its-data-center-footprint)).
  - NVIDIA is putting about $3B into Lancium ([ABI](https://www.abiresearch.com/market-research/insight/7788432-nvidias-us3-billion-lancium-investment-to-)).
  - Google is buying Intersect Power for $4.75B ([Introl](https://introl.com/blog/google-intersect-power-acquisition-4-75-billion-2026)).
  - Hyperscalers are building in-house land teams. A JLL source says "the true entrepreneurial wildcatter days are probably over" (Commercial Observer).
- **Landowners know.** The claim is $20k going to $400k per acre, or $2 going to $25 per sq ft once transmission is secured (Commercial Observer). Columbus farmland went from $30k to $150k+ per acre ([LandGate](https://www.landgate.com/news/the-hunt-for-powered-land-real-estate-is-rebranding-for-ai-in-2026)). Half a mile from a substation is where every broker already looks.
- **Fixable?** Only by finding substations that look weak on public maps but measure strong. That just loops back to (a).

## (c) Is our sensor redundant?
Largely, yes.
- Genscape already sold a "Transmission RT" service with real-time transmission flow and congestion data ([Power Systems Design](https://www.powersystemsdesign.com/articles/genscape-transmission-rt-service-offers-real-time-transmission-congestion-flow-data/8/5246)). It now sits inside Wood Mackenzie ([WoodMac](https://www.woodmac.com/nslp/power-and-renewables/north-america-power-solutions/)).
- Wood Mackenzie bought LandGate in mid-2026 ([T&D World](https://www.tdworld.com/utility-business/news/55388266/wood-mackenzie-scales-energy-ai-data-solutions-through-landgate-acquisition)). LandGate sells data-centre siting, offtake capacity and available transfer capacity (ATC) data. So one incumbent holds both the sensors and the siting data. It sells data rather than owning land, but "nobody has this" fails. Acres.com sells powered-land screening too ([Acres](https://www.acres.com/blog/find-powered-land-data-centers-using-parcel-nationwide-power-energy-data)).
- Public substitutes:
  - ISO congestion and shadow prices show which lines bind.
  - ERCOT publishes a large-load queue status report ([ERCOT](https://www.ercot.com/files/docs/2023/08/09/July%202023%20LLI%20Queue%20Status%20Update.pdf)).
  - FERC 715 power-flow cases are restricted as CEII, but are available under an NDA (unverified on turnaround).
  - EIA-930 covers only whole balancing areas, so it is no substitute.
- **Fixable?** Weakly. We could add sensors where Genscape is absent (lines at 138 kV and below, rural co-ops). But those nodes are worth less: 230/500 kV sites trade at about 2.4x (Altus).

## (d) Legality and practicality
- Ground stations on private land under a paid easement are fine; Genscape ran them for about 20 years. Stations on road right of way need encroachment permits (unverified).
- **Drones are the problem.** Texas Gov Code 423.0045 bans flying over substations and other critical infrastructure below 400 ft without consent ([TX HB1481](https://capitol.texas.gov/tlodocs/84R/billtext/html/HB01481F.htm)). Similar laws exist in many states (unverified count).
- Separating the phases on corridors with several circuits needs calibration at each site.
- **Fixable?** Yes. Drop the drones and use easements.

## (e) Terranox-shaped and defensible?
- **Shape: half.** The asset that gains value is a queue position plus a deposit, not the land option. The utility decides on that, not our data.
- **Defensibility: low.**
  - The hardware costs about $0.3-0.5M per region to copy, and an incumbent already runs it.
  - Duplicate-request disclosure and credit rules stop us spreading many cheap options.
  - Labels come slowly, perhaps 10-30 a year, and each costs $10M+ at risk.
- **Policy risk:** at least 15 states are considering data-centre bans, and New York has a one-year pause (Commercial Observer).

## Three strongest attacks
1. **Flow is not headroom; the queue decides.** At 4:1 oversubscription, physics rarely binds. Partly fixable, but the fix makes the hardware unnecessary.
2. **The incumbent has the data, and the step is not cheap.** Wood Mackenzie owns both Genscape and LandGate. Funds of $300-400M and hyperscaler teams chase the same sites. Each test puts $50k/MW at risk, 80% forfeitable, plus a $50k/MW fee. Not fixable within this thesis.
3. **Weak compounding moat.** Labels are few and costly, and the hardware is cheap to copy. Partly fixable by holding many queue positions, but disclosure and credit rules cap that.

## Pivot worth checking (unverified)
Point the sensors at generation instead, which was Genscape's original use. Find low-use or retiring plants whose grid connection sits idle. Option the plant and its interconnection right. Then reuse that right for co-located load. FERC has ordered PJM to write co-location rules ([Mayer Brown](https://www.mayerbrown.com/en/insights/publications/2026/01/ferc-directs-pjm-to-facilitate-co-location-arrangements)). This asset is scarcer and closer to Terranox's shape.

## Re-score
| Leg | Old (est.) | New | Why |
|---|---|---|---|
| c1 proving step | 4 | 3 | The step is real, but the sensor barely moves its hit rate |
| c2 proprietary data | 4 | 2 | Genscape flow data and LandGate siting data, both at Wood Mackenzie |
| c3 cheap right | 4 | 2 | Land priced in; $50k/MW security plus a $50k/MW fee; credit needed |
| c4 step-up buyer | 5 | 5 | Cloverleaf $200M for 1.3 GW; Silver Lake; hyperscalers |
| c5 size ladder | 4 | 3 | Large, but a capital-heavy land fund with policy risk |
| **Total** | **20-21** | **15** | |
