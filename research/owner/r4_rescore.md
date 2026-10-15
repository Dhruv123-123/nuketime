# Round 4: every candidate rescored on the corrected test

Written 15 Oct 2026. Inputs: ROUND4.md, all `lane_*.md`, `r2_*.md`, `r3_*.md`, `redteam_*.md`,
`research/converge/PICK8.md` and `proof/attrition_results.json`. I used 8 WebSearch calls, all on
crowding checks for revived ideas (listed at the end).

## The test, and how I scored it

Each part scores 0, 1 or 2. The maximum is 8.

| Part | 2 means | 1 means | 0 means |
|---|---|---|---|
| **P1 Buy blind** | The seller and rival buyers cannot see the true value, so the price is set too low | Some sellers are blind, but brokers, funds or strategics price most deals | The price is set by an auction, tender or informed owner who sees the value, or nothing is bought at all |
| **P2 ML unlocks it** | The value can only be estimated at scale by inference over illegible public data: sparse, messy, multi-modal, with no lookup that gets you there | ML helps (triage, extraction, speed), but a lookup, a join or an expert reading by hand does most of the work | The data step is a lookup or a join, or a backtest shows ML adds nothing |
| **P3 Spread** | The asset is worth several times its price once the value is known | It is worth a modest premium (tens of percent) or the hits are rare | There is no reliable spread |
| **P4 Realise it** | The company develops, operates or sells the output itself | It realises the value only through a discretionary gatekeeper (a contracting officer, court, regulator approval, or a monopsony of buyers) | Realising it needs an incumbent's channel, or it is an analytics or service business |

**Sector**: IN = energy, machines, robotics, deeptech, security (Dhruv, 04:31Z). SEC = secondary.

I was strict on P2. A 2 was given only where no public table, commercial database or competent
analyst reading by hand can produce the valuation. Our two backtests count as evidence. The queue
backtest scored 0.721 AUC for the model against 0.727 for a type x phase lookup, so queue ideas get
P2 = 0. The drug-gap proof was built entirely from joins, and redteam_drugs found the useful pool
enumerable in IQVIA and Citeline, so foreign-approved drugs get P2 = 0.

**Bought-kill**: Y means rounds 1-3 killed or capped the idea mainly because the right had to be
bought, had an owner, or was sold by tender. The revival verdict for each Y is in section 3.

## 1. Full table

| # | Idea (source) | Sector | P1 | P2 | P3 | P4 | Total /8 | Bought-kill | Ceiling note |
|---|---|---|---|---|---|---|---|---|---|
| **Energy and grid** |||||||||||
| 1 | Queue-attrition arbitrage: option land where capacity frees (lane_energy C1; PICK8) | IN | 1 | 0 | 1 | 2 | 4 | N | $2-5B on paper. Our backtest found no ML edge, and Cloverleaf, Tract and GridCARE hold the position |
| 2 | ERCOT Batch Zero fallout map (lane_energy C2) | IN | 1 | 0 | 1 | 2 | 4 | N | $0.3-1.5B. One-off window to 2027 |
| 3 | Retiring-plant interconnection rights, "brownfield headroom" (lane_energy C3) | IN | 1 | 0 | 2 | 2 | 5 | **Y** | Multi-billion, but owners and IPPs capture it. Retirement prediction runs on structured EIA-860 data |
| 4 | Hydro preliminary permits at non-powered dams (lane_energy C4, lane_wild, lane_earth) | IN | 0 | 0 | 0 | 1 | 1 | N | Tens of $M |
| 5 | Offshore and onshore wind or solar lease rounds (lane_energy C5) | IN | 0 | 0 | 0 | 1 | 1 | Y (auction) | Policy is hostile. ML only helps you bid |
| 6 | Transmission rights of way (lane_energy C5) | IN | 0 | 0 | 1 | 0 | 1 | Y | Utilities hold them, with eminent domain |
| 7 | Utility hosting-capacity maps (lane_energy C5) | IN | 0 | 0 | 0 | 1 | 1 | N | Sites under 20 MW. LandGate and Paces already ingest the maps |
| 8 | Firm gas-pipeline capacity (lane_energy C5) | IN | 1 | 0 | 1 | 1 | 3 | N | Tariff recall rules. Close to the banned gas lane |
| 9 | Nonattainment ERC "offset mining": buy sources to shut down and bank the credits (lane_built C1) | IN | 1 | 1 | 2 | 2 | 6 | N | $0.5-1.5B stock. **New 2026 headwind**: Texas data-centre turbines are using minor permits that need no offsets (search 6) |
| 10 | Data-centre moratorium and vesting arbitrage (lane_built C2) | IN | 1 | 1 | 1 | 2 | 5 | N | $2-4B in principle. Tract and GatherGov are already there |
| 11 | Stranded never-fired turbines worldwide, the Hallador model (r3_energy_hw B) | IN | 1 | 1 | 2 | 2 | 6 | **Y** | $1-5B one-off spread, open until about 2029-31. ML finds the units, but pricing them is a $/kW lookup |
| 12 | Idle transformers and GSUs at retired plants (r3_energy_hw A) | IN | 1 | 0 | 1 | 2 | 4 | **Y** | Low $B. Large units are not fungible. Sunbelt Solomon and Maddox are in it |
| 13 | Undervalued or restartable PJM units (r3_energy_hw C) | IN | 0 | 0 | 1 | 2 | 3 | Y | Priced by Vistra, NRG and Constellation |
| 14 | Behind-the-meter gensets found through air permits (r3_energy_hw D) | IN | 0 | 1 | 0 | 1 | 2 | N | Aggregation service. AGent Energy and Enchanted Rock are in it |
| 15 | OEM turbine slot reservations (r3_energy_hw E) | IN | 0 | 0 | 1 | 1 | 2 | N | Assignment needs the OEM's consent. No data |
| 16 | Buy retired plants whole, part out, keep the site (r3_energy_hw F) | IN | 1 | 0 | 1 | 2 | 4 | **Y** | Dealers already work the retirement list. Owners now keep sites for data centres |
| 17 | Retired aircraft engines converted to gensets (r3_energy_hw G) | IN | 0 | 0 | 1 | 2 | 3 | N | FTAI and ProEnergy |
| 18 | Underperforming solar and wind plants bought on a public-data screen, fixed by robotic O&M (r3_robotics 3) | IN | 1 | 2 | 1 | 2 | 6 | **Y** (partly) | Asset-sized: the US fleet is worth hundreds of $B. The edge is a 5-15% output uplift on plants bought at trailing-output prices |
| **Nuclear** |||||||||||
| 19 | Decommissioning-trust arbitrage (r3_nuclear 1) | IN | 0 | 0 | 0 | 1 | 1 | Y | Trusts are roughly fully funded. 0-3 plants in 15 years |
| 20 | Nuclear site banking (r3_nuclear 2) | IN | 0 | 1 | 2 | 1 | 4 | **Y** | Sites are worth $0.1-2.7B, but sellers read the same ADAMS docket |
| 21 | DOE spent-fuel damages claims (r3_nuclear 3a) | IN | 0 | 0 | 1 | 0 | 1 | N (law) | The Anti-Assignment Act blocks buying the claims |
| 22 | Dormant COLs and ESPs (r3_nuclear 3b) | IN | 0 | 1 | 1 | 1 | 3 | **Y** | Utilities are reviving them themselves |
| 23 | Cancelled-plant components (r3_nuclear 3c) | IN | 1 | 0 | 0 | 1 | 2 | Y | The restart pool is exhausted |
| 24 | DOE land for AI and energy parks (r3_nuclear 3d) | IN | 0 | 0 | 1 | 1 | 2 | Y (RFP) | Hyperscalers win the RFPs |
| 25 | Licensed LLRW disposal capacity (r3_nuclear 3e) | IN | 0 | 0 | 1 | 1 | 2 | N | A new licence takes about 10 years |
| **Robotics and machines** |||||||||||
| 26 | Robotic landfill mining for airspace (r3_robotics 1) | IN | 1 | 1 | 2 | 1 | 5 | **Y** | $50-500M per site, but only the owner captures airspace. About 12 projects ever, so almost no training labels |
| 27 | Buy retired telco copper in place (r3_robotics 2) | IN | 1 | 1 | 1 | 2 | 5 | **Y** (tender) | US profit pool under $1B. TXO and EMR are in it |
| 28 | Out-of-service subsea cable recovery (r3_robotics 4) | IN | 1 | 1 | 0 | 2 | 4 | Y | $1-3B gross. OEC and Mertech hold it |
| 29 | Modern abandoned wrecks (r3_robotics 5) | IN | 0 | 1 | 1 | 1 | 3 | N | Insurers keep title |
| 30 | Engine and aircraft part-out (r3_robotics 6) | IN | 0 | 0 | 1 | 2 | 3 | Y | FTAI, about $24B |
| 31 | Robotic e-waste and data-centre hardware recovery (r3_robotics 7) | IN | 0 | 0 | 1 | 2 | 3 | N | Molg, ITRenew, Sims |
| 32 | Robotic shipbreaking (r3_robotics 8) | IN | 0 | 0 | 0 | 2 | 2 | N | Thin margins. Cash buyers already use AIS |
| 33 | Buy idle factories and automate them (r3_robotics 9) | IN | 1 | 0 | 1 | 2 | 4 | Y | Isembard, Re:Build, Hadrian |
| 34 | Owned MRF and C&D sorting plants (r3_robotics 10) | IN | 0 | 0 | 1 | 2 | 3 | N | AMP |
| 35 | Robotic deconstruction for reclaimed lumber (r3_robotics 11) | IN | 0 | 0 | 0 | 2 | 2 | N | Small. Urban Machine |
| **Deeptech, defence and space** |||||||||||
| 36 | **Lineage**: buy dormant SBIR lineages for the Phase III sole-source path (r3_deeptech A, redteam_sbir, PICK8) | IN | 1 | 1 | 2 | 1 | 5 | **Y** (partly) | A BlueHalo-type company is worth about $4B, but a contracting officer gates every award (G2 Ops) |
| 37 | Phase III "wrapper" acquirer, using post-2019 lineages as the SBIR-derived component of a system (redteam_sbir reframing) | IN | 1 | 1 | 2 | 1 | 5 | Y | As above. Section 8 FPDS linkage turns the data step into a join over time |
| 38 | First qualified replacement for obsolete defence parts (r3_deeptech B, r2_certify DLA) | IN | 0 | 1 | 0 | 1 | 2 | N | Breaking a part out to competition destroys its margin |
| 39 | Authorised aftermarket for end-of-life chips, the Rochester model (r3_deeptech B2) | IN | 1 | 1 | 2 | 2 | 6 | **Y** (OEM negotiation) | Rochester, Micross and Flip hold it. Each line is negotiated with the OEM |
| 40 | Insurer-owned dead satellites (r3_deeptech C) | IN | 1 | 0 | 1 | 1 | 3 | Y | A handful of total losses a year |
| 41 | Orbital servicing contracts (r3_deeptech C2) | IN | 0 | 0 | 0 | 0 | 0 | N | A service market |
| 42 | Abandoned national-lab and ARPA-E tech licensed in (r3_deeptech D) | IN | 1 | 1 | 0 | 1 | 3 | N | Federal licence income about $180M a year. Patents on abandoned tech have often expired |
| 43 | Sole qualified QPL/QML source (r3_deeptech E) | IN | 0 | 0 | 1 | 1 | 2 | N | Lookup |
| 44 | Pending patent families with early priority dates whose specs read on today's energy and robotics products (lane_claims C2) | IN | 2 | 2 | 1 | 1 | 6 | N | Nine- and ten-figure single families, realised through licensing or courts (PTAB and §101 risk). An NPE business |
| 45 | AI materials discovery (lane_materials kill list) | IN | 0 | 1 | 1 | 2 | 4 | N | Periodic Labs, Lila, CuspAI. Amgen enablement risk |
| 46 | Patents on PFAS, Cr(VI) and REACH substitutes (lane_materials C3) | IN | 0 | 1 | 1 | 1 | 3 | N | The cleanest target, PFAS-free PAGs, is a few hundred $M. Resist makers hold the chemistry |
| 47 | Battery, magnet and refrigerant materials whitespace (lane_materials kill list) | IN | 0 | 1 | 1 | 2 | 4 | N | Chemix, Niron. The refrigerant space is exhausted |
| **Spectrum and space rights** |||||||||||
| 48 | D2D/MSS spectrum-rights aggregation (lane_claims C1) | IN | 1 | 0 | 2 | 0 | 3 | Y | $40B of deals, but about six strategic buyers |
| 49 | Dormant senior ITU L/S-band priority bought from dead satcos (r2_claims deep check 1, r2_itu) | IN | 1 | 0 | 2 | 0 | 3 | **Y** | 5-15 assets worldwide, about $0.1-0.5B. The data is structured, and a consultant found the AST seller in hours |
| 50 | New ITU filings (r2_claims) | IN | 0 | 0 | 0 | 0 | 0 | N | Junior to every existing filing |
| 51 | National MSS/D2D licences in small markets (r2_claims) | IN | 1 | 0 | 1 | 1 | 3 | N | Tens of $M per country |
| 52 | Other telecom first-come regimes: FCC Part 25 queue, Part 101 links, Ofcom shared access, AFRINIC IPv4, gTLDs, landing rights, cable landing (r2_claims) | IN | 0 | 0 | 0 | 1 | 1 | N | Small, or allocated by discretion or auction |
| 53 | Terrestrial FCC auctions (lane_claims) | IN | 0 | 0 | 0 | 1 | 1 | Y (auction) | Pricing skill against carriers |
| **Security** |||||||||||
| 54 | Inverter installed-base map leading to a domestic control-plane retrofit (r3_security 1a) | IN | 0 | 1 | 1 | 1 | 3 | N | $0.2-3B, depending on a rule that does not exist yet |
| 55 | Drone fleet transition (r3_security 1b) | IN | 0 | 0 | 1 | 2 | 3 | N | BRINC and Skydio |
| 56 | Rip-and-replace distressed carriers (r3_security 1c) | IN | 1 | 0 | 0 | 1 | 2 | Y | Small |
| 57 | Maintainer of record for EOL open source (r3_security 2a) | IN | 0 | 1 | 0 | 1 | 2 | N | A services market. HeroDevs, Chainguard |
| 58 | **Buy orphaned OT/ICS software and firmware product lines** (r3_security 2b) | IN | 2 | 1 | 2 | 2 | 7 | **Y** | $5-100M per line. A Constellation-style roll-up compounds into billions |
| 59 | AI vulnerability discovery with an owned outcome (r3_security 3) | IN | 0 | 1 | 0 | 1 | 2 | N | Bounty pool under $0.1B a year |
| 60 | Dormant legacy IPv4 blocks of defunct holders (r3_security 4a, PICK8) | IN | 2 | 1 | 2 | 2 | 7 | **Y** (owner) | **Fails the ceiling**: $0.6-1.8B one-off and shrinking. Hilco and Brander already hunt these blocks |
| 61 | Abandoned buckets, domains and package names (r3_security 4b) | IN | 0 | 0 | 0 | 0 | 0 | N | Only defensive value |
| 62 | First to certify, or CNA for orphaned products (r3_security 4c) | IN | 0 | 0 | 0 | 1 | 1 | N | Lab economics |
| **Aviation and parts certification** |||||||||||
| 63 | Aviation PMA first-mover parts (r2_certify 1) | IN | 0 | 1 | 1 | 2 | 4 | N | HEICO and TransDigm |
| 64 | Aviation STC modifications (r2_certify 1b) | IN | 0 | 0 | 1 | 2 | 3 | N | $20-100M+ per program |
| 65 | Orphan type-certificate acquisition (r2_certify 1c) | IN | 1 | 0 | 1 | 2 | 4 | **Y** | $10M-1B lumps. TCDS joined to the registry is a lookup |
| 66 | Nuclear and utility obsolescence parts (r2_certify 3) | IN | 0 | 0 | 0 | 1 | 1 | N | Curtiss-Wright |
| 67 | Rail, shipping class, medical repair, wind and fab spares (r2_certify 4-8) | IN | 0 | 0 | 0 | 1 | 1 | N | Non-exclusive, commoditised, or with no public data |
| **Materials and waste** |||||||||||
| 68 | **Hazardous-waste reclaimer that reads e-Manifest, TRI and the Biennial Report** (lane_materials C1) | SEC (materials; IN if framed as robotic reclamation) | 2 | 2 | 1 | 2 | 7 | N | $1-3B (Veolia paid $3.0B for Clean Earth). About half the revenue is tipping fees |
| 69 | Stranded cleantech plants bought out of bankruptcy and repurposed (lane_materials C2) | IN | 1 | 1 | 2 | 1 | 5 | **Y** (auction) | Lyten bought the Northvolt estate. Needs a product and a team |
| 70 | Second plant for chemicals made at only a few sites (lane_materials C4) | SEC | 0 | 1 | 1 | 1 | 3 | N | $50-500M per chemical. Government awards go to incumbents |
| 71 | Coal ash harvesting (lane_materials C5) | SEC | 0 | 1 | 1 | 2 | 4 | Y | Eco Material. Close to prospecting |
| 72 | Valuable waste streams held by consolidators: EAF dust, red mud, Ga/Ge, PGM catalysts, slag, sodium sulfate (lane_materials kill list) | SEC | 0 | 0 | 1 | 2 | 3 | Y | Befesa, Metallium, Johnson Matthey |
| 73 | PFAS destruction (lane_materials) | SEC | 0 | 0 | 0 | 1 | 1 | N | A services market |
| 74 | University or federal patents and expired patents (lane_materials, lane_wild) | IN | 1 | 1 | 0 | 1 | 3 | N | Tiny, or nothing left to own |
| **Land, water, ecology and the built world** |||||||||||
| 75 | **Brownfield closure arbitrage**: buy stigma-discounted sites, predict cost and time to closure from state case files (lane_land 2) | SEC (IN when aimed at powered industrial and data-centre sites) | 2 | 2 | 2 | 2 | 8 | **Y** | $1-3B deployed at real-estate returns. 5-20x per site where it can be powered and rezoned for data centres or factories |
| 76 | Western water rights repriced by satellite HCU (lane_wild C, lane_claims C4, lane_earth 2, lane_land 3) | SEC | 2 | 1 | 2 | 1 | 6 | **Y** | $1-3B. Vidler sold for $291M. Anti-speculation law and water-court changes gate the exit |
| 77 | Mitigation and conservation banks (lane_earth 1, lane_land 1, redteam_banks) | SEC | 1 | 1 | 1 | 2 | 5 | N | $1-3B and shrinking under WOTUS |
| 78 | Grey-belt and by-right land promotion (lane_built C3, lane_land 5) | SEC | 1 | 1 | 2 | 2 | 6 | Y (option, not claim) | Big uplift, but Gladman, Catesby and LandTech hold the field |
| 79 | Northeast landfill airspace and rail transfer (lane_built C4) | SEC | 0 | 1 | 1 | 2 | 4 | **Y** | WM, Republic, Casella |
| 80 | Rail and linear corridors for HVDC and fibre (lane_wild D, lane_land 4) | IN | 0 | 1 | 1 | 1 | 3 | Y | Brandt reversion. Railroads hold active corridors |
| 81 | Climate-forecast fishing quota (lane_earth 3) | SEC | 1 | 1 | 1 | 1 | 4 | **Y** | $0.3-1B. Ownership caps apply |
| 82 | Genebank trait mining (lane_earth 4) | SEC | 0 | 1 | 1 | 1 | 3 | N | No exclusivity on the input |
| 83 | Aquaculture licences (lane_earth) | SEC | 0 | 0 | 1 | 2 | 3 | Y (auction) | Mowi and Cermaq bid it up |
| 84 | Farmland, timber, climate land, solar land options, kelp, carbon developers, UK BNG, microbes (lane_earth, lane_land) | SEC | 0 | 0 | 1 | 2 | 3 | Y | Funds price it, or crowded |
| 85 | England unregistered land and ransom strips (r2_claims) | SEC | 1 | 1 | 2 | 1 | 5 | N | Niche. Ransom-strip specialists |
| 86 | Licence, permit and concession rights: towers, billboards, liquor, cannabis, taxis, pharmacies, broadcast, slots, poles, NEVI, CON, LIHTC, casinos, CCN, aggregates (lane_built kill list) | SEC | 0 | 0 | 1 | 1 | 2 | Y (mostly) | Small, or held |
| 87 | Upzoning bets, tax liens, heirs' property, akiya, title arbitrage, government land, conservation easements (lane_land) | SEC | 0 | 0 | 1 | 1 | 2 | Y | Bid away, or toxic |
| **Drugs and biology (all secondary)** |||||||||||
| 88 | CRL rescue: buy fixable rejected NDAs (lane_bio 1, redteam_drugs) | SEC | 1 | 1 | 2 | 2 | 6 | N | $3-10B in theory. In practice a handful of CMC-only abandoned CRLs a year. Publication was paused in April 2026 |
| 89 | Approved abroad, never in the US, licensed in (lane_wild A, lane_bio 2; proof 2) | SEC | 1 | 0 | 2 | 2 | 5 | Y (licence) | About 7 a year. IQVIA lists them |
| 90 | Tropical and rare-paediatric PRV harvesting (lane_wild B, lane_bio 3, r2_pharma 6c) | SEC | 1 | 0 | 1 | 2 | 4 | N | 5-15 molecules |
| 91 | First NDA for a marketed-unapproved drug (r2_pharma 1, r2_claims) | SEC | 1 | 0 | 2 | 2 | 5 | N | The NDC field is a lookup. The pool is depleted |
| 92 | Orphan first approval on an old off-patent drug (r2_pharma 6d, r2_claims) | SEC | 1 | 1 | 2 | 1 | 5 | N | Firdapse-style pricing backlash |
| 93 | Veterinary field-of-use licences (lane_bio 4) | SEC | 1 | 1 | 1 | 2 | 5 | N | $100-500M a year per asset at best |
| 94 | Responder-subgroup rescue from Vivli data (lane_bio 5) | SEC | 0 | 2 | 1 | 1 | 4 | N | The DUA hands sponsors the option on what you find |
| 95 | Other pharma and agchem first-filer regimes: thyroid race, 505(b)(2) 3-year, PUMA, QIDP, De Novo, FIFRA, REACH, BPR, CGT, PIV, OTC, Novel Food, NMN, tobacco, biosimilars (r2_pharma, r2_claims) | SEC | 0 | 0 | 1 | 1 | 2 | N | Labelled target lists. Farmed |
| 96 | Bio kill list: generic resurrection, metagenome antibiotics, genetic targets, natural products, FAERS, herbicides, China in-licensing (lane_bio) | SEC | 0 | 1 | 1 | 1 | 3 | N | Biossil, Formation, big pharma |
| **Legal, financial and IP claims (all secondary)** |||||||||||
| 97 | Copyright termination recapture (lane_claims C3) | SEC | 0 | 1 | 2 | 1 | 4 | N | No lock-up is allowed before the effective date |
| 98 | Art "sleepers" (lane_wild E) | SEC | 1 | 1 | 2 | 1 | 5 | N | $0.5-1B a year turnover. Attributions get contested |
| 99 | Duty refund claims (lane_claims C5) | SEC | 0 | 0 | 1 | 1 | 2 | N | Funds pay 50-90 cents |
| 100 | Claims trading, class actions, unclaimed property, MLC, carbon credits, domains and trademarks, lapsed patents, zombie biotech IP, shipwrecks, brand revival (lane_claims, lane_wild) | SEC | 0 | 0 | 1 | 1 | 2 | Y (some) | Priced, small or hostile |
| 101 | Paper IP regimes: Chinese utility models, design patents, trademark first-to-file, PVR, bona vacantia, catch history, Nepal and Philippines survey contracts, Chile water (r2_claims) | SEC | 0 | 0 | 1 | 1 | 2 | N | Options that are worthless until built, or out on ethics |

Rows 52, 67, 72, 84, 86, 87, 95, 96, 100 and 101 group ideas the source files themselves killed in
one line. With them expanded, the table covers about 95 distinct candidate companies, plus the
round 2 regime catalogue.

## 2. What the rescoring shows

- **Removing "first-come" lifts a different set of ideas.** The ideas that now score highest are
  ones where the seller is structurally blind: a generator paying to landfill metal-bearing sludge,
  a stigma-discounted contaminated site, an estate that does not know it holds a product line or an
  IPv4 block, a small owner pricing a solar plant on trailing output. Rounds 1-3 scored these
  4-5, because the asset had to be bought or the owner ran the sale.
- **Strict P2 still kills most of the old leaders.** Queue attrition (backtest), foreign-approved
  drugs (joins plus IQVIA), unapproved-drug NDAs (an NDC field), ITU priority (a structured
  database), orphan type certificates (TCDS joined to the registry), retiring-plant rights
  (EIA-860) and decommissioning trusts (a spreadsheet) all get P2 = 0. Only five ideas get P2 = 2:
  brownfield closure prediction, waste-stream composition inference, solar and wind loss
  decomposition, pending-patent claim mapping and Vivli responder subgroups. No spectrum, nuclear or
  drug idea does.
- **Lineage drops from pick to mid-table (5/8).** It is still in Dhruv's sectors, but it fails
  strict P2: once section 8 links FPDS records to prior SBIR awards, matching lineages becomes a
  join. It also fails P4: a contracting officer can decline Phase III (G2 Ops).

## 3. Ideas killed mainly because the right had to be bought, had an owner, or was sold by tender

| Idea (row) | Original killer | Revives under the corrected test? |
|---|---|---|
| Brownfield closure arbitrage (75) | Not claimable; "underwriting edge only" | **Yes, strongly.** Buying is now the point, and stigma pricing is exactly a price set by sellers and rival buyers who cannot see closure cost. Crowding check (searches 1 and 8): data-centre-on-brownfield is a 2026 law-firm theme (Bracewell, BCLP), and Liora ($5.1M) sells AI remediation as a service. I found no ML-underwritten principal buyer |
| Orphaned OT/ICS product lines (58) | Won by M&A and capital, not by claiming first | **Yes.** It is in a security sector, and the seller is often an estate or a small vendor. Search 3 found only strategic one-offs (Mitsubishi-Iconics, GE), not a roll-up of orphaned lines |
| Dormant IPv4 blocks (60) | Owner and successor have to sign | **Revives on the test, dies on the ceiling** ($0.6-1.8B and falling; Hilco is already hunting) |
| Underperforming solar and wind (18) | Negotiated M&A, with the edge visible in the data room | **Partly.** P2 is a real 2 at fleet scale, but search 2 and 5 show O&M executives and aggregators (CleanCapital, listed solar funds) already seek underperformers. The edge is sourcing off-market sellers, not diligence |
| Stranded never-fired turbines (11) | Physical object, owner known, OEM tracks the serial | **Partly, as a trading window only.** Sellers mark to scarcity (Hallador paid $760/kW), and valuation is a lookup once a unit is found |
| Western water rights (76) | Bought, not claimed; funds present | **Partly.** Buying is fine, but P4 is gated by water courts and anti-speculation law, and OpenET hands the ET layer to everyone |
| Rochester-model EOL chip lines (39) | Negotiated with the OEM | **Partly.** It scores 6, but Rochester has licences from 70+ OEMs, so mispricing is visible to the dominant buyer |
| Bankruptcy cleantech plants (69) | Auction; ML not decisive | **No.** Buying is fine, but the repurposing judgement is engineering, not ML, and it needs an operating team |
| Robotic landfill mining (26) | The owner (county) runs procurement | **No.** Only the landfill owner captures reclaimed airspace, and there are no labels to train on |
| Telco copper (27) | Tender (BT to EMR) | **No.** The tender is fine, but the profit pool is under $1B |
| Subsea cable (28) | The consortium owns it | **No.** Small; OEC and Mertech |
| Retiring-plant CIRs (3) | The owner holds them | **No.** P2 = 0 (EIA-860 is structured), and owners now know the value |
| Retired-plant part-out (16), idle transformers (12), PJM units (13) | Owners and dealers | **No.** P2 = 0, already priced |
| Nuclear site banking (20), dormant COLs (22), cancelled components (23), DOE land (24) | Owned; NRC transfer; RFP | **No.** Sellers read the same docket. The NRC and state PUC are the channel |
| Orphan type certificates (65) | M&A, not ML | **No.** P2 = 0 |
| Dormant ITU priority (49), D2D aggregation (48), FCC auctions (53) | Bought shells; monopsony; auctions | **No.** P2 = 0, and P4 depends on about six strategic buyers |
| Northeast landfill airspace (79) | Majors know every site | **No** |
| Fishing quota (81), aquaculture (83) | Bought, or auctioned | **No.** Ceiling and ownership caps |
| Foreign-approved drugs (89) | Licence needed | **No.** The real killer was P2 (lookup), not the licence |
| Lineage (36, 37) | (Partly) priced by primes and roll-ups | Unchanged at 5. Buying was always allowed for it |

## 4. Top-6 shortlist

The ranking weighs the total, sector fit and the ceiling. IPv4 (7/8) is left out because its
ceiling fails. CRL rescue (6/8) is left out because it is off-sector and its pool is a handful a
year.

### 1. Brownfield closure arbitrage, aimed at powered industrial and data-centre sites (8/8; secondary, IN when sited on power)
- **The play.** Buy contaminated parcels at a stigma discount. ML trained on decades of closed state
  case files predicts cost and time to regulatory closure. Remediate, get the no-further-action
  letter, then sell or develop, prioritising sites with industrial power service, rail and
  suitable zoning.
- **Data.** California GeoTracker and EnviroStor (full document histories and lab results), EPA
  ACRES, NJDEP, TCEQ and Michigan Part 201 files. All are public under right-to-know and CERCLA/RCRA
  rules, and they are scanned, multi-modal and unlabelled.
- **Strongest reason for.** The seller's price is set by lenders who refuse to lend and buyers who
  cannot model closure. No lookup gives cost-to-closure, so the model is the valuation (P2 = 2). The
  data-centre land rush (powered land at $0.3-1.5M/MW) puts a large step-up on the subset of sites
  that have power.
- **Strongest reason against.** Returns look like real estate unless sites are powered. The edge is
  underwriting, which brownfield funds (Cherokee's successors, Greenfield, Hilco Redevelopment)
  can copy once wins become visible, and environmental insurers already price some of this risk.
- **Proof that would settle it.** Train a cost and time-to-closure model on GeoTracker UST/SLIC
  cases using only documents dated before the first Phase II. Test it on later-closed cases, then
  join the predictions to recorded sale prices of contaminated parcels. **Kill** if discount minus
  predicted cost is not systematically positive in some segment, or if the model's error is no
  better than a contaminant x media x state lookup.

### 2. Hazardous-waste reclaimer sourcing feedstock from the manifest record (7/8; secondary, IN if framed as robotic reclamation)
- **Strongest reason for.** No public source gives waste-stream composition. Inferring metal content
  from e-Manifest, TRI transfers and Biennial Report free text is a true inference problem (P2 = 2).
  The generator pays to landfill something worth money (P1 = 2), and the company keeps the metal.
- **Strongest reason against.** About half the revenue is tipping fees. Once streams start being
  won, Clean Harbors and Veolia/Clean Earth can copy the targeting. The ceiling is $1-3B unless the
  company grows into permitted treatment capacity.
- **Proof that would settle it.** Hide 20% of TRI plant-to-facility metal masses and predict them
  within ±30% for at least 60% of pairs. Assay 5 top-ranked streams, and get 2 exclusive offtake
  LOIs. Search 7 found no ML manifest sourcer.

### 3. Roll-up of orphaned OT/ICS software and firmware product lines (7/8; IN, security)
- **Strongest reason for.** The sellers are estates, carve-outs and small vendors who cannot see
  the size of the captive installed base. The company owns the IP and earns from patches, support
  and successor hardware. The Constellation and Rochester precedents show such roll-ups compound
  to billions.
- **Strongest reason against.** P2 is only a 1: vendors know their own support customers, so ML
  mainly finds targets from CISA "EOL, no fix" advisories and Shodan exposure. Most of the value is
  M&A execution, and part of the revenue looks like a service.
- **Proof that would settle it.** Take the 2020-26 CISA advisories that say "EOL, no fix" or
  "discontinued", join them to exposure counts and refurb-part prices, and estimate the installed
  base. **Pass** if at least 10 lines have an owner who could sell, an installed base above $5M a
  year of support value, and an asking price under 2x that.

### 4. Underperforming solar and wind plants bought on a public-data screen and fixed with robotic O&M (6/8; IN, energy and robotics)
- **Strongest reason for.** Splitting each plant's gap into fixable and structural loss from
  EIA-923, NSRDB and imagery, with curtailment unreported, is a fleet-scale inference that only ML
  can do (P2 = 2). It finds off-market sellers before a data room exists. Robotic O&M is where the
  uplift gets captured.
- **Strongest reason against.** Any bidder sees SCADA data in diligence, so the mispricing closes at
  signing. Raycatch's average recoverable loss is only about 5%, and O&M executives and aggregators
  already seek underperformers (search 2).
- **Proof that would settle it.** Rank US 5-100 MW plants by actual versus expected generation, and
  check imagery for fixable causes. Then test whether the plants that traded in 2023-25 sold at a
  discount the model predicted. **Kill** if the model's fixable-loss estimate does not beat a
  "trailing capacity factor versus regional median" lookup at predicting post-sale uplift.

### 5. Pending patent families with early priority, mapped onto shipping energy and robotics products (6/8; IN, deeptech)
- **Strongest reason for.** Small entities let families lapse without knowing that their written
  description supports claims on products now shipping (P1 = 2). Reading spec-to-product support is
  hard inference (P2 = 2). The priority date cannot be copied.
- **Strongest reason against.** The value is realised through licensing or litigation, which is an
  NPE business carrying PTAB, §101 and reputational risk (P4 = 1). Patlytics and XLSCOUT already sell
  the continuation-mapping tools.
- **Proof that would settle it.** Take families abandoned in 2018-21 and have the model flag
  specifications that could have supported claims on later products. **Pass** if patent attorneys
  confirm at least 30% of the top 50, against under 5% for a CPC-class baseline.

### 6. Lineage, the SBIR Phase III wrapper (5/8; IN, security and deeptech), kept as the previous pick for comparison
- **Strongest reason for.** It is the only idea with a legal sole-source vehicle (Clear Align, Bode)
  and a $4.1B precedent exit in BlueHalo.
- **Strongest reason against.** A contracting officer can decline Phase III (G2 Ops), and section 8
  FPDS linkage turns the data step into a join.
- **Proof that would settle it.** The PICK8 test is unchanged. Using the hollomancer census, the
  model must add at least 0.05 AUC over an agency x topic lookup, and at least about 20 post-2019
  lineages must sit in inactive firms that match a live programme.
- **Why the alternatives were not chosen.** ERCs (6/8) took a hit from the Texas minor-permit route
  (search 6). Stranded turbines (6/8) are valued by a lookup. Rochester-model chips (6/8) have a
  dominant incumbent.

## Searches used (8)

1. AI brownfield acquisition and underwriting: Liora $5.1M AI remediation is a service; SRNL is
   government work. https://boereport.com/2025/08/06/liora-raises-5-1-million-to-accelerate-ai-driven-site-remediation/
2. Buyers of underperforming solar plants: https://pv-magazine-usa.com/2024/08/08/om-executives-seeking-underperforming-solar-assets ;
   https://www.solarpowerworldonline.com/2026/06/the-hidden-performance-gap-costing-solar-asset-owners-millions/
3. EOL ICS software acquisitions: only strategic one-offs found. https://www.esmagazine.com/articles/99523-mitsubishi-electric-corp-to-acquire-iconics
4. ERC scarcity in Texas: https://www.aiche.org/conferences/videos/conference-presentations/scarcity-emission-reduction-credits-ercs-and-potential-effects-on-expansions-petrochemical-and
5. Solar portfolio aggregators: https://solarbuildermag.com/news/cleancapital-with-yet-another-10-mw-solar-portfolio-acquisition/
6. Texas data-centre minor permits avoid offsets: https://www.latitudemedia.com/news/ai-data-centers-are-getting-built-thanks-to-a-permit-common-for-dry-cleaners/ ;
   https://aiweekly.co/alerts/texas-ai-data-centers-bypass-pollution-review-via-minor-permits
7. ML manifest sourcing for hazardous waste: none found (only Metallium and Sortera in adjacent recycling).
8. Brownfields for data centres: https://www.bracewell.com/resources/bringing-data-centers-to-brownfields/ ;
   https://www.iamagazine.com/2026/02/02/are-brownfield-sites-set-to-drive-a-building-boom-in-2026/
