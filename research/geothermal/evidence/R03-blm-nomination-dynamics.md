# R03: BLM geothermal nominations: who nominates, who wins, information leakage, permitting clock, and an ML-first land strategy

**Method note.** The shared WebSearch budget for this run was used up before this task started. This file therefore rests on documents fetched directly: eCFR text via Cornell LII, Federal Register API records and govinfo full texts, BLM sale notices and nomination calls, and GAO-26-108040. It also uses the parsed BLM bid reports already gathered in sibling files R01 and Z04, which I cross-checked where I could. I could not find any primary source that names a nominator who lost their own parcel. That evidence is inferential and is labeled as such. Anything not sourced is marked (unverified).

---

## 1. The mechanics: how a federal geothermal right is born

| Step | Rule / fact | Source |
|---|---|---|
| Who can nominate | Any qualified company or individual, on Form 3203-1 or online in NFLSS. BLM can also add lands on its own initiative. | 43 CFR 3203.5, 3203.10 |
| Nomination size | One lease per nomination, **≤5,120 acres**. Protracted sections must be nominated whole. | 43 CFR 3203.10; NV 2028 call |
| Cost to nominate | **$150 per nomination plus $0.14/acre**, nonrefundable. It was $145 + $0.14 in the 2025 notice. | NV nominations call (Jul 2026); NV Oct-2025 sale notice |
| Sale cadence | BLM must hold a sale **at least every 2 years** in any state with pending nominations. Nevada runs one every year. | 43 CFR 3203.13 |
| Pipeline lag | The Nevada nomination deadline for the **Oct 2028** sale is **30 Jun 2027**, about 16 months ahead. | Geo_Nominations_Due_2028.pdf |
| Public notice | The sale notice with the full parcel list is posted **≥45 days** before the sale. Before that, a public comment/NEPA period publishes **parcel lists and maps** about 4 months ahead. The 2026 NV comment period opened 24 Jun 2026 with 84 parcels and 268,251 acres, for a 20 Oct 2026 sale. | 43 CFR 3203.14; BLM NV announcement Jun 2026 |
| Award | Online ascending English auction (EnergyNet through 2025, Efficient Markets in 2026), one hour per parcel, sequential close. The **highest bid per acre wins** and bids are binding. The nominator gets **no preference right**. | 43 CFR 3203.15; NV 2025 notice |
| Floor | $2/acre minimum bid. Rental is $2/ac in year 1, $3/ac in years 2-10 and $5/ac after that. Primary term is 10 years. | NV 2025 notice |
| Unbid parcels | Open noncompetitively for 2 years. Offers filed on the first business day after the sale are treated as **simultaneous and drawn at random** (43 CFR 1822.17). After that it is first-come. The cost is a $520 fee plus $1/ac. | 43 CFR 3204.5; NV 2025 notice |
| Holding cap | **No more than 51,200 acres held "directly or indirectly" in any one state.** An owner is charged its proportionate share of entities in which it holds more than 10%. | 43 CFR 3206.13; NV 2025 notice |
| Keeping the lease past year 10 | Spend **$40/acre** in qualifying work (TG wells, geophysics, geochemistry, drilling), pay in lieu, or produce in commercial quantities. That earns a 5-year extension, and a second 5 years is possible. | 43 CFR 3207.10-3207.11 |

**Does nominating reveal your target? Yes, the land does; no, the name does not, as far as the public record shows.**

- BLM sale notices, comment-period announcements and the noncompetitive "available parcels" list publish exact legal descriptions (township/range/section). None of these documents names the nominator. The Jun-2026 NV announcement, the Oct-2025 NV notice and the Sep-2026 two-year-window list all checked out this way.
- Whether a nominator's identity can be obtained through FOIA is **(unverified)**. The 2024 oil-and-gas leasing rule says BLM releases "names and addresses" of nominators and lessees "to the extent allowed by the Privacy Act", and that bidder names stay confidential only "until the end of the sale" (89 FR, doc 2024-08138). That rule excludes geothermal, but it signals BLM's general posture: identities are not secret by right.
- After the sale, BLM publishes **every bid** with bidder name and $/acre in the "All Bids" reports. This means a loser's valuation becomes public. Zanskar's $231/acre bid on a Pumpernickel step-out became a public price signal (Z04).
- What a nominator gives away is therefore the **location and timing** of its interest, about 4-16 months before it can win. Because the nominator has no preference right, anyone who reads the parcel list can outbid it.

## 2. Who is nominating, and how crowded is it

GAO-26-108040 (Sept 2026) is the best primary dataset:

- Nominated acreage went from **~25,800 acres in 2020 to >1,000,000 acres in 2025**. Over 2019-2025, **3.385M acres** were nominated and 2.108M were processed (62%).
- Of the processed acreage, 1.245M acres were offered at sale and 862k were found unavailable. **~87% of offered acres were leased.**
- **~27% of nominated acres were rejected as duplicates.** Two or more parties are independently nominating the same ground, so signal collision is already common.
- About 20% were rejected because the land-use plan does not allow geothermal, and ~14% because DoD withheld consent near installations in CA and UT.
- State surges: New Mexico went from 4,468 acres (2024) to **>400,000** (2025). Idaho went from 280 acres (2020) to **>180,000** (2025).
- Revenue was **$39.4M from 19 sales in 2020-25**, $24M of it in 2025. Two 2026 sales cleared at $701/ac (NM) and **$1,207/ac (UT)**, together more than $41M. Active leases rose from 599 to 749 between Mar 2025 and Mar 2026 (+25%).

The bidder set, parsed from the BLM All-Bids reports in R01 and Z04:

- Developers: Ormat, Invenergy/"Ivenergy Energy Transition LLC", Zanskar, XGS, Raser, Baseload.
- A growing group of **opaque LLC and landman vehicles**: Buffalo River Minerals (Dover, DE; 28 NV parcels in 2024, plus the $344/ac UT 2025 top bid), Percheron Professional Services (Katy, TX; the $410/ac NV record), FLHN 1 LLC ($408/ac), Lithos48, Cordillera, Skyladder Capital, Chinati Minerals and Dudley Land.
- Who stands behind these entities is (unverified). The sale notice explicitly requires anyone "bidding for more than one party" to register a separate bidder number per principal, so **nominee bidding is lawful and normal**.

## 3. Do nominators lose? Evidence (inferential)

There is no primary source tying a named nominator to a specific lost parcel, because nominator names are not published. The available evidence:

1. **Duplicate nominations (27% of acreage).** Wherever two parties nominate the same block, at least one of them must either lose or pay up at auction.
2. **Zanskar's one-dollar losses, from the BLM All-Bids reports (Z04).**
   - NV-2024-10-2049 (Lander Co.): Invenergy $112 against Zanskar $111. Zanskar won the adjoining 2048 parcel at $61 over Invenergy's $60.
   - NV-2025-10-2143 (Humboldt Co., inside the Pumpernickel block): **Lithos48 $232 against Zanskar $231 (~$408k)**. This came about a month after Zanskar publicly announced Pumpernickel. Zanskar had bought the step-out acreage next door at **$2/ac in Nov 2023**, so the same ground repriced ~116x.
   - Whether Zanskar nominated those parcels is (unverified). Either way, a clustered, step-out nomination pattern next to an announced discovery drew bidders who were following Zanskar's lead.
3. **Floor-price wins when nobody else is looking.** In Nov 2023 Zanskar won **6 parcels / 16,720 ac, all at $2/ac**, each with a single bid (Z04). Nominating works when the parcel looks unremarkable to the crowd.
4. **Historic precedent of the nominator winning, slowly.** Ormat nominated the Don A. Campbell (blind, mining-hole-identified) land in **2001** and won it at auction in **2007**. That plant is now 42 MW (NREL "Mining G.O.L.D.", Levine et al. 2022, via L16). Ormat also won the McGinness Hills leases at auction in Aug 2007 after legacy mining holes found 190 °F water. The nominator *can* win, but the lag is long.
5. **Market bimodality** (R01): in NV 2025 the median winning bid was $3.50/ac and 37% of parcels cleared at the $2 floor, yet the maximum was $410/ac. Most nominations reveal nothing anyone else acts on. A few, on "consensus" ground, get bid up 100-200x.

**Takeaway.** Nominating is a leak only where your target falls inside the crowd's prior: near known fields, announced discoveries, Fervo/Cape or the play-fairway maps. On genuinely blind ground the nominator usually wins at the floor.

## 4. Pre-sale clock and backlog

GAO-26-108040, average days from nomination to sale for BLM-managed land (as of Feb 2026):

| State | Avg days | Acres offered | % processed |
|---|---|---|---|
| Nevada | **335** | 998,669 | 75% |
| New Mexico | 256 | 8,455 | 23% |
| Utah | 872 | 82,168 | 77% |
| Idaho | 932 | 94,998 | 48% |
| California | 1,017 | 22,445 | 53% |
| Oregon/Washington | **1,595** | 5,235 | 100% |
| All BLM | **455** (median 328) | 1,211,971 | 65% |

- Forest Service and Reclamation lands average **1,098 days** (Fishlake NF: 1,959).
- The **backlog is ~1.277M acres under review**, ~857k of them submitted in 2025. Another ~148k acres are deferred, mostly over sage-grouse litigation.
- **Staffing is the binding constraint.** One Nevada office is 60% vacant (1 of 6 geologists in post). Nevada has stretched its nomination review expectation from ~11 to ~15 months, and BLM paused its Jan-2025 workforce plan as of May 2026.
- Leasing NEPA usually tiers to the **2008 Geothermal PEIS** through DNAs or EAs. Through Nov 2013, 376 parcels were offered after the PEIS, 295 of them cleared via DNA (Young et al. 2014).

## 5. Post-lease permitting: what has changed in 2025-2026

- **New BLM geothermal exploration CX, effective 28 Apr 2026** (91 FR 22848, doc 2026-08235).
  - It covers approval of a **Notice of Intent to conduct geothermal exploration** under 43 CFR 3250, provided the work involves **≤10 acres total surface disturbance**, no direct testing of the resource or production, and reclamation of the disturbance.
  - It sets **no limit on well count or depth**, and TG wells and core holes are named in the substantiation.
  - It was substantiated on 28 geothermal EAs plus 20 oil-and-gas EAs with FONSIs, none with unanticipated effects.
  - An extraordinary-circumstances review is still required (43 CFR 46.215).
- **BLM adopted 65 other agencies' CXs, effective 2 Sep 2025** (doc 2025-16759). They include:
  - Navy 32 CFR 775.6(f)(39), pre-lease geothermal/geophysical exploration;
  - USFS 36 CFR 220.6(e)(8), geothermal investigations of ≤1 year;
  - DOE B3.7, infill exploratory/injection wells *within an existing field*;
  - USGS 516 DM 9.5(G), test/exploration drilling.
- **In use already.** BLM Cedar City approved up to 10 TG holes at Lund North (UT) under CX documentation on 13 Aug 2026.
- **Legacy rules cleaned up.** Direct final rules of 17 Jul 2025 (docs 2025-13404, -13405, -13394, -13393, -13392) removed obsolete EPAct-2005 transition provisions. They made no substantive change to nominations.
- **Historical baselines** (Young et al. 2014, GRC Trans. 38):
  - median NEPA time is **CX/DNA 1-2 months, EA 10 months, EIS 25 months**;
  - GAO (2013) found Nevada permits took 1-4 years.
  - DOE's Liftoff report puts exploration under a CX at 2-4 months, and says a lease sale "can take over 4 years" in slow offices.
- **Drilling-permit throughput** (GAO-26-108040): approved geothermal drilling permits went 7 (2019) → 22 (2023) → **68 (2024)**, of which NV 38 and UT 29. BLM has **no time-frame goals and no unified tracking**, and GAO recommends both.
- **Overall clock:** DOE cites **8-10 years** from start of exploration to revenue (GAO-26-108040).

**What this means for timing.** The slowest steps are now (a) nomination to sale, at 1-4+ years depending on the state, and (b) utilization/EA for production. Shallow exploration on a held lease is now on a CX track of weeks to months. Proving up a lease cheaply is therefore faster than getting the lease in the first place.

## 6. Implications for an ML-first land strategy

1. **Score everything, not just what you nominate.** Each year 1M+ acres of *other people's* nominations are published, NEPA-cleared and offered. An ML ranker can bid opportunistically on the parcels others nominated but mis-priced, which reveals nothing about your own targets. In NV 2025, **27 unbid parcels (97,120 ac) drew only one noncompetitive offer**. About 92k acres of already-cleared land was available at $1/ac on a random-draw basis (R01).
2. **Hide your signal in noise.** Nominating is extremely cheap: 100,000 acres costs about $14k plus $150 per 5,120-acre nomination, roughly $17k in total (calc).
   - Nominate whole fairways and decoy blocks, and stay away from tight clusters around one anomaly. Large nominations of plausible-but-cool ground cost little and raise the noise floor.
   - Use a separate bidder number per entity, as the notice allows. That must stay within the 30 USC 195 anti-scheme rules and the indirect-holding cap.
3. **Lock up a fairway before any public data event.** That means before a TG-hole permit filing, a Nevada Division of Minerals permit, a press release, a DOE award or a paper. Pumpernickel shows that disclosure reprices adjacent land ~100x within weeks. Sequence the steps:
   - quiet desktop ML;
   - non-permitted sampling, such as existing-well geochemistry (L15);
   - nominate the full block;
   - win at or near the floor;
   - only then drill TG holes under the new CX;
   - then announce.
4. **Respect the 51,200-acre per-state cap.** It is the hard ceiling on a Terranox-style federal land bank. Ten Western states × 51,200 ≈ **512k acres maximum per corporate family** (calc).
   - Unitized acreage is excluded from the cap (per the NV notice), which favors fast farm-outs into developer units.
   - The cap pushes the strategy toward **high-grading**: hold the best 51k acres per state, sell or farm out the rest, and use **private fee, state trust and split-estate rights**, which BLM does not cap or auction.
5. **Build the $40/acre diligence rule into the model.** A lease that is not worked lapses at year 10 unless ~$40/acre has been spent (about $2M on 51k acres) or paid in lieu. A land bank therefore has to flip, farm out with a work commitment, or prove up inside ~10 years. That matches a Terranox-style "own it, de-risk it cheaply, sell the step-up" cycle.
6. **Prioritize states with fast processing and thin competition.**
   - New Mexico (256 days) and Nevada (335 days) process nominations fastest. NV is crowded; NM is still building.
   - Idaho, Utah, CA and OR/WA take 2.5-4.5 years, which caps how fast new rights can be created there. Because few new leases come out, existing leases in those states trade at a premium, so buying them from holders who are not using them can beat nominating.
   - Avoid DoD-consent areas (14% of rejections) and USFS lands (~3 years).

---

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

- **The Terranox mechanic transfers, with a twist.** In Saskatchewan you stake the right first and others see it later. On BLM land the *location* becomes public 4-16 months before the auction, and the nominator gets no preference. The edge therefore has to come from three things:
  - (a) ranking blind ground the crowd does not value, where nominators routinely win at $2-4/ac;
  - (b) scale and noise in nominations;
  - (c) non-auction channels: day-after noncompetitive filings on unbid parcels, private and state rights, and buying existing leases from idle LLC holders.
- **The economics are tiny at entry and large at exit.** Nominating costs about $0.17/ac, the floor bid is $2/ac and rental is $3/ac/yr. Recent clearing prices on recognized ground run $232-$1,207/ac, and that is before any MW is proven. The step-up is already observable in BLM data.
- **The 2026 CX shortens the de-risking loop.** TG-hole programs up to 10 acres of disturbance can now move from NOI to drilling on a CX, in weeks to months rather than the ~10-month EA median. An owner can turn a floor-price lease into a TG-confirmed anomaly and sell it within roughly 12-24 months of the lease issuing (calc; assumes CX use and no extraordinary circumstances).
- **The gap vs Zanskar.**
  - Zanskar is a developer. Its BLM auction position is ~18 Nevada parcels and ~50k acres, bought for ~$0.76M. It has a 100 MW PPA, an operating plant and a project-finance facility (Z04).
  - Its bidding is visible and price-disciplined: it loses at the margin by $1 and won nothing outside Nevada.
  - Its own discovery announcements reprice its neighbors' land, and Zanskar cannot sell land neutrally to Ormat or Invenergy.
  - No one is running a **multi-state, ML-ranked, cap-aware land bank** that does all of the following:
    - nominates broadly as cover;
    - sweeps unbid parcels on day one;
    - proves up under the new CX;
    - farms out or sells to developers and data-center offtakers, keeping an override (royalty).
  - The landman LLCs (Buffalo River, Percheron, FLHN) already do the buying, but show no data thesis. Zanskar has the data, but runs it as a developer. A Terranox-shape company would sit between them.
- **Main risks.**
  - (1) Rising crowding: 27% duplicate nominations and 22-36 registered bidders per NV sale.
  - (2) BLM staffing makes timing unpredictable: the 1.28M-acre backlog and 15-month reviews in NV.
  - (3) The per-state cap limits federal scale, so private and state rights have to carry growth.
  - (4) Post-sale All-Bids reports expose your valuations, so bid strategy must assume competitors learn from you.

## Sources

- 43 CFR 3203.5 (competitive process): https://www.law.cornell.edu/cfr/text/43/3203.5
- 43 CFR 3203.10 (nominations): https://www.law.cornell.edu/cfr/text/43/3203.10
- 43 CFR 3203.13 (sale every 2 years): https://www.law.cornell.edu/cfr/text/43/3203.13
- 43 CFR 3203.14 (45-day notice): https://www.law.cornell.edu/cfr/text/43/3203.14
- 43 CFR 3203.15 (highest bidder; binding): https://www.law.cornell.edu/cfr/text/43/3203.15
- 43 CFR 3204.5 (noncompetitive after unbid): https://www.law.cornell.edu/cfr/text/43/3204.5
- 43 CFR 3206.12 / 3206.13 (lease size; 51,200 ac/state cap): https://www.law.cornell.edu/cfr/text/43/3206.12 ; https://www.law.cornell.edu/cfr/text/43/3206.13
- 43 CFR 3207.10 / 3207.11 (term extension; $40/ac work): https://www.law.cornell.edu/cfr/text/43/3207.10 ; https://www.law.cornell.edu/cfr/text/43/3207.11
- BLM NV Oct-2025 sale notice (nomination fee, noncompetitive random draw, acreage cap, separate bidder numbers): https://www.blm.gov/sites/default/files/docs/2025-08/20251021_Geothermal_Sale_Notice_Signed.pdf
- BLM NV call for Oct-2028 nominations (deadline 30 Jun 2027; $150 + $0.14/ac): https://www.blm.gov/sites/default/files/docs/2026-07/Geo_Nominations_Due_2028.pdf
- BLM NV parcels available noncompetitively (Sep 2026): https://www.blm.gov/sites/default/files/docs/2026-09/NV_Geot_20260910_Parcels_two_year_window.pdf
- BLM NV Oct-2026 sale comment period (84 parcels, 268,251 ac): https://www.blm.gov/announcement/blm-seeks-input-october-2026-geothermal-lease-sale-nevada
- BLM NV geothermal sales index: https://www.blm.gov/programs/energy-and-minerals/geothermal-energy/regional-info/nevada
- GAO-26-108040, Geothermal leasing and permitting (Sept 2026): https://files.gao.gov/reports/GAO-26-108040/index.html
- BLM geothermal exploration CX, 91 FR 22848 (28 Apr 2026): https://www.federalregister.gov/documents/2026/04/28/2026-08235/national-environmental-policy-act-implementing-procedures-for-the-bureau-of-land-management ; https://www.govinfo.gov/content/pkg/FR-2026-04-28/html/2026-08235.htm
- BLM adoption of 65 CXs (2 Sep 2025): https://www.federalregister.gov/documents/2025/09/02/2025-16759/notice-of-adoption-of-categorical-exclusions-under-section-109-of-the-national-environmental-policy
- Rescission of obsolete geothermal leasing provisions (17 Jul 2025): https://www.federalregister.gov/documents/2025/07/17/2025-13404/rescission-of-regulations-regarding-competitive-and-non-competitive-geothermal-leases
- 2024 Fluid Mineral Leases rule (bidder confidentiality until end of sale; Privacy Act release; excludes geothermal): https://www.govinfo.gov/content/pkg/FR-2024-04-23/html/2024-08138.htm
- BLM Lund North TG holes approved under CX (13 Aug 2026): https://www.blm.gov/announcement/blm-authorizes-geothermal-temperature-gradient-hole-drilling
- BLM geothermal program (245M acres; 51 plants; 2.65 GW): https://www.blm.gov/programs/energy-and-minerals/renewable-energy/geothermal-energy
- Young et al. 2014, Geothermal Permitting and NEPA Timelines, GRC Trans. 38: https://publications.mygeoenergynow.org/grc/1033639.pdf
- Levine et al. 2022, Mining G.O.L.D. (Don A. Campbell nominated 2001, won 2007): https://docs.nlr.gov/docs/fy22osti/81946.pdf
- DOE Liftoff Next-Gen Geothermal (CX exploration 2-4 months; lease sale can take >4 years): https://cdn.catf.us/wp-content/uploads/2025/06/09154348/doe-liftoff-nextgen-geothermal.pdf
- BLM All-Bids reports used for the Zanskar loss examples: https://www.blm.gov/sites/default/files/docs/2024-10/GEONV-2024-Q4-All%20Bids.pdf ; https://www.blm.gov/sites/default/files/docs/2025-10/NV_Geot_20251021_Bidding_Results.pdf ; https://www.blm.gov/sites/default/files/docs/2023-11/NV_Geot_20231114_Bidding_Results.pdf
- NV 2025 noncompetitive results: https://www.blm.gov/sites/default/files/docs/2025-10/NV_Geot_20251027_Non_Comp_Sale_Results.pdf
- Sibling evidence files: /home/user/nuketime/research/geothermal/evidence/R01-blm-competitive.md ; /home/user/nuketime/research/geothermal/evidence/Z04-land.md
