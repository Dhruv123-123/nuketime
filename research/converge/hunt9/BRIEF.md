# Hunt 9 brief: the drill test (shared by every sweep agent)

## Why this hunt exists
Dhruv (founder) is looking for a NEW company idea for a YC application (not his existing company Terranox; never pitch Terranox).
Terranox is the template: it reads public-but-illegible Canadian mineral-assessment files (SMAD) with ML to decide where to drill
for uranium; it BUYS the mineral right cheap from owners who cannot read those files; a successful exploratory drill takes the
land from about $1/ha to about $10,000/ha (a 10^4 step-up in speculative value); the developer who buys the proven ground then
spends about $30k/ha and collects about $100k/ha (a 2.5x on big dollars). ML works there because the proving step (an exploratory
drill) is expensive and usually fails (class imbalance), so cutting the cost per HIT by 10x means 10x more shots per dollar.
The cap on that lever is 1 / base hit rate: a 1% hit rate can give 10x or more, a 30% hit rate at most about 3x.

We want the same structure anywhere in the world economy. Dhruv's words: "don't overfit on the stuff you've found so far, just go
crazy" and "look broad, not only in the stuff we're looking at". So: ANY industry, ANY country, ANY public dataset.

## The four-part drill test (fill every part with numbers and sources, say "unknown" where unknown)
1. PROVING STEP. An expensive step that reveals a hidden state of an asset or right and usually fails. Give: what the step is,
   cost per attempt ($), time per attempt, base hit rate p (fraction of attempts that succeed today), who pays for it today.
   Lever cap = 1/p. Drilling, prospecting or mineral/oil/gas/geothermal/lithium/hydrogen/CO2-injection exploration are EXCLUDED
   (Dhruv's standing rule: "no prospecting or drilling related ideas"); list such a candidate only as a one-line footnote.
2. SIGNAL. Public data that predicts the outcome of the proving step, which incumbents do not extract because it is illegible at
   scale (scanned, PDF, unstructured, scattered across thousands of files, needs OCR/NLP/vision/joins). Name the dataset(s), the
   format, the size, and whether the owner or regulator has already written the answer into a legible field (if a lookup table
   gives the answer, there is no edge: earlier hunts found regulators' status fields get within 0.03-0.08 AUC of the best model).
3. UNPROVEN RIGHT. The thing you buy BEFORE proving. Who owns it, typical price, whether it can be bought (not auctioned, not
   first-come, not non-transferable), and whether sellers can read the data. Earlier hunts killed everything the owner sells by
   tender or auction (the owner runs the price) and everything non-exclusive (reading first wins nothing).
4. PROVEN STATE. After the step succeeds: who buys, at what price, step-up multiple R1 = proven value / unproven price, whether
   such proven assets actually trade (liquidity, named buyers, named comparable transactions), and whether it is tradable BEFORE
   the full physical build (you must be able to sell the proven option, not have to build the mine yourself).

Also for each candidate: MARKET CEILING (number of assets, total value of the proven pool; Dhruv rejects "too niche": there must be
a credible path to a large company, think asset pools of many billions), INCUMBENTS (who already does this, with what tools; name
companies), and a KILL TEST (the cheapest public-data check, doable in days with no building, that would falsify the candidate).
The company must DO the thing itself (own the asset / the right / the claim and realise the value), not sell software or a
service to the people who do. Feasibility only: we are not building anything in this hunt.

## Already seen (compete on equal terms; do not re-research unless you have a new angle or new numbers)
Geology/Terranox (excluded, it is Dhruv's company); powered brownfields (fails: open contaminated parcels already sell at clean
prices, step-up about 1.1x); rail corridor title from scanned ICC valuation maps and deed books for transmission/fibre routes
(passes on paper, untested); grid interconnection queue positions (probably occupied: GridCARE, Cloverleaf, Tract); Alberta oil
well closure-liability underwriting (small, drilling-adjacent); Lineage = buying dormant SBIR Phase II firms for Phase III
sole-source rights (5/10, legible data); orphaned ICS/OT software lines; robotic O&M of underperforming solar/wind; foreign-approved
drugs missing in the US; auctioned rights (spectrum, offshore leases); IPv4 legacy blocks (killed earlier as "owner sells by
tender", re-evaluate only if you find the unproven/proven structure); nuclear engineering picks (TRISO sorting, Margin, hafnium).

## How to work
- Use WebSearch (mode "standard" first, "extended" when results are thin) and WebFetch on result URLs. Budget about 30-45
  searches. The container's own network reaches only GitHub and PyPI, so do not try to download datasets; read documentation,
  reports, papers, company pages and news.
- Prefer named numbers with URLs. Numbers you infer are marked "(my estimate)". No invented transactions.
- Be adversarial with yourself: for every candidate ask who already does it, and whether the "illegible" data is in fact already
  summarised in a legible field somewhere.
- Produce 8-15 candidates, at least half NOT on the seen list, with a provisional fit score 0-10 and one line on the biggest doubt.
- Write your full report (markdown, up to about 3,000 words) to the file path given in your task, then return a 400-word summary
  with your top 3 and their numbers.
- Do not write anywhere under /mnt/project-files. Do not install packages. Do not build pipelines.
