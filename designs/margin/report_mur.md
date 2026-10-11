# Impact report: +1.6% licensed power, calorimetric uncertainty 0.4%

23 of 23 calculations of record are affected.

| Calc | Title | Affected through |
|---|---|---|
| PX-HB-001 | Heat balance at rated thermal power | RTP |
| PX-NS-010 | NSSS design parameters (PCWG), analysed at RTP x (1 + CAL_UNC) | RTP |
| PX-FA-101 | Large-break LOCA peak cladding temperature (Appendix K method) | RTP |
| PX-FA-102 | Non-LOCA transients, minimum DNBR (loss of flow) | RTP |
| PX-FA-103 | Pressurizer safety valve capacity, loss of load | RTP |
| PX-CN-201 | Containment LOCA mass and energy release | RTP |
| PX-CN-202 | Containment peak pressure and temperature | RTP -> PX-CN-201 -> ME_RELEASE |
| PX-EQ-301 | Environmental qualification temperature profile, inside containment | RTP -> PX-CN-201 -> ME_RELEASE -> PX-CN-202 -> CONT_T |
| PX-EQ-302 | ECCS sump NPSH margin, recirculation | RTP -> PX-NS-010 -> DECAY_HEAT |
| PX-RD-401 | Control room operator dose, alternative source term | RTP |
| PX-RD-402 | Exclusion area boundary dose, LOCA | RTP |
| PX-AF-501 | Auxiliary feedwater capacity, loss of normal feedwater | RTP -> PX-NS-010 -> DECAY_HEAT |
| PX-SW-601 | Component cooling and service water heat removal, design-basis UHS temperature | RTP -> PX-NS-010 -> DECAY_HEAT |
| PX-SF-602 | Spent fuel pool heat-up, full core offload | RTP -> PX-NS-010 -> DECAY_HEAT |
| PX-TG-701 | HP turbine flow-passing capability (valves wide open) | RTP -> PX-HB-001 -> STEAM_FLOW |
| PX-TG-702 | Main generator capability | RTP -> PX-HB-001 -> GROSS_MWE |
| PX-TG-703 | Main step-up transformer loading | RTP -> PX-HB-001 -> GROSS_MWE |
| PX-FW-801 | Main feedwater pump capability | RTP -> PX-HB-001 -> FW_FLOW |
| PX-FW-802 | Condensate pump NPSH and heater drain capacity | RTP -> PX-HB-001 -> FW_FLOW |
| PX-FA-901 | Flow-accelerated corrosion wear rates, feedwater and extraction lines | RTP -> PX-HB-001 -> STEAM_FLOW |
| PX-SG-911 | Steam generator tube vibration and wear (FIV) | RTP -> PX-HB-001 -> STEAM_FLOW |
| PX-IC-950 | Reactor trip setpoint, overtemperature delta-T | RTP |
| PX-PR-990 | PRA, internal events | RTP -> PX-NS-010 -> DECAY_HEAT |

## Margin map (headroom in % of licensed power before each limit binds)

| Calc | Limit | Headroom % | With modern method % | Status at this uprate | Fix |
|---|---|---|---|---|---|
| PX-TG-702 | <= 1240 (MWe (rating at 0.9 pf)) | 3.8 | 3.8 | OK |  |
| PX-TG-701 | <= 104.5 (% of current (VWO capability)) | 4.5 | 4.5 | OK |  |
| PX-TG-703 | <= 1330 (MVA (nameplate, forced cooling)) | 5.6 | 5.6 | OK |  |
| PX-FW-802 | <= 106 (% of current) | 6.0 | 6.0 | OK |  |
| PX-FW-801 | <= 109 (% of current (runout margin)) | 9.0 | 9.0 | OK |  |
| PX-FA-103 | <= 2748 (psia (110% design)) | 9.7 | 9.7 | OK |  |
| PX-AF-501 | >= 0 (%) | 10.6 | 10.6 | OK |  |
| PX-FA-102 | >= 1.3 ((safety analysis limit)) | 11.6 | 14.9 | OK |  |
| PX-SF-602 | <= 150 (F (pool design)) | 11.6 | 11.6 | OK |  |
| PX-FA-101 | <= 2200 (F (10 CFR 50.46)) | 12.3 | 23.0 | OK |  |
| PX-SW-601 | <= 120 (F (component cooling design)) | 13.0 | 13.0 | OK |  |
| PX-SG-911 | <= 1 (stability ratio) | 18.3 | 18.3 | OK |  |
| PX-EQ-302 | >= 0 (ft) | 18.8 | 18.8 | OK |  |
| PX-EQ-301 | <= 340 (F (qualified envelope)) | 23.5 | 23.5 | OK |  |
| PX-RD-401 | <= 5 (rem TEDE (10 CFR 50.67)) | 23.6 | 23.6 | OK |  |
| PX-FA-901 | >= 6 (years (inspection programme)) | 26.7 | 26.7 | OK |  |
| PX-CN-202 | <= 60 (psig (containment design pressure)) | 27.1 | 27.1 | OK |  |
| PX-RD-402 | <= 25 (rem TEDE (10 CFR 50.67)) | 80.2 | 80.2 | OK |  |
| PX-PR-990 | <= 0.0001 (per year (RG 1.174 region)) | >100 | >100 | OK |  |

Uprate available with no new analysis methods or hardware: 3.8% (binding: PX-TG-702).
Safety-analysis ceiling with modern methods: 9.7%. Hardware needed beyond: PX-TG-702 at 3.8%, PX-TG-701 at 4.5%, PX-TG-703 at 5.6%, PX-FW-802 at 6.0%, PX-FW-801 at 9.0%.
