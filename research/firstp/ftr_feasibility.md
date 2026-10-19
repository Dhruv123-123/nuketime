# FTR book kill test: feasibility scoping (19 Oct 2026)

Option A in `VERDICT.md` asks one question: does an ML-picked FTR book beat a naive "last year's congestion" book? This note says whether that test can run on public data, what it costs, and gives the first numbers from one auction.

## Verdict

- **Yes, the test can run on public data, starting with PJM.** PJM publishes every cleared annual and long-term FTR. Each row has the path, class, MW, clearing price and a **participant code**. PJM also publishes nodal clearing prices for each round, and hourly day-ahead congestion (cLMP) for every node through the Data Miner API. Monthly-auction bids are public with a 4-month lag. ERCOT publishes CRR results, including every bid, anonymised, plus day-ahead prices. MISO's day-ahead congestion is public, but its FTR results page could not be reached from here (Cloudflare 403).
- **Data costs $0. The real cost is pull time.** PJM archives data older than about 2 years, and the archive cannot be filtered by node. A full nodal backtest therefore means pulling about 350k rows per market day, at the 2-5 minutes per 50k-row page seen today. That is about 1 day of parallel pulling per year of history, or a paid vendor feed (Yes Energy, gridstatus). With the pull, a PJM-only backtest is **2-3 engineer-weeks**. That fits inside the $30-60k / 6-week budget, which also covered MISO.
- **First numbers (PJM 2024/25 Annual auction, round 4, the 42 hub, zone and interface nodes, realised Jun 2024-May 2025):**
  - On liquid aggregate paths, **the auction price is a better forecast than last year's congestion**: mean absolute error $4.3k vs $6.7k per MW-year, correlation 0.95 vs 0.85.
  - **The naive book loses.** Over all node pairs it lost -$2.0k/MW-yr and was right 39% of the time. On the paths the market actually cleared it was flat to negative.
  - **The market's own cleared book on these paths roughly broke even** (-$70/MW-yr).
  - **Simply buying the prevailing-flow direction made +$2.0k/MW-yr, or +22% of the price paid.** That is the known underpricing (risk) premium.
- **What this changes in the kill test.**
  1. The naive "last year" book is a **weak baseline**. It fails even before any ML is involved. The baseline that matters is the **prevailing-flow premium book**: buy every prevailing-flow path at the auction price.
  2. The literature (Leslie) says any edge lives on **illiquid nodal paths**, not hubs and zones, which is where this sample sits. So the decisive test has to be nodal.
- **Revised kill rule.** Kill unless the ML book, out of sample over 2022-26, earns **at least 30% per year on |auction cost| on nodal paths** and **at least 1.5x the better of the premium book and the naive book**. Monthly-auction Sharpe must be at least 1, with volume capped at 5-10% of cleared MW on each path.
  - Why 30%: it is the bar that clears both the free risk premium and the market-average nodal return (22-27%). The top speculators run at 1.6-4x profit on cost.

## 1. Data inventory

| Data | Market | URL / endpoint | Public? | Pulled here? |
|---|---|---|---|---|
| Annual FTR auction results: cleared FTRs (path, class, participant code, MW, MCP), binding constraints, nodal obligation prices, option path prices. Rounds 1-4, 2020/21 to 2026/27 | PJM | `https://www.pjm.com/-/media/DotCom/markets-ops/ftr/annual-ftr-auction/2024-2025/2024-2025-annual-auction-round-4-results.xlsx` (same pattern for other years and rounds; index: https://www.pjm.com/markets-and-operations/ftr) | Yes | **Yes**, 7.5 MB, 119,055 cleared rows |
| Long-term FTR results (3-year) | PJM | `.../markets-ops/ftr/2026-2029-long-term-ftr-auction-results-round-N.xlsx` | Yes | Listed only |
| Monthly FTR auction bids (all bids) | PJM | Data Miner feed `ftr_bids_mnt` (`ftr_bids_annual`, `ftr_bids_long_term` too), https://api.pjm.com/api/v1/ftr_bids_mnt | Yes, 4-month delay, back to 2006 | Metadata only (sample timed out) |
| Day-ahead hourly LMP with congestion component, every pnode | PJM | Data Miner `da_hrl_lmps`, https://api.pjm.com/api/v1/da_hrl_lmps | Yes, needs an API key (free registration at apiportal.pjm.com; the Data Miner web app serves a public key) | **Yes**: hubs, zones and interfaces, Jun 2023-May 2025, about 750k rows |
| FTR credit-calculator cLMPs (monthly) | PJM | Data Miner `ftr_cong_lmp` | Yes | Yes, and **it is a trap** (see §2) |
| Day-ahead LMP / MCC / MLC, all nodes, daily CSV | MISO | `https://docs.misoenergy.org/marketreports/YYYYMMDD_da_expost_lmp.csv` (about 1.1 MB/day) | Yes | **Yes**, 1 day |
| FTR annual and monthly auction results | MISO | misoenergy.org Market Reports (FTR section), files on cdn.misoenergy.org | Public on the web, **blocked here** (Cloudflare 403 on www and cdn) | No, unverified |
| CRR long-term auction results: every bid and offer, anonymised (source, sink, TOU, MW, bid price, shadow price), market results with account holder, binding constraints | ERCOT | Report type 11203 (NP7-802-M): list via `https://www.ercot.com/misapp/servlets/IceDocListJsonWS?reportTypeId=11203`, download via `https://www.ercot.com/misdownload/servlets/mirDownload?doclookupId=<DocID>` (the `ViewReport` link returns "No Document") | Yes, about 3-year retention | **Yes**, 13 MB zip (2029 1st-half annual, seq 6) |
| CRR monthly auction results | ERCOT | Report type 11201 | Yes, only 12 months retained | Listed |
| DAM settlement point prices (CRR payoff = sink SPP - source SPP) | ERCOT | Report 12331 (daily, all points); 13060 (historical hubs and load zones) | Yes | Yes, 1 day |
| FTR profits by participant type | PJM IMM | https://www.monitoringanalytics.com/reports/PJM_State_of_the_Market/2025/2025-som-pjm-sec13.pdf | Yes | Yes |

**Blocked from this sandbox:** www.misoenergy.org and cdn.misoenergy.org (Cloudflare challenge), www.ferc.gov (403), risk.net (JavaScript wall), intra.ece.ucr.edu (503).

**PJM API quirks:**
- Archived data (older than about 2 years) rejects `pnode_id`, `pnode_name`, `zone` and `fields` filters, but accepts `type=HUB|ZONE|INTERFACE|...`.
- A month that straddles the archive boundary returns HTTP 400 and must be split. For October 2024 the split is 1-17 / 18-31.
- Responses are slow: 1-5 minutes per page, with occasional 500 errors.

**What PJM's data uniquely allows:** participant codes on cleared FTRs mean the backtest can compute **each incumbent's realised ROI** by code (e.g. `CIFNGE`, `VIRIB`). The "return an ML book must beat" can then be measured, not assumed.

## 2. The computation (one auction, kept tiny)

**Setup.**
- Auction: PJM 2024/25 Annual, round 4 clearing prices. The price unit is $/MW for the full planning year, per class: OnPeak, WkndOnPeak, DailyOffPeak.
- Universe: the 42 nodes for which the archive allows a type filter (HUB, ZONE, INTERFACE). 40 of them are priced in the auction.
- Realised value of a 1 MW obligation on path s→k in class c: Σ over class hours of (cLMP_k − cLMP_s), using Jun 2024-May 2025 DA congestion.
- Prior-year value: the same sum over Jun 2023-May 2024.
- Payoff: realised value minus clearing price.
- Hour classes: on-peak is hour-beginning 07-22 EPT; NERC holidays count as weekend. The payout ratio is ignored.

| Book | n path-classes | Mean payoff $/MW-yr | Median | Hit rate | Σpayoff / Σ\|price\| |
|---|---|---|---|---|---|
| A. Market: every cleared buy-obligation path in this set | 200 | -70 | -15 | 0.49 | -0.01 |
| B. Naive, cleared paths where prior-year > price | 114 | -672 | +44 | 0.50 | -0.11 |
| C. Complement: cleared paths where prior-year ≤ price | 86 | +727 | -250 | 0.48 | +0.15 |
| D. Naive, all 2,340 pair-classes, direction set by prior-year edge | 2,340 | **-2,045** | -766 | 0.39 | -0.23 |
| G. Naive, top 20% of prior-year edge | 468 | -2,389 | -2,921 | 0.37 | -0.14 |
| E. Prevailing flow (buy the direction with positive price) | 2,340 | **+1,995** | +460 | 0.56 | **+0.22** |

- **Forecast quality.** Correlation with the realised value is 0.953 for the auction price and 0.849 for the prior year. Mean absolute error is $4,287 for the price and $6,707 for the prior year. The correlation between the prior-year edge and the realised edge is **-0.14**: last year's mispricing reversed.
- **Reading.** On aggregate nodes the auction already uses last year's information and improves on it. The only free lunch is the prevailing-flow premium, which matches the underpricing literature. One year and one round is n=1 of regimes. Winter Storm-type months (e.g. Jan 2025) dominate the annual sums.
- **Trap found: the `ftr_cong_lmp` feed is not realised congestion.** A full-nodal version run on it showed a too-good naive book: hit rate 0.88, correlation between prior and realised 0.98. A check against hourly DA data showed why. Western Hub, Jul 2024: the feed says $1.14/MWh, but the realised mean was $4.20. N. Illinois Hub, Jun 2024: the feed says +$0.05, but the realised mean was -$3.53. The feed holds smoothed historical values for credit purposes. Nodal tests must use `da_hrl_lmps`.
- **Scripts and data:**
  - `/tmp/claude-0/-home-user-nuketime/f1c16414-bbbf-52c4-a28a-1827ebc06356/scratchpad/scripts/pull_pjm.py`
  - `/tmp/claude-0/-home-user-nuketime/f1c16414-bbbf-52c4-a28a-1827ebc06356/scratchpad/scripts/analyze.py`
  - Data: `/tmp/claude-0/-home-user-nuketime/f1c16414-bbbf-52c4-a28a-1827ebc06356/scratchpad/ftr_data/` (scratch, not committed)

## 3. Literature: how much mispricing exists, and who captures it

| Source | Market / period | Finding |
|---|---|---|
| Leslie, *Energy Economics* 93 (2021), "Who benefits from ratepayer-funded auctions of TCCs?" | NYISO 2006-15 | ROI on \|cost\| (awarded contracts): **all 16.4%, zone-indexed 8.3%, nodal 26.8%; traders 21.7%, generators 19.3%, retailers -7%**. 1-month products 26.8%, 12-month 11.1%. **88% of trader profit comes from being first into previously illiquid products.** After a profitable purchase becomes public, that product's price rises about 10% in the next auction and the edge is gone. Retailers buy at actuarially fair prices. Edge is nodal only. |
| Deng, Oren & Meliopoulos, *Energy Economics* 32(4) (2010) | NYISO | Clearing prices differ "significantly and systematically" from realised congestion. Part of the gap is structural (auction mechanics), not a price-discovery error. |
| Opgrand, Preckel, Gotham & Liu, *Energy Journal* 43(3) (2022) | PJM | Underpricing comes from ARR supply conditions. Hedgers pay a positive premium; financial traders demand a negative trading premium (collateral cost plus risk). |
| Hildebrandt (CAISO DMM), 2018 testimony to House E&C | CAISO 2009-17, plus others | Ratepayers got **52 cents per $1** paid to non-LSE CRR holders, **"more than a 90 percent annual rate of return"**. MISO ratepayers got <80% of DA congestion rent. Nationwide loss >$400M/yr. PJM financial entities earned about $170M/yr (2011-17). |
| Birge, Hortaçsu, Mercadal & Pavlin, *Energy Economics* 75 (2018) | MISO | Limits to arbitrage. Some financial players took losing virtual positions to move congestion in favour of their FTRs, so FTR P&L can come from cross-product strategies. |
| Baltaduonis et al., *Journal of Energy Markets* | CAISO CRRs 2009-15 | Persistent, mostly positive abnormal returns on certain paths, after adjusting for systematic risk. |
| PJM IMM, 2025 SOM §13 | PJM | Total FTR profit: $897M (2024/25) and $913M (first 7 months of 2025/26). **Financial entities took 77.5%.** Annual-auction buy revenue (cost) was $941M in 2024/25 and $1,264M in 2025/26. Financial entities have been "persistently profitable"; 82-90% of participants were profitable. The top 5 financial participants earn $0.36/MWh at 25% of financial MWh. |
| Yes Energy (FERC EQR data), Jun 2025-May 2026 | All ISOs | FTR profit $4.27B (PJM $3.0B, MISO $0.9B). Top 10 hold about 56%. Profit/cost: DC Energy 4.18x, Saracen 1.99x, Appian Way 1.60x. |
| ML for FTRs | n/a | No published paper found with an ML congestion model backtested against auction prices. The closest is online-learning bidding work (CSEE JPES 2021). The method is proprietary; DC Energy-type firms hold it. |

**What return gap an ML book needs:**
1. **Floor: the free premium.** Buying prevailing flow earned +22% on |price| here. Leslie's market-wide ROI is 16% (8% zone, 27% nodal). An ML book that only matches this is a risk-premium harvester. Anyone with collateral can do that, so it is not an edge.
2. **Bar: the persistent winners.** In NYISO, traders' 21.7% average hides a skewed distribution. The PJM and FERC data show the top shops at 1.6-4x profit on cost. Leslie shows their edge decays within about one auction once revealed. The ML must therefore **discover new mispriced nodal paths every auction**, not hold a static list.
3. **Concrete pass line.** Out of sample, 2022-26 PJM monthly plus annual auctions, nodal universe, as a price-taker capped at 5-10% of cleared MW per path:
   - ROI on |cost| of at least 30%/yr;
   - at least 1.5x the better of the premium book and the naive book;
   - monthly Sharpe of at least 1;
   - positive in at least 4 of 5 planning years;
   - edge not concentrated in a single weather event (drop the top month and re-test).
4. **Leading kill signals.**
   - Most of the ML book's P&L is explained by the prevailing-flow premium.
   - The edge sits on paths already held by the top participant codes, which PJM's public results reveal.
   - Edge decays faster than one auction.

## 4. Smallest next steps (if Dhruv wants the real test)

1. **Register a PJM API key (free).** Pull `da_hrl_lmps` for all nodes, by day, 2019-2026 (about 1 day per year of pulling). Alternatively, quote Yes Energy or gridstatus for nodal DA cLMP history.
2. **Download all annual results** (2019/20-2026/27, 4 rounds each) and `ftr_bids_mnt` (monthly, 4-month lag).
3. **Run in this order:**
   - (a) Repeat the table above on the nodal universe for each auction.
   - (b) Compute each participant code's realised ROI. This gives the bar from data.
   - (c) Only then fit a model (gradient boosting on path features: prior cLMPs, binding-constraint history, outages file, queue additions) and score it out of sample.
   - Step (b) alone, about 1 week, says whether anyone outside the top 10 beats the premium book. If nobody does, kill before any ML is built.
4. ERCOT is the cheapest second market: all bids are public. Its 12-month retention on monthly results, though, means history must be archived from now on.
