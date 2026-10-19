# Airborne (helicopter) survey pain point: feasibility verdict

Run 2026-10-19. 36 agents: 12 research angles, 3 idea generators (12 unique ideas), 12 scorers on the gold rubric, 9 adversarial refuters on the top three. Raw angle reports are in `angles/`, scores in `SCORES.md` and `ideas_scored.json`. The exploratory-drilling pain point is covered by a separate thread and is not in this folder.

## Verdict

**No new company passes.** Best idea scored 15/25, the top three were each refuted 3/3, and no scorer found that ML or software on public data is what makes this pain point solvable. The survey cost is aircraft time and logistics, which is a hardware and operations problem, and in uranium the survey is a small, early line item next to ground EM and drilling.

Every idea that owns the value the survey creates is a prospect generator: fly or re-read data, stake, option out. That sits inside Dhruv's earlier "no prospecting" rule and overlaps Terranox's own loop. The ideas outside that rule (owned drone fleets, sovereign national surveys, aquifer rights) scored 9-12/25.

## What the step costs, and why

- **The ~US$100k figure is right for one small property.** Helicopter time-domain EM (VTEM, Xcite, AeroTEM, HeliTEM) bills C$117-279 per line-km in invoices filed in BC ARIS (e.g. Berg 2010: 754 line-km, C$99,894 all-in; GK 2008: 83 line-km at C$279/km). US$100k buys about 500-900 line-km, which is one Athabasca block (Stallion 676 km). Multi-property programs run US$0.2-1.8M (Atha's North Terra block alone: 7,166 line-km).
- **Where the money goes:** helicopter time about 40% (AS350B3/H125 at C$2,850-3,130/hr, flying 80-90 km/h at 30-80 m), mobilisation 10-25%, crew and camp 10-12%, standby 0-10%, processing about 8% (model in `angles/cost.md`; only the helicopter rate and crew list are sourced). Actual flying is 2-3 days of a 7-13 day invoice, so for small jobs the cost is mostly logistics. Small surveys pay about 2x per km because the fixed costs barely shrink.
- **In uranium the survey is not the binding cost.** Ground stepwise moving-loop TDEM runs about C$3-6k per line-km (estimate), 20-40x airborne, and drilling dominates: CanAlaska's C$15M 2026 West McArthur budget is three rigs plus ground EM, with no airborne line at all. Airborne is material only for land-bank-scale explorers such as Atha.

## Incumbents and margins

Thin, cyclical contracting that large owners keep leaving. The same airborne assets went CGG to Fugro to CGG to Xcalibur (2021). Aeroquest, the one pure-play with public accounts, ran an 11.6% airborne gross margin in late 2011 and sold to Geotech in 2012 for C$5.6M, about 90% below its 2007 value. SkyTEM made about US$7M gross profit and DKK 7M EBIT in 2025. Xcalibur is consolidating (40+ aircraft, €40M fleet debt Jan 2025, PE stake Jun 2026, buying interpretation firms) and is itself trialling drones and airships.

## What has been tried

- **Drones:** they made magnetics and radiometrics cheap for small, tight blocks (Pioneer, Ontario: C$153/line-km all-in with C$2,500 mobilisation). They have not touched deep EM. Drone TEM carries about 150-3,000x less transmitter moment than helicopter TEM and reaches tens to about 100 m; Athabasca targets sit at 480-1,000 m. Drone passive EM (Expert Geophysics MobileMTd, flying since 2023) and semi-airborne EM (BGR DESMEX) are still prototypes.
- **New sensors:** no single sensor gives 10x, because the sensor is not the cost. Drone passive EM plus shared mobilisation might give about 3-10x on small blocks and 1.5-2x on large ones (estimates).
- **Ground substitutes:** Fleet Space (ambient-noise seismic; US$100M Series D, US$525M valuation, Dec 2024) is a follow-up survey, not a replacement for regional airborne EM.
- **Public data instead of flying:** Saskatchewan's Airborne Surveys layer lists 1,831 company-flown surveys; 335 post-2000 helicopter EM records total about 395,000 line-km (about US$50-80M to re-fly, estimate). Raw contractor data goes public at three years or when the claim lapses (s.68, Mineral Tenure Registry Regulations). Two problems: re-processing cannot add what the original system never measured (depth is set by moment, bandwidth and spacing), and lapsed ground over old surveys is adversely selected, since holders drop what their own interpretation rejected. Saskatchewan also now credits 1.5x the cost of a new airborne survey toward assessment work (SR 62/2024), which subsidises flying fresh.

## Ceiling

- Global airborne geophysical services: about US$1.0-1.5B/yr (DataHorizzon US$1.5B 2024; bottom-up check agrees).
- Corporate mineral-exploration share: about US$370-740M/yr, 3-6% of the US$12.4B 2025 nonferrous budget (S&P), shrinking as grassroots spend hit a record-low share.
- Government buyers are the growth: USGS Earth MRI cumulative acquisition spend went from US$7M (FY19) to US$266M (FY25); only 2% of the US has modern airborne EM.
- Survey-stage step-up on the ground itself is about 3-10x (raw block C$50-300k, conductors identified C$0.3-1.5M; estimates), not 10^4. The 10^4 jump comes only on a drill hit, one rung above what a survey proves.

## The ideas (full table in SCORES.md)

| Score | Idea | Where it sits vs. the no-prospecting rule |
|---|---|---|
| 15 | Lapse Capital: re-stake ground over lapsed public survey data, vend it | Inside the rule; Terranox's loop with a geophysics layer |
| 14 | Lapsed-survey refinery and land bank | Inside the rule |
| 14 | Fly-first, stake-first multi-client surveys (private QUEST) | Inside the rule |
| 13 | Quietfield: drone passive-EM swarm that stakes what it flies | Inside the rule |
| 12 | Tx/Rx Robotics: autonomous semi-airborne EM | Service; outside the rule |
| 12 | Survey-for-equity geophysics fund | Inside the rule |
| 12 | Spec Sweep: pooled campaigns, fly and stake first | Inside the rule |
| 11 | Basin Air: owned uncrewed fleet with pooled mobilisation | Service; outside the rule |
| 11 | Sovereign Autonomous Mapping (data co-ownership + discovery equity) | Mostly outside the rule |
| 11 | Sovereign Sweep: national surveys paid in royalties and block rights | Mostly outside the rule |
| 10 | Aquifer Title: buy water rights, prove them with airborne EM | Outside the rule |
| 9 | Sovereign data co-ownership mapping | Outside the rule |

Why the top three died (3/3 each): buyers at the survey rung are cash-poor juniors paying in shares and work commitments (CanAlaska C$67M market cap, no revenue, C$17.7M TTM loss; Skyharbour C$82M, no revenue); generators (CanAlaska, Skyharbour, Kenorland, Eagle Plains, EMX) already run the model without ML; claim lapses are public in real time on MARS; governments give the same data away free.

## The only leads worth a second look

Refuters named two changes that could move an idea, neither evidenced yet:
1. **Move to a commodity where the airborne conductor is the ore**, such as massive Ni-Cu-PGE or VMS sulphides under cover, where an airborne hit is closer to a drill-ready result than an Athabasca graphitic conductor.
2. **Digitise the roughly 1,118 analog pre-1990 surveys** (chart and film records) with vision models, which only ML makes cheap and no generator has done. This is the one place where ML is the unlock, but it is still a prospect-generator data edge.

## Caveats

The shared web-search budget (200 calls per turn) ran out partway through. The cost, incumbents, ceiling, drones, sensors and public-data angles are sourced; the uranium, ops, adjacent-markets, business-models, startups and economics angles, and most scorers, ran on direct page fetches and prior knowledge. Figures marked "(estimate)" in the angle files are unverified, notably the survey-stage step-up ladder and the ground-EM cost per km.
