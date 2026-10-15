# Round 2 lane: regulatory first-filer claims in drugs, devices and agrochemicals

Written 15 Oct 2026. I used 18 of 20 WebSearch calls plus about 15 fetches.

**Data access.**
- The proxy blocked `api.fda.gov` and `www.accessdata.fda.gov` (CONNECT 403). I could not pull live counts
  from the NDC directory, so every NDC-count statement below comes from documentation or from memory and
  is marked as such.
- Anything marked **(memory)** is my own knowledge and was not re-checked in this run.

**Scope.** CRL rescue and in-licensing of foreign-approved drugs are excluded, per redteam_drugs.md. They
appear below only where a first-filer regime is a different mechanism.

## Verdict

Health and agriculture do have first-filer regimes, and one of them gives real legal exclusion: **the first
NDA for an old drug that is marketed without approval.** In that case FDA's enforcement discretion clears
the unapproved rivals off the market.

None of these regimes passes the Terranox test from ROUND2.md:

1. **The claim is not cheap.** A filing costs $5-50M and takes 2-4 years, plus PDUFA fees, against
   dollars a hectare for a mineral claim.
2. **The data is not illegible.** The NDC directory literally has a "marketing category" field that
   labels each product as UNAPPROVED. Finding candidates is a lookup.
3. **The exclusion is policy discretion, not a property right.** HHS tried to abolish the Unapproved Drugs
   Initiative in 2020, Vizient, the AHA and Congress attack it on price, and FDA has softened it case by
   case (thyroid in 2025-26).
4. **It is already farmed** by a known cohort of specialty and injectables firms.

The best of the lane is **5/10**: a disciplined unapproved-drug and orphan "first approval" filer, with ML
as triage rather than as the moat. Ag-chem and devices score 1-2 because their regimes compensate first
filers or protect them only for genuinely new active ingredients. They do not exclude followers.

## Scores

| # | Idea | Score |
|---|---|---|
| 1 | First NDA for a marketed unapproved drug | 5 |
| 1b | Animal-derived (desiccated) thyroid race | 3 for a newcomer |
| 2 | 505(b)(2) 3-year exclusivity; paediatric formulations (US and EU PUMA) | 3 |
| 3 | QIDP/GAIN 5-year add-on | 2 |
| 4 | Device De Novo | 1 |
| 5a | EPA FIFRA data compensation | 2 |
| 5b | EU REACH lead registrant | 1 |
| 5c | EU BPR Article 95 / EU plant-protection data protection | 2 |
| 6a | Competitive Generic Therapy (CGT) 180-day exclusivity | 3 |
| 6b | Paragraph IV first-filer 180-day exclusivity | 1 |
| 6c | Tropical-disease PRV on owner-free old molecules | 4 |
| 6d | Orphan exclusivity on an off-patent old drug (first approval for a disease) | 4 |
| 6e | OTC monograph order request (OMOR) 18-month exclusivity | 2 |

---

## 1. First NDA for a marketed unapproved drug (score 5)

### The mechanism
- Many pre-1938 and DESI-era drugs are sold without approval. Under CPG 440.100 (2006, revised 2011),
  when one firm wins an NDA for such a drug, FDA usually gives the unapproved marketers about a **one-year
  grace period** and then treats their products as enforcement priorities.
- The first approved firm gets a de facto monopoly until a second NDA or an ANDA referencing it arrives.
  It also gets formal exclusivity where it qualifies:
  - 3-year exclusivity if new clinical investigations were essential to approval
  - 7-year orphan exclusivity
  - patents on formulations
- Sources: [DrugPatentWatch summary](https://www.drugpatentwatch.com/blog/unapproved-drugs-opportunities-rapid-approval-market-exclusivity/),
  [Hogan Lovells](https://hlc.com/en/publications/in-sharp-rebuke-to-trump-administration-hhs-notice-ending-unapproved-drugs-initiative-is-withdrawn).

### Precedents with numbers
| Drug | What happened | Value |
|---|---|---|
| Colchicine (URL Pharma, Colcrys, 2009) | Approved with 3-year exclusivity, plus orphan exclusivity for FMF (memory). Price went from about $0.09 to about $5.00 per tablet. | URL Pharma sold to Takeda for about $800M in 2012 (memory) |
| Vasopressin (JHP, then Par; Vasostrict, 2014) | Monopoly for about 8 years | Annual US spend rose from $30.8M to $791M (2020) |
| Neostigmine (Éclat/Avadel, Bloxiverz, 2013) | First approval | Spend rose from $60.6M/yr to about $205.8M/yr |
| Dehydrated alcohol | First approval | $28M to $215M/yr |
| Selenious acid (American Regent) | First approval | $8.5M to $84.9M/yr |
| Tralement trace elements (American Regent) | First approval | +$100M over its exclusivity |
| Ephedrine (Éclat's Akovaz, 2016, memory) | Shows the weakness: with no 3-year exclusivity, Par (Corphedra), Nexus (Emerphed) and Eton (Rezipres) followed with their own 505(b)(2)s within a few years, and the monopoly collapsed | — |

Sources for the spend figures: [Vizient via HPN](https://www.hpnonline.com/sourcing-logistics/lab-pharmacy-supply-management/article/21164057/vizient-analysis-shows-ending-unapproved-drugs-initiative-could-save-between-752-billion-and-2659-billion).

**Evidence base of these approvals.** In an observational study of 34 drugs targeted by the UDI between 2006
and 2015, 19 later had approved products. **17 of those 19 (89%) were approved on literature,
bioequivalence data or both, without new trials.** Prices rose by a median of 37%, or 122% for the 10
approved products directly ([PMC10397719](https://pmc.ncbi.nlm.nih.gov/articles/PMC10397719)). So the
claim is cheap by pharma standards: about $5-20M in CMC, bioequivalence and literature work, plus the PDUFA
fee (memory: about $4M for an application with clinical data), over roughly 2-3 years.

### Status of the Unapproved Drugs Initiative in 2026
- **Policy history:**
  - HHS terminated the UDI on 20 Nov 2020.
  - HHS and FDA withdrew that termination on 27 May 2021 (86 FR 28422). The risk-based CPG approach was
    restored ([Hogan Lovells](https://hlc.com/en/publications/in-sharp-rebuke-to-trump-administration-hhs-notice-ending-unapproved-drugs-initiative-is-withdrawn)).
  - The promised new guidance on the "de facto exclusivity" period had not been issued by April 2026. No
    reform has been enacted (DrugPatentWatch).
- **Recent actions:** FDA's action list ([FDA](https://www.fda.gov/drugs/enforcement-activities-fda/fda-actions-remove-unapproved-drugs-market-drug))
  covers 13 drug classes. The newest are:
  - **Animal-derived thyroid** (Aug 2025, with a follow-up notice on 11 Mar 2026 and an industry letter
    on 5 Aug 2026)
  - iodoquinol (Dec 2024)
  - potassium phosphates injection (Aug 2024)
  - NSAIDs: salsalate and choline magnesium trisalicylate (2022)
  - isoxsuprine (2021)
- **Assessment:** the program is alive but slow, with about one class a year, and politically contested.

### Pool size
- **Vizient (Nov 2020)** identified **18 remaining unapproved drugs** that could still be approved through
  the program, adding **$7.52B** of US cost over 5 years of exclusivity, roughly $80M a year per drug on
  average. Approvals of five earlier drugs had already added $3.15B
  ([HPN](https://www.hpnonline.com/sourcing-logistics/lab-pharmacy-supply-management/article/21164057/vizient-analysis-shows-ending-unapproved-drugs-initiative-could-save-between-752-billion-and-2659-billion)).
  Some of those 18 have since been taken, e.g. potassium phosphates.
- **NDC directory "UNAPPROVED DRUG OTHER"** (also "...FOR USE IN DRUG SHORTAGE", "UNAPPROVED MEDICAL GAS"
  and "UNAPPROVED HOMEOPATHIC"). I could not fetch the counts (blocked).
  - My estimate (memory, unverified) is **low thousands of listings**. Most are Rx vitamins and prenatal
    vitamins, fluoride, topicals, urinary analgesic and antiseptic combinations (hyoscyamine,
    methenamine/methylene blue, phenazopyridine), oral phenobarbital, opium tincture and the like.
  - Most of these are commodity products with thin dollars.
  - The obvious high-value injectables (vasopressin, ephedrine, phenylephrine, neostigmine, trace
    elements, cysteine, ascorbic acid, phosphates, dehydrated alcohol) **are already taken**.
- **Old FDA estimate:** in 2006 FDA put unapproved products at up to 2% of US prescriptions.

### Who already farms it
Par/Endo (now merged with Mallinckrodt, memory), Exela/Éclat, American Regent (Daiichi), Nexus, Eton,
Fresenius Kabi, Hikma, Provepharm (methylene blue), McGuff (ascorbic acid), Belcher and BPI Labs
(epinephrine), Avadel (exited; sold its hospital products to Exela, memory) and Acella (thyroid).
503B outsourcers (Nephron, QuVa) supply the shortage side, but they hold no claim.

### Is ML on public data an edge?
Partly, but not decisively.
- **The useful model** joins three public sources:
  - NDC listings (marketing category, labeler, SPL label text)
  - Medicaid State Drug Utilization Data and Part D spend by NDC, to size each molecule
  - Literature, to predict whether a no-new-trial 505(b)(2) is feasible
- **What it predicts:**
  - P(enforcement or grace period)
  - P(a second filer within 3 years), which turns on whether 3-year exclusivity is attainable
- **Why it is not a moat.** The candidate set is short and labelled. Vizient, the generic firms'
  business-development teams and DrugPatentWatch already publish it, so the edge is execution speed plus
  formulation and CMC.
- **Why 5:** the legal mechanism genuinely excludes followers, and the per-asset economics (up to $800M
  exits) are proven. The score is capped by policy risk, a picked-over pool and the lack of an ML edge.

## 1b. Animal-derived (desiccated) thyroid: the live race (score 3 for a newcomer)
- **Size.** About **1.5M US patients** received animal-derived thyroid prescriptions in 2024, against 22M
  on levothyroxine ([FDA page dated 6 Aug 2026](https://www.fda.gov/drugs/enforcement-activities-fda/fdas-actions-address-unapproved-thyroid-medications)).
  My revenue estimate is about $0.4-0.8B a year at retail (not published).
- **Regulatory status.** FDA planned about 12 months of enforcement discretion. It promised draft guidance
  "before August 2026", and that guidance was still not issued as of the 5 Aug 2026 industry letter
  ([FDA letter](https://www.fda.gov/media/191621/download)).
- **The race.**
  - Acella (NP Thyroid) planned Phase 3 dosing for Feb 2026 and calls the product a "biologic drug". If
    it is licensed as a BLA, the first approval could carry 12-year reference-product exclusivity. That is
    my inference and is unverified.
  - AbbVie (Armour) has not committed to filing
    ([PharmaVoice, Oct 2025](https://www.pharmavoice.com/news/dte-fda-makary-drug-abbvie-hypothyroidism-acella/803137/)).
- **Assessment.** This is the largest live first-filer prize in the category. Two incumbents are already
  ahead, a Phase 3 is needed, and FDA keeps signalling "ensure access", so the exclusion may be softened.
  It is not winnable by a newcomer from data.

## 2. 505(b)(2) first-filer 3-year exclusivity, including paediatric formulations (score 3)

**US 3-year exclusivity.**
- **What it protects:** the specific change (new formulation, route, indication or population), and only
  when new clinical investigations (not bioavailability studies) were essential to approval.
- **What it does not protect:** it does not block other formulations, the old drug, or a rival that runs
  its own trials (memory, statute 505(c)(3)(E)(iii)).
- **Volume:** about 69 reformulation approvals in 2024-25 ([MedPath](https://trial.medpath.com/news/2c86f6856832466d/fda-505-b-2-pathway-drives-69-drug-reformulations-in-2024-2025-focusing-on-stability-and-patient-experience)).

**Paediatric incentives.**
- **US paediatric exclusivity:** a 6-month add-on that attaches only to existing patents or exclusivity.
  It is worthless on a bare off-patent molecule.
- **Eton, the best pure-play proof:** 10 commercial rare and paediatric products. FY2025 revenue was
  **$80.0M** (2024: $39.0M) and 2026 guidance is **>$110M**
  ([8-K](https://www.sec.gov/Archives/edgar/data/1710340/000143774926009060/ex_889836.htm)). The model
  works, but it is small.
- **EU PUMA (paediatric-use marketing authorisation):** 8+2 years of data and market protection for an
  off-patent drug in a paediatric formulation. Only 3 PUMAs had been granted after 10 years
  ([RAPS](https://www.raps.org/resource/10-years-in-eu-pediatric-use-marketing-authorizat.html)), and the
  count is still in single digits or low teens (memory). Uptake is poor because national pricing does not
  reward on-label paediatric versions.

**Who farms it.** Every specialty pharma, with Camargo-type consultancies selling the playbook.

**ML edge.** Low: off-label paediatric use, which is visible in claims and FAERS, is known to clinicians
and BD teams. The exclusion is narrow and the ceiling per product is $10-100M.

## 3. QIDP/GAIN 5-year add-on (score 2)
- **The incentive:** 5 years stacked onto NCE, 3-year or orphan exclusivity, plus priority review and fast
  track. An old moiety could in principle reach 3+5 = 8 years.
- **In practice, every QIDP approval so far has been an NME** (FDA, via [Camargo](https://camargopharma.com/resources/blog/qidp)).
  101 of 109 designation requests were granted in 2012-15, but only 6 approvals followed in that period.
- **The economics are broken** (memory):
  - Achaogen, Melinta and Nabriva went bankrupt or wound down. Nabriva's Contepo, IV fosfomycin and an
    old moiety, got repeated CRLs.
  - The PASTEUR Act has not passed.
- **Assessment.** Exclusivity is worthless when hospital antibiotic volumes are small and stewardship-capped.
  ML on resistance surveillance data does not change the payoff.

## 4. Medical devices: De Novo (score 1)
- **No exclusivity of any kind.** A De Novo grant creates a new classification regulation and makes the
  device **a predicate that any follower can cite in a 510(k) immediately**. The first mover pays the
  evidence cost and followers ride it.
- **Volume:** grants run at roughly 30-60 a year (memory).
- **Where protection does come from:** patents, CMS coverage and codes (TCET, NTAP, not exclusive), and
  brand. PMA approval likewise gives no data exclusivity, except a 6-year bar on citing the PMA's data
  (memory).
- **Conclusion:** first filing is a cost, not a claim. Dead.

## 5. Agrochemicals and industrial chemicals

### 5a. EPA FIFRA data compensation (score 2)
- **New active ingredients:** 10-year **exclusive use** of the data
  (FIFRA §3(c)(1)(F)(i), memory; up to 3 more years for minor uses).
- **After that:** a 15-year compensable period in which me-too registrants cite the data by "offer to
  pay", with binding arbitration. *Thomas v. Union Carbide*, 473 U.S. 568, upheld the scheme
  ([Cornell](https://www.law.cornell.edu/supremecourt/text/473/568)). After 15 years the data are free.
- **What the first registrant of an off-patent active gets:** cost-sharing, **not exclusion**.
  Data-call-in task forces split costs. Generic houses (Albaugh, Sharda, UPL, ADAMA, Rotam, Willowood)
  farm it.
- **ML edge:** none worth a company.

### 5b. EU REACH lead registrant (score 1)
- Data sharing is mandatory on fair, transparent and non-discriminatory terms (Implementing Regulation
  2016/9, memory). The lead registrant only recovers costs by selling letters of access. It is a
  cost-recovery club, not a claim.

### 5c. EU BPR Article 95 and plant-protection data protection (score 2)
- **Article 95 does exclude:** a biocidal product may contain an active substance only from a supplier on
  the Article 95 list, and listing requires your own dossier or a letter of access
  ([KemI](https://www.kemi.se/en/pesticides-and-biocides/biocidal-products/rules-for-biocidal-products/article-95-list),
  [Steptoe](https://www.steptoe.com/a/web/6102/3ZEtyX/article-95-and-beyond.pdf)).
- **But the positions are owned.** They belong to the incumbent dossier holders and task forces of the
  2000s review programme, and data protection on "existing" substances is expiring.
- **Plant protection (1107/2009):** 10 years of data protection for new actives and 30 months for renewal
  data (memory). Again, these protect new data, not first filing on old actives.

## 6. Other first-filer regimes in health

### 6a. Competitive Generic Therapy 180-day exclusivity (score 3)
- **The incentive:** the first approved ANDA for a CGT-designated drug with "inadequate generic
  competition" gets 180 days of exclusivity, provided it launches within 75 days.
- **FDA publishes the target list:** the Off-Patent, Off-Exclusivity List.
- **Volume:** **527 CGT approvals** to date. At least 46 were dated 2025 and 68 so far in 2026 (latest 28
  Sep 2026, Upsher-Smith prednisolone ophthalmic)
  ([FDA](https://www.fda.gov/drugs/generic-drugs/competitive-generic-therapy-approvals)).
- **Assessment:** heavily farmed (Upsher-Smith, Amneal, Zydus, Lupin, Hikma and others), small markets,
  only 6 months of protection.
- **ML edge:** modest. A model could predict which list items will draw a second entrant late, and which
  have reachable API or complex-formulation barriers.

### 6b. Paragraph IV first-filer 180-day exclusivity (score 1)
Firms line up on the NCE-minus-1 day and share the exclusivity. It is the most farmed first-filer regime
in pharma.

### 6c. Tropical-disease PRV on owner-free old molecules (score 4)
This is distinct from the excluded in-licensing idea when no licence is needed.
- **The incentive:** the first US approval of a qualifying drug for a listed tropical disease earns a
  transferable PRV. The program is permanent, with no sunset.
- **Track record:** 14 vouchers were awarded 2009-2023. Sale prices:
  - $98M (Lampit)
  - $103M (Ixchiq)
  - $125M (Impavido)
  - $290M (Vaxchora)
  - Bavarian Nordic's Vimkunya voucher at $160M (Jun 2025)
  - Sources: [FDA Law Blog](https://www.thefdalawblog.com/2025/02/can-the-tropical-prv-have-its-moment-again-not-all-priority-review-vouchers-are-created-alike-what-the-potential-loss-of-the-rare-pediatric-prv-could-mean-for-the-tropical-disease-prv-pr/),
    [Fierce](https://www.fiercepharma.com/pharma/bavarian-nordic-sells-priority-review-voucher-chikungunya-vaccine-approval-160m).
- **Eligibility:** the active ingredient must never have been approved in the US (memory; FDARA-era
  tightening).
- **Candidates (memory):**
  - CDC Drug Service IND drugs: sodium stibogluconate, melarsoprol, suramin, diethylcarbamazine
  - Approved-abroad antimalarials and anthelmintics: pyronaridine-artesunate, tribendimidine
- **Pool:** perhaps **5-15 molecules**. They are enumerable by hand, with no ML edge, and each needs
  US-grade CMC plus, often, a trial.
- **Assessment:** a good overlay, not a company.

### 6d. Orphan exclusivity on an off-patent old drug (score 4)
- **The incentive:** the **first approval** of a drug for a rare disease gets 7 years of exclusivity for
  that disease. Designation alone gives nothing; first to approval wins.
- **Precedents:** colchicine for FMF, amifampridine (Catalyst over Jacobus), deflazacort.
- **The public queue:** the FDA orphan designation database lists every competitor.
- **The ML angle** that is more than a lookup: mining literature and claims for an off-label old drug with
  strong case-series evidence in a rare disease, where nobody holds a designation. It is real but thin,
  and the "Firdapse backlash" pricing risk is high.

### 6e. OTC monograph order request 18-month exclusivity (score 2)
The CARES Act 2020 reformed OTC monographs. A requestor whose order needed new clinical investigations gets
18 months of exclusivity (memory). The volume is tiny (e.g. new sunscreen filters) and the protection is
short.

## Why this lane does not produce a Terranox
1. **Claim cost.** An NDA or BLA costs $5-50M and takes years. FIFRA, REACH and De Novo first filers pay
   for data that followers then cite.
2. **Data legibility.** Every first-filer target list is published and labelled:
   - FDA's off-patent/off-exclusivity list
   - the NDC marketing category
   - the orphan designation database
   - the tropical PRV disease list
   - the Vizient list of 18 drugs

   ML ranks candidates. It does not discover them.
3. **The exclusion is discretionary and political.** The most valuable exclusion, unapproved-drug
   enforcement, is FDA policy that HHS once tried to kill and that payers lobby against.
4. **Incumbents farm every regime:**

   | Regime | Incumbents |
   |---|---|
   | Unapproved injectables | Par/Endo, Exela, American Regent, Nexus |
   | Paediatric formulations | Eton |
   | CGT | The generic houses |
   | FIFRA | The ag-chem generics |

**If pursued at all:** treat it as the **"first approval" specialty pharma** already sketched in
redteam_drugs.md. Unapproved-drug NDAs, orphan first approvals and tropical PRVs would be its feedstocks,
with Medicaid SDUD × NDC × label-text ML used for triage. It fits "own the asset", but not "ML is the edge"
or "unattackable".

## Sources
- https://hlc.com/en/publications/in-sharp-rebuke-to-trump-administration-hhs-notice-ending-unapproved-drugs-initiative-is-withdrawn
- https://www.drugpatentwatch.com/blog/unapproved-drugs-opportunities-rapid-approval-market-exclusivity/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10397719
- https://www.hpnonline.com/sourcing-logistics/lab-pharmacy-supply-management/article/21164057/vizient-analysis-shows-ending-unapproved-drugs-initiative-could-save-between-752-billion-and-2659-billion
- https://www.fda.gov/drugs/enforcement-activities-fda/fda-actions-remove-unapproved-drugs-market-drug
- https://www.fda.gov/drugs/enforcement-activities-fda/fdas-actions-address-unapproved-thyroid-medications
- https://www.fda.gov/media/191621/download
- https://www.pharmavoice.com/news/dte-fda-makary-drug-abbvie-hypothyroidism-acella/803137/
- https://www.fda.gov/drugs/generic-drugs/competitive-generic-therapy-approvals
- https://camargopharma.com/resources/blog/qidp
- https://www.raps.org/resource/10-years-in-eu-pediatric-use-marketing-authorizat.html
- https://www.sec.gov/Archives/edgar/data/1710340/000143774926009060/ex_889836.htm
- https://trial.medpath.com/news/2c86f6856832466d/fda-505-b-2-pathway-drives-69-drug-reformulations-in-2024-2025-focusing-on-stability-and-patient-experience
- https://www.thefdalawblog.com/2025/02/can-the-tropical-prv-have-its-moment-again-not-all-priority-review-vouchers-are-created-alike-what-the-potential-loss-of-the-rare-pediatric-prv-could-mean-for-the-tropical-disease-prv-pr/
- https://www.fiercepharma.com/pharma/bavarian-nordic-sells-priority-review-voucher-chikungunya-vaccine-approval-160m
- https://www.law.cornell.edu/supremecourt/text/473/568
- https://www.kemi.se/en/pesticides-and-biocides/biocidal-products/rules-for-biocidal-products/article-95-list
- https://www.steptoe.com/a/web/6102/3ZEtyX/article-95-and-beyond.pdf
