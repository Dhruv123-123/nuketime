# Round 2: catalogue of cheap, first-come legal claim regimes outside mineral tenure

Written 15 Oct 2026. Web searches used: 16 of 20, plus fetches. Figures marked (memory) come from my own
knowledge and were not re-checked in this run. Government hosts (fda.gov, itu.int SNL, api.fda.gov) were
mostly not fetched. Where I say a dataset exists, I checked its documentation, not a live pull.

## Verdict first

There is no clean Terranox outside geology. Across about 50 regimes, the four-part law in ROUND2.md almost
never holds at once. The regimes split into three groups:

1. **Cheap and first-come, but the asset is worthless until you build or prove something expensive.**
   Examples: new ITU filings, FERC preliminary permits, Chinese utility models, patents, Nepal and
   Philippines energy survey contracts, domains.
   The claim works like Terranox. Condition (3) fails unless you also pay to develop the asset.
2. **The asset is worth far more than the claim, but the claim is not cheap.** Examples: the first
   approval of an old unapproved or compounded drug, a priority review voucher (PRV), orphan exclusivity
   on an old molecule, a PMA part, a freighter-conversion STC.
   The "claim" is a $3-50M regulatory dossier, so it looks like specialty pharma or aerospace, not
   staking.
3. **The asset can only be gained by the incumbent or by a qualified operator.** Examples: SPCs,
   paediatric exclusivity, broadcast and landing rights, cable landing, GIs.

**The best fit is buying dormant satellite priority, not filing it.** That means senior ITU MSS
filings in L- and S-band, plus the national MSS licences of failed or dormant satellite companies.
**Score 6/10.** One new fact raised it from "paperwork" to a real arbitrage:
- Sky and Space Global was a failed UK nanosatellite company.
- Its old S-band ITU priority sat in a shell that two people in Texas set up in 2025 (EllioSat).
- AST SpaceMobile bought that shell in August 2025 for $26M upfront and up to ~$46-64.5M in total.
- ITU Resolution 35's deployment milestones do **not** cover L- or S-band, so filings this old survive
  once they have been brought into use.

That is the nearest thing to "stake the claim nobody is reading". Two problems keep it at 6:
- The pool is finite: a few dozen senior, live filings.
- The buyers are three or four strategics (SpaceX, Amazon, AST, Rocket Lab/Iridium, Lynk/Omnispace),
  and Grain is now warehousing terrestrial D2D spectrum.

The deep checks below cover the top three regimes by score:
- dormant satellite priority (6);
- first approval of marketed-unapproved or compounded-only drugs (5);
- FAA PMA first-mover parts (4).

## Scoring method

Each regime is scored on the four ROUND2 conditions, marked Y (holds), P (partly) or N (fails):
- **C1:** the claim is cheap and first-come.
- **C2:** the public data is illegible and needs ML.
- **C3:** the asset is worth orders of magnitude more than the claim.
- **C4:** the value can be realised without an incumbent's channel.

The score out of 10 also takes crowding into account. Regimes that round 1 already covered keep its score
unless new evidence changed it.

## Catalogue

### A. Spectrum, orbit and telecom

| Regime | Cost to claim | First-come and exclusivity | Public, illegible data that says where to claim | Asset value | Who already farms it | C1 C2 C3 C4 | Score |
|---|---|---|---|---|---|---|---|
| **ITU NGSO/GSO filing, newly originated** | ITU cost-recovery fee (roughly CHF tens of thousands per filing, memory) plus an administration's sponsorship | First-in-time coordination priority, but **junior to every existing filing**. Res 35 milestones apply in Ku/Ka/V band. Must be brought into use. | SNL, BR IFIC, SRS | Only realised by launching | China (~244k satellites filed), Rwanda (327k), paper-satellite states | Y N P N | 3 |
| **Dormant, senior ITU MSS priority (L/S band) held by failed satellite companies** | Buy the shell or estate: low $M or less (the EllioSat pattern) | Senior priority is unique and cannot be copied. **Res 35 does not cover L/S band**, so a filing that was brought into use survives. Still needs administration support and national licences to operate. | SNL, BR IFIC (multilingual, partial, a state machine), corporate registers, insolvency dockets | $26-64.5M per right (AST/EllioSat). Aggregated, possibly hundreds of $M | EllioSat-type flippers. Strategics (AST, SpaceX, Amazon, Lynk/Omnispace, Fleet) buy directly | P P Y P | **6** |
| National MSS/D2D licences in small markets, which many licence on application | Licence fees, often low | Exclusive nationally. Often discretionary rather than strictly first-come. | National registers (FCC ULS/ICFS, Ofcom WTR, ACMA RRL, ANFR) | Tens of $M per country for D2D landing | Skylo, Lynk, AST and Starlink file everywhere | P P P P | 4 |
| FCC Part 25 GSO first-come processing queue | FCC application fees (~$10^4-10^5) plus a bond | First-come queue, US authorisation only | IBFS/ICFS | Small without a satellite | Operators | Y N N N | 2 |
| FCC Part 101 fixed microwave and 70/80 GHz light licensing | Hundreds of $ plus coordination | First-come per link | ULS | High only on HFT routes, which are already taken | McKay, Jump, Vigilant (memory) | Y P N N | 2 |
| Ofcom Shared/Local Access (3.8-4.2 GHz, unused MNO spectrum) | ~£80/yr per low-power licence (memory) | First-come per site, weak exclusivity | Ofcom WTR | Private-5G sites, small | Neutral hosts | Y N N P | 2 |
| AFRINIC and other residual IPv4 pools | Membership fees | Needs-based, and the pool is exhausted or under governance dispute | Whois, RIR stats | ~$30-50 per address, a closed pool | Cloud Innovation (litigation) | N N P Y | 1 |
| ICANN new gTLD round (2026) | ~$227k per application (memory) | Contention is resolved by auction, not first-come | Applicant guidebook | Mostly small | Donuts/Identity Digital | N N P Y | 1 |
| Broadcast and satellite landing rights | Fees plus local presence | Discretionary, qualified operators only | National gazettes | Medium | Incumbent broadcasters | N P P N | 1 |
| Subsea cable landing licences | Legal costs plus Team Telecom review; needs site control | Discretionary | FCC cable landing records, TeleGeography | High only if you build a cable | Hyperscalers, consortia | N P N N | 1 |
| Airspace and drone corridors | No claim regime exists (FAA Part 108 BVLOS rules are non-exclusive) | None | n/a | n/a | n/a | N - - - | 0 |

### B. Drugs, biologics and regulatory exclusivities

| Regime | Cost to claim | First-come and exclusivity | Public, illegible data that says where to claim | Asset value | Who already farms it | C1 C2 C3 C4 | Score |
|---|---|---|---|---|---|---|---|
| **First NDA for a marketed-unapproved or compounded-only drug** (FDA unapproved-drugs policy, plus 503B "essentially a copy" rule) | 505(b)(2) at about $3-30M, including CMC and BE/literature, plus the user fee | First approval wins. FDA then acts against the unapproved versions (de facto exclusivity) and 503B copies become unlawful. Plus 3-year, 5-year NCE or 7-year orphan exclusivity where they apply. | NDC directory "UNAPPROVED DRUG OTHER" SPL listings, 503B outsourcing-facility product reports, 503A/503B bulks nominations, Medicaid SDUD/Part D spend, shortage lists | Colcrys: ~$0.09 to ~$5 per tablet. Vasostrict: ~8-year monopoly, peak ~$0.8B/yr (memory). Vizient: $7.5B potential cost across 18 remaining candidates. | Par/Endo, Exela, Eton, American Regent, Nexus, Amneal, Hikma | P P Y Y | **5** |
| Orphan exclusivity on an old or off-patent molecule (Firdapse model) | $5-50M, usually needs a trial | First approval for the disease or indication gets 7 years in the US (10 in the EU) | Case reports, off-label literature, expanded-access and compassionate-use records, claims data | Catalyst worth several $B (memory) | Catalyst, Marathon/PTC, Travere, Eton, Zevra | P P Y Y | 5 |
| Tropical-disease, rare-paediatric and MCM PRVs | $10-50M | First approval of an active moiety for a listed disease. The voucher is transferable. | FDA tropical-disease list, foreign registers, WHO prequalification | **$195-210M per voucher in 2026** (SPARC $195M; Ultragenyx $210M, Oct 2026; a $200M sale, Jan 2026) | Knight, Exeltis, KaloBios history, Novartis | P P Y Y | 5 (round 1 wild lane B) |
| Molecules approved abroad but not in the US, licensed in for NCE | $10-150M | Exclusive licence plus first-approval NCE | EMA/PMDA/NMPA registers | Harmony, Catalyst | BD teams, Formation, Biossil | N P Y Y | 4 (round 1 red team) |
| Paragraph IV 180-day exclusivity | $1-5M ANDA plus litigation | First-to-file, but all same-day filers share it (NCE-1 date) | Orange Book, PTAB, dockets | Large per product | Teva, Viatris, Indian majors | N P Y Y | 2 |
| Competitive generic therapy (CGT) 180-day exclusivity | $1-3M ANDA | First approved CGT ANDA | Orange Book, "inadequate competition" list | $10-100M per product | Generic firms | P N P Y | 3 |
| NCE (5-year) and new clinical investigation (3-year) exclusivity | Full NDA | Earned at approval | n/a | Large | Pharma | N - - - | 1 |
| QIDP/GAIN +5 years | Approval | Add-on | n/a | Antibiotic economics are poor | Pharma | N - N - | 1 |
| First interchangeable biosimilar (up to 1 year) | $100M+ | First-come, but FDA's 2024 move away from switching studies erodes it | Purple Book | Shrinking | Biosimilar majors | N N P N | 1 |
| Paediatric exclusivity, SPCs, EU paediatric extension | Owner only | Attached to the patent or NDA holder | n/a | Large | Originators | N - - N | 0 |
| EU PUMA (paediatric-use MA, 8+2 years) | €1-10M | Data and market protection on an off-patent molecule | EMA PIP decisions | Small; only about 10 PUMAs ever (memory) | Few | P P N Y | 2 |
| Orphan designation (US/EU) | Free | **Not exclusive.** Exclusivity comes only at approval. | FDA OOPD database | Option value only | Everyone | Y P N Y | 2 |
| IND "drug preclusion" against supplements (FD&C 201(ff)(3)(B)) | IND preparation, about $0.1-1M | The first IND with public substantial clinical investigations bars supplement sales. **FDA reversed itself on NMN in Sep 2025**, and the doctrine is contested. | ODS/NDI notices, ClinicalTrials.gov | Protects nothing unless the drug is approved | Metro Biotech (NMN) | P N P N | 2 |
| FDA tobacco PMTA marketing orders | $1-10M+ per product | Not first-come, but early MGOs created an oligopoly (Zyn, Vuse, NJOY) | FDA MGO list | $B (Zyn) | Big tobacco | N N Y N | 2 |
| EU Novel Food 5-year data protection | €0.3-2M | First applicant's proprietary data is protected | EFSA opinions | $10-100M | Ingredient companies | P P P Y | 2 |

### C. Agriculture, chemicals and IP

| Regime | Cost to claim | First-come and exclusivity | Public, illegible data that says where to claim | Asset value | Who already farms it | C1 C2 C3 C4 | Score |
|---|---|---|---|---|---|---|---|
| US patents (first-inventor-to-file) | $10-30k to grant | 20 years, strong. ML-only "prophetic" claims are weak after Amgen v. Sanofi. | Everything | Highly skewed; the median is near zero | Everyone, NPEs | Y P P P | 3 |
| Chinese utility models | CNY 500 official fee before reductions (memory); granted in 6-12 months with **no substantive examination** | 10 years. Enforceable: Chint v. Schneider settled for ~CNY 157.5M (memory). Absolute novelty is required, so foreign art cannot be copied. | CNIPA publications, Chinese product launches | Litigation leverage in China | 2.65M filings in 2025 (down 16.8%), mostly domestic mills | Y P P N | 3 |
| German Gebrauchsmuster and other utility models | ~€40 fee (memory) | Unexamined, 10 years | DPMA | Small | Defensive filers | Y N N N | 2 |
| US/EU design patents (Amazon "Schedule A" suits) | $1-3k | Unexamined in the EU. Used in an abusive takedown practice. | Marketplace trend data | Small, contentious | Chinese sellers, ND Ill. plaintiff firms | Y P N N | 1 |
| Trademark first-to-file (China, much of civil-law Europe and Asia) | ~CNY 300 per class (memory) | First-to-file. China's 2019 law bars "bad faith not intended for use". | Brand-entry signals | Ransom value; **squatting, ethically out** | Squatters | Y P P N | 1 |
| Plant variety rights (UPOV) | $5-10k plus DUS trials | First-to-file, 20-25 years. **The variety must be new; you have to breed it.** | Genebanks; breeding data | $10-100M per elite variety | Bayer, Corteva, KWS | N P P Y | 2 |
| EPA FIFRA data compensation and 10-year exclusive use | $1-20M+ to generate the data | First submitter is compensated for 15 years. Followers must pay. | EPA data call-ins, registration review dockets | $1-50M per AI dossier | Agchem task forces, generics (Albaugh, ADAMA) | N P P Y | 2 |
| EU plant protection data protection (Reg. 1107/2009) | As above | 10-year data protection | EFSA conclusions | As above | As above | N P P Y | 2 |
| REACH lead registrant and letters of access | €50k-1M | The first registrant leads the SIEF and sells LoAs; costs must be shared fairly | ECHA dissemination | Small; the main deadlines passed in 2018 | Consortia, consultancies | P N N Y | 1 |
| Carbon methodology registration (Verra, Gold Standard) | $50-200k development | Developers earn a small per-credit fee (memory: ~$0.02/VCU); not exclusive | Registry data | Tiny | Methodology consultancies | P N N N | 1 |
| Geographic indications | Producer groups only | Collective, not private | n/a | n/a | n/a | N - - N | 0 |
| Copyright termination recapture | Notice-serving costs | No pre-grant lock-up (§203(b)(4)) | Copyright Office records | Catalogues $1B+ | Publishers, lawyers | N P Y P | 4 (round 1) |

### D. Physical, natural and other claimable rights (non-geological)

| Regime | Cost to claim | First-come and exclusivity | Public, illegible data that says where to claim | Asset value | Who already farms it | C1 C2 C3 C4 | Score |
|---|---|---|---|---|---|---|---|
| FERC hydro preliminary permits | Filing costs only; annual charges are small | True first-to-file, up to 4 years plus extension | NID, ORNL NPD, ANU atlas | Small without $2-4B/GW of build cost | Rye, Free Flow, pumped-storage speculators | Y N N N | 3 (killed in round 1) |
| Nepal hydropower survey licences | Low fees | First-come and hoarded; the government periodically cancels them | DoED lists | Only realised by building | Domestic developers | Y P N N | 2 |
| Philippines renewable-energy service contracts (including offshore wind) | Low | First-come; ~90 offshore wind contracts were awarded (memory) | DOE registry | Only realised by building | Speculators, CIP, BlueFloat | Y P N N | 2 |
| Wetland, stream and species mitigation banks | $5-30M per bank | Exclusive credits per service area. Approval is slow and not first-come. | RIBITS, permits | $1-3B ceiling | Wildlands, RES, Ecosystem Investment Partners | N P P Y | 4 (red-teamed) |
| Nonattainment emission reduction credits (ERCs) | Shutdown or control costs | Banked and rivalrous per air basin | State air permit records | $0.3-1.5B ceiling | Brokers | P P P Y | 5 (round 1 built lane) |
| Western water appropriation and seniority | Purchase | Priority dates are exclusive | State registers, OpenET | $B+ | Water Asset Mgmt, Vidler | N P Y P | 4 |
| Chile free water-right grants (pre-2022) | Formerly free | **Closed**: the 2022 reform made new rights temporary and use-it-or-lose-it | DGA | n/a | Historically, utilities | N - - - | 1 |
| England and Wales unregistered land and ransom strips | Purchase, or 10-12 years of adverse possession | Exclusive once registered, but slow | HMLR INSPIRE polygons vs. unregistered gaps, local plan allocations | Ransom value is often ~1/3 of uplift (Stokes v Cambridge, memory) | Land promoters, ransom-strip specialists | N P Y P | 3 |
| Bona vacantia and dissolved-company property (UK) | Market price from the Crown or the Government Legal Department | Not first-come | Gazette, Companies House | Small | Heir hunters, investors | N P P Y | 2 |
| Fishing catch history in fisheries that are about to be rationalised | Vessel operating costs | Future quota goes to qualifying history; regulators set "control dates" | NOAA/RFMO notices | Quota is valuable | Incumbent fleets | N P P Y | 2 |
| High-seas open-access fishing | Vessel plus RFMO registration | Not exclusive | GFW AIS | n/a | Distant-water fleets | N - - - | 1 |
| Salvage and shipwrecks | Search costs | Admiralty possession; sovereign immunity claims | Archives | Hostile courts | Odyssey, AE Studio | P P P N | 1 (killed in round 1) |
| Homesteading-like regimes abroad (usucapião, free patents) | Occupation and use | Requires residence or cultivation | Cadastres | Low, politically fraught | Local actors | N - - - | 1 |
| Domain names | ~$10 | First-come, exclusive | Trend data | Small | Domainers | Y P N Y | 1 |

### E. Aviation certification

| Regime | Cost to claim | First-come and exclusivity | Public, illegible data that says where to claim | Asset value | Who already farms it | C1 C2 C3 C4 | Score |
|---|---|---|---|---|---|---|---|
| **FAA PMA replacement parts** | ~$0.1-1M per part (memory) for reverse engineering, test and approval | **Not legally exclusive.** In practice the first PMA on a low-volume part often holds the market. | FAA DRS PMA listings, ADs, SDRs, IPCs, used-serviceable-material price feeds, fleet data | Per part, $1-20M/yr. HEICO: 19,000+ approvals, ~500 new parts a year, FSG margin ~24% | HEICO, Jet Parts Engineering (Vance Street), Wencor (Boeing), Chromalloy; AI reverse engineering (Novineer) | N P P P | **4** |
| FAA STC (e.g. passenger-to-freighter conversion of a type) | $20-150M+ (memory) | First STC per type is a de facto monopoly, not a legal one | DRS STC list, fleet retirement data | $0.5-2B programmes | IAI, Mammoth, KMC, AEI | N P P Y | 3 |

---

## Deep check 1: Buying dormant, senior satellite priority. Score 6/10

**The regime.** The ITU Radio Regulations give coordination priority by date of receipt. A network that has
been brought into use and recorded in the Master Register keeps its priority. For non-GSO systems in
10.7-51.4 GHz, Resolution 35 (Rev. WRC-23) forces deployment milestones: 10% at 2 years, 50% at 5 and
100% at 7, after the 7-year bring-into-use period. Outside those bands the milestones do not apply. That
includes the L-band (1.5-1.6 GHz) and S-band (2 GHz) MSS bands where D2D value now sits. A filing brought
into use there years ago by a small satellite company can still be senior today, even if the company died.

**The proof case.**
- Sky and Space Global (SSG) was a UK-filed nanosatellite MSS company. It launched three cubesats in
  2017 and then failed (per Tim Farrar, quoted by Mobile World Live).
- Its rights ended up in EllioSat, which "was set up earlier this year and controlled by two people in
  Texas" (Farrar). Dealroom/TechLeap lists the payee as CCUR.
- AST SpaceMobile agreed on 5 Aug 2025 to buy the entity for ~$64.5M headline. That is $26M upfront in
  shares plus $10M on each of the 2nd and 3rd anniversaries, about $46M certain. AST describes it as 60 MHz
  of global S-band (1980-2010 / 2170-2200 MHz) priority.
- Farrar thinks the rights are worth little. AST paid anyway, because priority clears coordination
  against later systems.

**Asset prices around it** (from round 1, plus updates):
- SpaceX-EchoStar ~$17B (AWS-4/H-block), plus ~$2.6B (unpaired AWS-3).
- Amazon-Globalstar $11.6B (Apr 2026).
- Rocket Lab-Iridium ~$8B.
- AST-Ligado $550M upfront plus ~$80M/yr (NPV ~$2B) for 40 MHz of US L-band.
- Grain is buying T-Mobile's 800 MHz for $2.9B to lease to D2D operators (FCC filing, 22 Apr 2026).

**The four-part law.**
1. **Cheap and first-come?** Partly. Originating a new filing is cheap, but it is junior to everything,
   so it is worth little. The value is in *old* priority, so the "claim" is buying a dead company's shell.
   That is cheap when the holder does not know what it has (EllioSat presumably paid little for SSG's
   remains; price not disclosed). Each right is unique, but anyone can make the purchase. It is not
   first-to-file.
2. **Illegible public data?** Yes, moderately:
   - SNL and BR IFIC are partial, multilingual and in PDF form.
   - Alive-or-dead status depends on the bring-into-use and suspension state machine (RR 11.44, 11.49,
     13.6).
   - Ownership sits in insolvency dockets and corporate registers across about 190 administrations.
   - The ML task: join these to find senior, live L/S/2 GHz filings held by entities that are dead,
     distressed or unaware.
   - That is real work, but a two-person spectrum boutique did the SSG deal without ML.
3. **Asset far above the claim?** Yes. Single rights trade at $26-64.5M. A stacked set of senior L/S
   priority plus national landing licences could reach the hundreds of millions.
4. **No incumbent channel needed?** Partly. Exit is a sale to one of 4-6 strategics. That is a real
   market, but a monopsony-like one, and each filing needs its notifying administration's goodwill (UK
   Ofcom for SSG) to change hands.

**Kill risks.**
- **Pool size.** The number of senior, live MSS filings in D2D-usable bands is dozens, not thousands.
- **Rules may change.** WRC-27 agenda item 1.13 (D2D in IMT bands) could move value to terrestrial-band
  holders, as Grain's bet shows. A future WRC could extend milestone rules to L/S band.
- **Notifying administrations** can suppress dormant entries. Ofcom and others have tightened against
  paper satellites.
- **Strategics know the field.** Lynk/Omnispace, AST and SpaceX employ the specialists. Farrar and
  Summit Ridge publish the landscape.

**First proof (4 weeks, about $40k).**
1. Parse SNL for every non-GSO and GSO MSS network in 1518-1675, 1980-2025 and 2160-2200 MHz, with its
   date of receipt and BIU, suspension and notification status.
2. Match each notifying entity to corporate status (UK Companies House, Luxembourg RCS, US state
   registries, insolvency registers).
3. Deliverable: a list of senior, live filings whose holder is dissolved, insolvent or dormant.
4. Kill test: if fewer than 5 such filings exist outside the big strategics, kill. If more than 10 exist,
   approach two holders with an LOI.

**Score: 6/10.** This is the closest outside-geology analogue to "read the abandoned record and stake it",
with a priced 2025 precedent. It is capped by pool size, by a monopsony of buyers, and by an ML edge that is
diligence-grade rather than inference-grade.

## Deep check 2: First approval of marketed-unapproved or compounded-only drugs. Score 5/10

**The regime.**
- **Unapproved drugs.** Many old drugs are sold without FDA approval: pre-1938 or DESI-era products,
  plus injectables made by 503B outsourcers. FDA's Unapproved Drugs Initiative (2006) is still in force:
  - HHS terminated it on 20 Nov 2020.
  - HHS and FDA withdrew that termination on 27 May 2021, calling it "legally and factually inaccurate".
  - It has produced 45 enforcement actions since 2006.
  - Under its risk-based policy, the first company to win an NDA for one of these drugs sees FDA act
    against the unapproved competitors.
- **Compounded copies.** Separately, the 503B "essentially a copy" provision (FDA guidance, Jan 2018)
  stops outsourcers making copies of an approved drug unless it is on the shortage list.
- **Statutory exclusivity on top.** The first approval also earns 3-year, NCE or orphan exclusivity
  where it applies.
- So the first NDA is a first-come claim that clears the market.

**Value evidence.**
- Colchicine (URL Pharma, Colcrys, 2009) went from ~$0.09 to ~$5.00 a tablet with 3-year exclusivity.
- Vasostrict (JHP filing in 2012, Par launch in 2014) kept a monopoly for about 8 years. The first
  generic came in late 2021.
- Vizient: five drugs that moved from unapproved to approved status added ~$3B in spending, and 18
  remaining candidates could add ~$7.5B.
- Recent operators include Eton (cysteine HCl approval), American Regent (selenious acid), Exela and
  Nexus.

**The four-part law.**
1. **Cheap and first-come?** First-come, yes. Cheap, no. A 505(b)(2) with CMC, BE or literature costs
   about $3-30M and takes 1-3 years. That is 10-100x cheaper than the asset, but it is not a $5 claim.
2. **Illegible public data?** Partly. The sources:
   - NDC directory/DailyMed SPLs with marketing category "UNAPPROVED DRUG OTHER";
   - the semiannual 503B outsourcing-facility product reports, which by statute list what is compounded
     at volume;
   - 503A/503B bulks nominations;
   - Medicaid SDUD and Part D spend;
   - shortage lists.
   Joining them ranks targets. This is a lookup more than an inference problem, and the high-value
   targets were mostly picked in 2006-2016.
3. **Asset far above the claim?** Yes for winners ($50-800M/yr), but the pool is depleted.
4. **No incumbent channel needed?** Mostly. Hospital injectables sell through GPOs and wholesalers, which
   any specialty generic company can reach.

**Kill risks.**
- **Political backlash** has been the pattern: colchicine, Makena, vasopressin and the 2020 HHS
  termination attempt. Vizient and other buyers lobby for simultaneous review of competing applications,
  which would end the first-come property.
- **Crowding.** Par/Endo, Exela, Eton, American Regent, Nexus, Amneal and Hikma watch the same lists.
- **Each win is public** in the approval letter and the 8-K.
- **Orphan scope.** The orphan-exclusivity add-on is narrowing back to "same use or indication" after
  Catalyst v. Becerra (2021); I did not check its current statutory status.

**First proof.**
1. Pull the NDC "unapproved" listings and the latest two 503B product reports.
2. Join them to SDUD and Part D spend.
3. Kill test: count molecules with more than $20M/yr in US spend, no approved NDA and no pending 505(b)(2)
   (checked against FDA approval lists and company pipelines). If fewer than 10, kill.

**Score: 5/10.** A real first-come regulatory claim with priced precedents. But it is a specialty-generics
business with a $3-30M ticket per claim, a depleted and politically exposed pool, and an ML edge that is a
lookup. It fits as the fallback "real business", alongside round 1's stranded-drug and PRV ideas.

## Deep check 3: FAA PMA first-mover parts. Score 4/10

**The regime.** The FAA grants Parts Manufacturer Approval (14 CFR 21 Subpart K) to anyone who shows a
replacement part is identical to or better than the OEM part. That is usually done by reverse engineering
plus testing, or by a licence.
- **No legal exclusivity:** a second PMA on the same part is allowed.
- **But markets per part are small,** so the first approved PMA often takes most of the non-OEM share.

**Value evidence.**
- HEICO has 19,000+ FAA approvals and adds ~500 new parts a year.
- Its Flight Support Group operating margin is ~24%, with 16% organic PMA growth (Q2 FY2025).
- It holds about 2% of the aftermarket.
- PMA can save up to 60% on an engine shop visit under time-and-materials contracts.
- HEICO's equity value is about $40B (memory). That is the value of a portfolio of first-mover
  approvals.

**The four-part law.**
1. **Cheap and first-come?** No. A PMA costs roughly $0.1-1M per part (memory) and is not exclusive.
2. **Illegible public data?** Partly. FAA DRS PMA and STC listings, ADs, Service Difficulty Reports, and
   fleet and retirement data are public. OEM list prices and failure rates are semi-public through used-
   material marketplaces. ML could rank parts by spend times no-PMA times feasibility. Startups such as
   Novineer (AI reverse engineering, Apr 2026) are entering.
3. **Asset far above the claim?** Moderately. A good part earns $1-20M/yr against a $0.1-1M approval.
4. **No incumbent channel needed?** Partly. Airlines and MROs buy PMA directly, but OEMs fight back with
   warranty threats and engine-maintenance lock-in on new engines (LEAP, GTF).

**Kill.** HEICO, Jet Parts Engineering (Vance Street, which acquired Mitchell PMA in 2024), Wencor (now
Boeing) and Chromalloy run exactly this franchise. The claim is not exclusive and not cheap.

**Score: 4/10.** It is a good business shape, but it fails C1.

## What the catalogue says about the law

- **Every regime where C1 truly holds** (a cheap, first-come, legally exclusive filing) gives an option
  that is worthless until heavy capital is spent: ITU originations, FERC permits, survey licences,
  utility models, patents. Mineral tenure is the rare regime where a *finding* (a body of ore) can be
  sold before development, because geology is the uncertainty and the data resolves it.
- **The nearest equivalents are "abandoned senior paperwork" regimes.** In these the dataset reveals that
  a past claimant already did the expensive step and then died:
  - dormant ITU priority;
  - lapsed or unaware holders of national licences;
  - unapproved drugs (where the "past claimant" is the market itself).
  These deserve attention, but the pools are finite and the buyers concentrated.
- **No regime outside geology combined all four** conditions with a multi-billion pool and no organised
  farmer.

## Sources

- HHS/FDA withdrawal of the UDI termination (May 2021): https://hlc.com/en/publications/in-sharp-rebuke-to-trump-administration-hhs-notice-ending-unapproved-drugs-initiative-is-withdrawn
- UDI economics, Vizient $7.5B, colchicine and vasopressin: https://www.drugpatentwatch.com/blog/unapproved-drugs-opportunities-rapid-approval-market-exclusivity/
- UDI price and competition study (not fetched; captcha): https://pmc.ncbi.nlm.nih.gov/articles/PMC8129902/
- FDA activities to remove unapproved drugs: https://www.fda.gov/drugs/enforcement-activities-fda/fda-activities-remove-unapproved-drugs-market
- 503B "essentially a copy" guidance: https://www.hhs.gov/guidance/sites/default/files/hhs-guidance-documents/FDA/Compounded-Drug-Products-That-Are-Essentially-Copies-of-Approved-Drug-Products-Under-Section-503B-of-the-Federal-Food--Drug--and-Cosmetic-Act-Guidance-for-Industry.pdf
- Eton cysteine approval: https://www.biospace.com/eton-pharmaceuticals-announces-fda-approval-of-cysteine-hydrochloride-injection
- PRV prices 2026: https://www.pharmexec.com/view/ultragenyx-sell-rare-pediatric-disease-priority-review-voucher-210-million ; https://www.lachmanconsultants.com/2026/01/bazinga-another-priority-review-voucher-sold-for-200-million/ ; https://www.geneonline.com/sparc-sells-rare-pediatric-disease-priority-review-voucher-for-195-million-after-sezaby-approval/
- NMN preclusion reversal (Sep 2025): https://www.nutritionaloutlook.com/view/fda-responds-to-citizen-petitions-on-nmn-amending-its-position-on-the-ingredient-s-status-as-a-dietary-ingredient
- AST S-band priority deal: https://www.mobileworldlive.com/ast-spacemobile/ast-spacemobile-pays-over-64m-for-s-band-spectrum/ ; https://finder.techleap.nl/news/feed/ast-spacemobile-acquires-elliosat-for-26m ; https://www.businesswire.com/news/home/20250806333130/en/AST-SpaceMobile-Announces-Agreement-to-Acquire-Global-S-Band-Spectrum-Priority-Rights-Held-under-the-International-Telecommunication-Union
- Resolution 35 (Rev. WRC-23) band list: https://www.itu.int/en/ITU-R/space/Documents/RES35(REV.%20WRC-23).pdf
- MSS holders and the AST-Ligado price: https://www.lightreading.com/satellite/satellite-texting-could-leave-mss-spectrum-lost-in-space
- D2D deal roundup: https://www.lightreading.com/satellite/satellite-d2d-dealmaking-spacex-amazon-rocket-lab-and-the-spectrum-they-re-after ; https://www.satellitetoday.com/connectivity/2026/05/05/what-amazons-globalstar-acquisition-means-for-mss-spectrum-and-d2d-market-analyst-roundtable/
- Grain D2D leasing plan: https://broadbandbreakfast.com/grain-aiming-to-lease-direct-to-device-spectrum-90-days-after-deal-closing/
- China utility models in 2025 (2.65M, down 16.8%): https://www.chinaiplawupdate.com/?p=4224
- HEICO PMA facts: https://findvalue23.substack.com/p/hei-heico-2
- AI reverse engineering for PMA (Novineer): https://runwaygirlnetwork.com/2026/04/press-release-novineer-launches-ai-reverse-engineering-with-am-craft/
- Jet Parts Engineering acquires Mitchell PMA: https://avitrader.com/2024/10/08/jet-parts-engineering-acquires-mitchell-pma
- Round 1 files in this folder: lane_claims.md, lane_energy.md, lane_wild.md, lane_earth.md, lane_built.md, lane_materials.md, redteam_drugs.md, redteam_banks.md
