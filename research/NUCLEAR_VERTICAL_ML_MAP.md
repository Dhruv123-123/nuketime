# The nuclear vertical, step by step: where models and software change the outcome

Fifty-nine steps from regional targeting to decommissioning and safeguards, each with what happens today, the real
bottleneck, what data exist, who is already applying software or machine learning, the gap that remains, the size
of the prize, and a verdict. Built from six parallel research streams (about 300 sources, listed in
`vertical_map_sources.md`) on 2026-09-29, then synthesised. Verdicts: **Exponential** means a model could change
the outcome by ten times or more (cost, time, recovery, risk); **Strong** three times; **Incremental** under two;
**Already commercial** means products exist and the remaining value is as a feed into other steps.

Count: 19 exponential, 11 strong, 28 incremental, 1 already commercial.

## Six theses that fall out of the map

**Documents are the bottleneck, not physics.** Across licensing, criticality evaluations, fuel-qualification topical reports, QA records, permitting and commissioning, the industry's binding constraint is producing and reviewing consistent documents. The physics codes are fast enough. The highest-leverage artefact anyone could build is a machine-readable safety case shared by vendor, constructor and regulator; every exponential item in stages B, C and F depends on it, and the NRC's own adoption of language models is the fastest-moving piece in the whole vertical.

**Scarce test time wants Bayesian design of experiments.** Irradiation slots, hot cells, criticality benchmarks, flawed NDE specimens and evaluator hours are the physical scarcities. The pattern that beats them is the same everywhere: a calibrated surrogate with honest uncertainty, and active learning that chooses the few experiments that shrink the uncertainty that matters. LANL's PARADIGM did it for nuclear data; nobody has productised it for fuels, packages or repositories.

**Closed loops that nobody closes.** Drill-hole selection, ISR well control, TRISO inspection, outage emergent work, condition-based maintenance and decommissioning characterise-cut-sort all have published models and no product that acts on them. In each case the model exists and the actuator is missing: the tool that changes the next decision.

**The data map is bimodal.** The vertical is fully public and machine-readable at both ends (geoscience, ADAMS, ICSBEP and EXFOR, NEPA, DOE cleanup records) and closed in the middle (enrichment, fabrication, plant historians, EPC schedules). Startups win where data are public or the customer owns them and buys tools; the middle belongs to incumbents and national laboratories.

**Regulatory acceptance of uncertainty-quantified ML is the meta-gate.** Every exponential item that touches a safety basis (thermal-hydraulic closures, fuel surrogates, criticality, repository assessment, autonomy) waits on the same thing: a framework under which a regulator credits a learned model with calibrated uncertainty. Whoever gets the first such credit sets the template for the rest.

**The physical world stays physical.** Forgings, acid, centrifuges, test reactors and concrete are not software problems. Software's yield there is availability and yield, 5 to 15 % at a sold-out plant, which is real money but not a change of kind.

## The twenty opportunities, ranked

Ranked by the product of prize, data availability and the absence of anyone already doing it, tempered by difficulty.

1. **The machine-readable safety case** (C5, F5). Applicant-side consistency checking, RAI prediction and pre-drafted safety evaluations today; a claim-to-evidence graph standard co-designed with the NRC tomorrow. The regulator has already gone from four years to nine months on one review type; the applicant side has not caught up. Buyers: Reactor vendors, utilities, DOE; fee hours alone about $1 B per year.

2. **Fuel qualification by design of experiments** (B7). Bayesian-calibrated fuel-performance surrogates choose the few irradiation capsules that shrink licensing uncertainty most, and automated post-irradiation examination turns months into days. Test-reactor and hot-cell time is the hard limit on every advanced fuel. Buyers: DOE, fuel vendors (X-energy, BWXT, Oklo, TerraPower, Framatome, Westinghouse).

3. **Closed-loop in-situ recovery** (A4, A3). Model-predictive control of acid dosing and flow per well on a calibrated reactive-transport surrogate, plus restoration forecasting. 56 % of world uranium runs through ISR and the acid shortage cost about $1 B of output in a year. Buyers: Kazatomprom, Uranium One, Cameco (Inkai), enCore, Ur-Energy, Boss.

4. **Autonomous decommissioning** (E7). Probabilistic 3D activity maps that update with every measurement, characterise-cut-sort loops, and cost models trained on project histories. The single largest pool of money in the industry (about $1 T of liabilities) with 30 to 50 % cost uncertainty. Buyers: DOE EM, NDA and Sellafield, TEPCO, EDF.

5. **The construction digital thread** (C7, C8, F2). Requirements-to-as-built traceability that closes ITAAC and QA automatically, delay forecasting from real progress, and automated NDE records. Rework and paper, not concrete, drove Vogtle. Palantir's NOS is the first attempt; nobody owns the QA and supplier-certificate layer. Buyers: EPCs, vendors, owners of multi-unit programmes.

6. **Outage emergent-work prediction** (D4, D6). Continuously re-optimised probabilistic outage schedules fed by condition-report text. The gap between the average 33-day outage and the best 21-day one is $8 to 12 M per plant-year, and the data already sit in every plant's work-management system. Buyers: US and European fleet operators.

7. **Condition-based maintenance that changes surveillance intervals** (D3). Predictive maintenance is pre-deployment everywhere; the prize is the risk-informed basis to defer time-based surveillances. Worth 0.5 to 1.5 capacity-factor points and 10 to 20 % of maintenance labour. Buyers: Fleet operators, EPRI.

8. **100 % in-line TRISO inspection** (B5). Line-rate X-ray and optical inspection of every particle with ML classification and statistical release replacing destructive sampling. QA dominates the cost of the fuel every HTGR and FHR depends on. Buyers: X-energy, BWXT, Kairos, Standard Nuclear.

9. **Auto-criticality-safety and ML nuclear data** (B3, B8). LLM-drafted criticality safety evaluations grounded in precedent, automated SCALE sweeps and k-eff surrogates; upstream, ML-assisted cross-section evaluation with real covariances. The scarcest skill in the fuel cycle, on the HALEU critical path, with fully public data. Buyers: Package vendors, fuel fabricators, DOE, national laboratories.

10. **Closed-loop exploration** (A1, A2). From prospectivity maps to sequential drill-hole selection under a budget with real-time downhole updates. The natural next step for an ML prospecting company, and the step that makes the map change what gets drilled. Buyers: Juniors and majors in the Athabasca and beyond.

11. **Cleanup mission optimisation** (E5). Active-learning glass formulation is proven at PNNL; the unbuilt layer is tank-to-glass-to-canister optimisation of a 40-year mission and ML sorting at scale. Hanford and Sellafield spend tens of billions. Buyers: DOE EM, NDA.

12. **Reference-class cost forecasting** (F1). A Bayesian model with design maturity, first-of-a-kind status and contract form as features, and an estimate-audit LLM that flags placement rates the industry has never achieved. Cost of capital is 40 to 60 % of nuclear LCOE and it is priced off these estimates. Buyers: Owners, lenders, rating agencies, DOE Loan Programs Office.

13. **The certified microreactor autonomy stack** (D1, F9). Fault detection, control and safeguards reusable across a fleet. Existential for sub-10 MWe economics and required by NASA's lunar reactor; the NRC framework does not exist, which is the whole difficulty. Buyers: Microreactor vendors, DoD, NASA.

14. **Fusion control and inverse design** (F8). Already pursued by DeepMind, CFS and Proxima; the open gaps are sim-to-real transfer for first-of-a-kind machines and design that couples plasma, coils, neutronics and cost. Buyers: Fusion companies.

15. **Isotope logistics optimiser** (E10). A stochastic optimiser over reactor schedules, target chemistry, processing, air freight and patient scheduling, with a shared outage-risk model across six ageing reactors. A $7 to 8 B market losing product to decay every day. Buyers: Isotope producers, radiopharma, hospital networks.

16. **Design optimisation with cost and licensability in the objective** (C3, C4). Generative design that co-optimises manufacturability, PRA and cost, so the design is complete before concrete. Needs the cost data nobody shares. Buyers: SMR and microreactor vendors.

17. **Regulator-credible surrogates for the back end** (E6, E1). ML surrogates with calibrated uncertainty for repository performance assessment and spent-fuel characterisation. Large leverage, politically paced. Buyers: Waste management organisations.

18. **Reload optimisation in an approved methodology** (D2). Reinforcement learning already beats legacy search; the work is getting it into a licensed method with uncertainty-aware margins. Buyers: Utilities, Studsvik, Westinghouse, Framatome.

19. **Commissioning and ITAAC automation** (C9). LLM-generated test procedures and automatic evidence assembly for the most expensive months of a build. Nobody is working on it. Buyers: Vendors, EPCs, owners.

20. **Laser enrichment control** (B2). A high-dimensional control problem where learning control could move cost per SWU; invisible from outside GLE and LIS until about 2030. Buyers: GLE, LIS Technologies.

## The map

### A. Front end: finding and producing uranium

#### A1 Regional targeting and prospect-scale exploration  —  Exponential · data open · difficulty high

- **Today.** Airborne EM, gravity, magnetotellurics, radiometrics, boulder and soil geochemistry, then diamond drilling to the unconformity at C$500 to 700 per metre. Target generation is expert-driven 3D conductivity and fault modelling. 60-plus Athabasca juniors; Cameco, Orano, Kazatomprom, CGN.
- **Bottleneck.** Cost per economic discovery under 500 to 1,000 m of cover, and very few positive labels (a few dozen Tier-1 unconformity deposits worldwide).
- **Data.** Provincial and federal geophysics, assessment files, SEDAR+ reports; Genesis AI's GeoHarmony aggregated 100,000 km2 of Athabasca public data. Drill assays and logs are proprietary.
- **Who is on it.** KoBold Metals ($537 M Series C, 2025; not uranium), Genesis AI (GeoHarmony, 2024), Ideon (borehole muon tomography with Orano), Fleet Space; academic prospectivity models at Husab, sandstone ResNets, physics-informed Korzhinskii-Net (2026).
- **Gap.** No closed loop for uranium: basin prospectivity model, then sequential drill-hole selection under a drill budget, then real-time update from downhole gamma and prompt-fission-neutron logs. Academic work is retrospective; commercial tools stop at data aggregation.
- **Prize.** Exploration spend about $0.9 B per year; halving cost per discovery is hundreds of $M per year and one Tier-1 discovery is a multi-billion asset (NexGen Arrow about C$12 B EV).
- **Verdict.** Exponential only if the model changes which holes get drilled, not just map colours. Label scarcity is the wall; physics-informed and transfer methods are the way through.

#### A2 Resource estimation and reporting  —  Incremental · data mixed · difficulty medium

- **Today.** Qualified persons build domains in Leapfrog, Datamine, Vulcan; ordinary and indicator kriging; NI 43-101, JORC, S-K 1300. ISR sandstone grade comes mostly from gamma logs corrected for radiometric disequilibrium, or prompt-fission-neutron probes.
- **Bottleneck.** Grade-thickness accuracy from logs (disequilibrium, spectral drift) and months per update; classification is judgment; reconciliation errors feed ISR ramp-up shortfalls.
- **Data.** Drill databases proprietary; hundreds of technical reports and US ISR applications with logs are public.
- **Who is on it.** Generic mining ML for categorization and domaining (Natural Resources Research 2021 to 2025); uranium-specific neural spectral-gamma quantification (2024, 87 to 93 % accuracy); vendors adding ML domaining.
- **Gap.** Reporting codes give no pathway for ML estimates (QP liability); no published disequilibrium-aware log-to-recoverable-uranium model for pattern-level ISR forecasting.
- **Prize.** 10 to 20 % grade-thickness error on ISR patterns; weeks of QP time.
- **Verdict.** Accuracy gains are real; regulation and liability block adoption.

#### A3 Mine method selection, ISR well-field design, mine planning  —  Strong · data closed · difficulty high

- **Today.** ISR pattern geometry, injector-to-extractor ratios and block sequencing done in-house with hydrogeologic models; Deswik, Vulcan, Minemax for conventional mines; Kazatomprom's Digital Mine is monitoring and ERP, not optimisation.
- **Bottleneck.** Well-field NPV under aquifer heterogeneity; drilling-rig logistics; acid versus alkaline method decided by column tests rather than predicted from logs.
- **Data.** Operator data proprietary; a few published industrial cases (Katco/HYTEC, 2,394 wells) and NRC applications.
- **Who is on it.** Deep-learning proxy plus clustering of geological realizations for ISL design, +15 % NPV (Water Resources Research 2026); multi-objective ISL design under uncertainty (Journal of Hydrology 2024); Orano and MINES Paris HYTEC reactive transport.
- **Gap.** Surrogate-model well-field optimisation exists in papers; no commercial well-field optimiser product; operators design by rules of thumb.
- **Prize.** 10 to 20 % NPV per well-field; 20 to 30 % fewer wells at $100 to 300 k each.
- **Verdict.** Productisable now; reactive-transport calibration and sparse logs are the technical risk.

#### A4 In-situ recovery operation: lixiviant, flow, restoration  —  Exponential · data closed · difficulty high

- **Today.** Kazakhstan uses about 40 kg of sulphuric acid per kg of uranium (Beverley 7.7); recoveries 70 to 90 % acid, 60 to 70 % alkaline; per-well flow, pH, Eh and uranium in solution logged at high frequency. Restoration runs about four pore volumes over two years and no US ISR aquifer has returned to baseline (USGS 2009).
- **Bottleneck.** Acid is the binding constraint: Kazatomprom's 2025 guidance fell from about 80 to 65 to 69 Mlb for lack of acid, about $1 B of revenue. Peak-lag between injection and recovery; restoration liabilities.
- **Data.** Entirely proprietary per-well time series; restoration data partly public through the NRC.
- **Who is on it.** Physics-guided multi-well forecasting of pregnant-solution uranium (2026); reactive-transport remediation toolboxes (2024); CatBoost groundwater uranium; Kazatomprom drones for well-field compliance. No operator publishes closed-loop control.
- **Gap.** Per-well adaptive acid dosing and flow control by model-predictive control on a calibrated surrogate, plus restoration forecasting. The largest un-served software problem in the front end: 56 % of world supply runs through ISR.
- **Prize.** +5 recovery points on about 80 Mlb per year of Kazakh output is about 4 Mlb (about $350 M per year); acid-limited volume lost in 2024 to 2025 exceeded $1 B per year.
- **Verdict.** Heterogeneous reactive chemistry with few sensors between wells; but the data are owned by a handful of operators who would buy the tool.

#### A5 Conventional mining, milling, leaching, ion exchange and solvent extraction  —  Incremental · data closed · difficulty low

- **Today.** Key Lake runs about 99 % recovery and set a record 20.3 Mlb in 2024 after automation upgrades; Kazakh plants use resin sorption then solvent extraction; distributed control, not ML.
- **Bottleneck.** Not recovery. Reagent, energy, throughput stability, resin and elution efficiency at low solution grades.
- **Data.** Historian data proprietary; nothing public at tag level.
- **Who is on it.** Nearly nothing published for front-end mills; adjacent neural model-predictive control of uranium extraction in reprocessing (2024).
- **Gap.** Soft sensors and model-predictive control for ion-exchange and solvent-extraction trains; ore-blend-aware leach setpoints.
- **Prize.** Low single-digit percent of opex and throughput on about $10 B per year of product.
- **Verdict.** Ordinary process-industry ML; data access is the only obstacle.

#### A6 Tailings, mine water, radon and environmental monitoring  —  Incremental · data mixed · difficulty medium

- **Today.** Long-lived liabilities (Ranger rehabilitation A$2.3 B; DOE Legacy Management cells); periodic well sampling plus geochemical models.
- **Bottleneck.** Sparse, slow data; regulators want mechanistic models.
- **Data.** DOE Legacy Management, NRC and Australian supervising-scientist data partly public; satellite SAR and optical public.
- **Who is on it.** ML plus spaceborne SAR for 3D soil moisture in a disposal cell (2024); tailings-pond early-warning networks (2020 to 2022); transformer water-quality models (2026).
- **Gap.** ML as an anomaly and early-warning layer over mechanistic models; not a replacement.
- **Prize.** Liability reduction on multi-billion closure books; avoided failures.
- **Verdict.** Except catastrophic-failure avoidance, which is high value but rare.

#### A7 Permitting, community and regulatory process for uranium recovery  —  Exponential · data open · difficulty low

- **Today.** About five years from resource to production in the US; Dewey-Burdock was NRC-licensed in 2014, EPA-permitted in 2020, and still in appeals in 2025. The May 2025 executive order set 18-month NRC decision targets.
- **Bottleneck.** Document volume and RAI loops on the applicant side; litigation and tribal consultation, which is not a document problem.
- **Data.** NRC ADAMS and the NEPA corpus (PNNL NEPATEC 2.0: 28,212 documents, 4.8 M pages).
- **Who is on it.** NRC itself uses Claude, Azure OpenAI and Gemini via GSA OneGov and an internal SimplifAI; one licensing type went from four years to a nine-month first round (NRC CDO, June 2026). PNNL PermitAI; INL, Microsoft and Everstar document generation. None names uranium recovery.
- **Gap.** Uranium-recovery-specific applicant tooling: environmental-report drafting, RAI prediction, baseline-data QA.
- **Prize.** One to two years off a $200 to 500 M project in carrying cost plus option value.
- **Verdict.** Exponential in time terms if applicant-side tooling matches the regulator's; politics caps it.

#### A8 Marketing, price, inventory and logistics of U3O8  —  Incremental · data closed · difficulty low

- **Today.** Prices set by two private reporters from broker-reported deals; 2025 US deliveries 46.9 Mlb, 87 % term; the Trans-Caspian corridor now carries about half of Kazakh western deliveries.
- **Bottleneck.** Thin, opaque, bilateral market; monthly paywalled data.
- **Data.** UxC and TradeTech paid; EIA and Euratom aggregates public; contract books private.
- **Who is on it.** Academic neural price studies only; UxC's indicator is expert scoring; traders use spreadsheets.
- **Gap.** Utility procurement and portfolio optimisation; freight and corridor risk modelling.
- **Prize.** Basis points on about $10 B per year of trade.
- **Verdict.** Data-bound; a hedge-fund style edge, not an industry change.

#### A9 Secondary supply: tails re-enrichment, reprocessed uranium, phosphate and seawater  —  Strong · data mixed · difficulty very high

- **Today.** Underfeeding and tails re-enrichment at Urenco; PhosEnergy demonstrated under $18 per lb from phosphate but no commercial plant; DOE cut seawater-adsorbent cost three to four times; CNNC runs a Hainan test platform targeting tonne scale by 2035.
- **Bottleneck.** Adsorbent discovery is data-starved (hundreds of samples); tails economics are SWU-price driven.
- **Data.** U-Predict v1.0 (2025): 220 adsorbents, 54 descriptors, test R2 0.75.
- **Who is on it.** Chinese and DOE adsorbent groups; ML materials discovery papers 2025.
- **Gap.** Active-learning materials discovery loop for adsorbents; nothing for tails or reprocessed uranium beyond spreadsheets.
- **Prize.** Seawater uranium below $100 per kg would be unlimited supply, on a 2035 to 2050 horizon.
- **Verdict.** Exponential ceiling, long horizon, tiny datasets.

### B. Conversion, enrichment, fuel

#### B1 Conversion and deconversion  —  Incremental · data closed · difficulty medium

- **Today.** Four Western UF6 plants (Metropolis, Port Hope, Malvesi and Tricastin) sold out through 2028; DUF6 deconversion at Paducah and Portsmouth with an 800,000 t backlog and 18 to 30 years to clear; six DOE HALEU deconversion contractors with no operating commercial capacity.
- **Bottleneck.** Physical capacity and fluorine chemistry, not information; old plants where availability is the lever.
- **Data.** DCS historians inside Honeywell, Cameco and Orano; none public.
- **Who is on it.** No public ML or digital-twin work found for conversion or deconversion.
- **Gap.** Predictive maintenance and advanced process control on fluorination and distillation.
- **Prize.** 5 to 15 % availability at a sold-out plant, tens of $M per year per plant.
- **Verdict.** Ordinary chemical-plant Industry 4.0 with three incumbents and safety-case inertia.

#### B2 Enrichment: cascade operation, HALEU, laser  —  Incremental · data closed · difficulty very high

- **Today.** About 63 M SWU per year (Rosatom 27, Urenco 18, CNNC 10, Orano 7.5); Centrus HALEU demo done, $900 M awards to Centrus, General Matter and Orano; GLE laser plant licence application complete (2025), production about 2030; LIS Technologies $1 B laser plant announced.
- **Bottleneck.** Capital, centrifuge manufacturing throughput and five- to eight-year licensing lead time; performance data classified and export-controlled.
- **Data.** Closed. Public work is simulation: metaheuristic cascade layout (2023 to 2024), ORNL and PNNL safeguards-side detection.
- **Who is on it.** Operators publish nothing on AI. Academic cascade optimisation saves about 1 % of machines.
- **Gap.** (a) Tails-assay and feed optimisation against live U3O8 and SWU prices, a multi-million-dollar per plant problem done in spreadsheets; (b) laser enrichment is a high-dimensional control problem (laser tuning, gas dynamics, separation-factor stability) where learning control could move cost per SWU; (c) centrifuge fleet health monitoring across tens of thousands of machines.
- **Prize.** 1 to 3 % of a $5 to 14 B per year market for centrifuges; unknown and possibly large for laser.
- **Verdict.** Incremental for centrifuges; the laser lane is the one to watch and nobody outside GLE and LIS can see it.

#### B3 Transport packages, cylinder tracking, criticality safety evaluations  —  Exponential · data open · difficulty medium

- **Today.** Above 5 % enrichment the water-exclusion exemption disappears and every package must show subcriticality flooded. HALEU packages: Orano DN30-X (2023), Versa-Pac, NAC OPTIMUS-L; Centrus lost its 900 kg delivery in 2024 for lack of cylinders. Every package and fissile operation needs a criticality safety evaluation by a qualified engineer validated against ICSBEP benchmarks; NRC package review takes one to two years.
- **Bottleneck.** The scarcest skill in the fuel cycle (NCS engineers, ageing workforce) and missing HALEU benchmark data; criticality validation, not shielding, is the HALEU schedule-critical path against 137 t (2030) to 501 t (2035) of demand.
- **Data.** ICSBEP handbook public; SCALE and MCNP widely licensed; 53 M pages of ADAMS.
- **Who is on it.** Atomic Canyon (document search on ADAMS, ORNL partnership 2025); Nuclearn (regulatory documents); nobody does the criticality-specific piece.
- **Gap.** An auto-CSE stack: LLM drafting grounded in ADAMS precedents, automated SCALE parametric sweeps, ML surrogates for k-eff sensitivity and validation bias, humans as signatories.
- **Prize.** Two to five times faster package and facility licensing on a multi-hundred-million-dollar HALEU logistics chain; the difference between advanced-reactor fuel in 2029 or 2032.
- **Verdict.** Open codes and benchmarks; regulator acceptance of AI-produced safety analysis is the gate. Cylinder tracking itself is done (RFID).

#### B4 LWR fuel fabrication  —  Incremental · data closed · difficulty medium

- **Today.** Framatome, GNF, Westinghouse (Columbia, $131 M automation, LEU+ line 2028), TVEL, ENUSA, KEPCO NF, CNNC; $5 to 6 B per year. ENUSA runs automatic pellet inspection with a deep-network defect classifier; structured-light deep learning for pellet cracks (2025).
- **Bottleneck.** Yield and scrap from powder-lot variability, press and sinter control, grinding, weld and grid defects; NRC-licensed change control freezes processes; LEU+ requires re-doing criticality limits on every vessel.
- **Data.** Rich per-plant SPC data locked behind NQA-1 change control; no public datasets.
- **Who is on it.** Incumbents' own vision QC; nothing published on ML sinter-furnace control or powder-lot-to-pellet property prediction.
- **Gap.** Process-model-plus-ML for sintering and powder chemistry; closed-loop grinding; faster ATF and LEU+ qualification runs.
- **Prize.** 10 to 30 % scrap reduction; 1 % yield on the sector is about $50 M per year.
- **Verdict.** Incumbents are solving vision QC themselves; commercial access is the barrier.

#### B5 Advanced fuel manufacturing: TRISO, metallic, MOX  —  Exponential · data mixed · difficulty high

- **Today.** X-energy TX-1 received the first Category II fuel licence in over 50 years (Feb 2026); BWXT makes TRISO for Pele; Kairos replicates LANL's pebble line. A core holds billions of particles; QA is statistical sampling with automated optical microscopy and destructive burn-leach tests on about 1,000-particle samples.
- **Bottleneck.** Cost per kilogram of qualified fuel is dominated by QA sampling and lot rejection, and qualification is tied to a fixed process envelope so any change re-opens it.
- **Data.** AGR-1 to AGR-7 characterisation data largely public; production-line imagery proprietary.
- **Who is on it.** ORNL ML segmentation of SiC grain boundaries (TopFuel 2025); an early in-line NDE project (2003 to 2006). Nobody has fielded line-rate 100 % inspection.
- **Gap.** 100 % in-line inspection (X-ray, optical, electromagnetic at line rate) with ML defect classification and statistical release replacing destructive sampling. Metallic casting (Oklo, TerraPower) has no public ML; MOX gloveboxes are already automated.
- **Prize.** TRISO costs thousands of dollars per kilogram with QA a large fraction; halving QA changes HTGR and FHR fuel economics and speeds re-qualification.
- **Verdict.** Needs particle-level ground truth and regulator acceptance of ML-based release; the physics of inspection is solved.

#### B6 Fuel QA, nondestructive assay, enrichment verification  —  Incremental · data mixed · difficulty medium

- **Today.** Rod-level passive gamma, X-ray welds, ultrasonic end plugs; IAEA and LANL NDA instruments; microcalorimeter gamma; ML radionuclide identification is a reviewed field (2025).
- **Bottleneck.** Throughput and false rejects; LEU+ and HALEU need re-calibrated NDA and new acceptance criteria.
- **Data.** Instrument data proprietary; spectra are simulable, so synthetic-to-real transfer works.
- **Who is on it.** LANL, ORNL, PNNL, ENUSA, Chinese groups; detector layouts now designed for ML suitability (2024).
- **Gap.** Fusion of gamma, neutron, X-ray and ultrasonic data into one automated release decision.
- **Prize.** Tens of $M per year across the industry unless coupled to TRISO.
- **Verdict.** Mature instruments; ML improves throughput.

#### B7 New-fuel qualification: irradiation, post-irradiation examination, performance codes  —  Exponential · data mixed · difficulty high

- **Today.** NRC NUREG-2246 framework (2022); accelerated qualification with MiniFuel in HFIR and FAST capsules in ATR; NRC uses FAST for confirmatory analysis; BISON (INL) is the multi-fuel code but not formally accepted for advanced fuels. ORNL calls the shrinking test-reactor fleet a major bottleneck; hot-cell PIE is the other queue.
- **Bottleneck.** Irradiation slots and hot-cell time, then regulator willingness to accept model-based extrapolation.
- **Data.** AGR, ATF, Halden and FUMEX datasets largely public but fragmented; INL's NSUF database.
- **Who is on it.** ML surrogates of FRAPCON and BISON at 1,000x speed (2020 to 2022); INL multifidelity active learning for TRISO failure probability (2023); INL ML segmentation of fission-gas bubbles and dislocation loops (2023 to 2025); Bayesian UQ for digital twins.
- **Gap.** (i) Bayesian-calibrated BISON surrogate plus active-learning design of irradiation tests, choosing the few capsules that shrink licensing uncertainty most; (ii) automated PIE pipelines turning months of microscopy into days; (iii) LLM-assisted topical reports against NUREG-2246.
- **Prize.** Each year cut from HALEU, TRISO or metallic fuel qualification unlocks billions of reactor deployment.
- **Verdict.** The highest-leverage software lane in the middle of the cycle; NRC already has the framework to hang it on.

#### B8 Nuclear data, cross-section evaluation and criticality benchmarks  —  Exponential · data open · difficulty medium

- **Today.** ENDF/B-VIII.1 (2024 to 2025), JEFF-4, TENDL; expert evaluation on a roughly seven-year cadence with a few dozen evaluators worldwide; validation on ICSBEP; adjustment by TSURFER and Whisper.
- **Bottleneck.** Evaluator headcount and sparse intermediate-spectrum benchmarks that matter for HALEU; nuclear-data uncertainty flows straight into criticality margins, package capacity and fuel-cycle economics.
- **Data.** EXFOR, ENDF and ICSBEP are public and machine-readable: the most data-open step in the vertical.
- **Who is on it.** LANL random-forest validation that found a fluorine cross-section problem (2020); PARADIGM ML experiment selection (Physical Review X, 2025); Berkeley NucML; graph networks across the chart (2024); Bayesian model averaging; k-eff surrogates at 50 to 70 pcm.
- **Gap.** End-to-end ML-assisted evaluation (EXFOR curation, model fitting, covariance, integral validation) with formal UQ that libraries adopt; cheap k-eff and sensitivity surrogates inside criticality workflows.
- **Prize.** Indirect but large: tighter covariances shrink HALEU margins and lift package and plant throughput; library cycle from about seven years to two.
- **Verdict.** Exponential in leverage, slow in institutional adoption (CSEWG, NEA).

### C. Reactor design, licensing, construction

#### C1 Core design and neutronics  —  Incremental · data mixed · difficulty low

- **Today.** OpenMC, Shift, MCNP, Serpent, CASMO/SIMULATE, VERA; ORNL ExaSMR reached 100x on Frontier; loading patterns by simulated annealing and genetic search at vendors.
- **Bottleneck.** Not compute for LWRs. For advanced reactors: validation data, nuclear-data uncertainty, and no accepted path for ML surrogates into safety-basis calculations.
- **Data.** Unlimited synthetic; sparse experimental for non-LWR designs.
- **Who is on it.** Deep RL for PWR reload beats legacy search (Nuclear Science and Engineering 2025; MIT NEORL); ReactorFold sequence-model assembly design (2025); MIT reduced-order full-core models.
- **Gap.** Generative design for advanced cores; multi-objective reload with uncertainty-aware margin recovery.
- **Prize.** $1 to 5 M per cycle per plant in fuel and cycle length; design iterations from months to days for new concepts.
- **Verdict.** Mature and largely solved for LWRs; medium for advanced designs.

#### C2 Thermal-hydraulics and multiphysics  —  Incremental · data closed · difficulty high

- **Today.** RELAP5-3D, TRACE, SAM; CFD; MOOSE coupling. Closures are decades-old empirical correlations.
- **Bottleneck.** Scarce, old, proprietary validation data for closures; regulatory evaluation-model pedigree (10 CFR 50.46, CSAU) that ML closures lack.
- **Data.** Test-loop data from the 1970s to 1990s, much proprietary.
- **Who is on it.** Physics-enhanced ML for critical heat flux with UQ (2025); neural-operator surrogates for helical steam generators; graph-neural-ODE digital twins (2026); INL RAVEN hybrid surrogates.
- **Gap.** ML closures that recover conservative margins, paired with a regulatory credibility framework for ML evaluation models.
- **Prize.** 5 to 10 % capital reduction on some safety systems; uprates.
- **Verdict.** Exponential only if the credibility framework exists first.

#### C3 Integrated design optimisation of SMRs and microreactors  —  Exponential · data closed · difficulty high

- **Today.** Manual, sequential, discipline-siloed design at vendors; MOOSE multiphysics; Aalo and Microsoft AI design collaboration (2025); Blue Energy ($380 M, shipyard prefabrication); no open, trusted bottom-up cost model.
- **Bottleneck.** Co-optimising design with manufacturability, licensability and cost under an incomplete cost model; the failure mode that sank Vogtle was design incomplete at construction start.
- **Data.** Cost data proprietary (EPRI tool); irradiation and corrosion data for advanced coolants limited.
- **Who is on it.** MIT, INL, ANL; startups.
- **Gap.** Generative design with an integrated cost, licensing and constructability objective.
- **Prize.** Moving first-of-a-kind cost from about $10,000 toward $5,000 per kW is tens of billions across a 400 GW build-out.
- **Verdict.** The missing ingredient is cost and manufacturing data, not algorithms.

#### C4 Probabilistic risk assessment and safety analysis  —  Strong · data mixed · difficulty medium

- **Today.** Static fault and event trees (SAPHIRE, CAFTA); dynamic PRA with RAVEN; severe accident with MELCOR and MAAP; deep-learning surrogates from thousands of MELCOR runs (2024 to 2025).
- **Bottleneck.** PRA is bespoke and manual: plant models, success criteria, human reliability; advanced-reactor licensing makes it central so cost is rising.
- **Data.** Rich synthetic; curated real failure data (INL IRIS, NRC event reports).
- **Who is on it.** Sandia next-generation risk-informed assessment; INL LWRS.
- **Gap.** LLM-assisted PRA model construction from P&IDs and FMEAs plus surrogate-driven dynamic PRA during design rather than after.
- **Prize.** Half of a $5 to 20 M PRA effort; risk-informed design iteration.
- **Verdict.** A multiplier for design optimisation and licensing.

#### C5 Licensing engineering and regulatory review  —  Exponential · data open · difficulty medium

- **Today.** NuScale's design application was 12,000 pages with 2 M pages of audit material, over $500 M and 2 M labour hours, 3.5 years of review. Kairos Hermes 2 reviewed in 10 months with 60 % fewer resources; 18-month construction-permit decisions mandated (EO 14300, May 2025). NRC uses Claude, Azure OpenAI and Gemini and reports one review type from four years to nine months; DOE and Everstar's Gordian generated a 208-page FSAR chapter in a day at Revision-0 quality; ORNL and Atomic Canyon's FERMI models trained on 53 M ADAMS pages; INL and Microsoft generate safety-analysis sections; Nuclearn screens 50.59 changes.
- **Bottleneck.** RAI loops caused by internal inconsistencies and missing cross-references; staff hours on precedent search and safety-evaluation drafting; no standard machine-readable application; no framework for crediting ML-generated analyses.
- **Data.** ADAMS, every prior safety evaluation, RAI and regulatory guide: arguably the best-labelled regulatory corpus in any industry.
- **Who is on it.** NRC, DOE, INL, ORNL, Atomic Canyon, Nuclearn, Everstar, Inductive, Westinghouse bertha.
- **Gap.** Applicant-side consistency checker, RAI predictor and safety-evaluation pre-drafter; above that, a machine-readable application standard co-designed with the NRC so applicant and regulator tools operate on one structured safety case (a claim-to-evidence graph, not PDFs).
- **Prize.** $50 to 150 M per year of carrying cost per GW-scale project; 6 to 18 months per project; fee hours alone are about $1 B per year.
- **Verdict.** The one step where data, motivation, executive mandate and demonstrated wins coincide. Institutional, not technical, difficulty.

#### C6 Siting and environmental review  —  Incremental · data open · difficulty low

- **Today.** GIS multi-criteria screening; seismic hazard by consultants; NEPA documents by contractors; NRC generic EIS and proposed categorical exclusion for microreactors (2026); PNNL PermitAI in beta.
- **Bottleneck.** Regulatory scope (now shrinking) more than analysis; site characterisation is physical and slow.
- **Data.** NEPA corpus, hazard maps, load and water data public.
- **Who is on it.** PNNL, NRC; ML seismic fragility surrogates (2025).
- **Gap.** Siting optimisation combining interconnection queues, water, seismic and load; fragility surrogates.
- **Prize.** Modest; policy is deflating the workload faster than ML would.
- **Verdict.** Incremental.

#### C7 Construction planning, cost estimation and schedule  —  Exponential · data closed · difficulty high

- **Today.** Bechtel, Fluor, Hyundai E&C; Primavera; Palantir and The Nuclear Company's NOS ($100 M, Foundry: sensors to digital twin, LLM review of tens of thousands of documents, agents validating field records against requirements); Westinghouse and Google Cloud task-sequencing optimisation cut a $3.8 M room to $2.8 M.
- **Bottleneck.** Rework and field productivity driven by incomplete or changed design, QA documentation burden (every safety-related weld and pour has a paper trail), and the forging supply chain. Construction data have been paper; as-built, NDE and QA records are not linked to the design model.
- **Data.** Historically terrible; NOS is the first serious unified data spine.
- **Who is on it.** Palantir, Westinghouse, Bechtel, EPRI construction roadmap.
- **Gap.** Requirements-to-as-built traceability so ITAAC and QA closure is automatic; delay forecasting from real progress data; automatic NDE with digital records.
- **Prize.** Construction is 70 to 80 % of overnight cost; 20 to 30 % on a 400 GW build-out is hundreds of billions.
- **Verdict.** Exponential for the digital thread plus automated fabrication combination; incremental for scheduling algorithms alone.

#### C8 Fabrication, welding, NDE and modular assembly  —  Strong · data closed · difficulty medium

- **Today.** Sheffield Forgemasters local electron-beam welding of a full SMR vessel demonstrator in under 24 hours versus about a year; EPRI and BWXT heavy-section EBW from 2026; ORNL 3D-printed formwork for the Hermes bioshield (14 days); AI-assisted automated defect recognition in NDE field trials; robotic pipe welding.
- **Bottleneck.** Qualification of new processes and of automated NDE against ASME performance demonstrations; few qualified suppliers.
- **Data.** Flawed-specimen datasets small and proprietary (EPRI NDE Center).
- **Who is on it.** Sheffield Forgemasters, EPRI, BWXT, Kairos, ORNL, Novarc, Trueflaw.
- **Gap.** ML as primary NDE analyst with digital records; cross-vendor labelled datasets.
- **Prize.** 10 to 100x on specific tasks already shown by EBW and printed forms; software makes the records automatic.
- **Verdict.** Physical automation delivers the leap; software captures it.

#### C9 Commissioning and startup testing  —  Strong · data closed · difficulty medium

- **Today.** Regulatory Guide 1.68 test programmes; hundreds of ITAAC closure packages verified before fuel load; Vogtle 4 hot functional testing far faster than Vogtle 3 from learning; NuScale templated test instructions. Almost no ML.
- **Bottleneck.** Sequential test execution, procedure preparation, deviation resolution and evidence packaging; digital I&C validation.
- **Data.** Plant-specific.
- **Who is on it.** Nobody.
- **Gap.** LLM-generated test procedures from the design basis and automatic evidence assembly for ITAAC.
- **Prize.** The last schedule window is the most expensive: carrying cost of a nearly complete plant is over $100 M per month.
- **Verdict.** High leverage per dollar because nobody is working on it.

#### C10 Simulators and operator training  —  Incremental · data mixed · difficulty medium

- **Today.** Full-scope simulators from GSE, Western Services, L3Harris, CORYS at $10 to 30 M each over years; Nuclearn and GSE natural-language scenario authoring (2026); an LLM fine-tuned on DOE handbooks reached about 80 % on NRC operator exams (2026).
- **Bottleneck.** Manual simulator model development; strict fidelity standards; formal licensing exams.
- **Data.** Simulator data plentiful; exam banks controlled.
- **Who is on it.** Nuclearn, GSE, GE Vernova VR, Fortum VR.
- **Gap.** Automated simulator model generation from the design digital twin; adaptive tutoring tied to simulator telemetry.
- **Prize.** A three-year simulator effort cut to months; workforce ramp of tens of thousands of operators.
- **Verdict.** Incremental to medium; moving already.

### D. Operations and maintenance

#### D1 Control room operations, alarms, procedures, autonomy  —  Exponential · data mixed · difficulty very high

- **Today.** Licensed operators in largely analog control rooms; INL computer-based procedures in pilots; Argonne PRO-AID diagnosis with an LLM explainer (2024); INL remote autonomous power control of a research reactor by a reinforcement-learning agent (July 2026); NRC discussion papers on autonomous operation (2025) with no guidance yet.
- **Bottleneck.** Regulatory: no qualification path for AI touching safety-related decisions; no NRC position on reduced staffing for autonomous microreactors.
- **Data.** Simulator data plentiful; real transient data sparse.
- **Who is on it.** INL, ORNL, Argonne, GE Vernova (MARVEL), Oklo (Aurora at INL, 2028).
- **Gap.** A certified autonomy stack (fault detection, control, safeguards) reusable across microreactor fleets; explainable operator advisory in a licensed control room.
- **Prize.** For the current fleet under one capacity-factor point; for microreactors, staffing is the dominant O&M line, so autonomy is existential.
- **Verdict.** Exponential for small reactors only; the NRC framework does not exist.

#### D2 Cycle-specific core reload design and in-core fuel management  —  Strong · data open · difficulty high

- **Today.** Utility reactor-engineering groups with Studsvik CMS5 (over 200 reactors), Westinghouse, Framatome and GNF; engineer-driven heuristic search; Blue Wave AI Labs BWR tools at Constellation since 2022 caught miscalibrated detectors and project about $80 M over three years across 32 BWRs.
- **Bottleneck.** Licence-basis constraints (approved methods, margins), vendor-proprietary codes, conservative crud-induced power-shift margins.
- **Data.** Every cycle simulated and measured; excellent, but held by utilities and vendors.
- **Who is on it.** Blue Wave AI Labs, Westinghouse ACE, Framatome-funded RL at Michigan.
- **Gap.** RL and surrogate results are not in an NRC-approved methodology; multi-objective optimisation with uncertainty-aware margin recovery is unexploited.
- **Prize.** $0.5 to 2 M per plant-year certain; more if margin recovery enables uprates or 24-month cycles.
- **Verdict.** Technically mature, licensing-bound.

#### D3 Predictive maintenance and condition monitoring  —  Exponential · data closed · difficulty medium

- **Today.** Fleet monitoring centres (Duke with AVEVA PRiSM; Constellation, Southern) running statistical pattern recognition; handheld vibration routes; INL and PSEG risk-informed maintenance on circulating-water systems; EPRI Open Power AI Consortium (2025). A 2026 review calls all of it pre-deployment.
- **Bottleneck.** Sensor coverage, rare failure labels, and time-based work management fixed by regulation and habit; converting an insight into a deferred surveillance needs a risk-informed basis.
- **Data.** Plant historians, utility-owned, air-gapped.
- **Who is on it.** AVEVA, EPRI, INL LWRS, NRC research.
- **Gap.** Condition-based maintenance at fleet scale with surveillance-interval extension.
- **Prize.** 0.5 to 1.5 capacity-factor points plus 10 to 20 % of preventive-maintenance labour, $5 to 15 M per plant-year.
- **Verdict.** Exponential if it unlocks surveillance reform; blocked by data silos and cyber posture, not algorithms.

#### D4 Outage planning and execution  —  Exponential · data closed · difficulty medium

- **Today.** 20,000 to 25,000 tasks per refuelling outage in Primavera; industry average 33 to 34 days (2024), Constellation 21.5 days (2025), records of 16 to 18 days; INL LOGOS, DACKAR and RAVEN open tools; commercial outage-AI offerings.
- **Bottleneck.** The critical path is physical (vessel head, steam-generator eddy current, fuel moves) and governed by discovered work and craft availability; data site-siloed.
- **Data.** P6 histories and work orders exist at every site.
- **Who is on it.** INL, consultants, Outage AI vendors.
- **Gap.** Probabilistic continuously re-optimised schedules with emergent-work prediction from condition-report text; cross-fleet learning as software rather than consultants.
- **Prize.** The 12 to 16 day gap between average and best is $12 to 20 M per outage per unit, about $8 to 12 M per plant-year, 2 to 3 capacity-factor points: the largest near-term dollar pool in operations.
- **Verdict.** Organisational more than technical.

#### D5 In-service inspection and NDE interpretation  —  Incremental · data closed · difficulty medium

- **Today.** Steam-generator eddy current on the critical path, every dataset analysed by two qualified analysts; Westinghouse automated single-pass analysis claims 35 % schedule and 75 % analyst reduction; EPRI's first AI automated defect recognition for ultrasonic head-penetration exams matched qualified analysts in 2024 to 2025 trials.
- **Bottleneck.** Qualification against ASME Section XI performance demonstrations; small proprietary flawed-specimen datasets; shrinking analyst supply.
- **Data.** EPRI NDE Center holds the specimens.
- **Who is on it.** EPRI, Zetec, Westinghouse, Trueflaw, PNNL.
- **Gap.** ML as primary analyst; cross-vendor labelled data; extension to visual and robotic inspection.
- **Prize.** 0.5 to 2 outage days and $1 to 3 M per outage; more in avoided missed indications.
- **Verdict.** Technically easy, qualification slow.

#### D6 Corrective action programs and operating-experience text  —  Already commercial · data open · difficulty low

- **Today.** Thousands of condition reports per plant per year screened by committees; Nuclearn CapAI at over 65 reactors automating about 80 % of scoring; Westinghouse bertha; Atomic Canyon at Diablo Canyon.
- **Bottleneck.** Largely solved technically; adoption limited by on-premises cyber posture, procurement and conservatism.
- **Data.** Abundant, text-rich, decades deep, utility-owned.
- **Who is on it.** Nuclearn, Westinghouse, Atomic Canyon, EPRI, INL MIRACLE.
- **Gap.** Closed-loop learning: predicting equipment failures and outage emergent work from condition-report text; fleet-wide operating-experience mining.
- **Prize.** $1 to 3 M per plant-year direct; larger as an input to maintenance and outages.
- **Verdict.** Already commercial; the next value is as a feed into D3 and D4.

#### D7 Radiation protection and ALARA  —  Incremental · data closed · difficulty low

- **Today.** Point-kernel planning tools; Spot robots for surveys at Duke, OPG, Talen; digital dose tracking; NRC proposed Part 20 overhaul (2026).
- **Bottleneck.** Dose is a regulatory and workforce constraint more than a cost; source term is chemistry.
- **Data.** Plant survey maps and dose records.
- **Who is on it.** Boston Dynamics users, SCK-CEN, Cyclife.
- **Gap.** Robotic surveys trimming outage days; 3D dose twins.
- **Prize.** Under $1 M per plant-year.
- **Verdict.** Incremental.

#### D8 Chemistry control  —  Incremental · data closed · difficulty medium

- **Today.** EPRI chemistry guidelines; crud-induced power shift assessed with BOA conservatively; EPRI Smart Chemistry with online ion chromatography; ML crud-distribution and multiphysics crud models (2022 to 2025).
- **Bottleneck.** Sparse online sensors, few crud events to learn from, coupling to core design.
- **Data.** Grab samples; utility records.
- **Who is on it.** EPRI, Westinghouse, academic groups.
- **Gap.** Virtual sensing and crud-risk prediction coupled to reload design.
- **Prize.** Event-driven: a bad crud event forces derates worth over $10 M.
- **Verdict.** High variance, sensor-limited.

#### D9 Cyber security and digital I&C  —  Incremental · data closed · difficulty very high

- **Today.** Air-gapped deterministic architectures under 10 CFR 73.54; Constellation's Limerick $167 M digital safety-system upgrade took a 3.5-year NRC review (approved Jan 2026), the first large US retrofit.
- **Bottleneck.** Regulation and vendor qualification; cyber rules actively impede data egress for every other item in operations.
- **Data.** By design.
- **Who is on it.** Westinghouse, Xage, Purdue research.
- **Gap.** Enabling infrastructure rather than direct return.
- **Prize.** Obsolescence mitigation; unlocks everything else.
- **Verdict.** A blocker, not an opportunity.

#### D10 Grid interaction, flexibility and dispatch  —  Incremental · data open · difficulty low

- **Today.** US plants run baseload; Columbia load-follows for BPA; behind-the-meter data-centre co-location (Talen and AWS, FERC rejection then an $18 B grid-connected PPA); MILP unit-commitment and integrated-energy-system research.
- **Bottleneck.** Fuel and mechanical wear, technical specifications, market design; value comes from contracts.
- **Data.** ISO data public; PPA terms private.
- **Who is on it.** INL, academic dispatch work.
- **Gap.** Co-optimising outages, uprates and PPAs; not reactor control.
- **Prize.** Tens of $M per year for merchant plants, from contracts.
- **Verdict.** Not a software problem.

#### D11 Aging management and life extension  —  Incremental · data mixed · difficulty medium

- **Today.** Subsequent licence renewal to 80 years; RPV embrittlement at high fluence, IASCC, concrete, cables; ML embrittlement models with uncertainty aimed at 80 to 100 year decisions (2023); dielectric-spectroscopy cable NDE with ML (2025).
- **Bottleneck.** Sparse surveillance data; slow acceptance of new correlations; plant-specific data in paper.
- **Data.** Surveillance capsules, industry databases, licence-renewal dockets.
- **Who is on it.** INL LWRS, ORNL, PNNL, university groups, Atomic Canyon and Argonne for renewal documents.
- **Gap.** Document mining for renewal applications; uncertainty-quantified embrittlement models.
- **Prize.** Enabling 20 more years of a $500 M per year asset is huge; ML's marginal contribution is modest.
- **Verdict.** Incremental.

#### D12 Workforce, knowledge capture and training  —  Incremental · data mixed · difficulty low

- **Today.** LLM and retrieval assistants are the first real deployments (Atomic Canyon Neutron, Westinghouse bertha, Nuclearn); operator licensing remains simulator and exam based; the UK needs about 123,000 workers this decade.
- **Bottleneck.** Cyber-compliant deployment and trust; tacit knowledge lives in retiring people.
- **Data.** Plant document stores; DOE handbooks public.
- **Who is on it.** Atomic Canyon, Westinghouse, Nuclearn, EPRI, INPO and NEI fleet assistant NIVA (2026).
- **Gap.** Knowledge capture from retiring experts; adaptive tutoring; NRC-approved AI-generated exam banks.
- **Prize.** $1 to 3 M per plant-year; enabling for SMR fleets.
- **Verdict.** Incremental but critical for scale.

### E. Back end, waste, safeguards, decommissioning

#### E1 Spent fuel characterisation: burnup, decay heat, isotopics  —  Incremental · data mixed · difficulty medium

- **Today.** ORNL SCALE/ORIGEN and UNF-ST&DARDS with a unified database of every US assembly; NDA for safeguards; ML on Swedish Clab decay-heat measurements since 2020.
- **Bottleneck.** Licensing-grade uncertainty: decay-heat validation bias and high-burnup data scarcity flow into cask limits, transport thermal limits and repository spacing. Measured decay heat exists for a few hundred assemblies.
- **Data.** Simulated data unlimited; measured data scarce and partly proprietary.
- **Who is on it.** ORNL, IAEA working group, academic surrogates of ORIGEN (2023).
- **Gap.** Regulator-accepted ML surrogate with calibrated uncertainty; a Bayesian per-assembly digital passport fusing NDA, operator records and depletion. Advanced-reactor fuels have no measured basis at all.
- **Prize.** Tens of $M per year in fewer casks; the input to storage, transport, repository and safeguards.
- **Verdict.** Enabling rather than exponential; licensing-critical for advanced fuels.

#### E2 Pool and dry cask storage management  —  Incremental · data closed · difficulty low

- **Today.** About 100 US independent storage installations at about $15 k per cask per year; EPRI chloride-induced stress-corrosion cracking guidance; loading by spreadsheets and vendor codes; academic loading optimisers solve 1,200-assembly problems in under a second.
- **Bottleneck.** Canister inspection access; conservative decay-heat limits; the US federal liability of $37 to 45 B is a cost of not moving fuel.
- **Data.** Inspection data utility-owned; few casks instrumented; one high-burnup demonstration cask public.
- **Who is on it.** EPRI, PNNL, Sandia, academic optimisers, ResNet corrosion detection (2020), 159 NDE and ML papers reviewed in 2025.
- **Gap.** A product coupling per-assembly characterisation, loading optimisation, thermal modelling and aging risk; fleet-wide cask health monitoring is absent.
- **Prize.** $100 to 300 M per year globally in fewer casks and avoided repacking.
- **Verdict.** Bounded dollars; loading optimisation is academically solved.

#### E3 Transport of spent fuel and high-activity material  —  Incremental · data mixed · difficulty low

- **Today.** DOE Atlas railcar certified 2023 to 2024 after ten years; START and TRAGIS routing tools; routine shipments in Europe and Japan.
- **Bottleneck.** Political and regulatory (no US destination) rather than computational.
- **Data.** Route data public; shipment and security data closed.
- **Who is on it.** DOE national laboratories; almost no ML in the open literature.
- **Gap.** Content-specific package analysis, national campaign scheduling once a destination exists.
- **Prize.** Incremental until a US repository or interim facility exists (DOE approved a 15,000 t interim facility plan in 2026).
- **Verdict.** Blocked by policy.

#### E4 Reprocessing and recycling  —  Strong · data closed · difficulty high

- **Today.** Orano La Hague (about 1,130 t in 2025), Rokkasho commissioning, Mayak; US entrants Curio, Oklo (Tennessee facility, up to $1.7 B roadmap), Alpha Nur, SHINE with $19 M DOE awards (2025); pyroprocessing at INL and KAERI.
- **Bottleneck.** Process chemistry data tacit and classified; material accountancy by periodic inventory with percent-level uncertainty; new US plants lack pilot data; 10 CFR 70 untested for a commercial recycler.
- **Data.** Closed; virtual plant simulators at Sandia and PNNL are the only route.
- **Who is on it.** PNNL and Sandia transformer anomaly detection on a virtual plant (2023, not deployable); electrochemical sensors with AI for pyroprocessing (2024).
- **Gap.** Hybrid physics-ML flowsheet twins with safeguards-by-design and process-monitoring accountancy for greenfield plants.
- **Prize.** A few percent of throughput and availability on a $5 to 20 B facility plus reduced accountancy uncertainty, over $100 M per year per plant, contingent on facilities existing.
- **Verdict.** A call option on US and UK recycling.

#### E5 Waste classification, treatment, vitrification, inventories  —  Exponential · data open · difficulty medium

- **Today.** Hanford WTP commissioning (56 M gallons; DOE Environmental Management liability over $417 B); Sellafield forecast 136 B pounds and rising; PNNL Gaussian-process and active-learning glass-formulation models with uncertainty replaced a traditional equation (2024 to 2026); DOE Genesis Mission AI roadmap for cleanup (2025); NDA's 9.5 M pound Auto-SAS sorting on site 2027.
- **Bottleneck.** Tank-waste heterogeneity and sparse sampling; glass formulation constrained by property models; waste-acceptance conservatism drives volume; inventories are static PDFs.
- **Data.** Decades of Hanford tank samples and PNNL glass property databases, comparatively rich and partly public.
- **Who is on it.** PNNL, DOE EM, NDA, Sellafield.
- **Gap.** Active-learning loops still offline; no tank-to-glass-to-canister optimisation of the 40-year mission schedule; no ML waste classification and sorting at scale.
- **Prize.** Hanford and Sellafield burn tens of billions; 10 % glass volume or a year of schedule is billions.
- **Verdict.** Data exist, the customer has the money and a mandate; institutional adoption is the pace-setter.

#### E6 Geological disposal science and licensing  —  Strong · data mixed · difficulty high

- **Today.** Onkalo operating licence under review (extended to 2026); Forsmark approved 2022; Nagra application 2024; Cigeo under review; Deep Isolation licensed to Navarro (2025); DOE GDSA framework (PFLOTRAN and Dakota).
- **Bottleneck.** Performance assessment over a million years needs thousands of coupled runs; process models too expensive to embed, so abstractions are used; reviews take years.
- **Data.** Simulations abundant; underground-laboratory field data rich but scattered; PFLOTRAN open.
- **Who is on it.** Sandia neural surrogates of fuel-matrix degradation inside PFLOTRAN (2020 to 2023); physics-guided graph-attention transport surrogates with conformal UQ (2025); reviews report one to four orders of magnitude speed-up.
- **Gap.** Regulator-credible UQ for ML surrogates; end-to-end differentiable performance assessment; LLM-assisted review of repository dockets.
- **Prize.** Repositories cost $10 to 30 B each and a licensing year is about $1 B of carrying cost; but timelines are dominated by politics.
- **Verdict.** Exponential in leverage, uncertain realisable slice.

#### E7 Decommissioning: characterisation, robotics, cutting, cost  —  Exponential · data closed · difficulty high

- **Today.** Sellafield, Fukushima Daiichi (first debris grains retrieved 2024 to 2025; 20 m arm for 2026), DOE EM, EDF, KHNP; gamma imaging (Createc N-Visage), Spot and LiDAR mapping, Bayesian drum profiling; NEA cost structure; GAO (2026) says DOE cost and schedule information is inaccurate.
- **Bottleneck.** Characterisation and waste routing: over-classification multiplies disposal cost; remote operations are teleoperated, not autonomous; cost estimates carry 30 to 50 % uncertainty.
- **Data.** Site data closed but huge; benchmark exercises exist.
- **Who is on it.** Createc and RAICo, ANYbotics, NDA robotics programme, Bayesian and Gaussian-process contamination inference; cost-estimation ML nearly absent.
- **Gap.** Autonomous characterise-cut-sort loops; probabilistic 3D activity maps that update with every measurement; ML cost and schedule models trained on NEA, DOE and NDA project histories.
- **Prize.** Global liabilities about $1 T (DOE $544 B, Sellafield 136 B pounds, Fukushima over 8 T yen); 5 % is $50 B.
- **Verdict.** Robotics in high-dose environments and procurement culture; but the pool is the largest in the industry.

#### E8 Safeguards and nonproliferation  —  Incremental · data closed · difficulty medium

- **Today.** IAEA safeguards in 190 states, over 3,000 in-field verifications; robotic Cherenkov viewing device authorised 2024; ML for open-source relevance, satellite change detection, particle matching; antineutrino detection still below IAEA detection thresholds for small reactors.
- **Bottleneck.** Inspector person-days and analyst review time; bulk-facility accountancy uncertainty; SMR and microreactor fleets will multiply sites.
- **Data.** Mostly classified; virtual facilities and open satellite imagery.
- **Who is on it.** IAEA in-house, PNNL, Sandia, ORNL, LANL, BNL.
- **Gap.** Fleet-scale unattended verification for SMRs; validated partial-defect detection; process-monitoring safeguards for new reprocessing plants.
- **Prize.** Small in dollars (IAEA safeguards budget 150 to 200 M euro per year), high strategic leverage, weak commercial pull.
- **Verdict.** Institutional adoption slow by design.

#### E9 Environmental monitoring and emergency response  —  Incremental · data open · difficulty low

- **Today.** NARAC plume products in 5 to 10 minutes; JRODOS and EURDEP in Europe; national dose-rate networks; NARAC has learned weather-physics uncertainty from 1,200-run ensembles.
- **Bottleneck.** Source-term inversion under uncertain meteorology in minutes; sparse or faulty sensors.
- **Data.** Open sensor networks, weather ensembles, Fukushima and Chernobyl datasets.
- **Who is on it.** LLNL, European consortia; many 2025 to 2026 papers on ML inversion and PINNs.
- **Gap.** Operational deployment of learned emulators with calibrated UQ; sensor placement; fusion with satellite data.
- **Prize.** Incremental in money, high in public trust; a ready regulatory customer base.
- **Verdict.** Mature academic base, deployment gap.

#### E10 Isotope production and supply chains  —  Strong · data closed · difficulty low

- **Today.** Reactor-based Mo-99 and Lu-177 from six ageing reactors; a 2025 Petten outage caused a weeks-long global shortage; Ac-225 supply about 2 Ci per year; radiopharmaceutical market $7.7 B (2025) growing about 8 % per year; SHINE, NorthStar, BNL.
- **Bottleneck.** Decay-constrained logistics (Tc-99m 6 h, Lu-177 6.7 d), single points of failure, irradiation slot scheduling, customs; hospitals plan with rudimentary tools.
- **Data.** Demand and delivery data commercial; irradiation physics well modelled.
- **Who is on it.** BNL ML for irradiation placement and scheduling; reinforcement-learning irradiation simulation; logistics vendors.
- **Gap.** An end-to-end stochastic optimiser linking reactor schedules, target chemistry, processing, air freight and patient scheduling; a shared outage-risk model across the six reactors.
- **Prize.** 10 % less decay and logistics loss on a $7 to 8 B market is $0.5 to 1 B per year, plus the therapeutic wave (Pluvicto, Ac-225).
- **Verdict.** Buyers exist now; the problem is unowned.

### F. Cross-cutting and system layer

#### F1 Project finance, cost estimation and reference-class forecasting  —  Exponential · data mixed · difficulty medium

- **Today.** Bottom-up estimates on incomplete designs plus vendor quotes and Monte Carlo contingency; Vogtle from $14 B to over $34 B; Flamanville twelve years late; post-1970 US plants averaged 241 % overnight overrun; the MIT Joule 2020 study put most escalation in indirect costs. Reference-class forecasting (Flyvbjerg) is known and almost never applied.
- **Bottleneck.** Estimates are politically anchored and made on immature designs; no live structured cross-project cost and schedule dataset; EPC claims records are private.
- **Data.** EEDB, NEA and INL reports, PUC filings (Vogtle monitor reports unusually granular), Flyvbjerg's database; schedules private.
- **Who is on it.** INL parametric overrun models (2021); Westinghouse and Google Cloud sequencing; Aalo and Microsoft risk models.
- **Gap.** A Bayesian reference-class model with design maturity, first-of-a-kind status, contract form and float as features, updated live from construction telemetry; an estimate-audit LLM that flags placement rates disjoint from five decades of actual rates.
- **Prize.** 10 % less first-of-a-kind contingency on a $15 to 30 B project is $1.5 to 3 B; better-calibrated risk lowers cost of capital, which is 40 to 60 % of nuclear LCOE.
- **Verdict.** Almost no ML in use; data access and incentives are the difficulty.

#### F2 Supply chain, QA documentation, counterfeit parts, forgings  —  Strong · data closed · difficulty medium

- **Today.** NQA-1 programmes, paper travellers and material certificates, NUPIC audits; Japan Steel Works makes about 80 % of ultra-large forgings with 36 to 60 month lead times; IAEA and NRC counterfeit-item guidance; Westinghouse's $80 B ten-unit AP1000 programme (2025).
- **Bottleneck.** Documentation labour (QA packages of tens of thousands of pages), 18 to 36 month supplier qualification, no machine-readable provenance chain; forging capacity is physical but its scheduling is not.
- **Data.** Unstructured private PDFs; Part 21 reports public.
- **Who is on it.** Forged Operations (startup), VCDNP and King's College fraud papers (2025), Nuclearn document search.
- **Gap.** LLM extraction of certificates and travellers into structured records; anomaly detection on certificate patterns; automated supplier-qualification evidence; forging-slot optimisation across a multi-unit programme.
- **Prize.** QA documentation is a meaningful share of the indirect costs behind overruns; halving supplier onboarding widens the vendor base.
- **Verdict.** Incremental to large; regulatory acceptance of digital records is the gate.

#### F3 Fuel markets and trading  —  Incremental · data closed · difficulty low

- **Today.** Spot U3O8 about $90, term about $97; SWU spot $200 to 215; Sprott and Yellow Cake financialise spot; US utilities 60 % covered for 2030 and 9 % for 2033, the fourteenth straight year of under-replacement.
- **Bottleneck.** Thin, opaque, bilateral, paywalled monthly data; geopolitics dominates.
- **Data.** UxC and TradeTech paid; EIA and SPUT holdings public.
- **Who is on it.** Academic price models only; traders use spreadsheets.
- **Gap.** Stochastic procurement optimisation for utilities; event-driven price models.
- **Prize.** Tens of $M per year for a large utility.
- **Verdict.** Data moat belongs to the reporters.

#### F4 Grid and system planning, co-location, PPAs  —  Incremental · data open · difficulty medium

- **Today.** Capacity-expansion models treat nuclear as a fixed inflexible block; data-centre load drives PJM capacity prices; 15 to 20 year PPAs (Meta-Constellation Clinton, Amazon-Talen, Microsoft-Constellation); interconnection queues of seven years push co-location.
- **Bottleneck.** Models cannot represent modularity, ramping or first-of-a-kind cost distributions; PPA and hedge structuring for a plant that may slip years is bespoke.
- **Data.** ISO queues, prices and ELCC studies public; PPA terms private.
- **Who is on it.** Modo Energy, Yes Energy, academic GenX and ReEDS work.
- **Gap.** Surrogate capacity-expansion models running thousands of scenarios in minutes with nuclear timing uncertainty; a PPA and hedge structuring engine; siting optimisation over queues, water, seismic and load.
- **Prize.** Large but shared with other technologies.
- **Verdict.** Mature modelling ecosystem with nuclear-specific gaps.

#### F5 Regulation as a system: review throughput  —  Exponential · data open · difficulty medium

- **Today.** NRC recovers about 90 % of budget via fees ($336 per hour, $154 for advanced reactors); Hermes 2 in 10 months, NuScale US460 in 22 months, Kemmerer in 18; Part 53 finalised 2026; NRC AI strategic plan (2025), AI-powered ADAMS search, internal assistants; NRIC estimates AI could cut document development and review cycles by up to 50 %. Concerns: automation bias and LLMs not yet able to generate safety-case arguments (AI Now, NASA).
- **Bottleneck.** Review hours dominated by RAI ping-pong and cross-document consistency; both sides now instrumented but no shared structured digital application format.
- **Data.** ADAMS and the full regulatory corpus.
- **Who is on it.** NRC, DOE, Atomic Canyon, Nuclearn, Everstar, Inductive, Argonne Regulatory Context Protocol.
- **Gap.** Verified generation with traceable claim-to-evidence graphs; automated RAI prediction; a machine-readable licensing basis.
- **Prize.** Licensing is the schedule-critical path; fee hours alone about $1 B per year.
- **Verdict.** Same prize as C5 seen from the regulator's side; institutional difficulty.

#### F6 Workforce and education pipeline  —  Incremental · data mixed · difficulty low

- **Today.** NRC generic fundamentals exam pass rate about 96 %; VR field-operator training (GE Vernova, Fortum); an LLM fine-tuned on DOE handbooks passed 8 of 14 operator exam papers (2026).
- **Bottleneck.** Scale: hundreds of thousands of workers needed this decade; tacit knowledge retiring.
- **Data.** Public handbooks; controlled exam banks.
- **Who is on it.** GSE, Nuclearn, universities.
- **Gap.** Adaptive tutoring tied to simulator telemetry; NRC-approved AI exam banks.
- **Prize.** Incremental but critical for scale.
- **Verdict.** Incremental.

#### F7 Public acceptance and communication  —  Incremental · data open · difficulty low

- **Today.** Gallup 61 % support (2025), near record; communication by press releases and hearings; fine-tuned LLMs on 1.26 M nuclear tweets (Michigan 2024).
- **Bottleneck.** A single failed siting costs years.
- **Data.** Social and media data public.
- **Who is on it.** Academic.
- **Gap.** Localised sentiment and misinformation tracking for siting; evidence-based messaging tests.
- **Prize.** Small to medium.
- **Verdict.** Support already high.

#### F8 Fusion: control, disruption prediction, design  —  Exponential · data mixed · difficulty high

- **Today.** DeepMind and EPFL reinforcement-learning magnetic control on TCV (Nature 2022); tearing-mode avoidance on DIII-D (Nature 2024); DeepMind and CFS using the differentiable TORAX code to run millions of virtual SPARC shots (2025); Proxima's stellarator surrogates and open ConStellaration dataset; ORNL generative models for tungsten microstructure.
- **Bottleneck.** Shot data scarce and machine-specific; ITER needs over 95 % disruption avoidance with few false alarms; materials qualification lacks a neutron source.
- **Data.** Machine data partly open; simulation codes increasingly open and differentiable.
- **Who is on it.** DeepMind, CFS, Proxima, Type One, DIII-D, ORNL.
- **Gap.** Sim-to-real transfer for first-of-a-kind machines; foundation models across tokamaks; inverse design coupling plasma, coils, neutronics and cost.
- **Prize.** Fusion viability is design- and control-limited.
- **Verdict.** Exponential and already being pursued by the strongest teams in the field.

#### F9 Space nuclear and microreactor autonomy  —  Exponential · data closed · difficulty very high

- **Today.** NASA and DOE lunar fission surface power by 2030 explicitly requires autonomous operation; Project Pele ships to INL in 2026; INL MARVEL and autonomy programme; graph-neural-ODE digital twins and health-aware reinforcement-learning supervisory control (2026).
- **Bottleneck.** No regulatory pathway for remote or autonomous commercial operation; sparse operating data for new designs.
- **Data.** New designs have no operating history.
- **Who is on it.** INL, BWXT, Northrop Grumman, Lockheed Martin.
- **Gap.** A certified autonomy stack reusable across fleets; fleet learning.
- **Prize.** Staffing dominates O&M below 10 MWe; exponential for microreactor economics.
- **Verdict.** Same gate as D1: licensing.

#### F10 Codes, standards and digital engineering  —  Strong · data mixed · difficulty high

- **Today.** ASME Section III, NQA-1 and ANS standards are PDFs on multi-year cycles; ASME digital-engineering programme; INL and NRIC MBSE-first implementation; NRC HARDENS; Sandia security-inclusive MBSE.
- **Bottleneck.** Standards are not machine-readable, so compliance cannot be automated; MBSE adoption partial and unconnected to licensing.
- **Data.** Standards paywalled; models proprietary.
- **Who is on it.** ASME, INL, NRIC, Sandia, Westinghouse HiVE.
- **Gap.** Executable standards (rules as code); requirements-to-evidence traceability across MBSE models; LLM-assisted code-case drafting.
- **Prize.** Enabler for licensing, construction QA and supply chain; exponential only in combination.
- **Verdict.** Consensus bodies move slowly; the multiplier is large.

## For a company that already does ML prospecting

**Now: close the loop on drilling.** Turn prospectivity into sequential drill-hole selection under a budget (Bayesian optimisation or active learning over the basin model), updated in real time from downhole gamma and prompt-fission-neutron logs. This is the difference between a map and a decision, and it is where the label-scarcity problem is actually solved: each hole is a new label.

**Next: own log-to-grade.** A disequilibrium-aware model from spectral gamma and PFN logs to recoverable uranium at pattern scale. It is the same data you already handle, it feeds resource estimation, and it is the entry ticket to ISR operators because their ramp-up shortfalls start here.

**Then: the well-field.** Well-field design with surrogate reactive-transport models (a published +15 % NPV) and, above all, closed-loop acid and flow control per well. This is the largest un-served software pool in the front end and the customer list is short and rich.

**Adjacent: uranium-recovery permitting.** The regulator is already using language models; applicants are not. Environmental-report drafting, RAI prediction and baseline-data QA for ISR licences is a small product with a one-to-two-year prize per project.

## Method and limits

Six research agents each covered one stage group with web searches (September 2026), returning per-step findings with sources;
the synthesis, verdicts, ranking and theses are the author's. Prize figures are order-of-magnitude and come from the cited
public numbers (NEI cost data, DOE liabilities, project overruns, market sizes). Anything inside enrichment plants, fuel
fabrication lines and plant historians is inferred from the outside, because those data are closed. The map is a starting
point for diligence, not a substitute for it.
