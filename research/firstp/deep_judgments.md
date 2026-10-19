# Adversarial deep check: unenforced commercial judgments, ML picks debtors with reachable assets (2026-10-19)

## Verdict
**15/25 after the check, down from 17. It fails the v4 bar (17+). The shape is real but small: it is a specialty-finance fund, not a venture-scale company.**

Score: **S1 3, S2 3, S3 3, S4 3, S5 3 = 15.** No leg is at 0-1, so the idea is not dead. It drops below the bar on three things:
1. **Adverse selection at the cheap price.** Judgments sold below 5c are the ones the holder already gave up on, and large holders (banks, MCA funders, debt buyers) usually ran a LexisNexis/TLO asset search before giving up. The real "seller can't read the data" pool is small creditors (contractors, suppliers, landlords) who never searched. S1 4 -> 3.
2. **Net step-up is about 2-3x, not 4-6x.** Gross recovery of 20-30% of face against a 3-5c price looks like 4-6x. After contingency counsel (33-50%), $2-5k of enforcement cost per file, 1-3 years of time and a long tail of zeros, it is about 2-3x. Statutory post-judgment interest (NY 9%, CA 10%) helps. S2 stays at 3 only because the high-confidence tail (asset located) resells at 50-73c.
3. **Size.** I found no published estimate of the commercial pool. My estimate from what is published (below) is roughly $3-10B of new unpaid commercial face value a year. At 3-5c that supports $100-500M a year of purchases if you bought *everything*, and a realistic share is a $20-100M/yr fund. That is a good boutique, not a path to a large company unless it ladders into the consumer pool. That pool is held by Encore/PRA and is heavily regulated.

The ML leg (judgement) holds at 3. The problem is prospectivity-like and has real labels (recorded satisfactions). But the strongest asset signals (bank accounts, receivables, wages) are not public. Post-judgment discovery is the actual "assay", and a simple rule baseline ("owns unencumbered real property and the entity is still active") may capture most of the lift.

**Cheapest test (Section 6):** about $3-5k and 3-4 weeks, scoring around 500 Florida commercial judgments recorded in 2016-18 against later recorded satisfactions. Prior on a clear pass: about 30%.

## 1. Pool size (no published commercial estimate exists)
| Datum | Value | Source |
|---|---|---|
| State incoming contract cases (39 states, 2022) | 3.6M. This includes debt collection, landlord/tenant and foreclosure, so it is overwhelmingly consumer | [NCSC CSP 2022 highlights](https://ncfsc-web.squiz.cloud/__data/assets/pdf_file/0026/97514/2022-Caseload-Highlights-Trial.pdf), [NCSC trends](https://www.ncsc.org/newsroom/at-the-center/2024/court-statistics-project-releases-trial-court-caseload-trends) |
| Small claims (41 states, 2022) | 2.2M incoming | same |
| Federal contract filings | 8,944 in 2022, the decade low; about 10k in 2023 | [Lex Machina 2023 report](https://www.lexisnexis.com/community/pressroom/b/news/posts/lex-machina-releases-2023-contracts-commercial-litigation-report) |
| Federal commercial contract damages | $6.3B in 1,990 commercial cases, 2020-22 (about $2B/yr). Over $13B in 2021-23 under a broader scope. Mostly large solvent defendants; 31-32% of those appealed were reversed | same; [2024 report](https://legal.lexisnexis.com/2024-Contract-Lit-Report) |
| Utah, all judgments 2013-20 | 385k judgments, $2B face; fewer than half paid in full by 2022 (consumer-dominated) | [Pew 2022](https://www.pew.org/en/research-and-analysis/articles/2022/04/20/utah-is-using-data-to-drive-debt-litigation-reform) |
| "80% of judgments uncollected", "$1B/yr uncollected" | Industry marketing with no primary source. Do not use | [insideARM](https://www.insidearm.com/news/00012215-an-estimated-1-billion-worth-of-court-awa/), [ABA Journal voice](https://www.abajournal.com/voice/article/why-do-80-of-judgments-remain-uncollected) |
| DOJ $97B unpaid federal judgments | Government debts (restitution, fines). Not purchasable and mostly asset-less | [Senate PSI](https://www.hsgac.senate.gov/?p=107550) |
| Large-claimant recovery | Only 2% of 350 senior in-house lawyers recover 100% of judgments/awards (vendor survey) | [Burford research](https://www.burfordcapital.com/media-room/media-room-container/new-research-how-businesses-extract-more-value-from-claims-judgments-and-unenforced-awards/) |

**My estimate (labelled as such):**
- Business-v-business is perhaps 3-8% of about 4.5M national contract filings, giving 150-350k cases a year.
- About 50-60% of these end in a judgment, many by default, giving 100-200k commercial judgments a year.
- Median face is likely $15-50k; federal and large-case judgments add about $2B.
- That gives about $3-10B of face a year, with perhaps half to two-thirds never paid.
- Judgments live 10-20 years and are renewable, so the unpaid stock could be $30-100B of face.
- The stock is dominated by dissolved LLCs and judgment-proof debtors, much like the DOJ book.
- A distinct sub-pool worth naming: merchant-cash-advance judgments against small businesses *plus personal guarantors*. The guarantor is often the collectable party. But MCA funders are sophisticated holders, so their files are adversely selected.

## 2. Economics
- **Price paid.**
  - One recovery firm states its target as "below $.05 on the dollar, recover 20-30% of face" ([newswire](https://www.newswire.com/news/judgment-recovery-services-texas-who-buys-judgments-69396)).
  - Forum and anecdotal prices run 2.5-3.5c for old uncollected judgments and 10-15c otherwise, higher when real estate backs the judgment ([CRE forum](https://forum.creonline.com/t/judgments-posted-by-paul/138241), [ibiblio](https://ibiblio.org/archives-archivists/msg18186.html)).
  - Most "buyers" actually pay "future pay" (a contingent share), not cash. Cash buyers are few (same newswire). That is good for S1: there is little competition for cash.
  - Prior slice B work: a judgment with assets already located trades at 50-73c, against 5.6c for a junk portfolio.
- **Collection and cost.**
  - Asset searches plus supplementary proceedings add $2-5k per moderate judgment. Costs can exceed the judgment when the debtor is judgment-proof ([Daeryun/NY](https://www.daeryunlaw.com/ar/insights/enforcement-cost-procedures-in-new-york)).
  - Agencies keep 20-40% and attorney contingency runs 33-50%. Getting to judgment takes 4-20 months ([Kaplan](https://www.kaplancollectionagency.com/collection-litigation-information/)).
  - Holders who do enforce net 40-60% of face (vendor claims).
  - Net to a 4c buyer: with roughly 25% of the book paying 60% of face, less 40% fees and $3k cost per file, a $40k-average book returns about 2-3x over 2-3 years. That is attractive for a fund, but it is not a 10x proof step.
- **Legal limits.**
  - **NY Judiciary Law 489** makes buying claims or judgments *for the purpose of* suing on them a misdemeanor. The safe harbor applies only to an aggregate purchase price of $500k or more *actually paid* ([Justinian v WestLB, NY Ct App 2016](https://nycourts.gov/REPORTER/3dseries/2016/2016_07047.htm)).
  - Espadarte (2020) says buying distressed debt to collect it is not champerty, because "the" purpose and "a" purpose differ ([Schlam Stone](https://www.schlamstone.com/blogs/commercial/2020-06-10-buying-distressed-debt-to-collect-on-it-not-champerty)).
  - Most other states have abolished or narrowed champerty (an advocacy claim of 46 states, 2004).
  - **Licensing:** about 34 states license collection agencies ([MS Law](https://www.mslaw.com/mslaw-blog/collection-agency-licensing-and-exemptions)). Buyers of *consumer* debt are increasingly held to be agencies even when they collect through counsel: WA AG suits ([Orrick](https://infobytes.orrick.com/2018-10-09/washington-state-attorney-general-says-debt-buyers-are-collection-agencies-files-lawsuit-operating-without-license/)), Arkansas Supreme Court, Illinois appellate court 2026 ([accountsrecovery](https://www.accountsrecovery.net/2026/08/03/ill-appeals-court-rules-buying-defaulted-mortgage-notes-requires-collection-agency-license/)).
  - Commercial-only books avoid FDCPA and most consumer licensing, but not every state's agency licence. Budget per-state counsel.
  - **Assignment mechanics:** the assignment must be filed of record in the court to enforce in the buyer's name. Execution formalities vary by state ([Robins Kaplan](https://www.robinskaplan.com/-/media/pdfs/how-hedge-fund-managers-can-address-common-issues-and-risks.pdf)).
- **Structural drag specific to commercial debtors.**
  - A judgment against an LLC does not reach the owners without alter-ego, veil-piercing or fraudulent-transfer litigation. That is costly, and it is exactly where the money usually went.
  - Operating businesses' receivables and inventory usually sit under a prior UCC-1 blanket lien (bank or MCA funder), so the judgment creditor is junior. UCC data mostly tells you who is *ahead* of you.
  - Civil judgments left the big-3 credit reports in 2017 (NCAP; [CFPB](https://files.consumerfinance.gov/f/documents/cfpb_quarterly-consumer-credit-trends_public-records-credit-scores-performance_2019-12.pdf)), which weakens the debtor's incentive to pay. LexisNexis still sells lien and judgment data.

## 3. Who holds the rung
| Tier | Players | Evidence |
|---|---|---|
| Top end (awards and judgments over $10M, sovereign) | Omni Bridgeway, Burford, Therium | Omni: 13 award/judgment investments in enforcement at about A$478M fair value (Mar 2026); recent completions at 5.7x MOIC ([ASX Jul 2026](https://announcements.asx.com.au/asxpdf/20260731/pdf/0727xbqh2lwgkp.pdf), [Omni enforcement](https://omnibridgeway.com/litigation-funding/judgment-enforcement)). Burford buys judgments outright and has in-house tracing ([Burford](https://www.burfordcapital.com/insights/insights-container/introduction-to-financed-enforcement)). Not interested in $20-500k |
| Consumer judgments (millions of files) | Encore/Midland, PRA, enforcement law firms | Encore legal collections about $401.6M in H1 2026; PRA legal spend about $376M in 2024, "optimizing post-judgment activities" ([Ginsburg blog on filings](https://ginsburglawgroup.com/2026/08/midland-credit-management-is-collecting-more-than-ever-what-encore-capital-groups-numbers-tell-us-about-its-debt-collection-strategy/)). Eltman Eltman & Cooper built a liquidation model on "hundreds of thousands of judgment accounts" ([insideARM](https://calvin.insidearm.com/news/00038649-eltman-eltman-cooper-announces-deep-look-)). **Analytics on judgment outcomes already exist here** |
| Mid/small commercial ($10k-$1M) | Fragmented: EnforcePay (FL, since 2012), Final Verdict Solutions ($25k minimum), JudgmentMarketplace listings, many "future pay" shops, contingency firms | [EnforcePay](https://www.enforcepay.com/), [Final Verdict](https://www.finalverdictsolutions.com/), [JudgmentMarketplace](https://smallbiztrends.com/judgment-marketplace/). None claims ML |
| Data/tools | LexisNexis (Accurint/TLO, RiskView liens and judgments), TransUnion TLOxp, Kroll tracing; AI tracing pitched at INSOL 2026 as analyst-assist | [Kroll INSOL 2026](https://www.kroll.com/en/publications/restructuring-advisory/reflecting-on-insol-london-2026-ai-asset-tracing-future-enforcement) |
| ML-native buyer | **None found.** SmallClaims (DK, EUR 2M seed) automates filing and enforcement; it does not buy | [ArcticStartup](https://arcticstartup.com/smallclaims-raises-e2-m-seed/) |

Read: the mid-market commercial rung is genuinely open and fragmented, which is good for S1/S5. It is open partly because it is small and labour-heavy.

## 4. ML plausibility (judgement, scored 3)
**For:**
- This is prospectivity-shaped: many weak signals across many sources, a low base rate, and a ranking target. Signals include:
  - entity status and age, officer overlap with *new* entities (phoenixing)
  - property owned and its equity
  - UCC filings (secured parties, renewals as a sign of activity)
  - other judgments and suits against the same debtor (being a payer elsewhere)
  - liens, permits and licences, web and hiring activity
  - guarantor identity
- Debt-recovery scoring is a mature analog (Eltman model; patents on NPV-of-debt models; a 2024 review of ML in collections).
- Labels exist in public records: recorded satisfactions and releases of judgment liens, and dockets showing garnishments.
- An expert shown a ranking that says "old LLC dissolved, but the same officers opened an LLC at the same address holding a fleet UCC" would say "I wouldn't have picked that, but it makes sense". That passes the v4 test.

**Against:**
- The decisive assets (bank balances, receivables, wages) are invisible until post-judgment discovery. The model ranks *where to spend $2-5k on discovery*. It does not know the answer.
- Satisfaction records are noisy: they are under-filed when settled privately, and a lien release is not proof of full payment.
- Commercial base rates are low and the samples are small per state.
- The baseline is strong: "owns unencumbered real property in-county" and "entity still active and filing UCCs" probably carry most of the signal.
- No real negative test is known, so the score stays at 3 rather than dropping. There is also no positive evidence for commercial judgments specifically.

## 5. Terranox-shape and scale
| Leg | Score | Why |
|---|---|---|
| S1 buy before it's known | 3 | Cheap, cash-light buys from small creditors who never searched. Professional sellers are adversely selected |
| S2 step-up | 3 | Proven-asset judgments resell at 50-73c (10-15x per hit); portfolio net about 2-3x after fees and cost |
| S3 ML plausibility | 3 | Prospectivity-like, with labels; key assets non-public; strong rule baseline |
| S4 discovery-heavy | 3 | Choosing is the main edge. Enforcement is routine legal labour done by contingency counsel, but it costs 33-50% of recoveries |
| S5 compounding edge | 3 | Your own discovery results ("what we found when we subpoenaed") are private, outcome-labelled data no public source has. Consumer incumbents have bigger judgment datasets, but not commercial asset-discovery outcomes |

**Terranox-shaped?** Partly. "Buy the right cheaply, learn, then prove" fits. But the "proof" is a lawsuit-like enforcement step, the upside is capped at face plus interest (no 1000x), and the asset does not reprice to others the way a proven deposit does. It is a collection business with a better picker.

**Venture-scale?** No as framed: it is a $20-100M/yr fund with 2-3x gross multiples. Possible ladders:
- (a) Sell the score and discovery data to Burford/Omni/agencies. This is a service, which breaks "own the asset".
- (b) Extend to consumer judgments. That is crowded and regulated.
- (c) Become the cash market-maker for small judgments (a JudgmentMarketplace that actually prices). That is plausibly the largest version, but still specialty finance.

## 6. Cheapest feasibility test (3-4 weeks, about $3-5k)
- **State: Florida.**
  - County official records index recorded certified judgments and recorded satisfactions. FS 55.141 requires the holder to file a satisfaction after payment (verify the current text).
  - Sunbiz holds judgment lien certificates on personal property ([DOS](https://dos.fl.gov/sunbiz/forms/judgment-lien/)) and full entity and officer history.
  - County property appraiser rolls are free in bulk. UCC filings are on the Florida Secured Transaction Registry.
- **Sample:** 500 judgments recorded 2016-2018 in 2-3 large counties (Miami-Dade, Hillsborough, Orange), defendant an entity or a guarantor of one, face $10k-$1M. Features are taken *as of the recording date*: property owned and equity, entity status and officer graph, UCC count and recency, prior and parallel suits, lien certificate filed.
- **Label:** satisfaction, release or garnishment-paid entry within 5 years. Hand-audit 50 for label noise.
- **Baselines:**
  - B0: the base rate.
  - B1: the rule "owns in-county real property with equity over 1.5x face, or the entity is active".
- **Model:** gradient boosting, plus an LLM pass to link officers to successor entities.
- **Pass:** top-decile satisfaction rate at least 2x B1's top decile and at least 25% absolute, stable across counties.
- **Also price the supply:** list 20 of the scored "dead" judgments on JudgmentMarketplace or approach the creditors directly, and record the asks. If creditors with high-score judgments ask more than 15c, S1 collapses.
- **Kill if:** the model does not beat B1, or satisfactions are too under-recorded to label (under 60% agreement on the audit).
