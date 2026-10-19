# Adversarial deep check: failed-Phase-3 rescue with pooled patient data (N2) (2026-10-19)

## Verdict
**N2 scores 13/25 after the check, down from 18. It is not a venture for this team, and it is only partly Terranox-shaped.**

The deal facts hold up: Summit's ridinilazole went for $0.5M upfront, Galera's two assets for $3.5M, and Biossil is valued at $1B. There are at least 12 more orphaned late-stage sales at $0.25-40M upfront. But four things the 18 depended on fail under checking.

1. **The ML lever has direct negative evidence, and on our own test bed.**
   - Chekroud et al. (Science, Jan 2024) used **YODA**, the platform we planned to test on. They trained outcome models on 5 schizophrenia RCTs. The models were accurate within their own trial and **at chance on every other trial**. **Pooling across trials did not help.**
   - Causal forests found effect-varying subgroups in ACCORD that **did not replicate in VADT**, a near-identical diabetes trial (Ann Epidemiol 2021).
   - Wallach 2017: none of 5 retested subgroup claims replicated.
   - We found **no published case** of an ML-discovered subgroup from a failed trial replicating prospectively.
   - Rescues that worked used a mechanistic biomarker, a genotype the drug targets (olaparib BRCA, gefitinib EGFR), and the original big-pharma owner made them. They were not orphaned and not ML.
2. **The data moat is not ours to build.** Biossil already gets each asset's patient-level data with every deal (12+ assets, $153M raised). Pathos AI ($1.6B, bought Rain's failed Phase 3 milademetan) does too. Pooling patient data is a by-product of buying assets, so it is not a wedge. The pooled data is also heterogeneous: different drugs, indications and endpoints, which is exactly where Chekroud found that pooling fails.
3. **L3 is not really inverted; the low price is fair.** A seller dumps the asset for $0.5M because the asset's value is P(win) x value minus a $20-60M re-trial, which is close to zero. The cheap price reflects the cost of the proof, not a seller who cannot read the data. Buyers see the full data room under NDA, so there is no information asymmetry the way there is with SMAD. The upside only exists if your subgroup model beats everyone else's, and that is point 1.
4. **C1 and fit.**
   - The proof is a $20-60M biomarker Phase 2b/3 that takes 2-4 years. The median pivotal trial costs about $19M (Moore et al., JAMA IM 2018, memory).
   - Each rung needs regulatory, CMC and clinical operations staff and $50-200M of equity. A two-person ML team from energy and mining would be about $220M and 3 years behind Biossil.

**Score: C1 2, C2 4, C3 2, C4 2, C5 3 = 13/25.**
- **Killers:** R-ML, now with direct evidence; C1, because the proof is a trial; L6, now hard, since Biossil and Pathos both hold the rung and reach the same data.
- **What would revive it:** a positive cross-trial replication test (Section 5) clearing at least 30% replication where the literature shows about 0%. That test is cheap (about $10-30k and 3-6 months), but the prior on it passing is now low (we estimate 10-15%).

## 1. Deal verification and orphaned late-stage sales

| # | Asset (seller to buyer, date) | Stage / why orphaned | Upfront | Back-end | Source |
|---|---|---|---|---|---|
| 1 | Ridinilazole (Summit to Biossil, 14 Jul 2026) | Phase 3 missed superiority; no buyer since 2022 | **$0.5M** | up to $104.5M milestones + royalties | [BioSpace PR](https://www.biospace.com/press-releases/summit-therapeutics-signs-agreement-to-sell-phase-iii-asset-ridinilazole-to-biossil-inc), [Fierce](https://www.fiercebiotech.com/biotech/summit-sells-failed-antibiotic-openai-backed-startup-105m-deal) **VERIFIED** |
| 2 | Avasopasem + rucosopasem (Galera to Biossil, 22 Oct 2025) | Phase 3 asset received a CRL (Aug 2023); FDA wanted another Phase 3 | **$3.5M** | up to $105M + CVR; Biossil also takes on Blackstone's 4% royalty | [StockTitan](https://www.stocktitan.net/news/GRTX/galera-therapeutics-announces-acquisition-of-dismutase-mimetics-8pulrnbo7s22.html), [Barchart](https://www.barchart.com/story/news/35605028/galera-therapeutics-announces-acquisition-of-dismutase-mimetics-portfolio-by-toronto-based-biossil-for-up-to-105-million) **VERIFIED** (the earlier "$3.5M" was right; the buyer is Biossil) |
| 3 | Veverimer (Tricida to Renibus, Feb 2023, s.363) | Phase 3 VALOR-CKD failed; bankruptcy | **$0.25M** | $2.5M on approval + up to $150M sales milestones | [Davis Polk](https://www.davispolk.com/experience/tricida-chapter-11-liquidation-june-2023) |
| 4 | MultiStem (Athersys to Healios, Apr 2024) | Pivotal stroke trial disappointed; bankruptcy | **$2.25M** (credit bid) | none | [Fierce](https://www.fiercebiotech.com/biotech/athersys-files-bankruptcy-sells-assets-healios-wake-roke-cell-therapys-struggles) |
| 5 | Intepirdine (GSK to Axovant, Dec 2014) | Abandoned after 4 failed trials | **$5M** | | [Alzforum](https://alzforum.org/node/900631). Axovant IPO'd at a ~$2-3B valuation, then MINDSET failed in 2017 and the stock fell 70% |
| 6 | Pegzilarginase (Aeglea to Immedica, Jul 2023) | Refuse-to-file from FDA | **$15M** | up to $100M; $10M earned 2025 | [Fierce](https://www.fiercebiotech.com/biotech/immedica-takes-embattled-rare-disease-asset-aegleas-hands-15m-cash) |
| 7 | Berdazimer gel (Novan to Ligand, Sep 2023, s.363) | Under FDA review; seller bankrupt | **$12.2M** | none | [BioSpace](https://www.biospace.com/ligand-acquires-assets-of-novan-inc-for-12-2-million). **Approved Jan 2024 as Zelsuvmi** |
| 8 | Milademetan (Rain Oncology to Pathos AI, Jan 2024) | Phase 3 MANTRA failed | about $1.16/share, near cash value, so the asset was effectively free | CVR $0.17 | [Pharma Letter](https://www.thepharmaletter.com/article/pathos-ai-to-buy-rain-oncology), [BusinessWire](https://www.businesswire.com/news/home/20240126877395/en) |
| 9 | Avexitide (Eiger to Amylyx, 2024) | Seller bankrupt after a Phase 3 failure elsewhere | **$35M** | | [BioSpace](https://www.biospace.com/business/biopharma-bankruptcies-still-at-peak-with-little-relief-in-sight) |
| 10 | Bentracimab (PhaseBio, 2022, s.363 stalking horse) | Seller bankrupt mid-Phase 3 | **$40M** | $60M regulatory | [SEC 8-K](https://www.sec.gov/Archives/edgar/data/1169245/000116924522000103/phasebioplansfornear-terms.htm) |
| 11 | Praliciguat (Cyclerion to Akebia, Jun 2021, licence) | Phase 2 failed in DKD/HFpEF | **$3M** | up to $585M (later cut) | [SEC 8-K](https://www.sec.gov/Archives/edgar/data/1755237/000114036121019923/brhc10025496_8k.htm) |
| 12 | Gritstone assets (2024 auction) | Seller bankrupt | **$21.2M** total | | [BioSpace](https://www.biospace.com/business/biopharma-bankruptcies-still-at-peak-with-little-relief-in-sight) |
| 13 | Ztalmy / Marinus (to Immedica, Dec 2024) | Approved drug; RAISE Phase 3 failed | about **$151M** for the company | | [Fierce Pharma](https://www.fiercepharma.com/pharma/troubled-marinus-tides-turn-151m-buyout-immedica-pharma) |
| 14 | Concentra / Tang Capital buyouts (IGM, Cargo, Kronos, Elevation, Allakos, iTeos; 2025) | Failed biotechs bought at or below cash, with CVRs | ~$0 implied for assets | CVR on asset sales | [SEC TO-T](https://www.sec.gov/Archives/edgar/data/1496323/000114036125025957/ny20051934x1_exa1d.htm), [Fierce](https://www.fiercebiotech.com/biotech/concentra-curveball-offer-throws-acelyrin-merger-alumis-doubt) |

**Biossil, verified:**
- **Funding:** Out of stealth 21-23 Apr 2026, with $43M announced and about $70M total equity ([BetaKit](https://betakit.com/biossil-exits-stealth-with-70-million-usd-to-give-failed-medicines-a-second-chance/)). In Sep 2026 it raised **$153M at a ~$1B valuation**, led by the OpenAI Startup Fund, with Founders Fund and ADIC also in ([The Logic](https://thelogic.co/briefing/openai-backs-biossil-in-us153m-funding-round-report/), [Dealroom](https://dealroom.co/news/157312-openai-leads-150m-round-for-drug-reviving-startup-biossil/)).
- **Pipeline:** About 30 staff. Active trials in sickle cell, IPF, glioblastoma, breast cancer and Alzheimer's, and "nearly a dozen" more planned. The "12 molecules" figure is unverified; no public list exists.
- **Method:** It uses LLMs over public failed-trial data to pick assets, then buys or licenses them. It also earns licensing revenue, so it is already part asset-flipper.

**What the deals show:**
- Upfronts are $0.25-5M for true orphans and $12-40M where a bankruptcy auction has bidders.
- The seller keeps $100-150M in milestones, so the upside is shared.
- Supply is plentiful: biotech bankruptcies are at a peak, and in Hwang 2016, 54% of drugs entering Phase 3 failed.
- **Correction to the pair sweep:** the low price reflects how cheap the asset is to buy relative to the cost of proving it. It does not mean the seller could not read the data.

## 2. Base rate: do rescued failed or orphaned late-stage drugs get approved, and for how much?
No cohort study measures "failed Phase 3 → later approved". Our searches found none. Average Phase 3-to-approval probability of success is about 59%, but that is for fresh Phase 3s. The ~30% "repurposing success" figure is a blog-recycled number for curated candidates ([review](https://www.medrxiv.org/content/10.1101/2021.09.28.21264254v1.full)). From cases:

| Case | Rescue route | Outcome / value |
|---|---|---|
| Pirfenidone (InterMune) | CAPACITY 1/2 inconsistent → FDA CRL 2010 → ASCEND re-run in a more homogeneous population | Approved 2014; **Roche paid $8.3B** ([GEN](https://www.genengnews.com/news/roche-to-acquire-intermune-for-8-3b/)). The original owner rescued it with trial design, not ML |
| Olaparib (AZ) | Dropped Dec 2011 → retrospective BRCA subgroup from Study 19 → ODAC voted 11-2 against → confirmatory SOLO2 | Approved Dec 2014 (memory); now multi-$B/yr ([BioCentury](https://www.biocentury.com/article/275564/fda-panel-rebuffs-olaparib)). Mechanistic genotype, original owner |
| Gefitinib (AZ) | ISEL OS failure → EGFR-mutation subgroup → IPASS | EU approval 2009 in EGFR-mutant only; US 2015 (memory) ([NICE TA192](https://www.nice.org.uk/guidance/TA192/chapter/committee-discussion)). Genotype, original owner |
| Istradefylline (Kyowa Kirin) | FDA "not approvable" 2008 → more trials | Japan 2013, US 2019 (memory). 11 years, modest sales |
| Nirogacestat / mirdametinib (Pfizer shelved → SpringWorks 2017) | Shelved, not failed; re-run in a rare indication | Approved 2023/2025; **Merck KGaA paid $3.9B** in Apr 2025 ([Pharm Tech](https://www.pharmaceutical-technology.com/news/merck-kgaa-strikes-3-9bn-deal-for-springworks/)) |
| Roivant (vibegron, relugolix, tapinarof, brepocitinib, RVT-3101) | In-licensed shelved pharma assets | Several approvals; Telavant sold to Roche for $7.1B (memory). These were shelved, not failed |
| Berdazimer (Novan → Ligand, $12.2M) | Bought out of bankruptcy | Approved weeks later. Small product (Pelthos) |
| Aducanumab | Futility → high-dose subgroup re-analysis | Accelerated approval 2021 → discontinued 2024 (memory). The subgroup "rescue" destroyed value ([Alzforum](https://alzforum.org/node/1512151)) |
| Intepirdine (Axovant, $5M from GSK) | Bought after 4 failed trials | Phase 3 failed 2017 |
| Solanezumab (Lilly) | EXPEDITION 1/2 failed → pooled "mild AD" subgroup → EXPEDITION3 | Failed 2016 (memory). This is the textbook prospective test of a subgroup rescue, and it failed |
| Tradipitant (Vanda) | Missed primary endpoint; argued from subgroup and exposure-response | CRL 2024 ([Pharmaphorum](https://pharmaphorum.com/news/vanda-slams-fda-rejection-gastroparesis-drug)) |
| Ataluren, bucindolol, milademetan | Subgroup or genotype rescue attempts | Not approved, or EU authorisation withdrawn (memory) |

**Read:**
- Rescues that re-run a trial with a better design or population do succeed sometimes, and the winners are worth $3-8B.
- Subgroup rescues succeed when the subgroup is a **mechanistic genotype**. When it is a statistical subgroup of clinical covariates (aducanumab, solanezumab, tradipitant), they have mostly failed or destroyed value.
- We estimate the base rate for an orphaned failed-Phase-3 asset reaching approval at **about 5-15%**, against about 59% for a fresh Phase 3.
- For a $1B+ approval value against a $20-60M trial, the expected value is positive only at the top of that range.

## 3. Does patient-level data transfer, and can it be pooled?
- **Transfer: usually yes.**
  - The buyer must take over the IND/NDA, and FDA requires the sponsor to hold the underlying data. Asset purchase agreements routinely list "clinical data" and "regulatory documentation" as transferred assets (general practice; we did not find an APA showing it).
  - Consent forms usually name "the sponsor and its successors". **EU/GDPR is the risk:** a regulator can block a new controller's use of acquired health data, as a Cagliari biobank case shows ([Portolano](https://portolano.it/en/blog/life-sciences/new-consent-for-processing-sensitive-data-not-needed-after-change-of-data-controller-data-protection-thoughts-and-ma)).
  - Re-using one asset's patients to train a model for **other** drugs is secondary research. It is defensible under US de-identification rules, but it is not guaranteed under GDPR Article 9.
- **Usability across assets: weak.**
  - Studies started after Dec 2016 must be in CDISC SDTM/ADaM, so the formats are compatible.
  - The semantics are not. Each asset brings a different drug, indication, endpoint, follow-up schedule and set of covariates. A responder model is drug-by-indication specific.
  - What does transfer is a **placebo-response / prognostic model**, a risk-based approach to effect variation (PATH statement). That is useful, but it is enrichment and not a moat. It is exactly what Chekroud found does not generalize across trials.
- **Diligence access:** a buyer can usually see the data room under NDA before signing. That is the best feature: the model can be run before paying. But every bidder, Biossil included, gets the same access.

## 4. Who else does this, and how they're doing

| Player | Model | Status (as checked) |
|---|---|---|
| Biossil (Toronto) | LLMs over public failed-trial data; buy or license; re-run | $153M at ~$1B (Sep 2026); ~30 staff; several trials; no readout yet. **The direct occupant** |
| Pathos AI (Tempus spin-out) | Data-driven oncology; bought Rain's failed Phase 3; in-licensed Novo's pocenbrodib | **$365M Series D at $1.6B** (May 2025) ([Fierce](https://fiercebiotech.com/biotech/pathos-ai-secures-365m-series-d-fund-trial-novo-nordisk-solid-tumor-drug)); has not mentioned milademetan since |
| Formation Bio | AI plus in-licensing of clinical assets; Sanofi/OpenAI partner | $372M Series D (Jun 2024, a16z) ([APR](https://www.americanpharmaceuticalreview.com/1315-News/613785-Formation-Bio-Secures-372MM-Series-D-Funding-to-Expanding-AI-Drug-Development-Platform/)); no 2025-26 round found |
| Roivant | Shelved-pharma in-licensing "Vants" | ~$3.9B cash (Jun 2026); brepocitinib (ex-Pfizer) launching for dermatomyositis ([Trefis](https://www.trefis.com/data/companies/roiv)). Won with capital and dealmaking, not ML |
| BridgeBio / SpringWorks pattern | Pharma-shelved assets in rare or genetic disease | SpringWorks → $3.9B. The winners used genetic mechanism, not ML |
| BenevolentAI | AI target and repurposing | Delisted 13 Mar 2025 via take-private ([BusinessWire](https://www.businesswire.com/news/home/20250312584164/en)) |
| Lantern Pharma (RADR) | AI-rescued oncology compounds | Market cap ~$20-37M in 2026; going-concern warning May 2026 ([TipRanks](https://www.tipranks.com/stocks/ltrn/market-cap)) |
| Healx | AI repurposing for rare disease | $47M Series C (2024); HLX-1502 in Phase 2 for NF1; no readout found ([Silicon Canals](https://siliconcanals.com/?p=52360)) |
| Every Cure | Nonprofit; MATRIX AI repurposing of approved drugs | $48.3M ARPA-H contract (Feb 2024) ([ARPA-H](https://www.arpa-h.gov/news-and-events/arpa-h-awards-ai-driven-project-repurpose-approved-medications)); no trial results found |
| Concentra (Tang), XOMA | Buy failed biotechs at or below cash | Financial arbitrage; they hold assets cheaply and option them |

**Pattern:**
- Capital is flowing to the occupants: Biossil $1B, Pathos $1.6B.
- No AI-rescue company has yet produced a positive pivotal readout from an ML-picked subgroup.
- The public AI-repurposing companies (BenevolentAI, Lantern) have collapsed.
- The winners from shelved or failed assets (Roivant, SpringWorks, InterMune) won with capital, trial design and mechanistic genetics.

## 5. Cheapest feasibility test (kill or keep in about 4 months)
**Question:** can an ML subgroup or effect model trained on trial A predict who benefits in an independent trial B of the same drug, better than chance and better than a simple risk model?

**Data:**
1. **Vivli.** Requests are free. The standard secure environment is free for 365 days, then $12/day; the premium one is free for 90 days, then $25/day ([Vivli](https://vivli.org/resources/requestdata/)). Access takes "a few months", and data cannot be exported from the secure environment. It holds Lilly, GSK, Roche and many other sponsors.
   - Target **twin trials of failed drugs**: solanezumab EXPEDITION 1/2 → 3, if Lilly lists them. That is the ideal pre-registered test, because the pooled mild-AD subgroup failed prospectively.
   - Also target twin Phase 3s that split, where one hit and one missed.
2. **YODA** (J&J only). Free. Median **25 days** to a decision and **80 days** to data access (n=531) ([YODA metrics Jul 2026](https://yoda.yale.edu/wp-content/uploads/2026/07/YODA-Project-Dashboard-Metrics-July-2026.pdf)). Chekroud already used this route for schizophrenia, so pick other indications: canagliflozin, esketamine, rivaroxaban twin trials.
3. **NHLBI BioLINCC** (memory: free, needs IRB, weeks). ACCORD/VADT/SPRINT already show negative replication of causal-forest subgroups.
4. **Project Data Sphere.** Free and immediate, with 200+ Phase 3 oncology trials and about 240k patients. It is **mostly comparator arms** ([RTI/ASA 2021](https://ww2.amstat.org/meetings/proceedings/2021/data/assets/pdf/1913812.pdf)), so it is useful only for prognostic models, not for treatment-effect models.

**Protocol:**
- Choose 6-10 drug-indication pairs that each have 2 or more independent RCTs.
- Pre-register the analysis on OSF.
- Train causal forest, X-learner and LLM-feature models on trial A. Pre-specify one subgroup per drug, then test the treatment-by-subgroup interaction in trial B.
- **Pass bar:** at least 30% of predicted subgroups replicate at p<0.05 in the same direction, **and** the model beats a risk-based (PATH) baseline on c-for-benefit. The base rate from Wallach, Chekroud and ACCORD/VADT is about 0%.

**Cost:** about $10-30k cash (compute after the free tiers, IRB for BioLINCC). Time: 2 people for 3-4 months, plus 3-5 months of waiting for access, which overlaps the work. **Run the YODA and BioLINCC arms first**; they are fastest.

**Kill rule:** if fewer than 2 of 8 subgroups replicate, R-ML is confirmed and N2 is dead. A pass would be publishable on its own. It would also be the one thing Biossil cannot claim, because it selects on public summaries.

## 6. Verdict for Dhruv: venture scale, team fit and Terranox shape

| Criterion | Pair sweep | After check | Why |
|---|---|---|---|
| C1 Frame | 2 | **2** | The proof is a $20-60M, 2-4 year trial. Discovery is perhaps 20% of the work |
| C2 Step-up | 5 | **4** | $0.5-3.5M upfront → $1-8B on approval, but $100-150M of milestones go back to the seller and $20-60M of trial cost comes first. On a risk-adjusted basis, about 10-100x on capital at risk |
| C3 Lever | 3 | **2** | Lift is unproven and the direct evidence is negative (Chekroud 2024 on YODA, ACCORD/VADT, Wallach) |
| C4 Data and right | 4 | **2** | The right is cheap, but the data is not illegible-public: every bidder gets the data room. The pooled-data moat accrues to Biossil and Pathos too. GDPR limits secondary use |
| C5 Ladder | 4 | **3** | Asset → partner → own commercial is real (Roivant, SpringWorks), but it is a capital ladder, not an ML ladder |
| **Total** | **18** | **13** | |

- **Venture scale?** The category is venture scale: Biossil at $1B, Pathos at $1.6B and Roivant prove that. But it is a **capital-and-clinical-operations business**. It needs $150-300M before the first pivotal readout and a team with regulatory, CMC and medical leadership. A two-person ML team with an energy and mining background has no edge to bring, and arrives about $220M and 3 years behind Biossil, against an occupant that bids on the same deals.
- **Terranox-shaped?** Only half.
  - **Same:** buy a right cheaply from an owner who has moved on, then prove it.
  - **Different on all three things that make Terranox work:**
    - the data is not public, so you see it only in a competitive data room;
    - the proof is a $20-60M trial rather than drilling that a land position can fund;
    - the ML lift is unproven, and the evidence against it is negative.
- **Recommendation:** do not pick N2 for the YC application. Log the new evidence in LEDGER: **R-ML is confirmed on trial data**, with Chekroud 2024 on YODA at chance out-of-sample. Spend about $15k and a few weeks only if Dhruv wants a cheap lottery ticket: the YODA and BioLINCC twin-trial replication test in Section 5. A pass would revive the idea to about 17, and it would also make a strong paper.
