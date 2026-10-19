# v4 slice E: sweeps L1-L6 re-scored on ML plausibility (19 Oct 2026)

Scope: every idea in `sweep_L1.md` to `sweep_L6.md`, old ideas that were re-scored and new ones, deduped into 146 rows.
Rubric (`V4_PLAUSIBLE.md` on `V3_SHAPE.md`), each leg out of 5:
- **S1:** buy before it's known.
- **S2:** step-up of 3x or more.
- **S3:** ML plausibility.
- **S4:** discovery-heavy frame.
- **S5:** compounding edge.

A pass is 17+/25 with no leg at 0-1.
Gates: no prospecting or drilling, not Terranox, own the asset (not a service), and a path to a large company. **x** means a gate fails.

## Verdict

**Nothing passes after the checks.**
- Before the checks, one idea reaches 17: EV-pack second-life grading.
- After the web checks it drops to 16. New storage packs fell to $70/kWh, which caps the certified-module price, so S2 is 2.
- Easing the ML rule lifts S3 by 1-2 points on about 40 ideas. The biggest gainers are:
  - planning and entitlement outcomes, which resemble prospectivity (many weak signals, many past decisions);
  - battery state-of-health from short tests;
  - claim-to-product matching for patents;
  - record reconstruction;
  - molecular property prediction.
- What still binds:
  - **S1:** the seller prices in the hope (land, interconnection, closed plants).
  - **S2:** the step-up is under 3x (LOMA, GPU lots, solar rescue, second life).
  - **S4:** the proof is a plant, a trial or a qualification (materials, drugs, hydro).
- Only **two** ideas have a real negative ML test:
  - powered land and queue attrition (AUC 0.721 against 0.727 for a lookup table);
  - signals priced off a legible lookup (MHz-pop, comps, nameplate MW).

  Both keep S3 at 1-2.

## Top 10 (gates pass; score before the check, then after it where checked)

| # | Idea (source) | S1-S2-S3-S4-S5 | /25 | Why it ranks / what holds it back |
|---|---|---|---|---|
| 1 | **EV-pack second-life grading:** buy salvage packs, ML reads SoH and remaining life from a short pulse or impedance test, sell certified modules or BESS (L6 N2) | 4-3-4-3-3 | **17 -> 16** | S3: battery-life prediction from early or short data is the closest analogue to prospectivity in this slice. S5: your own field returns compound. S2 falls to 2 after the check |
| 2 | **UK small-site plot engine:** option garden or backland plots, win consent, sell to SMEs (L1 N1) | 3-3-4-3-3 | **16 -> 15** | S3: millions of past decisions plus officer reports, appeal history and local-plan context, which is prospectivity-like. S1: the homeowner holds the hope. The pool is shrinking |
| 3 | **Back-to-birth trace recovery:** buy LLPs and engines with broken trace, rebuild the records (L1#19, L6#6) | 3-3-4-3-3 | **16 -> 15** | S3: OCR plus entity linking across messy multi-operator records. After the check S2 is 2, because the documentation discount is only 20-50% |
| 4 | UK land promotion / grey belt (L1#1, N4; L2#5; L3 r6, N9) | 2-3-4-3-3 | 15 | S3 rises: the "1.3x lift" was arithmetic, not a test. The promoter keeps 10-25%, and landowners ask for hope value |
| 5 | Hidden lots: antiquated-subdivision legal-lot recovery (L1#13) | 4-3-3-2-3 | 15 | Cheap heir and tax-sale lots. Entitlement and the horizontal build are heavy (S4) |
| 6 | Lineage: dormant SBIR firms' Phase III rights (L6#7) | 4-3-3-3-2 | 15 | Predicting programme-office pull from budget documents and SAM is plausible. The proof usually fails |
| 7 | DropIn: Li-ion electrolyte additives, first-filed and toll-made (L5#7) | 3-3-4-2-3 | 15 | Molecular property ML is well founded. Cell-maker qualification takes 2-3 years (S4) |
| 8 | Shelved-drug NewCo: licensor keeps equity (L3 N2, N11) | 3-5-3-2-2 | 15 | Telavant-scale step-up. BenevolentAI is a weak negative. The trial is the bulk of the work. Outside Dhruv's field |
| 9 | Discontinued ANDA x shortage relaunch (L2 N3, L3 N18) | 4-4-3-2-2 | 15 | About $150k per right against marketed ANDAs worth tens of millions. Manufacturing is the proof |
| 10 | Metagenome enzyme claims (L5#3) | 3-3-4-2-2 | 14 | Protein ML is a strong analogue. Basecamp's data moat caps S5 |

**Gated out despite high scores:**
- Orphan patents with evidence of use: 4-3-4-3-2 = 16. Fails the path gate: the market is $158M/yr.
- Government-surplus mislisted lots: 3-3-4-4-2 = 16. Fails the path gate: a resale shop with no ladder.
- Dropped domains: 2-3-4-4-2 = 15. Fails the path gate.
- FEMA LOMA land bank: 15, but S2 = 1.

## Full table (deduped; one line each)

Format: S1-S2-S3-S4-S5 = total. Source tags: L1#n means old idea n in that sweep, and Nn means new idea n.

**Land and entitlement**
| # | Idea (sources) | Legs | /25 | Note |
|---|---|---|---|---|
| 1 | Small-site plot engine UK (L1 N1) | 3-3-4-3-3 | 16 | Top 3, checked |
| 2 | UK promotion / grey belt (L1#1, N4; L2#5; L3; L3 N9) | 2-3-4-3-3 | 15 | Hope value with the owner |
| 3 | US middle-housing lots, SB 9 etc. (L1 N2) | 2-3-3-3-3 | 14 | Owner-occupancy affidavit; LA 0/28 |
| 4 | Class Q / MA prior-approval factory (L1 N3) | 2-3-3-3-2 | 13 | Farmers already file |
| 5 | Exurban entitlement arbitrage (L1#4; L3; L6#4) | 2-3-3-2-3 | 13 | Multi-year campaigns |
| 6 | Entitled Acre, DC rezoning (L1#3; L3; L6#3) | 2-2-3-3-2 | 12 | Power, not zoning, sets value |
| 7 | Powered-land options / JV (L1#2; L2#2; L3, N3; L6#2) | 2-4-2-2-2 | 12 | Real negative: AUC 0.721 vs 0.727 |
| 8 | Thin-auction powered / trust land (L4#1, N1; L3 r5) | 2-2-2-3-2 | 11 | Sole bidder pays the appraisal |
| 9 | Tax-delinquent x headroom (L2 N4) | 3-2-2-3-2 | 12 | Grid signal shares the AUC result |
| 10 | Australian rural-to-urban rezoning (L1#5; L3) | 2-2-3-2-2 | 11 | Growth maps public |
| 11 | German Bauerwartungsland (L3) | 2-2-3-2-2 | 11 | Municipalities buy first |
| 12 | Poland plan-ogolny rezoning (L3) | 2-2-3-2-2 | 11 | GML published |
| 13 | Texas ETJ release plus MUD (L3) | 2-2-2-2-2 | 10 | Execution |
| 14 | Haryana/Maharashtra CLU (L3) | 2-2-3-2-2 | 11 | 2-5x net |
| 15 | BC ALR exclusion swaps (L3) | 2-2-2-2-2 | 10 | Political |
| 16 | German wind-zone optioning (L3) | 2-2-3-2-2 | 11 | Public race |
| 17 | UK Gate-2 land (L3; L2 N15) | 2-2-2-2-2 | 10 | NESO rations capacity |
| 18 | Hidden lots, antiquated subdivisions (L1#13) | 4-3-3-2-3 | 15 | Top 10 |
| 19 | Zombie subdivisions (L1#14; L3) | 3-1-3-2-2 | 11 | Millrose cost-plus; S2 = 1 |
| 20 | Florida CCCL lots (L1#12) | 2-2-3-3-2 | 12 | Erosion line public |
| 21 | FEMA LOMA land bank / flood-lot flipper (L1#16, N5) | 3-1-4-4-3 | 15 | S2 = 1 (5-15%) |
| 22 | By-right commercial-to-residential (L1#15) | 1-2-2-3-2 | 10 | GIS-legible |
| 23 | Prior-converted wetland proof (L1#17) | 2-2-3-3-2 | 12 | No wetland discount |
| 24 | Institutional land JV, SB 4 (L3 N13) | 2-3-2-3-2 | 12 | Small |
| 25 | Japan akiya at volume (L1 N20) | 4-2-3-2-2 | 13 | Renovation is the step |
| 26 | Transit air rights (L3 N20) | 1-2-1-1-1 | 6 | Political |
| 27 | GSA ex-military bases with substations (L4 N13) | 2-2-2-3-2 | 11 | Hyperscalers bid |
| 28 | Billboard permit sites (L1#11; L2#15) | 2-2-2-3-1 | 10 | Discontinuance rules |
| 29 | STR permits in capped cities (L1 N19) | 1-2-2-2-1 | 8 | Lotteried |
| 30 | Pre-approved ADU plan sets (L1 N22) | 1-1-1-2-1 | 6 | x service |
| 31 | LL97 fine-exposed buildings (L2 N20) | 1-1-2-2-2 | 8 | Owners know |
| 32 | Commercial tax over-assessment (L1 N21) | 2-1-3-3-2 | 11 | 5-15% step |
| 33 | Foreclosure surplus (L2#18) | 2-1-2-3-1 | 9 | Fee caps |

**Power, grid and energy sites**
| # | Idea (sources) | Legs | /25 | Note |
|---|---|---|---|---|
| 34 | Surplus / latent interconnection, all variants (L1#18, N8; L2#1, N6; L3 N1, N5, r4; L4#12; L6 N4) | 1-3-3-2-2 | 11 | Plant owner holds the POI |
| 35 | CIR clock arbitrage, PJM (L2 N2) | 1-3-2-3-2 | 11 | Same-site rule; IPP sellers |
| 36 | Closed-plant / idle large-load capture (L2#3, N1; L3 N4) | 1-3-3-3-2 | 12 | Hawesville: the owner kept it |
| 37 | Powered brownfields (L3) | 2-1-2-2-2 | 9 | Remediation |
| 38 | Queue-position buyer / Ch.11 pipelines / attrition options (L3 N6, N7; L6#5, N1) | 2-3-2-3-2 | 12 | Real negative AUC test |
| 39 | Air-permitted BTM power pad (L3) | 2-3-2-2-2 | 11 | Turbines scarce |
| 40 | Distribution BESS RTB factory (L1 N7) | 2-3-3-3-2 | 13 | Hosting maps public |
| 41 | Congestion-node batteries (L2 N7) | 2-2-3-2-3 | 12 | A build |
| 42 | BESS site royalties (L3 N15) | 2-2-2-2-2 | 10 | Crowded |
| 43 | Gas-tap sites (L2#16) | 2-2-2-2-2 | 10 | Firm transport held |
| 44 | Bitcoin-miner to AI conversion (L2 N8) | 1-3-2-2-1 | 9 | Seen in 2024 |
| 45 | NRC-terminated switchyards (L2 N10) | 1-3-1-2-1 | 8 | About 10 sites |
| 46 | Restart Option Co (L2#11) | 1-4-1-1-1 | 8 | 3-5 plants |
| 47 | Retired-iron transformers (L2#17) | 3-2-2-2-2 | 11 | Haul plus refurb |
| 48 | Wind repower options (L3 N8) | 1-2-3-2-2 | 10 | Owner reads SCADA |
| 49 | Solar repower finder, EIA-923 (L6 N3) | 2-2-3-3-2 | 12 | 1.5-2x |
| 50 | Wind life extension (L6 N9) | 2-1-3-2-2 | 10 | Merchant price below opex |
| 51 | Small IPP PPA roll-off (L2 N18) | 2-2-2-2-2 | 10 | PE screens |
| 52 | Hospital central-plant BTM (L3 N14) | 1-2-1-1-2 | 7 | Build |
| 53 | Seized crypto-mining sites (L4 N10) | 2-3-1-2-1 | 9 | Handful |
| 54 | Spain/Portugal just-transition nodes (L4 N8) | 1-2-1-1-1 | 6 | Jobs-scored |
| 55 | Pumped hydro: FERC closed-loop, NSW dams, public tenders (L4#2, #3, N3) | 2-2-3-2-2 | 11 | $1-3B build |
| 56 | Non-powered dam hydro / FERC surrenders (L1#8; L4#8; L2 N13) | 2-1-2-1-1 | 7 | $5-12k/kW |
| 57 | Emerging-market hydro concessions (L4 N4) | 3-2-3-1-2 | 11 | Build |
| 58 | Wind/solar public tenders: PH GEA, NL/BC Crown, BLM, NM trust, India, JP/KR/TW offshore (L4#4-7, N11, N20) | 2-2-2-1-2 | 9 | IPP rounds |
| 59 | Chilean maritime concessions (L4#9) | 2-2-2-2-1 | 9 | Use-it-or-lose-it |
| 60 | DOT corridors for HVDC/fibre (L4 N7) | 2-3-1-1-2 | 9 | No discovery |
| 61 | Landfill-gas tenders (L4 N6) | 2-2-2-2-2 | 10 | GHGRP legible |
| 62 | Minigrid concessions (L4 N14) | 2-1-3-2-2 | 10 | S2 = 1 |
| 63 | Abandoned pipelines for CO2/H2/fibre (L2#7) | 3-2-2-1-1 | 9 | Requalification |
| 64 | Ghost Offsets, ERCs (L2#13) | 3-2-2-3-1 | 11 | Small |
| 65 | Ghost SRECs (L2#20) | 2-1-1-3-1 | 8 | Owner self-registers |
| 66 | Expiring CRP near transmission (L2 N12) | 2-2-2-2-2 | 10 | Developers canvass |
| 67 | German MaStR idle BESS approvals (L2 N16) | 2-2-2-2-1 | 9 | Tied to the SPV |
| 68 | Mitigation / BNG habitat banks (L2#10; L3; L1 N18) | 2-2-3-2-2 | 11 | Stewardship |
| 69 | Water rights: CU Prove, lease-fallow JV (L1#7; L3 N12) | 2-2-3-2-2 | 11 | Water court |
| 70 | Alberta end-of-life liability underwriter (L2#6) | 2-2-4-3-3 | 14 | Capped and service-shaped (PICK8) |
| 71 | Distressed C&I / community solar; resi books (L6#8, N7) | 3-2-3-2-2 | 12 | Credit bids |
| 72 | Community-solar subscriber books (L6 N20) | 2-1-3-1-2 | 9 | No step-up |
| 73 | Nodal, Texas batteries (L6#18) | 1-1-3-1-2 | 8 | $29/kW-yr |
| 74 | Bridge-power gas fleets; Quiet Fleet (L6 N15, #17) | 1-1-1-1-2 | 6 | Capex |

**Spectrum, orbital and licences**
| # | Idea | Legs | /25 | Note |
|---|---|---|---|---|
| 75 | Spectrum: zombie, thin FCC auctions, CBRS, rural JV (L2#14; L4#11, N2, N12; L3 N16) | 2-2-1-2-1 | 8 | MHz-pop lookup |
| 76 | ITU filings (L2 N9; L3 N17; L4 N9) | 1-3-1-2-1 | 8 | Sovereign |
| 77 | Slot futures (L2#12) | 1-3-1-1-1 | 7 | Carriers only |
| 78 | Dark TV licences (L2#19) | 2-1-1-2-1 | 7 | Capex |
| 79 | Tower entitlements / comm sites (L1#6; L4#10) | 2-2-2-2-2 | 10 | Carrier RF private |

**IP and rights**
| # | Idea | Legs | /25 | Note |
|---|---|---|---|---|
| 80 | Orphan patents with evidence of use (L1#9, chk2; L3; L6#1) | 4-3-4-3-2 | 16 | x path: $158M/yr |
| 81 | Continuation Forge (L1#10; L2#4) | 3-2-4-3-2 | 14 | Late surcharge; Patlytics |
| 82 | Lapsed-patent revival (L2 N5) | 4-2-3-3-2 | 14 | Litigation value |
| 83 | University/DOE licences with ML triage (L4#13, N16; L3 N10) | 3-2-3-2-2 | 12 | Prototype is the proof |
| 84 | Method-of-use repurposing patents (L1 N16) | 3-1-3-3-2 | 12 | No buyer at proof |
| 85 | Generative-materials provisionals (L1 N17) | 3-1-2-3-1 | 10 | Opinion |
| 86 | Dormant / expired trademarks (L1 N9; L2 N11) | 3-2-3-3-2 | 13 | Small royalties |
| 87 | Lineage, SBIR Phase III (L6#7) | 4-3-3-3-2 | 15 | Top 10 |
| 88 | Black Box / defunct-label masters (L2#8, #9) | 3-1-3-3-2 | 12 | Royalties tiny |
| 89 | Dropped-domain catcher (L1 N10) | 2-3-4-4-2 | 15 | x path |
| 90 | Settlement / securities claims buyer (L1 N6; L2 N14) | 3-2-3-3-2 | 13 | Capped by face value |

**Pharma and bio**
| # | Idea | Legs | /25 | Note |
|---|---|---|---|---|
| 91 | Shelved-drug NewCo (L3 N2, N11) | 3-5-3-2-2 | 15 | Trial dominates |
| 92 | Discontinued ANDA x shortage (L2 N3; L3 N18) | 4-4-3-2-2 | 15 | Manufacturing is the proof |
| 93 | 510(k) re-clearance factory (L1 N14) | 2-1-2-2-1 | 8 | Non-exclusive |
| 94 | Orphan-drug designation factory (L1 N15) | 3-1-3-3-1 | 11 | Designation sells for little |
| 95 | Captive Scent, plus non-natural analogues (L5#1, N20) | 3-2-4-2-2 | 13 | Osmo POM plausible; 7-10 yr; monopsony |
| 96 | Cryptic Clusters (L5#2) | 3-3-4-1-2 | 13 | Clinic |
| 97 | Metagenome enzyme claims (L5#3) | 3-3-4-2-2 | 14 | Basecamp |
| 98 | Nagoya enzymes (L5#4) | 2-2-3-2-1 | 10 | Non-exclusive |
| 99 | Freezer Estate strain banks (L5#5) | 4-2-3-2-2 | 13 | Scale-up |
| 100 | Suppressa microbiomes (L5#9) | 2-2-3-2-2 | 11 | Re-isolable |
| 101 | Survivor Budwood (L5#10) | 3-3-2-2-2 | 12 | Base rate about 0 |
| 102 | SweetSource proteins (L5#11) | 2-2-3-2-2 | 11 | GRAS and titre |
| 103 | Polymorph Keys (L5#12) | 2-2-3-3-1 | 11 | In-house screens |
| 104 | Wild microbes / Taq / PFAS cultures / WildTrait (L5#13-15) | 2-1-3-2-1 | 9 | Non-exclusive |

**Materials (discover, then own the manufacture)**
| # | Idea | Legs | /25 | Note |
|---|---|---|---|---|
| 105 | DropIn electrolyte additives (L5#7) | 3-3-4-2-3 | 15 | Top 10 |
| 106 | PFAS-free dielectric coolant (L5 N2) | 3-3-4-2-2 | 14 | Orbital's first product |
| 107 | HT polymer film dielectric (L5 N6) | 3-3-4-2-2 | 14 | Film-line capex |
| 108 | SorbentRights (L5#8) | 3-2-4-1-2 | 12 | Pilot plant |
| 109 | FreeMag / RE-free motor co-design (L5#6, N21) | 3-3-3-1-2 | 12 | $170-605M plant |
| 110 | Ge-free IR glass (L5 N1) | 2-2-1-1-2 | 8 | Known compositions |
| 111 | Sb-free FR synergist (L5 N3) | 3-2-3-2-2 | 12 | Sb price eased |
| 112 | Ir-free PEM anode (L5 N4) | 3-3-4-1-2 | 13 | 10k-hour durability |
| 113 | PFAS-free PAGs (L5 N5) | 3-3-4-1-2 | 13 | Fab qualification |
| 114 | Biocide-free antifouling (L5 N7) | 3-3-3-1-2 | 12 | BPR approval |
| 115 | NH3-cracking catalyst (L5 N8) | 3-2-4-1-2 | 12 | Reactor hours |
| 116 | Scintillators / He-3-free detectors (L5 N9, N10) | 3-2-4-2-2 | 13 | Small market |
| 117 | PFAS-free ionomers (L5 N11) | 3-3-3-1-2 | 12 | Ionomr |
| 118 | AI-chip TIMs / loop corrosion inhibitors (L5 N12, N13) | 2-2-3-2-2 | 11 | High hit rate |
| 119 | Metal-hydride moderator stabilisers (L5 N14) | 2-2-3-2-1 | 10 | 3-5 buyers |
| 120 | Co/W-lean carbide binders (L5 N15) | 3-2-3-2-2 | 12 | Machining trials |
| 121 | Ashless EV driveline additives (L5 N16) | 3-2-3-1-2 | 11 | $100k OEM tests |
| 122 | Phosphors / H2 alloys / barocaloric / radiative coatings (L5 N17-19, N22) | 2-2-3-2-2 | 11 | Commodity |

**Machines, aviation and hardware**
| # | Idea | Legs | /25 | Note |
|---|---|---|---|---|
| 123 | EV-pack second-life grading (L6 N2) | 4-3-4-3-3 | 17 | Checked: 16 |
| 124 | Back-to-birth trace recovery (L1#19; L6#6) | 3-3-4-3-3 | 16 | Checked: 15 |
| 125 | Government-surplus mislisted lots (L1 N11; L2 N17) | 3-3-4-4-2 | 16 | x path |
| 126 | Aircraft part-out / USM teardown selection (L1 N13; L6 N6) | 2-2-4-3-3 | 14 | Lessors informed |
| 127 | Untraceable cores to ground power (L6 N5) | 4-3-2-2-2 | 13 | FTAI |
| 128 | Surplus military aviation lots (L4#14) | 3-3-3-2-2 | 13 | Overhaul |
| 129 | Timber sales with LiDAR (L4 N5) | 3-1-4-3-2 | 13 | S2 = 1 |
| 130 | GPU/network lot test-and-certify (L1 N12) | 3-1-3-3-2 | 12 | 1.3-2x |
| 131 | AlloySort / black-mass sorting (L6#16, N11) | 2-1-4-2-2 | 11 | Commodity spread; TOMRA |
| 132 | Transformer reman / DGA (L6#12, N10) | 2-2-3-1-1 | 9 | Incumbent data |
| 133 | Recast / Dedicate obsolete spares (L6#10, #11) | 2-2-2-1-2 | 9 | Job shop |
| 134 | Laid-up vessels (L2 N19) | 2-2-2-2-1 | 9 | Shipbroking |
| 135 | Orphan embodied data (L1#20) | 2-2-2-2-1 | 9 | No buyer |
| 136 | Expired FAA registrations (L2 N21) | 2-1-1-2-1 | 7 | Small |
| 137 | Breakerline / Bayline switchgear (L6#13, #14) | 1-1-1-1-1 | 5 | Supply kill |
| 138 | Armature motor repair (L6#9) | 1-1-2-1-1 | 6 | Roll-up |
| 139 | Idle fab shells / fab cryopump reman (L3 N19; L6 N18) | 1-2-1-1-1 | 6 | OEM lock |
| 140 | Used robots as a service (L6 N17) | 1-1-1-1-1 | 5 | Rental |
| 141 | Port/airport concessions (L4 N17) | 1-2-1-1-1 | 6 | Infra PE |
| 142 | Loopworks / Overwatch (L6#19, #20) | 1-1-1-1-1 | 5 | No demand / false why-now |
| 143 | Nuclear CM / heat-to-power blocks (L6#21, #22) | 1-1-1-1-2 | 6 | No discovery |
| 144 | OT/ICS software roll-up (L6 N8) | 2-2-2-1-1 | 8 | Broker multiples |
| 145 | Services: NETA, alarm, HVAC, elevator, C-UAS, NDT (L6#15, N12-14, N16, N19) | 1-1-1-1-1 | 5 | x service |
| 146 | Drilling or prospecting: Chile DGA water, geothermal/CCS pore, Indian coal (L4 N15, N18, N19) | - | - | x excluded |

## Web checks on the top 3 (everything except the ML leg)

### 1. EV-pack second-life grading: 17 -> 16 (S2 3 -> 2)

**Buy price (S1 = 4 holds):**
- Salvage acquisition is quoted at about £5-30/kWh depending on state of health ([mgrid](https://mgrid.org/?p=4285)).
- An unverified, unattributed consultant figure puts it at $20-60/kWh, with $20-70/kWh for refurbishment (search snippet only; source not opened).
- Both ranges come from search summaries. I did not open the source pages.

**The ceiling on the proven state:**
- BNEF's Dec 2025 survey: stationary-storage packs fell 45% to **$70/kWh**, and LFP averaged $81/kWh across segments ([BNEF](https://about.bnef.com/insights/commodities/lithium-ion-battery-pack-prices-fall-to-108-per-kilowatt-hour-despite-rising-metal-prices/), [Taiyang](https://taiyangnews.info/business/bloombergnef-battery-pack-prices-hit-new-low-in-2025)).
- B2U installs second-life storage at under $100/kWh, against about $149/kWh for new installed systems ([mgrid](https://mgrid.org/?p=4285)).
- So a certified module can be worth about 2-4x the salvage price, but refurbishment eats much of that. Gross step-up is about 2-3x, so **S2 = 2**.
- US FEOC and tariff rules on Chinese cells may widen the gap in the US (inference, not checked).

**Who holds it (S5 = 3):**
- Redwood Energy has "multiple GWh" of repurposed inventory approved for BESS and a 63 MWh Crusoe microgrid. Redwood raised $350-425M (sources conflict) ([ESN](https://www.energy-storage.news/redwood-energy-positions-second-life-bess-as-essential-infrastructure-for-us-data-centre-load-growth-domestic-manufacturing-needs/), [Redwood](https://www.redwoodmaterials.com/news/2025-a-defining-year-for-redwood/)).
- Moment raised a $40M Series B, over $100M in total ([ESN](https://www.energy-storage.news/?p=100476)).
- The rung is funded, but none of these sells grading as its moat. Redwood's advantage is pack flow.

**Path:** large, since second-life BESS sells into data-centre and utility demand. S4 = 3 holds: grading is the value, and repack is doable with a partner.

### 2. UK small-site plot engine: 16 -> 15 (S1 3 -> 2)

**Base rate and pool:**
- London 5-9 unit schemes are approved at 54%, against 81% for schemes of 50+ units.
- Small sites win about 21% of appeals, against about 40% for major schemes.
- Small applications are down 55% since 2018, and some councils approve at 80%+ (Cornwall, Telford) ([Searchland](https://searchland.co.uk/guides/small-residential-sites-market-trend-data), [Construction Index](https://www.theconstructionindex.co.uk/news/view/study-reveals-london-planning-authority-bias-against-small-builders)).
- 3-9 unit approvals were about 17k in 2024, against 35k historically, and 94% of applications missed the statutory deadline ([Housing Today/HBF](https://www.housingtoday.co.uk/news/approvals-for-smallest-sites-halve-hbf-report-shows/5138641.article)).
- Wide variation between councils is good for a ranking model (S3 stays at 4). The shrinking pool comes from SME economics, not from plots nobody has found.

**Step-up:** serviced plots sell for £100k-400k each, and value uplift is proportionally larger in high-value areas ([planningsignal](https://planningsignal.co.uk/knowledge-hub/property-development/planning-permission-increase-property-value)). Consent lapses after 3 years. S2 = 3 holds.

**S1:** homeowners know their garden exists and will ask for a share, so the option price carries hope value. S1 = 2.

**Policy:** the 2026 reforms promise simpler rules for small sites ([homebuilding](https://www.homebuilding.co.uk/news/planning-reforms-could-be-revolutionary-for-the-self-build-industry)). That is a tailwind, but if outcomes become more by-right, the ML lever shrinks.

**Who already does it:** Searchland, LandTech and Plota sell screens, which caps S5 at 3.

### 3. Back-to-birth trace recovery: 16 -> 15 (S2 3 -> 2)

**Step-up:**
- Engines and LLPs without adequate back-to-birth documentation lose **20-50%** of market value ([Safe Fly](https://safefly.aero/?p=15576), [ISTAT Jetrader](https://nxtbook.com/nxtbooks/ISTAT/jetrader_autumn2020/index.php?startid=45)).
- So restoring the trace is about 1.25-2x on a whole engine. That rises to 3x+ only on individual LLPs that would otherwise be scrapped, which is a narrower pool. **S2 = 2.**
- Back-to-birth is a commercial standard, not a regulatory one: regulators accept trace to the last operator ([ATW](https://atwonline.com/mro/supply-chain/usm-specialists-mull-options-improve-parts-traceability)). The discount could therefore shrink if lessors relax the standard after AOG Technics ([Aviation Week](https://aviationweek.com/mro/supply-chain/opinion-aviation-must-align-parts-traceability-vision)).

**Who already does it:** ProvenAir runs AI trace for landing gear and parts as a **service**, with about $1.8-3M raised ([CB Insights](https://www.cbinsights.com/company/provenair-technologies/), [VCBacked](https://www.vcbacked.co/company/provenair-technologies)). It is small, so the "own the parts" version is open. AerFin and AerSale do trace in-house.

**S1 = 3:** discrepant parts are separated out at part-out, so they can be bought cheaply. The records, though, sit with the original operators.

**S5 = 3:** a growing archive of reconstructed operator records compounds.

**Path:** USM is a multi-billion-dollar market (from memory, not checked).

## Takeaways
- Plausibility moved the ML leg, but the slice's ceiling stays at S1, S2 and S4.
- Shapes that come closest have three things in common:
  - a cheap physical item graded by ML (battery packs, parts);
  - a planning outcome predicted from many weak signals;
  - an owner who sells for a "can't tell" discount.
- In all of them the proven-state premium is 2-3x, not 3x+.
- Worth a combined look with other slices: **EV-pack grading (16)** and **UK small sites (15)**. Both have the most prospectivity-like S3 and a real compounding loop from their own outcomes.
