# California powered-brownfield experiment

Question (Dhruv, 15 Oct 2026: "use a lot of compute and actually run a really deep experiment of doing this
in cali"): can ML over California's public cleanup record price contaminated sites better than the buyers
who price them today? If it can, a company can buy ex-industrial sites at the stigma discount, remediate the
ones the model says will close fast and cheap, and sell them as powered land. The experiment is the kill test
for the round-4 pick in `../../converge/PICK8.md`.

## Data (all public, all downloaded by `download.py`)

| source | what | why it is illegible |
|---|---|---|
| GeoTracker statewide zip | every cleanup case: type, status history, regulatory activities, coordinates | 100k+ cases, free-text activities |
| GeoTracker EDF by county (4.6 GB) | every lab result ever uploaded: analyte, value, matrix, well, date | 200M+ rows, 500+ analyte codes, mixed units |
| GeoTracker Geo by county | well construction, depth to water, field points, survey coordinates | per-well tables |
| EnviroStor | DTSC cleanup sites with GeoTracker aliases | joins only by alias |
| UST Cleanup Fund (Web Archive) | reimbursed-to-date per claim, 2020 | no bulk download; archived report only |
| CEC/HIFLD substations | 3,371 substations with kV | for the buying simulation |

## Design

* Snapshot panel: at each T in 2004, 2007, ..., 2019 take every case open on 1 Jan T; features use only
  records dated before T; label = closed within 5 years of T; plus time to closure.
* Four scorers: two buyer lookups (case type x county; case type x status x years open), LightGBM on
  structured fields only, LightGBM on everything (lab time series per analyte, wells and depths, activity
  text, neighbour closure history).
* Splits: temporal (train T<=2013, test 2016 and 2019) and leave-counties-out.
* Kill bar: full model beats the best lookup by >= 0.05 AUC on the temporal test and beats the
  structured-only model by >= 0.02. The second gap is the point: it is the value of reading the illegible
  record, which is what ML is for.
* Buying simulation at T=2016: among open sites within 1.5 or 3 km of a >=115 kV substation, the realised
  5-year closure rate of the top 50/100/300 by each scorer versus random.

## Run

    ./run_all.sh                 # ~5 GB download, then build + backtests; needs ~30 GB disk, 12 GB RAM
    SKIP_DOWNLOAD=1 ./run_all.sh # reuse $CA_DATA

Outputs go to `results/` (backtest.json, backtest.md, buy_sim.json, buy_sim.md, top_sites_2016.csv,
SCHEMA.md). Intermediate tables live in `$CA_DATA/work/` and are not committed.

Before trusting the numbers: read `results/SCHEMA.md` and check the analyte-map section; if a common PARLABEL
code is not mapped in `common.ANALYTES`, add it and rerun `build_edf.py` with `--counties` for a test county.

`make_fake.py` builds a synthetic dataset in the same layout so the whole chain can be smoke-tested.
