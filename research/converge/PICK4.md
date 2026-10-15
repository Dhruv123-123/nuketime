# The fourth hunt: everything in nuclear, and an honest result

Written 7 October 2026. The brief was the widest yet: anything in nuclear, hardware or software,
excluding prospecting and drilling, judged on novelty ("a gap nobody has found"), tangible merit,
and size first (a credible path past about $300M a year). Raw agent output, with every URL the agents
cited, is in `gap_hunt_r1.md` and `gap_hunt_r2.md` in this folder (round 3 is summarised below).
Models are in `designs/zirc/`.

## The answer

**No new idea cleared both bars.** Across three rounds, about 70 research agents generated and tried
to kill roughly 330 hypotheses. Every survivor was either new but small, or large but already named
by someone with money behind it. The best idea of the hunt, recovering the hafnium the zirconium
industry throws away, was real, quantified and extremely timely. It was also announced as a
commercial project on 25 August 2026, six weeks before this hunt found it.

That result is itself the finding worth acting on, and it changes how to pick:

> **In nuclear in 2026, novel gaps are small and big gaps are named.** A venture-scale company here
> will not come from spotting something nobody has seen. It will come from executing on a named,
> large bottleneck faster or differently than the people who named it.

On that basis the recommendation is to **commit to the third pick, the nuclear-qualified
manufacturer (`PICK3.md`)**, which is still the largest open bottleneck we have found, and this hunt
added fresh evidence for it (below). If Dhruv would rather trade size for novelty, the hafnium race is
the sharpest alternative, with an eight-week plan and kill criteria at the end of this memo.

## What was run

| Round | Agents | What it did | Result |
|---|---|---|---|
| 1 | 12 hunters, 1 judge, 24 skeptics | One hunter per domain: chokepoint materials, stable isotopes, back-end byproducts, finance and insurance, fleet economics, radiation applications, fusion and space, AI and software, heat, detection and safeguards, lateral analogues, 2026 policy changes. A judge merged 49 survivors into 8 finalists; three skeptics (novelty, market, feasibility) attacked each. | 238 killed in the hunt. All 8 finalists weakened or killed, mostly on size. |
| 2 | 3 investigators, 6 hunters, 12 skeptics | Deep dive on hafnium (supply and price, technology and competitors, biggest possible company), plus size-first hunters on byproduct inversions, orbital radiation, waste capacity, big software, enabling hardware and practitioner complaints. | Hafnium found to be taken. Every new survivor capped under $300M a year. |
| 3 | 7 investigators, 7 skeptics | Seven cross-silo bets where a nuclear-physics fact might control value in a huge non-nuclear market (below). | All seven killed by both investigator and skeptic. |

## Why the law holds

The table shows the pattern. The left column is where the hunt found things nobody is doing; the
right column is where the money is.

| New, but small (best ceiling found) | Large, but already named |
|---|---|
| Neutron soft-error mitigation for liquid-cooled AI racks ($20-100M/yr) | Nuclear-qualified manufacturing (Hadrian adjacent; the incumbents are full) |
| Zr-91-stripped cladding (whole world value pool $160-310M/yr, our model) | Hafnium recovery (Daiichi Kigenso, Sanxiang, Critical Metals, Energy Fuels) |
| Fusion breeder-inventory lessor (no $300M year before about 2045) | HALEU, enrichment, conversion (Centrus, Orano, Urenco, General Matter, GLE) |
| Merchant QUICC ion-beam qualification lab ($30-60M/yr) | Fuel and module leasing (utility fuel trusts, traders, vendor build-own-operate) |
| C-14 from CANDU resins ($5-30M/yr entrant) | He-3 (Interlune), Li-6/7 (Molten Salt Solutions), C-14 (OPG, ASP Isotopes) |
| Radium residuals from Permian produced water ($5-40M/yr) | Licensing and plant-ops AI (Atomic Canyon, Nuclearn, Everstar) |

The reason is structural. Nuclear is a small number of very large buyers, a few dozen fuel lines,
about 400 reactors, and a handful of governments. A gap nobody has noticed is almost always one
nobody noticed because it sits on too few buyers to matter. Where the money is large (fuel,
construction, the fleet's operating budget, critical materials), consultants, national labs, DOE
programmes and now generalist investors have been mapping it hard since 2024.

## The closest calls, and how each one died

### 1. Hafnium: the nuclear byproduct the AI buildout runs on (killed: taken, and the market is thin)

The insight is genuinely striking. About 1.2 Mt of zircon is mined a year (USGS MCS 2026), carrying
on the order of 10 kt of hafnium at Hf:Zr of about 1:50. Only about 70-150 t a year is recovered,
because hafnium is separated only where nuclear-grade zirconium is made (Framatome Jarrie,
Westinghouse Ogden, ATI Albany, Chepetsky, Chinese plants). Hafnium is in every HBM and logic gate
stack and in the superalloys of the gas turbines being bought to power AI data centres. After China's
H2-2025 export controls the Western price went from about $5,000/kg to $13,115/kg in April 2026 (SMM)
and above $14,000/kg in June (MMTA). At that price the hafnium in a tonne of zircon is worth 20 to
100 times the zircon. Oregon State published a water-based precipitation with a separation factor of
33 against 6-7 for the industrial solvent process (JACS, September 2026), and its lead author said
scaling it "would likely require a start-up" (ANS, 1 October 2026).

Why it dies:
- **Taken.** Daiichi Kigenso, the largest non-Chinese zirconium-chemicals maker, filed on
  25 August 2026 that it will recover hafnium from its Vietnamese zirconium intermediate with the
  startup Emulsion Flow Technologies: samples in 2026, mass production in 2028 (JPX filing). In China,
  Sanxiang and Liaoning Huaxiang are commissioning zirconium-hafnium separation on their oxychloride
  lines. Huaxiang's 20,000 t/yr plant cost about $42M and alone carries roughly 110 t of hafnium a
  year, about the size of the whole world market.
- **Thin.** The market is 100-150 t a year, roughly $0.4-1.9B depending on which side of the export
  controls you sell. Our model (`designs/zirc/hafnium_market.py`) gives a new Western producer a
  revenue-maximising $70-190M a year in most cases and clears $300M in one of eight scenarios (export
  controls hold, no rival supply, elastic demand). Rival supply already exists.

### 2. Zr-91-stripped zirconium cladding (killed by our own model)

Zr-91 is 11.2% of natural zirconium but causes about 71% of its thermal neutron absorption (0.131 of
0.185 b). Westinghouse, LLNL, USEC and AECL patented ways to strip it in the 1980s and 90s and dropped
them when uranium was $10-40/lb. With uranium at $86/lb and contract SWU at $109 (EIA via ANS,
August 2026), the revival case looked plausible and no active competitor turned up. Our textbook
pin-cell estimate (`designs/zirc/zr91_value.py`) shows why nobody revived it: cladding takes only about
0.3% of thermal absorptions in a PWR, so removing Zr-91 frees about 200-340 pcm, worth a 0.6-1.0% fuel
saving, about $80-160 per kg of zirconium. Across about 2,000 t a year of LWR reload zirconium, the
entire world value pool is $160-310M a year before anyone pays for separation, which costs more than
that.

### 3. Neutron soft errors in liquid-cooled AI data centres (killed: real physics, small money)

Water moderates cosmic neutrons to thermal energies, and boron-10 in chips captures them, so liquid
cooling raises soft-error rates; NTT and Hokkaido found low-energy neutrons cause a fifth to a quarter
of FPGA errors and expect water cooling to raise that. The Llama 3 405B run lost 17% of its 419
interruptions to HBM3 and 4.5% to SRAM (Meta, arXiv 2407.21783). Our investigator's bottom-up puts the
radiation tax at about 0.3-0.6% of cluster goodput at sea level, $30-60M per GW per year, but most of
it is uncontrollable, so a vendor could capture tens of millions a year at most.

### 4. The rest of the finalists

| Candidate | Why it died | Best ceiling found |
|---|---|---|
| Fusion breeder-inventory lessor (Li-6, tritium, Be) | No plants before the 2030s; $300M/yr around 2045 on the paper's own deployment path; collateral not repossessable | Under $50M/yr to 2035 |
| HALEU and fuel-inventory lessor | Utility fuel-lease structures still exist (AEP, Entergy); spreads thin against investment-grade buyers | $50-120M/yr net spread |
| E-beam grain disinfestation utility | Elevator-scale plants were tried before; export buyers block irradiated grain | $50-200M/yr |
| C-12 diamond heat spreaders | Gain is about 14% over today's poly diamond, worth about 1 K at the chip | $10-50M/yr |
| AI evidence for reclassifying DOE tank waste | Blocked by law and a 2024 settlement, not by analysis | $10-50M/yr |
| QUICC ion-beam qualification lab | Free DOE beam access and the inventor consortium fill most of it | $30-60M/yr |
| Phosphogypsum radium stripping | Displaces $13/t gypsum; EPA has never approved indoor use | $75-240M/yr industry-wide |
| Sterile-insect production (screwworm) | USDA's own Texas plant and Mexico's Metapa close the gap by 2028 | $20-80M/yr |
| Low-alpha packaging materials for HBM | Milligrams per stack; incumbents qualified per fab | $10-50M/yr |
| Neutron sorting of copper in steel scrap | Thermo Gamma-Metrics has sold it since 2001 | $20-60M/yr |
| Muon tomography outside mining | Six funded companies over 20 years; flux too low for fast imaging | $50-150M/yr |
| ISR co-products (Sc, Re, REE) | Kazatomprom, Uzbekistan and Russia already pilot it; world Sc+Re markets are small | $20-120M/yr |
| Orbital-compute radiation layer | NVIDIA and captive hyperscalers will own it | $5-30M/yr near term |
| RF tube second source (klystrons, gyrotrons) | Defence sockets locked by incumbents | $40-120M/yr |
| Licensed-operator foundry | Vendors and utilities are already the operators | $15-100M/yr |

Also checked and killed in round 1 (reasons and sources in `gap_hunt_r1.md`): Li-7 and Li-6
(Molten Salt Solutions), He-3 (Interlune), boron-10 (5E), beryllium (Materion), nuclear graphite,
heavy water from electrolysers (Aternium), DU tails to fluorochemicals (INIS tried), fission-product
Ru/Rh/Xe (no US reprocessing), cost-overrun and liability MGAs, unattended ISFSI security, formally
verified I&C, heat import and heat-sink services, CdZnTeSe crystals, tritium accountancy, MC&A
instruments, IFE target foundry, Cl-37 and N-15 for advanced fuels, and uranium from phosphoric acid
(PhosEnergy, backed by Cameco).

## What the hunt adds to the third pick

The third pick is to become the nuclear-qualified manufacturer the buildout is short of, with software
quality records as the moat, starting with commercial-grade dedication and obsolete spares. Three
things from this hunt strengthen it:
- **Qualified suppliers have pricing power now.** ATI renewed its naval nuclear contract at $1B over
  five years, more than double the prior annual revenue, with about two-thirds of the uplift from price
  (ATI Q2 2026 call).
- **The materials layer is being solved by others.** Hafnium, zirconium, lithium isotopes, HALEU and
  conversion all have funded entrants, so a manufacturer will not be starved of inputs; the parts and
  their paperwork remain the bottleneck the Nuclear Scaling Initiative named.
- **Nothing in 330 hypotheses was larger and open.** The only bigger pools (fuel, construction capex)
  are either commodity businesses or the same manufacturing bottleneck seen from another side.

Its weak point is unchanged: the result hinges on how much idle qualified capacity exists, which the
census in `PICK3.md`'s eight-week plan measures first.

## If Dhruv prefers the hafnium race instead

A smaller, sharper company: license the Oregon State water-based process and run toll dehafniation at
Western zirconium-chemical sites outside the three nuclear incumbents, selling semiconductor-grade
hafnium compounds to US fabs and turbine makers that are cut off from Chinese supply.

| Week | Do | Evidence it produces |
|---|---|---|
| 1 to 2 | Call OSU's tech-transfer office about the patent and a licence; call Luxfer MEL, Saint-Gobain ZirPro and Tosoh about host liquor | Whether the IP and a feed are available |
| 2 to 6 | Contract a lab to repeat the precipitation on real zirconium oxychloride mother liquor, three stages, with reagent recycle | Separation factor on dirty feed and reagent cost per kg Hf |
| 3 to 6 | Calls with a US fab materials team, GE Vernova and PCC Structurals purchasing, and the Navy SBIR office (TDMAZ topic) | Volume, spec and price each would sign for |
| 6 to 8 | Re-run `hafnium_market.py` with quotes and the Daiichi and Sanxiang ramp | A defensible revenue ceiling |

Kill criteria: the separation factor on real liquor falls below about 10; reagent cost above about
$500 per kg Hf; no buyer will sign above $5,000/kg for non-Chinese hafnium; or the licence is not
available.

## Kill criteria for the recommendation itself

Drop the third pick too if the `PICK3.md` census shows lead times under about six months for common
part families, or no reactor vendor or utility will audit a new supplier within a year. In that case
the honest next step is a hunt with a different filter: named, large bottlenecks ranked by how well
an ML team can execute on them, rather than by novelty.

## Key sources

- Daiichi Kigenso hafnium filing, 25 Aug 2026: https://www2.jpx.co.jp/disc/40820/140120260825525456.pdf
- Emulsion Flow Technologies MOU: https://prtimes.jp/main/html/rd/p/000000004.000171462.html
- SMM, Western hafnium price to $13,115/kg: https://news.metal.com/en/newscontent/103938701-from-stability-to-surge-the-overseas-hafnium-market-caught-between-ai-demand-and-supply-controls
- MMTA/CPM on capacity, demand and thresholds: https://mmta.co.uk/hafnium-demand-dynamics-and-capacity-constraints/ and https://mmta.co.uk/hafnium-where-will-it-end/
- USGS MCS 2026, zirconium and hafnium: https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-zirconium-hafnium.pdf
- Oregon State process (ANS): https://www.ans.org/news/2026-10-01/article-8451/study-finds-a-better-way-to-separate-zirconium-and-hafnium/
- Liaoning Huaxiang Zr/Hf plant: https://cdn.asianmetal.com/news/2217938/Liaoning-Huaxiang-to-launch-zirconium-hafnium-separation-project/1
- Sanxiang (Huaxin Securities note): https://pdf.dfcfw.com/pdf/H3_AP202607051826725916_1.pdf
- ATI Q2 2026 call: https://www.fool.com/earnings/call-transcripts/2026/08/13/ati-ati-q2-2026-earnings-call-transcript/
- Uranium and SWU prices (EIA via ANS): https://www.ans.org/news/2026-08-05/article-8270/uranium-prices-steady-as-eia-releases-annual-market-report/
- Llama 3 interruption breakdown: https://arxiv.org/pdf/2407.21783
- NTT and Hokkaido on thermal neutrons and water cooling: https://theregister.com/2023/03/17/neutrons_cause_soft_errors_electronics
- PhosEnergy (uranium from phosphates): https://world-nuclear-news.org/articles/cameco-buys-into-phosenergy-technology
