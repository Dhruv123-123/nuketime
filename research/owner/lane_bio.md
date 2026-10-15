# Lane: biopharma and life sciences. Re-reading abandoned development work

Written 15 Oct 2026. 20 WebSearch calls used. Fetches noted inline. The cloud proxy blocked api.fda.gov (curl returned CONNECT 403), so the openFDA CRL API is verified from its documentation and secondary analyses only, not from a live pull.

## Bottom line

The obvious version of this lane ("AI finds failed drugs worth reviving, then buys them") is no longer open. **Biossil** (Toronto) raised a US$153M round led by the OpenAI Startup Fund at a US$1B valuation in September 2026. It already holds 12 molecules, including Summit's ridinilazole, bought for $0.5M upfront plus up to $104.5M in milestones (July 2026). **Ignota Labs** bought Kronos Bio's entire clinical portfolio in October 2025. Healx, Every Cure, BridgeBio and Roivant cover the rest. A new company should not pitch generic resurrection.

What is still open is narrower. It uses **legally created public datasets that are younger than these incumbents' platforms**, and it ends in an **exclusive, rivalrous claim**:

1. **The FDA CRL corpus.** Published since July 2025. Read it for abandoned near-approvals whose failure was fixable, then buy the NDA or BLA. **Score 7.5.**
2. **Molecules approved abroad but never in the US.** Get US rights by exclusive licence, then earn US NCE exclusivity (and orphan exclusivity where it applies), whatever the patent status. **Score 6.5.**
3. **Rare-pediatric PRV yield from orphaned assets.** The program was reauthorised on 3 Feb 2026, runs through 30 Sep 2029, and vouchers sell for $150-200M. **Score 5.5.** Best run as an overlay on #1 and #2, not as a standalone company.
4. **Veterinary field-of-use licences on shelved human clinical assets.** **Score 4.5.** The precedents are real, but exits are small and Anivive and others are already doing it.
5. **Responder-subgroup rescue from patient-level trial data (Vivli, YODA, Project Data Sphere).** **Score 2.5.** Killed: the Vivli DUA gives data contributors licence and option rights over any IP you generate, and Biossil runs exactly this thesis.

I recommend #1, with #2 and #3 as the same machine reading different source sets. All three share one structure: (public regulatory record) → (ML judges which failures are fixable or which assets transfer) → (buy or exclusively licence the asset from a distressed or uninterested owner) → (FDA exclusivity plus PRV). That is the Terranox structure: read what others abandoned, then stake the claim.

---

## Candidate 1: CRL-rescue. Buy fixable rejected drugs (score 7.5/10)

**Dataset and why it is public.** FDA began publishing Complete Response Letters in July 2025 (a batch of 200+, covering 2020-2024 applications). In September 2025 it said it would publish new CRLs as they are issued, including for **unapproved** applications. This reversed decades of confidentiality. openFDA serves them at `api.fda.gov/transparency/crl` as separate approved and unapproved PDF sets (https://open.fda.gov/apis/transparency/completeresponseletters). The corpus held 458 records as of 13 Aug 2026 (https://intuitionlabs.ai/articles/fda-complete-response-letters-dataset). Join it with:
- Drugs@FDA action history
- ClinicalTrials.gov results
- the orphan designation database
- SEC 8-K/10-K and bankruptcy dockets, for sponsor distress
- FDA Form 483 and warning letters, for the facility behind a CMC failure
- USPTO patent and term data
- EMA withdrawn-application assessment reports

**Why it is a re-read of abandoned work.** Before this, sponsors' press releases spun CRLs ("FDA requested additional information"), and the market priced a CRL as roughly fatal. Now the letter itself is public. An independent coding of the 2025 batch found facility-inspection deficiencies in 58% of letters, product-quality deficiencies in 43%, and clinical deficiencies in only 28% (categories overlap; same source). The JAMA 2014 series of first-cycle NME failures found 15% were CMC/labelling-only. Many CRL'd assets belong to microcaps that then ran out of cash. Their NDA, data package and orphan or RPD designations sit in a zombie shell or a bankruptcy estate.

**The anchor case: arimoclomol.**
- FDA issued a CRL to Orphazyme on 17 Jun 2021. Orphazyme went into Danish in-court restructuring.
- KemPharm (now Zevra) bought substantially all of its assets for **US$12.8M cash** plus about $5.2M of assumed liability (May 2022) (https://www.biospace.com/kempharm-announces-strategic-acquisition-of-arimoclomol-from-orphazyme-expanding-its-rare-cns-diseases-pipeline).
- Zevra won approval as Miplyffa in September 2024 and **sold the rare-pediatric PRV that came with it for $150M** in April 2025 (https://www.pharmaceutical-technology.com/news/zevra-sells-priority-review-voucher-for-150m-to-support-drug-launches/).
- Miplyffa then booked $17.1M of net revenue in its second full quarter (Q1 2025) (https://www.sec.gov/Archives/edgar/data/0001434647/000143774925016452/ex_762500.htm).
- The voucher alone returned more than 10x the purchase price.

**ML problem (hard, not lookup).**
- (a) Parse letters into structured deficiencies: which ones, how many trials needed, whether a facility can be swapped, whether a REMS is required. They are messy, partly redacted PDFs with heterogeneous language.
- (b) Train a "fixability, cost and time to resubmission" model on historical CRL → resubmission → approval outcomes. Labels come from Drugs@FDA action histories (Class 1 and Class 2 resubmissions) and from older CRLs reconstructed from approval-package "Other Action Letters" PDFs, which FDA has long posted for drugs that were eventually approved, so pre-2025 labels exist.
- (c) Model sponsor distress and asking price from SEC filings, cash runway and bankruptcy dockets.
- (d) Value the asset with exclusivity and PRV eligibility included.

This is sparse, multi-modal survival-style inference with a few thousand events. Generic biotech BD teams read these letters by hand, one deal at a time.

**What the company owns.** The NDA or BLA itself, the data package, and the orphan, RPD and fast-track designations, bought by asset purchase or exclusive licence. That ownership is rivalrous: only one buyer can hold an NDA. After approval the company also holds:
- 5-year NCE exclusivity, if the active moiety was never approved
- 7-year orphan exclusivity
- any surviving patents
- a tradeable PRV, where the asset qualifies

**Why defensible.**
1. The claim is exclusive. Once you sign the asset purchase, nobody else can file that NDA.
2. The corpus is new: published CRLs only run from mid-2025, so no incumbent has a decade-long lead.
3. Learning compounds. Each resubmission outcome adds a label nobody else has joined to the letter text.
4. Speed. A 6-month Class 2 resubmission clock beats de novo development by years, so the first reader wins.

**Ceiling (numbers).**
- **Per asset:** PRV $150-200M at recent prices: Jazz $200M (Jan 2026), Abeona $155M (Jun 2025), Zevra $150M (Apr 2025) (https://www.lowenstein.com/news-insights/publications/client-alerts/congress-reauthorizes-pediatric-priority-review-voucher-program-in-fy2026-budget-renewed-incentives-for-rare-pediatric-drug-development-fdalife-sciences). A rescued orphan or specialty drug is typically worth $100M-$1B+ in peak sales.
- **Pipeline:** At 458 public CRLs with roughly 40-60% unapproved (assumption: the split is not published), and about 50-100 new CRLs a year, a realistic funnel is 5-15 actionable distressed assets a year.
- **Scale:** Ten approvals at $300M-$1B of enterprise value each is a $3-10B outcome. That is set by asset value, not by a software market.

**Who already does it (adversarial).**
- **Biossil:** generic failed-trial resurrection. Its news coverage never mentions CRLs; its 12 molecules are mainly Phase 2/3 efficacy misses such as senicapoc, rivipansel and ridinilazole. It is the closest threat and could pivot to this.
- **Zevra, Catalyst, Eton, Day One, Amneal and other specialty pharma:** they buy opportunistically but have no systematic reader.
- **XOMA and Concentra (Tang Capital):** they buy zombie biotechs for their cash and milestones, not for regulatory fixability. Concentra bought Kronos for $0.57 per share and then let Ignota take the assets.
- **Analytics vendors** (Clarivate, Citeline, CRL dashboards): they sell analytics and own nothing.

No ML-native "CRL-to-ownership" buyer turned up in my searches. This is the least crowded position I found in the lane.

**Killer risks.**
- FDA could stop publishing. The policy rests on agency discretion, not statute.
- Bad CRLs are bad for real reasons. The 28% clinical-deficiency share and redactions limit what the text reveals.
- Rescues need $20-150M each. This is a capital-heavy holding company (a Roivant-style "Vant" structure).
- Bigger players can copy it once two or three wins are public.
- The PRV program ends 30 Sep 2029 unless extended again. FDA has asked for permanence (https://www.pharmaceutical-technology.com/news/fda-seeks-permanent-future-for-rare-pediatric-priority-review-vouchers/).

**Concrete first proof (6-8 weeks, <$100k).**
1. Pull all openFDA CRLs from an unblocked network. LLM-code each deficiency into about 15 classes and hand-check 100 of them.
2. Join to Drugs@FDA to find which unapproved CRL'd applications have **no resubmission after 12+ months**. FDA may treat one-year inactivity as implicit withdrawal, which signals abandonment.
3. Join sponsor status from SEC/EDGAR.
4. Output: a ranked list of about 20 assets that combine a CMC/facility-only or single-question deficiency, a distressed or non-core owner, and orphan or RPD designation.
5. Back-test the fixability model on reconstructed pre-2025 letters, measured against actual later approvals.
6. Milestone: one signed LOI or option on an asset for under $3M upfront, plus a written CDMO or facility-swap plan.

---

## Candidate 2: US-naive molecules approved abroad, claimed through NCE and orphan exclusivity (score 6.5/10)

**Dataset and why it is public.** Regulators publish approvals and review reports by law or policy:
- PMDA review reports (Japanese)
- NMPA approvals (Chinese)
- MFDS (Korea)
- CDSCO (India)
- Russia's GRLS register
- EMA EPARs and national authorisations
- WHO prequalification and the Essential Medicines List

Compare these against Drugs@FDA and the Orange Book to find **active moieties with human approval and marketed-use data somewhere but no US approval**. Layer on:
- ClinicalTrials.gov, ICTRP and jRCT registries
- VigiBase/FAERS case counts, for safety maturity
- US epidemiology from CDC WONDER and published claims prevalence

**Anchor case: Harmony Biosciences.**
- Harmony licensed pitolisant from France's Bioprojet. Pitolisant was EU-approved in 2016 and US-approved as Wakix in 2019.
- WAKIX net revenue was **$868.5M in 2025**, and Harmony guides to **$1.0-1.04B in 2026** (https://www.businesswire.com/news/home/20260224164879/en/Harmony-Biosciences-Reports-Strong-2025-Financial-Results-and-Reiterates-2026-Net-Revenue-Guidance-of-Over-%241-Billion).
- The company was built on one licence of one drug approved abroad.

Similar cases (from memory, not re-verified this session):
- Catalyst/Firdapse: amifampridine, EU-approved first
- MediciNova/ibudilast: a Japanese asthma drug
- Radicava/edaravone: Japan first

**ML problem.**
- Multilingual extraction from heterogeneous regulatory documents (Japanese and Chinese review reports, Cyrillic registers) into a normalised table of molecule, indication, evidence strength and safety exposure.
- Entity resolution of salts, prodrugs and INN variants against US "active moiety" definitions. This decides NCE eligibility, which is a subtle legal-chemical mapping.
- Prediction of FDA acceptability of foreign data (ICH E5 bridging, ethnic sensitivity) and of US commercial value.

The hard part is resolution and judgement across messy multilingual sources, not search.

**What the company owns.**
- An exclusive US (or ex-originator-territory) licence: rivalrous, signed with the originator.
- On approval, **5-year NCE exclusivity**, if the moiety is new to the US, regardless of whether patents have expired.
- 7-year orphan exclusivity, if applicable.
- A tropical-disease PRV, if the indication is on the list. That program is permanent. Half of the 14 NTD vouchers to 2024 went to drugs already used in endemic countries, and the vouchers sold for $60-290M (https://pmc.ncbi.nlm.nih.gov/articles/PMC12911920).

**Why defensible.** The licence is exclusive and the FDA exclusivity is a regulatory monopoly. The originators are often small or regional firms with no US ambitions, so the asset is effectively unclaimed until someone signs.

**Ceiling.** One Wakix-class win is a ~$1B/yr revenue franchise. A portfolio of 3-5 smaller orphan wins at $100-300M/yr each is a multi-billion-dollar specialty company.

**Who already does it.**
- Specialty-pharma BD teams (Harmony, Catalyst, Eton, Zevra, Jazz) do this by hand.
- Big pharma and NewCo vehicles have crowded the China novel-asset licensing boom. That segment is **not** open.
- The open segment is the long tail of *old, approved, unglamorous* foreign molecules.
- No ML-native player identified (one search; low confidence).

**Risks.**
- Foreign originators increasingly file in the US themselves (the Mitsubishi model).
- The FDA may require new US trials, which raises cost.
- The tropical-disease PRV faces repeal or reform pressure (same PMC paper).
- Opportunities are fewer than in Candidate 1, and the ML edge is moderate.

**First proof (6 weeks).**
1. Build the "approved somewhere, never in the US" moiety table from EMA, PMDA and NMPA lists, aiming for several hundred moieties.
2. Score them for US unmet need and orphan or PRV eligibility.
3. Have a regulatory counsel review the top 10 for NCE eligibility.
4. Approach 3 originators.

Kill test: if fewer than 10 credible candidates survive legal NCE and orphan screening, fold this into Candidate 1 as a source feed.

---

## Candidate 3: PRV-yield overlay. Rare-pediatric and tropical vouchers from orphaned assets (score 5.5/10)

**Datasets.**
- FDA orphan designation database: thousands of designations, most never approved.
- RPD designation lists.
- gnomAD, ClinVar and OMIM, to match mechanism to a monogenic pediatric disease.
- ClinicalTrials.gov terminated and withdrawn studies.
- The CRL corpus.

**ML problem.** Match shelved mechanisms to rare pediatric diseases using genetic evidence. Drugs with human genetic support succeed about 2.6x more often (Minikel et al., Nature 2024; from memory). Then predict whether an approval can be won within the voucher window.

**What the company owns.** The asset licence, plus the **PRV, a transferable property right**. Under the Consolidated Appropriations Act 2026 (signed 3 Feb 2026) the program runs through **30 Sep 2029**, with recent sales at $150-200M (Lowenstein, above).

**Why it is only 5.5.**
- The window is short: about 3 years to designation and approval.
- BridgeBio, Zevra and dozens of rare-disease biotechs harvest vouchers the same way.
- Healx and Every Cure do the mechanism-to-disease matching.

It is best used as a value multiplier inside Candidate 1: arimoclomol's voucher alone was 10x its purchase price.

**First proof.** Flag every orphan- or RPD-designated asset in the CRL and terminated-trial sets. Estimate how many could reach approval before September 2029. If there are 5 or more, the PRV overlay alone justifies a fund-of-assets structure.

---

## Candidate 4: Veterinary field-of-use licences on shelved human assets (score 4.5/10)

**Datasets.**
- ClinicalTrials.gov terminated and withdrawn trials, and pharma "available for licensing" lists
- Ensembl/OMA orthology and AlphaFold DB, for dog and cat target conservation
- Species pharmacogenomics flags: dog MDR1, the cat's glucuronidation deficit
- FDA CVM Green Book
- The NCI Integrated Canine Data Commons

**ML problem.** Predict cross-species target engagement and PK and toxicity transfer for shelved human compounds.

**What the company owns.** An exclusive animal-health field licence (rivalrous) and, after approval, FDA CVM exclusivity.

**Precedents.**
- Aratana in-licensed RaQualia's EP4 antagonist and ghrelin agonist in 2011, which became Galliprant and Entyce (https://www.biospace.com/raqualia-and-aratana-therapeutics-sign-animal-health-licensing-agreement).
- Nexvet's caninised anti-NGF became Librela, under Zoetis.

**Why low.**
- Exits were small. Aratana went to Elanco for about $245M, Kindred Bio to Elanco for about $440M, and Nexvet to Zoetis for about $85M (all from memory, not verified).
- Zoetis's whole Dogs and Cats segment was $6.28B in 2025 (https://www.businesswire.com/news/home/20260211839882/en/Zoetis-Reports-Fourth-Quarter-and-Full-Year-2025-Results), and Librela/Solensia sales are now declining on safety concerns.
- **Anivive** (pet repurposing, $20M from Leonid), FidoCure/One Health, ImpriMed and Loyal occupy adjacent ground.
- The single-asset ceiling is about $100-500M/yr at best.

**First proof.** Screen about 500 terminated human assets for canine and feline conservation and PK flags, then sign one option for pain, dermatology or feline CKD. It is probably not multi-billion.

---

## Candidate 5: Responder-subgroup rescue from patient-level trial data (score 2.5/10; killed)

**Datasets.** Vivli, YODA and Project Data Sphere patient-level data.

**ML problem.** Find heterogeneous treatment effects in failed Phase 3 trials, then in-license the asset with a biomarker-enriched design.

**Why killed.**
1. **The Vivli DUA**, fetched at https://vivli.org/Vivli-Data-Use-Agreement:
   - It limits data use to the approved research plan and expects publication.
   - It requires the recipient to grant data contributors a **perpetual, royalty-free, non-exclusive licence** to new IP.
   - It gives contributors a **180-day option to negotiate an exclusive licence**.
   - The original sponsor therefore gets first claim on your discovery, which is the opposite of Terranox.
2. **Biossil's stated thesis** is exactly "molecules that failed but may work in specific patient groups or with better trial designs", backed by $223M and a $1B valuation. Lantern Pharma (oncology) and BioXcel also play nearby.

---

## Ideas killed for crowding (not written up)

| Idea | Who already holds it, or why it fails |
|---|---|
| Generic AI drug resurrection | Biossil, Ignota Labs, Healx, Every Cure (nonprofit), Roivant, BridgeBio |
| Metagenome antibiotics, AMPs, enzymes | de la Fuente lab, Phare Bio, Basecamp Research, Profluent. Antibiotic economics are broken (Achaogen); PASTEUR Act not law |
| Human-genetics target discovery | Regeneron Genetics Center, Alnylam, Maze, deCODE/Amgen. Target method-of-treatment patents are weak after *Amgen v. Sanofi* |
| Natural products | Enveda, Hexagon Bio, Brightseed |
| FAERS benefit signals on generic drugs | Skinny-label carve-outs leave nothing ownable |
| Paragraph IV and CGT 180-day first-filer exclusivity | Indian and global generic firms file on NCE-1 day; per-product value $10-50M |
| Novel herbicide and crop-protection modes of action | Moa Technology, Enko Chem, Micropep, AgPlenus |
| China novel-asset in-licensing | Big pharma and NewCo funds dominate |

## Sources
- https://open.fda.gov/apis/transparency/completeresponseletters
- https://intuitionlabs.ai/articles/fda-complete-response-letters-dataset
- https://www.pharmamanufacturing.com/industry-news/news/55314510/fda-to-publish-all-complete-response-letters-releases-batch-of-89
- https://www.biospace.com/kempharm-announces-strategic-acquisition-of-arimoclomol-from-orphazyme-expanding-its-rare-cns-diseases-pipeline
- https://www.pharmaceutical-technology.com/news/zevra-sells-priority-review-voucher-for-150m-to-support-drug-launches/
- https://www.sec.gov/Archives/edgar/data/0001434647/000143774925016452/ex_762500.htm
- https://www.lowenstein.com/news-insights/publications/client-alerts/congress-reauthorizes-pediatric-priority-review-voucher-program-in-fy2026-budget-renewed-incentives-for-rare-pediatric-drug-development-fdalife-sciences
- https://www.pharmaceutical-technology.com/news/fda-seeks-permanent-future-for-rare-pediatric-priority-review-vouchers/
- https://betakit.com/biossil-exits-stealth-with-70-million-usd-to-give-failed-medicines-a-second-chance/
- https://www.startupresearcher.com/news/openai-leads-usd153-million-round-for-biossil-at-usd1-billion-valuation
- https://www.fiercebiotech.com/biotech/summit-sells-failed-antibiotic-openai-backed-startup-105m-deal
- https://businesscloud.co.uk/news/former-3-5bn-valued-kronos-has-assets-acquired-by-ignota-labs/
- https://www.businesswire.com/news/home/20260224164879/en/Harmony-Biosciences-Reports-Strong-2025-Financial-Results-and-Reiterates-2026-Net-Revenue-Guidance-of-Over-%241-Billion
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12911920
- https://vivli.org/Vivli-Data-Use-Agreement
- https://www.biospace.com/raqualia-and-aratana-therapeutics-sign-animal-health-licensing-agreement
- https://www.businesswire.com/news/home/20260211839882/en/Zoetis-Reports-Fourth-Quarter-and-Full-Year-2025-Results
- https://pharmashots.com/20910/anivive-lifesciences-receives-20m-funding-from-leonid-capital-partners-to-develop-novel-programs-for-pets
