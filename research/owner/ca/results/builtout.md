# Built-out industrial sites near substations (California)

Industrial class = GeoTracker case types Cleanup Program Site, Military Cleanup Site, Military UST Site (gas-station LUST cases excluded). Substations: CEC/HIFLD, Type SUBSTATION, by max kV. 300 m is the "substation on or beside the parcel" proxy (GeoTracker gives a point, not a parcel boundary).


Industrial-class sites open at T=2019 (with coordinates): 7,263; open today: 7,403.


## 1. Pool size by substation distance

| pool | substation | within | sites | of which Cleanup Program | Military |
|---|---|---|---|---|---|
| open_at_2019 | >=115 kV | 300 m | 133 | 104 | 29 |
| open_at_2019 | >=115 kV | 1500 m | 1,379 | 1,138 | 241 |
| open_at_2019 | >=115 kV | 3000 m | 2,780 | 2,250 | 530 |
| open_at_2019 | >=230 kV | 300 m | 20 | 20 | 0 |
| open_at_2019 | >=230 kV | 1500 m | 278 | 265 | 13 |
| open_at_2019 | >=230 kV | 3000 m | 831 | 760 | 71 |
| open_today | >=115 kV | 300 m | 135 | 116 | 19 |
| open_today | >=115 kV | 1500 m | 1,443 | 1,252 | 191 |
| open_today | >=115 kV | 3000 m | 2,928 | 2,465 | 463 |
| open_today | >=230 kV | 300 m | 24 | 24 | 0 |
| open_today | >=230 kV | 1500 m | 292 | 282 | 10 |
| open_today | >=230 kV | 3000 m | 863 | 798 | 65 |

Top counties, open_at_2019, >=115 kV within 300 m: Alameda 42, San Mateo 17, Santa Clara 15, Sonoma 8, Kern 8, Sacramento 7, Los Angeles 5, Yolo 4, San Joaquin 3, Fresno 3, San Diego 3, Contra Costa 3, Shasta 2, San Francisco 2, Santa Barbara 2

Top counties, open_at_2019, >=230 kV within 3000 m: Los Angeles 273, Sacramento 190, San Diego 103, San Mateo 48, Contra Costa 38, Alameda 34, Santa Clara 26, Orange 16, Solano 16, Sonoma 11, Yolo 10, Placer 9, Stanislaus 9, San Francisco 9, Marin 6

Top counties, open_today, >=115 kV within 300 m: Alameda 30, Santa Clara 17, San Francisco 16, San Mateo 13, Kern 9, Sacramento 7, San Diego 6, Sonoma 6, Los Angeles 5, Yolo 4, San Joaquin 3, Fresno 3, Contra Costa 3, Shasta 2, Butte 2

Top counties, open_today, >=230 kV within 3000 m: Los Angeles 310, Sacramento 190, San Diego 80, Alameda 51, San Mateo 44, Santa Clara 42, Contra Costa 29, Orange 20, Solano 13, San Francisco 11, Yolo 9, Placer 8, Stanislaus 8, Kern 8, San Bernardino 7

## 2. Top industrial sites at T=2016 (non-LUST, within 3 km of >=230 kV)

Pool 835 sites, realised 5-year closure 0.163. Top 100 by the full model: closure 0.68, median time to close 1.5 y; top 100 by lookup L2: 0.45. Median distance to the substation 1.94 km. List: `top_industrial_2016.csv`.


## 3. Power plants (EIA-860 2025) x GeoTracker

Source: https://www.eia.gov/electricity/data/eia860/xls/eia8602025.zip (2___Plant, 3_1_Generator Operable and Retired sheets; canceled projects dropped). EIA-860 only lists plants with a generator reported since about 2001, so plants demolished before then are missing. Status: operating = all MW operable; partly retired; retired = no operable MW. Thermal = coal, gas, oil, nuclear, biomass, waste, geothermal (solar/wind/hydro/storage excluded).

| plants | radius | plants | with a GeoTracker case | with an OPEN case | with an open cleanup (LUST/Cleanup/Military) case | MW at plants with an open case |
|---|---|---|---|---|---|---|
| all | 500 m | 2,008 | 785 | 436 | 237 | 31,348 |
| all | 1000 m | 2,008 | 1,113 | 748 | 429 | 46,970 |
| thermal | 500 m | 473 | 327 | 211 | 117 | 27,778 |
| thermal | 1000 m | 473 | 411 | 322 | 198 | 41,125 |
| thermal, retired or partly retired | 500 m | 121 | 87 | 49 | 28 | 13,916 |
| thermal, retired or partly retired | 1000 m | 121 | 107 | 76 | 46 | 18,287 |

Thermal plants with a GeoTracker case within 1 km, by plant status x case status (plants):

```
case            closed case  open case
plant_status                          
operating               244        246
partly retired           51         37
retired                  48         39
```

Thermal plants with an open case within 1 km, by main technology: Natural Gas Fired Combustion Turbine 104, Other Natural Gas 62, Natural Gas Fired Combined Cycle 44, Geothermal 25, Other Waste Biomass 23, Petroleum Liquids 17, Natural Gas Internal Combustion Engine 15, Wood/Wood Waste Biomass 13, Natural Gas Steam Turbine 9, Other Gases 7, Conventional Steam Coal 1, Municipal Solid Waste 1, Petroleum Coke 1

Examples (retired/partly retired thermal plant, open case within 1 km): Humboldt Bay (Natural Gas Internal Combustion Engine, 102 MW retired) - PG&E HUMBOLDT BAY POWER PLANT [Cleanup Program Site, Open - Site Assessment, 339 m]; Hunters Point (Natural Gas Steam Turbine, 427 MW retired) - Lucon, Inc.  - Lucon Inc - 1719 Wallace Ave [* Cannabis Program Site, Active - WDR, 656 m]; Dynegy Moss Landing Power Plant Hybrid (Natural Gas Fired Combined Cycle, 1704 MW retired) - Moss Landing Power Plant [Cleanup Program Site, Open - Verification Monitoring, 120 m]; Geysers Unit 5-20 (Geothermal, 110 MW retired) - SRGC CLASS II WMU [Land Disposal Site, Open, 920 m]; Silver Gate (Petroleum Liquids, 247 MW retired) - Boshart, Michael - HWM Industries, LLC [* Cannabis Program Site, Active - WDR, 848 m]; AES Alamitos LLC (Natural Gas Steam Turbine, 940 MW retired) - SCE - ALAMITOS GENERATING STATION [Cleanup Program Site, Transferred to Other Agency, 158 m]; AES Huntington Beach LLC (Natural Gas Steam Turbine, 803 MW retired) - ASCON LANDFILL [Land Disposal Site, Open - Referred, 768 m]; Long Beach Generation (Natural Gas Fired Combined Cycle, 335 MW retired) - Tidelands Oil Production Co - Wilmington - UIC Project No. 84918002 [Underground Injection Control (UIC), Received, 802 m]; Magnolia (Natural Gas Steam Turbine, 88 MW retired) - BURBANK STEAM PLANT [Cleanup Program Site, Open - Inactive, 77 m]; Grayson (Natural Gas Fired Combined Cycle, 296 MW retired) - Fleming, L.E. [Land Disposal Site, Pre-Title 27 CAI - Completed - Case Closed/No Monitoring, 482 m]; Brawley (Petroleum Liquids, 23 MW retired) - Brawley SoCo Bulk Plant (SC Fuels) [Cleanup Program Site, Open - Remediation, 551 m]; Harbor (Natural Gas Fired Combustion Turbine, 47 MW retired) - PORT OF LA:WILMINGTON WATERFRONT DEVELOPMENT [Cleanup Program Site, Open - Inactive, 248 m]; Haynes (Natural Gas Steam Turbine, 1146 MW retired) - SCE - ALAMITOS GENERATING STATION [Cleanup Program Site, Transferred to Other Agency, 325 m]; Scattergood (Natural Gas Steam Turbine, 497 MW retired) - Cooper & Brain Inc. - El Segundo - UIC Project No. 23200001 [Underground Injection Control (UIC), Received, 288 m]; Valley (CA) (Natural Gas Steam Turbine, 546 MW retired) - Valley Generation Station Landfill - L.A. City DWP [Land Disposal Site, Pre-Title 27 CAI - Closed/No Monitoring, 295 m]

## 4. How many open contaminated sites are plausibly built-out industrial with a live substation?

Of 7,403 industrial-class cleanup cases open today, 135 sit within 300 m of a >=115 kV
substation (24 for >=230 kV), 1,443 within 1.5 km and 2,928 within 3 km
(>=230 kV within 3 km: 863). Power plants are the cleanest test of "infrastructure already on the parcel": of
473 California thermal plants in EIA-860, 188 have an open Cleanup Program or military case within
1 km (546 distinct cases), and 44 of the 121
retired or partly retired thermal plants do (143 cases), several of them the plant's own cleanup case (Moss Landing,
Humboldt Bay, Burbank/Magnolia, Alamitos). On this evidence the "on the parcel" set in California is in the low hundreds: roughly
135 industrial cases beside a >=115 kV substation plus about 188 power-plant sites with an open case,
with overlap; the "near power" set (within 1.5 km of >=115 kV) is about 1,443. Caveats: GeoTracker gives one point per
case, so large sites (refineries, bases, plants) whose point is a centroid are undercounted at 300 m; the substation layer omits many
plant switchyards; "open today" includes inactive and transferred cases; and nothing here checks parcel size, zoning or interconnection
capacity.

