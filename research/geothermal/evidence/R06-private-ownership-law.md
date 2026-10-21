# R06 — Who owns geothermal on private land, state by state; private lease economics

Research note. **Method caveat:** the shared web-search budget for this run was used up before this agent began. The work below comes from fetching primary sources directly: state legislature statute pages, the Texas Legislature bill system, CourtListener case search, eCFR/govinfo (43 CFR 3200), and SEC EDGAR 10-K full text. Items I could not verify against a fetched source are marked **(unverified)**.

## 1. The core legal question

Geothermal is heat carried in rock and fluid, so it doesn't fit neatly into the usual property categories. US states have chosen four ways to classify it:

1. **Mineral.** It goes with the mineral estate, so on split-estate land the mineral owner (which can be the federal or state government) owns it.
2. **Water.** The fluid is appropriated under water law, so the right comes from the State Engineer, not from a deed.
3. **Sui generis.** It is its own resource, usually vested in the surface owner by statute.
4. **Surface-owner statute.** A statute gives it to the surface estate explicitly, even when the estates are severed.

For an asset-acquisition company, this decides **whom you pay and what you hold**:
- Under category 4, the rancher who owns the surface can lease the heat to you.
- Under category 1, the counterparty may be a fragmented, absentee mineral owner, or Uncle Sam.
- Under category 2, the "asset" is partly a water-rights permit.

## 2. State by state

### Texas: surface owner, by statute (2023)
- **The bill is SB 785, not HB 1818.** The brief cited HB 1818; that number in the 88th Legislature is a county tax-rate bill (Muñoz).
- SB 785 (Birdwell; House sponsors Darby, Guerra, E. Morales, Anchía; identical House companion HB 1336) is captioned "Relating to the ownership of and certain insurance policy provisions regarding geothermal energy and associated resources." It was filed without the Governor's signature on 06/18/2023 and took effect immediately.
- **Ownership rule.** New Nat. Res. Code §141.004(a): geothermal energy and associated resources belong to the landowner, or, where surface and minerals are severed, **to the surface estate owner**. This holds "except as otherwise expressly provided by a conveyance, contract, deed, reservation," exception, limitation, lease or "other binding obligation."
- **Carve-outs (§141.004(c)).** The rule does not apply to minerals dissolved in groundwater, including in hot brines. It leaves unchanged:
  - the ownership and use of groundwater;
  - oil, gas or mineral extraction "regardless of its heat or energy potential";
  - the dominant/servient-estate rule. In Texas the mineral estate stays dominant, so the oil company's surface-use rights still win.
- **Definitions.** "By-product" excludes Property Code §75.001 minerals and oil and gas (§141.003(5)).
- **Title insurance.** Insurers may except "geothermal energy and associated resources" from coverage.
- **Why it matters.** Texas is the clearest "rancher owns the heat" state. Its millions of oil and gas wells with bottom-hole temperatures are exactly the illegible public dataset. The weak spots: brine minerals such as lithium are excluded, and a producing operator's dominant estate can constrain surface use.

### Nevada: real-property owner by default, with water law layered on top
- **NRS 534A.050:** "The owner of real property owns the rights to the underlying geothermal resources" unless "reserved by or conveyed to another person."
- **NRS 534A.010:** the resource is the natural heat of the earth, plus the energy, pressure and dissolved minerals of the heat-transfer medium. It excludes hydrocarbons and helium.
- **NRS 534A.040:** consumptive water brought to the surface is subject to water appropriation (NRS 533/534). Water produced and **reinjected into the same aquifer or reservoir is exempt**, as are reasonable test losses.
- **Practical effect:** a closed-loop or reinjecting binary plant on private fee land needs only the landowner's lease. The catch is that a large share of Nevada private land carries federal mineral reservations; see §3.

### Oregon: surface owner
- **ORS 522.035:** "Ownership rights to geothermal resources shall be in the owner of the surface property underlain by the geothermal resources" unless "otherwise reserved or conveyed." The state's own rights are preserved.

### Idaho: sui generis
- **Idaho Code §42-4002(c):** "Geothermal resources are found and hereby declared to be sui generis, being neither a mineral resource nor a water resource." Idaho also regulates them in part through the Department of Water Resources (Title 42).
- Who owns them between surface and mineral owners is handled elsewhere in the code. Common commentary says the surface owner, absent a reservation **(unverified)**.

### Utah: heat and fluid split; the fluid is a water right
- The Utah Geothermal Resource Conservation Act (Title 73, Ch. 22, administered by the **Division of Water Rights**) was amended by **Ch. 477, 2026 General Session**, effective 5/6/2026. Under §73-22-3 as amended:
  - "geothermal resource" is "the natural heat of the earth at temperatures greater than 100 degrees centigrade," now explicitly including energy recovered through enhanced or advanced systems;
  - that definition "does not include a geothermal fluid";
  - "geothermal fluid" is water and steam above 100 °C naturally in the system, and a "water right" expressly includes geothermal fluid;
  - "owner" is a person with "the right to drill into, produce, and make use of a geothermal resource";
  - owners in a geothermal area hold correlative rights to a fair share.
- **Practical effect:** in Utah you need both a heat lease from the landowner and a water-right appropriation for the fluid. Utah's fluid-as-water framing goes back to 1981 **(unverified detail)**.

### California: geothermal follows the "minerals" (case law, no statute)
- ***Geothermal Kinetics, Inc. v. Union Oil Co.*, 75 Cal.App.3d 56 (1977).** The issue was "whether geothermal resources belong to the owner of the mineral estate or the owner of the surface estate." The court held that a general grant or reservation of minerals carries geothermal resources, so **the mineral estate owner wins**.
- ***Pariani v. State of California*, 105 Cal.App.3d 923 (1980).** Applying *Geothermal Kinetics*, the court upheld a judgment "that the mineral rights reservations in the patents reserved to the State" the geothermal resources. The State wins on former state school lands.
- ***United States v. Union Oil Co. of California*, 549 F.2d 1271 (9th Cir. 1977).** The Stock-Raising Homestead Act (SRHA) mineral reservation includes geothermal steam. This is the Geysers case: **the federal government owns geothermal under SRHA patents**.
- ***Occidental Geothermal v. Simmons*, 543 F.Supp. 870 (N.D. Cal. 1982)** involved the same split-estate pattern on SRHA land.
- **Practical effect:** in California, the rancher often does **not** own the heat if minerals were ever severed. Expect quiet-title work, and expect BLM or the State Lands Commission as lessor on reserved lands.

### New Mexico: mixed; federal SRHA reservation is decisive
- ***Rosette, Inc. v. United States*, 277 F.3d 1222 (10th Cir. 2002)** ruled "in favor of the United States as to the ownership of geothermal resources on property obtained pursuant to patents" under the SRHA. This is the Lightning Dock area in Hidalgo County, which Zanskar now operates.
- A state-court companion is *Rosette v. DOI*, 2007-NMCA-136.
- NM's Geothermal Resources Conservation Act (NMSA 71-5) treats low-temperature geothermal water partly under State Engineer water jurisdiction **(unverified specifics)**.
- 2023's HB 365 created a Geothermal Center of Excellence at NM Tech, a project fund and a revolving loan fund. It did not change ownership.

### Other states (unverified; for follow-up)
- **Hawaii:** the state reserves geothermal as a "mineral" on most lands (HRS ch. 182). The fetch was blocked, so this is unverified.
- **Colorado:** geothermal fluid is tied to groundwater law (CRS 37-90.5) **(unverified)**.
- **Louisiana and Gulf Coast:** geopressured brine is treated like minerals. There is an OSTI 1978 study on legal problems in Louisiana; contents not read.

## 3. The federal split-estate overlay (the biggest trap for "lease from ranchers")

- The **Stock-Raising Homestead Act of 1916** reserved "all coal and other minerals" to the United States. Courts in the 9th Circuit (*Union Oil*, 1977) and 10th Circuit (*Rosette*, 2002) hold that this includes geothermal.
- So across large parts of NV, NM, UT, CA, OR and ID, a rancher with an SRHA patent owns the surface but **the US owns the heat**. The right must come from BLM.
- OSTI record 6465469 (1981), "Impact of geothermal development on stockraising homestead landowners," documents surface-use and compensation fights at The Geysers between SRHA surface owners and federal geothermal lessees.
- **Federal benchmark terms** (43 CFR 3211.11, 3211.17; govinfo CFR 2023):

| Term | Competitive lease | Noncompetitive lease |
|---|---|---|
| Rent, year 1 | $2/acre | $1/acre |
| Rent, years 2–10 | $3/acre | $1/acre |
| Rent after year 10 | $5/acre | $5/acre |

  - Electricity royalty: **1.75% of gross proceeds for the first 10 years of production, 3.5% thereafter**. If you sell the fluid at arm's length to a generator instead, the royalty is 10%.
  - Maximum lease size is **5,120 acres**; the primary term is 10 years (43 CFR 3206.12, 3200.1).

## 4. Can you lease from ranchers cheaply? Yes. Hard numbers from filings

Raser Technologies, 10-K for FY2009 (SEC):
- **Klamath Falls, OR:** $10,000 bonus for 984 acres of private farm, 10-year initial term, $1,000/yr delay rental, royalty "based on a percentage of electrical sales." That is about **$10/acre bonus and $1/acre/yr**.
- **Truckee area, NV:** $5,000 total for seven leases covering **4,444 acres**, 50-year terms, delay rentals of $4,444/yr. That is **about $1/acre bonus and $1/acre/yr**.
- **Trail Canyon:** $15,000 bonus for 560 acres, 15-year initial term (about $27/acre).
- **Greater Thermo, UT:**
  - three private leases cost $41,200 for **about 10,800 acres** (about $3.8/acre), with $33,300/yr total rentals (about $3/acre/yr) and 5–10 year terms;
  - the core Thermo lease on a 75% undivided interest carried rent of **$1.00/acre**;
  - additional private and state agreements covered about 35,000 acres;
  - each 10–11 MW plant needs under 1,000 acres.
- **Truckee (Dec 2006):** a $25,000 bonus plus 25,000 shares (fair value $115,250). Equity kickers do happen.

US Geothermal 10-K (FY2017) royalty schedules:
- **Neal Hot Springs, OR** (about 7,429 acres of geothermal water rights): one lease pays 3% of gross proceeds for the first 5 years, 4% for the next 10, then 5%. Another pays 2% of revenue for 10 years, then 3%.
- A private lease at another project pays 3% of gross for 10 years, then 4%.
- **Raft River, ID** (about 5,144 acres): six contracts pay 10% of net income.
- **The Geysers:** USG acquired leases on 3,809 acres in 2014.
- A third-party overriding royalty on a BLM lease was 4% of gross for power and 5% for direct use.

Ormat 10-K (FY2025):
- About **434,430 domestic acres**: about **78% BLM**, **18% leased or subleased from private landowners or leaseholders**, 4% owned.
- Private leases have 5–30 year primary terms, held by production. Royalty is a percentage of value "at the well," of gross proceeds or of gross revenues.
- "In many cases, the lessor under these private geothermal leases owns only the geothermal resource and not the surface." Ormat can buy or lease the subsurface right separately.
- **Royalties were about 4.5% of Electricity segment revenue in 2025** (4.6% in 2024), blended across federal, county and private leases.

Other:
- *R & R Energies v. Mother Earth Industries*, 936 P.2d 1068 (Utah 1997): a Cove Fort steam fee of **$0.015/kWh**, an example of a resource-owner payment set per unit of output.

**So typical private terms are:**
- bonus of $1–$30/acre;
- delay rental of about $1–$3/acre/yr;
- primary term of 5–50 years, held by production;
- royalty of **2–5% of gross electricity revenue**, often stepping up after 5–10 years.

That makes the brief's "1–3%" guess too low for private land. The federal rate (1.75% then 3.5%) is at the bottom of the range. Entry is very cheap: **about $5k–$40k controlled roughly 1,000–10,000 acres** in 2007–2008.

## 5. Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **The "buy the right before proof" mechanic exists and is cheap on private land.**
   - Thousand-acre blocks have been tied up for four- to five-figure bonuses and about $1/acre/yr rent, with 2–5% royalties paid only after production.
   - That is cheaper per acre than BLM competitive sales, where bonus bids can be large on hot parcels, and far faster: no NEPA-gated nomination, no auction, no public signal to competitors.
   - Like Terranox's pre-proof mineral claims, the option value accrues to the lessee.
2. **Jurisdiction choice is the edge. Texas is the standout.** Since SB 785 (June 2023), the *surface* owner holds the heat even on severed estates, and Texas has the deepest archive of well logs and bottom-hole temperatures.
   - A company could systematically lease heat rights from Texas surface owners. The leases would be cheap, legally clean and statute-backed, and sit above ML-identified sedimentary or geopressured anomalies.
   - Oregon and Nevada are also surface or real-property-owner states. Nevada exempts reinjected water from appropriation.
3. **The trap that becomes a moat: title work.**
   - In CA, NM and the SRHA-heavy West, the rancher frequently doesn't own the heat; the US or the state does, through mineral reservations (*Union Oil*, *Pariani*, *Rosette*).
   - An ML-plus-title pipeline would read county records, BLM Master Title Plats and patent type (SRHA vs cash entry vs railroad grant) together with the subsurface data. It would sort targets into lease-from-landowner, BLM-nominate and state-lease buckets. That joins two illegible public datasets, which is exactly the Terranox pattern.
4. **The gap vs Zanskar.**
   - Zanskar's public story centres on Great Basin hydrothermal and federal BLM land, plus buying an operating plant (Lightning Dock, NM, which itself sits on SRHA-reserved federal geothermal per *Rosette*). In that model Zanskar finds the resource and then develops it as an operator.
   - The gap is a **land-bank or royalty model on private and Texas surface-owned heat**: acquire many cheap private leases before proof, de-risk with data, then sell or farm out to developers (Fervo, Sage, Ormat, oil and gas majors moving into geothermal). Keep an override of 1–3% on top of the landowner's 2–5%.
   - Ormat's 18% private and leasehold-sublease acreage and the third-party overrides in USG's filings show this aggregator and override layer already exists informally. Nobody has industrialised it with ML.
5. **Risks to price in.**
   - Texas dominant-estate oil and gas operations can interfere with surface use.
   - Brine-mineral upside such as lithium is excluded from the Texas heat right.
   - Utah's fluid-as-water-right means a second permit layer.
   - Short primary terms (5–10 years) put a clock on proof, as in mining.
   - Landowners who learn of a discovery will demand higher royalties at renewal, so lock in long terms with options up front.

## Sources
- Texas SB 785 (88R) bill history: https://capitol.texas.gov/BillLookup/History.aspx?LegSess=88R&Bill=SB785
- Texas SB 785 enrolled text: https://capitol.texas.gov/tlodocs/88R/billtext/html/SB00785F.htm
- Texas SB 785 companion (HB 1336): https://capitol.texas.gov/BillLookup/Companions.aspx?LegSess=88R&Bill=SB785
- Texas HB 1818 (88R) is a tax-rate bill: https://capitol.texas.gov/BillLookup/History.aspx?LegSess=88R&Bill=HB1818
- Tex. Nat. Res. Code §141.003: https://texas.public.law/statutes/tex._nat._resources_code_section_141.003
- Nevada NRS 534A: https://www.leg.state.nv.us/NRS/NRS-534A.html
- Oregon ORS 522.035: https://oregon.public.law/statutes/ors_522.035
- Idaho Code §42-4002: https://legislature.idaho.gov/statutesrules/idstat/title42/t42ch40/sect42-4002/
- Utah Code §73-22-3 (2026 version): https://le.utah.gov/xcode/Title73/Chapter22/C73-22-S3_2026050620260506.html
- Utah Code §73-22-2 (2026 version): https://le.utah.gov/xcode/Title73/Chapter22/C73-22-S2_2026050620260506.html
- NM HB 365 (2023): https://www.nmlegis.gov/Sessions/23%20Regular/final/HB0365.pdf
- Geothermal Kinetics v. Union Oil (1977): https://www.courtlistener.com/opinion/2173099/geothermal-kinetics-inc-v-union-oil-co/
- Pariani v. State of California (1980): https://www.courtlistener.com/opinion/2156691/pariani-v-state-of-california/
- Occidental Geothermal v. Simmons (1982): https://www.courtlistener.com/opinion/1460931/occidental-geothermal-inc-v-simmons/
- CourtListener search incl. US v. Union Oil 549 F.2d 1271 and Rosette 277 F.3d 1222: https://www.courtlistener.com/api/rest/v4/search/?q=%22Union%20Oil%22%20%22Stock-Raising%20Homestead%20Act%22%20geothermal%20steam%20mineral%20reservation&type=o
- R & R Energies v. Mother Earth Industries (Utah 1997): https://www.courtlistener.com/opinion/1224637/r-r-energies-v-mother-earth-industries-inc/
- 43 CFR Part 3200 (govinfo 2023): https://www.govinfo.gov/content/pkg/CFR-2023-title43-vol2/xml/CFR-2023-title43-vol2-part3200.xml
- OSTI 6465469, SRHA landowners and geothermal (1981): https://www.osti.gov/api/v1/records/6465469
- Ormat 10-K FY2025: https://www.sec.gov/Archives/edgar/data/1296445/000129644526000006/ora-20251231.htm
- US Geothermal 10-K FY2017: https://www.sec.gov/Archives/edgar/data/1172136/000106299318001121/form10k.htm
- Raser Technologies 10-K FY2009: https://www.sec.gov/Archives/edgar/data/1103078/000119312510060692/d10k.htm
