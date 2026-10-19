# Sweep L4: drop "public bodies reprice to market or keep the best" (2026-10-19)

## Verdict

Nothing survives. With L4 dropped, the best total is **14/25**, for thin public-land auctions where an informed applicant nominates powered or industrial parcels. No idea reaches C2 >= 3 and C4 >= 3 at the same time, and the top three all failed adversarial checks.

Dropping L4 changes the rest of the rubric in three ways:
- **Thin tenders exist, but they clear at the appraised minimum.** Arizona's sole-bidder sales (Novva, Biscuit Flats, Blandford) all went at the minimum bid. When bidders do compete, the price runs up to about 3.6x the appraisal (Superstition Vistas). So winning without competition gives at most a 1-3x spread (C2 of 1-2), not 10^3x.
- **"Know which lots are worth more" fails on L2.** Value is already legible: MHz-pop for spectrum, comps-based appraisals for land, and NREL/ANU atlases plus agency pre-feasibility for pumped hydro.
- **"Hold the non-transferable right and build" fails on the standing rules.** It turns the idea into a bespoke-build developer (L1, C1), on a rung that Tract, T-Mobile or the big IPPs already hold (L6).

**Which law kills instead:** L2 first, then L3 (the clearing price, not the seller, now carries the hope value), L1/C1 for the operate-it variants, and L6 everywhere.

## Method
- **Old ideas:** grepped `research/converge/PICK9.md` (round 5 "fifth law" table) and `gold/round4/5/6_results.json` and `scored_263.csv` for ideas killed mainly by public-body behaviour. 14 were rescored with L4 dropped and every other law and rule kept.
- **New ideas:** 20 generated that only make sense once L4 is dropped.
- **Checks:** the top 3 were checked with web search.

**Rescoring rule:**
- **C4:** may now reach 3 when the right comes from a thin tender or an RFP the company can win as the best-informed bidder. It stays at 1-2 when the value signal is legible (L2).
- **C2:** scored on the spread the informed winner actually captures over the clearing price. It is not scored on the gap to the nominal fee.

---

## 1. Old ideas rescored (L4 dropped)

| # | Idea (source) | Old score | New /25 (C1-C5) | Why it moved, and what now kills it |
|---|---|---|---|---|
| 1 | Large-load data-centre site on state trust land (R5 #4, R6) | 15 / 11 | **14** (2,2,3,3,4) | **Moved:** C4 1 to 3, because AZ commercial auctions are often sole-bidder (Novva, Biscuit Flats, Blandford). **Kills:** the minimum bid is an appraisal at proposed use (Novva paid about $380k/acre, data-centre value), so C2 is about 2. Power, not land, is the proof (L1/L3: utility tariffs). Tract holds the rung (L6). |
| 2 | Closed-loop pumped storage via FERC preliminary permits (R5 #1) | 14 / 12 | **12** (2,2,3,2,3) | **Moved:** non-transferability is now acceptable because the company is the operator. **Kills:** operating means a $1-3B bespoke build (L1, C1 = 2). The NREL closed-loop atlas (about 15k pairs) makes the screen legible (L2). Early-stage sales run about C$50k/MW upfront, only 3-8x on proving capital. |
| 3 | Old-dam-site pumped hydro on Crown land, NSW/Qld (R5 #2) | 13 / 12.3 | **12** (2,2,3,2,3) | **Moved:** you can now win the WaterNSW tender as the informed bidder. **Kills:** WaterNSW pre-screened all 41 dams and published the shortlist (Blowering, Burrendong, Hume). The tender is not thin (65 opportunities, 24 progressed), and the build is bespoke. |
| 4 | Philippine DOE wind/solar service contracts (R5 #3) | 13 / 12.3 | **11** (2,2,2,2,3) | **Kills:** the GEA rounds are not thin. GEA-3 pumped hydro drew 6.95 GW against 4.25 GW; GEA-4 drew 111 bids and 88% subscription. Wind and solar resource is in public atlases (L2), and the winner must build (C1). |
| 5 | Crown land wind licences, Newfoundland/BC (R5 #5) | 13 / 11 | **11** (2,2,3,2,2) | **Moved:** winning the Newfoundland scored call is now allowed. **Kills:** the call is scored on construction capability, so a discovery startup loses to IPPs. Resource is legible, and value comes from First Nations equity plus offtake. |
| 6 | BLM solar ROW outside SEZs (R5 #6) | 13 / 10.7 | **9** (2,2,2,2,1) | **Kills:** a policy freeze (Interior's 2025 capacity-density order and secretary review) plus the OBBBA credit sunset. The ladder is dead regardless of L4. |
| 7 | Fixed-rate state-trust wind/solar leases (R5 #13) | 12 | **12** (2,2,3,3,2) | **Moved:** NM auctions may be thin. **Kills:** Pattern paid $9.3M for about 148k acres (about $63/acre), and Pattern is itself the informed bidder (L6). The spread to a dev-stage site is about 2-10x and is legible from transmission plans (L2). |
| 8 | FERC permits on non-powered federal dams (R5, R6) | 11 / 11 | **10** (2,1,3,2,2) | **Kills:** the retrofit costs $5-12k/kW (bespoke build), and a built asset is worth about $2-3M/MW. C2 is about 1. |
| 9 | Chilean maritime concessions for desal (R5 #8) | 13 / 10.3 | **11** (2,2,3,2,2) | **Moved:** discretionary grant now acceptable. **Kills:** Law 21.813 imposes a use-it-or-lose-it start within 2-4 years. Buyers (miners) site intakes themselves. |
| 10 | Federal comm-site leases, USFS/BLM (R5) | 12 | **11** (2,2,2,2,3) | **Kills:** carriers decide which ridges they need from private RF data (L2 for them). Value comes from the anchor tenant, not the site. |
| 11 | Zombie / rebanded spectrum (R1 #53) | 10 | **12** (2,3,2,2,3) | **Moved:** thin FCC auctions now count. **Kills:** see check B. Value is legible in MHz-pop, and the end buyer bids directly. |
| 12 | Retired fossil sites, surplus interconnection (R4, R6) | 13 / 11 | **11** (2,2,2,1,4) | **Kills:** public-power sellers running RFPs are now acceptable, but retirement lists and ISA MW are legible fields (L2) and the asset is heavily shopped. |
| 13 | DOE national-lab patent options (R5) | 12 | **12** (2,2,3,3,2) | **Moved:** fair-value licence clawback now acceptable. **Kills:** the proof is a prototype build (L1/C1), the lab negotiates after seeing the results, and nothing is venture-scale per licence. |
| 14 | Surplus military aviation lots, DLA/GovPlanet (R4) | 12 | **11** (2,3,2,2,2) | **Moved:** thin GovPlanet lots now count. **Kills:** overhaul and AC 20-142 eligibility are the proof (physical). Brokers are crowded and the business is not $1B. |

**Takeaway:** dropping L4 lifts C4 by about 1-2 points on roughly half the old ideas. It lowers C2 almost everywhere, because the winning bid or appraisal absorbs the hope value. The old round-5 ideas mostly net to the same score or lower.

---

## 2. New ideas that only make sense with L4 dropped (/25)

| # | Idea | C1 | C2 | C3 | C4 | C5 | Total | Main killer |
|---|---|---|---|---|---|---|---|---|
| N1 | **Thin-auction powered land.** Be the informed applicant on state-trust, GSA and TVA land auctions, nominating parcels whose appraisal misses latent grid headroom (ML on FERC 715, utility hosting maps and scanned load studies). | 2 | 2 | 3 | 3 | 4 | **14** | Check A: sole bidders pay the appraised minimum. Appraisals do lag (Superstition Vistas went at 3.6x appraisal), but only when bidders compete. Paces and LandGate sell the grid signal (L2), and Tract holds the rung (L6). |
| N2 | **Thin FCC auction informed bidder.** Win rural county licences cheaply, then sell or lease to carriers or private LTE users. | 3 | 2 | 1 | 2 | 2 | **10** | Check B: Auction 108 cleared under 2c/MHz-pop against EBS comps of 3-33c, but T-Mobile won 7,154 of 7,872 licences itself. Value is legible (L2), and the auction pipeline is now large national bands. |
| N3 | **Public-reservoir pumped hydro tenders worldwide** (WaterNSW, Philippine GEA-3, Indian state PSH allotments, Brazil). | 2 | 2 | 3 | 2 | 3 | **12** | Check C: not thin, pre-screened by the agency, and a bespoke build. |
| N4 | **Emerging-market hydro concessions** (Nepal, Georgia, Central Asia, Africa), with ML on scanned Soviet-era hydrology. | 2 | 2 | 3 | 3 | 2 | **12** | A $2-3M/MW bespoke build (L1/C1). Dev rights trade at only 3-10x, plus political risk. |
| N5 | **USFS / state timber sales.** LiDAR ML beats the cruise estimate on volume and grade. | 3 | 1 | 2 | 3 | 1 | **10** | Cruise error is 10-20%, so C2 < 1.5x and the business is not $1B. |
| N6 | **Landfill-gas rights tenders** run by counties for RNG. | 2 | 2 | 2 | 2 | 3 | **11** | EPA GHGRP waste-in-place data is legible (L2). Archaea/BP, OPAL and Ameresco hold the rung (L6). |
| N7 | **State DOT highway corridors leased for HVDC or fibre** (thin, operator). | 2 | 3 | 1 | 2 | 3 | **11** | No discovery problem: corridors are public. Value comes from transmission build and offtake (C1). |
| N8 | **Spain/Portugal "just transition" node capacity tenders** at retired coal nodes. | 2 | 2 | 1 | 2 | 3 | **10** | Scored on jobs and local criteria, not information. ML is irrelevant. |
| N9 | **ITU satellite filings via thin administrations** (orbital priority). | 2 | 3 | 1 | 2 | 2 | **10** | Bring-into-use milestones force you to launch. ML is not core, and rule-making is fragile. |
| N10 | **Government-seized crypto-mining sites with power contracts**, repurposed for AI (Paraguay, Kazakhstan, US Marshals). | 2 | 3 | 2 | 2 | 2 | **11** | A handful of lots, and power contracts are usually voided on seizure. Too small. |
| N11 | **Indian state solar-park / pumped hydro allotment** to the informed bidder. | 2 | 1 | 1 | 1 | 3 | **8** | Hyper-competitive, with record-low tariffs. |
| N12 | **CBRS PAL / rural licence aggregation** for industrial private networks (mines, ports). | 2 | 2 | 1 | 2 | 2 | **9** | GAA is free, so the licence carries little scarcity value. Legible. |
| N13 | **GSA disposal of ex-military bases with 100+ MW substations.** | 2 | 2 | 2 | 3 | 3 | **12** | Few lots a year. The DOE/DoD AI-site RFPs (Idaho, Oak Ridge, Paducah, SRS) are heavily contested by hyperscalers. |
| N14 | **Thin-tender minigrid concessions** (Nigeria, DRC): win the best villages with ML on demand. | 2 | 1 | 2 | 3 | 2 | **10** | An operator business with utility returns. The prize is grant-driven. C2 is about 1. |
| N15 | **Chile DGA water-rights auctions** in contested basins (sold to H2, mining and data centres). | 2 | 3 | 2 | 3 | 2 | **12** | Proof needs hydrogeology (drilling, against the standing rule). The 2022 reform makes rights temporary, and buyers know the basins. |
| N16 | **University and national-lab exclusive licences**, with ML triage of 100k dormant patents. | 3 | 2 | 2 | 3 | 2 | **12** | The proof is a prototype build. The licensor renegotiates on success. Base rate is poor. |
| N17 | **Port and airport ground concessions in small markets** (fuel farms, cold chain). | 1 | 2 | 1 | 2 | 2 | **8** | Infrastructure PE, with no discovery core. |
| N18 | **BLM / state geothermal and CCS pore-space lease sales.** | - | - | - | - | - | **excl.** | Drilling (standing rule). |
| N19 | **Indian coal-block and mineral auctions** read through scanned GSI reports. | - | - | - | - | - | **excl.** | Prospecting-adjacent and Terranox-like (standing rule). |
| N20 | **Japan, Korea and Taiwan offshore wind rounds** as the informed bidder. | 1 | 2 | 1 | 1 | 3 | **8** | Mega-consortia only. Mitsubishi's 2025 exit shows the bid risk. |

---

## 3. Adversarial checks on the top 3

### A. Thin-auction powered land on state-trust and federal surplus (N1 / old #1), 14/25 to dies

**Bid counts are thin, but the price is set by appraisal:**
- Novva bought 165 acres in Mesa for **$62.7M (about $380k/acre). Novva's CEO was the sole bidder** (https://baxtel.com/data-center/3636).
- About 2,340 acres at I-17 and Carefree Highway sold to Biscuit Flats Dev as the **only bidder, at the $56.28M minimum** (about $24k/acre).
- Blandford Homes in Mesa was the **applicant and only bidder at the $37.85M minimum** for 114.7 acres (https://www.connectcre.com/stories/az-state-land-auction-drawing-heavy-hitters/; https://ktar.com/arizona-news/gilbert-builder-wins-state-land-auction-with-plans-to-build-more-than-400-homes).

**Real step-up:**
- Appraisals do lag the market when bidders compete. Superstition Vistas was appraised at **$68M and sold for $245.5M with 4 bidders (3.6x)** (https://www.roselawgroup.com/?p=8185).
- So an informed sole applicant captures at most about 1-3.6x on land, which is C2 = 1-2.
- Nominating a parcel publicly notices it, which invites the 4-bidder outcome on exactly the parcels worth most.

**Who already does it:**
- Paces sells the grid-capacity signal ($12.9M raised; its CEO calls it "a nationwide land grab... for the sites which have the most grid capacity") (https://www.datacenterdynamics.com/en/company/paces/).
- **Tract controls 25-30k+ acres** and holds the rung (https://www.globenewswire.com/de/news-release/2025/05/07/3076274/0/en/TRACT-CLOSES-ACQUISITION-OF-1-515-ACRES-IN-CALDWELL-COUNTY-TEXAS-FOR-MULTI-GIGAWATT-DATA-CENTER-TECHNOLOGY-PARK.html).
- GSA sales are not reliably thin either: a 2017 DC sale drew 14 registered bidders and 74 bids (https://origin-www.gsa.gov/about-us/newsroom/news-releases/gsa-officially-announces-31-million-auction-sale-of-surplus-federal-property-in-the-district-of-columbia-03012018).

**Verdict: dies on L2 + L3 + L6.** The proof that matters (a utility load commitment) is the real gate, and the utility prices it through large-load tariffs.

### B. Thin FCC spectrum auctions as the informed bidder (N2 / old #11), 12/25 to dies

- **Thin and cheap:** Auction 108 offered 8,017 rural county 2.5 GHz licences, with 82 qualified bidders and 63 winners. Gross proceeds were **$427.8M, under 2c/MHz-pop**, against a $0.10-0.20 pre-auction estimate (https://auctiondata.fcc.gov/public/projects/auction108; https://techblog.comsoc.org/2022/08/29/fcc-auction-108-2-5-ghz-ends-with-total-proceeds/).
- **Secondary comps are higher:** pre-2019 EBS leases ran **3-14c/MHz-pop**, and Sprint's EBS cost about **33c/MHz-pop** (https://www.fierce-network.com/5g/could-c-band-auction-set-price-t-mobile-will-pay-ebs-licenses). That suggests an apparent 2-15x gap.
- **The gap went to the end buyer, not to an intermediary.** **T-Mobile won 7,154 of 7,872 licences for $304M** (https://tvtechnology.com/news/t-mobile-spends-dollar304m-on-25-ghz-spectrum). The licences were the "holes in the Swiss cheese" of T-Mobile's footprint, worth a lot only to T-Mobile, so there was no informed edge to win.
- **The signal is not illegible.** Value is population x MHz x encumbrance, all legible (L2), so ML adds about nothing (standing rule).
- **The pipeline is not thin.** Auction authority returned in 2025 for large national bands (upper C-band), where the big carriers dominate.

**Verdict: dies on L2 + the ML rule.** It is also too small: the whole thin auction was $0.43B.

### C. Public-reservoir pumped hydro tenders (N3 / old #2-3), 12/25 to dies

- **Not thin, and the agency reads its own files:**
  - WaterNSW ran pre-feasibility on all 41 dams and shortlisted Blowering, Burrendong and Hume itself (https://www.waternsw.com.au/news/media-releases/2025/waternsw-shortlists-3-more-sites-for-pumped-hydro).
  - The earlier round found 65 commercial opportunities and progressed 24 (https://www.pumpindustry.com.au/landmark-pumped-hydro-clean-energy-project-for-nsw).
  - Philippine GEA-3 drew **6,950 MW of pumped hydro offers against 4,250 MW** (https://www.ess-news.com/2025/02/13/philippines-green-energy-auction-heavily-oversubscribed-with-nearly-7-gw-of-pumped-hydro-bids/).
  - GEA-4 drew 111 bids (https://www.pv-magazine.com/2025/09/05/philippines-renewable-auction-awards-9-4-gw-short-of-10-6-gw-goal/).
- **Real step-up:** AGL agreed **A$31M for Kanmantoo's 250 MW rights (about A$124k/MW)**, and the deal was later scrapped (https://esdnews.com.au/agl-secures-right-to-turn-mine-into-pumped-hydro/). TransAlta paid about C$50k/MW upfront for Tent Mountain (deep dive in `research/converge/gold/round5_deep_closed-loop_pumped_storage_sit.md`). That is 3-15x on proving capital.
- **Base rate:** about 3 of 67 US pumped-storage projects in the pipeline reached FERC authorisation (DOE 2021 market report). The failures are commercial, not technical, so the ML lever is about 1.2-1.5x.

**Verdict: dies on L1/C1 (bespoke $1-3B build), L2 (atlases and agency pre-feasibility) and L6 (ACEN, AGL, IPPs).**

---

## 4. What kills each class once L4 is gone

| Class | Killer instead of L4 |
|---|---|
| Thin land auctions (trust land, GSA, TVA) | L3 via appraisal minimums, L2 (comps, grid data sold by Paces and LandGate), L6 (Tract) |
| Spectrum and orbital | L2 (MHz-pop is legible), the end buyer bids directly, the ML-essential rule |
| Pumped hydro, hydro, wind and solar tenders | L1/C1 (bespoke build), L2 (atlases), L6 (IPPs) |
| Non-transferable operator rights (FERC permits, concessions) | Turn into a developer business, where the proof is the build (C1 <= 2) |
| Timber, minigrids, landfill gas | C2 < 3x, too small |

## 5. Single most interesting finding

Thin public auctions really do leave money on the table:
- Auction 108 cleared at under 2c/MHz-pop against 3-33c secondary comps.
- Arizona sole bidders pay only the appraised minimum, while competed parcels go for up to 3.6x appraisal.

But in each case the surplus went to the **end user bidding directly** (T-Mobile, Novva, homebuilders), not to an intermediary with better information. When the end buyer can bid in the public auction itself, there is no rung to discover and resell. Terranox works because the end buyer (a miner) does not stake ground at the proof stage.
