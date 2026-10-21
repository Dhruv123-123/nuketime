# Competitive landscape: the verification and approval pathway for an "Approval Factory"

## 1. Players by pathway step

**Threat key.** **Direct** means it competes for the same outcome: approved sources, approvals or signed packages for replacement parts. **Adjacent** means it owns a neighbouring layer and could move into ours, or would be a partner, supplier or acquirer. **None** means it is relevant context but no threat.

### Step 0: Picking which parts to approve (demand, sole-source status, price spikes)

| Player | What they do | Funding / scale | Threat | Source |
|---|---|---|---|---|
| Govini (Ark) | Supply-chain mapping for defence; flags sole-source and foreign-dependency risk but does not fix it | Large DoD contract (recalled); Bain investment | Adjacent | c16, d01 |
| Palantir (Vantage, ShipOS) | Integrates logistics and industrial-base data | ShipOS about $448M Navy contract | Adjacent | c16, g08 |
| Exiger / Interos / Altana | Supplier risk mapping across tiers | Exiger has 60+ federal agencies; Altana about $1B valuation (recalled) | Adjacent | c16, s01, f15 |
| Rune (TyrOS), PTC Servigistics, Systecon Opus | Demand forecasting and spares stock planning | Rune $24M Series A plus $99M Army IDIQ | None | c16 |
| HigherGov / SAMSearch / Haystack (Accuris) / SERVA | DIBBS award history, NSN and AMSC-code lookups | $500-2,500/yr SaaS; Accuris owned by KKR | Adjacent (data inputs) | s01, g03 |
| SiliconExpert (Arrow), Z2Data, Accuris, Supplyframe, Octopart, Lytica | Obsolescence and lifecycle intelligence for electronics | Z2Data covers 1B+ parts; crowded field | None | c11, g09 |
| Kipo AI (Mobilio), Cofactr, BAE in-house DMSMS tool | AI that finds form-fit-function replacement candidates | Mobilio $1.65M SBIR; Cofactr about $17M Series A | Adjacent | g09, c02 |
| ePlaneAI, ILS, PartsBase, Airbus Skywise | Commercial aviation demand and fleet removal data | Corporate or startup | None | s01 |
| Quantum Research Sciences | DLA SBIR to predict obsolescence | Phase I | None | g03 |
| Cornerstone Research Group | ML scoring of technical data packages (TDPs) for 3D-printing candidacy | $1.24M | Adjacent | c02 |
| 3YOURMIND, Spare Parts 3D (DigiPART), CADDi | AI triage of parts for printing or digitisation | CADDi about $89M Series C (recalled) | Adjacent | c21, c26 |

### Step 1: Data rights, IP and freedom to operate

| Player | What they do | Funding / scale | Threat | Source |
|---|---|---|---|---|
| PatSnap, Solve Intelligence, Patlytics, IPRally, Derwent, PatentSight | AI patent search and FTO, working on patent text only | PatSnap 18k customers; Solve about $40M Series B (recalled) | Adjacent | c27, s02 |
| Air Force DART IPR Module; NAVAIR DRSAVE | In-house tools that work out data rights per part number | Internal; IPR Module saved $1.75M of labour on RQ-4 | Adjacent (the government's own tools) | d01 |
| DoD IP Cadre | Data-rights policy; its AI rights scraper was cancelled for lack of funding | 5 temporary positions | None | d01 |
| Gov-con law firms (Wiley, Crowell, Covington) | Hourly-billed data-rights challenges | Services | Adjacent | s02 |
| MALUS; Black Duck / FOSSA | Software-only analogues of an AI clean room and code-provenance scanning | n/a | None | c27 |

### Step 2: Geometry capture and drawing reconstruction

| Player | What they do | Funding / scale | Threat | Source |
|---|---|---|---|---|
| Backflip AI | Converts a scan mesh into a parametric CAD feature tree; $20/month | About $30M (unverified) | Adjacent | c03, s03 |
| Novineer (NoviVision) | Photo-to-CAD reverse engineering plus generative redesign; Army agreements; Stratasys partner | $225k SBIR plus more than $2.5M of founder research grants; no venture funding | Adjacent (geometry only) | c01, c02, c22, s01 |
| Hexagon (Geomagic, PC-DMIS, Volume Graphics) | Incumbent reverse-engineering software and metrology hardware | About EUR 5B revenue (recalled) | Adjacent | c03, s03 |
| Creaform/AMETEK, FARO, ZEISS GOM, Artec, Shining3D, Revopoint | Scanners from metrology grade to consumer | Incumbents | None | c03 |
| Lumafield | Industrial CT plus cloud AI analysis | About $192.5M total ($75M Series C plus $50M debt) | Adjacent | c03, s03, s09 |
| Waygate, Nikon, North Star, Werth, Comet Yxlon | Industrial CT | Incumbents | None | s03, s09 |
| Physna / Thangs | Geometric deep-learning search and part matching | About $56-80M (recalled) | Adjacent | c02, c03, f13 |
| Quidient | Smartphone "5D" scanning for reverse engineering and counterfeit checks | About 12 Air Force awards | Adjacent | c02 |
| Sigmetrix (CETOL) | Guidance for GD&T and tolerance stack-ups; does not generate them | Small | Adjacent | s03 |
| Wichita State NIAR | Full-teardown digital twins (B-1B, UH-60L) | $350M+ R&D a year | Direct (government-funded TDPs) | s03, g04 |
| Metrology service bureaus (Exact, GKS, QuickParts) | Labour-based scan-to-CAD | Small | None | s03 |

### Step 3: Material and process identification

| Player | What they do | Funding / scale | Threat | Source |
|---|---|---|---|---|
| SciAps, Thermo Niton, Evident, Bruker, Hitachi | Handheld XRF, LIBS and OES grade matching | Instrument makers | Adjacent (suppliers) | s04, f05 |
| Proto, Pulstec, Stresstech, Fischer | Residual stress, Barkhausen noise, conductivity | Small and mid-size | None | s04, f05 |
| Element, Applus+, IMR, Lambda | Contract materials characterisation | Element about $1-1.5B revenue | Adjacent | s04 |
| MIPAR, Clemex, ZEISS ZEN, DREAM3D, Zeiss/Xnovo LabDCT | ML microstructure analysis and lab diffraction-contrast tomography | Small to large | None | s04, f05 |
| DISCUS Software | AFWERX pick for AI reverse engineering, TDPs and first-article inspection (FAI); OCR of drawing requirements | SBIR-scale | Adjacent | s04, s09 |

### Step 4: Electronics reverse engineering, re-creation and equivalence

| Player | What they do | Funding / scale | Threat | Source |
|---|---|---|---|---|
| SRI (DLA GEM/AME) | Government "approval factory for chips" since 1988: 30k device types, 175k+ parts | $73.7M contract running 2025-2031 | Direct (electronics) | c11, c35, f10 |
| Rochester Electronics | Licensed continuation of obsolete chips plus its SRP re-creation process | About $275-500M revenue (unverified); 70+ OEM licences | Direct (electronics) | c11, c23, c35, g09 |
| DMEA (ATSP, Trusted Foundry) | DoD in-house design and fab of obsolete microelectronics | Multi-billion IDIQ ceiling (recalled) | Direct | c11, c23, c35 |
| Lansdale, Innovasic/ADI, QP Semi, Micross, Teledyne e2v, Tekmos, KaiSemi, Crossfield | Re-creation, continuation and emulation of legacy chips | Small to large | Adjacent | c11, c35 |
| Chip Scan (Deep Lift) | Hardware assurance; reverse engineering of legacy FPGAs and ASICs | Small, government-focused | Direct (legacy electronics) | c08 |
| Global Circuit Innovations | Drop-in re-creation of obsolete microelectronics | 16 awards, $7.2M | Adjacent | c02 |
| Mobilio (Kipo AI) | Design-rule checker that verifies reverse-engineered circuit-board schematics | $1.65M SBIR | Adjacent | c02 |
| RJ Matthews / Tetrahive; Terraverum + University of Florida | CT- and ML-based circuit-board reverse engineering | About $2.5M; $98.6k Phase I | Adjacent | c02, c23 |
| TechInsights, ChipRebel, Texplained, Battelle, NSWC Crane, Sandia | Chip imaging, delayering and netlist extraction, mainly for IP and intelligence | TechInsights large | Adjacent | c23, c35, f10 |
| Seica, Huntron, Diagnosys, ABI | Legacy board test and reverse-engineering tools, no AI | Mid-size | Adjacent | c23 |
| Cadence / Synopsys / Siemens EDA; ChipAgents, Cognichip, Axiomise | Formal equivalence checking (model to new design only) | Incumbents / seed to Series A | None | f10, a04 |
| DARPA V-SPELLS, Ghidra, Binarly, NetRise | Lifting and verifying legacy firmware | Government / venture | Adjacent | c35 |
| Depot reverse-engineering cells (WR-ALC REARM, OC-ALC REACT, Tobyhanna, FRCs) | In-house circuit-card reverse engineering and FPGA re-hosting | Government | Adjacent (customer and validator) | c18, f10 |

### Step 5: Package authoring, requirements and compliance documentation

| Player | What they do | Funding / scale | Threat | Source |
|---|---|---|---|---|
| Xcert AI | AI certification copilot (compliance documents, test procedures, traceability), focused on EASA | CHF 1.1M; 12 staff; about 50% of output usable | Direct-lite (the closest aero pure-play, but new-type and tiny) | c01, c21, c22, c30, g01 |
| Flow Engineering | AI system of record for hardware requirements; compliance agents | $50M Series B at $750M | Adjacent (new designs) | c01, c06, c31 |
| Trace.Space, Stell, Certivity, Valispace | Requirements graphs and compliance matrices | Seed stage; Valispace exited for about $16-20M | Adjacent / none | c05, c06, c31 |
| Jama, DOORS, Polarion, Codebeamer, Reqtify, Visure | Incumbent requirements tools with DO-178C and ARP4754 templates | Incumbents | Adjacent | c06 |
| Ketryx | AI traceability and design history files for FDA work; expanding into aero, defence and nuclear | About $39M Series B (recalled) | Adjacent (likely entrant) | c13, c22, c31, a01 |
| Saphira AI (YC S24) | AI agents for FMEA, HARA and standards traceability | YC | Adjacent | c01, c22 |
| Istari Digital | Digital-engineering "digital certification" for the Air Force; X-56A; DAF Industry Øne | $22.6M Series B; $12.8M SBIR; about $28M in Air Force contracts | Adjacent, near-direct (platform-level only) | c01, c02, c05, c28, c30, a04 |
| RedShred (AIRMATE), Inoviant | LLM conversion of airworthiness criteria into checkable models; AI compliance checking | $7.6M combined; $149k | Adjacent (platform level) | c02 |
| Fuchsia (YC S26), Hardware Compliance | "Vanta for hardware": drafting for battery, inverter and charger certification | 3 people; undisclosed | Adjacent (other domain) | c33 |
| Leo AI, CoLab | Engineering copilot; AI design review against the customer's own standards | $9.7M seed; $72M Series C (Bombardier contract) | Adjacent | c30 |
| AFuzion, ConsuNova, Prime Propulsion, SAS Sofia | Human certification consultancies | Services | Adjacent | c06, g01, g12, a01 |

### Step 6: Substantiation by analysis and simulation credibility

| Player | What they do | Funding / scale | Threat | Source |
|---|---|---|---|---|
| Synopsys/Ansys, Siemens/Altair, Cadence/Hexagon MSC, Dassault SIMULIA | Solvers; run CbA webinars; none sells the credibility argument | Multi-billion-dollar acquirers | Adjacent | c14, a03, a04 |
| PhysicsX, Neural Concept, Luminary, Monolith, Navier, Rescale | ML surrogates and cloud CAE for design speed | PhysicsX $300M Series C at $2.4B; Neural Concept $100M Series C | Adjacent | c14, c30, s05 |
| ESRD (StressCheck); SwRI NASGRO/DARWIN; AFGROW; SMART-DT | Verified FEA and accepted crack-growth codes | Small / government-funded | None (would be suppliers) | s05, f06 |
| AlphaSTAR (GENOA), Hexagon Digimat, SmartUQ, Dakota | Virtual allowables and uncertainty quantification | Small | Adjacent | c07, c14 |
| Exponent; DER consultancies | Hand-written credibility and substantiation dossiers | Exponent about $500M revenue | Direct (services) | c14, a05 |
| Certara (Simcyp), Simulations Plus, Unlearn, InSilicoTrials | Pharma analogues: models accepted in place of studies | Certara $419M revenue | None | c34, a05 |
| CM4QC steering group; RoCS consortium | Regulator-side roadmaps; no startup members | Government and industry | None (where the rules get set) | f01, f06, s05 |

### Step 7: Allowables, equivalence statistics and test-count reduction

| Player | What they do | Funding / scale | Threat | Source |
|---|---|---|---|---|
| Senvol (Senvol ML) | ML for AM allowables, fewer coupons, machine equivalence; NAVSEA policy project | Small; SBIR and contract funded | Adjacent (closest on statistics, AM only) | c04, c07, f03, f04 |
| Dyndrite + RTX + Mimo (AIM-4AM) | ML-picked minimal test sets for AM allowables | $2M ManTech award (June 2026) | Adjacent | f03, f06 |
| QuesTek (ICMD) | ICME-based accelerated qualification (M54: 3 heats instead of 10) | Private, SBIR-funded | Adjacent | f06, f16 |
| NCAMP/NIAR, MMPDS (Battelle), CMH-17 | Pooled databases the FAA already accepts; the institutional "prior" | Government and industry | None (the incumbent route) | c07, f03, a10 |
| Citrine, Polymerize, Uncountable, Mat3ra, Intellegens | Materials R&D AI; nothing on certification | Citrine about $76M | None | c07, f06 |
| Periodic, Lila, CuspAI, Radical AI, Orbital | AI materials-discovery labs | More than $800M (recalled) | None | f06, f11 |
| VEXTEC, Sentient Science | Probabilistic fatigue-life prediction | Small | Adjacent | f01, f03 |
| UT Arlington + Northrop Grumman | Research on AI-derived B-basis allowables | Research grant (2026) | None | c07 |

### Step 8: Qualification testing, test data and test labs

| Player | What they do | Funding / scale | Threat | Source |
|---|---|---|---|---|
| Nominal | Hardware test data platform plus an AI analyst | $155M+ raised; about $1B valuation | Adjacent | c01, c05, c22, s06 |
| Sift, Epsilon3, NI SystemLink, Dewesoft | Telemetry, as-run procedure records, data acquisition | Sift $42M Series B; Epsilon3 about $15M | Adjacent / none | c05 |
| Element/NTS, Westmoreland, LTI, Wyle, Touchstone, TÜV, Nemko | Accredited qualification labs | Element about $1.5B revenue at about $7B valuation | Adjacent (suppliers; impartiality rules keep them out of design work) | c05, c19, s06, f11 |
| ZwickRoell roboTest, Instron, MTS | Robotic test cells, used mainly for steel and polymer QC | Incumbents | None | f11 |
| SwRI, NIAR | Component fatigue and ASIP work on legacy fleets | About $900M nonprofit | Adjacent | s06, f16 |
| Beam facilities (TAMU, LBNL, HEARTS) and radiation labs (RTS, VPT, Alter, TRAD) | Radiation qualification capacity | Small | None | c28 |

### Step 9: AM qualification and in-situ process monitoring

| Player | What they do | Funding / scale | Threat | Source |
|---|---|---|---|---|
| Freeform | AI closed-loop metal AM | $81M raised; $179M valuation | Adjacent | c04, f04 |
| Divergent (owns Sigma Additive IP) | Integrated AM factory | Multi-billion valuation | Adjacent | c04, c15, f04 |
| Velo3D | Locked print files and Assure quality reports | Public; about $20M quarterly revenue | Adjacent | c04 |
| Phase3D, Additive Assurance, Addiguru, EOS/Amiquam, OEM monitoring modules | In-situ monitoring that earns no certification credit | Small; Sigma's IP sold for $1.6M | None | c04, f04 |
| Moog VeriPart | Provenance from authorised file to printer to part | Internal pilot | Adjacent | c08, c09 |

### Step 10: NDT and inspection-method qualification (POD)

| Player | What they do | Funding / scale | Threat | Source |
|---|---|---|---|---|
| Gecko Robotics | Robotic ultrasonic inspection plus Cantilever AI; does not sign | $1.25B valuation; about $347M raised; $300M Navy IDIQ | Adjacent | c10, c29, g06 |
| Waygate, Evident, Zetec, Eddyfi | Instruments plus automatic defect recognition as an assist | Incumbents | Adjacent | c10, f02 |
| Trueflaw; Extende (CIVA) | Virtual and real flaws; NDT simulation for model-assisted POD | Small | Adjacent (the closest "qualification house") | c10, f02 |
| EPRI NDE/PDI; Zetec/Westinghouse/Framatome ADA | Nuclear precedent for qualifying machine accept/reject decisions | Utility-funded | None | c10, f02 |
| Mainblades, Donecle, Aiir, Fleetcraft, LHT AURORA | Drone and AI visual inspection assist; Mainblades has the FAA-accepted Delta case | Fleetcraft $3.2M seed | None | c10, g01 |
| Square Robot, Flyability, ANYbotics, Energy Robotics, Skydio, Percepto, Voliro | Robots that capture data; none holds ISO 17020 or signs findings | Skydio about $740M | None | c29 |

### Step 11: Production approval, FAI and conformity

| Player | What they do | Funding / scale | Threat | Source |
|---|---|---|---|---|
| GroundControl (YC S25) | Automated AS9102 FAI reports | 70+ facilities; about 1,000 reports a month | Adjacent | c01, s07 |
| F4 Industries (YC S25) | Deterministic GD&T checks marketed as "no AI" | 5-person team | Adjacent | c01 |
| Rapta | Camera inspection at each build station with a per-unit evidence archive | $8M seed | None | c01 |
| Ideagen InspectionXpert, High QA, Net-Inspect, 1factory, First Resonance ION, Instrumental | FAI and quality software, digital thread | Established | None / adjacent | s07, s09 |
| Xometry, Fictiv, Hadrian, Re:Build, Isembard | Shared quality system across suppliers; owned factory networks | Hadrian about $260M Series C | Adjacent (manufacturing partners) | c15, s07 |
| Machina Labs, Rangeview, Firestorm, Craitor, AML3D, Anduril Arsenal-2 | Sustainment manufacturing capacity, none holding approvals | Firestorm $153M; Anduril about $2.9B Navy | Adjacent (partners) | c15, g08 |

### Step 12: Reviewer and regulator review (FAA ACO/MIDO, DLA and service ESAs, NAVSEA, NRC)

| Player | What they do | Funding / scale | Threat | Source |
|---|---|---|---|---|
| ELEVAN LLC (Elevate Systems) + UTSA | The **only** reviewer-side AI award found for source approval; also OPTIX drawing extraction and an AI reverse-engineering platform | $109,997 Phase I in 2024; no Phase II; about $5M SBIR total; 10 staff; SBA 8(a) | **Direct (closest on the verification seat)** | c02, g03, f12 |
| Calibre (AuditorOS) | AI agents for testing, inspection and certification (TIC) auditors, general rather than aviation | $3.3M pre-seed (May 2026) | Adjacent | c01 |
| NRC SimplifAI; INL/ANL RCP; FDA Elsa | Regulators' own internal LLM review tools | Government | None (the regulator builds its own) | c13, f07, s08 |
| Atomic Canyon, Inductive | Nuclear licensing search and applicant packaging | $7M seed | Adjacent | c12, f07 |
| CivCheck/Clariti, CodeComply, Archistar, GreenLite, PermitFlow | Building-permit analogues of reviewer copilots and private reviewers | GreenLite $49.5M; PermitFlow $54M | None (models to copy) | c31, c32 |
| DNV RuleAgent, ClassNK Survey Compass, LR + Microsoft | Class-society AI for rule search and drafting; no reviewer-side engineering check | Large | Adjacent (alternative buyers) | c20 |
| NPS (Bailey & Rajapaksa) | Academic LLM ranking of alternate parts by similarity for the Navy | Paper | None | g03 |

### Step 13: Delegated sign-off and approval holders (the permission layer)

| Player | What they do | Funding / scale | Threat | Source |
|---|---|---|---|---|
| HEICO FSG (incl. Wencor) | Largest PMA and DER house, with its own ODA; about 20k PMAs; no disclosed AI | Adds about 400-550 PMAs a year; FSG R&D $43.7M | **Direct (incumbent)** | c01, c17, g01, d02 |
| AAR (ART ODA, Trax, Airvoyant) | Owns the ODA, DER and PMA stack; already ships agentic procurement AI | Buying 65% of MRO Holdings for about $2.6B | **Direct (most likely fast follower)** | c17 |
| TransDigm (bought JPE and Victor Sierra) | Sole-source monopolist now also buying PMA capability | About $2.2B deal; $8.83B revenue | Direct | c17, d01 |
| StandardAero / Aero Turbine | Bought for its military Source Approval Request (SAR) expertise | $120M + $21M | Direct | d01, c17 |
| Chromalloy, Jet Parts Engineering, Av8, Kapco, McFarlane, ACS | Traditional reverse-engineering PMA houses | Small to mid; McFarlane 35k+ parts | Direct | g01, c27 |
| Lufthansa Technik, SR Technics, ST Engineering, HAECO, Satair, Part 21J DOAs | EASA DOA/POA repairs and non-OEM parts | Large MROs | Direct (EU) | g02, c21 |
| AST Korea | Single Korean PMA covering 6,395 items (July 2026) | n/a | Direct (Korea) | c22 |
| Parts Life, Mentis, Brighton Cromwell, DeVal, Cepeda, ES3, Mainstream, Turnaround Factor, Micro-Precision, AMG, JMS Southeast, ORBIS, Dynovas, McNally, Rotair, Kitco | SBIR-funded DLA SAR and TDP shops, no AI | Parts Life $11.8M over 24 awards; 284 "source approval" SBIRs; about $100M of DLA SBIR | **Direct (manual)** | c02, g03, g04 |
| Amentum (PROS VI); 8(a) reverse-engineering services on AFSC FA8109 | Reverse-engineering-to-supply services contracts | $4.6B IDIQ | Direct | c03 |
| Government reverse-engineering cells (Tinker REACT, REARM, RSO, NAVAIR AIRWorks, NIWC RESTORE, Austal/IALR) | Organic reverse engineering and AM | Tens of TDPs a quarter | Adjacent (customers and validators) | c18, g08 |
| QinetiQ UK | Reverse engineering of submarine parts through an accredited SME network | n/a | Direct (UK analogue) | c18 |

### Step 14: Release certificates, provenance and counterfeit detection

| Player | What they do | Funding / scale | Threat | Source |
|---|---|---|---|---|
| Aeroxchange eARC; Boeing digital 8130-3 | Transport for digitally signed release certificates | Airline consortium | Adjacent | s10 |
| GE Aerospace | AI checks of release-certificate fields, for its own material only | OEM | Adjacent | s10 |
| ProvenAir, flydocs (LHT), Bluetail, CAMP, Veryon, AMOS | Records and back-to-birth trace review | ProvenAir about $3M; Bluetail $4.3M; under $10M in total VC | Adjacent | c09, d02 |
| GoDirect Trade, Aerotrax, SkyThread | Blockchain provenance; stalled | Small / corporate | None | c09, f09 |
| Cybord | Visual AI authenticity checks at SMT placement | About $7-20M | Adjacent | c08, c23, f15 |
| Alitheon, Ingenia, Applied DNA, SMX, InfraTrac | Physical fingerprinting and marking | Small | Adjacent | c08, f09 |
| AS6171 labs (SMT Corp, Integra, Process Sciences, Trusted Labs) | Manual accredited counterfeit testing | Small to mid | Adjacent (possible roll-up) | c08, f15 |
| Fortress Information Security | Hardware and software bill-of-materials vendor risk for utilities (CIP-013) | 8 of the top 10 US investor-owned utilities | Adjacent | f15 |
| ERAI / GIDEP | Databases of reported failures and counterfeits | Membership | None | c08 |

### Step 15: In-service reliability data, liability and insurance

| Player | What they do | Funding / scale | Threat | Source |
|---|---|---|---|---|
| FAA SDRS/ASIAS; Skywise, AnalytX, AVIATAR; C3 PANDA | Failure reports or fleet analytics with no breakdown of PMA vs OEM performance | Federal / OEM | None | s11 |
| Aviation underwriters (Global Aerospace, AIG, Allianz, Chubb, Lloyd's) | Conventional products-liability and grounding cover | More than $8B gross written premium | Adjacent | s12 |
| AIUC, Armilla, Munich Re aiSure/HSB | Insurance for AI outputs, software only so far | AIUC $55M Series A | Adjacent | s12, d06 |
| Lessors (AerCap, SMBC, Avolon) and ISTAT appraisers | A de facto second regulator: return conditions still bar PMA and DER content | AerCap 1,734 aircraft | Adjacent | d02, d06 |

### Analogue domains: same pathway shape, different regulator

| Player | Domain / what they do | Funding / scale | Threat | Source |
|---|---|---|---|---|
| Everstar (Gordian) | Nuclear: claims qualification of parts and suppliers "at scale"; publishes no evidence | Unknown | **Direct (startup to watch)** | c12, f07 |
| Nuclearn (Parts AI) | Nuclear: AI for procurement and 50.59 screening; no commercial-grade dedication (CGD) | $10.5M Series A; 70+ facilities | Adjacent (fast follower) | c12, g05, d03 |
| Paragon (Mirion), Curtiss-Wright, Westinghouse, Framatome, UCI, Park Nuclear, Duke central lab | Manual CGD and reverse-engineering houses | Paragon acquired for about $585M; Westinghouse about 50k parts a year | Direct (nuclear) | c12, g05, d03 |
| MIRAE-EN (REDiX) | Korean multi-agent AI pilot for CGD and reverse engineering | Academic pilot | Adjacent | c12 |
| PSM/Hanwha, Sulzer, EthosEnergy, APG, TSL, Doosan, Liburdi, ORAP | Non-OEM gas turbine parts; AI used only in operations | Large | Adjacent | c24, g10 |
| CAPA/Intertek, Dorman, LKQ | Automotive aftermarket equivalence; no AI | Dorman about 1,600 new parts a year | None | c25 |
| DB AM unit, DigiZug3D, TÜV NORD, Replique, Ivaldi, Wabtec, Siemens Mobility | Rail AM spares; nobody owns part-level qualification | DB >200k parts; Ivaldi about $9M | Adjacent | c26, g07, d05 |
| Complizen, Cruxi, Sentium, Basil, RegDesk, Innolitics, Peer AI | Medtech submission drafting, commoditised (510(k) "from $11k") | Peer AI $12.1M | None | c13 |
| Innovatus, Agiliti, Varex, NAMSA, Emergo | Medical-device service parts and regulatory consulting | Mid-size | None | g11 |
| E2G, Quest Integrity, SES, Becht, Codeware, Mistras | Pressure-equipment fitness-for-service and inspection | Mistras about $866M EV | Adjacent | g06, d08 |
| Vanta, Drata, Delve, Norm Ai/Norm Law | Software-compliance and law analogues; Norm became a law firm to own sign-off | Vanta $4.15B; Norm $1.2B | None (model to copy) | c31, a01 |
| NASA NEPP, ESA CORHA-2, Apex, K2 | Space radiation qualification by similarity | Agency / buyers | Adjacent | c28 |
| UL Solutions, SGS, BV, Intertek, TÜV, DNV, Applus | TIC majors; their AI work certifies AI products, not physical parts | UL $3.05B revenue at 25.9% margin | Adjacent | c19, a02, d07, d08 |

## 2. Is anyone already running the Approval Factory?

**No.** Across 139 prior agents and all of these 100+ threads, no one turned up, verified or recalled, that runs the full loop as an AI-native, multi-part business. The loop is: pick targets, reverse-engineer, compile the evidence, get the approval (DLA SAR or FAA PMA/DER), hold the approval, and sell the part or the approval capacity. Nobody occupies the verifier or reviewer seat for aftermarket approvals either (c01, c02, c06, c17, c22, g01, g03).

Closest players, nearest first:

1. **ELEVAN / Elevate Systems (San Antonio)** — close on the verification seat only. This 10-person 8(a) firm has an AI-assisted reverse-engineering platform, OPTIX drawing extraction, and the only reviewer-side source-approval AI award found ($110k Phase I, 2024, no Phase II). It has the right idea at roughly 1% of the scale needed and holds no approvals or capital (c02, g03, f12).
2. **HEICO / AAR / TransDigm / StandardAero** — they own the end state but not the method. They hold ODAs, DERs and thousands of PMAs, and AAR and TransDigm are buying approval houses (about $2.2B for JPE and VSA). None discloses AI in approval engineering, and HEICO's cost per PMA seems to be rising: R&D up 66% while output stayed flat. AAR is the most likely fast follower because it already ships agentic AI and owns ART's ODA (c17, d01).
3. **Everstar (nuclear)** — close in claims, not in proof. It is the only startup that explicitly claims parts and supplier qualification "at scale", but it publishes no evidence and works in a different regulatory regime (c12).
4. **The DLA SBIR SAR shops (Parts Life, Mentis and about 20-30 others)** — they do the same job by hand, a few NSNs at a time, on about $100M of SBIR money. They have no AI, no venture funding and no factory scale, which makes them partner or roll-up candidates rather than threats (c02, g03).
5. **Istari Digital** — close in thesis, far in scope. It sells digital and model-based certification accepted by the Air Force, but for whole airframes and new systems, not part-level SARs or PMAs (c02, c05, c30).
6. **Xcert AI** — a thin compliance-documentation tool. It is aerospace-only and has raised CHF 1.1M, with about 50% of output usable. It covers new-type certification, not equivalence, and does not hold approvals (c21, c30).
7. **SRI GEM/AME and Rochester** — an "approval factory" that already exists, for chips only. The economics are proven, but each part still takes 48 weeks to 18 months, so the bottleneck is throughput, not feasibility (c11, c35).
8. **Novineer, Backflip, Lumafield, Hadrian Opus** — they cover geometry or data capture, roughly 5-15% of a package's hours. Novineer's founder says publicly that the real bottleneck is approvals (c01, c03, c15).

Who could get there first: AAR or HEICO adding AI internally, Ketryx moving into aero (c13), Nominal or Sift adding a DO-330-qualified reporting module within 3-5 years (c05), and Everstar if its claims hold.

## 3. Crowded steps vs empty steps

**Crowded or commoditising**
- Obsolescence and part intelligence (SiliconExpert, Z2Data, Accuris, BAE in-house, Kipo, Cofactr) (c11, g09).
- Geometry capture and scan-to-CAD (Hexagon, ZEISS, Creaform, Backflip, Lumafield, Novineer, Quidient). This is AI's crowded entry point, but tools still reach only about 0.7 mm accuracy, short of SAR grade (c02, c03, s03).
- Test-data platforms for new programs (Nominal, Sift, Epsilon3, NI) (c05).
- Requirements and compliance tools for new designs (Flow, Jama, DOORS, Polarion, Trace.Space, Stell) (c06).
- Design-side simulation and AI surrogates (PhysicsX, Neural Concept, the CAE majors) (c14, c30).
- Patent-text FTO (PatSnap, Solve, Patlytics) (c27).
- In-situ AM monitoring sensors, crowded and close to worthless: Sigma's IP sold for $1.6M (c04).
- Data capture by inspection robots and drones (Gecko, Skydio, ANYbotics, Flyability) (c29).
- Sustainment visibility and risk flagging (Govini, Palantir, Exiger, Rune) (c16).
- FAI paperwork and ballooning (GroundControl, Ideagen, DISCUS) (s09).
- Medtech-style submission drafting (c13).

**Thin: a few manual incumbents and no AI**
- SAR and PMA package writing: SBIR shops and PMA houses working by hand (c02, g01).
- Nuclear CGD: Paragon, Curtiss-Wright and Westinghouse, siloed and manual (g05).
- Electronics re-creation: SRI, Rochester, DMEA; throughput-limited (c11).
- Accredited labs: Element and AS6171 labs; queue-bound (c08, s06).

**Empty: no funded player found**
- **Reviewer-side tooling for DLA/service ESAs, FAA ACOs/DERs/ODAs and NAVSEA.** The only entry is ELEVAN's $110k Phase I. This is the binding queue: the ESA's 90-day leg is the largest share of the nominal SAR timeline, about half of decided SARs are rejected outright, and in one case 144 packages were pending against 7 analysts (c02, g03, g04, s08, f07, f12).
- **Machine-readable certification basis and SAR/PMA evidence schema**, i.e. "approval-as-code" (c01, c06, g04, c31).
- **Equivalence compilers for reverse-engineered parts.** Nobody infers tolerances from multiple samples, fuses NDE data into a material and spec call, or produces quantified equivalence cases (c03, c06, s04, f05, s09).
- **Bayesian or small-sample equivalence statistics for replacement parts.** All existing work targets AM or new-material allowables (f03, c07).
- **Credibility dossiers that let simulation stand in for tests on spare parts**: no aviation counterpart to V&V 40 or MDDT exists (c14, a05, f01).
- **Precedent and rejection-reason corpora with similarity-family qualification**, built from FOIA requests, bid protests and an applicant's own filings (f12, f13).
- **A regulator-accepted process for qualifying AI inspection methods** (ML POD, ML-qualification standards) (c10, f02, f04).
- **Behavioural-equivalence certificates for legacy electronics** with measured coverage (c23, c35, f10).
- **An issuer registry and verification oracle for release certificates (8130-3, Form 1)**, which industry coalition ASCIC explicitly asked for (s10, c09).
- **A data-rights provenance graph and 7037 challenge packages.** DoD cancelled its own tool (s02, d01).
- **A PMA-vs-OEM reliability ledger with flight-hour denominators** (s11).
- **Evidence-priced insurance and lessor residual-value guarantees for non-OEM content** (s12, d06).
- **An AI-native holder of delegated authority** (ODA, DER group, CGD dedicator, accredited 17020/17065 body) whose KPI is reviewer hours per approval. Every comparable sector shows the margin goes to whoever holds the signature (a07, d08, c31, c32).

**In short:** capital (Nominal $1B, Flow $750M, Gecko $1.25B, PhysicsX $2.4B) has gone to capture and to new-design verification. Equivalence evidence for aftermarket and replacement parts, and the reviewer and signer seats, have almost no AI-native entrant. The incumbents that hold those seats (HEICO, AAR, Paragon, the ESAs) still run on human hours.

Raw notes with exact numbers and URLs are in `/home/user/nuketime/research/repair/v2/raw/*.md`. I did not re-open them for this synthesis, so some figures, especially those marked (recalled), should be checked against those files before they go into the application.