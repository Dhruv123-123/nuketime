# Round 4 sweep: buyable assets whose value only ML can read (energy, machines, robotics, deeptech, security)

Written 15 Oct 2026 against the corrected test in `ROUND4.md`:
(1) you buy it at a price set by people who cannot see its value; (2) the value sits in illegible public data, and ML is what makes valuation possible at scale; (3) it is worth far more than its price; (4) the company realises the value itself.
Budget: 17 web searches. Government hosts were not reachable from here (pjm.com, courtlistener and celestrak all timed out). Two routes do work. `raw.githubusercontent.com` serves files, but the gh API is limited to repositories configured for this session, so GitHub search returns little. The PUDL S3 bucket (EIA-860/923, FERC Form 1, EPA CEMS) also answered: `pudl.sqlite.zip` returned 200.
Earlier rounds already covered and scored these, so this sweep does not repeat them: stranded turbines (5), part-out of retired plants (4), idle grid equipment (3), queue attrition (killed by backtest), ERC offset mining (5, `lane_built.md`), orphaned ICS software (5), and SBIR Lineage (5).

## Scores at a glance

| # | Candidate | Illegible data | ML essential? | Score |
|---|---|---|---|---|
| 1 | **Corridor rights: rail rights-of-way whose fee-vs-easement status is buried in scanned deeds and ICC valuation maps, bought and developed as transmission/fiber corridors** | 1850-1920 handwritten deeds, ICC valuation maps, STB dockets | Yes | **6** |
| 2 | Late-stage projects with signed GIAs, priced off cluster-study PDFs | Thousands of study PDFs in 7+ formats, contingent-upgrade trees | Yes for extraction; edge unproven | 5 |
| 3 | Closed industrial "powered sites" (mills, smelters, chemical plants): which rights survive | Permit PDFs, water-rights files, utility dockets, imagery | Partly | 5 |
| 4 | Bankruptcy-estate hardware (factories, tool sets, IP) bought by a builder | Dockets, asset schedules, auction photos, multilingual insolvency registers | Helpful, not what unlocks value | 4 |
| 5 | Surplus interconnection headroom at low-output plants | EPA CEMS hourly output + interconnection rights | No, mostly a join | 4 |
| 6 | Underperforming small hydro (FERC dockets + USGS flow series) | Scanned licence dockets, flow time series | Partly | 4 |
| 7 | Idle Chinese/European solar and battery lines from judicial auctions | Chinese appraisal PDFs, photos | Yes | 3 |
| 8 | Used in-orbit GEO satellites priced from TLE-derived fuel | TLE time series | Yes | 2 |
| - | SBIR Lineage, re-scored | | Yes | 5 (unchanged) |

Nothing reaches the Terranox bar of 8+. The best new idea is a 6. That is one point above anything found in rounds 1-3 inside Dhruv's sectors.

---

## 1. Corridor rights from rail rights-of-way (6/10, best of sweep)

**The idea.** Long linear corridors are the scarcest input for new transmission, and to a lesser degree for long-haul fiber. Siting a 300-mile line across hundreds of landowners takes about a decade. Grain Belt and Clean Line are the cautionary tales ([Canary Media](https://www.canarymedia.com/articles/transmission/how-transmission-along-railroads-and-highways-could-break-open-clean-energy-growth)). SOO Green, a $2.5B, 2.1 GW, about 350-mile underground HVDC line, avoided that by following Canadian Pacific's right-of-way. It took "the path of least resistance, a private negotiation with a private railroad that owned virtually all the rights of way" (same source).

The catch is that a rail corridor is a patchwork:
- Some parcels are owned in fee simple. The owner can host anything, with no landowner consent needed.
- Others are only railroad-purpose easements. These revert to adjoining owners or limit what the corridor can host.
- Federal land-grant segments come under separate rules (1875-Act grants are easements; earlier grants differ).

One 11.5-mile corridor in Talbot County, Maryland crosses **318 parcels** ([TPL report, Nov 2025](https://www.tpl.org/wp-content/uploads/2025/11/TPL-report-on-Rails-to-Trails-Landowner-Rights-Act-final.pdf)). Whether a segment is fee or easement can be settled only by reading each acquisition instrument ([Rails-to-Trails, "Who actually owns the right of way"](https://www.railstotrails.org/wp-content/uploads/2024/02/Who-Actually-Owns-the-Right-of-Way.pdf)). The 1990s fiber builds along railroads ended in landowner class actions because nobody had read the easements.

**The data and why it is illegible.**
- County grantee indexes and deeds, 1850-1920, mostly scanned, many handwritten, filed under defunct railroad names.
- ICC valuation maps and schedules (1915-1920s). These list every parcel and how it was acquired, as scanned drawings in state archives and at railroads.
- STB abandonment and railbanking dockets (14,184 miles abandoned 1983-2008, 5,079 miles railbanked: [Wikipedia, Railbanking](https://en.wikipedia.org/wiki/Railbanking)).
- State rail plans, short-line sale filings, and parcel GIS.

**Why ML is essential.** Classifying granting-clause language as fee or easement across hundreds of thousands of scanned instruments needs handwriting OCR, legal-text classification, matching to the right parcel, and chaining to the original railroad. A title lawyer does this one corridor at a time for months, which is why nobody prices whole networks this way. A spreadsheet join cannot do it, because the information exists only in the images.

**What is bought, and the typical price.**
- Short-line railroads and branch lines. These trade among Genesee & Wyoming, Watco, OmniTRAX and small owners, often valued on freight EBITDA alone.
- Out-of-service or abandonment-pending branches, bought from Class Is at near salvage value.
- Fee strips from railbanked corridors held by states and trail groups. These are leases rather than sales, and politically harder.

Corridors trade for freight or salvage value: low millions for a 50-150 mile short line. This is my estimate; I did not find a price series.

**Value once known.** The value is a continuous fee-owned corridor between a generation-rich node and a load node. Merchant HVDC capacity or a hyperscaler fiber route is worth hundreds of millions to billions per corridor (SOO Green is $2.5B of capex built on one). Even an easement-heavy corridor tells a developer exactly which parcels to buy, which cuts siting risk.

**How the company realises it.** It owns the corridor and develops the line (merchant HVDC or buried fiber), or brings in a developer as partner with an equity stake. The rail operation keeps running and keeps the corridor in rail use. That also preserves federal preemption over local land-use fights.

**Who already does it.** Direct Connect (SOO Green) negotiates with one Class I railroad at a time. Class I railroads lease corridors to fiber firms through in-house real-estate arms. NGI Consulting promotes highway corridors. I found nobody running document AI over historical railroad title at network scale.

**What holds it back.**
- The best corridors belong to the six Class I railroads, which know what they own and price it.
- Transmission still needs state siting approval, an ISO or merchant route to market, and underground HVDC costs.
- Easements are a state-by-state legal question.
- The upside depends on long-distance transmission demand being real, as with SOO Green and its slow progress.

**First proof.** Take one state that has digitised ICC valuation maps or a county deed index online. Have a vision-language model classify instruments for one abandoned corridor whose fee/easement split was already litigated in a reported rails-to-trails takings case (the Court of Federal Claims decisions list the parcels). Kill it if parcel-level accuracy is below 90%, or if no chain of 50+ miles of mostly-fee segments turns up in the state's short-line network.

**Mirror.** None found. GitHub search is restricted in this session, and the FRA rail network and STB dockets are on government hosts.

## 2. Late-stage projects with signed interconnection agreements, priced from study PDFs (5/10)

**The idea.** Upgrade costs depend on the neighbours: when higher-queued projects withdraw, the shared network upgrades are re-allocated ([Simple Thread](https://www.simplethread.com/?p=8265)). Buy projects whose sellers see fatal upgrade costs, but whose costs a model of the contingent-upgrade tree predicts will fall. Do the same for projects whose interconnection (ERIS vs NRIS) is worth more than its label suggests. Then build them, or sell them at notice to proceed.

**The data.** Feasibility, system-impact, facility and restudy reports, affected-system studies, and GIA appendices. These are thousands of PDFs across seven ISOs and dozens of non-ISO utilities, each in its own table format, often redacted (for example [PJM AC1-055](https://www.pjm.com/pjmfiles/pub/planning/project-queues/impact_studies/ac1055_imp.pdf) and SCE's redacted appendices).

**Why ML.** Extracting the cost allocations and the dependencies between upgrades across those formats is a genuine document-AI task. Predicting re-allocation then needs a model on top. Queue lists alone failed our backtest (AUC 0.72 vs a 0.73 lookup), so the open question is whether study text adds signal.

**Bought and price.** Development-stage MW with an IA. Enerdatics counts 44 development-stage trades across the five largest ISOs since January 2025 ([Enerdatics release](https://www.daily-tribune.com/online_features/press_releases/enerdatics-releases-m-a-signals-from-the-queue-mapping-780-gw-in-us-interconnection-queues/article_fe4e4e7f-3c88-59df-9fe1-1d29d2809140.html)). It found buyers already favour projects whose IA risk is resolved. Virginia's 6.6 GW of secured capacity barely trades, because owners hold it for load.

**Who already does it.** Enerdatics ("AI-native deal intelligence"), Nira Energy, Pearl Street, Paces, Enverus and Simple Thread on the data side; dozens of PE and IPP buyers on the asset side. At the top end, Google bought Intersect for about $4.75B ([pv magazine](https://pv-magazine-usa.com/2026/01/02/google-acquires-clean-energy-developer-intersect-power-for-nearly-5-billion/)).

**Why only 5.**
- The extraction layer is being commoditised by vendors, so the mispricing is increasingly visible.
- Signed-IA projects are the most-watched asset class in US power.
- The edge reduces to forecasting re-allocation, which our backtest suggests is weak.

**First proof.** Extract allocated network-upgrade costs from PJM transition-cycle reports at phase 1 and at the final GIA. Test whether a model using study text predicts cost drops of more than 30% better than a lookup by zone and technology.

**Mirror.** `selormdzakpasu/gen_interconnection_queues` (queue lists, reachable via raw.githubusercontent) and the Berkeley Lab mirrors used in `proof/attrition_backtest.py`. I found no mirror of the study PDFs.

## 3. Closed industrial "powered sites": which rights survive (5/10)

**The idea.** Closed paper mills, smelters and chemical plants carry some or all of the following: a high-voltage substation with interconnection, water withdrawal rights, discharge permits, rail, industrial zoning and air permits. AFRY counts more than 10 GW of interconnected capacity across about 220 operating US mills ([DCD, Aug 2026](https://www.datacenterdynamics.com/en/opinions/the-powered-mill-10gw-of-shovel-ready-data-center-sites-is-hiding-in-plain-sight/)). Recent conversions include Aligned's $1.5B campus at Pixelle Chillicothe, Amp Z at Southland Paper (2.1 GW target) and EcoDataCenter at Kvarnsveden.

**The illegible part.** The illegible question is not where the mills are; everyone knows that. It is which rights still exist and transfer. Air permits lapse after extended shutdown. Water rights can be lost through non-use. Interconnection service lapses under ISO retirement rules unless a replacement is filed in time. Discharge permits have renewal clocks. The answers sit in state permit PDFs, water-court filings, ISO deactivation notices and utility dockets, in a different form for each state. ML is needed to read them at national scale. Satellite imagery and thermal time series show whether a plant is "idle" or truly dead.

**Bought, value, realisation.** The site is bought from the mill owner or a liquidator at industrial-land value, and the company develops a powered campus and leases or sells it. The gap between a site whose rights are intact and one whose rights have lapsed is the whole value.

**Who already does it.** AFRY, Amp Z, Aligned, Cloverleaf, Tract, Hut 8, utilities' economic-development teams and every data-centre site broker. The mispricing is already visible at the site level. The only edge is the timing of rights lapse, which is narrow.

**First proof.** For the roughly 40 US mill closures from 2020-2026, read the permit and ISO records and test whether a model predicts which ones became data-centre deals. Then check whether any site with intact rights still sells at land value.

**Mirror.** PUDL (EIA-860 retirements, reachable on S3).

## 4. Bankruptcy-estate hardware bought by a builder (4/10)

**Evidence the asset class exists.**
- Lucid bought Nikola's Coolidge plant and HQ for about $30M at auction ([Drive Tesla Canada](https://driveteslacanada.ca/news/lucid-acquires-nikolas-arizona-facilities-for-30-million)).
- Meyer Burger's US cell and module equipment, about $29M, went to Waaree and Babacomari ([TaiyangNews](https://taiyangnews.info/business/meyer-burger-selling-us-production-assets-to-waaree-babacomari)).
- Lyten took over Northvolt Sweden. Lyten put the assets at about $5B; the price was not disclosed; the deal completed 27 Feb 2026 ([The Local](https://www.thelocal.se/20260108/whats-happening-with-the-american-takeover-of-swedens-northvolt)).
- Volocopter went to Wanfeng, Lilium's plant equipment went to auction, and Agrointelli was sold in parts.

**Data.** Asset schedules, bid procedures, auctioneer catalogues with photos, patent files, and insolvency registers in several languages.

**Why it fails test 2.** These sales are cheap because few bidders can restart a factory, not because the data is unreadable. Every strategic buyer gets the sale notice. AI docket tools (9fin, V7 agents, Stretto) already serve investors. ML helps with sourcing, but the value is unlocked by an operating team.

**Score 4.** It is good as a tactic for a hardware company, but it is not a data moat.

## 5. Surplus interconnection headroom (4/10)

**The idea.** FERC Order 845 (2018) lets plants over 20 MW share unused interconnection with new resources outside the queue ([Pew, Feb 2026](https://www.pew.org/nb/research-and-analysis/articles/2026/02/09/to-harness-power-plants-unused-capacity-states-can-turn-to-surplus-interconnection-service)). Buy peakers that run a few days a year and add storage, solar or load.

**Why it fails test 2.** Headroom is EPA CEMS hourly output set against interconnection capacity. That is a join, and PUDL ships both. LS Power, Vistra, NRG and data-centre developers already buy peakers for exactly this reason. It is a good business but not an ML-unlocked one.

## 6. Underperforming small hydro (4/10)

FERC licence dockets are scanned and decades long. USGS flow time series and EIA-923 generation together show plants producing well below their water. Rye, Eagle Creek and Enel already roll up plants. Relicensing risk sits in docket text, which ML can read, but the pool is about 1,500 small plants and is broker-priced. Score 4.

## 7. Idle solar and battery lines from Chinese and European insolvencies (3/10)

The data is genuinely illegible: judicial-auction listings with Chinese appraisal reports and photos. But the lines are idle because the technology (PERC, older LFP) is obsolete. China restricted exports of some battery and solar process technology in 2025. FEOC rules and tariffs cut the value of the equipment in the US. Score 3.

## 8. Second-hand GEO satellites priced from TLE fuel inference (2/10)

Station-keeping manoeuvres in TLE histories allow an outside estimate of remaining propellant, and that is genuinely ML (see the [physics-informed estimation literature](https://arxiv.org/pdf/2403.19736)). But operators know their own fuel to the kilogram, the pool is a few dozen satellites, and buyers are a handful of operators. Score 2.

## SBIR Lineage under the corrected test: unchanged at 5

The correction removes one objection, that a successor must buy rather than claim. Buying was always the plan, and it is now fine. The test now asks whether ML is essential. It is: matching 220k abstracts and Phase II reports to live requirements is genuine text inference. The binding objections are untouched:
- Phase III is a preference that an agency may decline (*G2 Ops*).
- Older dormant lineages lack data rights.
- Roll-ups and SBIR Advisors already price lineages.
- The April 2026 law makes lineage links public in FPDS, which erodes the data edge.

Score: 5. The kill test in PICK8 still applies.

## Quickly killed in this sweep

- **Used heavy machinery valued from public inspection records.** Condition records for most machines are private: aircraft back-to-birth records, crane inspections, OEM telematics. Where photos are public (IronPlanet, Ritchie Bros), the auction houses already price with ML.
- **Idle pipelines repurposed for CO2 or hydrogen.** The owner converts the pipe itself (Tallgrass Trailblazer, [RBN](https://rbnenergy.com/daily-posts/blog/tallgrass-follows-own-playbook-converting-trailblazer-pipeline-co2-service)). The easement-scope question is real, but it is the same fee-vs-easement problem as in candidate 1 with fewer sellers. I folded it into 1.
- **Idle semiconductor fabs.** There are too few, and the industry knows each one (SkyWater/Infineon Fab 25 and the like).

## Bottom line

Under the corrected test, the sweep's one new idea worth testing is **corridor rights**. It has a truly illegible record (a century of handwritten deeds and ICC valuation maps), a reason only ML can value it at network scale, an asset that trades at freight or salvage value, and a realisation path the company controls (build the line or the fibre on its own corridor). It is a 6, not an 8. Class I railroads own the best corridors, and transmission still needs siting approval and buyers. Its first proof (parcel-level fee/easement classification against litigated rails-to-trails cases) is cheap. It needs a laptop with access to state archives and court sites, which this environment cannot reach.
