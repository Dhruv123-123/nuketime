# Red team: Fee-and-Split Western Ranch Bank, through the cheap-right / auction-repricing lens

**Play:** Build a parcel-level title map of Nevada, Utah and Oregon (fee land, patents with no mineral reservation, and SRHA-reserved land). Join it to ML favorability and newly released well files. Quietly lease private geothermal plus surface, pad and water options, add $1/acre noncompetitive BLM leases, and sell the package to Ormat or Fervo for a 2-5% override.

**Scorer's score:** 21 (c3 cheap right = 5).

**Method note:** The shared WebSearch budget for this workflow turn was used up before this agent's first query. The only fresh fetch was the Nevada statute NRS 534A. Everything else comes from the sibling evidence files in `/home/user/nuketime/research/geothermal/evidence/`, which cite primary BLM, SEC, court and statute sources. Inferences are labelled.

## Verdict up front

**Not refuted. Wounded on c3.** The *private* half of the right stays cheap, for three reasons:
- There is no auction.
- The statutes give the heat to the surface owner.
- Private lease prices are never published.

The play as written, however, depends on a **bundle** of private ground plus adjoining federal land. The federal half does **not** stay cheap once anyone can see where you are working. Three public signals give the location away before proof:
1. a state drilling permit that lists coordinates;
2. a BLM nomination that publishes the legal description 4-16 months before the sale;
3. any announcement of a discovery.

The repricing is documented: $2 to $232/acre at Pumpernickel. Repricing does not wreck the economics, because land at $300/acre is only about $0.15M/MW. What it destroys is the *spread* on the BLM leg. It can also strand a private block that sits on a reservoir shared with federal ground that a land bank won. The AI-leveraged sequencing answer below largely rescues the play, at a cost of 12-18 months. I would trim c3 from 5 to 4 and leave the rest. **Revised total: 20.**

## Rung 1: Is the private right actually cheap at signing? Yes.

- **Statutes give the heat to the surface owner:**
  - Nevada: "The owner of real property owns the rights to the underlying geothermal resources" unless "reserved by or conveyed to another person" (NRS 534A.050, fetched this turn).
  - Oregon: ORS 522.035, same rule.
  - Utah: heat "derives from an interest in land" (73-22-4). The 2026 amendment (Ch. 477) moved the threshold to 100 C and explicitly brings in enhanced and advanced systems.
- **Comparable deals, from Raser's FY2009 10-K:**

  | Area | Acres | Cost | Approx. per acre |
  |---|---|---|---|
  | Truckee, NV | 4,444 | $5k for 50-year terms | ~$1/ac bonus, $1/ac/yr |
  | Klamath, OR | 984 | $10k bonus | ~$10/ac |
  | Thermo, UT | ~10,800 | $41.2k | ~$3.8/ac |

  Typical private terms are a $1-30/acre bonus, $1-3/acre/yr rent, and a 2-5% gross royalty that steps up (US Geothermal 10-K: 3%, then 4%, then 5%).
- **Nobody can see the price.** Private lease terms do not appear in any BLM bid report. A rancher has no public comparable to anchor on, unlike a BLM parcel that went to auction.
- **Incumbents are not bidding against you in an auction here.** Ormat holds 18% of its 434k acres privately and Fervo holds about 27% of its 595.9k acres privately. They do run landmen. But Fervo assembled its whole book at about **$4/acre** in 2019-21, which suggests private ground was not bid up even while the boom built.

**This rung holds.** The play is right that the private channel is structurally insulated from auction repricing at signing.

## Rung 2: Does the right stay cheap once you nominate or drill? Not for the federal leg.

### Leak 1: the drilling permit puts a public pin on the map

- NRS 534A.060 requires an NDOM permit for every geothermal or exploratory well. A temperature-gradient (TG) permit costs $100 and is decided within 10 days.
- The data stays confidential for 5 years (NRS 534A.031).
- But NDOM's public well table (dated 2026-09-29, 938 wells) publishes **permit number, operator, county, UTM coordinates, land type and BLM lease number** (D03).
- Result: the play's "first test" gradient hole on a fee ranch announces the target's exact location on day one, even though the temperatures stay hidden.
- Land-bank LLCs already trade on exactly this kind of signal:
  - Buffalo River, Percheron, FLHN, Lithos48 and Cordillera took about **52% of 2022-25 NV+UT bonus dollars** (Z08).
  - About 27% of nominated acreage is rejected as duplicates, which means several parties are converging on the same ground (R03).
- NRS 534A requires no public notice of the application itself. The fetched text only routes copies to the State Engineer, NDEP and NDOW. So the leak is the published table, not a notice (inference).

### Leak 2: the "adjoining unbid BLM parcel" may not exist

- A noncompetitive lease is available **only** on a tract that was offered at a competitive sale and drew no bid (30 USC 1003(c)).
- If the federal section next to your ranch has not been nominated by someone else and gone unsold, you must nominate it yourself. That means:
  - the legal description is published **4-16 months** before the sale;
  - the nominator gets **no preference right**;
  - the auction is a binding ascending one;
  - Nevada nomination-to-sale times are about 335 days, and the review standard slipped from about 11 to about 15 months (R03, GAO-26-108040).
- Even where an unbid parcel exists, day-after filings are a **random draw** among simultaneous applicants (43 CFR 1822.17). After that it is first-come.
- The "about 53,686 acres open at $1/acre" in Sep 2026 is other people's rejected ground. It is useful for opportunistic filing, but it will only rarely be the section that adjoins *your* ranch.

### Leak 3: an announcement or neighbourhood signal reprices the step-out

- Zanskar bought Pumpernickel step-outs at $2/acre in Nov 2023. Adjacent NV-2025-10-2143 cleared at **$232/acre** to Lithos48, over Zanskar's $231, about a month after the Sep 2025 announcement (Z04).
- Utah ground near Cape cleared at up to $344/acre, and reportedly $1,207/acre in 2026 (R04).
- The 2025 Nevada top bid was $410/acre.

### Leak 4: county records and word of mouth (unverified)

- In practice a memorandum of lease is recorded to protect priority against later purchasers. In thinly populated counties (Humboldt, Pershing, Lander, Churchill), a systematic campaign across 20 ranches becomes visible in the recorder's index, and ranchers talk to each other.
- I could not verify this with a fetch, but it is standard landwork (inference).

### Leak 5: Utah water rights are public by design

- An application is advertised for 2 weeks with a 20-30 day protest window, and the applicant must show "financial ability and good faith" (Utah 73-3-7/8; R09).
- A Utah fluid-right filing therefore broadcasts the project and cannot be held as a speculative option.
- In Nevada, reinjected fluid is exempt (NRS 534A.040), so this leak is Utah-specific.

## Rung 3: Does a cheap private block still have value if the federal leg reprices or goes to someone else?

This is the deepest crack.

- **Reservoirs cross ownership lines.** Great Basin blind systems follow range-front faults. Roughly 80%+ of Nevada is federal (R05, unverified), so a typical fault segment crosses both fee or checkerboard sections and BLM sections. A single fee section is rarely a full development unit; R05 notes that "a blind system rarely sits wholly inside one section."
- **Nevada has no pooling or unitization rule for private geothermal owners.** The fetched NRS 534A contains no unitization, pooling, correlative-rights or drainage provisions. That cuts two ways:
  1. A holdout rancher inside the fault zone cannot be forced in.
  2. A BLM lessee on the adjoining section, such as a land-bank LLC, can produce the same reservoir with no obligation to you.
- **Who controls the unit?** If the land bank wins the repriced federal sections, *it* holds the majority of the development unit. Your private block becomes a minority piece that a buyer can drill around. Utah's correlative "fair share" rule (73-22-3, 2026) at least creates a claim on drainage, but no comparable rule was found in Nevada.
- **Implication.** The private leg's value depends on locking the federal leg *before* any public signal. Otherwise the cheap private right is cheap because it is a minority position.

## Rung 4: Will the buyer pay a 2-5% override on top? Probably not at 5%.

- Ormat's blended royalty load was about **4.5% of electricity revenue in 2025** (10-K). Royalties on the same ground can stack:
  - landowner, 2-5%;
  - BLM, 1.75% then 3.5%;
  - the proposed override, 2-5%.

  Together that would roughly double the incumbent's royalty burden.
- Fervo and Ormat run private leasing themselves. They will pay a step-up only for a **blocking, contiguous, de-risked** unit, not for a scattered collection of ranch leases.
- The live precedent for a non-landowner override is Centaurus's **$5/MWh** on Cape Phase I, about $0.4M/MW in present value (B07). That came with $75M of preferred capital, not land.
- My expectation is that a land-and-data originator realistically gets about **1-2% or about $2-3/MWh**, or a cash step-up at $300-1,500/acre (inference; R04 gives $0.1-0.5M/MW-equivalent for TG-confirmed leases).
- At 1.5% of $100/MWh and a 90% capacity factor, that is about **$1.2k/MW-yr**. Origination therefore has to reach GW scale before the royalty book matters. B07 says about 10-20 GW under override is needed to support a company worth $5-10B.

## Rung 5: Does ML spread close the gap? Partly, and on the public layer.

- The USGS ML favorability map is public. It places 15 of 28 producing systems in the top 1% of map area (L05), and every land bank can download it.
- Nominated acreage went from about 25.8k acres (2020) to **over 1M acres (2025)** (R14). The crowd's prior is converging.
- What ML spread does **not** yet commoditise is the **title layer**. Classifying parcels as fee, SRHA, Pittman, railroad grant or post-FLPMA takes patent-by-patent reading of GLO and BLM Master Title Plats plus county records (R08). No competitor discloses a private or fee program:
  - Zanskar: none disclosed (Z04, Z06);
  - the land-bank LLCs: they appear only in BLM auction data (Z08).
- That is the durable data edge. It decays more slowly than the geology edge, because it is a messy, legal, county-level dataset.

## Rung 6: Title traps that reprice the right to zero

- **SRHA land:** 33M+ acres where the US owns the heat. A private lease there is void (30 USC 1020; *Union Oil* 1977; *Rosette* 2002).
- **Pittman Act patents in Nevada valley bottoms:** "coal and other valuable minerals" were reserved, and whether that covers geothermal is **untested** (R08; *Bedroc* 2002 read "valuable minerals" narrowly for gravel). This is a live title risk on exactly the valley-margin ground the play targets. *Rosette* took about 10 years to resolve.
- **Ormat's 10-K warning:** "In many cases, the lessor under these private geothermal leases owns only the geothermal resource and not the surface." Heat and surface can be severed even on private land, so the title map has to track both estates.

## Best AI-leveraged answer to the killer (sequencing), and does it rescue the play?

The killer is that public signals (permits, nominations, recordings, announcements) reprice the federal leg and strand the private block. The answer is to make the federal leg get issued blind, before any pin goes on the map.

1. **Rank and map title first, entirely offline.**
   - Join released NDOM TG data and the Phillips/Chevron sheet (786 holes, 116 at 10 F/100 ft or more across 28 prospects; L16).
   - Add oil and gas BHTs, which are public after 1 year at most (NAC 522.540), and the USGS map.
   - Overlay a parcel title classifier. Score whole fault segments, not parcels.
   - **Prefer segments where the modelled reservoir footprint is majority fee, railroad checkerboard or non-reserved patent.** There the private leg is the unit and federal repricing is a minor risk.
2. **Nominate the federal sections first, inside noise.**
   - Nominations cost about $0.17/acre, so 100k acres costs about $17k (R03).
   - Cover whole fairways plus decoys, filed through more than one entity, as the incumbents already do.
   - On blind ground, nominators "usually win at the floor": Zanskar won 16,720 acres at $2/acre in 2023, with single bids. R03 frames this as "a leak only where your target falls inside the crowd's prior."
3. **Sign long-dated private options in one short sweep** during the 11-16 month auction lag.
   - Use options with fixed exercise terms, fixed royalty steps and 30-50 year tails (the Raser Truckee terms were 50 years). That kills renewal holdout.
   - Bundle the surface, pad and access easements in the same instrument, including on SRHA surface where the rancher owns no heat.
4. **De-risk without permits until the leases are issued.**
   - Use MT, gravity, InSAR, soil CO2 or He, and re-reads of old logs. These need no NDOM well permit (inference: permits attach to wells).
   - Drill the first TG hole only **after** the federal sections are issued.
5. **Run a standing ML watch on every unbid parcel and every new NDOM permit**, including rivals', and file $1/acre day-after applications where the model disagrees with the crowd. This is opportunistic, not core.
6. **Sell a unit, not leases.** Offer a contiguous fee plus federal plus surface package with a TG result. Price it as a cash step-up ($300-1,500/acre) plus about a 1-2% override, rather than demanding 5%.

**Does it rescue the play?** Mostly, yes.
- The cost is **12-18 months of nomination lag** before the first hole. Utah, Idaho and Oregon nomination lags of 2.5-4.5 years make them slower, so lead with Nevada and with fee-majority targets.
- The residual risks the AI does not fix:
  - Pittman and other title ambiguity;
  - override-rate pushback from Ormat and Fervo;
  - the fact that value is crystallised at the PPA rather than at confirmation (no arm's-length sale of a proven-but-unbuilt resource is priced in the evidence; R04).
- None of these is a "too small" or "service-only" killer. The play still owns the asset.

## Score adjustment

| Criterion | Scorer | Mine | Why |
|---|---|---|---|
| c1 proving step | 5 | 5 | A cheap TG hole after the leases are issued |
| c2 illegible data | 4 | 4 | The title layer is the durable edge; the geology layer is diffusing |
| c3 cheap right | 5 | **4** | The private leg is cheap and unpriced, but the federal leg reprices on any pin, and Nevada has no pooling to protect a minority private block |
| c4 step-up buyer | 3 | 3 | Buyers exist, but expect 1-2% override or cash, not 5% |
| c5 size ladder | 4 | 4 | 30 GW undiscovered (USGS mean); needs GW-scale origination |
| **Total** | **21** | **20** | |

## Sources

- NRS 534A, Nevada geothermal statute (fetched this turn; 534A.031 confidentiality, 534A.050 ownership, 534A.060/.070 permits, no pooling provisions): https://www.leg.state.nv.us/NRS/NRS-534A.html
- NAC 522, Nevada oil and gas well-data confidentiality: https://www.leg.state.nv.us/NAC/NAC-522.html
- Oregon ORS 522.035: https://oregon.public.law/statutes/ors_522.035
- Utah Code 73-22-3 (2026): https://le.utah.gov/xcode/Title73/Chapter22/C73-22-S3_2026050620260506.html
- 30 USC 1003 (noncompetitive leasing only on unbid tracts): https://www.law.cornell.edu/uscode/text/30/1003
- 30 USC 1020 (reserved-mineral lands leasable only under the Act): https://www.law.cornell.edu/uscode/text/30/1020
- Watt v. Western Nuclear, 462 U.S. 36 (33M SRHA acres): https://www.law.cornell.edu/supremecourt/text/462/36
- Rosette v. US, 277 F.3d 1222: https://www.courtlistener.com/opinion/161903/rosette-incorporated-v-united-states/
- Bedroc v. US, 314 F.3d 1080 (Pittman Act): https://www.courtlistener.com/opinion/7109873/bedroc-ltd-v-united-states/
- BLM NV Oct 2025 bidding results (Pumpernickel step-out at $232/acre): https://www.blm.gov/sites/default/files/docs/2025-10/NV_Geot_20251021_Bidding_ (full URL in Z04-land.md)
- BLM NV 2025 noncompetitive day-after results: https://www.blm.gov/sites/default/files/docs/2025-10/NV_Geot_20251027_Non_Comp_Sale_Results.pdf
- BLM NV parcels in the 2-year window (Sep 2026): https://www.blm.gov/sites/default/files/docs/2026-09/NV_Geot_20260910_Parcels_two_year_window.pdf
- Ormat 10-K FY2025 (18% private, 4.5% royalty load): https://www.sec.gov/Archives/edgar/data/1296445/000129644526000006/ora-20251231.htm
- Fervo 424B4 (about $4/acre assembly, 27% private, Centaurus $5/MWh): https://www.sec.gov/Archives/edgar/data/1853868/000162828026034849/fervoenergy-424b4.htm
- Raser Technologies 10-K FY2009 (private lease comparables): https://www.sec.gov/Archives/edgar/data/1103078/000119312510060692/d10k.htm
- US Geothermal 10-K FY2017 (royalty step-ups): https://www.sec.gov/Archives/edgar/data/1172136/000106299318001121/form10k.htm
- Evidence files used: R02, R03, R04, R05, R06, R08, R09, R14, Z04, Z06, Z08, D03, D05, B07, in /home/user/nuketime/research/geothermal/evidence/
