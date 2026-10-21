# D09 — Europe: geothermal data openness and rights regimes (DE, NL, UK, FR). Is there a land-first play?

**Research caveat.** The shared WebSearch budget for this workflow run was already used up when this agent started: every search returned "budget used up". Direct WebFetch of primary sources mostly worked for NLOG, UKOGL, BGS, geothermie.de and Vulcan. It failed (503/403/bot-wall) for gesetze-im-internet.de, buzer.de, BMWK, BRGM InfoTerre and geothermies.fr. So the statutory numbers for Germany and France below come from prior knowledge and are marked **(unverified)**. Anything marked (verified) was read on the cited page during this run. A follow-up run with search budget should confirm the German BBergG §§14/16/30/31 numbers, the GeolDG release periods and the French Code minier durations.

---

## 1. Netherlands: the most open data regime in Europe

**Data openness (verified).** NLOG is the national portal run by TNO for the Ministry. It publishes borehole, seismic, production/injection, field, model and core data for oil, gas, geothermal, storage and salt. On wells it says: "Well log measurements and reports are available after the confidentiality period of five years has expired." Administrative well data is always public. Per borehole you get composite logs (TIF/PDF), digital LIS/LAS curves, Rock-Eval and vitrinite reflectance, core measurements, lithostratigraphy and deviation. Deviation, gas composition, poro/perm, Rock-Eval, stratigraphy and vitrinite can be downloaded as national spreadsheets covering all boreholes (https://www.nlog.nl/en/boreholes). This is about the same as Saskatchewan's 3-year SMAD rule (5 years vs 3), and it is already digitised: LAS curves and spreadsheets, not scanned paper.

**State-funded de-risking already public (verified).** SCAN (Seismische Campagne Aardwarmte Nederland) is run by TNO and EBN from 2019. It acquires new 2D seismic and reprocesses legacy seismic in data-poor areas, plus some exploration wells (e.g. BHG-01, LTG-01). "All research data and final results" are made public, and the seismic is on NLOG (https://www.nlog.nl/en/scan). WarmingUP (2020–2023, 38 participants) and its follow-on WarmingUP-GOO (geothermal; data inventory for the Upper North Sea Group delivered January 2024; a geothermal "digital twin" shown at EGC 2025) add more public geothermal knowledge (https://www.warmingup.info/). TNO's ThermoGIS public potential maps also exist **(unverified URL/details: thermogis.nl)**.

**Rights regime (verified structure).** NLOG says producing geothermal heat under the Mining Act (Mijnbouwwet) now takes four licence steps. The amended geothermal chapter is in force:
1. search area allocation;
2. start licence;
3. agreement with a geothermal energy operator;
4. follow-up licence.

An environmental permit (omgevingsvergunning mijnbouw) is also needed. Applications are published in the Staatscourant, and **there is a call for competing applications** on the area still open (https://www.nlog.nl/en/geothermal-licences). The Minister of Economic Affairs and Climate decides, so this is a discretionary award, not first-come staking.

**Resource character.** The resource is low-enthalpy sedimentary aquifers at 40–100 °C, produced with doublets. Deeper (>120 °C) Rotliegend, Triassic and Dinantian targets are being studied (https://www.nlog.nl/en/geothermal-energy). The sector says geothermal could meet about a quarter of Dutch heat demand and more than half of greenhouse sustainable heat (https://www.geothermie.nl/). Commercial production started in 2007. About 25–30 operating doublets and about 6–8 PJ/yr of heat **(unverified)**. Masterplan targets are about 50 PJ by 2030 and about 200 PJ by 2050 **(unverified)**. EBN, the state participant, is set to take minority stakes in geothermal projects, as it does in gas **(unverified)**.

**Land-first?** Weak. (a) The data is already open and the aquifer potential is already mapped by the state (ThermoGIS/SCAN), so the "hidden resource" edge is small. (b) The award is discretionary and competitive, and it rewards a credible operator, a financing plan and a heat customer, not a cheap filing. (c) The buyer is a local heat network or greenhouse cluster, so it is a local monopsony. (d) It is heat-only, with SDE++ subsidy economics. What the Netherlands does offer is the best **open European training set**: thousands of digital LAS logs, BHTs, core poro/perm and production/injection data, all licensable for ML.

## 2. Germany: Bergrecht, first-come exploration permits, the closest European analogue to staking

**Legal status (verified).** Deep geothermal (Erdwärme) is a *bergfreier Bodenschatz*. That means it does **not** belong to the landowner, and mining law (Bundesberggesetz, BBergG) governs it. The Vierte Bürokratieentlastungsgesetz set a national threshold: shallow geothermal down to **400 m** generally needs no mining entitlement (Bergbauberechtigung) and no operating plan (https://www.geothermie.de/bibliothek/lexikon-der-geothermie/b/bergrecht). The structure is close to Saskatchewan's: the state owns the resource, and you buy a right to a *Feld* (field) from the Land mining authority (Bergamt / LBEG / LGRB / LfU). Ownership of the surface does not matter for the subsurface right.

**Rights mechanics (unverified, BBergG text not fetchable this run):**
- *Erlaubnis* (exploration permit, §7). Up to **5 years**, extendable by up to 3 years at a time (§16(4)). Priority goes to the first complete application if several are made for the same field (§14 Vorrang).
- *Bewilligung* / *Bergwerkseigentum* (production right, §8/§9). Normally up to **50 years** (§16(5)). Bergwerkseigentum is a transferable property-like right that can be mortgaged.
- *Feldesabgabe* (field fee, §30). Very low statutory scale, on the order of €5/km² in year 1 rising to about €25/km² **(unverified)**. *Förderabgabe* (production royalty, §31) is 10% of market value by default, but the Länder have widely exempted Erdwärme **(unverified)**.
- Refusal grounds (§11) include no credible work programme, no financing, and overriding public interest. The permit can be revoked if the work is not done (§18) **(unverified)**. So pure warehousing is possible for a few years but is legally fragile.

**Market evidence that "claim first" happens in Germany.** In the Upper Rhine Graben (URG), Vulcan Energy and others filed large Erlaubnis positions for combined geothermal and lithium brine *before* proving them, and the permit map is now dense. Vulcan's Lionheart project (between Karlsruhe and Landau) is described as 24,000 tpa LiOH, 275 GWh/yr renewable electricity and 560 GWh/yr heat. It has an A$3.9 bn financing package and targets commercial production in H2 2028 (verified: https://www.v-er.eu/projects/lionheart). That is a step-up from cheap Erlaubnis to a multi-billion asset, which is the Terranox playbook. But the URG was found by the lithium-brine thesis, not by ML. The Bavarian Molasse (Munich area) is also heavily permitted: Unterhaching uses about 38 MWth for district heat (verified: https://en.wikipedia.org/wiki/Geothermal_energy_in_Germany), and Stadtwerke München holds a large position **(unverified)**.

**Data openness.** The Geologiedatengesetz (GeolDG, 2020) requires all drilling and geophysical data to be submitted to the state geological surveys. It sorts data into *Nachweisdaten* (metadata, public quickly), *Fachdaten* (raw measurements) and *Bewertungsdaten* (interpretations). Non-state Fachdaten become public after a fixed period, roughly **5–10 years**, and Bewertungsdaten later, roughly **10–20 years**, with the longer periods for commercially generated data **(unverified, GeolDG §§27–34 not fetchable)**. Old hydrocarbon data falls under transition rules, and release of legacy industry 3D seismic has been contested **(unverified)**. In practice, the North German Basin (Lower Saxony, LBEG's hydrocarbon database) holds thousands of old oil and gas wells with BHTs and logs. Access is uneven by Land, much of it is paper or TIF, and public release has started only recently. This is **"public-but-illegible"**, which is the Terranox wedge.

**Policy tailwind (unverified).** The federal government has announced about 10 TWh/yr of geothermal heat by 2030 and about 100 additional projects. A Geothermie-Beschleunigungsgesetz (2025) declares geothermal an *overriding public interest* and speeds up Bergrecht and water-law approvals. Municipal heat-planning law (Wärmeplanungsgesetz) requires every municipality to produce a heat plan. That creates a long list of Stadtwerke buyers.

**Land-first?** **Yes, conditionally. Germany is the best European fit.** The right is state-owned, comes from cheap first-come field permits, is transferable as Bergwerkseigentum, and sits under thousands of legacy wells whose data is now entering public registers. The open space is outside the crowded URG and Molasse. Candidates: the North German Basin (Rotliegend/Buntsandstein, also lithium-bearing brines), the Thuringian Basin, and heat-demand clusters near large cities and industrial parks. The constraints are the work-programme and financing tests, revocation risk, induced-seismicity politics (Landau, Basel, Vendenheim), and the fact that the end buyer is mostly a municipal utility buying heat. Expected sale or JV value is in the tens of millions of euros per project, not hundreds of millions, unless lithium is a co-product.

## 3. United Kingdom: open data, but no right to stake

**Data (verified).** UKOGL gives free access to onshore 2D/3D seismic and well records, "supported by charitable donations", with the aim of making the subsurface record "freely available to all" (https://www.ukogl.org.uk/). BGS released a digital legacy geothermal catalogue (subsurface temperature, thermal conductivity, heat flow), with a second version in **June 2026**. It also runs a government-funded UK Geothermal Platform with an interactive map (https://www.bgs.ac.uk/geology-projects/geothermal-energy/). The NSTA National Data Repository holds released petroleum well data **(unverified detail)**.

**Rights (mostly unverified).** The UK has **no specific geothermal licensing regime**. Ownership of heat is legally unclear, and BGS's own page is silent on licensing (verified that it is silent). The Infrastructure Act 2015 gives a statutory right to use "deep-level land" below 300 m for petroleum or deep geothermal, which removes the trespass problem **(unverified)**. What actually gates a project is a surface lease from the landowner, planning permission (Cornwall Council approved United Downs and Eden in 2010, verified) and an Environment Agency abstraction or permit. United Downs (GEL) has a production well to 5,275 m and an injection well to 2,393 m, about 10 MWe / 60 MWth design, a budget of about £50 m, and per Wikipedia began generating in 2026 (https://en.wikipedia.org/wiki/Geothermal_power_in_the_United_Kingdom). A 2012 REA report estimated a technical potential of 9.5 GW electricity and >100 GW heat (same source).

**Land-first?** No state right exists to stake. You would be optioning surface land (as GEL did in Cornwall), which is landowner-by-landowner and gives no exclusivity over the resource. Not a Terranox shape.

## 4. France: Code minier, state-granted PER, data in BRGM BSS

**Rights (unverified, Légifrance and geothermies.fr unreachable).** Deep geothermal is a mining resource under the Code minier. Exploration needs a **permis exclusif de recherches (PER)**, granted by the State after a competition period, for up to about 5 years and renewable. Production then needs a **permis d'exploitation**, for up to about 50 years. Small-scale "géothermie de minime importance" (GMI; roughly <200 m and <500 kW) is a declaration regime. The 2022 Code minier reform added environmental and consultation requirements. Hydrocarbon exploration was ended by the 2017 Loi Hulot. That frees old hydrocarbon prospects, and their well data sits with BRGM / BEPH.

**Data (unverified, InfoTerre 503).** BRGM's Banque du Sous-Sol (BSS) via InfoTerre is a free national borehole register with a very large number of entries. Deep petroleum well logs are archived and become public after confidentiality, but much of it is scanned paper.

**Activity (unverified).** The Paris Basin Dogger aquifer has about 50+ district-heating doublets, the densest geothermal heat cluster in Europe. In Alsace (French URG), Soultz-sous-Forêts and Rittershoffen operate, Fonroche's Vendenheim project was halted after induced seismicity in 2020–21, and lithium players (Lithium de France, Eramet and others) have filed PERs. That is the same "claim before proof for Li+heat" behaviour as on the German side.

**Land-first?** Partial. PERs are state rights, but they are awarded through competition and the files are scrutinised. The political risk after Vendenheim is real. A plausible sub-play is the Alsace and Rhône-graben lithium-plus-heat PERs.

---

## 5. Cross-country scorecard

| Country | Who owns deep heat | Cheap pre-proof right? | Data openness | Hidden-resource edge | Exit buyers |
|---|---|---|---|---|---|
| Netherlands | State (Mijnbouwwet) | No: discretionary, competing calls, operator test | **Best**: 5-yr release, digital LAS (verified) | Low: aquifers mapped by TNO/SCAN | Heat networks, growers, EBN co-invest |
| Germany | State (*bergfrei*, verified) | **Yes**: first-come Erlaubnis, low field fee (unverified figures) | Improving (GeolDG); legacy hydrocarbon data illegible | **Medium-high** outside URG/Molasse | Stadtwerke, EnBW/E.ON-type utilities, lithium majors |
| France | State (Code minier) | Partial: PER after competition | BSS free; deep logs mostly scanned | Medium (Alsace, Paris Basin margins) | Engie/Dalkia-type heat networks, Li players |
| UK | Unclear; no regime | No: surface leases plus planning | Free (UKOGL, BGS) | Medium (Cornwall granites, basins) | Few; grant-dependent |

---

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **Europe is a second market, not the beachhead.** The US (BLM competitive geothermal lease sales, state trust land and private fee geothermal rights) remains the cleanest "buy the right cheaply, own the step-up" market. Europe adds one jurisdiction with the right legal shape, **Germany**. There deep heat is state-owned and *bergfrei*, exploration fields go by first-come Erlaubnis for a small field fee, and the production right (Bergwerkseigentum) is transferable, mortgageable property. That is structurally close to Saskatchewan mineral dispositions. The Netherlands, the UK and France either award rights at the Minister's discretion or have no stakable right.

2. **Germany's illegible legacy data is the Terranox wedge.** The GeolDG is pushing decades of hydrocarbon well data (BHTs, logs, cores) from the North German Basin and elsewhere into state registers. Much of it is paper or TIF and spread across Länder. The Netherlands proves the model: NLOG's 5-year release and fully digital LAS give a ready, open **training set** for BHT correction and temperature-at-depth models. Train on Dutch data, then transfer to German data, which is geologically continuous (Rotliegend, Buntsandstein) and much less read.

3. **The Upper Rhine already showed that claiming before proof works in Europe.** Lithium-brine developers like Vulcan blanketed the URG with Erlaubnis before proof. Lionheart (24 ktpa LiOH, 275 GWh power, 560 GWh heat, A$3.9 bn package) shows how big the step-up can be. The gap is that nobody is doing this systematically and data-first across the *rest* of Germany for heat-plus-lithium targets.

4. **The economics are different.** European deep geothermal is mostly **heat** (40–150 °C sedimentary aquifers) sold to municipal heat networks. Each asset is worth less than a US 20–50 MWe power plant unless lithium is a co-product. To clear the "too small" bar, the play has to be a **portfolio** (dozens of Erlaubnis fields matched to the heat-plan demand of large cities and industrial sites) with lithium upside. Germany's municipal heat-planning mandate and the reported ~10 TWh-by-2030 target (unverified) supply the buyers.

5. **Gap vs Zanskar.** Zanskar is a US Great Basin company: it targets electricity from blind hydrothermal systems on BLM land, and its capital goes into operating plants (Lightning Dock) and drilling. It has no visible European rights or data position **(unverified: no search possible this run)**. A Terranox-shape company could be **"the land bank for European sedimentary geothermal and lithium brine"**: ML over the newly released German and Dutch legacy well data, filing first-come Erlaubnis in under-claimed basins, and selling or JV-ing proven fields to Stadtwerke, utilities and lithium majors. Zanskar is not playing that game, and the European incumbents (utilities, Vulcan) are project developers, not data-driven acreage aggregators.

6. **Risks to score, not to kill.** Erlaubnis work-programme and revocation tests limit pure warehousing. Induced-seismicity politics (Basel, Landau, Vendenheim) are a factor. Heat-only assets have a single local buyer. Data release under the GeolDG is uneven and some periods run to 10–20 years (unverified). Net verdict: **a credible second leg (Germany) for a US-first company; not a standalone European company.**

---

## Sources

Verified this run:
- NLOG boreholes, 5-year confidentiality and data types: https://www.nlog.nl/en/boreholes
- NLOG geothermal licences, four-step regime and competing applications: https://www.nlog.nl/en/geothermal-licences
- NLOG geothermal energy, resource description: https://www.nlog.nl/en/geothermal-energy
- NLOG SCAN programme: https://www.nlog.nl/en/scan
- NLOG portal: https://www.nlog.nl/en
- WarmingUP / WarmingUP-GOO: https://www.warmingup.info/
- Geothermie Nederland: https://www.geothermie.nl/
- Bundesverband Geothermie, Bergrecht lexicon (*bergfrei*, 400 m threshold): https://www.geothermie.de/bibliothek/lexikon-der-geothermie/b/bergrecht
- Vulcan Energy Lionheart: https://www.v-er.eu/projects/lionheart
- UKOGL: https://www.ukogl.org.uk/
- BGS geothermal: https://www.bgs.ac.uk/geology-projects/geothermal-energy/
- Wikipedia, Geothermal power in the UK (United Downs, Eden, REA 2012): https://en.wikipedia.org/wiki/Geothermal_power_in_the_United_Kingdom
- Wikipedia, Geothermal energy in Germany (Unterhaching, Landau): https://en.wikipedia.org/wiki/Geothermal_energy_in_Germany

Attempted but unreachable this run (claims from them are marked unverified):
- BBergG: https://www.gesetze-im-internet.de/bbergg/BJNR013100980.html
- GeolDG: https://www.gesetze-im-internet.de/geoldg/BJNR138710020.html
- BMWK geothermal: https://www.bundeswirtschaftsministerium.de/Redaktion/DE/Artikel/Energie/geothermie.html
- BRGM InfoTerre: https://infoterre.brgm.fr/
- geothermies.fr regulation: https://www.geothermies.fr/espace-reglementaire
