## Continuation Forge: feasibility memo

*Note: the shared WebSearch budget was used up before this run, so no new searches could be made. Numbers marked [ROI25] come from the primary report, which I downloaded and parsed this run: 2025 Richardson Oliver Patent Market Report, https://static1.squarespace.com/static/62e409548ddf9a45093621ec/t/691788dcafe85415ced5eb9a/1763150044519/The+2025+Richardson+Oliver+Patent+Market+-+The+Brokered+Patent+Market+Report+in+2024+-+A+Smarter%2C+Sharper+Patent+Market+-+IAM+Media+-+20250917.pdf. USPTO fees come from https://www.uspto.gov/learning-and-resources/fees-and-payment/uspto-fee-schedule. Everything else is labelled as prior knowledge or an estimate.*

### Frame of reference
The rung is: buy a family that still has a pending continuation, get a claim allowed that reads on a product shipping today, and sell the asset with an evidence-of-use (EoU) chart. The physical step is legal prosecution, which is cheap and can be outsourced. That passes the geothermal-in-coal-mine test. Discovery is not 80%+ of the rung, though. I estimate that finding spec support and a target product is about 50-65% of the work. The rest is written-description risk at the examiner (Ariad 2010), validity risk the buyer will price in (IPR, Alice 101), and a slow, buyer-controlled sale. The proof does not settle value the way a drill core does. The buyer is still pricing years of litigation.

### Step-up ratio
- **Unproven price:** a small-inventor or distressed family costs about $10-50k (estimate). For comparison, the median asking price of assets that actually sold in 2023 was only $33k, and $95k in 2024 [ROI25].
- **Proven price:** the median ask is $325k per family across all listings and $158k per family that sold [ROI25]. Packages with EoU command a 32-108% premium [ROI25]. Closing discounts from asking run 0-75%+ [ROI25]. A rough proven, EoU-backed close is $325k × 1.54 × 0.65 ≈ $325k (estimate). Deals above $1M per asset happen but are rare [ROI25].
- **Ratio:** about 5-30x on purchase price, and about 3-15x on all-in cost. That is two to three orders of magnitude short of 10^3-10^4.
- **Transactions per year:** the whole brokered market was $158M in 2024, flat against 2022 and 2023. 1,611 packages were listed, with a median of 2 assets each [ROI25]. Only 20-30% of listings sell, and it takes years: 2019 listings have only now reached 30% [ROI25]. My estimate is about 300-500 sales a year. The report says there are "rarely competing buyers" [ROI25].

### Hit rate and proving capex today and with ML
- **Prosecution cost:** small-entity filing, search and exam fees total about $800, plus a $516 issue fee. Track One costs $1,806 for a small entity [USPTO]. Attorney fees add about $5-40k (estimate). Since 2025, continuations filed more than 6 years after the priority date also carry a surcharge (prior knowledge).
- **All-in per shot:** about $20-100k (estimate).
- **Base rate:** allowance itself is high, at roughly 70-90% (estimate). The real hit is an allowed claim that reads on a product and actually sells. Base sell-through is about 30% even for packages that are already marketed [ROI25], and only 21% of packages include an EoU today [ROI25]. My estimate of the true hit rate (allowed, reads on a product, sells for 10x or more) is about 5-15%. That caps the ML lever at roughly 7-20x in theory. In practice, ML improves only the matching step, not validity or buyer demand, so the realistic gain is about 2-4x (estimate).

### Data source
The sources are USPTO Patent Center file wrappers, USPTO bulk full text, PatentsView, the USPTO assignment database, PACER section 363 sale schedules, FCC equipment authorisation photos, iFixit and TechInsights teardowns, product manuals, and GitHub. All are public.

Most of this data is legible. Pending-continuation status is a structured status field, and specs are full text. The teardown side is less legible, but TechInsights sells exactly that mapping, and Patlytics already advertises "crawl for evidence of use across public sources" with citation-backed claim charts (patlytics.ai, fetched by an earlier verifier). The outcome is effectively summarised already: brokers list "open continuations" as a standard quality factor [ROI25].

### How the right is bought
Patents and pending applications are assignable under 35 USC 261, and assignments are recorded with the USPTO. Bankruptcy estates sell them under 11 USC 363. Drafting continuation claims to cover a competitor's product you already know about is lawful (Kingsdown v. Hollister, 1988). The limits are written-description support and prosecution laches (Hyatt v. Hirshfeld, 2021).

The cheap-purchase thesis is weak. Brokers handle 87% of sold packages [ROI25], and they price open continuations in. A live continuation is also a wasting asset: distressed owners often let it lapse before anyone can buy it (prior knowledge).

### Capitalised buyer
From 2020 to 2024, operating companies bought 15-40% of packages, NPEs 11-50%, and defensive aggregators 20-40% [ROI25]. Litigation funders also buy (Burford, Fortress; prior knowledge). These buyers are real, but they set the price; they are not price-takers. Sold packages have a 22% litigation rate [ROI25], which shows that the value is realised through litigation.

### Integration ladder above
1. Prosecute and sell (this rung).
2. License directly.
3. Self-fund assertion.
4. Run a portfolio licensing programme, at Acacia or IV scale.

The ceiling is a few billion dollars at most: IV raised about $6B, and Acacia is worth under $1B (both prior knowledge). The ladder never connects to making products, so there is no trillion-dollar path.

### Who else does this
- **Aggregators and NPEs:** IP Edge, Dominion Harbor, Acacia and IV, all of which run continuation practice on acquired families (prior knowledge).
- **Defensive aggregators:** RPX and AST.
- **Brokers:** brokers who screen for open continuations, such as Tangible IP and Iceberg.
- **Claim-charting tools:** Patlytics, Solve Intelligence and IPRally commoditise the matching step.

### Smallest feasibility test (2 weeks)
1. Pull about 300 small-entity US families with a pending continuation from PatentsView and Patent Center bulk data.
2. Run LLM spec-to-product matching against FCC photos and manuals.
3. Hand-build 5 EoU charts for proposed continuation claims.
4. Get firm purchase quotes from 5 owners or trustees.
5. Show the 5 charts under NDA to 3 buyers (RPX or AST, one NPE such as IP Edge, one funder) and ask for indicative bids conditional on allowance.

**Kill criterion:** median bid divided by (quote + estimated prosecution cost) is below 20x, or owners quote above $50k because a broker is already involved. Based on the ROI25 figures, I expect the test to kill the idea.

### Verdict
**Fails the rubric.** The frame is real and the physical step is trivial, but the step-up is about 3-30x, not 10^3-10^4. The signal is legible and already priced by brokers. Incumbents already run this exact playbook, and the ladder tops out as an NPE.

Scores: C1 2, C2 2, C3 2, C4 1, C5 2, **total 9/25.** Not a lead candidate for the YC memo. Its one useful lesson is that a frame where the physical step is a cheap legal action does pass the geothermal test, so look for a ladder where that kind of legal or proving step sits in front of a buyer that pays at once.