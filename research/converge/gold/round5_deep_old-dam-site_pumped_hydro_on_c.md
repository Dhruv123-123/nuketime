## Old-dam-site pumped hydro on Crown land (NSW/Qld): feasibility deep-dive (relaxed C3)

**Research note:** the shared WebSearch budget for this turn (200 calls) was already used up, so I ran no new searches. Of 13 direct fetches, only 4 worked: ANU atlas, NSW Crown Lands, and two RenewEconomy pages. WaterNSW, the Hillgrove/Kantra PDF, ASL, ARENA and AEMO returned 403/404/503. Figures not re-verified this round are marked as estimates or "unverified".

### Frame of reference
The rung is a feasibility-grade pumped hydro (PHES) project with a site right, sold to a genco. Finding a site with good head, geology and an old state investigation is roughly 25-40% of the work (estimate). The rest is water entitlement, grid connection, EPBC and state planning approval, native title future-act processes, community licence and cost estimation. None of that is discovery. Snowy 2.0 and Borumba show that cost and buildability, not site identification, decide whether these projects live. Borumba went from A$14.2B to more than A$18B, and Pioneer-Burdekin was scrapped as "not financially viable" ([RenewEconomy](https://reneweconomy.com.au/queensland-pushes-ahead-with-borumba-pumped-hydro-despite-cost-blowout-and-renewable-pause/)). This is close to the geothermal-in-coal-mines counter-example: the hard part is not finding the site.

### Step-up ratio
- **Unproven price:** a licence under A$10k is assumed but unverified. NSW actually allocates renewable-energy Crown land by EOI then RFP, at a site the state picked itself (Balranald, EOI 2 Mar-17 Apr 2023) ([Crown Lands](https://www.crownland.nsw.gov.au/news/renewable-energy-opportunity-crown-land)).
- **Proven price:** Hillgrove sold AGL the Kanmantoo PHES rights (250 MW / 8 h) for a A$31M headline (~A$124k/MW), with about A$1M on signing and the rest tied to milestones over 18-36 months ([Hillgrove PDF](https://hillgroveresources.com.au/uploads/downloads/224/190416%20Hillgrove%20Sells%20Rights%20to%20Pumped%20Hydro%20Project.pdf), now 404; terms come from the candidate's sourcing). From memory and unverified: AGL did not complete the full payments.
- **Ratio:** about 10^3x on the licence, but about 5-15x on the A$1-4M at risk, and about 1x on cash paid at signing (estimate).
- **Transactions per year:** about 0-3 feasibility-grade PHES site sales a year in Australia (estimate).

### Hit rate and proving capex, today and with ML
- **Capex today:** about A$1-4M and 1-2 years per site for geotechnical boreholes, hydrology, connection studies and pre-feasibility design (candidate estimate, consistent with Kanmantoo's drilling milestones). The expensive leg passes.
- **Hit rate today:** 40-60% pass to feasibility (unsourced estimate).
- **Hit rate with ML:** ML over old borehole logs addresses geotech risk only, which is a minority of attrition. Connection, water, approvals and economics dominate. Estimated lift in cost per proven project is 1.2-1.5x, which scores C3 = 3.

### Data source
- **Named datasets:**
  - Scanned WaterNSW and former NSW Water Resources Commission / Water Conservation and Irrigation Commission dam investigation reports and borehole logs (NSW State Archives).
  - Queensland Water Resources Commission reports (Qld State Archives).
  - AEMO ISP REZ and connection data.
  - The Crown cadastre.
- **Why the old reports are illegible:** they are scanned typescript and hand-drawn logs, scattered across archives.
- **The ANU atlas is the legible baseline but has no geology:** none of its sites "have been the subject of geological, hydrological, environmental, heritage and other studies" ([ANU atlas](https://re100.eng.anu.edu.au/pumped_hydro_atlas/)). That makes old geotech a real gap.
- **Outcome field:** the outcome is not summarised in a legible field.
- **But the data owner reads its own files:**
  - WaterNSW is running its own pre-feasibility studies across 41 dams ([WaterNSW update](https://waternsw.com.au/__data/assets/pdf_file/0010/263458/Community-update-Renewable-Energy-Program-pre-feasibility-studies-March-2025.pdf), 403 this round).
  - Queensland Hydro ran its own 2017 site study (from the candidate's sourcing; not fetched).

### How the right is bought
This fails.
- **NSW Crown land:** the state now chooses sites itself and runs EOI/RFP processes. RenewEconomy says this "reverses the normal process of developers identifying potential land" ([RenewEconomy](https://reneweconomy.com.au/nsw-in-landmark-crown-land-tender-for-major-solar-and-wind-projects/amp)). A developer-initiated application route exists, but neither fetched page gives its fees or terms.
- **NSW dam land:** WaterNSW allocates access by competitive tender with Development Agreements. ACEN won Burrendong, Upper Hunter Hydro won Glenbawn, ZEN won Burragorang (candidate sourcing, not re-verified).
- **Queensland:** the state develops through its own company, Queensland Hydro ([RenewEconomy](https://reneweconomy.com.au/queensland-pushes-ahead-with-borumba-pumped-hydro-despite-cost-blowout-and-renewable-pause/)).
- **Legal mechanics (general knowledge, unverified):** Crown licences are personal, revocable and not freely transferable. Commercial use pays market rent, and any grant triggers native title future-act processes.
- **Share of uplift kept:** the public owner captures most of the hope value. The company keeps whatever is left after tender premiums, rent and milestone-contingent payments (estimate: well under 50%).

### Capitalised buyer
Real buyers exist: AGL (the Kanmantoo precedent), ACEN, EnergyAustralia, Snowy Hydro, CleanCo, Quinbrook, and bidders in the CIS/LTESA tenders. They pay in staged, conditional tranches, not on the hit.

### Integration ladder above
Strong in principle. The path runs from site rights and feasibility, to development approval and connection, to EPC and owning the storage asset, to a storage portfolio, to a genco or retailer. Building costs about A$1-2M/MW or more (estimate), so the upper rungs are multi-billion-dollar.

### Who else does this
From general knowledge, unverified:
- **PHES developers:** Genex (Kidston, an old mine pit), Upper Hunter Hydro, ZEN, ACEN, BE Power, Hydro Tasmania (Battery of the Nation), EnergyAustralia (Lake Lyell).
- **State bodies:** WaterNSW and Queensland Hydro.
- **Engineering consultancies:** Entura, GHD and SMEC, which routinely reuse historic state dam reports.

### Smallest feasibility test (2 weeks)
1. Pull the NSW State Archives catalogue entries for Water Resources Commission dam investigations from about 1950-1990.
2. Pick 20 sites that have borehole logs and sit outside the 41 WaterNSW dams and the current tender sites.
3. For each site, record land tenure. Is it Crown land, WaterNSW land or freehold farmland? If it is Crown land, check whether it is already reserved, under claim or offered by EOI.
4. Make one call to Crown Lands asking for the fee, term, transferability and native title handling of a developer-initiated investigation licence.

**Pass if:** at least 5 sites have geotech that is not on the ANU atlas and are held as freehold or unreserved Crown land, where an option or licence costs under A$50k and can be assigned to a genco.

This test also checks the untested rescue raised in the third verifier's notes: options over freehold farmland at old proposed-dam sites, bought from owners who cannot read the files.

### Verdict
**Kill as framed.** Proving is expensive and buyers have capital. But the state that owns the land holds and reads the illegible files, and it tenders the hope value away. Discovery is a minority of PHES development work. The realised step-up on capital at risk is about 10x.

| Criterion | Score (0-5) |
|---|---|
| C1 Frame | 2 |
| C2 Step-up | 3 |
| C3 Hit-rate lever | 3 |
| C4 Data + right | 1 |
| C5 Ladder | 4 |
| **Total** | **13/25** |

Not excluded.