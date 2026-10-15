# Lane: materials, chemistry, manufacturing and industrial waste

Written 15 Oct 2026 for the eighth hunt (see BRIEF.md). Search budget used: 19 of 20 WebSearch calls,
all on prior-art and crowding checks. I fetched no government datasets. Data access is confirmed from
documentation only.

## Bottom line

Nothing in this lane reaches Terranox grade. The template only works where the asset is rivalrous
(first to claim wins) and the data edge comes before the claim. In materials and waste:

- **Patents on ML-found materials** are rivalrous, but the race is now crowded and well funded.
  Periodic Labs raised a $300M seed at $1.3B (Sep 2025) and was in talks at about $7B (Mar 2026).
  Lila is valued above $1.3B. Radical AI, CuspAI and Orbital are also in it. On top of that, materials
  claimed from ML predictions without lab work are weak after Amgen v. Sanofi (2023) on enablement.
  A newcomer has no data edge here, because every company in the race uses the same databases
  (Materials Project, OQMD, ICSD, NOMAD).
- **Waste with value in it** is real, but each valuable stream is already held by a consolidator.
  Steel-mill (EAF) dust is held by Befesa, red mud by ElementUS, gallium by Metallium and Flash Metals,
  coal ash by Eco Material, and battery scrap by Redwood and others.
- The best candidate left (C1) is a **hazardous-waste reclaimer that reads mandatory manifests better
  than anyone else**. Its defence is the permits it holds and exclusive feedstock contracts. That is
  real but slow, and the business is partly a service business. Score 5/10.

---

## C1. Mining the manifests: a reclaimer of hazardous industrial wastes that carry value. Score 5/10

**Datasets, and why they are public**
- **RCRA e-Manifest.** The 2012 e-Manifest Act requires it, and it has run since 30 Jun 2018. Every
  shipment of hazardous waste is recorded with:
  - the generator's EPA ID;
  - the EPA waste codes (F006 electroplating sludge, D-codes for metals, K061 EAF dust, and so on);
  - the quantity;
  - the transporter and the receiving facility (TSDF);
  - the final management-method code (H-code, for example H132 landfill, H040 incineration,
    H010/H020 metals or solvent recovery).

  The data is published through RCRAInfo public and its national downloads.
  ([EPA e-Manifest overview](https://rcrapublic.epa.gov/rcrainfoweb/action/modules/em/emoverview;jsessionid=056DBA46B10FFBA01D34F871DF778FD0), [R7 fact sheet](https://www.epa.gov/sites/default/files/2018-05/documents/r7-e-manifest-fact-sheet-general-public-may-2018.pdf))
- **RCRA Biennial Report.** RCRA §3002 requires it from large-quantity generators and TSDFs. It gives,
  per stream: form code, source code, management method, quantity and a free-text waste description.
  ([EPA Biennial Report](https://epa.gov/hwgenerators/biennial-hazardous-waste-report))
- **TRI Form R.** EPCRA §313 requires it. It reports the mass of each listed chemical, including metal
  compounds, transferred off-site, broken out by receiving facility and that facility's RCRA ID.
  ([TRI National Analysis](https://epa.gov/trinationalanalysis/releases-chemical-and-industry))
- **Supporting sources:** ECHO/NPDES discharge monitoring reports, state permit files and EU E-PRTR
  waste transfers (for a later expansion to the EU).

**The ML problem.** No public source gives the composition of a waste stream. A manifest says "F006,
14 t, sent to landfill". TRI says the same plant sent "3.1 t nickel compounds to RCRA ID X". The
Biennial Report free text says something like "Ni/Cu hydroxide filter cake from plating line". The model
has to:
1. **Match records.** Link entities across the three systems: different IDs, misspellings, parent
   companies.
2. **Estimate composition.** Infer the metal or solvent content of each stream from:
   - TRI mass ÷ manifest mass, where both exist;
   - industry type (NAICS), process and waste code, as priors;
   - NLP on the free-text descriptions;
   - a hierarchical Bayesian model that pools information across plants in the same industry.
3. **Price each stream.** Combine the estimated content with distance, metal prices and current
   disposal cost. The output is a ranked list of streams that are landfilled or stabilized today but
   would be worth more than zero if reclaimed.
4. **Spot capacity gaps.** Manifests show how far each kind of waste travels. Long hauls mean a region
   lacks treatment capacity, which tells you where to site a plant or which permit to buy.

**The model's core advantage:** incumbents price streams one sales call at a time. Nobody models the
whole national flow.

**What the company owns**
- **Exclusive multi-year feedstock contracts.** The generator pays less than its landfill fee, and the
  company keeps the recovered metal.
- **Reclamation plants.** Some can operate under the 2015/2018 Definition of Solid Waste rule's
  transfer-based exclusion (40 CFR 261.4(a)(24)), which lowers the permit burden for real recycling.
- **RCRA Part B permits.** Where a full TSDF is needed, the permit itself is the scarce, rivalrous
  asset. New permits take years to win.

**Why it is defensible**
- **Permits are scarce.** Clean Harbors' incinerators ran at 89% utilization in Q2 2025, and its
  average incineration price rose 7%. Kimball, the only new US commercial incinerator in decades,
  was still ramping up. ([Waste Dive](https://www.wastedive.com/news/clean-harbors-q2-2025-earnings-phoenix-hub-and-spoke/756319/))
- **Contracts lock in feedstock.** Once a plant's feedstock is under contract, a rival cannot easily
  take it.
- **The data model compounds.** Every sample analysed sharpens the composition model.

**Weakness, said plainly:** the data edge only decides which contracts to sign first. Incumbents can
copy the targeting once they see you winning streams.

**Ceiling**
- **Recent comparable deals:**
  - Veolia bought Clean Earth, a hazardous-waste business, for $3.0B in Nov 2025.
    ([Financier Worldwide](https://www.financierworldwide.com/fw-news/2025/11/25/veolia-acquires-enviris-clean-earth-in-3bn-deal))
  - Befesa paid $450M for American Zinc Recycling's EAF-dust plants in 2021.
    ([Recycling Today](https://www.recyclingtoday.com/article/befesa-american-zinc-recycling-acquisition-usa-eaf-steel-mill-dust/))
  - Clean Harbors is a public company worth roughly $10B+.
- **Plausible outcome:** a reclaimer focused on metals and solvents is worth $1-3B. That is
  multi-billion only if it grows into permitted treatment capacity, in effect a new Clean Harbors.
- **Waste volume:** US hazardous waste is about 30-40 Mt/yr by Biennial Report tonnage. Most of that
  is wastewater, so the solid streams that matter are a few Mt/yr. **I did not confirm the exact
  national total or the metal mass in landfilled streams.** Those two numbers are the first thing to
  compute from the downloads.

**Risk against the brief:** about half the revenue is tipping fees, which is a service. That partly
breaks the "ceiling set by asset value" test.

**Who already does it**
- **Incumbents:**
  - general hazardous-waste firms: Veolia with Clean Earth, Clean Harbors / Safety-Kleen, Heritage;
  - single-stream specialists: Befesa (EAF dust), Cronimet, Metallix, Sipi;
  - sludge recyclers: World Resources Co. (F006 sludge);
  - spent-catalyst recyclers: Johnson Matthey, Umicore, Heraeus.
- **Startups:** AI sorting firms such as WeSort.AI work on municipal and scrap sorting, not hazardous
  manifests. Metallium and Flash Metals target gallium from waste with DoD contracts
  ([Metal Tech News](https://www.metaltechnews.com/story/2026/04/08/tech-metals/metallium-achieves-pentagon-gallium-contract/2710.html),
  [Mining.com](https://www.mining.com/?p=1187167)).
- **Gap:** I found no one running national manifest-scale ML to source feedstock.
- **Streams to exclude:** EAF dust (Befesa), gallium (Metallium, Flash Metals), spent PGM catalysts
  (Johnson Matthey, Umicore, Heraeus), battery scrap (Redwood and others).

**Prospecting flag: low.** Reclaiming metals from waste that manufacturing produces today is recycling,
not geology. Avoid legacy piles (ash ponds, tailings, red mud), which Dhruv may count as prospecting.

**Concrete first proof (6-8 weeks, about $50k)**
1. Pull e-Manifest (2018-2025), Biennial Report (2019-2023) and TRI Form R from the public downloads.
2. Build the match-and-estimate model.
3. **Validate on held-out data.** Hide TRI metal masses for 20% of plant-to-facility pairs and predict
   them. Target: within ±30% for at least 60% of pairs.
4. Rank the top 50 streams that are landfilled today and carry the most estimated value.
5. Ask 10 generators for their waste profiles or SDS and assay 5 samples.
6. **Pass bar:** at least 3 streams with positive net value after transport, plus 2 letters of intent
   for exclusive offtake.

---

## C2. Buying stranded advanced-manufacturing plants out of bankruptcy, chosen by ML. Score 4/10

**Datasets, and why they are public**
- US bankruptcy dockets and claims-agent sites (Kroll, Stretto, Epiq). Asset schedules and sale
  motions are public by law. PACER charges a fee.
- The USPTO assignment database, which records who owns which patent and which patents are pledged.
- State air and water permits and NEPA filings for half-built plants.
- DOE Loan Programs Office and grant disclosures.
- The EU insolvency registers.

**The ML problem**
- Price the bundle of equipment, permits, site and patents in a distressed plant.
- More importantly, match each stranded asset to a **different product** it could make profitably.
  This means reasoning about process equipment: which reactors, kilns, dryers, cleanrooms and
  electrolysis halls suit which chemistries.

**What the company owns:** plants, permits and patent families bought at 2-10% of what they cost to
build.

**Rivalrous?** Partly. Each auction has a single winner.

**Ceiling.** The Lyten deal shows what is possible. Lyten bought the bankrupt Northvolt estate,
including Skellefteå, which it says was previously valued at about $5B. It used its own funds, and
the deal closed in Feb 2026. ([The Local](https://www.thelocal.se/20260108/whats-happening-with-the-american-takeover-of-swedens-northvolt))
The 2024-26 cleantech bust (batteries, electrolyzers, green steel, fuels) left many such estates.

**Who already does it**
- Lyten (battery strategic buyers);
- distressed private-equity funds;
- liquidators;
- patent aggregators (RPX, Intellectual Ventures).

**Why only 4/10**
- ML is not the hard or decisive part. Winning the asset depends on having a product and an operating
  team to restart the plant.
- Taking it further belongs to the industrial or finance lane, not this one.

**First proof:** list every US/EU cleantech manufacturing bankruptcy from 2023-26 with asset sales.
Compare sale price with capital spent, and show whether a repurposing model would have found any sale
that later proved valuable.

---

## C3. Patents on substitutes that regulation forces industry to adopt (PFAS, Cr(VI), REACH Annex XIV). Score 4/10

**Datasets, and why they are public**
- **The EU universal PFAS restriction dossier and its consultations.** The 2023 consultation drew
  more than 5,600 submissions in which companies said, use by use, where no alternative exists.
  - RAC's final opinion came on 2 Mar 2026.
  - SEAC's draft opinion opened a consultation that closed on 25 May 2026; its final opinion is due
    end-2026.
  - SEAC **rejects derogations for fluoropolymers and volatile PFAS** and proposes 5- or 12-year
    transitions.

  ([Linklaters](https://sustainablefutures.linklaters.com/post/102mp62/eu-universal-pfas-restriction-process-enters-its-decisive-phase-seac-draft-opin))
- **REACH authorisation applications.** These are public and include "Analysis of Alternatives"
  documents.
- **TSCA §6 rules.**
- **Patent full text,** used to map what is already claimed.
- **PubChem and quantum-chemistry property sets.**

**The ML problem**
1. **Build a demand map.** Use NLP to turn thousands of industry submissions into a list of each
   function with no substitute and the specification it must meet. Example: a photoacid generator
   (PAG) with pKa below X and transparency at 193 nm or EUV.
2. **Design candidates.** Run inverse design that respects those constraints, and check each candidate
   against existing patent claims.

**What the company owns:** composition-of-matter and use patents on the substitutes. It then licenses
them or makes the material.

**Rivalrous?** Yes, patents are first-to-file.

**Defensibility:** 20-year patents, with demand forced by law.

**Ceiling, and why it is weaker than it looks**
- The biggest PFAS uses are refrigerants (HFOs) and fluoropolymers (PTFE, PVDF, FKM), together roughly
  $10B+ a year.
- **Refrigerants:** NIST screened about 60k candidate molecules (McLinden et al., Nature Comms 2017).
  The usable low-GWP ones are nearly all fluorinated olefins. Natural refrigerants (CO2, propane) are
  winning and cannot be patented.
- **Fluoropolymer replacements** are mostly reformulation work that the material makers already do.
- **The cleanest target, PFAS-free PAGs for chip lithography,** is a market of only a few hundred $M.
  It is also being run by imec with resist makers since 2023
  ([PFAS Central](https://pfascentral.org/news/removing-pfas-from-semiconductor-manufacturing-from-resists-to-rinses);
  [Sanyo Chemical PFAS-free PAG](https://www.sanyo-chemical.co.jp/eng/wp/wp-content/uploads/2025/06/k20250624_1_e.pdf)).

**Who already does it**
- IBM (MatGFN-PFAS, NeurIPS 2023), [link](https://research.ibm.com/publications/matgfn-pfas-an-ai-driven-approach-for-toxic-pfas-replacement)
- Citrine, which sells PFAS reformulation as a service ([Citrine](https://citrine.io/removing-pfas-from-adhesives/))
- CuspAI with Kemira, AI-designed MOFs for PFAS removal (May 2026), [Kemira](https://www.kemira.com/newsroom/new-ai-designed-materials-show-promising-potential-to-remove-forever-chemicals/)
- Resist makers: JSR, TOK, Fujifilm, Shin-Etsu, DuPont
- Ionomer makers such as Ionomr

**Why only 4/10:** the clever part is the demand map built from the consultation, and it is copyable.
The chemistry is held by incumbents.

**First proof:** parse all 5,600+ 2023 submissions plus SEAC's derogation tables. List the uses with no
substitute that SEAC refused to derogate, and size each one. For the top 3 uses, show that no patent
family covers a feasible non-PFAS substitute.

---

## C4. A second plant for chemicals made at only a few sites. Score 3/10

**Datasets, and why they are public**
- EPA Chemical Data Reporting (TSCA §8(a)): production volume by site, partly withheld as
  confidential business information (CBI).
- TRI.
- US customs manifests. These are public under 19 CFR 103.31 and resold by Panjiva and ImportGenius.
- FDA Drug Master Files (DMF) list.
- REACH registration tonnage bands.
- DLA and DoD industrial-base reports.

**The ML problem:** match entities and infer missing links in the supply graph, to find chemicals made
at one or two sites worldwide that critical buyers depend on.

**What the company owns:** the plant plus government-backed offtake (DPA Title III, Office of Strategic
Capital, DoD contracts).

**Why it fails the test**
- **Government awards go to incumbents.**
  - Nitradyn, a joint venture of Dyno Nobel and Paligen, won $581M for an IMX-104 plant (Sep 2026).
    ([Defense Post](https://thedefensepost.com/2026/09/14/nitradyn-insensitive-munitions-production-kentucky/))
  - Repkon won the Army's TNT plant ($404M+).
    ([Defence Blog](https://defence-blog.com/u-s-army-commits-404m-to-build-its-first-tnt-plant-since-the-1980s/))
- **Startups are already working on reshoring:** Vulpes, Solugen, Phlow, and Scimplify and Atomgrid in
  India.
- **The ML adds little:** buyers already know which of their suppliers is a single source.
- **Each chemical is small:** most are $50-500M markets.

---

## C5. Harvesting coal ash found through CCR disclosures. Score 2/10, killed

**Dataset:** under the CCR rule (40 CFR 257.107), utilities must post on public websites:
- groundwater monitoring results;
- closure plans;
- impoundment volumes.

**The ML problem:** parse hundreds of PDFs to predict which ponds will be closed by removal, then
contract to harvest the ash for cement.

**Why killed:** Eco Material Technologies already has multi-site harvesting deals with Southern Co.,
including about 18 Mt in Georgia and North Dakota.
([Concrete Products](https://concreteproducts.com/?p=30910)) SEFA, Charah, Holcim and Heidelberg are
also in.

**Prospecting flag:** recovering rare earths, gallium or germanium from ash or red mud **is close to
prospecting** under Dhruv's rule. It is also taken: ElementUS and Metallium on Gramercy red mud, and
ElementUSA with Colorado School of Mines on DOE funding (Jun 2026)
([Mining Weekly](https://www.miningweekly.com/article/colorado-school-of-mines-elementusa-awarded-us-gov-funding-to-recover-rare-earths-from-alumina-tailings-2026-06-03)).

---

## Kill list (checked, do not re-pitch)

| Idea | Killed by |
|---|---|
| ML discovery of materials and catalysts in general | Periodic Labs ($300M seed, about $7B talks Mar 2026), Lila (>$1.3B), Radical AI, CuspAI, Orbital, Mattiq, Dunia, Citrine, Microsoft Azure Quantum with PNNL; plus the Amgen enablement risk for patents on predicted materials |
| Solid electrolytes and battery cathode whitespace | Chemix, Aionics, SES AI, Mitra Chem, CATL's patent thickets |
| REE-free magnets | Niron, Materials Nexus |
| Red mud (scandium, gallium) | ElementUS, Metallium ($10M deal) |
| Gallium and germanium from waste | Metallium and Flash Metals USA (DoD contracts), Nyrstar Clarksville |
| Tailings and low-grade leaching | Phoenix Tailings, Jetti, Nuton (Rio Tinto); also prospecting-flagged |
| EAF dust (zinc) | Befesa owns the US capacity (AZR, $450M) |
| Spent PGM and hydroprocessing catalysts | Johnson Matthey, Umicore, Heraeus, Eramet |
| Slag and CO2 mineralization | Fortera, Brimstone, CarbonBuilt, Carbon Upcycling |
| Sodium sulfate from cathode plants | Aepnus |
| PFAS destruction | 374Water, Aclarity, Revive, Claros, Onvector |
| Low-GWP refrigerants | NIST screen shows the space is exhausted; natural refrigerants cannot be patented |
| Exclusive licences on unlicensed university or federal patents | Tekcapital (an AI-led version that stays small-cap), Allied Minds (collapsed) |
| Expired or abandoned patents | Already public domain, so nothing to own |
