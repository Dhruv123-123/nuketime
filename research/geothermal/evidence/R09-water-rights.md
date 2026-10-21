# R09: Water rights as a constraint on geothermal (NV, UT, ID, federal), and is the water right the hidden cheap right?

**Research note:** the shared WebSearch budget for this workflow turn ran out before this agent's first query. All findings below come from direct WebFetch of primary statute and agency pages (Nevada Legislature, Utah Legislature, Utah Division of Water Rights, Idaho Legislature, Cornell LII US Code, OSTI/Argonne, NREL OpenEI RAPID). Anything not backed by one of those fetches is marked (unverified). Market prices for water rights and specific protest case histories could not be checked; they should be re-researched in a follow-up turn.

## 1. Bottom line

- **Nevada: the water right is mostly not needed.** Geothermal fluid that is produced and reinjected into the same aquifer or reservoir is exempt from water appropriation (NRS 534A.040). Only *consumptive* use of water brought to the surface outside a geothermal well goes through the ordinary NRS 533/534 appropriation process. In a Nevada binary or flash project with full reinjection, the heat right is the BLM or private geothermal lease. The water right covers only makeup, cooling and construction water. Ownership of the heat follows the land (NRS 534A.050).
- **Utah: two separate rights.** Utah law separates the *geothermal resource* (heat above 120°C; ownership "derives from an interest in land and not from an appropriative right", Utah Code 73-22-4) from the *geothermal fluid* (water and steam above 120°C, held by an "appropriative right to geothermal fluids"). Direct-use and open-loop systems need a Title 73 water right. Power production is governed by the Geothermal Resource Conservation Act and R655-1. A Utah developer needs both the land or lease right and a water appropriation. Chapter 73-22 was amended in 2026: the 2026 versions of 73-22-2 and 73-22-4 are marked "Superseded 5/6/2026". The new text was not retrieved (unverified what changed).
- **Idaho: the heat is acquired through water law.** Low-temperature geothermal is acquired *by appropriation* (Idaho Code 42-233), valued "primarily for heat value and secondarily for the value as water", with a well bond of $5,000 to $20,000.
- **Federal:** the Geothermal Steam Act takes no position on whether the US is exempt from state water law (30 USC 1021). A BLM geothermal lease does not convey a state water right. Federal lessees still go through the state engineer for any consumptive water (RAPID roadmap structure; the exact eCFR text was blocked).
- **Is the water right the hidden cheap fixed-fee right?** Only partly, and not in the form Terranox needs. Filing fees are trivially cheap, a few hundred dollars. But appropriation law blocks speculative holding. Rights come with diligence deadlines and are lost if the water is not put to use. They are first-in-time on unappropriated water, which is scarce in most Nevada and Utah basins. In Nevada the fluid itself doesn't need one. So the water right is a **gating constraint and a possible blocking position**, not the asset itself.

## 2. Nevada in detail

**Statute (NRS 534A, fetched):**
- NRS 534A.010 defines a geothermal resource as "the natural heat of the earth and the energy associated with that natural heat", plus pressure and dissolved minerals, excluding hydrocarbons and helium. https://www.leg.state.nv.us/NRS/NRS-534A.html
- NRS 534A.040 applies NRS 533/534 appropriation *only* to "consumptive uses of water brought to the surface outside of a geothermal well". Water reinjected into the same aquifer or reservoir is exempt. So are reasonable losses during well testing or temporary system failure.
- NRS 534A.050: landowners own the geothermal resource unless it was reserved or conveyed. This makes geothermal a land or mineral-like right in Nevada. That matters for a Terranox model: private severed geothermal rights are the thing to buy.
- NRS 534A.060/070: drilling permits come from the Division of Minerals. Exploratory well applications must be decided within **10 days** (permits last up to 2 years). Production well applications must be decided within **90 days**, with State Engineer consultation.
- NRS 534A.080: permit fees may be based partly on acreage.
- NRS 534.050: the State Engineer may *waive* the groundwater permit for temporary water use "exploring for water, oil, gas, minerals or geothermal resources", in both designated and undesignated basins. Exploration-phase drilling water is therefore cheap and quick to get. https://www.leg.state.nv.us/NRS/NRS-534.html

**When a Nevada project does need a water right** (makeup water for evaporative cooling, EGS fluid losses, construction), the process is as follows (RAPID 19-NV-a/b; NRS 533):
- Most Nevada water is already appropriated. The usual route is to buy or lease an existing right and file a change application (NRS 533.345), not to make a new appropriation. https://openei.org/wiki/RAPID/Roadmap/19-NV-a
- Steps: the application is published for 4 consecutive weeks. **Protests** must be filed within **30 days** of the last publication (NRS 533.365). If a hearing is held, the decision is due within 240 days of the hearing record. Overall the State Engineer generally acts within **2 years** of the protest deadline. Construction must be done within 5 years and beneficial use proven within 10 years, or the permit is cancelled. https://openei.org/wiki/RAPID/Roadmap/19-NV-b
- Rejection grounds (NRS 533.370): no unappropriated water, conflict with existing rights, threat to domestic wells, or harm to the public interest. Interbasin transfers face extra tests. NRS 533.372 lets the State Engineer approve or deny water for **energy generated for export from Nevada** "based upon the public interest and the economic welfare of the State". That is a discretionary political hook for data-centre or California-bound power. https://www.leg.state.nv.us/NRS/NRS-533.html
- Critical management areas (NRS 534.110(7)) cover basins where pumping exceeds perennial yield. After 10 years, use is curtailed to senior priorities unless a management plan is in place. Junior geothermal makeup rights in such basins are at risk.

**Fees (NRS 533.435, fetched):**

| Item | Fee |
|---|---|
| Application to appropriate | $360 (incl. $50 publication) |
| Permit issuance, general | $360 + $3 per acre-foot |
| Change application | $240; temporary change $180 |
| Change permit issuance | $300 + $3/AF |
| Certificate | $350 |

A 1,000 AF/yr makeup-water right costs roughly $360 + $3,360 ≈ **$3.7k in state fees**. The fees are negligible. The real costs are buying an existing right in an over-appropriated basin (market price per AF, unverified), engineering and hydrology studies, protest litigation, and time.

## 3. Utah in detail

- Utah Division of Water Rights (State Engineer) regulates all geothermal drilling and production. https://waterrights.utah.gov/geothermal/
- Thresholds and rules: high-temperature means above 120°C (248°F), covering flash, binary, EGS and deep closed-loop. Closed-loop heat pumps need no water right. Open-loop and direct-use systems need a Title 73 water right, and open-loop systems must reinject into the same aquifer (a non-consumptive right). Power production falls under the Geothermal Resource Conservation Act (73-22) and rule R655-1.
- Definitions (73-22-3, pre-2015 version): "geothermal resource ... does not include geothermal fluids". Geothermal fluid means water and steam above 120°C. **Correlative rights** give each owner a fair share of a shared reservoir, without waste. https://le.utah.gov/xcode/Title73/Chapter22/C73-22-S3_1800010118000101.html
- Ownership (73-22-4): it "derives from an interest in land and not from an appropriative right". The chapter applies to federal and Indian lands as far as law allows. https://le.utah.gov/xcode/Title73/Chapter22/C73-22-S4_1800010118000101.html
- Appropriation process (RAPID 19-UT-a): file with the State Engineer and advertise for 2 weeks. **Protest within 20 days** (informal) or 30 days (formal) (Utah Code 73-3-7). To be approved, the applicant must show unappropriated water, no impairment of existing rights, feasibility, *financial ability and good faith*. Typical time is **90 to 180 days**, before perfection by proof of beneficial use. https://openei.org/wiki/RAPID/Roadmap/19-UT-a
- The "good faith / financial ability" test is an anti-speculation filter. You cannot stack up water applications as cheap options without a real project (Utah 73-3-8 anti-speculation language, unverified exact text).
- Basin closure: much of the Escalante Valley/Milford area, where Fervo Cape Station and Utah FORGE sit, is under groundwater management restrictions (unverified; the Division's area-policy map could not be parsed). So EGS makeup water there generally has to come from purchased or changed existing rights.

## 4. How much water geothermal actually uses

Argonne's ANL/EVS/R-10/5 (Clark, Harto, Sullivan and Wang, 2010), operational consumption:
- Flash: about **0.01 gal/kWh**. Flash also loses about **2.7 gal/kWh** of geofluid to evaporation. That is reservoir fluid loss, not makeup water.
- Binary: about **0.27 gal/kWh**
- EGS: **0.29 to 0.72 gal/kWh**
https://www.osti.gov/biblio/1013997

Worked example for a 100 MW EGS plant at a 90% capacity factor (about 788 GWh/yr): 0.29 to 0.72 gal/kWh gives about 229 to 567 million gal/yr, roughly **700 to 1,740 AF/yr**. That is real but modest, about the water for 150 to 400 acres of irrigated alfalfa at roughly 4 to 4.5 AF/acre (unverified agronomic figure). Buying it means buying out a few farms' rights, not a first-order cost. For hydrothermal binary with full reinjection and air cooling, consumptive water is near zero and, in Nevada, is statutorily exempt.

## 5. Protests and conflict: what the record shows

- Statutory protest windows are short: 30 days in Nevada, 20 to 30 days in Utah. Protests trigger hearings that can stretch decisions to 240 days or more after the hearing (Nevada).
- Specific geothermal water-right protest cases could not be retrieved this turn. Examples to check include ranchers and tribes contesting makeup water and spring-impact claims near Dixie Valley and the Fallon area (unverified). The well-known Dixie Meadows fight (Ormat, Dixie Valley toad, 2022) was an ESA and NEPA challenge on BLM land, not a water-right protest (from background knowledge, unverified here).
- The main water-related risk for hydrothermal projects is **spring and surface-water impact claims** (hot springs, wetlands, tribal cultural springs), raised through NEPA, ESA and public-interest rather than the water right itself.

## 6. Is the water right the hidden cheap fixed-fee right? Assessment

| Test | Nevada | Utah | Idaho |
|---|---|---|---|
| Needed to own the heat? | No (land/lease) | No (land/lease), but fluid right separately needed | Yes, for low-temperature (appropriation) |
| Cost to file | ~$360 + $3/AF | Fee schedule (amounts unverified), low | Low + $5k to $20k well bond |
| Can it be held speculatively? | No: 5-yr build, 10-yr beneficial use | No: good faith + financial ability tests | No: application-permit-license with proof |
| First-in-time priority value? | Low (reinjection exempt) | **Moderate**: a senior fluid appropriation in a contested reservoir is a blocking position | Moderate |
| Blocking value | Makeup water in closed basins | Fluid plus makeup in closed basins | Heat itself |

Verdict: the water right is **not** a standalone cheap option to buy before proof. It is the opposite of a Saskatchewan mineral claim. Water rights are use-it-or-lose-it, publicly noticed, protestable, and judged on good faith. Two narrower angles do hold up:
1. **Utah's split right is an opening.** Where the heat sits under federal or state land, a party holding the senior *fluid appropriation*, or the only purchasable senior groundwater rights in a closed basin, can extract value from whoever leases the heat. This works best combined with the lease, not as a pure play.
2. **Owned makeup water is a real de-risking input for EGS** (Fervo-style projects need about 700 to 1,700 AF/yr per 100 MW). Holding pre-positioned, changeable, senior agricultural rights in the right basins adds sale value to a de-risked site package. It raises the step-up when you sell to Fervo, Ormat or a utility.

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

- **The water right won't do the job the Saskatchewan mineral claim does.** The cheap asset to buy before proof is still the **BLM competitive lease** (bid in nominations), **state trust land leases**, or **private severed geothermal rights**. In Nevada, NRS 534A.050 attaches geothermal to the land estate, so private heat rights can be bought directly. Water law then adds almost no friction for reinjected hydrothermal projects: the fluid is exempt and exploration water can be waived.
- **The water right belongs in the bundle as a value-add.** The sellable "proven state" should be lease + permits + **water (makeup rights already acquired or under change application) + transmission position**. Buyers pay for packages they can permit. Because state fees are minimal ($3.7k for 1,000 AF in Nevada), the cost is purchasing existing ag rights. Those are often cheaper in rural closed basins than the value they unlock (prices unverified; research next).
- **Utah strategy:** in Utah, file the fluid appropriation early, as soon as there is a good-faith project. That locks in priority over later entrants on the same reservoir, alongside correlative-rights claims. It is cheap, but the diligence clock has to be managed.
- **Data/ML angle:** the State Engineer databases are a public-but-illegible dataset too. Nevada NDWR and Utah DWR water-right registries hold points of diversion, well logs, temperatures and priority dates. Fusing them with geothermal favourability maps can show which prospects have buyable senior rights and which basins are closed. It can also flag "water-ready" blind systems. This is a data moat in the same spirit as Terranox's assessment-file mining.
- **Gap vs Zanskar:** Zanskar finds and develops (Big Blind, Lightning Dock) as an operator. It owns plants and bears the full development, permitting and water-integration cost itself. Its edge is exploration science. There is no public sign it sells de-risked, permit-ready packages, including water, to EGS developers and data-centre offtakers (unverified). The gap is an asset-light-ish **land + water + permit bank**: acquire rights cheaply before proof, prove them with ML and cheap temperature-gradient holes, assemble the water and permits, and flip at the step-up. Water-rights assembly in closed Great Basin basins is slow, local, relationship-heavy work that a science-led operator is unlikely to prioritise. That makes it a defensible complement, though it is not itself the cheap option.
- **Risks to underwrite:** NRS 533.372 gives the State Engineer discretion over water for power exported from Nevada. Critical-management-area curtailment threatens junior rights. Spring-impact claims through NEPA/ESA are the real protest vector. The 2026 Utah 73-22 amendments are unread and need checking.

## Sources

- Nevada NRS 534A (geothermal): https://www.leg.state.nv.us/NRS/NRS-534A.html
- Nevada NRS 533 (appropriation, protests, fees 533.435, energy export 533.372): https://www.leg.state.nv.us/NRS/NRS-533.html
- Nevada NRS 534 (groundwater, exploration waivers 534.050, CMAs 534.110): https://www.leg.state.nv.us/NRS/NRS-534.html
- NREL OpenEI RAPID, Nevada geothermal water rights: https://openei.org/wiki/RAPID/Roadmap/19-NV-a
- NREL OpenEI RAPID, Nevada appropriation process: https://openei.org/wiki/RAPID/Roadmap/19-NV-b
- NREL OpenEI RAPID, Utah water rights: https://openei.org/wiki/RAPID/Roadmap/19-UT-a
- Utah Division of Water Rights, geothermal: https://waterrights.utah.gov/geothermal/
- Utah Code 73-22-3 (definitions): https://le.utah.gov/xcode/Title73/Chapter22/C73-22-S3_1800010118000101.html
- Utah Code 73-22-4 (ownership): https://le.utah.gov/xcode/Title73/Chapter22/C73-22-S4_1800010118000101.html
- Utah Code 73-22-2 (purpose): https://le.utah.gov/xcode/Title73/Chapter22/C73-22-S2_1800010118000101.html
- Idaho Code 42-233: https://legislature.idaho.gov/statutesrules/idstat/title42/t42ch2/sect42-233/
- 30 USC 1001 and 1021 (Geothermal Steam Act): https://www.law.cornell.edu/uscode/text/30/1001 , https://www.law.cornell.edu/uscode/text/30/1021
- Clark et al. 2010, Argonne ANL/EVS/R-10/5, water use in geothermal: https://www.osti.gov/biblio/1013997
