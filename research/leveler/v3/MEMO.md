# Machines Immortal: what kills the vision and what lets it live (20 Oct 2026)

**Vision under test.** "No machine that runs the world should ever wait on, or be held hostage by, a part." *AI made code abundant; we make machines immortal.* The master plan as first stated had four steps:
1. Buy machines nobody can keep running (old gas turbines) and keep them running.
2. Build every part they need with AI, and own the factories for the hard parts.
3. Sell that capacity to every operator.
4. Become the qualified factory for everything that isn't a chip.

**Method.** Five parallel researchers each took one killer:
- fleet supply and permits;
- owning a foundry;
- the "TSMC for parts" end state;
- OEM lawfare and safety;
- timing and capital.

Earlier rounds are in `../MEMO.md` and `../v2/MEMO.md`. Numbers marked est. are inference.

## Verdict

**The vision lives. The plan as first written dies.** Two of its pieces are fatal as stated, and both are fixable by changing the order of the rungs, not the destination.

1. **Fatal: fleet first.** Buying turbines at seed fails on capital, because debt only follows contracts. It also fails on permits: a relocated baseload frame is a major NOx source in non-attainment areas, and Texas has frozen data-centre permits. Data centres prefer modular units, and batteries now beat gas peakers in all 43 markets Wood Mackenzie surveyed.
2. **Fatal: "any design in, everything".** That is the contract-manufacturer model, and it earns about 5% (Jabil, Flex) or losses (Xometry). The "digital inventory" graveyard proves it: Shapeways, Fast Radius, Desktop Metal and Velo3D. TSMC margins come from customers designing to *TSMC's* rules. In an aftermarket the design is fixed by the OEM, so the right model is HEICO: per-part-number certified evidence, priced just under the OEM, with about 23% operating margin.
3. **Fatal for a startup: a greenfield single-crystal foundry.** It costs $150-300M and takes about 5 years to ramp; Rolls-Royce Rotherham took 2012-2017. It would land in the 2028-30 window when Howmet, CPP, Doncasters and SpaceX capacity arrives. BNEF warns of oversupply.

**What lets it live: re-sequence to parts, then foundry, then fleet, then breadth.** The re-sequenced company scores **19/25 (N4 T4 C4 A4 D3)**, a narrow pass. The literal plan as written scores about 14.

## Each killer ruled

| Killer | Ruling | Evidence | What lets it live |
|---|---|---|---|
| **Seed capital to buy turbines** | **Fatal if step 1** | Crusoe raised a $4.5M seed and got project finance only after a proven unit. VoltaGrid's $550M loan and $2B notes, and Solaris's $1.3B notes, came only on contracted fleets ([Global Venturing](https://globalventuring.com/blog/2021/04/27/crusoe-cruises-to-128m-series-b/?format=md); [Sidley](https://www.sidley.com/en/newslanding/newsannouncements/2025/11/sidley-represents-voltagrid-in-us-2-billion-of-senior-secured-second-lien-notes); [Energy Mag](https://theenergymag.com/news/market-news/solaris-energy-infrastructure-1-3-billion-private-debt-offering)). No project finance for refurbished orphan turbines was found. | Parts first (little capital). Buy units later, with project debt against contracts. |
| **Air permits for relocated frames** | **Fatal** for relocated baseload units in non-attainment areas. **Survivable** in place. | One 7EA running uncontrolled emits about 2,200 t/yr NOx (est.), far over the 25-100 t/yr non-attainment thresholds ([SemiAnalysis](https://newsletter.semianalysis.com/p/what-is-so-hard-about-behind-the)). New units need 5 ppm under NSPS KKKKa ([EPA](https://www.epa.gov/system/files/documents/2026-01/final-rule_fact-sheet-nsps-stationary-combustion-turbines_0.pdf)). Texas paused data-centre permits from 21 Sep 2026 ([Bracewell](https://www.bracewell.com/resources/governor-abbott-orders-tceq-to-pause-all-permit-issuance-for-data-center-projects/)). | Moving a unit is not a "modification" under 40 CFR 60.14(e)(6). An open-market DLN-1 retrofit took a 7EA to 9 ppm in under 9 months, with no SCR ([CCJ](https://www.ccj-online.com/gas-turbines-open-market-dln-1-system-anchors-quick-cc-to-gt-peaker-conversion/)). Buy *sited, permitted, grid-connected* units in place. |
| **Can you buy the units?** | Survivable | Fermi paid $18M for three GE 6Bs plus a steam turbine, about $158/kW for 114 MW ([SEC](https://www.sec.gov/Archives/edgar/data/2071778/000164117225022363/filename1.htm)). But about 60% of PJM's planned fossil retirements were postponed in 2025 ([Reuters via WHBL](https://whbl.com/2025/12/23/ai-data-centers-are-forcing-obsolete-peaker-power-plants-back-into-service/)). | Become the parts supplier to the owners first. They become the sellers and partners later. |
| **Revenue for old units** | Answered to about 2029/30 | PJM capacity cleared $329, $333 and $325/MW-day, with uncapped prices of $530-555 ([PJM](https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2026-releases/20260714-pjm-capacity-auction-procures-138318-mw-of-generation-resources.pdf)). That is about $120/kW-yr against about $200-250/kW all-in, a ~2-year payback for units that already hold grid rights (est.). | The price collar expires after about 4 auctions, and batteries compress peaking value. Prefer firm and capacity roles, and N+1 multi-unit sites for data centres. |
| **AI parts edge on common frames (6B/7EA/7FA)** | Weak | PSM, EthosEnergy, Allied, Sulzer and TTS already sell equivalent parts ([PSM](https://www.psm.com/products/b-e-class-frames/7b-e-ea)). The bottleneck is foundry capacity, not design. | Compete on lead time where castings are the constraint (see foundry row). |
| **AI parts edge on orphan frames (W501D, GT11N, FT4)** | **Plausible: the wedge** | Aftermarket support is thin. Allied added GT11 work only recently. GE's lead times on Alstom-heritage parts are about 24 months, and a 25% expedite fee does not guarantee delivery ([CCJ](https://www.ccj-online.com/?p=22552)). | AI reverse engineering makes many low-volume part numbers economic. This is the long tail the incumbents ignore. |
| **Greenfield superalloy foundry** | **Fatal for single-crystal; survivable narrowed** | Rotherham: about $170M and about 5 years. SpaceX Bastrop: $280M. Doncasters: $52M over 3 years as an incumbent ([Foundry Mag](https://www.foundrymag.com/molds-cores/article/21928462/rollsroyce-starts-up-foundry-for-turbine-blades); [foundry-planet](https://www.foundry-planet.com/d/spacex-plans-its-own-turbine-blade-foundry-in-texas-ai-boom-meets-casting-bottleneck)). Rangeview, about $5.6M raised, was still at development stage with Kratos about 4 years after seed. Government money comes in $1-25M cheques. | Start with equiaxed and DS parts, no single-crystal. Buy a small approved vacuum foundry; Chromalloy built a $30M captive Tampa foundry for its own repair network. Add printed cores (DDM, Lithoz) and process ML. Fund it with customer deposits; Howmet will not add IGT capacity without formal orders ([Eastern Progress](https://www.easternprogress.com/hwm-q2-earnings-call-centers-on-capacity-and-higher-outlook/article_2060fecf-8c40-5ca7-8728-4b9c6474e5f8.html)). |
| **Yield and tacit knowledge** | Unanswered (plausible) | Howmet's core design is "all proprietary". Automating wax patterns took that step from 80% to 95%+ yield at Rolls-Royce ([MTC](https://www.the-mtc.org/insights/automation-wax-pattern-production)). DDM's claimed 40% to 90% yield is a vendor claim. | A bought foundry brings data and people. ML needs that data, so the AI layer goes in after acquisition. |
| **"Any design in" end state** | **Fatal as stated** | TSMC: 59.9% gross margin. Jabil: ~5.4% operating. Flex: 6.3%. Xometry: −$61.7M net. Protolabs: ~4% net ([SEC Xometry](https://www.sec.gov/Archives/edgar/data/1657573/000119312526066959/xmtr-20251231.htm)). Shapeways (Ch. 7, 2024), Fast Radius (sold for ~$16M), Desktop Metal (Ch. 11, 2025). | Use the HEICO × Howmet shape: a library of certified part numbers with reusable evidence, a small set of frozen processes ("our process rules"), and pricing at 60-75% of OEM. TransDigm earns 53.9% EBITDA and HEICO 22.7% operating margin ([TDG](https://transdigmgroupinc.gcs-web.com/news-releases/news-release-details/transdigm-group-reports-fiscal-2025-fourth-quarter-and-year-end); [HEICO](https://www.sec.gov/Archives/edgar/data/46619/000004661925000076/a10312025ex991earningsrele.htm)). |
| **OEM lawsuits and IP** | **Answered** | Reverse engineering a lawfully bought part is not improper under the DTSA (§1839(6)(B)). HEICO beat Pratt & Whitney: the trade-secret claims were dismissed in 1997 and non-infringement was granted in 1998 ([SEC](https://www.sec.gov/Archives/edgar/data/0000046619/000095017098000125/0000950170-98-000125.txt)). OEMs win only when documents were taken: GE v. Feuz, Siemens' $104M DOJ settlement, the Zheng espionage case. | Use a clean room. Own every scanned part. Sign no reverse-engineering bans. Wall off ex-OEM hires. Run a freedom-to-operate check per part; 1980s-2000s frame patents have mostly expired. |
| **Warranties, LTSAs, controls lockout** | Survivable | OEMs warn against non-OEM parts, and Mark VIe software is GE-licensed. No hard part lockout was found. | Serve only out-of-warranty, post-LTSA and orphan units, and stay out of controls. |
| **A hot-section failure** | **Potentially fatal** | FM Global: about 20 turbine failures a year at about $100M each, with blades behind more than 75% of losses. One non-OEM 7EA bucket set lost half its tip shrouds ([Turbomachinery](https://www.turbomachinerymag.com/oems-advise-aftermarket-part-loyalty/)). Failures trace to material or process substitution. | Start with combustion, mid-section and later-stage parts. Build fleet hours before going to stage 1. CT scan and metallurgy on every serial. Carry product-liability cover sized for subrogation. |
| **Trust shock (AOG Technics)** | Answered, and a tailwind | AOG Technics forged paperwork on 60,000+ parts; its director was jailed in Feb 2026 ([Fox](https://www.foxnews.com/world/man-sentenced-selling-fake-airplane-parts-popular-engine.amp)). Buyers now want provenance they can verify. | Make the parts yourself and never broker them. Give each serial a digital record, which is something the OEM can't withhold. |
| **Shortage ends** | Survivable | GE Vernova goes from 20 GW/yr now to 24 GW in 2028 and 30 GW by 2030, with slots booked into 2031 ([GEV Q2](https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000147/gevpressrelease2q26.htm)). Rystad sees oversupply risk in 20-50 MW units by 2028. | Aftermarket parts burn on fixed inspection cycles whether or not new turbines sell. Qualified parts revenue must exist **by 2028**. |
| **AI capex pause, policy reversal** | Dangerous for owning a fleet; survivable for parts | UBS AI-capex growth: 76% (2026), 25% (2027), 6% (2028). The EPA repealed gas greenhouse-gas rules on 14 Sep 2026; reversal risk is around 2029. | This is the second reason parts come first. |
| **Antitrust and policy** | Tailwind | DOJ forced divestiture of PSM in 2015 and linked PSM to 60-70% price drops ([DOJ](https://www.justice.gov/opa/pr/justice-department-requires-general-electric-divest-aftermarket-business-order-complete)). FTC v. Deere settled on 8 Jul 2026. EU Data Act applies from Sep 2025. The Army is mandating right-to-repair clauses. | Use it in the pitch: regulators protect independent aftermarket sources. |

## The re-sequenced master plan (the version that lives)

1. **Now to 2028: Orphan parts house.** AI reverse-engineers combustion, mid-section and equiaxed parts for frames whose OEM support is gone or slow:
   - which frames: Westinghouse W501B/D, Alstom GT11N/GT13, P&W FT4, and older 6B/7EA;
   - how they get made: partner foundries and machine shops, with clean-room data packages;
   - what it costs: little capital.
   - The company owns the part-number library and its evidence.
2. **2027-30: Own the scarce capacity.** Buy one small approved vacuum foundry, using deposits and seller notes. Add printed cores and process ML, then DS parts. Sell quick-turn capacity to ISPs and new turbine makers. No single-crystal until the plant has its own yield record.
3. **2028+: Own the machines, in place.** Partner with or buy already-sited, permitted, grid-connected orphan units, ideally with PJM capacity rights. A Fermi-type price is about $158/kW. Run them as capacity and firm units, with DLN retrofits to stay inside permits. Finance with project debt once contracts and qualified parts exist. The fleet becomes the evidence generator and the first customer.
4. **Then: Breadth.** Carry the same library and process discipline to other industries:
   - nuclear commercial-grade dedication, with no NRC review up front;
   - orphan defence electronics, by buying product lines that hold their approvals;
   - naval castings;
   - aviation PMA, by buying a house with an ODA.
   - **End state:** the independent source of record for the world's aging machines, a "HEICO for everything" whose evidence works like a PDK.
   - **Prize:** OEM aftermarket pools of about $250-400B/yr (est.): aviation MRO $119B, gas-turbine services $27-48B, Caterpillar services $24B. A 3-4% share at 25% margin is about $9-12B of revenue (est.).

**Pitch line that survives.** "AI made code abundant. We make machines immortal. Today 45 GW of US turbines and countless defence and nuclear systems depend on parts nobody makes. We rebuild those parts with AI, prove them on our own machines, and become the independent source of record for the world's aging infrastructure."

## Rescore of the re-sequenced company
- **N4.** Little capital to first revenue. The foundry is funded by deposits. Fleet economics at about a 2-year payback come later.
- **T4.** First paid parts orders are possible in year 1. $100M revenue needs the foundry and fleet, around year 6-7.
- **C4.** HEICO ($4.5B sales) and TransDigm ($8.8B) are the scale proofs; $10B+ requires the breadth rung.
- **A4.** AI turns the long tail of orphan part numbers into something economic. Yield ML is plausible but unproven.
- **D3.** PSM, Ethos and Sulzer are in the common frames. SpaceX and GE/CPP are in castings. The moat is the orphan library, fleet hours and owned capacity.

**Total: 19/25, a narrow pass.** The literal plan (fleet first, "any part", greenfield single-crystal) scores about 14.

## Cheapest tests, and what a Demo Day could show
1. **Orphan demand (3 weeks, ~$5k).** Map turbine models onto the EIA-860 units using state air permits. Call 15 owners of W501D, GT11N, FT4 and older 6B/7EA units. **Kill if** fewer than 5 name a part with a lead time of 12 months or more at a price above $50k.
2. **One part (8-10 weeks, ~$40-80k).** Clean-room scan of one combustion or later-stage part. Cast it through a partner foundry, then run first-article and metallurgy. **Kill if** it fails acceptance twice, or comes out less than 30% below the OEM price.
3. **Insurer (2 weeks).** Talk to one HSB or FM Global underwriter. **Kill if** a fully documented non-OEM combustion part loads the premium more than 20%.
4. **Foundry target (6 weeks, ~$50k).** Get data rooms for 2-3 small approved vacuum casters. **Kill if** every one is priced above 8x EBITDA.
5. **Demo Day (W27, about March 2027).** One reverse-engineered part cast and accepted, one *paid* purchase order from an orphan-fleet operator, and one unit under LOI with a project-finance term sheet conditional on offtake. Starcloud's ~$21M seed out of Demo Day is the hard-tech benchmark.

## Gaps
- No public data on orphan-part prices or lead times, real used-turbine transaction prices beyond Fermi, DS yield curves, insurer pricing of non-OEM parts, or how long OEMs and insurers take to qualify a new caster.
- All of these need calls, not search.
- One synthesiser; five researchers, one per killer.
