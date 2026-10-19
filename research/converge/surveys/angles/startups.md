## Startup and venture landscape for cutting airborne-survey cost and speed

**Limitation:** the shared WebSearch budget for this run (200 calls across all agents) was already used up before my first search. I could not search at all. Everything sourced below comes from WebFetch on primary pages I already knew to visit (company sites, newsrooms, TechCrunch tag pages). A new message would be needed to restart searching. Anything marked "(estimate)" or "(unverified, from memory)" has no source.

### Main findings
1. **No venture-backed startup has clearly taken the routine "helicopter TDEM/mag/rad survey after targeting" step.** The money has gone to two other places:
   - **Vertically integrated explorers** that own the whole pipeline: KoBold (~US$1B+ raised in total, estimate) and Earth AI.
   - **Ground-based alternatives to airborne surveys**: Fleet Space ambient-noise seismic and MT, and Ideon muon tomography.
   - The airborne operators themselves are private-equity-backed or bootstrapped service firms (Xcalibur, Dias, Expert Geophysics), not venture-scale software businesses.
2. **Fleet Space is the closest venture comparable, and its investors valued it as a geophysics-services company.**
   - Funding history: US$7.35M (Sep 2019), US$26.4M Series B (Nov 2021), A$50M Series C (May 2023, about US$33M).
   - Series D: A$150M (about US$100M), closed Dec 12 2024 and led by Teachers' Venture Growth. TechCrunch put the valuation at US$525M; Fleet's own newsroom says "A$800M+".
   - The valuation "more than doubled" from the Series C.
   - Traction claims: Fleet says 54% of tier-1 miners use it and it has delivered more than 400 projects.
   - A customer quote: "survey within a week," with detailed grids taking "a few months instead of years."
   - Largest named contract: Ma'aden (Saudi Arabia), a multiyear deal covering 12,012.6 km² of the Arabian Shield (May 2025).
   - Fleet does not publish revenue or ExoSphere pricing.
   - Fleet does not replace airborne magnetics or EM for regional coverage. It is a denser, deeper, ground-deployed follow-up survey.
3. **KoBold Metals shows that investors pay for owning discoveries, not for survey tooling.**
   - Rounds: US$491M first reported Oct 2024, then US$537M Series C at a US$2.96B valuation (Jan 2025).
   - The Series C was led by Durable Capital and T. Rowe Price, with a16z, Breakthrough Energy, Equinor, Mitsubishi and others participating.
   - KoBold flies or commissions geophysics in-house as part of its own work (unverified, from memory). It sells none of it to third parties.
   - Lesson: the value captured by a better sensing or targeting stack goes to whoever holds the mineral rights.
4. **Earth AI (YC 2019) does the same for drilling and does not attack airborne surveys.**
   - It builds its own drill rigs (claimed "2-3x faster" drilling) and is building in-house labs to cut assay turnaround from about 5 months to 5 days (TechCrunch, Apr 29 2026).
   - Earth AI on drilling: "there's still no replacement for drilling."
   - Funding: a Series A of about US$20M around 2024–25 (unverified, from memory). The amount could not be sourced.
5. **Ideon Technologies (muon tomography, Vancouver) is growing as a service company, but sits underground and after drilling.**
   - Ranked #101 on Deloitte's North America Fast 500 (Nov 2025) and named to Canada's Technology Fast 50 (Oct 2025).
   - Signed a global partnership with Rio Tinto (Oct 2025). Customers include Vale Base Metals, BHP, Glencore and Evolution Mining.
   - Received ARPA-E funding with Berkeley Lab for a transportable active-source muon imager (Aug 2026).
   - Detectors go in boreholes or underground workings, so it complements drilling rather than replacing airborne surveys.
   - Total raised: about US$70–80M (unverified, from memory).
6. **The incumbent airborne operators are consolidating with private-equity money, not venture money.**
   - **Xcalibur Smart Mapping (Spain):**
     - Scale: 40+ specialised aircraft, 103 geophysical systems, 400+ staff, operations on 5 continents.
     - Capital comes from Moira Capital and the Spain Oman Private Equity Fund. It earlier acquired other airborne operators (unverified, from memory).
     - It is testing uncrewed carriers through a partnership with Dronamics' Black Swan cargo drone for magnetics and gravity.
     - Programmes include national-scale surveys (Egypt's first nationwide airborne survey in 42 years, DRC, Mauritania) and uranium work at Erongo, Namibia.
   - **Dias Geophysical (Saskatoon):**
     - Runs DIAS32 3D IP plus several airborne sensors: QMAGT full-tensor SQUID magnetic gradiometry, QAMT passive airborne EM, HELISAM (helicopter) and UAVSAM (drone).
     - Its site says QMAGT is currently surveying the Athabasca Basin, which is Terranox's home basin.
     - No disclosed funding or ownership details.
   - **Expert Geophysics (MobileMT):** a passive airborne EM system flown on helicopter or fixed-wing, marketed as deep penetration at lower cost per line-km than active TDEM (unverified, from memory). Its site returned no content.
7. **Drone geophysics is cheap but still small.**
   - Example payload: the Geometrics MagArrow II cesium magnetometer weighs 1.2 kg and flies at up to 10 m/s for about 2 hours per battery, or roughly 60–70 line-km per flight (estimate).
   - Implied economics: about US$30–80 per line-km for drone magnetics versus about US$150–300 per line-km for helicopter TDEM plus magnetics (estimate). This explains the founder's ~US$100k figure: roughly 400–600 line-km at about US$200 per line-km plus US$20–40k mobilisation (estimate).
   - Constraint 1, beyond-visual-line-of-sight (BVLOS) regulation: Transport Canada's BVLOS rules were not verified this run, so how far a drone can survey without visual line of sight in Saskatchewan is unconfirmed.
   - Constraint 2, payload: deep-penetrating TDEM transmitter loops weigh hundreds of kg. That is why drones do magnetics and radiometrics well but not deep EM. Athabasca unconformity uranium sits roughly 200–800 m deep, below drone-capable systems (estimate).
   - Constraint 3, endurance and wind in winter, when much Athabasca flying happens (estimate).
8. **Autonomous fixed-wing (Reliable Robotics) is a possible long-term carrier but not a survey business today.**
   - Reliable raised US$100M (Oct 2021). Later rounds and its FAA certification status were not verified.
   - It targets Cessna 208 cargo. No survey customers were found.
   - Autonomy removes pilot cost, but much of the cost of a helicopter EM survey is aircraft hours, mobilisation and equipment (estimate). Removing the pilot alone saves perhaps 10–20% (estimate).
9. **Mira, Terra AI, Zeus and QuSpin-based startups:**
   - The terra-ai.com domain is parked and for sale. No mineral company exists at that URL.
   - I could not verify Mira, or any startup building on QuSpin's optically pumped magnetometer (OPM) sensors, without search.
   - QuSpin OPMs (about 20 g sensors) are what make sub-kg drone magnetometers possible. The integrators are mostly small service firms (unverified, from memory).

### What did not work, or shows the limits
- **Satellite and hyperspectral remote sensing** cannot see 200–800 m deep basement conductors, which is why helicopter EM is still required in the Athabasca (estimate).
- **Selling geophysical services** limits valuations to roughly 3–6x revenue (estimate). Fleet's US$525M on what is probably tens of millions in revenue (estimate) is the top of that range.
- **Drone EM** is still shallow. Deep uranium targets keep helicopter TDEM in use.
- **Vertical integrators** (KoBold, Earth AI) build in-house and do not buy third-party survey tools, so they are not customers for a survey startup.

### Implications for a new venture
- **Most plausible openings:**
  - (a) Swarms of drones flying magnetics and radiometrics plus passive EM (MobileMT/AFMAG-style) as a first pass that cuts helicopter line-km by 50–80% (estimate).
  - (b) Software that designs minimal flight plans from ML priors, flying only where it reduces uncertainty.
  - (c) A shared survey marketplace that pools juniors in one basin to split the US$20–40k mobilisation (estimate).
- **Risk:** Xcalibur and Dias are already moving into uncrewed platforms and SQUID sensors with PE balance sheets. Dias is already flying in the Athabasca.

### Sources
- https://www.fleetspace.com/
- https://www.fleetspace.com/newsroom
- https://techcrunch.com/tag/fleet-space-technologies/
- https://techcrunch.com/2024/12/12/fleet-space-raises-100m-to-scale-satellite-enabled-mineral-prospecting-tech/
- https://techcrunch.com/tag/kobold-metals/
- https://techcrunch.com/2025/01/02/kobold-used-ai-to-find-copper-now-investors-are-piling-in-to-the-tune-of-537m/
- https://www.earth-ai.com/
- https://techcrunch.com/tag/earth-ai/
- https://techcrunch.com/2026/04/29/earth-ai-is-vertically-integrating-the-search-for-critical-minerals/
- https://ideon.ai/
- https://ideon.ai/newsroom
- https://xcaliburmp.com/
- https://xcaliburmp.com/news/
- https://www.diasgeo.com/
- https://www.geometrics.com/product/magarrow/
- https://techcrunch.com/tag/reliable-robotics/
- https://www.terra-ai.com/ (redirects to a domain-for-sale page)
