# Cross-history pattern: how repair and knowledge monopolies break, and who ends up with the value

*Built from the research summaries [v01–z10] and the notes in `raw/*.md`. Evidence caveat: the shared web-search budget ran out early in the run, so most agents worked from direct page fetches plus knowledge they recalled. Figures marked (recalled) were not re-checked this session.*

## Bottom line

In every case examined, the monopoly that broke was **not mainly a knowledge monopoly**. Challengers almost always already knew how to do the work:
- Kodak's independent service organisations were cheaper and sometimes better than Kodak [v08].
- Plug-compatible makers had IBM-grade engineering [h03].
- HEICO held about 20,000 PMA approvals with "no material patents" [p06, h11].
- Generic drug chemistry was easy to copy [h02].
- Guild secrets were in print from 1555 [h04].

What held each monopoly together was **permission**: the legal right to connect, install, sign or sell; a cryptographic key; an accepted standard of proof. Each one broke when a **regulator, court or standards body changed what counted as acceptable proof or access**. Once it broke, the rent did not disappear. It **moved to the next scarce layer**: verification, distribution density, physical capacity, liability-bearing sign-off, or proprietary outcome data. The party that spread the knowledge almost never kept the value.

## Case table

| Case | What held the monopoly | What broke it | Time to break | Price effect | New scarce layer | Who captured value | IDs |
|---|---|---|---|---|---|---|---|
| **US auto aftermarket** | OEM parts and manuals, later dealer-only diagnostics | Distribution networks (NAPA 1925 on); third-party manuals (Chilton, MOTOR, Haynes, ALLDATA); Magnuson-Moss 1975; OBD rules; Massachusetts ballot 2012 (86%) → national MOU 2014 | About 90 years overall; about 2 years from the ballot to the MOU | Aftermarket parts 15–50% cheaper; independents hold 70–75% of post-warranty work. Total repair cost still **rose** (collision severity +63% 2015–24) | Parts inventory within hours, store density, then telematics, security gateways, VIN-paired modules, ADAS calibration capital | Dense parts retailers (AutoZone and O'Reilly, about 19% operating margin, about $2.4–2.5B net income each). Haynes sold for only £114.5M. Advance Auto, at similar scale, runs near 0% margin | h01, v05, s04, s05, k04, u04 |
| **Heavy trucks** | Dealer and OEM diagnostics | Industry MOU around 2015 (recalled) | Fast once agreed | Downtime still about $1,500 per truck-day | Coordination and authorisation latency; diesel technicians (52% gap); certified emissions parts | The coordination platform (Decisiv, about 60% of North American commercial vehicles) | e09 |
| **Deere / ag** | Service ADVISOR, payload files, DTAC case base, DEF derates | Antitrust and FTC: $99M class settlement (Apr 2026); FTC/state order with 10 years of dealer-equivalent tools (Jul 2026); EPA derate guidance | About 8 years of advocacy; tool price fell **about 16x ($3,160 → $195 per machine per year) within months** of the FTC suit | Settlement about $500 per class member, against PIRG's estimated $4.2B/yr harm (advocacy source) | Field technician hands in harvest windows; telematics data ownership; pairing and calibration as a service | Not yet settled. The lock was technically shallow (DEF CON 2022 jailbreak); the barrier was legal | v01, v03, v04, z01, z03 |
| **Aviation PMA / DER / USM** | OEM type design, ICA, licences, warranties, power-by-the-hour terms, lessor return conditions | FAA legal route (CAR 1.55 in 1956, FAR 21.303 in 1965); 1990s enforcement plus airline capital (Lufthansa Technik took 20% of HEICO); competition terms on CFM56 | About 35+ years from legal route to real industry. Still a low single-digit share of parts (recalled) | PMA about 30–40% below OEM (recalled); USM caps OEM pricing | Certification throughput (HEICO adds about 400–550 approvals a year); FAA reviewer capacity; DER liability; feedstock; records integrity | HEICO (about 21–24% operating margin; about half of TransDigm's ~47%), FTAI (aerospace revenue about 3.5x in 2 years on 25-year-old engines), AerSale (owned parts at 35–39% gross vs 17% on labour). TransDigm **bought PMA makers for $2.2B (Jan 2026)** | h11, p06, o05, m01, m05, x02 |
| **Gas turbine service** | GE fleet data, LTSAs, castings, warranties, lender and insurer acceptance | Independent service providers enter after 8–16 years; EC forced divestment of PSM | 8–16 years per frame | PSM's 7F parts extend intervals (32k+ hours vs 24k) | Superalloy casting capacity; proven fleet hours; risk-transfer wrapper | The OEM keeps over 90% on new frames; independents win on mature frames; Calpine insourced | e01, o01 |
| **Generic drugs (Hatch-Waxman 1984)** | Repeat-trial rule plus patents. Not knowledge | **Changing the standard of proof**: bioequivalence against a reference product replaced repeat efficacy trials | Months once the law passed; 13% → 90% of prescriptions over 40 years | >95% unit price collapse, but only after about 6 verified suppliers; generics are 12% of spend | Manufacturing quality, data integrity, supply resilience; pay-for-delay ($3.5B/yr) | **Payers.** Teva lost $1.64B in 2024; Teva and Mylan turned to price-fixing and chokepoint products (EpiPen). Verification was corrupted within 5 years (1989 scandal) and again with Ranbaxy | h02 |
| **Carterfone / Part 68** | Bell's "harm to the network" veto | Hush-A-Phone 1956 → Carterfone 1968 → Part 68 registration → divestiture 1984 | About 28 years | Equipment became a commodity; owners took on wiring and repair costs; basic service prices rose; many kept paying leases above purchase price | Neutral certification and published interfaces | Equipment buyers, certification labs; AT&T broken up | h03 |
| **IBM plug-compatibles** | Interfaces, maintenance refusal, software licensing | Antitrust settlements, GSA procurement anchor, Amdahl entering maintenance itself | About 1–2 decades, then **re-closed** | Prices cut | Interface cadence, software licences | IBM: Telex and Memorex failed; IBM bought the emulator maker PSI and closed mainframes again by about 2000 | h03 |
| **Kodak / Xerox / Intuitive aftermarkets** | Parts refusal, copyrighted software, usage chips | Kodak 1992 (Supreme Court); Ninth Circuit revived SIS v Intuitive (Aug 2026) | About 10 years per case; Kodak's practical legacy near zero for 20 years | Aftermarket margins stayed high | Lexmark 2017 weakened patents → lock moved to chips and pairing | OEMs mostly. Plaintiffs usually lost | v08, z01 |
| **Medical device independents** | Service keys, DMCA, gated training (one course about 80% of device price) | FDA 2018 found independent servicing about as safe; DMCA 1201 exemptions | Still in progress; locks moving into OEM clouds as priced tiers (Philips Levels 0–3) | Estimated 20–40% savings on service spend; OEM labour $600–800/hr vs $150–200/hr | Telemetry ownership; evidence and traceability layer; biomed workforce | OEMs still (GE HealthCare service about 52% gross margin) | v06, v09, k01 |
| **Elevators** | Controller software, parts, contract conversion; EU cartel 2007 that covered maintenance | Independents already service about 50% of units | Ongoing | Otis service margin 25% vs 4.8% on new equipment | Route density, licensed labour, mandated inspection | OEMs; KONE+TKE merger justified by route density | m10 |
| **Craft guilds** | Legal privilege plus embodied skill | **Legal abolition** (Turgot 1776, Le Chapelier 1791). Printed "books of secrets" (1555) and the Encyclopédie (1751–72) did *not* end it | About 236 years from cheap print to abolition in France | Rents lasted until privilege was removed | Certification and the master's mark; skilled "mechanics" who could absorb codified knowledge | States and the absorbing upper tail of skilled people (Encyclopédie subscriptions predict growth; literacy does not) | h04 |
| **Open source / Stack Overflow / AI coding** | Proprietary code | Free licences, free Q&A, LLMs | About 20 years | Maintenance still about 42% of developer time; AI on mature repos from −19% to +18% (METR) | Accountability (certification, SLAs), operated lifecycle, proprietary data | Red Hat ($34B), AWS ($45.6B operating income), model owners licensing the commons. 60% of maintainers unpaid; Stack Overflow questions −78% | h08 |
| **Shanzhai / Huaqiangbei** | Phone design know-how | MediaTek *deliberately* released turnkey reference designs (gongkai) | A few years | Build cost cut about 5–10x; about 20% of the global 2G market briefly | Core silicon and displays; parts liquidity; microsoldering hands; OEM cryptographic pairing | MediaTek (owner of the scarce layer) and parts traders. A $12 phone made repair irrational | h09 |
| **Remanufacturing** | OEM engineering data, cores, dealer channel | Independent remanufacturers plus retailer channels | Mature; stuck at about 2% of manufacturing for decades (recalled) | Independents earn about 20% gross | Core supply and working capital (MPA holds about $298M of cores on retailer shelves) | Retailers (3 take 85% of MPA sales) and OEMs (Caterpillar bought independent remanufacturers) | h10 |
| **Legal, tax, travel, real estate** | Information plus licence | Online booking, free software, listing portals | Travel: about 10–15 years. Real estate: commissions held at 5–6% for about 20 years after listings went public, until the 2023 Burnett verdict | Travel collapsed. Tax: Free File used by 2.7% of eligible filers; IRS Direct File killed in 2025 | The licensed, liability-bearing signature; coordination rules (MLS); defaults; lobbying | Licensed incumbents. LegalZoom's endgame was *owning* a law firm (Arizona ABS) | h07 |
| **Healthcare task-shifting** | Physician licence | NP scope-of-practice laws, telehealth waivers, autonomous FDA-cleared AI | Decades | Episode cost moved to tests and referrals; telehealth covers about 5% of claims | Accountable sign-off plus billing codes | Licensed providers. LLM alone 92% vs physicians using the LLM 76% on vignettes | h12, d02 |
| **On-demand manufacturing** | Quoting and manufacturability know-how | Instant quoting | About 7 years | Protolabs operating margin about 20% → 4.7%; Xometry 2.7% adjusted EBITDA | Owned certified automated capacity (Hadrian) | **Buyers.** Fictiv folded into MISUMI | x04, l03 |
| **Collision photo-estimating** | Appraiser time | Tractable and similar AI (90% of estimates with no human appraiser) | About 5 years | Appraisal went from days to minutes; repair cost still rose | Parts, labour, ADAS calibration, payer data | Insurers and the data platform (CCC, Mitchell); Tractable distributes through Mitchell | s05, x03 |
| **RCM / MSG (aviation, 1960s–78)** | Fixed-overhaul doctrine (not a monopoly) | Pooled fleet data plus decision logic in a joint airline/OEM/FAA forum | About 15 years | **The one real 10x+**: structural inspection about 4M → 66k man-hours (DC-8 → 747) (recalled) | Fleet failure data; authority to change maintenance programmes | Airlines and the system as a whole; written into regulation | n02, k05 |
| **Scarcity economies** (Cuba, USSR, sanctioned Russia and Iran) | — (knowledge was a commons) | n/a | n/a | Assets kept running at a cost to safety | Certified parts plus sign-off authority | Nobody. Cannibalisation and grey imports (about €1B for Russia, recalled) | h05 |

## Cross-case regularities

**1. What broke it.** In about 15 of the 18 cases, the trigger was a change in **law, standard of proof or certification**: Hatch-Waxman bioequivalence, Part 68 registration, PMA rules, the Massachusetts ballot and MOU, the FTC v Deere order, Turgot and Le Chapelier, Burnett. Technology and knowledge diffusion came first by years or centuries without breaking anything: printing before the guilds fell, public listings before real estate commissions moved, free tax software before Free File uptake, YouTube before DIY auto repair (DIY share actually shrank) [h04, h07, u04].

The exceptions are where the *owner of the scarce layer chose* to release knowledge (MediaTek with shanzhai), and where the transaction was unlicensed, low-stakes and fully digital (travel booking) [h09, h07].

**2. How long it took.** Without a legal shock, decades to centuries: PMA about 35 years, Carterfone about 28, guilds about 236 after print, real estate commissions about 20 after listings went public. Once law moved, months to a few years: Deere tool price −16x in months, ANDA filings straight after 1984, about 2 years from the Massachusetts ballot to the MOU.

But **mandates without enforcement stall**. The 2020 Massachusetts telematics vote is still in litigation six years on. No state attorney general has enforced an electronics repair law. Military right-to-repair was stripped in conference in December 2025 [v03, v05, v10].

**3. What happened to prices.** Prices fell in proportion to the **number of verified, accepted entrants**, not to how widely the knowledge spread:
- One certified alternative takes off roughly 30–40% (PMA, recalled), or roughly 15–50% for auto aftermarket parts.
- About six verified generic suppliers take off more than 95% [h02].
- Total system cost often **rose** while unit prices fell. Collision severity was +63% with open repair data [s05]. Software maintenance load grew [h08]. Telecom owners took on wiring costs [h03].
- Cheaper access released latent demand. Apple's $29 battery programme did 11M+ replacements against 1–2M expected [s02, q04].

**4. The new scarce layer.** It was always one of five:
- **(a) Verification and certification throughput**: bioequivalence, FAA approvals, Part 68 labs, commercial-grade dedication.
- **(b) Cryptographic and legal authorisation**: pairing, keys, return-to-service signatures.
- **(c) Physical liquidity and density**: parts within hours, cores, rotables, route density, technician hands.
- **(d) Physical capacity**: castings, test cells, docks, shop slots.
- **(e) Proprietary outcome data and telemetry.**

The same move shows up inside AI-era incumbents. OEMs are the leading deployers of AI and telemetry in elevators, mining, fab tools and gas turbines [m10, m13, m09, e01].

**5. Who captured value.** Not the knowledge producer: Haynes, Stack Overflow, Red Hat's upstream maintainers, the Encyclopédie, Predix's $7B+ bet [x07]. The value went to whoever owned the adjacent layer:
- **Distribution density**: AutoZone, O'Reilly, Fastenal (20% operating margin on vending and onsite stock vs Applied's 11% on technical knowledge) [p04].
- **Payers**: generics, collision insurers.
- **Accountability or certification holders**: HEICO, Red Hat, licensed agents.
- **Operated-lifecycle providers**: AWS, Rolls-Royce TotalCare, which repriced its risk transfer [o03].
- **Acquiring incumbents**: IBM buying PSI, TransDigm's $2.2B PMA purchase, Caterpillar buying remanufacturers, Asurion absorbing uBreakiFix and Domestic & General [x06].

## Test of the sibling-thread hypothesis

*"Knowledge levels → monopoly moves to approvals, test evidence, installed fleets and scarce factories; the leveller rarely keeps value; hardware goes generic at 30–70% of OEM price; best shape is an orphan-parts house growing toward 'HEICO for everything'."*

- **Monopoly migrates, leveller doesn't keep value: strongly supported** across all 18 cases.
- **"30–70% of OEM price": partly supported.** It holds for single-entrant certified domains: PMA at about 60–70% of OEM price, medical independents 20–40% cheaper. It is wrong as a general law. Price depends on entrant count. Where certification throughput is high and the product is a commodity, prices go to about 5% of brand (generics). Where throughput is rationed (about 500 approvals a year), they stay near 60–70%. The "physics clock" is really a **certification-throughput clock** plus capacity.
- **Orphan-parts house: supported, with three amendments.**
  1. Independents win **late in the lifecycle**: FTAI on 25-year-old engines; CFM56 overhauls spread across about 40 shops with the OEM doing about a third; gas-turbine independents entering after 8–16 years; Rochester Electronics at about 12B die under licence from 70+ OEMs [m05, m01, e01, p01].
  2. The moat is **approval track record plus feedstock plus records**, not fabrication. Every "parts factory" that skipped certification failed or shrank (Fast Radius, Shapeways, Maersk onboard printing) [l02, l03].
  3. **Expect to be bought, not to stay independent**: TransDigm bought PMA makers [x02]. HEICO's ~23% margin is real but is about half of TransDigm's, so certified competition narrows the rent without removing it [o05].
- **Not supported: "AI erases the knowledge gap, so the industry rebuilds."** In the cost data, knowledge or diagnosis is 5–15% of engine shop-visit cost [m01, r02], about 12% of community repair failures [v07], and a 10–26% recoverable slice in field service [m06, s03]. The only measured 10x gains came from removing unnecessary work (RCM [n02]), standardised hardware (RecX transformers [e02]), redundancy (hyperscalers [m14]), or prediction plus logistics (Delta [d01]). None came from cheaper knowledge.

## Laws: who wins when AI makes repair knowledge abundant

**Law 1. Knowledge is never the last lock.** When know-how commoditises, rent moves to the **permission layer**: the right to install, sign, pair or connect. The winner is whoever holds or manufactures that permission. Examples: guilds → certification [h04]; Lexmark patents → chips [v08]; manuals → cryptographic pairing [v03, s02]; F-35 data rights [q03]. *Prediction:* AI-native **approved-data and sign-off organisations** (DER/DOA houses, Part 145 stations, accredited dedication labs) capture more than AI diagnosis vendors.

**Law 2. Monopolies fall when the standard of proof changes, not when knowledge spreads.** The time constant is decades without a legal or standards shock and months with one. Examples: Hatch-Waxman [h02], Part 68 [h03], Massachusetts/MOU [h01], FTC v Deere's 16x tool-price cut [v04]. *Prediction:* the biggest AI-era value event in repair is a regulator accepting an **AI-generated equivalence or qualification package**, the "bioequivalence for parts" (EASA NPA 2025-07, 10 USC 3243(e) expedited qualification [i03, p06]). Whoever writes that test protocol, and is first to pass it, gets the first-filer rent.

**Law 3. The leveller doesn't keep the value; the adjacent layer does.** The knowledge producer is absorbed as a free add-on by whoever owns distribution, payment or accountability. Examples: Haynes vs AutoZone [h01]; ALLDATA inside AutoZone and Mitchell 1 inside Snap-on [h01]; Stack Overflow vs model owners [h08]; Tractable via Mitchell [s05]; Protolabs and Xometry margins passing to buyers [x04]. *Prediction:* standalone AI repair copilots get bundled by OEMs, field-service platforms and parts sellers. Durable profit goes to whoever owns **parts liquidity, payment or claims, or the liability wrapper**.

**Law 4. Price falls with the number of verified entrants, and certification throughput sets that number.** One accepted alternative gives about a 30–40% discount; about six give more than 95% [h02, h11, o05]. Unverified abundance gives counterfeits, not lower prices: GAO's sting found 16/16 bad parts, and AOG Technics put 60,000 forged parts into the fleet [p01, p02]. *Prediction:* AI-assisted substantiation that multiplies approvals per year (HEICO manages about 500) is worth more than any fabrication capability. The first two or three entrants per part family earn the margin.

**Law 5. Abundance creates a trust deficit, and verification becomes the scarce layer, which is then attacked.** Examples: the 1989 generics scandal and Ranbaxy [h02]; AOG Technics [p02]; AI lowering forgery cost [p02, p03]; policy tightening toward authorised-source preference after counterfeit scandals [p02]. *Prediction:* winners include **signed digital release certificates, provenance graphs and independent inspection that is not chosen or paid by the inspected party** [z05, z08, i02]. Inspection grows in a world with more AI; it does not shrink [i01].

**Law 6. Incumbents re-lock at the next layer and buy the breakers.** Examples: IBM/PSI [h03]; TransDigm's $2.2B PMA purchase [x02]; Caterpillar buying remanufacturers [h10]; Asurion consolidating [x06, x07]; OEMs owning the AI telemetry [m09, m10, m13, e01]; medical OEMs pricing cloud service tiers [v09]. *Prediction:* an AI repair entrant either (a) owns a layer the OEM structurally can't re-lock: owner-controlled data rights, regulator-compelled access (the 10-year Deere order), orphaned fleets the OEM has walked away from; or (b) is built to be acquired. "Fight the OEM on its current fleet" loses.

**Law 7. Cheap knowledge raises volume more than it cuts total cost (Jevons), so the scarce input becomes hands and capacity.** Examples: Apple batteries 11M vs 1–2M [s02]; radiologist demand rising after AI [d02]; software maintenance staying around 42% [h08]; auto repair cost rising after 2014 [k04]; downtime cost per hour doubling as downtime hours fall [z06, q02]. *Prediction:* value goes to whoever owns **certified technician-hours, shop and dock slots, rotable pools and pre-positioned parts**, and to whoever sells **outcome or risk contracts** priced on uptime (power-by-the-hour, Asurion-style protection plans, Mantle-style uptime operators) [o03, x06, x05].

**Law 8. Independents win at the end of the lifecycle, not the frontier.** The OEM monopoly decays on a clock of roughly 8–16 years, and the orphaned tail is where independents compound. Examples: FTAI [m05]; CFM56's 40 shops [m01]; gas turbines [e01]; Rochester [p01]; orphaned inverters (Fimer, SunPower, Powin) [e07]; dead e-bike brands [s07]; legacy PLCs [e05]; obsolete rail electronics [m12]. *Prediction:* the strongest company shape remains an **orphan or late-life fleet house**: approval track record, feedstock and teardown, records integrity, pooled spares, then an uptime contract on top. It expands one installed base at a time rather than as "an AI parts factory for everything".

## What this predicts in one table

| Likely winners | Likely losers |
|---|---|
| Approved-data and sign-off holders using AI internally (DER/DOA, Part 145, dedication labs) [i02, h07] | Standalone AI diagnosis or knowledge apps [h01, h08, x01, x07] |
| Verification and provenance infrastructure (signed certificates, POD-qualification-as-a-service) [p02, i01, i03] | Lead-gen and matching marketplaces (Angi spends about 49% of revenue on marketing; Homejoy, Handy) [s06, x07] |
| Parts liquidity, teardown and rotable pools with trusted records [m05, z09, h09] | Uncertified on-demand parts factories (Fast Radius, Shapeways) [l03, x04] |
| Risk-bearing uptime and outcome contractors [o03, x06, z05] | Horizontal predictive-maintenance platforms (Predix, Uptake, C3, AWS Monitron) [n01, n03] |
| Owners of closed-loop outcome data (symptom → fix → result) [u05, d02, z08] | Brute litigation against an OEM's current fleet without a legal unlock [v08] |

## Main caveats

- Many figures were recalled because search was unavailable: PMA market share and discounts, ANDA cost, the remanufacturing share of manufacturing, RCM man-hours, HEICO and TransDigm margins [o05, h11, h10, n02].
- The 2026 Deere settlements come from Wikipedia and still need docket confirmation [z01].
- The PIRG harm estimates come from an advocacy source, and CEI's estimate is about 7x lower [v07].

Raw notes: `raw/` (h01–h12, p06, o05, m05, x02–x04, v04, v08, z01, k04 are the most load-bearing for this synthesis).