# Round 3, lane: nuclear assets, sites and liabilities

Written 15 Oct 2026. Used 20 of 20 WebSearch calls. No reactor or spent-fuel design content. Scores run
from 1 to 10 against the four-part law in ROUND2.md: a cheap first-come claim; public but illegible data
where ML gives an edge; an asset worth far more than the claim; and value that can be realised without
an incumbent's channel.

**Bottom line: no Terranox here.** Nuclear liabilities and sites are real assets worth billions. But
every one of them is owned by a strategic: a utility, Holtec, EnergySolutions, NorthStar, a hyperscaler
or Brookfield. Each changes hands through a bilateral sale or an RFP that the NRC must approve. None is
a first-come claim. The decommissioning pipeline has also mostly dried up, because licence extensions
and data-centre demand have stopped plants from retiring. The best thing to come out of this lane is a
small, cheap proof that would kill or revive thesis 2 (section 2). It is not a company.

---

## 1. Decommissioning-trust arbitrage: score 2/10 (kill)

**Dataset and why it is public.** Licensees must report on decommissioning funding under 10 CFR
50.75(f). Operating plants report every two years (the March 2025 round is the latest) and shutdown
plants report every year. The reports go into NRC ADAMS because the Atomic Energy Act and NRC policy
make licensing records public. Each report gives the trust balance, the cost estimate and cash-flow
projections at an assumed real return (usually 2%). Example: Holtec's 26 March 2026 report, ADAMS
ML26085A513 (https://www.nrc.gov/docs/ML2608/ML26085A513.pdf).

**Pool size**
- Total US nuclear decommissioning trust (NDT) assets were about **$94.7B at end-2024**. That figure
  covers only the 24 sponsors in the survey (81% of capacity), so the implied national total is about
  $110B+. Estimated costs are "over $90B", so the industry as a whole is roughly fully funded. Source:
  NISA 2024 NDT Survey
  (https://www.nisa.com/wp-content/uploads/2025/09/2024-NDT-Survey-NISA-Investment-Advisors-LLC.pdf).
- **The pipeline is close to empty.** There are 94 operating reactors, and subsequent licence renewals
  to 80 years are now routine (Peach Bottom, St Lucie and others). Restarts have taken shut plants out
  of the pool: Palisades restarted in 2025, Crane/TMI-1 is under way and Duane Arnold is under way.
- The only named retirement before 2040 is **Diablo Canyon, 2030**. Even that is soft: the governor
  declined in Aug 2026 to push past 2030 and left the decision to his successor, and licences could run
  to 2044/2045 (https://calcoastnews.com/2026/08/newsom-wont-extend-diablo-canyon-operations-past-2030/).
- From memory, not verified this session: plants already shut are almost all spoken for. Holtec has
  Oyster Creek, Pilgrim and Indian Point 1-3. NorthStar has Vermont Yankee, and ADP (NorthStar plus
  Orano) has Crystal River. EnergySolutions has Kewaunee, TMI-2 and La Crosse. The rest (SONGS,
  Fort Calhoun, Humboldt Bay) are being decommissioned by the utilities themselves. Realistic deal flow
  is therefore **0-3 plants in 15 years**.

**The margins are thinner than the thesis assumes**
- **Indian Point.** Holtec's own filing projects $1.91B of trusts at the start of 2021 falling to about
  **$263M by 2063**, against a $2.3B cost estimate. The surplus is about 14% of the starting balance and
  arrives roughly 40 years later
  (https://www.exchangemonitor.com/holtec-projects-2-3-billion-price-tag-indian-point-decommissioning).
- **Holtec fleet, end-2025.** Trusts total about $2.98B across seven units. At Pilgrim, IP2, IP3 and
  Palisades the remaining undiscounted cost is greater than the trust balance (gaps of $22-99M each).
  The reports close those gaps only by assuming a 2% real return (ML26085A513).
- **Vermont Yankee.** NorthStar received a $602M trust and has spent "almost all" of it. About $8.5M is
  left, with the work 99% done and finishing in 2027, three years early
  (https://vtdigger.org/2026/09/23/vermont-yankee-decommissioning-is-nearly-complete/).
  Even the fastest, best-run fixed-price job leaves almost no trust surplus.
- **Where the money really is:**
  - Fees that the decommissioner bills against the trust.
  - Recoveries from DOE spent-fuel breach-of-contract claims, which travel with the plant.
  - The site itself, which is a call option on new generation (thesis 2).
- Holtec's July 2026 S-1 restructured decommissioning trusts and work into "DEAMCO", outside the IPO
  entity. That suggests the decommissioning line is not what drives its valuation. The IPO, at about
  $10B and $900M raised, was withdrawn in Sep 2026
  (https://www.sec.gov/Archives/edgar/data/0002104277/000119312526301023/d40440ds1.htm;
  https://uanalyze.com.tw/articles/8734155573).

**The ML problem.** Turning the reports into cost-versus-trust gaps by plant is a spreadsheet job, not
an inference problem. Robotics and ML can lower dismantling cost: segmenting reactor internals, mapping
contamination, characterising waste. Owners already buy those capabilities as services from Westinghouse,
Orano, Veolia and Kraftanlagen. Robotics R&D is government-funded in the UK (Sellafield/NDA) and Korea
(KAERI to Victex), so the know-how is not proprietary.

**What would be owned, and rivalry.** The plant, trust and site would be owned through a 10 CFR 50.80
licence transfer. That is a negotiated sale from the utility, approved by the NRC and the state PUC,
with intervenors (Massachusetts, New York and Vermont all fought these). The NRC requires decommissioning
experience and financial qualification. A new entrant with no track record and no balance sheet to
backstop a trust shortfall loses to Holtec, NorthStar or EnergySolutions. Nothing about it is
first-come.

**Ceiling.** Lifetime trust surplus plus fees on 0-3 future plants comes to perhaps **$0.3-1B**. That is
service-sized and fails rule 4.

**Who already does it.** Holtec (HDI), NorthStar, ADP, EnergySolutions and Westinghouse. Atomic Canyon
has the AI-over-NRC-documents position: it is backed by Nvidia and launched NIVA fleet-wide with
INPO/EPRI/NEI in Aug 2026 (https://axios.com/2026/08/18/atomic-canyon-ai-nuclear-nvidia).

**First proof (for completeness).** Pull every 50.75(f) report for 2019-2026 through the ADAMS API and
regress trust surplus at licence termination against the plant's attributes. I expect it to confirm
there is no pool.

**GitHub mirror.** No mirror of the funding reports exists. There are ADAMS API clients:
- `mrdenman-nuclear/nrcadams` (R, updated Aug 2026)
- `bradfox2/nrc-adams-py`
- `seakintruth/NRC_ADAMS_Metadata`
- `TAMU-AESL/NRC-ADAMS-AI` and `hyeongkis/nrc-adams-mcp` (MCP servers)

---

## 2. Nuclear site banking: score 4/10 (best of lane, still fails the law)

**Dataset and why it is public**
- **NRC ADAMS** holds early site permit, COL and FSAR site chapters: seismic, hydrology,
  meteorology, population and geotechnical data, plus environmental reports. These are public as
  licensing records. They are huge, scanned and inconsistent, so they are genuinely illegible.
- **EIA-860 and 860M** list retirements, interconnection capacity and cooling for every unit, and are
  public by statute. The usable mirror is Catalyst Cooperative's PUDL (`catalyst-cooperative/pudl`; the
  `pudl-catalog` repo is archived).
- **ORNL OR-SAGE** has screened siting suitability for the US. Its May 2024 summary is on the Texas
  PUC's FTP (https://ftp.puc.texas.gov/public/puct-info/industry/nuclear/Summary_of_Siting_Analyses_by_Oak_Ridge-MAY2024.pdf).
- **USGS seismic hazard, FEMA flood maps and the HIFLD transmission layer.**

**The ML problem.** The idea is to extract site-characterisation facts from decades of FSARs and ESPs
and fuse them with EIA retirement and interconnection data. That would rank parcels by how much
licensing time is already "pre-paid": an existing ESP, an accepted seismic model, a cooling-water
right, a surviving point of interconnection. Doing that across the whole corpus is a real extraction
problem. But the top ~50 sites are already obvious to every developer: retired nuclear sites,
cancelled units, and big coal plants with cooling water.

**What would be owned.** Fee title or options on land, plus licence or ESP positions acquired through
NRC transfer.

**Rivalry and exclusivity.** There is no first-come regime. The valuable sites come in four kinds, and
each is already held:
1. **Retired nuclear sites.** Decommissioners own them and are developing new nuclear on them:
   - EnergySolutions at Kewaunee, with WEC. It filed a notice of intent with the NRC in Jan 2026 and
     plans an application by June 2028
     (https://www.ans.org/news/2026-01-21/article-7685/energysolutions-confirms-plans-for-new-nuclear-at-kewaunee/).
   - Holtec at Palisades (SMR-300 plus restart) and at Cottam in the UK (a coal site, with EDF and
     Tritax).
   - NorthStar owns the 140-acre Vermont Yankee site.
2. **Cancelled units.** These are sold by RFP or auction:
   - Bellefonte went for **$118M** in 2016 to Nuclear Development LLC. A judge cancelled the sale, and
     TVA withdrew the construction permit in 2021
     (https://www.power-eng.com/nuclear/tva-withdraws-construction-permit-for-abandoned-bellefonte-nuclear-project-after-judge-nixes-sale-to-private-group/).
   - At V.C. Summer 2/3, Brookfield was selected by RFP in Oct 2025 and signed an MOU in Dec 2025. It
     would pay **$2.7B cash** to Santee Cooper, conditional on FID, and Santee Cooper would keep 25%
     (https://www.wistv.com/2025/12/09/santee-cooper-announces-27b-deal-feasibility-study-into-reviving-nuclear-project/).
3. **Retired coal sites.** Utilities own them, together with the interconnection rights (which round 3
   already killed as an option). Examples are TerraPower at Kemmerer/Naughton and the TVA, Duke and
   Dominion coal-to-nuclear programmes.
4. **Greenfield nuclear-ready sites.** These are crowded by funded developers:
   - **Elementl Power.** Google funds three sites of at least 600 MW each with an offtake option;
     Elementl targets 10 GW by 2035
     (https://wnn.world-nuclear.org/articles/google-to-fund-elementl-to-prepare-three-nuclear-power-sites).
   - **The Nuclear Company.** $51M Series A to develop multi-GW sites
     (https://techcrunch.com/2025/05/16/the-nuclear-company-raises-51m-to-develop-massive-reactor-sites).
   - Also Deep Fission (TX/UT/KS), Last Energy (TX), Fermi America (Amarillo) and X-energy/Dow
     (Seadrift).

**Ceiling.** A real site is worth hundreds of millions to several billion:
- Bellefonte: $118M.
- V.C. Summer: $2.7B, conditional.
- Talen's Susquehanna campus sold to AWS for $650M in 2024 (from memory, not re-verified this session).

That is asset-sized. But entry means paying near those prices to a strategic seller who has read the
same ADAMS docket.

**First proof (cheap; it would revive the idea if it surprised).**
1. Take EIA-860 from PUDL.
2. List every retired or planned-retirement coal or nuclear unit of at least 400 MW with surface water
   cooling, about 150 sites.
3. Cross-reference each against announced redevelopment: press releases, NRC letters of intent, and
   hyperscaler deals.

If more than 30% of the top 50 have no announced plan *and* the owner is a non-utility (an IPP or a
bankrupt estate) that might sell an option, the thesis lives. I expect fewer than 10% to qualify.

---

## 3. Other find-and-own plays in nuclear

| Play | Public data | Owned thing | Why it fails | Score |
|---|---|---|---|---|
| DOE Standard Contract damages claims | Court of Federal Claims dockets; DOE IG audits. **$11.1B paid; $37.6-44.5B remaining liability (FY2024)** (https://morganlewis.com/blogs/upandatom/2024/12/us-spent-fuel-storage-liability-increases-while-other-countries-develop-geologic-repositories) | Claim against the US | The claim belongs to the contract holder and moves only with the plant. The Anti-Assignment Act (31 USC 3727) blocks buying claims before they are allowed. Outcomes are already modelled by owners and DOJ. | 2 |
| Dormant COLs and ESPs (e.g. Turkey Point 6/7, Fermi 3, North Anna 3, Clinch River ESP, PSEG ESP; from memory) | ADAMS | Licence, acquired through 50.80 transfer | Utilities hold them as their own options and are now reviving them. Transfer is negotiated, not first-come. | 3 |
| Cancelled-plant components and used equipment for restarts | ADAMS, auction notices, DOE surplus | Hardware | The restart pool is exhausted (Palisades, Crane, Duane Arnold). Bellefonte has been stripped. Components are obsolete or need requalification. The market is small and Curtiss-Wright, Westinghouse and others serve it (obsolescence was already killed). | 2 |
| DOE land for AI and energy parks (INL, Oak Ridge, Paducah, Savannah River) | DOE RFPs | Lease | Leases are competitive RFPs that favour hyperscalers. Nothing to read better. | 2 |
| Licensed LLRW disposal capacity (Clive, Andrews) | NRC and Agreement State records | Licence | A duopoly asset, but a new licence takes about 10 years and is politically blocked. The data holds no edge. | 3 |

---

## Scores

| Thesis | Data illegible | ML edge | Exclusive claim | Ceiling | Uncrowded | Overall |
|---|---|---|---|---|---|---|
| 1 Decommissioning-trust arbitrage | 4 | 2 | 2 (50.80 transfer, negotiated) | 2 | 2 | **2/10** |
| 2 Nuclear site banking | 7 | 4 | 2 (auction or bilateral) | 7 | 3 | **4/10** |
| 3a DOE fuel damages | 5 | 3 | 1 | 7 | 3 | 2/10 |
| 3b Dormant COLs and ESPs | 6 | 3 | 2 | 5 | 3 | 3/10 |
| 3c Used and cancelled equipment | 5 | 3 | 4 | 1 | 3 | 2/10 |

**Lesson.** In nuclear, the regulator *is* the incumbent's channel. Every asset passes through an NRC
licence transfer and a state PUC, and that rewards track record and balance sheet, not reading the
data first. That breaks parts (1) and (4) of the law. Dhruv's nuclear edge is better spent as the
operator on the buy side of a site deal than on a data-first claim.
