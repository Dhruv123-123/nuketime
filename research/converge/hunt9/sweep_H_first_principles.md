# Hunt 9, Sweep H: First principles (enumerate every place the drill test holds)

## 0. Method, and an honest caveat on evidence
The shared WebSearch budget for this turn (200 calls across all agents) was already exhausted when this sweep started, so every search I fired was refused. I fell back to WebFetch on canonical pages I could name from memory (Wikipedia, gov.uk, EPA, ADWR, company sites). Numbers below are tagged:
- **(verified)** = read from a fetched page, URL given;
- **(memory)** = a figure I believe from prior knowledge but could not re-check this turn;
- **(my estimate)** = inferred.
Nothing is an invented transaction. Every (memory) number is a search away from being (verified) or killed; the kill tests say which.

The drill test, restated as four conditions on any asset class: (a) buyable cheap because true state unknown; (b) an expensive, usually-failing physical/legal/regulatory step reveals it; (c) the revealed state is worth a large multiple to a capitalised buyer before any full build; (d) public records that predict (b) exist but are illegible at scale, so incumbents pick by heuristic. A "junior" buys options on (a), uses ML to choose which to prove, proves them, sells to "majors".

## 1. The enumeration grid
I walked the economy by asset class and asked where a hidden state is revealed by a step somebody pays for and usually loses. Verdicts: C = candidate (section 2), N = near miss (section 3), F = footnote (excluded, drilling/prospecting), X = fails outright.

| Domain | Asset / right | Revealing step | Verdict |
|---|---|---|---|
| Natural resources | Western US ag water rights (yield + transferability unknown) | change-of-use case / adjudication | C8 |
| | Arizona desert land (100-yr assured supply unknown) | ADWR designation / certificate | C9 |
| | Non-powered dams, pumped-storage sites | FERC preliminary permit to licence | C7 |
| | Degraded farmland (restorable to wetland/stream) | mitigation-bank approval by IRT | C2 |
| | Wetland-encumbered land post-Sackett | Approved Jurisdictional Determination | C3 |
| | Forest carbon eligibility, timber inventory | validation / cruise | N (does not usually fail; NCX tried) |
| | Spring water sources, geothermal, aggregate, all minerals | test wells / drilling | F |
| Built infrastructure | Rail corridors (title) | quiet title / abandonment | seen (Brandt angle added) |
| | Landfills (expandable airspace) | expansion permit | C13 |
| | Retired plant sites with interconnection | surplus-interconnection approval | seen (powered brownfields) |
| | Grandfathered billboard / nonconforming-use permits | zoning litigation | N (niche) |
| | Nuclear sites | Early Site Permit | N (too costly, rarely fails) |
| Legal rights | UK option land | planning permission / appeal | C1 |
| | US raw land | entitlement / rezoning | C1 variant |
| | Possibilities of reverter in old deeds (schools, churches, railroads, parks) | declaratory / quiet-title action | C4 |
| | Patents from distressed owners | IPR + litigation | N (legible, occupied, auctioned) |
| | Copyright termination rights (35-yr) | notice + litigation | N (non-assignable before exercise) |
| | Film/TV chain of title | clearance + E&O | C14 |
| | Carbon / nutrient / species credits | validation | folded into C2 |
| | Spectrum, orbital slots, IPv4, domains | n/a | N / seen (auctioned, legible, or non-transferable) |
| Government positions | CON-licensed closed facilities | CON transfer / renewal | C12 |
| | Bank, insurance, broker charters | change-of-control approval | N (regulator decides; legible) |
| | SBIR Phase III (Lineage) | n/a | seen |
| | Qui tam from public data | DOJ intervention | N (public-disclosure bar; non-assignable) |
| Firms | Bankruptcy estates' causes of action | litigation | N (litigation funders) |
| | NOL shells | s.382 analysis | N (legible) |
| Biological | Shelved pharma compounds | Phase 2 | C5 |
| | University patents, germplasm, strain libraries | screening / trials | N (non-exclusive or legible) |
| | Racehorse foals (pinhooking) | breeze-up | N (no public data; small) |
| Financial claims | Unsatisfied commercial judgments | asset discovery + enforcement | C10 |
| | Bankruptcy trade claims, sovereign awards, life settlements | allowance / enforcement / underwriting | N (occupied, legible) |
| | Historic liability policies (insurance archaeology) | coverage litigation | N (folds into brownfields) |
| Digital | Old data, software, game IP | title clearance | N (small) |
| People / orgs | Minor-league athletes (BLA) | reaching MLB | N (stats legible; PR risk) |
| | Startups (YC itself) | PMF | comparable only |
| Collectibles | Misattributed paintings ("sleepers") | scholarship + technical analysis | C6 |
| | Shipwrecks (Odyssey) | expedition | F |

## 2. Candidates (scored 0-10 on drill-test fit; D = biggest doubt)

### C1. Land-promotion junior with ML site selection (UK first; Ireland/Australia/US entitlement as the second market). Score 7
1. **Proving step.** Promote a greenfield site through the Local Plan or a speculative planning application and, usually, an appeal to the Planning Inspectorate. Cost £250k-£1M per site in consultants, EIA, legal and appeal (memory/my estimate); 2-5 years. Base rate: England granted 87% of all 291,900 decisions in the year to June 2026, and 3,600 major residential decisions were granted (verified, gov.uk statistical release, https://www.gov.uk/government/statistics/planning-applications-in-england-april-to-june-2026/planning-applications-in-england-april-to-june-2026-statistical-release). That headline rate is for everything, including extensions; for speculative greenfield promotions the relevant p is "site becomes allocated or wins on appeal", which promoters put at roughly 30-50% (memory; appeal allow-rates for major housing have run around a third). Lever cap 2-3x. The promoter pays today.
2. **Signal.** Local Plans and evidence bases (PDF, 300+ authorities), five-year housing land supply statements (the single biggest predictor of appeal success, buried in PDFs and council committee reports), PINS appeal decisions (PDF letters, tens of thousands), call-for-sites submissions, SHLAA/HELAA site assessments, constraints (Green Belt, flood zone, AONB), committee minutes. Scattered across hundreds of Idox-style portals. Partly legibilised already by software vendors (LandTech/LandInsight, Searchland), which is both a warning (edge is shrinking) and evidence that incumbents still pick by hand.
3. **Unproven right.** A promotion agreement or option with a farmer: nominal upfront (£ thousands to low tens of thousands, memory), promoter recovers costs and takes roughly 15-25% of net sale proceeds (memory). Ag land about £21,000/ha (memory of the VOA 2019 land-value estimates; spreadsheet at https://assets.publishing.service.gov.uk/media/5f770df5d3bf7f7c30a588c6/VOA_land_values_2019.xlsx). Bilateral, not auctioned; farmers cannot read the planning evidence base.
4. **Proven state.** Consented land sells to housebuilders (Barratt, Persimmon, Taylor Wimpey, Vistry, Bellway) at roughly £1-6M/ha outside London (memory of VOA 2019): 50-300x the ag value. Liquid; sold by tender to builders before any build. R1 on the promoter's own outlay is 5-20x on a win.
- **Ceiling.** 212,000 homes granted in the year to June 2026 (verified, same release). At £50-100k of land value per plot (my estimate) that is £10-20B/yr of consented-land value created every year in England alone.
- **Incumbents.** Gladman (acquired by Barratt, 2022, around £250M, memory), Catesby (Urban&Civic), Richborough, Rosconn, Terra Strategic, Hallam Land (Henry Boot), L&Q Estates; land agents (Savills, Strutt & Parker). Tools: GIS, LandTech; site choice is relationship-led.
- **Kill test (days).** Pull 200 PINS major-housing appeal decisions 2022-2025; label allowed/dismissed; check whether 5YHLS shortfall + Local Plan age + Green Belt flag already predicts outcome (if the regulator's own fields give AUC > 0.85, the ML edge is thin). Then check LandTech's "planning probability" product; if it exists and is good, the data is already legible.
- **D.** This is a political, relationship process in which incumbents are entrenched; the ML edge may only be in picking which of thousands of farms to approach, which may still be worth a lot.

### C2. Mitigation-bank junior (wetland and stream credits). Score 6.5
1. **Proving step.** Take a degraded parcel from prospectus to an approved Mitigation Banking Instrument with the Interagency Review Team, then hit performance milestones that release credits over "around 10 to 12 years" (verified, Wikipedia Mitigation banking). Cost $0.5-2M per bank in hydrology, design, legal, financial assurances before the first credit sells (my estimate); 2-4 years to MBI (my estimate). p of a filed prospectus reaching an approved instrument: unknown (my guess 40-60%), but the hidden state that really matters is credit count and credit demand, not approval alone. Lever cap about 2x on approval; higher on "which parcel yields saleable credits".
2. **Signal.** RIBITS (bank list, service areas, credit ledgers) is legible; the demand side (404 permits issued, impact acreage per watershed) is in ORM but as summaries; the illegible layer is district JD letters and delineation reports (PDF), historic aerials, drainage-district records, hydric-soil surveys, dam and levee records, state 401 files. Over 1,200 banks and 750,000 credits approved nationwide as of 2024 (verified, Wikipedia); 1,800+ bank sites in RIBITS by 2013 (verified, EPA page https://www.epa.gov/cwa-404/mitigation-banks-under-cwa-section-404).
3. **Unproven right.** Degraded cropland or pasture at $3-8k/acre (memory), bought or optioned bilaterally from farmers who cannot read permit demand in their watershed.
4. **Proven state.** Wetland credits roughly $30k-$150k+ per credit-acre and stream credits hundreds of dollars per linear foot depending on district (memory); whole banks are bought by Ecosystem Investment Partners, Resource Environmental Solutions (KKR-owned, memory), Westervelt Ecological Services, Wildlands. Step-up on land 5-30x. Credits sell before the ecological work is complete (credit-release schedule), so the option is tradable.
- **Ceiling.** US compensatory-mitigation market around $3-4B/yr (memory, ELI/Ecosystem Marketplace); 62% of banks are private entrepreneurial banks (verified, EPA page). Credible multi-billion pool, plus species and nutrient credits.
- **Incumbents.** EIP, RES, Westervelt, Wildlands, Mitigation Solutions USA, Ecosystem Planning & Restoration; dozens of regional sponsors. Picking is done by ecologists with local networks.
- **Kill test.** From RIBITS, for five Corps districts, compute credits sold per year against credits available (if supply overhangs demand everywhere, no step-up); count prospectuses that never reach an MBI (RIBITS shows "pending"); check whether ELI's bank-failure finding ("a significant portion of compensation sites are failing", verified) is about ecology or economics.
- **D.** The proving step does not usually fail; the risk is demand and the 10-year credit release, so the ML lever is on site choice and demand forecasting rather than on a binary drill.

### C3. Post-Sackett jurisdiction arbitrage. Score 5
1. **Proving step.** Request an Approved Jurisdictional Determination from the Corps under the "continuous surface connection" test (verified, Wikipedia Sackett 2023). Cost $10-50k for delineation and consultant (memory), 6-18 months. p unknown; anecdotally most post-Sackett AJDs find no federal waters (memory), which means p is high and the lever small.
2. **Signal.** NWI maps, LiDAR, hydric soils (legible); the illegible layer is district AJD letters and delineation reports posted as PDFs, plus state wetland rules (which fill the gap in FL, NJ, MN, WI and others).
3. **Unproven right.** Land priced as wetland-encumbered, $2-5k/acre (memory), bilateral purchase.
4. **Proven state.** Developable land at $20-100k/acre in growth corridors (memory); buyers are homebuilders. Earthjustice claims "over 59 million acres of wetlands are threatened" (verified, advocacy figure).
- **Ceiling.** Large but confined to states without their own wetland programmes (TX, GA, AL, SC, parts of NC).
- **Incumbents.** Land developers and wetland consultants do it parcel by parcel.
- **Kill test.** Scrape one district's AJD list for 2024-2025; if >70% non-jurisdictional, the step is not "usually failing" and the market will already have repriced.
- **D.** Cheap proving step and high p: the economics are real but the ML lever is weak.

### C4. Reverter archaeology (buy possibilities of reverter in old deeds). Score 5
1. **Proving step.** Declaratory or quiet-title action to establish that a fee simple determinable ("so long as used for school/church/railroad purposes") has terminated and the land has reverted. Cost $50-250k, 1-3 years (my estimate). p low (my estimate 10-20%): marketable title acts in Florida, Michigan, Ohio, Minnesota, Iowa "among others" extinguish old interests not re-recorded within "typically 30 to 40 years" (verified, Wikipedia Marketable title), courts read purpose language as covenants rather than conditions, and reverters are sometimes inalienable. Lever cap 5-10x.
2. **Signal.** County deed books and grantor-grantee indexes, 1850-1950, scanned or on microfilm: the most illegible public record in America. Also school-closure lists, church deconsecrations, railroad abandonments. The rail version is already seen; Brandt (verified) confirms 1875 Act rights-of-way are easements that disappear on abandonment and the dissent put takings exposure at "hundreds of millions".
3. **Unproven right.** Heirs' reversionary interests, bought for hundreds to low thousands of dollars from people who do not know they hold them; alienable in most non-MTA states (memory).
4. **Proven state.** Fee in a closed-school, church or depot parcel worth $0.5-10M; buyer is the occupant or a developer. R1 of 10^2-10^3 on a win.
- **Ceiling.** Unknown; plausibly thousands of parcels, not obviously "many billions".
- **Incumbents.** None at scale; a few title lawyers.
- **Kill test.** Sample 50 school and railroad deeds in a non-MTA state (Texas, Pennsylvania), count determinable language, search case law for reverter-claimant win rates since 2000.
- **D.** Reputationally ugly (taking a school's land from heirs' paper) and the pool is unproven.

### C5. Shelved-compound junior that reads what pharma does not (Roivant 2.0). Score 6
1. **Proving step.** Phase 2 trial, $20-60M, 2-3 years; Phase 2 to Phase 3 transition about 30% industry-wide (memory of BIO data). Lever cap about 3x.
2. **Signal.** Structured: ClinicalTrials.gov, FDA labels. Illegible: FOIA'd FDA reviews, EMA EPARs, old INDs and Japanese/Chinese trial registries, conference posters, pharmacovigilance narratives, legacy company archives. Roivant's own Datavant/Lokavant show the data play is recognised.
3. **Unproven right.** A licence from a pharma shelf: Axovant bought intepirdine from GSK "for only $5 million" (verified, Wikipedia Axovant). Bilateral, but pharma often runs a process, which is the "owner runs the price" failure.
4. **Proven state.** Telavant sold to Roche for "$7.1 billion upfront" about a year after Roivant licensed the TL1A asset from Pfizer (verified, Wikipedia Roivant); Axovant raised $315M in a 2015 IPO on the $5M asset before any proof, then failed Phase 3 (verified). Dermavant to Organon with $175M upfront (verified). Very liquid, tradable before approval.
- **Ceiling.** Thousands of shelved assets; biopharma M&A exceeds $100B/yr (memory).
- **Incumbents.** Roivant, BridgeBio, Centessa, Cullinan, PureTech, Royalty Pharma; shell-sweepers (Tang Capital).
- **Kill test.** List 30 assets Roivant and BridgeBio in-licensed 2015-2024 and check whether their outcomes were predictable from unstructured regulatory documents available at the time; and check how many were acquired in a competitive process.
- **D.** Lever is only ~3x and the strongest incumbent already runs the model.

### C6. Art "sleeper" junior (ML over scanned auction catalogues). Score 6
1. **Proving step.** Provenance and technical research plus scholarly consensus: Salvator Mundi was bought in 2005 for "$1,175" and reached National Gallery authentication in 2011 after restoration that began in 2006 (verified, Wikipedia). Cost $20-100k per serious candidate (my estimate); 1-5 years. p of a flagged candidate getting upgraded: my estimate 2-10%. Lever cap 10-50x: the most Terranox-like profile here.
2. **Signal.** Auction catalogues worldwide (scanned, image-heavy, decades deep), Getty Provenance Index, RKD, Witt Library photo archive, catalogues raisonnés, sale-room records. Philip Mould: "we scour daily the world's auction catalogues for paintings that are wrongly identified" (verified, Wikipedia). Incumbents do this by eye.
3. **Unproven right.** Lots at regional and estate auctions. Caveat: it is an auction, but the seller is ignorant and the reserve is set at the wrong attribution; competition is a handful of dealers.
4. **Proven state.** $1,175 to $80M (2013) to $450M (2017) at the tail (verified); typical sleeper upgrades are £5k to £500k (memory). Buyers: Sotheby's/Christie's consignment, dealers, museums; liquid.
- **Ceiling.** Global art market around $65B/yr (memory); sleeper upgrades perhaps $100-300M/yr (my estimate). Modest; tail-driven.
- **Incumbents.** Philip Mould, Fabrizio Moretti, Eric Turquin, Colnaghi, auction-house specialists; AI-attribution startups sell services rather than own works.
- **Kill test.** Tabulate 2015-2025 publicised sleeper sales from Art Newspaper coverage with purchase and resale prices; test whether an image model flags them from the original catalogue photos.
- **D.** Attribution is contested even for Salvator Mundi (verified disputes); ceiling is small for YC.

### C7. Hydro-licence junior (non-powered dams and closed-loop pumped storage). Score 5
1. **Proving step.** FERC preliminary permit to licence: $3-10M and 4-8 years (my estimate); most preliminary permits lapse without a licence application (memory), so p about 10-20%. Lever cap 5-10x.
2. **Signal.** National Inventory of Dams (legible), ORNL HydroSource (legible and already ranks NPDs, which is the problem), FERC eLibrary filings and Corps dam-inspection reports (PDF).
3. **Unproven right.** Preliminary permits are first-come from FERC (fails "buy from ignorant seller") but small holders' permits and land options can be bought bilaterally.
4. **Proven state.** Licensed projects sell to infrastructure funds: Goldendale (1,200 MW) and Swan Lake (393 MW) hold FERC licences and are "owned by Copenhagen Infrastructure Partners and ... developed by Rye Development" (verified, ryedevelopment.com/projects.html). Over 80,000 non-powered dams with about 12 GW of potential; 81 of the top 100 are Corps-owned (verified, Wikipedia Hydropower in the US).
- **Ceiling.** 12 GW NPD plus a pumped-storage pipeline; tens of billions in capex but development premiums are perhaps $50-100/kW (my estimate).
- **Incumbents.** Rye, rPlus Hydro, Gridflex, Absaroka, Premium Energy.
- **Kill test.** Count preliminary permits issued 2010-2018 against licences issued by 2025 (FERC eLibrary); if the ORNL ranking already predicts which got licensed, there is no data edge.
- **D.** Federal dams need a Corps lease, and the legible ORNL ranking has already written the answer.

### C8. Western water "paper-to-wet" junior. Score 4
Urban users pay "up to 10 times more than agricultural users" (verified, Wikipedia Water trading), but C-BT transfers take "4 to 6 weeks and don't require state engineer approval" (verified), so the most liquid market has no hidden state. Non-project rights need a change case (1-3 years, $100k-$1M, memory) that rarely fails outright but trims yield. Colorado's HydroBase has digitised diversion records, so the regulator has written the answer. Incumbents: Water Asset Management, Vidler (sold to D.R. Horton in 2022, memory), Greenstone, Renewable Water Resources, Cadiz. Kill test: compare decreed vs claimed consumptive use in 50 recent Division 1 change decrees; if the haircut is predictable from HydroBase, p is high and legible.

### C9. Arizona Assured Water Supply arbitrage. Score 3
ADWR requires proof the supply "is uninterruptible for the 100-year period" (verified, azwater.gov/aaws). After the 2023 Phoenix AMA model found multi-million-acre-foot unmet demand, new groundwater-based determinations were paused (memory), so proving now means procuring alternative water, not revealing a hidden state. Driller logs are scanned but the problem is drilling-adjacent. Near-footnote.

### C10. Commercial judgment-enforcement junior. Score 5
Buy unsatisfied business-to-business judgments at 5-15 cents (memory), use ML over county civil dockets (scanned, 3,000 counties), recorder, UCC and corporate registries to find the 10-20% with reachable assets (my estimate), prove by asset discovery and garnishment, collect or sell the collectable paper. Lever cap 5-10x. Pool size unknown this turn (searches refused); judgments are assignable in most states. Incumbents: small judgment-recovery shops; debt buyers (Encore, PRA) on consumer paper; Legalist on government receivables. D: operational grind, and the "proven state" is only semi-tradable. Kill test: sample 500 Texas district-court money judgments over $100k from 2019 and check abstract-of-judgment and release filings to measure the collected fraction.

### C12. CON-licensed closed facilities. Score 3.5
Buy closed rural hospitals or nursing homes for their certificate-of-need or bed licences; prove via transfer/renewal (contested, $200k-1M, my estimate); sell to systems. "Approximately 35 states and the District of Columbia maintain CON regulations"; "CONs are sometimes sold in bankruptcy as an asset"; CON rents for urban hospital CEOs estimated at "$91,000 annually" (all verified, Wikipedia Certificate of need). D: value is local and the buyers are the contestants.

### C13. Landfill-airspace junior. Score 4
Buy small or closed landfills; prove via expansion permit (2-5 years, $1-5M, p 30-50%, my estimates); sell to WM/Republic/GFL who value airspace at NPV of tipping fees. Signal: state permit files and groundwater monitoring reports (scanned). D: NIMBY, liability, and the buyers already know every site.

### C14. Film/TV chain-of-title junior. Score 4
Buy old titles and negatives from estates and bankrupt distributors; prove via chain-of-title clearance and E&O insurability (p 30-50%, my estimate); sell to streamers and boutique labels. Signal: Copyright Office Catalog of Copyright Entries and pre-1978 assignment records (scanned). D: small pool; lawyers' work.

## 3. Near misses (one condition failed)
- **Patents (Intellectual Ventures: "over $5.5 billion" raised, "nearly 40,000 assets", verified)**: fails (d), USPTO data is legible and portfolios are brokered/auctioned.
- **Copyright termination rights**: fails (3): the right cannot be assigned before exercise; the window opened in 2013 (verified, Wikipedia Copyright Act of 1976). Agent model only.
- **Minor-league athletes (Big League Advance, "average investments are about $350,000", lawsuits 2018 and June 2025, verified)**: fails (d), stats are legible; PR risk shown.
- **Bankruptcy trade claims, sovereign awards, life settlements**: fail (d), registers are legible and claims traders are entrenched.
- **Qui tam from public data**: fails (3), public-disclosure bar and non-assignable.
- **Heirs' property / partition**: fails on ethics; also UPHPA now blocks forced sales in many states.
- **Bank/insurance charters**: fails (b)/(d), regulator decides on the buyer, not the asset; call reports are legible.
- **University patents, germplasm, strain libraries**: fail (3), non-exclusive or legible.
- **Forest carbon (NCX), Western water C-BT, interconnection queues**: fail (b), step does not usually fail or regulator has written the answer.
- **Septic perc tests, FEMA LOMAs, tax-deed quiet title**: fail (b), proving is cheap and mostly succeeds, so no ML lever.
- **Solar/wind development rights**: fail on incumbency (hundreds of developers) and the seen interconnection angle.
- **Orbital slots, spectrum, IPv4, domains**: fail (3), auctioned, legible, or non-transferable.
- **Grandfathered billboard permits, nonconforming uses**: pass on paper, pool too small.
- **Cell-tower / ground-lease aggregators (Landmark, AP Wireless)**: no proving step; pure information arbitrage.
- **Nuclear early-site permits**: proving too expensive and rarely fails.

## 4. Footnotes (excluded by the standing rule)
Spring-water sources (test wells), geothermal, aggregate, shipwreck salvage (Odyssey: Black Swan treasure awarded to Spain, $1M fees for "bad faith", pivot to seabed minerals, all verified) and every mineral or hydrocarbon play.

## 5. Structural comparables YC will ask about
- **Junior miners / Terranox**: the template.
- **Roivant/Axovant**: $5M licence to $315M IPO before proof; Telavant to Roche at $7.1B upfront (verified).
- **Legalist**: "more than $1.5 billion", "artificial intelligence to identify investments from public datasets" (verified, legalist.com).
- **Burford**: YPF share estimated at $6B, then overturned on appeal in 2026 (verified): proof that proven claims trade and can un-prove.
- **Intellectual Ventures**: the cautionary patent junior.
- **Big League Advance**: the people junior.
- **EIP / RES / Westervelt**: the mitigation-bank juniors and majors.
- **Rye Development / Copenhagen Infrastructure Partners**: the licence junior and its major (verified).
- **Gladman / Barratt; Hallam Land / Henry Boot**: the land-promotion junior and its major (memory).
- **Vidler / D.R. Horton; Water Asset Management**: water juniors (memory).
- **Philip Mould; Eric Turquin**: the sleeper hunters (verified method).

## 6. Ranking
1. C1 Land-promotion junior, 7. 2. C2 Mitigation-bank junior, 6.5. 3. C6 Art sleepers, 6 (best structural fit, smallest ceiling). 4. C5 Shelved-compound junior, 6 (largest ceiling, weakest lever). 5. C4 Reverter archaeology, 5. 6. C3 Sackett arbitrage, 5. 7. C10 Judgment enforcement, 5. 8. C7 Hydro licences, 5. Rest 3-4.
