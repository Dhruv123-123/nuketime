# R08: Split estate, federal geothermal reservations under private surface, and surface access

**Scope:** Stock-Raising Homestead Act (SRHA) lands, where the federal government reserved geothermal under private surface; how those parcels are leased; conflicts with surface owners; private landowners who don't know their geothermal value; scale of acreage.

**Research constraint:** The shared WebSearch budget for this workflow run was used up before this agent's first query. Everything below comes from direct fetches of primary sources (US Code via Cornell LII, 43 CFR via govinfo, CourtListener search API, OSTI records, BLM pages), from Wikipedia where marked, and from sibling evidence files R06 and Z04. Claims I could not check against a fetched source are marked **(unverified)**.

---

## 1. The legal machinery: federal geothermal under private surface is federal-leasable

1. **Statutory leasing authority.**
   - The Geothermal Steam Act, 30 U.S.C. §1002, lets Interior issue geothermal leases on three classes of land:
     - lands Interior administers;
     - Forest Service lands;
     - "lands which have been conveyed by the United States subject to a reservation" of "the geothermal resources therein."
   - The regulation 43 CFR §3201.10(a)(3) repeats this: BLM may lease "Lands conveyed by the United States where the geothermal resources were reserved to the United States."
2. **Exclusivity.** 30 U.S.C. §1020 says:
   - Geothermal resources "in lands the surface of which has passed from Federal ownership but in which the minerals have been reserved to the United States shall not be developed or produced except under geothermal leases made pursuant to this chapter."
   - If production is imminent, the Attorney General is "authorized and directed" to sue to quiet the federal title and enjoin production outside the Act.
   - The surface owner therefore cannot lawfully sell or lease the heat. Only BLM can.
3. **SRHA reservation.** The SRHA of 1916 (43 U.S.C. §299(a)) requires every patent to carry "a reservation to the United States of all the coal and other minerals," with the right to prospect, mine and remove them.
4. **Courts hold that "minerals" includes geothermal.**
   - *United States v. Union Oil Co. of California*, 549 F.2d 1271 (9th Cir. 1977), concerned The Geysers.
     - The district court had first held that steam was **not** a mineral (369 F.Supp. 1289, N.D. Cal. 1973; OSTI 5322239).
     - The Ninth Circuit reversed: the SRHA reservation covers geothermal resources.
     - The Supreme Court later summarised it in *Watt v. Western Nuclear*, 462 U.S. 36 (1983), n.13: the Ninth Circuit "held that geothermal steam constitutes a mineral reserved to the United States under the SRHA."
   - *Rosette Inc. v. United States*, 277 F.3d 1222 (10th Cir. 2002), concerned Lightning Dock, Hidalgo County, NM.
     - Summary judgment for the US on ownership of geothermal resources under SRHA patents.
     - Earlier rounds: 141 F.3d 1394 (10th Cir. 1998, a limitations issue); 64 F.Supp.2d 1116 (D.N.M. 1999).
     - State companion: *Rosette v. DOI*, 2007-NMCA-136.
     - Zanskar's Lightning Dock plant sits in this exact fact pattern (R06).
   - *Watt v. Western Nuclear* (1983) broadened the SRHA "minerals" test even further (gravel counts):
     - the substance must be a mineral that can be removed from the soil and used commercially;
     - it must not be the kind of substance intended to be part of the surface estate.
5. **Surface use without consent.**
   - *Occidental Geothermal, Inc. v. Simmons*, 543 F.Supp. 870 (N.D. Cal. 1982), at The Geysers in Lake and Sonoma counties.
   - The federal government "can lease the right to drill geothermal wells and build geothermal power plants on lands patented to homesteaders without the surface owner's consent" (OSTI 5703721, GRC Bulletin 12(1):3-6, 1983).
   - The surface owner's remedy is damages, not a veto (OSTI 5350053, 1982).
6. **Surface-owner protections are weak for leasable (not locatable) minerals.**
   - SRHA §299 requires a mineral entrant to pay for damage to crops and improvements or post a bond.
   - The 1993 amendments (Pub. L. 103-23) added notice, consent, a plan of operations, a fee and a reclamation bond. Those amendments are framed around **mining claims** and **locatable** minerals: §299(b)-(c) text refers to exploring for and locating claims.
   - Reading the text, a geothermal lessee is a leasable-mineral operator, so these consent rules appear not to apply. The protection comes back to the original "damages or bond" clause plus BLM lease bonds. **(unverified as applied to geothermal; needs counsel.)**
   - 43 CFR Part 3200 has no geothermal analogue to the oil and gas "Onshore Order 1" surface-owner agreement. The regulations I read cover:
     - consultation with a *federal* surface management agency (§3250.10(a)(2), §3210.14);
     - reclamation bonds (§3214.12(b), §3214.18(b));
     - private land excluded from the exploration-permit rules (§3250.10(b)(3)).
   - I read 200k of the ~309k characters of Part 3200. The last third, Subparts 3260-3280 on drilling and utilization, may contain more **(unverified)**.
7. **Federal lease economics apply as on any BLM parcel** (43 CFR §3211.11, 2023):
   - competitive lease: $2/ac in year 1, then $3/ac in years 2-10;
   - noncompetitive lease: $1/ac for 10 years;
   - all leases: $5/ac after year 10;
   - minimum lease 640 ac or the whole available section (§3206.12);
   - **rent prorated where the US owns only a fractional geothermal interest** (§3211.11(d)). This is a direct regulatory signal that split and fractional federal geothermal title exists and is leased.

## 2. Scale of acreage

| Category | Acres | Source |
|---|---|---|
| BLM subsurface mineral estate | ~700M | BLM "What we manage" |
| BLM surface | 245M | BLM |
| Lands where BLM manages geothermal leasing (incl. 104M USFS) | ~245M | BLM geothermal page |
| Federal minerals under private or state surface (split estate, all minerals) | ~58M | BLM 2006/2017 split-estate material, cited by Wikipedia (secondary) |
| Land patented under SRHA | **>33M** | *Watt v. Western Nuclear*, 462 U.S. 36 (majority and dissent both say ~33M) |
| SRHA maximum per entry | 640 ac | SRHA text (Wikipedia citing 39 Stat. 862) |
| Operating plants on BLM-managed geothermal | 51 plants, >2.65 GW | BLM geothermal page |

Interpretation:
- **Size of the SRHA pool.** At least 33M acres of private-surface land in the West carry a federal geothermal reservation as a matter of settled 9th and 10th Circuit law. By count that is up to roughly 52,000 full-section patents. That is an upper bound, because many patents were under 640 ac **(unverified count)**.
- **How it compares with the open federal estate.** 33M acres is about 13% the size of the 245M-acre federal geothermal estate. It sits disproportionately on low-elevation valley and range-front grazing land in NV, NM, UT, AZ, CA, OR, ID, WY, CO and MT. Range-front faults and valley margins are exactly where blind Basin-and-Range hydrothermal systems hide.
- **State breakdown.** I could not source an SRHA breakdown by state **(unverified)**.
- **Other reservation statutes widen or complicate the pool:**
  - **Pittman Underground Water Act (1919, Nevada).** It reserved "coal and other valuable minerals" (*Bedroc v. US*, 314 F.3d 1080, 9th Cir. 2002, held sand and gravel were *not* "valuable minerals" under Pittman). Whether Pittman reserves geothermal is, as far as I can find, untested **(unverified)**. That is a live title question across Nevada valley-bottom patents.
  - **The 1909 and 1910 Acts (coal; Agricultural Entry Act).** These reserve *specific* minerals, so geothermal generally passed to the patentee **(unverified)**. *Aulston v. US*, 915 F.2d 584 (10th Cir. 1990), shows courts reading these specific reservations narrowly: CO2 was not included in an oil and gas reservation.
  - **Post-1976 FLPMA sales and exchanges.** These generally reserve all minerals **(unverified)**.
  - **Railroad-grant checkerboard.** The Central Pacific/Union Pacific grants along the Humboldt corridor in northern Nevada passed fee title without a general mineral reservation, so private owners of alternate sections may hold the geothermal outright **(unverified)**.
- **Total federal leasing activity** (lease counts, acres under lease): see R01, R02 and R04. Not re-derived here.

## 3. Conflicts and their history

- **The Geysers, 1970s-80s.** This is the canonical conflict.
  - Union Oil and other lessees held federal leases under SRHA ranch surface.
  - The federal government had to win in the 9th Circuit before those leases were clean (1973 loss, 1977 win).
  - Surface owners then fought plant siting and compensation: *Occidental v. Simmons*, 1982; OSTI 6465469 (1981, "Impact of geothermal development on stockraising homestead landowners").
  - That report records that "surface use and compensation conflicts have developed at the Geysers" and makes recommendations to the Secretary on compensation methods. It also asked whether similar conflicts could arise on SRHA lands elsewhere.
- **Lightning Dock, NM, 1990s-2007.**
  - A greenhouse operator (Rosette) using geothermal water on SRHA land claimed it owned the resource.
  - It lost through three federal rounds and one state round across about 10 years.
  - The federal BLM lessee's position prevailed. The asset is now Zanskar's (R06).
- **Commentary.** Contemporary literature criticised *Union Oil* (OSTI 5265578, 1974; OSTI 5567427, 1978). The 1978 note flags unresolved **estoppel and compensation questions for private lessees**: people who had leased "geothermal" from the surface owner before the federal title was confirmed.
- **Pattern.** Title is now settled for SRHA. The residual friction is:
  - surface access;
  - plant and pad siting;
  - compensation negotiations with ranchers who own the surface but not the heat;
  - county-level permitting where the surface is private.

## 4. "Private landowners who don't know their geothermal value": where it actually applies

- **SRHA ranchers do *not* own the heat.** An acquisition strategy that leases "geothermal rights" from them is legally void (30 U.S.C. §1020; *Union Oil*; *Rosette*). This is the most common trap.
- **Where a landowner really holds unrecognised value:**
  - fee lands with no mineral severance (cash-entry patents, original homestead patents, some railroad lands);
  - private mineral owners in states where geothermal follows the mineral estate (California: *Geothermal Kinetics v. Union Oil*, 1977);
  - states where it follows the surface estate (Texas SB 785; see R06 and R07).
- **SRHA surface owners still hold real leverage, even without the heat:**
  - physical access across private roads;
  - pad and plant sites;
  - water;
  - goodwill with the county;
  - compensation for surface damage.
- **What a sophisticated acquirer does:** win the federal lease cheaply, then sign surface-use and option agreements with the rancher *before* the resource is proven. The rancher is unlikely to price the surface option at discovery value **(unverified, inference)**.
- **Market signal.** In the NV-2025-10 BLM sale, a 732.63-acre **split-estate** parcel (NV-2025-10-2174, Eureka/Lander Co.) cleared at **$21/acre** with Zanskar winning (Z04). Split-estate parcels do come up in BLM sales, and they clear at prices comparable to ordinary federal parcels.
- **Possible discount.** Split-estate parcels may carry a modest surface-access discount compared with nearby pure federal parcels, for example the $232/ac paid for Pumpernickel step-out acreage. Proving it would need parcel-level analysis **(unverified)**.

## 5. Practical acquisition mechanics for split estate

1. **Identify** federal-reserved geothermal under private surface. Sources:
   - BLM Master Title Plats and MLRS/LR2000 records;
   - historical index entries showing SRHA patent type;
   - county recorder records for the patent's mineral-reservation language.
2. **Nominate** to BLM. Since EPAct 2005, BLM offers leases competitively first; noncompetitive leases are available on parcels left over after a sale (R02). Every nomination is public, which leaks signal (Z04).
3. **Lock up surface.** Before announcing anything, sign surface-use agreements, rights-of-way and pad options with SRHA surface owners.
4. **Clear title.** For non-SRHA patents (1909/1910/Pittman/railroad), resolve whether geothermal went with the patent or the reservation. Expect quiet-title cost and delay, which in Rosette's case took about 10 years.

---

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **The direct Terranox analogue is a title-classification problem.**
   - Terranox joins illegible historical *geology* records with *tenure*.
   - In the US West the tenure layer for geothermal is itself illegible: about 33M+ acres of SRHA patents (federal heat, private surface), about 58M acres of all-minerals split estate, Pittman lands in Nevada of uncertain status, and railroad checkerboard where the private owner may hold the heat.
   - A model that classifies every parcel by **who can legally grant the geothermal right** (BLM, the state, the mineral owner or the surface owner) and joins that to temperature and structure data is a genuine moat. Every competitor has to do this work parcel by parcel with lawyers.
2. **The pre-proof acquisition plays are clear and cheap:**
   - (a) nominate and win BLM leases on SRHA split-estate parcels at about $2-21/ac plus $1-3/ac/yr rent;
   - (b) take surface-use options from the ranchers at agricultural prices;
   - (c) buy fee geothermal outright where no reservation exists (railroad checkerboard, cash-entry patents) **(unverified extent)**.
3. **Owning the asset works.** A federal lease plus a surface option is a transferable package that Fervo, Ormat or a data-centre developer would pay a step-up for. This mirrors the roughly 100x reprice seen after Zanskar's Pumpernickel disclosure (Z04).
4. **The gap vs Zanskar.**
   - Zanskar's land book is overwhelmingly Nevada BLM competitive-sale acreage plus one SRHA-type plant (Lightning Dock).
   - It has won only one split-estate parcel visibly (2174), and nothing outside Nevada at auction (Z04, Z07).
   - Nothing public shows it running a systematic split-estate, surface-option or fee-geothermal acquisition program **(inference)**.
   - The open lane: a land bank that targets SRHA and checkerboard valley-margin parcels across NM, UT, OR, ID and AZ. Pair each federal lease with a locked surface agreement, then sell de-risked "lease + surface + data" packages to developers. Zanskar is an explorer and operator, not a seller of de-risked packages.
5. **Risks:**
   - surface-owner hostility and compensation litigation, as at The Geysers;
   - the weak statutory consent protections could change politically;
   - Pittman and other-reservation title fights can take about 10 years, as in *Rosette*;
   - BLM nominations publicly leak targets;
   - split-estate NEPA and cultural-resource review on private surface can slow BLM leasing **(unverified magnitude)**.
6. **Verdict on this angle:** Plausible, and not too small. 33M+ acres of SRHA land alone is a large, legally settled federal-heat pool under private surface. This is a differentiated acquisition channel, not a service. It strengthens the Terranox-shape case, provided the ranchers' surface leverage is converted into options before discovery.

---

## Sources
- 30 U.S.C. §1002 (lands subject to geothermal leasing): https://www.law.cornell.edu/uscode/text/30/1002
- 30 U.S.C. §1020 (reserved-mineral lands; exclusive leasing; quiet title): https://www.law.cornell.edu/uscode/text/30/1020
- 43 U.S.C. §299 (SRHA reservation; surface protections, 1993 amendments): https://www.law.cornell.edu/uscode/text/43/299
- 43 CFR §3201.10: https://www.law.cornell.edu/cfr/text/43/3201.10
- 43 CFR Part 3200 (govinfo, 2023): https://www.govinfo.gov/content/pkg/CFR-2023-title43-vol2/xml/CFR-2023-title43-vol2-part3200.xml
- Watt v. Western Nuclear, 462 U.S. 36 (1983) (">33 million acres patented under the SRHA"; n.13 on Union Oil): https://www.law.cornell.edu/supremecourt/text/462/36
- US v. Union Oil, 549 F.2d 1271 (9th Cir. 1977): https://www.courtlistener.com/opinion/343212/united-states-v-union-oil-company-of-california/
- US v. Union Oil, 369 F.Supp. 1289 (N.D. Cal. 1973): https://www.courtlistener.com/opinion/2290346/united-states-v-union-oil-company-of-california/
- Rosette v. US, 277 F.3d 1222 (10th Cir. 2002): https://www.courtlistener.com/opinion/161903/rosette-incorporated-v-united-states/
- Rosette v. US, 141 F.3d 1394 (10th Cir. 1998): https://www.courtlistener.com/opinion/156182/rosette-incorporated-v-united-states/
- Rosette v. DOI, 2007-NMCA-136: https://www.courtlistener.com/opinion/2625254/rosette-inc-v-united-states-of-department-of-the-interior/
- Occidental Geothermal v. Simmons, 543 F.Supp. 870 (N.D. Cal. 1982): https://www.courtlistener.com/opinion/1460931/occidental-geothermal-inc-v-simmons/
- Bedroc v. US, 314 F.3d 1080 (9th Cir. 2002) (Pittman Act): https://www.courtlistener.com/opinion/7109873/bedroc-ltd-v-united-states/
- Aulston v. US, 915 F.2d 584 (10th Cir. 1990): https://www.courtlistener.com/opinion/548788/joe-aulston-and-lola-aulston-v-united-states-of-america-and-shell-western/
- CourtListener search used: https://www.courtlistener.com/api/rest/v4/search/?q=%22Union%20Oil%22%20%22Stock-Raising%20Homestead%20Act%22%20geothermal%20steam%20mineral%20reservation&type=o
- OSTI 6465469 (1981), Impact of geothermal development on stockraising homestead landowners: https://www.osti.gov/api/v1/records/6465469
- OSTI 5703721 (1983), Occidental v. Simmons commentary, GRC Bulletin: https://www.osti.gov/api/v1/records/5703721
- OSTI search (SRHA + geothermal; records 5350053, 5265578, 5567427, 5322239): https://www.osti.gov/api/v1/records?q=%22stock-raising%20homestead%22%20geothermal&rows=20
- BLM geothermal program: https://www.blm.gov/programs/energy-and-minerals/renewable-energy/geothermal-energy
- BLM what we manage (700M ac subsurface): https://www.blm.gov/about/what-we-manage/national
- Wikipedia, Split estate (58M ac figure citing BLM; secondary): https://en.wikipedia.org/wiki/Split_estate
- Wikipedia, Stock-Raising Homestead Act (secondary): https://en.wikipedia.org/wiki/Stock-Raising_Homestead_Act
- Sibling files: /home/user/nuketime/research/geothermal/evidence/R06-private-ownership-law.md, Z04-land.md, Z07-other-ai.md
