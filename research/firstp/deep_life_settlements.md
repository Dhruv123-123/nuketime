# Adversarial deep check: lapse-rescue life settlements (2026-10-19)

## Verdict
**13/25 after the check, down from 17. It fails v4 (two legs at 2, total under 17). It is a real, growing market, but it is a capital-and-origination business. It is not Terranox-shaped and it is a poor fit for venture money.**

Scores (v4 legs): **S1 3, S2 2, S3 3, S4 3, S5 2 = 13/25.**

Four things that the 17 depended on fail under checking.

1. **The "lapsing for nothing" pool is mostly policies that are worth nothing to a buyer either.**
   - Buyers only want insureds aged 65+ with face of $100k+, an impairment that shortens LE, and a UL or convertible-term contract.
   - Lapsing term policies are mostly unsellable once the conversion window closes.
   - Owners lapse largely *because* the premiums have become uneconomic, and the buyer inherits those premiums.
   - Conning already filters the pool to settle-able policies ($224B/yr gross potential), and only about $4-5B/yr of face actually trades. The gap is mainly an origination cost (finding and convincing seniors), not a mispricing a model can read.
2. **The buyer's step-up is a yield, not a revaluation.**
   - Purchase prices run about 15-20% of face. Premiums then roughly double the cost basis over the holding period.
   - Pricing discount rates are 10-22%, and realised returns have often come in well below priced IRRs.
   - That is about 1.5-2.5x on capital over 8-12 years, not 3x+.
3. **LE error is the industry's recurring killer, and ML does not fix the part that kills.**
   - The 2008-09 extensions, Life Partners and GWG all failed on *calibration drift and bias* (mortality improvement, optimistic LEs, discount-rate games), not on ranking.
   - Calibration feedback arrives a decade late, so any model, ML or not, learns slowly.
4. **The rung is held and the data moat is theirs.**
   - Coventry (13 years #1, about $1.6B face bought in 2025) and Abacus (public, $3.5B AUM, $544M raised in H1 2026) hold the rung.
   - The LE houses (ITM, AVS/21st, Fasano, LSI) sit on decades of LEs matched to deaths.
   - A new entrant's own maturities arrive at roughly 1-3% of the book a year, so S5 compounds slower than the incumbents' head start.

**What would revive it:** evidence that an ML LE model beats a VBT-plus-debits baseline on *calibration* (A/E near 100% by LE decile) on out-of-sample senior data, **and** an origination channel that buys below auction prices at scale. The cheap tests are in section 6.

## 1. Market size (face transacted, lapse pool, 2024-2026 trend)

| Measure | Figure | Source / caveat |
|---|---|---|
| New settlements, face/yr (Conning) | ~$4.6B/yr projected; 2024 study said ~$5B/yr; 2024 volume *fell* ("a pause") | [Conning 2025 study](https://www.conning.com/about-us/news/ir-pr---life-settlements-2025), [Conning 2024](https://conning.com/about-us/news/ir-pr---life-settlements-2024) |
| Historic face | $1.2B in 2011; after the 2008 LE extensions, face sold fell 46% to $7.0B | [ThinkAdvisor 2012](https://thinkadvisor.com/2012/11/16/conning-life-settlements-face-supply-and-demand-disparity), [ThinkAdvisor 2009](https://thinkadvisor.com/2009/10/19/the-life-settlement-business-after-the-storm-2) |
| LISA members, 2025 | 2,955 deals (+9.5%), $626.6M paid to sellers, avg $212,066 vs $24,360 surrender (~8.7x); 2021-25: $3.6B paid, ~15,000 policies | [beinsure](https://beinsure.com/news/life-settlement-payouts-reached-626mn/), [rethinking65](https://rethinking65.com/?p=31591), [insurance-forums](https://www.insurance-forums.com/life-insurance/life-settlements/life-settlements-net-9x-more-for-policyholders-than-surrenders-lisa/) |
| Coventry 2025 | >1,400 policies, ~$1.6B face, >$240M paid (self-reported league table) | [mychesco / Coventry PR](https://www.mychesco.com/a/news/regional/coventry-leads-life-settlement-market-in-2025-league-table-report/) |
| Abacus 2025 | 1,310 policies bought for $580.8M; ~1,059 traded (~$1.8B face) | [Coverager](https://coverager.com/abacus-posts-record-life-settlement-activity-in-2025/) (via slice B; page 403 today) |
| Gross market potential | $224B/yr of face owned by 65+ that lapses or surrenders and could qualify | [Conning 2025](https://go.conning.com/2025-Life-Settlements-Report-Highlights.html) |
| All-ages lapse pool | >33M policies/yr terminated early, $2.5T face (mostly term, mostly not settle-able) | [Braun, Cohen, Malloy, Xu draft](https://www.vwrm.rw.fau.de/files/2018/08/E1_1-Braun-Cohen-Malloy-Xu.pdf) |
| 2026 trend | Panel expects ~10% deal growth again; tertiary portfolio trading is active; Abacus AUM $50M to $3.5B in 3 yrs | [ELSA ILSF26](https://elsa-sls.org/wp-content/uploads/2026/06/ILSF-26-Summary.pdf), [Quartr ABX fireside](https://quartr.com/events/abacus-global-management-abx-fireside-chat_FGBVuKbe) |

**Read.**
- The investable flow is about **$4-5B of face a year**, which is roughly $0.6-1B paid to sellers.
- Coventry and Abacus together buy roughly $3B+ of face (the figures overlap with the tertiary market). So two firms take most of the flow.
- The $224B "potential" is the TAM that sales pitches quote. Converting it is a marketing-to-seniors problem, and Coventry has spent on TV for 20 years doing exactly that.
- The 2008 LISA "$112B/yr lapsed by seniors" figure is stale and comes from an interested party.

## 2. Economics (price, premiums, IRRs, blow-ups)

**Purchase price.**
- Coventry paid about $240M for about $1.6B of face, which is **~15% of face**.
- Conning's 2011 average was about 20% of face, against about 10% cash surrender ([FedWeek](https://www.fedweek.com/retirement-financial-planning/settling-up-4/)).
- Short-LE insureds go far higher, up to 60%. State floors apply: Oregon requires 85% for an LE under 6 months ([OAR 836-014-0270](https://oregon.public.law/rules/oar_836-014-0270)).

**Premiums carried.**
- An 80-year-old's UL cost of insurance commonly runs several % of face a year (memory, not sourced today).
- Over an 8-12 year LE, cumulative premiums are of the same order as the purchase price.
- The buyer also takes cost-of-insurance-increase risk, as seen in the Transamerica and Phoenix COI hikes and lawsuits (memory).

**Discount rate and returns.**
- Market discount rates fell from about 22% (2023) to about 10% (2026) as capital flowed in (slice B, France Epargne). Thinner spreads mean less room for LE error.
- AA-Partners: advertised IRRs and NAV curves "are not reliable measures" for investment decisions ([AAP white paper](https://www.aa-partners.ch/fileadmin/documents/White_Paper/Life_Settlement_Performance_V1.2.pdf)).
- SL Investment Management: assuming maturity at LE can inflate valuations by up to 40% ([Investment Week](https://www.investmentweek.co.uk/investment-week/news/1603746/life-settlement)).

**How LE errors blew things up.**
- **2008-09 extensions.** 21st Services revised its tables, and its new LEs ran 20-30% longer in many cases. The other LE providers followed. Funders re-priced, offers were withdrawn and portfolios were revalued ([SOA monograph, Granieri](https://soaconnect1.soa.org/493915/globalassets/assets/files/resources/essays-monographs/2011-living-to-100/mono-li11-4b-granieri.pdf), [ThinkAdvisor](https://thinkadvisor.com/2009/10/19/the-life-settlement-business-after-the-storm-2)). AVS/ITM lengthened LEs again around 2013-15 (memory; not verified today).
- **Life Partners Holdings.** The SEC alleged "systematically and materially underestimating" LEs from one physician with no actuarial training. Of 302 policies he priced in 2004-07, he predicted 157 would mature by end-2007; **7 did**. The company went bankrupt in 2015 after a $46M jury verdict ([Wikipedia summary](https://en.wikipedia.org/wiki/Life_Partners,_Inc.), [ThinkAdvisor SEC](https://thinkadvisor.com/2012/02/01/sec-brings-up-charges-on-life-partners-holdings), [Fifth Circuit](https://cite.case.law/f3d/926/103)).
- **GWG Holdings.** GWG sold $1.6B of L Bonds backed by settlements, defaulted in January 2022 and filed Chapter 11 in April 2022 ([InvestmentNews](https://www.investmentnews.com/gwg-holdings-files-for-bankruptcy-220355)).
  - Its FY2018 10-K took a charge for a change in LE methodology. SLCG estimates **$179M of mortality write-off, offset by an undisclosed discount-rate cut**, and notes that filings repeatedly showed "fewer death benefits and more premiums than expected" ([SLCG](https://www.slcg.com/files/blog/L_Bonds_Were_Always_Impaired_by_Craig_McCann_and_Regina_Meng.pdf); advocacy source).
  - The trustee later sold the residual portfolio interest for about $10M ([Banks Law](https://bankslawoffice.com/blog/gwg-l-bonds-value-in-september-2023-and-how-we-got-here/)).
  - Fraud and leverage were central, but LE optimism is what made the assets look covered.
- **Abacus 2025.** Morpheus Research alleged that Abacus used short LEs from **Lapetus**, an ML/facial-analytics LE vendor in which Abacus holds a stake, to inflate marks. The stock fell 20% in a day.
  - Abacus answered with a Lewis & Ellis revaluation ($449M vs $446M stated) and sued Coventry over the campaign ([GlobeNewswire](https://www.globenewswire.com/news-release/2025/06/10/3096617/0/en/Abacus-Refutes-Misleading-Balance-Sheet-Claims-With-Independent-Third-Party-Actuarial-Valuation.html), [Hagens Berman](https://www.newsfilecorp.com/release/259478/Abacus-Global-Management-Inc.-ABL-Shares-Tumble-Following-Second-Morpheus-Report-Hagens-Berman), [Coventry response](https://www.stocktitan.net/news/ABL/coventry-responds-to-baseless-lawsuit-by-abacus-global-management-zfeh5ttq25c5.html)).
  - **The market already treats "our proprietary ML LE is shorter" as a red flag.** That is directly hostile to an ML-native pitch.

**S2 = 2.** Seller gain over surrender is about 9x, but that gain goes to the seller. The buyer's money multiple on cost plus premiums is about 1.5-2.5x over about a decade, and the tail risk is longevity.

## 3. Who holds the rung
- **Coventry** (Coventry First / Coventry Direct / Life Equity): #1 for 13 years by its own league table, and runs the direct-to-consumer TV origination machine. It is large and private.
- **Abacus Global Management (ABX, formerly Abacus Life)**:
  - Q2 2026 revenue $73.0M (+30%); 2026 adjusted net income guide $100-106M.
  - Policy assets $383M against $330.6M debt.
  - First registered retail fund launched; tokenising in-force policies.
  - Owns or partners with an ML LE vendor (Lapetus) ([BusinessWire Q2 2026](https://secure.businesswire.com/news/home/20260806840808/en/Abacus-Global-Management-Inc.-Reports-Second-Quarter-2026-Results), [Webull transcript](https://www.webull.com/news/15740108878210048)).
- **Carlisle (Luxembourg funds), Vida Capital, Blackstone-backed and other institutional buyers.** No fresh 2025-26 volume data turned up. They act mainly as capital and tertiary buyers.
- **LE underwriters:** ITM TwentyFirst, AVS, Fasano, LSI, plus Lapetus (ML/facial). The Xu "Dating Death" study finds the four majors "rarely agree" and are biased by cohort ([EPFL](https://infoscience.epfl.ch/record/277819?ln=en)).
- **ML-flavoured entrants:**
  - Harbor Life Settlements: an ML pricing calculator that "reverse-engineers" investor heuristics, used on the broker side ([ITL](https://www.insurancethoughtleadership.com/life-health/ml-improves-life-settlements)).
  - Longevity Holdings: tree-ensemble LE work presented at UMN ([UMN seminar](https://cse.umn.edu/node/134646)).
  - **No funded ML-native policy *buyer* was found** ([search](https://raising.fi/ai-startups)).

## 4. Regulation
- **Licensing.**
  - 43 states plus PR regulate settlements under the NCOIL and/or NAIC model acts. AL, MO, SC, SD, WY and DC have no specific regime ([ELSA licence matrix](https://elsa-sls.org/elsa-publishes-latest-fact-sheet-life-settlement-licence-matrix-2025/)).
  - Providers need a state licence, a bond or other financial assurance, audited financials and an anti-fraud plan (e.g. [Utah 31A-23a-117](https://codes.findlaw.com/ut/title-31a-insurance-code/ut-code-sect-31a-23a-117/), [NY Ins. Law 7803](https://codes.findlaw.com/ny/insurance-law/isc-sect-7803/), [Texas 28 TAC 3.1721](https://regulations.justia.com/states/texas/title-28/part-1/chapter-3/subchapter-r/division-2/section-3-1721)).
  - A buyer either becomes a licensed provider in about 40 states or buys through one.
- **Consumer protection.**
  - Rescission windows, disclosure, and minimum-payout floors for terminal or chronic insureds (Oregon, Tennessee).
  - Brokers owe sellers duties in many states.
  - Kentucky, Maine, Washington and Oregon require insurers to tell seniors about the settlement option before lapse ([ThinkAdvisor KY](https://www.thinkadvisor.com/2010/04/05/kentucky-enacts-settlement-notice-rule/), [LII](https://lifeinsuranceinternational.com/news/state-lawmakers-back-life-settlements-1788663507)). These laws erode the "unshopped lapse" edge.
- **STOLI.**
  - NCOIL bans settlement within 2 years of issue; the NAIC model uses 5 years for policies with STOLI indicators. States are split ([MMM Law](https://www.mmmlaw.com/news-resources/2009-proposed-legislation-to-have-a-significant-impact-on-the-life-settlement-industry), [ThinkAdvisor](https://thinkadvisor.com/2007/07/23/ncoil-backs-2-year-ban-on-settling-policies)).
  - Insurers still litigate insurable interest. Delaware rulings (PHL v. Price Dawe 2011; Sun Life v. Wilmington 2019-21, memory) let a policy be voided as a wager years later, so chain-of-title diligence is a cost.
- **Data.** Medical records need HIPAA authorizations. Rx history (Milliman IntelliScript) is consented, FCRA-governed data and covers about 70% of applicants ([RGA Rx study](https://www.rgare.com/knowledge-center/article/rx-mortality-study)). No buyer gets claims data without seller consent.
- **Securities.** Funding the book from retail turns it into a securities business. Life Partners, GWG and Mutual Benefits all died there.

## 5. ML plausibility versus actuarial LE (judgement)

**For ML (v4 rules):**
- The outcome depends on many weak signals spread across messy APS records, Rx fills and claims, which is credit-like.
- Gradient-boosted survival models beat traditional comorbidity scoring in clinical prognosis.
- The LE houses are known to disagree and to show cohort bias (Xu).
- Rx-based risk scores validate on mortality (Milliman Rx/Irix scores, validated by Munich Re and [Gen Re](https://www.genre.com/us/landing-pages/whitepaper/gen-re-review-of-milliman-irix-risk-score-4-a-mortality-validation-study)).
- So ranking lift over a debit-method underwriter is **plausible**.

**Against:**
1. **Calibration matters more than ranking.** Money is lost on systematic level error (2008, GWG), and A/E tends toward 100% over the long run even when the underwriting is biased ([Bauer, Fasano et al., NAAJ 2017](https://pure.psu.edu/en/publications/evaluating-life-expectancy-evaluations/)).
2. **Adverse selection.** Sellers know their health. The broker auction selects for the buyer whose LE is too short (the winner's curse), so better ranking helps only if you can avoid bidding on the policies others reject.
3. **Outcome lag.** Labels take 5-15 years to arrive, and the SSA Death Master File has been restricted since 2011, which slows everyone's label collection.
4. **No published head-to-head.** We found no peer-reviewed ML-versus-LE-house accuracy result on settlement data, and the Morpheus/Lapetus episode shows the market discounts ML LEs.

**S3 = 3** (plausible, credit-like, but the lift is in the wrong place). This is not a 4.

## 6. Shape, scale, cheapest test

**Terranox-shaped?** Mostly no.
- S1 exists, but it is a **marketing rent**: Coventry Direct pays seniors less than an auction would, and the edge comes from TV ads, not a geological read.
- There is no step-change revaluation at "proof". Value accrues as yield plus mortality.
- S4: picking matters, but the business is cost of capital, premium funding, licensing and origination.
- S5: your maturities compound years behind the incumbents' head start.

**Venture-scale?** A large company is possible (Abacus is roughly a $1B-class public company with $100M+ adjusted net income; Coventry is a large private). But it is an asset manager or specialty-finance company that needs $100M+ of fund or credit capital before the ML matters. VCs will not fund the balance sheet, and the LE-model layer on its own is a services or vendor business (Lapetus, Harbor), which v4 rules out.

**Cheapest feasibility tests (4-8 weeks, under $25k):**
1. **Calibration test on public data (~$0-5k).**
   - Data: the Health and Retirement Study (65+, rich health, self-reported Rx, mortality follow-up; restricted Medicare-linked files on application).
   - Method: train a GBM/Cox survival model and compare it with a VBT-2015-plus-debits baseline.
   - Report: C-index **and** A/E by predicted-LE decile, out of sample by cohort year.
   - Kill if: calibration does not beat the baseline within ±5% A/E.
2. **Shadow-bid test (~$5-10k).**
   - Register as an investor or tertiary viewer on a broker auction (LISA-member brokers) or buy a small tertiary data tape.
   - Price 100-200 live cases blind, then compare against the clearing bids and the multiple LEs. Tertiary portfolios with matured policies give real outcomes.
   - Kill if: your price is not systematically different from the clearing bid where your model is confident.
3. **Origination test (~$10-20k).**
   - Partner with a licensed broker and run search and social ads aimed at "policy about to lapse" for owners 70+.
   - Measure cost per *qualified* lead (65+, $100k+ face, UL/convertible, impaired) and per closed deal against the direct-buyer economics implied by Coventry's ~15% of face.
   - Kill if: CAC per closed case is above about 3-5% of face. This is the binding constraint.

Score detail: S1 3 (direct buying below auction is real, but notice laws and broker duties erode it); S2 2 (buyer ~1.5-2.5x over about 10 years); S3 3; S4 3; S5 2 (maturity lag; LE-house and Coventry datasets are deeper). **13/25: fail.**
