# Round 2: the "underwriter of drill holes" (an ML-selected drill-for-royalty fund)

Written 19 Oct 2026. Builds on lane E (business models), lane D (fewer holes) and lane F (public data and ML).
Tags: "(memory)" means not re-verified this session; "(estimate)" means my own arithmetic or judgement. Every other
number has a URL. Currency is given each time.

## 10-line summary
1. **The slot is already occupied by VerAI.** At Conquest's Belfast-TeckMag (Ontario, 2024) it took a 1.5% NSR for AI targets and a further 1.5% NSR for paying for the 3,549 m drill program. That is exactly "fund someone else's holes for a royalty, picked by ML". VerAI has 60+ projects and a US$24M Series B (Feb 2025) led by Insight Partners. Earth AI (up to 3% NSR for A$4.5M of drilling, Kincora/Legacy) and Lithosquare (2% NSR plus ~50% for €0.5-1.4M with Aterian; US$25M seed, May 2026) run the same structure. GoldSpot ran it in 2019 with Triple Flag backing and was absorbed into ALS for ~C$24M.
2. **Cash buys pre-discovery royalties at roughly fair value, so cash alone earns no edge.** Pre-discovery Athabasca options routinely set the price of 1% NSR at C$1M (the buyback right). Other prices paid: Hayasa sold 1.25% for US$1M in 2025 to fund drilling; TerraX sold 1% to Osisko for C$1M in 2015. Information and targets buy royalties far more cheaply: 1% for C$5,000 (Ontario Exploration Corp), and VerAI's 1.5% for targets alone.
3. **After discovery the royalty is worth 100-300x as much.** Altius sold 1% of its Arthur (ex-Silicon) NSR, a royalty that started from project generation, to Franco-Nevada for US$250M plus US$25M contingent (2025). Triple Flag paid C$421M for Orogen, whose value was essentially a 1% NSR on the same project. In uranium the prices are much lower. A whole 16-royalty uranium book, including a 2% NSR on part of Shea Creek (~96 Mlb resource), changed hands at a US$15M valuation in 2026.
4. **Portfolio maths (estimate).** Assume C$2M buys a 2% NSR at the market rate, and a deposit's 2% NSR is worth C$19-40M when it is discovered (risked for the 45% of discoveries that become mines). Breakeven then needs a 5-11% chance per program that it becomes a deposit. Base greenfield rates are 1-3%. ML lift of 1.5-3x gives 1.5-9%, so the fund returns 0.1-1.8x money, and most of that range loses money. A positive expected value needs a 3% base rate, a 3x lift and the high-value case together, and even that is only ~12% IRR before fees.
5. **Step-outs (60-90% hit rates) do not rescue it.** They are drilled on known mineralisation, where sellers already price the royalty near NAV. ML has the least lift exactly where the base rate is high.
6. **Equity or carried interest beats an NSR by ~3-5x per dollar.** A 30% interest in a 100 Mlb deposit at C$9-12/lb in situ is worth ~C$90M, against ~C$20-40M for a 2% NSR. That is the earn-in model run by Cameco, Orano and Kinterra (US$565M+ fund), and it needs follow-on capital.
7. **Pool.** Grassroots spending was US$2.57B in 2025, a record-low 21% share (S&P), and junior budgets were US$4.39B. A fund taking 4% of grassroots deploys ~US$100M/yr. That is sizeable, but it is a fund, and the value comes from 2-5 rare hits a year that pay out 5-15 years later.
8. **ML is necessary but not sufficient, and the data does not exist.** Program-level labels (did this program lead to a deposit?) must be built by joining assessment PDFs (SMAD, ARIS, OAFD, WAMEX) to later NI 43-101 resources. Positives are scarce: Canada finds ~50 deposits a decade (MinEx), so there are perhaps a few hundred labelled wins in total. A 3x lift on that sample is unprovable for years.
9. **Rubric: 39/60.** It passes on #1 (the fund never drills), #3 (cheap pre-discovery royalties) and #5 (fund to generator to royalty major). It is weak on #2 (lift unproven, dataset unbuilt), #4 (the step-up is paid only at the resource stage) and #6 (generators stay small; Franco-Nevada's scale came from buying royalties, not creating them).
10. **Verdict: kill as a new company.** It is VerAI's live business model, and at market prices the cash-for-royalty leg has a negative expected value. The part worth keeping is royalties paid for with information (targets, base rates), which are 100-200x cheaper per point than royalties paid for with drilling cash. For Terranox that is a revenue line: sell SMAD-derived targets on ground it does not want, for 1-2% NSRs. Against the 3 Oct no-drilling rule: it never drills, so it sits inside the rule, but every dollar of return still depends on someone else's drill bit.

---

## 1. Who already does "pay for, or pick, someone else's holes for a royalty"

| Player | What it does | Scale / funding | Outcome so far | Source |
|---|---|---|---|---|
| **VerAI Discoveries** | AI targets on third-party ground for an NSR, plus the option to fund the drilling for more NSR. Conquest: 1.5% NSR for targets (Apr 2024) and a further 1.5% NSR for funding a 3,549 m / 9-hole program (Sep-Dec 2024). Also earn-in JVs on staked ground | US$24M Series B first close (Feb 2025, Insight Partners); 60+ projects; "multiple royalties across North and South America" | Conquest: "3 of 4 AI targets intersected a potential mineralized system". Best intercept 0.83% Cu over 0.5 m. 2 of 9 holes missed the target horizon. No deposit yet | https://www.newsfilecorp.com/release/240334/Conquest-Drill-Testing-of-VerAI-AIgenerated-Targets-Identifies-Potential-VMS-System-at-Its-BelfastTeckMag-Project ; https://www.insightpartners.com/ideas/verai-discoveries-secures-24-million-in-series-b-funding-led-by-insight-partners-to-grow-its-global-asset-portfolio-of-ai-based-mineral-discoveries/ |
| **Earth AI** | Co-funds or performs drilling on others' tenure for a royalty or earn-in. Kincora alliance: up to A$4.5M over 2 years for up to 3% NSR, conditional on ≥1,500 m of diamond drilling and a "qualifying discovery". Legacy/Fontenoy: 80% or up to 3% NSR | US$20M Series B (Jan 2025) | Mineralised intercepts claimed; "75% discovery rate" is self-defined. No sale of a proven project found | https://mma.prnewswire.com/media/1915072/Kincora_Copper_Limited_Alliance_with_Artificial_Intelligence_Exp.pdf?p=pdf ; https://www.mining-technology.com/news/earth-ai-20m-ai-driven-mineral-exploration-drilling/ |
| **Lithosquare** (Paris) | AI targets plus full funding of the first program for a 2% NSR and just under 50% of the assets (Aterian, 8-9 projects, Morocco/Botswana; €0.5M first, up to €1.4M; another version is €1.0M for 15% + 0.5% NSR) | US$25M (or €22M) seed, May 2026 (World Fund, Kindred) | Too early | https://www.omnescapital.com/press-release/lithosquare-raises-25m-to-expand-and-break-critical-minerals-bottleneck-with-ai-powered-geology-platform ; https://www.ajbell.co.uk/news/articles/aterian-enters-ai-led-exploration-pact-lithosquare ; https://joshthompson.co.uk/investing/aterian-completes-lithosquare-jv-exploration-funding-drilling-campaigns/ |
| **Geomorphic AI** | Generates targets for juniors for a 0.5% NSR plus a US$5,000 success fee per property acquired (Latin Metals, Argentina) | Endeavour Financial strategic investment (Jul 2026) | Too early | https://www.newsfilecorp.com/release/312089 |
| **GoldSpot Discoveries** (the historical precedent) | ML targeting services paid partly in royalties. Triple Flag paid C$100k plus ~C$2.9M of equity (Jan 2019) for a right of first refusal over 50% of all royalties GoldSpot generates | TSXV-listed | Tech and consulting arm sold to ALS for ~C$24M (Dec 2022). I found no royalty from the model that became a mine | https://www.sec.gov/Archives/edgar/data/1829726/000110465922092225/tm2220483d2_ex4-1.htm ; https://www.alsglobal.com/fr/News-and-publications/2022/12/ALS-acquires-the-ExplorTech-Division-of-Earthlabs-Inc |
| **Orogen Royalties** (post-Triple Flag) | Generator: partners pay for drilling, Orogen keeps NSRs. 2026: 14 partner-funded programs, >69,000 m. Received C$1.72M from sales and partner payments year to date | Small cap; a March 2026 placement did not proceed | The earlier Orogen sold for C$421M on the back of one 1% NSR (Silicon/Merlin) | https://www.newswire.com/news/orogen-royalties-announces-project-partner-and-royalty-update ; https://www.miningweekly.com/article/triple-flag-to-acquire-orogen-royalties-for-c421m-in-expanded-silicon-gold-deal-2025-04-23 |
| **EMX Royalty** | Generator plus royalty buyer. In 2020: C$16.4M spent on royalty generation, C$8.0M recovered from partners, >C$13.5M of partner-funded programs | US$443.5M at last trade before the Elemental Altus merger (Nov 2025) | Value is concentrated in Timok and Caserones, and Caserones was bought, not generated (memory). **No portfolio IRR is published.** I searched and found none | https://www.newsfilecorp.com/release/79016 ; https://stockanalysis.com/stocks/emx/ |
| **Altius Minerals** | Project generation plus a junior-equity book (C$49.3M at 31 Dec 2025). Cost base under C$15M in Orogen turned into C$92M+ | C$3.3B market cap, mostly bought royalties (memory) | Sold 1% of its 1.5% Arthur NSR for US$275M (250 + 25 contingent). That royalty started from generator ground (origin: memory) | https://www.nasdaq.com/press-release/altius-provides-3rd-quarter-2025-project-generation-update-2025-10-08 ; https://www.nasdaq.com/press-release/altius-provides-4th-quarter-2025-project-generation-update-2026-01-08 ; https://www.miningweekly.com/article/franco-nevada-buys-1-royalty-on-anglogolds-arthur-project-2025-07-28 |
| **Osisko "accelerator"** | Takes equity plus an NSR in juniors early (Barkerville: 35.2% plus a 2.25% NSR; Windfall). The CEO says Osisko creates royalties with internal expertise "instead of paying full price" | Osisko Gold Royalties is a large royalty company | It worked when Osisko picked camps it knew; the equity book adds market risk | https://www.cruxinvestor.com/posts/osisko-gold-royalties-or-best-royalty-company-in-the-world ; https://projects.gbreports.com/qubec-mining-2021/osisko-gold-royalties-interview |
| **Ontario Exploration Corp** (OPA, government-backed) | Buys a 1% royalty on grassroots prospector projects for C$5,000 each, to be self-sustaining from royalties | Northern Ontario Heritage Fund | No results found | search summary of https://northernminer.com/news/opa-helps-fund-grassroots-work/1000185618 (article paywalled; the C$5,000 figure is from the search snippet) |
| **South Africa Junior Mining Exploration Fund** | Non-repayable grants that convert to equity or a profit share on discovery. R1bn after a producer added R600m (Feb 2026) | State plus producer | Early | https://www.engineeringnews.co.za/article/junior-mining-exploration-fund-delivering-meaningful-progress-2025-10-31 |
| **Kinterra Capital** | Private equity for critical minerals, taking control or large minority stakes (Maronan ~20% pre-PFS; New World 12%; Pumpkin Hollow). Equity, not royalties | US$565M debut fund (2023); later reports cite ~US$1.5B | Mostly development stage, not hole-by-hole underwriting | https://electricautonomy.ca/2023/12/21/kinterra-battery-fund-critical-minerals-projects/ ; https://dealroom.co/news/132821-maronan-metals-lands-22m-from-kinterra-capital-to-fast-track-drilling/ |
| **Ridgeline** (two companies) | Ridgeline Minerals (TSXV: RDG) is a hybrid explorer that uses partner capital (South32 US$20M earn-ins). Ridgeline Royalties is a private battery-metals royalty and stream financier aimed at producers (first deal: James Bay lithium). **Neither underwrites drill holes** | ~C$33M cash after a 2025 Nevada Gold Mines sale (RDG) | Not applicable | https://www.cruxinvestor.com/posts/ridgeline-minerals-strategic-partnerships-continuous-exploration-carried-interests ; https://finance.yahoo.com/news/ridgeline-royalties-completes-first-transaction-210000096.html |
| **The Metals Royalty Co.** (Nasdaq) | Holds 2% of the NORI nodule royalty and a Mesabi pellet royalty; no revenue. **Not exploration-stage underwriting** | Market cap ~US$167-327M (conflicting sources) | Not applicable | https://quartr.com/companies/the-metals-royalty-company-inc_23076 |
| **Drill-for-equity contractors** (Topdrill, Geodrill, etc.) | Take 25-55% of the invoice in shares | A$0.5-4M deals | Lane E: break-even needs a ~7% hit rate, with adverse selection | lane_E_business_models.md §1 |
| **Sprott / Franco / Triple Flag / URC** | Buy royalties mostly at resource stage or later. Franco's 2025 early-stage deals were few and small (Yilgarn Star 1% for US$4.7M on a past producer) | Large royalty companies | They are the exit buyer, not the underwriter | https://www.sec.gov/Archives/edgar/data/1456346/000110465926032133/fnv-20251231xex99d3.htm |

**Read.** The exact model in the question, "pick third-party drill programs with ML and pay for them in exchange for an NSR", is VerAI's live business. Earth AI and Lithosquare run variants. GoldSpot did it with a royalty major behind it and ended as a C$24M services sale. No one runs it as a pure diversified book of "hundreds of programs". All of them bundle targeting with funding, because the targeting is what earns the cheap royalty (section 2).

## 2. What pre-discovery royalties actually cost

| Deal | Stage | What was paid | Implied C$ per 1% NSR | Source |
|---|---|---|---|---|
| Ontario Exploration Corp | Grassroots prospector claims | C$5,000 for 1% | ~C$5k | search summary of northernminer.com/news/opa-helps-fund-grassroots-work/1000185618 |
| VerAI / Conquest | Targets only (no cash) | 1.5% NSR for AI targets | targets only, no cash | newsfilecorp 240334 |
| Geomorphic / Latin Metals | Targets only | 0.5% NSR plus US$5k success fee | targets only, no cash | newsfilecorp 312089 |
| VerAI / Conquest | Drill funding | further 1.5% for a 3,549 m program; cost not disclosed, ~C$1.0-1.5M at ~C$300-400/m in Ontario (estimate) | ~C$0.7-1.0M (estimate) | newsfilecorp 240334 |
| Athabasca option deals (North Shore/West Bear 2025, Refined/Searchlight, Zadar/Canterra, Lakeland/Basin) | Grassroots to early drilled | Optionor keeps 2% NSR; buyer can buy back 1% for C$1M | C$1M (seller's ceiling price) | https://www.barchart.com/story/news/35631331/north-shore-makes-final-option-payment-and-completes-earn-in-for-west-bear-property ; https://www.mining-technology.com/news/refined-energy-secures-options/ |
| Stallion / Glorious Creation (E. Athabasca) | Grassroots | 3% NSR kept; half (1.5%) buyable for C$2.25M | C$1.5M | https://mugglehead.com/stallion-uranium-sells-non-core-assets-in-eastern-athabasca-basin-retains-net-smelter-royalty/ |
| Foremost / Strider option | Early | 1% of NSR buyable for C$1.5M | C$1.5M | https://www.sec.gov/Archives/edgar/data/1935418/000117184325007296/exh_991.htm |
| Hayasa / EMX + Franco-Nevada (Urasar, Armenia, Jan 2025) | Drilled, pre-resource; proceeds "ensure a robust 2025 drilling program" | US$1M for 1.25% | ~US$0.8M (~C$1.1M) | https://api.newsfilecorp.com/redirect/zEo14IVpjX |
| TerraX / Osisko (Yellowknife City Gold, 2015) | Drilled, pre-resource | C$1M for an additional 1% (plus C$2.5M equity) | C$1M | https://miningnewsnorth.com/story/2015/06/28/northern-neighbors/terrax-raises-unprecedented-funds-for-ycg/3244.html |
| Landore / GT1 (Root Lake, 2022) | Historic resource | C$3M for 3% | C$1M | https://www.sharesmagazine.co.uk/news/market/LSE20221031070007_4561029/completion-of-disposal-of-nsr-at-root-lake |
| Vox / individual prospector | Mixed: one near construction decision, one pre-maiden resource | US$1.43M for three royalties | ~US$0.5M per royalty | https://www.mining-journal.com/precious-metals/news/4069367/vox-buys-royalties-individual-prospector (403 this session; figure from search snippet) |
| Royal Uranium book → Fusion Fuel (Jul 2026) | 16 uranium royalties incl. 2% NSR on two Shea Creek claims (Orano/UEC; 67.6 Mlb indicated + 28.1 Mlb inferred project-wide) | US$15M valuation for the whole book, paid in shares | ~US$0.5-1M per royalty (estimate) | https://energydigital.com/globenewswire/3331282 ; https://finviz.com/news/340654/ |
| URC / Millennium + Cree Ext. (Oct 2024) | Advanced (Cameco) | C$6M for a 10% NPI on ~20.7% of the projects | n/a (NPI) | https://www.uraniumroyalty.com/news/uranium-royalty-acquires-existing-royalty-on-camecos-advanced-stage-millennium-and-cree-extension-uranium-projects |
| **Post-discovery comparators** | | | | |
| Altius → Franco-Nevada, Arthur (2025) | Large resource, pre-feasibility | US$250M + US$25M for 1% | ~C$375M | https://www.miningweekly.com/article/franco-nevada-buys-1-royalty-on-anglogolds-arthur-project-2025-07-28 |
| Triple Flag → Orogen (2025) | Same project, 1% NSR | C$421M for the company | ~C$343M net of Spinco | https://www.miningweekly.com/article/triple-flag-to-acquire-orogen-royalties-for-c421m-in-expanded-silicon-gold-deal-2025-04-23 |

**What the table says.**
- **Cash buys 1% pre-discovery for about C$1M,** almost regardless of jurisdiction (Armenia, Yukon, Ontario, Athabasca). It is a market clearing price, and the C$1M buyback is set by the seller as a ceiling, so a buyer of new royalties will not get it much cheaper for cash.
- **Information buys 1% for close to nothing** (C$5k, or targets only). The arbitrage is in selling knowledge, not in writing cheques.
- **Uranium royalties trade at a deep discount to gold.** A 16-royalty uranium book including a Shea Creek 2% was valued at US$15M, against US$275M for 1% of one Nevada gold project. Uranium deposits are worth much less per deposit to a royalty holder: low price per tonne of rock, long permitting, and partial-claim coverage (Shea Creek's royalty covers only two claims).

## 3. What a royalty is worth if the hole finds a deposit (estimate)

Assumptions: 100 Mlb U3O8 mined at 97% recovery, US$80/lb, 3% NSR deductions, a 10-year mine life starting 8-12 years after discovery.

- **Undiscounted value of a 1% NSR:** ~US$75M.
- **PV at discovery of a 1% NSR (my calculation):**

| Discount rate | Production starts year 8 | Production starts year 12 |
|---|---|---|
| 5% | US$41M | US$34M |
| 8% | US$30M | US$22M |
| 10% | US$24M | US$16M |

- **Risk adjustment.** MinEx/Schodde found that only 45% of 3,500 significant discoveries (1950-2013) became mines (https://canadianminingjournal.com/news/pdac-factors-that-affect-whether-a-discovery-turns-into-a-mine). On that basis a risked 1% on a 100 Mlb discovery is worth ~US$7-19M, and a risked **2% is worth ~US$15-37M (C$20-50M)**. This matches lane E's US$15-40M.
- **Deposit size.** Most Athabasca deposits are well under 100 Mlb (memory). A plausible average deposit (~60 Mlb, estimate) cuts this by ~40%. In the portfolio maths below I use **C$19M (base), C$30M and C$40M (optimistic)** for a 2% NSR at the point of discovery.
- **Market check.** The Royal Uranium book (US$15M including a 2% NSR on part of a ~96 Mlb resource) says the market prices discovered-but-undeveloped uranium royalties well below the DCF above, because of coverage, the operator's timeline (Shea Creek has been idle for years) and illiquidity.

## 4. Portfolio maths for the underwriter (estimate)

Structure: the fund pays C$2M for one program (the C$1-5M range in the brief) and receives a 2% NSR, which is the market price from section 2. p is the probability that the program leads to a deposit. The fund sells or marks the royalty at about year 5.

| 2% NSR value at discovery | Breakeven p | Base 1%, ML lift 1x / 3x | Base 2%, lift 1x / 2x / 3x | Base 3%, lift 1x / 2x / 3x |
|---|---|---|---|---|
| C$19M | 10.8% | 0.09x / 0.28x | 0.19x / 0.37x / 0.56x | 0.28x / 0.56x / 0.84x |
| C$30M | 6.7% | 0.15x / 0.45x | 0.30x / 0.60x / 0.90x | 0.45x / 0.90x / 1.35x |
| C$40M | 5.0% | 0.20x / 0.60x | 0.40x / 0.80x / 1.20x | 0.60x / 1.20x / **1.80x (~12% 5-yr IRR)** |

Values are the expected money multiple on capital deployed.

**Diversification works, but only once the book is large.** With a 5% hit rate, a 20-program book has a 36% chance of zero hits, and a 100-program book has a 0.6% chance. "Hundreds of juniors" is needed for the law of large numbers. At C$2M a program, that means C$200M+ a year.

**What it would take to work:**
1. **Pay with information, not just cash.** Pricing at VerAI's 3% for targets plus funding, rather than 2% for cash, adds 50% to every cell above. Royalties paid for in targets are nearly free (section 2).
2. **Take a working interest, not an NSR.** A 30% interest in a 100 Mlb deposit at the observed C$9-12/lb in-situ buyer prices is worth ~C$90M (estimate, using lane E's Paladin/PLS and Rio/Hathor comparables). That is 3-5x a 2% NSR for similar cash. This is the earn-in model: Cameco paid C$22M for 70% of Uravan's ground, and Foremost spent C$20M+ for 70% from Denison. But an earn-in needs follow-on capital and becomes a JV operator, which turns it back into an explorer.
3. **Fund the most expensive greenfield programs.** ML lift is largest where the base rate is lowest, and those are the programs juniors find hardest to fund.

**Step-outs.** A 60-90% hit rate on step-out holes sounds attractive. But step-outs are drilled on known mineralisation, so the market has already priced in the expected result. A seller who has a hole at 10% eU3O8 will not sell 1% for C$1M. The edge collapses to near zero, and ML has little to add to an already-high base rate.

**Adverse selection, Canada-specific.** In Saskatchewan, flow-through money with stacked METC/SMETC credits costs investors roughly C$0.2-0.25 per C$1 after tax (lane E §5), so juniors raise FT equity at a premium. Royalty money is the more expensive capital: it encumbers the asset forever, and majors discount royalty-stacked ground (memory). So the juniors who sell royalties for drilling cash tend to be the ones that cannot raise FT. Royalties also reduce the takeover value, and a 3%+ stack is a known deal-killer (memory).

## 5. Pool and ceiling

- **Grassroots spending:** US$2.57B in 2025, down 8%, a record-low 21% share of US$12.4B of global non-ferrous exploration. Minesite exploration was a record 45% (https://www.businessday.co.za/economy/2026-04-09-gold-drives-mining-exploration-as-global-budgets-fall-for-third-year ; https://www.spglobal.com/content/dam/spglobal/mi/en/documents/general/World-exploration-trends-2026.pdf). This is slightly above the brief's US$1.5-2B, which matches the US$2.79B for 2024 (https://mining.com/?p=1167406).
- **Junior budgets:** US$4.39B in 2025, down 13% (BusinessDay, citing S&P).
- **A fund taking 4%** of grassroots spending deploys ~US$100M/yr into ~70 programs. At a 5% hit rate and C$30M per hit, that books ~3.5 deposits worth ~C$105M a year against ~C$138M deployed. Marginal at best, before G&A and the cost of ML and data.
- **Ceiling reference points:**
  - Franco-Nevada is a ~US$35-45B company (memory), but its value comes from buying producing royalties, not creating exploration royalties.
  - The generators that create royalties: Orogen (C$421M exit), EMX (US$444M), Altius (C$3.3B, mostly bought royalties), Mirasol (C$27M), Riverside (C$34M) (lane E).
  - The pattern is a power law. One giant (Silicon, Timok) makes the company, and the rest of the book is noise.
  - A diversified underwriter improves the odds of hitting a giant only to the extent the ML lift is real.
- **Uranium specifically is the wrong place to start.** The Athabasca has ~60 junior explorers (lane F, repo memory) and perhaps C$100-300M a year of basin drilling (lane D, estimate). Uranium royalties also price far below gold ones (section 2). Gold and copper carry the royalty market.

## 6. Does ML make this solvable at all?

**What the selection model needs.** Labelled programs: features at funding time (geology, geophysics, prior holes, target type, depth, team, cash), joined to an outcome 3-10 years later (abandoned, intercept, resource, mine).

**What exists:**
- Hole-level structured data is thin. BC's ARIS has 41,500 reports but only 2,034 holes structured (~0.5%). Ontario's ODHD has 164k collars with flags. Saskatchewan's compilation has 20,145 collars and depth picks with no lithology or assays. WAMEX is structured only from 2007 (lane F, BCGS GF2026-11).
- **Program-to-outcome labels exist nowhere.** I found no one who publishes hole-level or program-level base rates. MinEx publishes only aggregate discovery counts (lane F, W6).
- Building the labels means two jobs: (a) LLM and vision extraction of assessment PDFs (needed: LLMs reach ~70% accuracy on image scans, arXiv 2405.05438, via lane F), and (b) entity resolution from programs to later NI 43-101 resources on SEDAR. Both are doable and both are ML-load-bearing. **This passes rubric #2 in form.**

**Sample-size problem.**
- Schodde counts ~50 deposits a decade in Canada (3 tier-1, 7 tier-2, 40 tier-3) (https://www.northernminer.com/news/minexs-schodde-canadian-explorers-still-have-their-mojo/1003528223/).
- Over 1970-2025 that is a few hundred positive labels across all commodities and geologies, set against tens of thousands of negative programs (estimate).
- Lift estimates on a few hundred positives have wide error bars. Validating a 3x lift out of sample takes a decade of real outcomes, because the label (deposit) lags the decision by 3-10 years.
- No AI explorer has published an audited lift (lane D). Investors in the fund would be buying an unproven claim.
- Part of any real lift will come from non-geological features (team, cash runway, follow-up discipline), which the public record captures poorly.

**Bottom line on ML.** ML is necessary to build the dataset, and the dataset is genuinely unbuilt. But the model it produces cannot show its lift quickly enough to raise a fund on it. The fund's economics need ~2-3x lift *and* better-than-market pricing. A model that delivers only 1.5x leaves the cash-for-royalty book losing money (section 4).

## 7. Relative to the 2026-10-03 no-drilling rule

- **It never drills, never owns rigs and never owns ground.** On the letter of the rule, it is allowed, like a generator.
- **Its returns are entirely a function of other people's drilling.** It is the purest form of "betting on drill holes", with no control over execution (hole abandonment, which lane F found in 1 of 3 holes at Cree East and 2 of 9 at Conquest).
- **The capital-light variant, targets for royalties, is the closest to the spirit of the rule.** It exchanges information for royalties and puts up no drilling cash.

## 8. Score on Dhruv's gold rubric (0-10 each)

| # | Criterion | Score | Why |
|---|---|---|---|
| 1 | Discovery is 80%+ of the work; the physical step is abstracted | 8 | The fund only selects. Juniors and contractors do all the physical work |
| 2 | Signal in public-but-illegible data; ML makes it solvable at all | 5 | The program-outcome base-rate dataset is genuinely unbuilt and ML-load-bearing, but the lift is unprovable for years and the positives number in the hundreds |
| 3 | Unproven right bought cheap | 8 | 1% NSR at C$1M pre-discovery, against US$275M post-discovery (gold). Cheaper still for targets (C$5k) |
| 4 | Capitalised buyer pays a step-up at once | 5 | Royalty majors (Franco, Triple Flag, URC) pay, but only at resource stage, 3-5+ years after the intercept, and uranium royalties fetch little (US$15M for 16) |
| 5 | Ladder | 7 | Targets for royalties → fund programs → earn-in interests → royalty company → own ground. Altius and Osisko walked versions of this |
| 6 | Ceiling | 6 | The royalty sector supports US$40B companies, but exploration-royalty creators sit at C$30M-C$3B and depend on one giant. At market pricing the cash leg has negative expected value |
| | **Total** | **39/60** | |

Base-rate lever: greenfield 1-3% × 1.5-3x ML = 1.5-9%. That passes Dhruv's "1.5-3x is accepted" bar on the lever. It fails on unit economics, because at market prices breakeven needs 5-11%.

## 9. Verdict and what to keep

- **Kill as a new standalone company.**
  - VerAI already runs the model (targets plus funding for NSR, 60+ projects, US$24M Series B), and Earth AI and Lithosquare run variants.
  - GoldSpot's earlier attempt, with Triple Flag behind it, ended as a ~C$24M services exit.
  - The cash-for-royalty leg is roughly fairly priced by the market (C$1M per 1%), so it needs a 5-11% per-program deposit rate against a 1-3% base.
  - In uranium the royalty prize per deposit is small.
- **Keep, as a Terranox revenue line:** "targets for royalties" on Athabasca ground Terranox does not want to hold. SMAD-derived targets can be sold to juniors for 1-2% NSRs plus a success fee (the Geomorphic and VerAI terms). Terranox would add cash only on its highest-conviction third-party targets, to take the extra point (the VerAI/Conquest structure). This costs almost nothing and builds a royalty book that a URC or royalty major can buy.
- **The dataset idea survives as infrastructure.** A program-to-outcome base-rate table (lane F's W6) is the asset that would make an underwriter possible later. It is worth building inside Terranox for its own decisions to stop or continue drilling first.

## Gaps
- No EMX or Altius portfolio IRR is published; I searched and found none. Altius gives only quarterly equity marks.
- VerAI's dollar cost of the Conquest program, and its full royalty count, are undisclosed.
- I could not read the Red Pine/Franco-Nevada 1.5% NSR price (paywall). The C$6.8M figure in one snippet is unverified.
- The Ontario Exploration Corp C$5k per 1% figure comes from a search snippet; the article is paywalled.
- I found no measured realised return on any diversified book of early-stage royalties.
