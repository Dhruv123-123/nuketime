# Deep check: distributed capacity utility in PJM (v5 #1)

19 Oct 2026. Frame: `V5_OPTIMIST.md` (optimistic on tech, rigorous on numbers and time). Idea under test: `v5_energy.md` #1, scored 20/25. The model is to own 0.5-3 MW behind-the-meter (BTM) batteries at C&I sites, register them as PJM capacity, sell that capacity to data-centre-serving load under 5-10 yr contracts, share demand-charge savings with hosts, and use AI to cut soft costs from ~$300k to ~$100k per MW.

**Verdict: 17/25 as written, so it fails. A narrowed version can reach 19 if a 6-10 week test hits three thresholds.**

The v5 model got three things wrong:
1. **Capacity accreditation.** It counted capacity at a 92% ELCC applied to the full nameplate MW. A 4-hour battery registered as demand response (DR) does get the 91% DR rating. However, DR is now a 24-hour product with penalties of ~$2,300/MWh, so a 4-hour battery can safely nominate only ~75-85% of its nameplate.
2. **Hardware cost.** It assumed $300/kWh all-in, but C&I systems that comply with the 2026 foreign-entity (FEOC) rules cost about $325-450/kWh.
3. **Post-2030 decline.** Its 14% IRR ignored the drop in capacity price after the price collar ends, and the augmentation capex.

Rebuilt, the base case (PECO/ComEd, the zones v5 chose for the test) earns **4-5% unlevered**, which is below the cost of capital.

The idea survives only in a different place: high-transmission-cost zones, PSEG above all, where the network transmission rate is **$183k/MW-yr**. There the battery earns three stacked payments:
- shaving the customer's share of the annual zonal peak (its NSPL tag), which cuts its transmission charge;
- a DR capacity contract;
- the host's demand-charge share.

That reaches **~12% unlevered and ~17% levered with the AI cost stack, versus ~9% and ~11% for an incumbent's cost stack**. The AI soft-cost move is real and worth about +3 points of IRR. It is the margin, but it cannot rescue a bad zone.

---

## 1. Can BTM batteries sell PJM capacity, and at what accreditation?

| Question | Finding | Source |
|---|---|---|
| ELCC, 2028/29 BRA (final) | **4-hr storage 59%**, 6-hr 68%, 8-hr 71%, **Demand Resource 91%**, Gas CT 67%, CC 78%, Nuclear 96% | [PJM, ELCC class ratings for 2028/29 BRA (Feb 2026)](https://www.pjm.com/-/media/DotCom/planning/res-adeq/elcc/28-29-bra-elcc-class-ratings.pdf) |
| ELCC, 2027/28 | 4-hr storage 58%; DR rose from 69% to 92% because DR became a 24-hour, all-year product from 2027/28 (FERC accepted this 5 May 2025) | [ESS News](https://www.ess-news.com/2025/12/16/long-duration-storage-emerges-triumphant-under-pjms-new-scheme/); [Environment+Energy Leader](https://environmentenergyleader.com/stories/pjm-demand-response-rules-now-reach-overnight-hours,143201) |
| How a BTM battery participates | **As DR** (Load Management / Emergency Load Response through a curtailment service provider), measured against the host's peak load contribution (PLC) and a winter peak load set at hour ending 9 (HE9). It cannot be a "storage" capacity resource unless it goes through the interconnection queue. The DER Aggregator model (Order 2222) slipped to **1 Feb 2028**. | [PJM FO 2222 clean-up filing (Oct 2025)](https://www.pjm.com/-/media/DotCom/committees-groups/subcommittees/disrs/2025/20251006/20251006-item-03---fo-2222-clean-up-filing.pdf); [Renewable Energy World](https://www.renewableenergyworld.com/energy-business/policy-and-regulation/pjm-proposes-a-2-year-delay-for-implementing-the-der-aggregation-model/) |
| Implication | DR-registered batteries get the **91%** DR rating rather than the 59% storage rating, which is good news. The catch is that DR must perform in any hour, with no cap on event duration. A 4-hour battery facing an 8-hour event under-delivers. The penalty (PAI) rate for 2027/28 is ~**$2,300/MWh**, with a non-PAI rate of ~$1,150 that PJM proposes to raise to ~$2,575; annual stop-loss is 1.5× the capacity revenue. PJM is calling events more often (Enel). | [PJM MRC 25 Mar 2026, LM/PRD performance](https://www.pjm.com/-/media/DotCom/committees-groups/committees/mrc/2026/20260325/20260325-item-04---1-load-management-and-prd-performance-solution---presentation.pdf); [PJM MIC Jan 2026](https://www.pjm.com/-/media/DotCom/committees-groups/committees/mic/2026/20260120/20260120-item-01-1---load-management--price-responsive-demand-event-performance---pjm.pdf); [Enel 2028/29 BRA blog](https://www.enelnorthamerica.com/insights/blogs/pjm-2028-2029-capacity-auction-results) |
| 2027/28 BRA | $333.44/MW-day (the cap); DR cleared 7,299 MW | [Enel 2027/28](https://www.enelnorthamerica.com/insights/blogs/pjm-2027-2028-capacity-auction-results) |
| 2028/29 BRA (cleared 14 Jul 2026) | **$325/MW-day (cap) in every zone** ($118,625/MW-yr); 138,318 MW cleared; **6,831 MW short**; uncapped price would have been $554.72; DR cleared 7,017 MW | [PJM release 14 Jul 2026](https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2026-releases/20260714-pjm-capacity-auction-procures-138318-mw-of-generation-resources.pdf); [publicpower.org](https://www.publicpower.org/periodical/article/pjm-capacity-auction-procures-138318-mw-generation-resources-capacity-price-comes-cap-325); [Enel](https://www.enelnorthamerica.com/insights/blogs/pjm-2028-2029-capacity-auction-results) |
| A 4-hr front-of-meter battery for comparison | ~$70/kW-yr at 59% ELCC | [Modo Energy](https://modoenergy.com/research/en/pjm-capacity-auction-2028-2029-reliability-price-cap-elcc) |
| Price collar | FERC accepted it 28 Apr 2026: cap ~$325, floor ~$175/MW-day (adjusted for accreditation) for **2028/29 and 2029/30** only. The 2029/30 BRA closes 15 Dec 2026. Nothing protects prices from **2030/31** onward. | [JD Supra, FERC accepts collar extension](https://www.jdsupra.com/legalnews/ferc-accepts-pjm-capacity-market-price-1132646/); [Troutman](https://www.troutmanenergyreport.com/2026/03/pjm-seeks-extension-of-price-collar-for-capacity-auctions/) |
| Reliability Backstop Procurement (RBP) | Filed 31 Jul 2026 (ER26-3380). Target 6,831 MW; offer cap **$555/MW-day** (MW-weighted average); **15-year terms through 2042/43**; in service by 1 Jun 2032. FERC (29 Sep 2026) **kept DR and DER aggregations eligible**, overruling the market monitor, and **kept the 15-yr lock-in**. It also suspended the procurement for 5 months (effective 28 Feb 2027) and set cost allocation and LSE collateral for hearing. PJM pulled the 30 Sep auction, with a revised filing due ~29 Oct. New batteries at existing DR sites count as net-new. Each site behind a DR/DER offer must be under contract **before bidding**. | [Utility Dive, delay](https://www.utilitydive.com/news/pjm-delays-backstop-procurement-ferc-data-center/831751/); [Utility Dive, filing](https://www.utilitydive.com/news/pjm-backstop-capacity-auction-ferc-data-centers/826792/); [mgrid.org analysis of FERC order](https://mgrid.org/2026/10/03/ferc-keeps-der-aggregators-in-pjms-6831-mw-backstop-then-upholds-the-15-year-lock-in-few-can-meet/) |
| Bilateral path | Charles River Associates (CRA) runs confidential matching of load and new supply over 6-9 months from Jul 2026. "Offset" bilaterals have looser criteria, with terms as short as 5 yrs. BTM eligibility was argued for by Calibrant and Convergent (Stack Energy deck, 16 Mar 2026) with 38 supporters, including Google, MD, PA, NJ, Constellation, Vistra and Voltus. Opponents were the market monitor, Buckeye and Invenergy. | [Stack Energy deck for Calibrant/Convergent](https://www.pjm.com/-/media/DotCom/committees-groups/workshops/rbpw/postings/behind-the-meter-capacity-participation-in-the-reliability-backstop-procurement.pdf); [Voltus submission to PJM Board, Jun 2026](https://www.pjm.com/-/media/DotCom/committees-groups/cifp-rbp/2026/20260630/20260630-item-02l---voltus---cm-and-rbp---executive-summary.pdf) |
| Bilateral price evidence | Google and Voltus signed a "Bring Your Own Capacity" (BYOC) deal: **up to 100 MW a year for 3 years** in PJM, coming online in 2027. **Price not disclosed.** | [Latitude Media](https://www.latitudemedia.com/news/google-is-voltus-first-bring-your-own-capacity-customer/); [DCD](https://www.datacenterdynamics.com/en/news/google-signs-100mw-bring-your-own-capacity-agreement-with-voltus/) |

**What v5 got wrong.**
- The "5-10 yr data-centre bilateral at ~$270/MW-day" has no public price comparable.
- The only long-tenor public instrument, the RBP, demands **15 years** and signed host contracts before bidding, and it is now suspended.

**What v5 under-sold.** The 15-year lock-in suits an *asset owner* holding 15-yr site leases much better than an aggregator holding 1-3 yr DR customer contracts. Advanced Energy United told FERC that "few DR/DER aggregations hold customers for 15 years." This is the one structural edge an owner model has over Voltus and CPower.

## 2. Costs, tax credits, tariffs

**Installed cost (1 MW / 4 MWh C&I, PJM, 2026).**
- No 2026 primary benchmark exists.
- Industry ranges are $250-450/kWh installed for C&I, falling to $180-300 for large standardised containers ([sunlithenergy via Lazard search](https://sunlithenergy.com/?p=6728)).
- Lazard's 2025 C&I levelised cost of storage (LCOS) is $319-506/MWh for a 1 MW / 2 h system ([Energy-Storage.news](https://www.energy-storage.news/?p=81297)).
- Tariffs on Chinese grid cells are ~65-82% from Jan 2026, after the Section 301 step-up ([Energy-Storage.news tariff analysis](https://www.energy-storage.news/?p=80188); [Yale CEF](https://cleanenergyforum.yale.edu/2025/07/22/impacts-of-trump-administration-tariffs-on-the-battery-energy-storage-system-market)).
- BNEF's US turnkey price for 2025 was $219/kWh at utility scale (v5 facts table).
- **Used here: $350/kWh = $1.40M/MW of hardware and EPC (range $300-450).** v5 used $1.20M.

**Tax credits after the One Big Beautiful Bill Act (OBBBA).**
- 48E storage ITC at 30% through 2033 for standalone storage ([S&P](https://www.spglobal.com/market-intelligence/en/news-insights/research/2025/10/nearly-two-thirds-of-planned-us-bess-projects-eligible-for-40-tax-credits)).
- FEOC "material assistance" rules apply to construction starting after 31 Dec 2025. The non-foreign-entity cost share must be ≥**55% in 2026**, rising 5 pts a year to 75% by 2030. Cells carry heavy weight in the safe-harbour tables, ~52% of direct cost in some configurations. Notice 2026-15 is partial guidance, with full tables promised by end-2026 ([Energy-Storage.news](https://www.energy-storage.news/feoc-compliance-for-bess-is-a-decade-long-obligation/); [Norton Rose, Notice 2026-15](https://www.projectfinance.law/publications/new-feoc-guidance-notice-2026-15)).
- The FEOC test applies through the recapture period, so it is a 10-year obligation.
- A domestic-content adder of +10% is possible, but only with US cells at a premium. I treat it as upside.
- **Used here: 30% ITC on hardware plus half of soft costs, sold through transfer at $0.93.**

**Host-side tariff values** (these, not demand charges, are the big lever):

| Zone | Network transmission rate (NITS), $/MW-yr, 1 Jun 2026 | Distribution demand charge (example) |
|---|---|---|
| PSEG | **183,353** | LPL-S >500 kW: $27.18 / $41.17 per kW-month by season, bundled on the OpenEI record, effective 1 Apr 2026 ([OpenEI](https://apps.openei.org/IURDB/rate/view/69e260f7a75acac5df0e8fdd)) |
| AEP | 138,849 | n/a |
| PPL | 112,973 | n/a |
| Met-Ed / Penelec | 96,066 | n/a |
| Dominion | 85,191 | GS-3 not found |
| BGE | 56,999 | GL not found |
| ComEd | 46,876 | distribution facilities charge (DFC) per kW, value not retrieved ([IPA/ComEd](https://ipa.illinois.gov/content/dam/soi/en/web/ipa/documents/20260611-response-irp-ra-comed.pdf)) |
| PECO | **29,542** | GS $11.35/kW (2025, secondary source; [Nectar](https://nectarclimate.com/rates/peco-energy-co)) |

NITS source: [PJM NITS rates, Jun 2026](https://www.pjm.com/-/media/DotCom/markets-ops/settlements/network-integration-trans-service-june-2026.pdf).

The NITS charge reaches retail customers through their network service peak load (NSPL) tag. In NJ, PSEG zone, the tag is set at the 1-hour summer coincident peak (1CP). Pass-through rules differ by distribution utility, which I did not verify zone by zone.

**The key finding: the v5 test zones (PECO, ComEd) are the two worst transmission zones in PJM, and PSEG is 6x PECO.**

NJ also has GSESP Phase 2, which targets **500-800 MW of BTM and distribution storage** with fixed plus performance incentives. Phase 1 pays 15-yr fixed $/MW-yr. The Phase 2 straw proposal came out 17 Aug 2026 (docket QO26040116), and its $/kW is not yet public ([Stem NJ playbook](https://www.stem.com/the-nj-storage-playbook-inside-gsesp-phase-2-and-beyond-part-1/); [NJ BPU Sep 2026 stakeholder deck](https://www.nj.gov/bpu/pdf/publicnotice/Phase2%20Block1_Sep%202026%20Public%20Stakeholder%20Meeting.pdf)). This is upside I have not counted.

**Stacking caveat.**
- The PLC tag is set from 5 summer peak hours, and the NSPL tag from 1 hour.
- Shaving the 1CP hour lowers next year's PLC by ~1/5 of the shaved MW, which shrinks the DR nomination.
- I apply ~0.85 MW of effective nomination and NSPL shaving to 1 MW of nameplate, which absorbs this effect along with the duration buffer.

## 3. Soft costs and customer acquisition: what the comparables show

- **Stem.** It did not go bankrupt.
  - FY2025 10-K: ~27% workforce cut (Apr 2025), $6.1M restructuring cost, and a pivot to PowerTrack software.
  - Earlier: ~$547M goodwill impairment and ~$38.7M of hardware/inventory/AR write-offs.
  - It paused two products and did a reverse split ([10-K FY2025](https://www.sec.gov/Archives/edgar/data/1758766/000175876626000016/stem-20251231.htm); [Q1 2025 release](https://investors.stem.com/news-events/press-releases/detail/105/stem-announces-first-quarter-2025-results)).
  - Why the owned/shared-savings C&I model stalled, in my synthesis since no root-cause filing exists:
    - The value base was California demand charges, which moved when time-of-use windows shifted ([pv magazine 2019](https://pv-magazine-usa.com/2019/08/27/demand-charges-energy-arbitrage-and-behind-the-meter-energy-storage/)).
    - It depended on the SGIP subsidy.
    - There was no long-dated contracted revenue to finance against.
    - After the SPAC it drifted into low-margin hardware resale and an expensive software acquisition.
  - **I found no published customer acquisition cost (CAC) figure for Stem, Enel X, Voltus, Calibrant, Convergent or Base.** The $300k → $100k/MW soft-cost claim is my estimate: 20-25% of a $1.2-1.5M C&I project, in line with C&I solar soft-cost shares. It is not a sourced figure.
- **Advanced Microgrid Solutions (AMS).** Fluence bought its software business in Oct 2020 for an undisclosed price ([pv magazine](https://pv-magazine-usa.com/2020/10/15/fluence-acquires-advanced-microgrid-solutions-in-bid-to-help-customers-monetize-storage-renewable-assets/)). The owned-asset business did not survive as a standalone company.
- **Calibrant.** A Macquarie GIG / Siemens joint venture since 2020; it **acquired Enel's distributed energy solutions business (Enel DES, Oct 2024)**; it is doing data-centre battery projects (Feb 2026) and hired a PJM policy executive (Jul 2026) ([Akin Gump](https://www.akingump.com/en/insights/press-releases/akin-gump-advises-macquarie-capital-in-launch-of-calibrant-energy-joint-venture); [CB Insights](https://www.cbinsights.com/company/calibrant-energy/financials)). It is the closest direct rival and is backed by Macquarie's balance sheet.
- **Convergent.** Co-sponsor of the BTM-in-backstop deck. I did not find its funding.
- **Voltus.** $225M Series D (2026), Google BYOC customer, acquired the battery startup Brightfield to "double down on batteries", target of 20 GW by 2030, possible IPO ([Latitude Media](https://www.latitudemedia.com/news/voltus-raises-225-million-to-scale-byoc-for-data-centers/)). It is moving into batteries at existing DR sites, which are exactly our hosts.
- **Base Power.** $1B Series D at **$13B post-money** (Aug 2026), with a factory in Austin. It is residential, but launched in ComEd in Jun 2026 ([Dealroom](https://dealroom.co/news/142739-base-power-raises-1b-series-d-at-13b-valuation-launches-us-built-home-ba/)).

## 4. Per-MW cash flow and IRR (rebuilt)

**Assumptions** (model at `/tmp/claude-0/-home-user-nuketime/f1c16414-bbbf-52c4-a28a-1827ebc06356/scratchpad/model.py`):
- 1 MW / 4 MWh, 15 years, 1.5%/yr degradation, $150k augmentation in year 8.
- DR nomination of 0.85 MW × 91% ELCC.
- Capacity at $300/MW-day for years 1-5 (bilateral or at the cap), then $225.
- Host distribution demand-charge share $43k (50% of ~0.6 MW × ~$12/kW-month).
- NSPL share = 0.85 × NITS × 50%; energy/TOU $10k; expected DR penalty $8k.
- O&M + insurance + lease: $16k with the AI stack, $20k for an incumbent.
- Soft costs: $0.12M with AI, $0.30M for an incumbent.
- Hardware and EPC $1.40M; ITC 30%; debt 55% at 7.5% over 12 years.

| Zone (NITS) | AI net capex | Year-1 cash flow | AI unlevered IRR | AI equity IRR | Incumbent unlevered IRR | Incumbent equity IRR |
|---|---|---|---|---|---|---|
| **PSEG ($183k)** | $1.11M | $192k | **12.2%** | **17.0%** | 9.3% | 11.0% |
| AEP ($139k) | $1.11M | $173k | 10.0% | 12.4% | 7.1% | 6.7% |
| PPL ($113k) | $1.11M | $162k | 8.6% | 9.6% | 5.8% | 4.2% |
| Dominion ($85k) | $1.11M | $150k | 7.0% | 6.6% | 4.4% | 1.3% |
| ComEd ($47k) | $1.11M | $134k | 4.8% | 2.0% | 2.2% | -3.1% |
| PECO ($30k) | $1.11M | $126k | 3.7% | -0.1% | 1.2% | -5.1% |

**Sensitivities** (generic zone with the v5 stack: $1.50M hardware, $22k NSPL share, $300 then $200):

| Case | Unlevered IRR |
|---|---|
| Base | 3.5% |
| Hardware at $300/kWh | 6.8% |
| Hardware at $450/kWh | 1.0% |
| Capacity floor $175 throughout | 0.9% |
| Host share falls to 25% | -1.6% |
| A 15-yr RBP award at a flat $450 | 10.6% |

**Best realistic stack:** $325/kWh, NSPL share $40k, backup/resilience fee plus TOU $25k, a 10-yr data-centre contract at $350 then $250. This gives **13.2% unlevered and 19% levered with AI, versus 10.0% and 12.5% for an incumbent**. Adding the 10% domestic-content adder gives 14.6% / 21.7%.

**AI effect, quantified.** Cutting soft costs from $0.30M to $0.12M and O&M by $4k adds **+2.4 to +3.2 pts unlevered and +5 to +6.5 pts equity** in every zone. In PSEG it is the difference between an infrastructure-grade deal (12%) and a marginal one (9%).

**Capital to 600 MW and $100M revenue.**
- Gross revenue per MW (capacity + our host shares + energy) is ~$190k in PSEG-type zones and ~$140k in a blended PJM mix.
- **$100M of revenue ≈ 525-700 MW ≈ 550-750 sites.**
- Project capital ≈ $1.11M × 600 = **~$670M** net of ITC, with ITC bridge/transfer facilities on top, plus ~$0.84B gross.
- Debt at 55-60% is ~$370-400M. Contracted DR plus tariff savings support DSCR ~2x outside the augmentation year, so leverage of 60-65% is plausible once there are 24 months of telemetry.
- Equity ~$270-300M. Of that, ~$100-150M is corporate VC for the platform and development; the rest is project-level infrastructure equity, the Hunt/Manulife or Calibrant/Macquarie pattern.
- That is raisable *only if* the portfolio earns ≥10% unlevered, which means concentrating in PSEG/AEP/PPL.
- **There may not be enough PSEG-quality sites for 600 MW.** PSEG zone peak is ~10 GW. The number of LPL hosts ≥1 MW is unverified (my estimate is ~2-4k).

**Time.**
- C&I installs take 6-12 months.
- DR registration for the 2027/28 delivery year (from 1 Jun 2027) is feasible, and NSPL/PLC savings start after the first summer peak is shaved, i.e. tags reset in year 2.
- First revenue in ~12-18 months, so T stays at 4.
- $100M revenue by year 6-7 needs ~100-120 sites a year from year 3. Hunt did 33 larger sites in 5 years; Base ramps faster but in residential.

## 5. Ceiling and the ladder

| Rung | Status (sourced) | Read |
|---|---|---|
| PJM | 3 straight auctions at the cap; 6.8 GW short; collar ends after 2029/30; RBP one-shot and delayed | Core market. Value is concentrated in high-NITS zones. |
| NYISO | NYC Zone J spot hit a record $32.6/kW-month in May 2026, then fell to $12.4 in July after CHPE came online ([Modo](https://modoenergy.com/research/nyiso-capacity-prices-record-summer-2026)) | Best per-kW value in the US, but volatile, and FDNY fire code adds cost. A good second market for the AI permitting edge. |
| ISO-NE | Forward capacity auction delayed. First prompt/seasonal auction for 2028/29 around May 2028 (CAR-PD accepted, ER26-925). Order 2222 effective 1 Nov 2026 ([Utility Dive](https://www.utilitydive.com/news/iso-new-england-capacity-market-prompt-seasonal-FCA19-delay/707339/)) | Opens in 2028. |
| MISO | 2026/27 summer $424/MW-day North/Central, annualised ~$120 (v5); Order 2222 in 2029 | Seasonal and volatile; weaker. |
| Retail supply to hosts | Retail choice in PA/NJ/MD/OH/IL | Supplying the host lets us keep 100% of the PLC/NSPL savings instead of 50%. That adds +$40-90k/MW-yr in PSEG-type zones and is the biggest economic lever after zone choice. |
| Owning the data-centre power relationship | Voltus/Google BYOC already occupies this rung; Calibrant is doing data-centre batteries | A contested rung, not open ground. |

At 3 GW × ~$170k = ~$500M revenue at ~70% EBITDA, a 12-14x multiple gives **$4-5B**. $10B+ needs retail supply at scale plus NY/NE. **C = 4** is generous; 3.5 is honest.

## 6. Kill risks, AI answers, quantified

| # | Kill risk | AI counter-move | Quantified effect | Does it hold? |
|---|---|---|---|---|
| 1 | Hardware at $350-450/kWh under FEOC rules | AI sizing from 15-minute interval data: right-size kWh per site (3-3.5 h, not a blanket 4 h) and pick sites where the shave hits ~0.85 of nameplate | -10-15% kWh, i.e. -$0.15-0.2M/MW, i.e. +2 pts IRR | Partly. Cell cost itself is not AI-addressable. |
| 2 | DR 24-hour obligation with ~$2,300/MWh penalties on a 4 h battery | AI event-duration forecasting plus co-dispatch of host flexible load (HVAC, refrigeration, process) to stretch effective duration | Nominate 0.95 instead of 0.75-0.85 MW: +$10-20k/MW-yr | Plausible. Needs host load-control rights in the lease. |
| 3 | Missing the 1CP/5CP hours (the NSPL/PLC value depends on hitting them) | AI peak-hour prediction on PJM load, weather and zonal data; a 4 h battery covers multi-hour windows on several candidate days | Hit rate ~80% → ~95%: +$10-15k/MW-yr in PSEG | Yes. This is where AI matters most. |
| 4 | Soft costs and origination (what sank Stem/AMS-era fleets) | AI proposals from tariffs and interval data; automated NFPA 855 / authority-having-jurisdiction packets; broker channel | $0.30M → $0.12M/MW: **+2.4-3.2 pts unlevered** | Yes, but the CAC baseline is unsourced. |
| 5 | Capacity price after May 2030 | Sign a 10-15-yr RBP or bilateral contract first, then build. AI originates 15-yr host leases at a pace aggregators cannot match. | A 15-yr award at $450 flat lifts a generic site from 3.5% to 10.6% | Depends on the RBP surviving FERC and on price. Not AI-solvable. |
| 6 | Competitors with balance sheets (Voltus+Brightfield, Calibrant/Macquarie, Base) | Speed and cost of origination; zone focus (PSEG) | Only a cost edge, ~3 pts | Weak. D = 3. |
| 7 | Regulatory response to tag-shaving: the NITS revenue requirement is fixed, so shaving shifts cost to others and the BPU or utility can change the allocation | None. This is a political risk. | — | Real risk for the PSEG thesis at scale. |

## 7. Cheapest feasibility test (6-8 weeks, ~$40-70k)

1. **PSEG and AEP host funnel.**
   - Get 15-minute interval data (Green Button or broker-supplied) for 30-50 LPL/GT hosts ≥1 MW.
   - Run the AI sizing and 1CP/5CP model.
   - Produce 30 proposals and seek 15-yr site-lease letters of intent (LOIs).
   - **Kill if** fewer than 3 LOIs, or hosts demand more than 60% of the savings.
2. **Hardware quotes.** Get 3 FEOC-compliant integrator quotes for 1 MW / 3.5-4 MWh delivered, installed and interconnected in NJ.
   - **Kill if** above $375/kWh all-in.
3. **Offtake price discovery.** Talk to 3 data-centre LSEs or hyperscaler energy teams, CRA bilateral matching, and Voltus/CPower about the price for 7-15-yr BTM DR capacity in the PSEG/AEP zones.
   - **Kill if** no indicative bid ≥$275/MW-day for ≥7 yrs.
4. **Regulatory check.** Have counsel confirm how PSEG and AEP Ohio pass through NSPL/PLC charges for CIEP and large customers, the GSESP Phase 2 $/kW value, and the revised RBP filing (~29 Oct) on BTM/DR gating.

**Pass on all four, and the idea is 19/25 in a PSEG-first form.**

## 8. Rescore

| Leg | v5 | Now | Why |
|---|---|---|---|
| N (numbers close) | 4 | **3** | Generic PJM: 3.5-5% unlevered (fails). PSEG: 12%. Closes only by zone and only with long offtake. |
| T (time) | 4 | **4** | First revenue in 12-18 months; $100M by year 6-7 is tight but possible |
| C (ceiling) | 4 | **4** (3.5) | $4-5B base; $10B needs retail supply plus NY/NE |
| A (AI answers killers) | 4 | **3** | AI is worth ~+3 pts and fixes origination and peak-hour hit rate. The binding killers (cell cost, post-2030 price, tariff politics) are not AI-addressable. |
| D (defensibility) | 4 | **3** | Voltus (Google, Brightfield, $225M), Calibrant (Macquarie), Base ($13B) are all here. The 15-yr host leases are a real edge only in the RBP. |
| **Total** | 20 | **17/25: FAIL** | A narrowed "PSEG/AEP tag-shaving + 15-yr DR offtake + host retail supply" variant scores 19 (N 4, T 4, C 4, A 4, D 3) **if** the Section 7 test passes. |
