# L19 — International geothermal exploration science and AI (Indonesia, Kenya, Philippines, Turkey, Mexico, Chile, New Zealand, Iceland, Japan)

**Method note (important):** The shared WebSearch budget for this run was used up before this agent's first query, so no searches ran. Everything below comes from direct fetches of primary-source pages and bibliographic APIs (DOI to Crossref / OpenAlex / Semantic Scholar / OSTI) for papers I could name in advance, plus a few country-statistics pages. Bibliographic details (authors, venue, volume, pages) were checked against Crossref/OpenAlex for every paper. Abstract content is labelled "abstract verified" only where an API or OSTI returned the abstract. Otherwise it is labelled "metadata/keywords only", and anything I add from memory is marked (unverified). The IGA/WGC PDF server (geothermal-energy.org) returned HTTP 503 on two tries, so I could not read the WGC 2020 country updates. A follow-up run with search budget should pull the WGC 2023 country updates for Indonesia, Kenya and the Philippines.

---

## 1. Market context: where the world's hydrothermal capacity is (year-end 2024)

ThinkGeoEnergy's Top-10 for 2024 (https://www.thinkgeoenergy.com/thinkgeoenergys-top-10-geothermal-countries-2024-power/) gives a global total of **16,873 MW**:

| Country | MW (YE2024) |
|---|---|
| USA | 3,937 |
| Indonesia | 2,653 |
| Philippines | 1,984 |
| Türkiye | 1,734 |
| New Zealand | 1,207 |
| Kenya | 985 |
| Mexico | 976 |
| Italy | 916 |
| Iceland | 786 |
| Japan | 601 |

Seven of the nine countries in this review are in the global top 10. Together they hold about **10.9 GW**, versus 3.9 GW in the US. Stated potentials are far above installed capacity:
- **Indonesia:** about 28 GW often cited (secondary source). The Ministry (ESDM) reports 2,744 MW installed in 2025 (https://en.wikipedia.org/wiki/Geothermal_power_in_Indonesia, citing ANTARA/Tempo 2025).
- **Japan:** 19.14 GW (Ministry of the Environment, 2011) to 23 GW, "third largest after US and Indonesia", against about 540 MW in 98 plants (JOGMEC 2022, via https://en.wikipedia.org/wiki/Geothermal_power_in_Japan).
- **Türkiye:** about 4 GW hydrothermal potential (PMC8986971, via https://en.wikipedia.org/wiki/Geothermal_power_in_Turkey).
- **Chile:** a ministerial claim of 6–112 GW (unreliable). The rigorous estimate is about 659 MWe (Aravena et al., below).
- **Kenya:** a 5–5.5 GW 2030 target, with GDC as the state steam developer (https://en.wikipedia.org/wiki/Geothermal_power_in_Kenya).

## 2. Deep literature review (primary sources)

### P1. Okoroafor, Smith, Ochie, Nwosu, Gudmundsdottir & Aljubran (2022). "Machine learning in subsurface geothermal energy: Two decades in review." *Geothermics* 102, 102401. DOI 10.1016/j.geothermics.2022.102401
- Status: metadata only (closed access, abstract not returned).
- It is the standard review of ML in geothermal, with about 160 citations by 2026 and an FWCI of 5.6 (OpenAlex).
- **Key fact for us:** OpenAlex lists co-author **Connor M. Smith with Zanskar Geothermal**. The leading Western ML-geothermal review was co-written by Zanskar people. Zanskar is ML-literate and also shapes the scientific agenda.
- Keyword coverage: exploration, petrophysics, reservoir characterisation, drilling, seismicity.
- (Unverified, from memory) The review finds that most exploration-ML work is US-centric, much of it Great Basin, with few transferable models.

### P2. Tüfekçi, Süzen & Güleç (2010). "GIS based geothermal potential assessment: A case study from Western Anatolia, Turkey." *Energy* 35(1):246–261. DOI 10.1016/j.energy.2009.09.016
- Abstract verified (Semantic Scholar summary).
- Inputs were **public data only**: magnetic anomaly, gravity anomaly, earthquake epicentres (Gutenberg–Richter b-value) and lineaments. The authors applied Index Overlay and Weights-of-Evidence, and weighting by spatial association with known sites improved accuracy.
- The highest-potential provinces were **Aydın, Denizli, Manisa, Balıkesir and Kütahya**. Aydın and Denizli were already developed, which validates the method. Manisa, Balıkesir and Kütahya were "largely unexplored" in 2010.
- Relevance: an early proof that public regional data can rank under-explored acreage. Since then Türkiye has gone from about 100 MW (2010) to 1,734 MW (2024), much of it in the Büyük Menderes/Gediz grabens these maps highlighted.

### P3. Yalçın et al. (2017). "A GIS-based multi criteria decision analysis approach for exploring geothermal resources: Akarcay basin (Afyonkarahisar)." *Geothermics* 67:18–28. DOI 10.1016/j.geothermics.2017.01.002
- Metadata only. Co-author attribution differs between databases: OpenAlex has F. Batuk, Semantic Scholar has F.K. Gul.
- It is a basin-scale multi-criteria decision analysis (MCDA) prospectivity map in Türkiye. It shows a steady Turkish academic pipeline of prospectivity mapping, mostly knowledge-driven rather than learned.

### P4. Carranza, Wibowo, Barritt & Sumintadireja (2008). "Spatial data analysis and integration for regional-scale geothermal potential mapping, West Java, Indonesia." *Geothermics* 37(3):267–299. DOI 10.1016/j.geothermics.2008.03.003
- Metadata and keywords only. Authors are from ITC Enschede and ITB Bandung; about 97 citations.
- Keywords: evidential belief functions, hot springs, gravity lows, fault orientation.
- (Unverified detail) It quantifies the spatial association of known prospects with fault orientations and hot-spring distance, then integrates data-driven evidence layers into a regional favourability map.
- Relevance: the canonical Indonesian data-driven prospectivity paper. It is nearly 20 years old, which suggests the Indonesian ML frontier is thin.

### P5. Noorollahi, Itoi, Fujii & Tanaka (2007). "GIS model for geothermal resource exploration in Akita and Iwate prefectures, northern Japan." *Computers & Geosciences* 33(8):1008–1021. DOI 10.1016/j.cageo.2006.11.006. Companion: Noorollahi et al. (2008), "GIS integration model for geothermal exploration and well siting," *Geothermics* 37(2):107–131. DOI 10.1016/j.geothermics.2007.12.001
- Metadata only. Authors are from Kyushu University. The 2008 paper has about 119 citations and concepts that include geothermal gradient, overlay and well siting.
- Relevance: Japan's regional favourability work dates to the 2000s. Japan's binding constraint is access, not discovery: national parks and onsen opposition (Kubota et al. 2013, *Energy Policy* 61, DOI 10.1016/j.enpol.2013.05.031). The same authors built Iran's national map (Yousefi et al. 2010, *Geothermics* 39:140–151, DOI 10.1016/j.geothermics.2009.11.001).

### P6. Ishitsuka, Mogi, Sugano, Yamaya, Uchida & Kajiwara (2018). "Resistivity-based temperature estimation of the Kakkonda geothermal field, Japan, using a neural network and neural kriging." *IEEE GRSL* 15(8):1154–1158. DOI 10.1109/LGRS.2018.2832647
- Abstract verified (OpenAlex).
- Neural kriging, a neural network constrained by a temperature variogram, maps temperature from MT resistivity. Against plain neural-network methods it cut estimation error by **6–87%** and variogram error by **191–285%** in cross-validation, with large gains far from well logs.
- Relevance: this is the "temperature-at-depth from geophysics plus sparse wells" method a Terranox-shape company needs. It is validated in a Japanese supercritical-target field (Kakkonda, AIST/JOGMEC programme).

### P7. Aravena, Muñoz, Morata, Lahsen, Parada & Dobson (2016). "Assessment of high enthalpy geothermal resources and promising areas of Chile." *Geothermics* 59:1–13. DOI 10.1016/j.geothermics.2015.09.001
- Abstract verified (OSTI 1532179). Authors are from CEGA / University of Chile and LBNL.
- Method: USGS heat-in-place with Monte Carlo.
- **Indicated** resources in three systems (Apacheta, El Tatio, Tolhuaca) total **228 ± 154 MWe**. **Inferred** resources in six systems total **431 ± 321 MWe**.
- The authors propose **65 favourable areas**, and **8** look highly favourable on initial exploration.
- Relevance: Chile is under-explored. Only Cerro Pabellón (48 MW gross, 2017, Enel/ENAP) operates, and the rigorous potential is far below the 6–112 GW political claims. Chile has a clean **concession system** (Law 19.657, 2000) that separates subsurface geothermal rights from surface ownership and is open to any Chilean entity (https://en.wikipedia.org/wiki/Geothermal_power_in_Chile). Structurally this is the closest analogue to the Saskatchewan mineral-claim model, but the resource is mostly remote high-Andes, and offtake and transmission constrain it.

### P8. Prol-Ledesma (2000). "Evaluation of the reconnaissance results in geothermal exploration using GIS." *Geothermics* 29(1):83–103. DOI 10.1016/S0375-6505(99)00051-6
- Metadata and keywords only (UNAM).
- Keywords: Los Azufres, rhyolite domes, apparent resistivity, **fuzzy logic, Boolean model**, well placement, fault-zone permeability.
- Relevance: Mexico's GIS/fuzzy prospectivity work is old and centred on CFE fields. CFE dominates the sector (Cerro Prieto, Los Azufres, Los Humeros; https://en.wikipedia.org/wiki/Geothermal_power_in_Mexico). Private rights exist under the 2014 Geothermal Energy Law (details unverified this run), but data and offtake are state-controlled.

### P9. Bertrand, Caldwell, Hill et al. (2012). "Magnetotelluric imaging of upper-crustal convection plumes beneath the Taupo Volcanic Zone, New Zealand." *Geophys. Res. Lett.* 39(2). DOI 10.1029/2011GL050177
- Abstract verified (OpenAlex).
- Broadband MT on the SE margin of the TVZ shows vertical low-resistivity plumes linking surface geothermal fields to a magmatic heat source below the brittle–ductile transition. This supports hydrothermal convection in the upper about 6–7 km.
- Companion: Kissling & Weir (2005), "The spatial distribution of the geothermal fields in the Taupo Volcanic Zone," *JVGR* 145:136–150, DOI 10.1016/j.jvolgeores.2005.01.006 (metadata only). It treats field spacing as a convective-plume pattern, which by implication bounds how many undiscovered fields could exist.
- Relevance: TVZ fields are mostly expressed at the surface and well known. The blind upside is deeper ("supercritical") rather than new shallow fields. Access runs through RMA resource consents and Māori land trusts, and NZGA calls the RMA "the single largest obstacle" (https://en.wikipedia.org/wiki/Geothermal_power_in_New_Zealand).

### P10. Coro & Trumpy (2020). "Predicting geographical suitability of geothermal power plants." *J. Cleaner Production* 267:121874. DOI 10.1016/j.jclepro.2020.121874
- Abstract verified (OpenAlex). Authors are from CNR Pisa.
- A **global** Maximum-Entropy suitability map, validated against active and planned plants and released as open science (data and services reusable).
- Relevance: open global baseline maps already exist and are free, so a coarse global favourability layer is not a moat by itself.

### P11 (US comparator for the "blind" claim). Moraga, Duzgun, Cavur & Soydan (2022). "The Geothermal Artificial Intelligence for geothermal exploration." *Renewable Energy* 192:134–149. DOI 10.1016/j.renene.2022.04.113
- Abstract verified (OSTI 1867408).
- Remote-sensing ML using mineral markers, land-surface temperature, faults and deformation (InSAR) at Brady's (surface manifestations) and **Desert Peak (blind)**.
- Accuracy was **92–95%** on independent data but only **72–76%** when trained on one site and applied to the other.
- Takeaway: transfer to new, blind terrains is the hard part. This is exactly what international deployment needs, and remote sensing works almost anywhere (arid Anatolia, the Andes, the Kenyan Rift, NE Africa) regardless of how open a country's well data is.

## 3. Data openness by country

- **New Zealand: open.** The NZP&M Geodata Catalogue offers petroleum, minerals and coal reports, surveys and boreholes released under the Crown Minerals Act 1991, **free to download** with a RealMe login (https://www.nzpam.govt.nz/maps-geoscience/exploration-database). The page does not mention geothermal-specific data. Taranaki petroleum wells give bottom-hole temperatures (BHTs) outside the TVZ: a genuine "Saskatchewan-style" corpus, but the basin is lower-temperature.
- **Iceland: open-ish, state-led.** The National Energy Authority (Orkustofnun) publishes statistics. 799 MWe in 2020 was 25.9% of power capacity, and geothermal generated 5,961 GWh (https://orkustofnun.is/gogn/os-onnur-rit/Orkutolur-2020-enska.pdf). The Master Plan (Rammaáætlun) gates every new project through Parliament (https://www.ramma.is/english/the-master-plan-today/). Three incumbents run the plants (HS Orka, ON Power, Landsvirkjun). There is little whitespace.
- **Türkiye.** MTA (the state geological survey) did the founding exploration (Kızıldere found in 1968) and historically tendered MTA-discovered fields. The 2007 Geothermal Law cut licensing to two licences. The feed-in tariff was 10.5 USc/kWh (2010–2021) and is now lira-denominated with an 8.6 USc cap (https://en.wikipedia.org/wiki/Geothermal_power_in_Turkey). There are private licence holders and a secondary licence market (unverified), which makes Türkiye the most "flippable-licence" market outside the US.
- **Indonesia.** Rights come as government-tendered working areas (WKP). The 2014 Geothermal Law removed the "mining" classification so projects could proceed in conservation forests, where about 80% of reserves lie (Jakarta Post via Wikipedia). Pertamina Geothermal and PLN dominate. Data stays with ESDM/Geological Agency. The right is not cheap-staked; it is won by tender with capital commitments.
- **Philippines.** Rights come through DOE service contracts. Since 2020, 100% foreign ownership is allowed for large-scale projects above US$50M (Rappler 2020, via Wikipedia). The sector is incumbent-heavy (EDC, Aboitiz; unverified this run).
- **Kenya.** The state-owned GDC drills and sells steam. KenGen and independent power producers generate. Rift data is held by the state. 985 MW at YE2024.
- **Mexico.** CFE holds the main fields. Private permits exist under the 2014 law (unverified detail).
- **Japan.** Data is via JOGMEC and AIST/GSJ. The barrier is national parks and onsen communities, not discovery.
- **Chile.** A concession system open to any Chilean entity (Law 19.657). CEGA publishes geoscience. This is the closest structural match to "stake the right cheaply".

## Implications for a Terranox-shape geothermal company and the gap vs Zanskar

1. **Most international markets do not support the "buy the right cheap before proof" mechanic.** Indonesia (WKP tenders), Kenya (GDC monopoly on steam), Mexico (CFE), Iceland (parliamentary Master Plan), NZ (RMA consents and Māori trust land) and Japan (parks and onsen) all give rights through state tender or consent processes. Rights are not cheaply staked, and data is not compulsorily disclosed under a Saskatchewan-style rule. This kills "international-first" as the opening wedge. The US BLM competitive lease sale plus private fee land remains the best right-acquisition regime. **Chile** (open concession law, 65 favourable areas, only 48 MW built) and **Türkiye** (two-licence regime, private licence holders, under-explored western provinces) are the two most plausible second markets.
2. **The scientific frontier abroad is old.** Most country literature is 2000s-era GIS/weights-of-evidence/fuzzy work: Carranza 2008, Noorollahi 2007/08, Prol-Ledesma 2000, Tüfekçi 2010. Only a few modern neural methods exist (Ishitsuka 2018). The best ML review (Okoroafor 2022) was co-written by Zanskar staff, so Zanskar owns the US science narrative. There is no international equivalent of Zanskar's data-plus-rights machine.
3. **What transfers is remote sensing and temperature-from-geophysics, not well data.** Moraga 2022 shows cross-site transfer drops to 72–76%. Ishitsuka 2018 shows sparse-well temperature interpolation improves sharply with geostatistical constraints. A company whose edge is digitising **illegible legacy records** (BHTs, mining and assessment files, temperature-gradient holes) has its corpus advantage mainly in the US. Abroad, only NZ (free Crown Minerals data) and possibly Türkiye (MTA archives) offer a comparable corpus.
4. **Gap vs Zanskar.** Zanskar is US/Great Basin-focused, buys and drills to develop (Lightning Dock), and publishes. Gaps a Terranox-shape company could take:
   - **(a)** A pure rights-and-flip strategy at scale: many cheap leases and fee rights across many basins (sedimentary BHT-rich basins, not just Great Basin hydrothermal), sold de-risked to Fervo, Ormat or utilities rather than developed in-house.
   - **(b)** An international optionality layer: a Chile/Türkiye concession portfolio later, where no ML-driven rights aggregator exists.
   - **(c)** Mining-assessment-file data (hard-rock exploration drillholes carry temperature logs). Zanskar's public work leans on oil/gas and USGS data (unverified).
5. **Size check.** The international hydrothermal market is real: about 10.9 GW installed across the reviewed countries versus 3.9 GW in the US, and stated potentials of tens of GW (Indonesia about 28 GW, Japan about 19–23 GW). It is not "too small". It is just not the first market. Score international as upside optionality, not the wedge.

## Sources
- https://doi.org/10.1016/j.geothermics.2022.102401 (Okoroafor et al. 2022; metadata via https://api.openalex.org/works/doi:10.1016/j.geothermics.2022.102401)
- https://doi.org/10.1016/j.energy.2009.09.016 (Tüfekçi et al. 2010)
- https://doi.org/10.1016/j.geothermics.2017.01.002 (Yalçın et al. 2017)
- https://doi.org/10.1016/j.geothermics.2008.03.003 (Carranza et al. 2008)
- https://doi.org/10.1016/j.cageo.2006.11.006 (Noorollahi et al. 2007)
- https://doi.org/10.1016/j.geothermics.2007.12.001 (Noorollahi et al. 2008)
- https://doi.org/10.1016/j.geothermics.2009.11.001 (Yousefi et al. 2010)
- https://doi.org/10.1109/LGRS.2018.2832647 (Ishitsuka et al. 2018)
- https://www.osti.gov/biblio/1532179 (Aravena et al. 2016 abstract); https://doi.org/10.1016/j.geothermics.2015.09.001
- https://doi.org/10.1016/S0375-6505(99)00051-6 (Prol-Ledesma 2000)
- https://doi.org/10.1029/2011GL050177 (Bertrand et al. 2012)
- https://doi.org/10.1016/j.jvolgeores.2005.01.006 (Kissling & Weir 2005)
- https://doi.org/10.1016/j.jclepro.2020.121874 (Coro & Trumpy 2020)
- https://www.osti.gov/biblio/1867408 (Moraga et al. 2022 abstract); https://doi.org/10.1016/j.renene.2022.04.113
- https://doi.org/10.1016/j.enpol.2013.05.031 (Kubota et al. 2013, Japan onsen)
- https://www.thinkgeoenergy.com/thinkgeoenergys-top-10-geothermal-countries-2024-power/
- https://www.nzpam.govt.nz/maps-geoscience/exploration-database
- https://orkustofnun.is/gogn/os-onnur-rit/Orkutolur-2020-enska.pdf
- https://www.ramma.is/english/the-master-plan-today/
- https://en.wikipedia.org/wiki/Geothermal_power_in_Indonesia (secondary; cites ESDM, Jakarta Post)
- https://en.wikipedia.org/wiki/Geothermal_power_in_Kenya (secondary)
- https://en.wikipedia.org/wiki/Geothermal_power_in_the_Philippines (secondary; cites Rappler 2020)
- https://en.wikipedia.org/wiki/Geothermal_power_in_Turkey (secondary; cites UNESCO, Norton Rose Fulbright)
- https://en.wikipedia.org/wiki/Geothermal_power_in_Japan (secondary; cites JOGMEC, MoE 2011)
- https://en.wikipedia.org/wiki/Geothermal_power_in_Chile (secondary; cites Law 19.657 text)
- https://en.wikipedia.org/wiki/Geothermal_power_in_Mexico (secondary)
- https://en.wikipedia.org/wiki/Geothermal_power_in_New_Zealand (secondary)
- https://en.wikipedia.org/wiki/Geothermal_power_in_Iceland (secondary)
