# How big is the nuclear dedication market?

*2026-10-21. Eight parallel research agents covered top-down spend, incumbent revenues, volumes, pricing, the market outside the US, growth to 2040, adjacent markets for the same engine, and evidence of buyer demand. Their full notes and sources are in `raw/` (spend, incumbents, volumes, pricing, global, growth, adjacent, demand). The search quota was shared, so each agent ran about 6 searches and fetched the rest directly from filings and primary documents.*

**Evidence labels.** **[S]** means sourced (a filing, EPRI, NEI, FERC, NRC). **[E]** means an agent's estimate built on stated assumptions. **[R]** means recalled from memory and not verified.

---

## Verdict

1. **Dedication as a service is a small market:** about **$0.3B a year in the US (range $0.15-0.6B) and about $0.4-0.7B worldwide** [E]. Sold as a fee-for-service business, it caps at roughly Paragon's size. Paragon is the best comparable: about $150M in revenue at a 20-22% EBITDA margin, bought by Mirion for $585M in Dec 2025 [S]. On the "too small kills" rule, a pure AI dedication service fails.
2. **The market around the signature is larger:**
   - US safety-related replacement parts sold with dedication: about **$2.0B a year (range $1.3-2.8B)** [E, built bottom-up from incumbent revenues; a top-down check gives $0.8-2.0B].
   - Obsolescence and reverse-engineering services: **$0.2-0.4B** [E].
   - The value of speed, which nobody is paid for today: critical-path outage days worth about **$50-400M a year**, plus **$0.4-1.35B a year** of carrying cost on $3.2-6B of plant inventory [S for inventory, E for the rest].
   - Growth: the value of dedicated items rises from about **$1.1B in 2026 to $2.4B in 2040** (high case $4.5B), and new builds go from 5% to about 40% of that [E].
3. **Demand is limited by capacity, not by interest:**
   - Duke runs dedication for 25-50% of its safety-related purchasing, tracks a backlog, and says it "would be performing more CGD" with more people [S, EPRI 3002029261].
   - Licensees rank cost *last*, behind quality and lead time [S].
   - The number of qualified suppliers is at an "all-time low" [S, Paragon CEO]. Worldwide N-stamp holders fell 32% from 2013 to 2019 [S].
4. **So the company only reaches venture scale if it sells dedicated parts and approvals, not dedication hours.**
   - Own the dedicated-part library and sell parts at nuclear margins.
   - Charge for guaranteed turnaround on emergent parts.
   - Take a share of the documented savings on obsolete-part reverse engineering.
   - Run the same engine across regimes. The largest adjacent pool is DLA, which bought **$10.4B of non-competed items in FY25**, about $3.4B of it engineered aviation parts [S, USAspending].

   A realistic nuclear outcome is **$300-600M of revenue by the mid-2030s** [E], 10-20% of a $2-3B parts-and-services pool. At current deal multiples (3-4x revenue, 14-18x EBITDA [S]) that is a **$1-2.5B company** from nuclear alone. Defence approvals are the upside beyond that.
5. **The cautionary datapoint.** AZZ bought NLI, a dedicator, for about $77-80M in 2012 and sold it to Paragon for $23.6M in 2020 at an $18.6M loss [S]. Generic dedication labour without a proprietary part library was worth little. Paragon was worth 25x more five years later, once it held a library and the nuclear revival had arrived.

---

## 1. Top-down: where the money sits (US)

| Layer | $/yr | Basis |
|---|---|---|
| Fleet operating cost | **$16.3B** | NEI 2025 data: $20.82/MWh on about 783 TWh [S] |
| Labour | ~$8.8B | NEI says "more than half" of operating cost [S] |
| Maintenance (FERC accounts 528-532) | ~$5.5B fleet-wide | $2.26B on 320 TWh for regulated plants in 2025, scaled up [S] |
| Parts and materials, excluding fuel | $3.0-5.5B (central $4.3B) | Expense plus capital materials [E] |
| Safety-related parts, including capital | $0.8-2.0B (central $1.3B) | 20-30% of items are safety-related (ENEC) [S]; dollar share assumed [E] |
| Routed through dedication | $0.1-0.5B (central ~$0.3B) | EPRI: 25-50% of safety-related purchases at more than 20 reactors (by item count) [S]; dollar share [E] |
| Dedication premium pool | $50-300M (central ~$150M) | Premium of 40-65% of item price [E] |
| Inventory on hand | $3.2-6B (Constellation alone $1.485B) | SEC XBRL [S]; about 995 days on hand [S, 2009 benchmark] |

**Per site (about 54 sites):** $30-55M of parts issued a year, $8-22M of it safety-related, $2-9M routed through dedication, and $55-115M of inventory [E/S].

## 2. Bottom-up: incumbent revenues (US)

| Player | Relevant revenue | Notes |
|---|---|---|
| Westinghouse parts | ~$350-600M US [E] | New Stanton site: 125+ staff, 4,000+ plans covering about 100k part numbers, 50-60k parts a year [S]. Group about US$5.1B revenue at about 22% EBITDA [S, from Cameco's 49% share] |
| Mirion / Paragon | ~$150M (2026E) | 20-22% EBITDA. $585M deal, about 3.9x revenue and 18x EBITDA. More than 20,000 proprietary parts, in 100% of North American reactors [S] |
| Curtiss-Wright nuclear aftermarket | ~$250-350M US [E] | Naval & Power segment $1.50B at 15.4% operating margin; Power & Process $635M (+17%) [S]. Bought Ultra I&C for $200M, about 3.1x revenue [S] |
| Framatome and GE Vernova Hitachi parts | ~$300-600M [R/E] | |
| Equipment makers (Crane, Flowserve, Emerson, Ametek) | ~$300-600M [E] | |
| Independents (UCI, Nutherm, Park) | ~$50-150M [E] | |
| Engineering firms (Sargent & Lundy, ENERCON, Zachry) | ~$40-110M [E] | |
| Utilities in-house | ~$100-250M [E] | |
| **Total** | **~$2.0B (range $1.5-2.8B)** | Value-add from pure dedication and qualification services: **$0.3-0.6B** |

## 3. Volumes

- **Dedication jobs:** about **20,000-30,000 a year** in the US (central about 25,000) [E].
  - Westinghouse: 5-10k (derived from about 50k parts).
  - Paragon: 1,300 [S].
  - Utilities in-house: 6-15k.
  - EPRI's survey of 8 suppliers: 3 dedicate more than 500 unique items a year, and more than 30 firms offer dedication worldwide [S].
- **New dedication plans:** about **4,000-6,000 a year** [E]. Paragon alone writes 70-100 a month [S].
- **Emergent jobs:** about **5,000-8,000 a year**, of which about **1,000-2,000** sit on an outage's critical path [E].
- **Obsolescence:**
  - 20-25% of components are no longer supported by their original maker [S, Rolls-Royce study].
  - 75% of obsolete items are found only at the point of purchase [S].
  - TVA measured about 58 obsolescence events per site per year [S, OIG], which scales to about 3,000 across the fleet [E].
  - Reverse-engineering projects run about 300-800 a year [E].
- **Liability tail:**
  - Part 21 defect reports fell from 509 in 1985 to 22-39 a year [S].
  - 10 of 24 reports in 2023 involved dedicated items [S].
  - That works out to about one dedication-related report per 1,500-3,000 jobs [E], a risk that can be priced.

## 4. Pricing and value per event

- **No public per-item dedication price exists.** The recalled ranges are 2-10x the commercial price, $5-50k for a new plan (digital $100-500k+), and 20-200 hours of engineering per technical evaluation [R]. Real numbers need interviews with procurement engineers.
- **Outage day:** about $1M or more by long-standing industry rule [S]. For a 1.1 GW unit in 2026 that is about $1.5M at base, about $2.5M on the critical path, and $5M or more on scarcity days [E]. PJM capacity cleared at the $329/MW-day cap for 2026/27 [S].
- **Value per event** [E]:
  - An emergent part in a refuelling outage is worth $3-10M.
  - A forced outage waiting on an obsolete part is worth $6-27M.
  - Rational fees are $100-500k per event, or a $250-750k per site per year retainer with a 72-hour guarantee.
- **Reverse engineering:**
  - The Utilities Service Alliance documented about $30M of savings over 3 years at 9 stations. Examples: a turbine governor ($7.85M), a voltage regulator ($898k), butterfly valves ($622k) [S].
  - Price as 10-30% of the design change avoided, which comes to $50k-1M per part family [E].
- **Capturable fleet revenue from speed and obsolescence:** about **$55-285M a year** on a $0.15-0.9B value pool [E].

## 5. Outside the US

- **Who uses dedication:** about 173 of 443 operable reactors (39%) are in countries that routinely use EPRI-style dedication [E from the World Nuclear Association list; EPRI says about 40%, S].
- **Dedication services outside the US:** about **$180-325M a year** (parts value $0.7-1.3B) [E]. Worldwide including the US: **$0.4-0.7B services** and $1.7-2.7B parts [E].
- **Best first market: Canada.**
  - Bruce units 3-8: C$13B over 2020-2033 [S].
  - Pickering refurbishment: C$26.8B, starting 2027 [S].
  - Darlington BWRX-300: C$20.9B [S], a US-origin design.
  - Canada is worth about $30-60M a year to a dedicator, through a Canadian partner because of the Ontario-content preference [E].
- **Korea:** 26 units on EPRI-style dedication. A strong need for audit trails after the 2012-13 forged-certificate scandal, which covered 7,682 components [S]. Entry is through a partner.
- **Finland, KELPO:** a joint utility platform for dedication data, with the regulator observing. It is the closest analogue to this idea, and a possible partner or competitor [S].
- **France, Japan and the UK's gas-cooled AGR fleet:** effectively closed. France qualifies in-house under its RCC-M code, and Japan relies on its OEM groups.

## 6. Growth to 2040 (base case, 2026 dollars) [E]

| | 2026 | 2030 | 2035 | 2040 |
|---|---|---|---|---|
| US safety-related procurement | $4.4B | $6.2B | $9.2B | $11.9B (high case $22B) |
| Value of items routed through dedication | $1.1B | $1.5B | $2.0B | $2.4B (low $1.6B, high $4.5B) |
| Dedication service fees | $0.3-0.4B | | | $0.6-0.85B |

Growth drivers [S]:
- **Restarts:** about 2.2 GW (Palisades in 2026, Crane in 2027, Duane Arnold in 2029).
- **Licence renewals to 80 years:** about 60-65 of 94 units over time.
- **Uprates:** about 1.9 GW committed.
- **Hyperscaler deals:** about 6.8 GW of existing plants under contract.
- **Large new builds:** the AP1000 programme ($80B Westinghouse partnership; DOE's $17.5B conditional commitment for long-lead parts) and the Fermi America units.
- **SMRs and advanced reactors:** construction permits for TVA's BWRX-300 at Clinch River and for Natrium at Kemmerer, plus Kairos's Hermes units.
- **DOE reactor pilot:** 10 companies, with NQA-1 quality assurance overseen by DOE.

Notes:
- The existing fleet remains the main buyer until about 2032.
- The biggest swing factor is whether the AP1000 tranche reaches an investment decision.
- Advanced reactors are new, digital-first buyers with no dedication departments of their own.

## 7. Adjacent markets for the same engine

| Market | Pool | Can a private company sign? | Fit |
|---|---|---|---|
| DLA SARs and defence alternate sourcing | $10.4B non-competed buys (FY25) [S]; $50-200M/yr spent preparing SARs [E] | No. The government approves, so the business is a package factory or a reviewer tool | High: the largest pool |
| Nuclear reverse engineering, obsolescence and digital I&C | $200-400M/yr in US services [E]; I&C upgrades $4.2B worldwide [low confidence] | Yes | High: an upsell to the same buyers |
| DOE complex (Hanford, Savannah River, national labs) | $0.5-1.5B of NQA-1-graded purchasing; $50-150M dedication layer [E] | Yes, through each site contractor's supplier list | High |
| Advanced reactors | $20-80M now, $100-300M by the early 2030s [E] | Yes | High |
| EQ and seismic testing | $150-300M/yr in the US [E] | Yes, but needs capital-heavy rigs | Medium: partner with Element or Curtiss-Wright |
| Naval reactors, fusion, medical and rail | — | Mostly no | Low |

## 8. Buyers and how they buy

- **About 21 buying organisations** run 95 units at 55 sites [S, NRC list].
  - The top 6 run 64% of units: Constellation 21, Duke 11, Southern 8, TVA 7, Dominion 7, NextEra 7. The top 8 run about 75%.
  - It is a concentrated enterprise sale, and one or two fleet wins come close to the NUPIC threshold.
- **Who inside the utility:** procurement engineering writes or reviews the evaluation, supply chain places the order, and QA owns the approved-supplier list.
- **Cold start:** NUPIC runs joint audits on a 33-month cycle, but only for suppliers with at least 5 utility customers [S]. Expect 12-24 months to get onto approved-supplier lists at scale [R].
  - Workaround: buy an already-accepted dedicator, or sell through one at first.
- **Appetite for AI as an assistant is proven:**
  - Nuclearn: $10.5M Series A, at more than 65 reactors [S]. Its CEO says "Liability always falls with a person."
  - Atomic Canyon: at Diablo Canyon, and its NIVA tool was built with INPO, EPRI and NEI [S].
  - NRC: published an AI strategic plan in Sep 2025 [S].
  - Machine-drafted, human-signed work fits practice. Machine-decided acceptance does not.

## 9. Risks that the sizing exposes

1. **The pure service pool is small** ($0.3B in the US). The plan depends on parts margin, a speed premium, and expanding into adjacent regimes.
2. **"Days, not months" holds only where an item's critical characteristics can be checked by quick tests.** EQ ageing, supplier surveys and making reverse-engineered parts set the real lead time for the rest.
3. **Incumbents already sell on speed**, with 8-26-week lead times and a claimed "8+ week schedule improvement" at Westinghouse [S].
4. **EPRI templates and utility-side AI tools could speed up in-house dedication** and shrink what gets outsourced.
5. **Part 21 liability and NRC vendor inspections** will focus early on a new, AI-heavy process.

## 10. What to verify next (cheap)

- Interview 5-10 procurement engineers: actual prices per dedication, hours per technical evaluation, backlog size, and what they would pay for a 72-hour turnaround.
- Search NRC event reports (LERs) to count shutdowns and outage extensions caused by parts.
- Pull FERC Form 1 account 154 (materials and supplies) for the regulated nuclear utilities.
- Get Paragon's revenue mix (parts versus services) from Mirion's investor materials.
