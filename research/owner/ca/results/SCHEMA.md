# Input schema (2026-10-15)

## statewide/GeoTrackerDownload.zip :: sites.txt

columns (47): GLOBAL_ID, BUSINESS_NAME, STREET_NUMBER, STREET_NAME, CITY, STATE, ZIP, COUNTY, EPA_REGION, LATITUDE, LONGITUDE, COORDINATE_SOURCE, CASE_TYPE, STATUS, STATUS_DATE, CLAIM_NO, CLAIM_STATUS, LEAD_AGENCY, CASEWORKER, LOCAL_AGENCY, RB_CASE_NUMBER, LOC_CASE_NUMBER, FILE_LOCATION, POTENTIAL_CONTAMINANTS_OF_CONCERN, QUANTITY_RELEASED_GALLONS, POTENTIAL_MEDIA_OF_CONCERN, SITE_HISTORY, BEGIN_DATE, LEAK_REPORTED_DATE, HOW_DISCOVERED, HOW_DISCOVERED_DESCRIPTION, DISCHARGE_SOURCE, DISCHARGE_CAUSE, STOP_METHOD, STOP_DESCRIPTION, NO_FURTHER_ACTION_DATE, CALWATER_WATERSHED_NAME, DWR_GROUNDWATER_SUBBASIN_NAME, DISADVANTAGED_COMMUNITY, CALENVIROSCREEN3_SCORE, CALENVIROSCREEN4_SCORE, MILITARY_DOD_SITE, FACILITY_PROJECT_SUBTYPE, RWQCB_REGION, 2022_ASSEMBLY_DISTRICT, 2022_SENATE_DISTRICT, 2022_CONGRESSIONAL_DISTRICT
```
      GLOBAL_ID                            BUSINESS_NAME STREET_NUMBER                 STREET_NAME          CITY STATE    ZIP       COUNTY EPA_REGION          LATITUDE          LONGITUDE        COORDINATE_SOURCE             CASE_TYPE                       STATUS          STATUS_DATE CLAIM_NO CLAIM_STATUS                         LEAD_AGENCY CASEWORKER   LOCAL_AGENCY RB_CASE_NUMBER LOC_CASE_NUMBER                            FILE_LOCATION        POTENTIAL_CONTAMINANTS_OF_CONCERN QUANTITY_RELEASED_GALLONS               POTENTIAL_MEDIA_OF_CONCERN                             SITE_HISTORY           BEGIN_DATE LEAK_REPORTED_DATE HOW_DISCOVERED HOW_DISCOVERED_DESCRIPTION DISCHARGE_SOURCE DISCHARGE_CAUSE STOP_METHOD STOP_DESCRIPTION NO_FURTHER_ACTION_DATE                 CALWATER_WATERSHED_NAME            DWR_GROUNDWATER_SUBBASIN_NAME           DISADVANTAGED_COMMUNITY CALENVIROSCREEN3_SCORE CALENVIROSCREEN4_SCORE MILITARY_DOD_SITE FACILITY_PROJECT_SUBTYPE                        RWQCB_REGION 2022_ASSEMBLY_DISTRICT 2022_SENATE_DISTRICT 2022_CONGRESSIONAL_DISTRICT
0   SL374452458                ARCO MARINE TERMINAL - T3          1400          WEST PIER C STREET    LONG BEACH    CA  90744  Los Angeles          9  33.7731901221004  -118.209714889526  Manual Entry on Screens  Cleanup Program Site       Open - Site Assessment  2015-01-26 00:00:00      NaN          NaN        LOS ANGELES RWQCB (REGION 4)         RO            NaN          0343B             NaN                           Regional Board  Benzene, Toluene, Xylene, Diesel, MT...                       NaN  Aquifer used for drinking water supp...  Tesoro owns and operates Terminal 3,...  2002-06-30 00:00:00                NaN            NaN                        NaN              NaN             NaN         NaN              NaN                    NaN              Dominguez Channel (411.01)  Coastal Plain Of Los Angeles - West ...  Severely Disadvantaged Community                    NaN                    NaN                No                      NaN        LOS ANGELES RWQCB (REGION 4)                     69                   33                          42
1  T10000017805                         CYPRESS CLEANERS          9947                   WALKER ST       CYPRESS    CA  90630       Orange          9        33.8177607       -118.0378939                      NaN  Cleanup Program Site       Open - Site Assessment  1965-01-01 00:00:00      NaN          NaN                       ORANGE COUNTY         TE  ORANGE COUNTY            NaN         09IC009         All Files are only on GeoTracker  Tetrachloroethylene (PCE), Trichloro...                       NaN                                      NaN  Please refer to recent Site Document...                  NaN                NaN            NaN                        NaN              NaN             NaN         NaN              NaN                    NaN    San Gabriel River - Anaheim (845.61)   Coastal Plain Of Orange County (8-001)                               NaN                 41-45%                 35-40%                No                      NaN          SANTA ANA RWQCB (REGION 8)                     67                   36                          45
2  T10000002294  Redwood City Rail Spur (between Bay ...           NaN  Bay Road to Charter Street  REDWOOD CITY    CA  94063    San Mateo          9  37.4860387639807  -122.213287353515          Google Map Move  Cleanup Program Site  Open - Long Term Management  2022-08-11 00:00:00      NaN          NaN  SAN FRANCISCO BAY RWQCB (REGION 2)        DKM            NaN        43S1138             NaN  All Files are on GeoTracker or in th...  Other Chlorinated Hydrocarbons, Poly...                       NaN                                     Soil                                      NaN  2010-07-13 00:00:00                NaN            NaN                        NaN              NaN             NaN         NaN              NaN                    NaN  South Bay - San Mateo Bayside (204.40)  Santa Clara Valley - San Mateo Plain...  Severely Disadvantaged Community                 81-85%                 80-85%                No                      NaN  SAN FRANCISCO BAY RWQCB (REGION 2)                     21                   13                          15
```

## statewide/GeoTrackerDownload.zip :: status_history.txt

columns (3): GLOBAL_ID, STATUS, STATUS_DATE
```
  GLOBAL_ID                          STATUS          STATUS_DATE
0         1          Open - Case Begin Date  2000-08-29 00:00:00
1         1  Open - Verification Monitoring  2000-08-29 00:00:00
2         1         Completed - Case Closed  2000-08-30 00:00:00
```

## statewide/GeoTrackerDownload.zip :: regulatory_activities.txt

columns (4): GLOBAL_ID, ACTION_TYPE, DATE, ACTION
```
     GLOBAL_ID  ACTION_TYPE                 DATE                                   ACTION
0  T0606701131  ENFORCEMENT  2006-10-30 00:00:00  Technical Correspondence / Assistanc...
1  T0606700949  ENFORCEMENT  2005-09-25 00:00:00  Technical Correspondence / Assistanc...
2  T0603790023  ENFORCEMENT  2006-05-31 00:00:00  Technical Correspondence / Assistanc...
```

## statewide/GeoTrackerDownload.zip :: contacts.txt

columns (8): GLOBAL_ID, CONTACT_TYPE, CONTACT_NAME, ORGANIZATION_NAME, ADDRESS, CITY, EMAIL, PHONE_NUMBER
```
      GLOBAL_ID                             CONTACT_TYPE    CONTACT_NAME           ORGANIZATION_NAME                              ADDRESS              CITY                        EMAIL PHONE_NUMBER
0             1  Regional Board Caseworker - Primary ...      BRIAN GREY  LAHONTAN RWQCB (REGION 6T)            2501 LAKE TAHOE BOULEVARD  SOUTH LAKE TAHOE     bgrey@waterboards.ca.gov          NaN
1             1                  Local Agency Caseworker  West Bourgault               PLACER COUNTY  3091 County Center Drive, Suite 180            Auburn       wbourgau@placer.ca.gov          NaN
2  GAOG10011328       SWRCB Contact - Primary Caseworker        EVAN FAU                       SWRCB                            1001 I st        SACRAMENTO  evan.fau@waterboards.ca.gov   9163275613
```

## statewide/GeoTrackerDownload.zip :: readme.txt

columns (2): The files contained in this export are TAB delimited and can be imported/viewed using Microsoft Excel,  Microsoft Access or any other program that can access TAB delimited data.
```
  The files contained in this export are TAB delimited and can be imported/viewed using Microsoft Excel  Microsoft Access or any other program that can access TAB delimited data.
0  NOTE: Some of the data files contain...                                                                                                   NaN                                  
1  There are 4 data files contained in ...                                                                                                   NaN                                  
2  sites.txt - Contains data pertaining...                                                                                                   NaN                                  
```

## statewide/GeoTrackerPermittedUST.zip :: permitted_ust.txt

columns (14): CERSID, FACILITY_ID, BUSINESS_NAME, ADDRESS, CITY, ZIP, COUNTY, PERMITTING_AGENCY, LATITUDE, LONGITUDE, CALENVIROSCREEN4PERCENTILE, 2022_ASSEMBLY_DISTRICT, 2022_SENATE_DISTRICT, 2022_CONGRESSIONAL_DISTRICT
```
     CERSID    FACILITY_ID                 BUSINESS_NAME              ADDRESS           CITY    ZIP       COUNTY                        PERMITTING_AGENCY  LATITUDE   LONGITUDE CALENVIROSCREEN4PERCENTILE 2022_ASSEMBLY_DISTRICT 2022_SENATE_DISTRICT 2022_CONGRESSIONAL_DISTRICT
0  10217281      FA0005739            BONFARE MARKET #38  2600 RIO LINDA BLVD     SACRAMENTO  95815   Sacramento  Sacramento County Environmental Mana...  38.61486  -121.44579                     80-85%                      6                    8                           6
1  10263142  LACoFA0022618                 AQUA PURA INC  310 S ROSEMEAD BLVD       PASADENA  91107  Los Angeles       Los Angeles County Fire Department  34.14112  -118.07294                     45-50%                     49                   25                          28
2  10263178  LACoFA0024092  HMC StratCap 1980 Saturn LLC       1980 SATURN ST  MONTEREY PARK  91755  Los Angeles       Los Angeles County Fire Department  34.03831  -118.11391                     60-65%                     49                   25                          28
```

## statewide/GeoTrackerPermittedUST.zip :: permitted_ust_tanks.txt

columns (45): OWNER_TYPE, FACILITY_TYPE, NUM_OF_INUSE_UST, NUM_OF_CLOSED_UST, NUM_OF_OOS_UST, FACILITY_NAME, FACILITY_STREET, FACILITY_CITY, FACILITY_ZIP, FACILTIY_STATE, EPA_REGION, TRIBAL_LANDS, FACILITY_LATITUDE, FACILITY_LONGITUDE, TANK_OWNER_NAME, TANK_OWNER_MAILING_ADDRESS, TANK_OWNER_MAILING_CITY, TANK_OWNER_MAILING_ZIP, TANK_OWNER_MAILING_STATE, TANK_OPERATOR_NAME, TANK_OPERATOR_MAILING_ADDRESS, TANK_OPERATOR_MAILING_CITY, TANK_OPERATOR_MAILING_ZIP, TANK_OPERATOR_MAILING_STATE, CERSID, TANKIDNUMBER, TANK_STATUS, TANK_CONFIGURATION, TANK_CLOSURE_DATE, TANK_INSTALLATION_DATE, TANK_NUM_OF_COMPARTMENTS, TANK_CONTENTS, TANK_CAPACITY_GALLONS, TANK_TYPE, TANK_PC_CONSTRUCTION, TANK_PWPIPING_CONSTRUCTION, TANK_PIPING_TYPE, TANK_PIPING_CONSTRUCTION, TANK_SACRIFICIAL_ANODE, TANK_CP_IMPRESSED_CURRENT, TANK_CP_SHUTOFF, TANK_ALARMS, TANK_BALL_FLOAT, TANK_SPILL_BUCKET, CALENVIROSCREEN4PERCENTILE
```
       OWNER_TYPE          FACILITY_TYPE NUM_OF_INUSE_UST NUM_OF_CLOSED_UST NUM_OF_OOS_UST                 FACILITY_NAME          FACILITY_STREET FACILITY_CITY FACILITY_ZIP FACILTIY_STATE EPA_REGION TRIBAL_LANDS FACILITY_LATITUDE FACILITY_LONGITUDE                          TANK_OWNER_NAME TANK_OWNER_MAILING_ADDRESS TANK_OWNER_MAILING_CITY TANK_OWNER_MAILING_ZIP TANK_OWNER_MAILING_STATE                       TANK_OPERATOR_NAME   TANK_OPERATOR_MAILING_ADDRESS TANK_OPERATOR_MAILING_CITY TANK_OPERATOR_MAILING_ZIP TANK_OPERATOR_MAILING_STATE    CERSID         TANKIDNUMBER                    TANK_STATUS TANK_CONFIGURATION      TANK_CLOSURE_DATE TANK_INSTALLATION_DATE TANK_NUM_OF_COMPARTMENTS    TANK_CONTENTS TANK_CAPACITY_GALLONS    TANK_TYPE TANK_PC_CONSTRUCTION TANK_PWPIPING_CONSTRUCTION      TANK_PIPING_TYPE TANK_PIPING_CONSTRUCTION TANK_SACRIFICIAL_ANODE TANK_CP_IMPRESSED_CURRENT TANK_CP_SHUTOFF TANK_ALARMS TANK_BALL_FLOAT TANK_SPILL_BUCKET CALENVIROSCREEN4PERCENTILE
0  Non-Government                  Other                0                 1              0       AT&T California - TD214      478 Los Alamos Road    Santa Rosa        94505             CA          9           No        37.2718810       -119.2702330  Pacific Bell Telephone Company dba A...   308 S Akard St Room 1700                  Dallas                  75202                       TX  Pacific Bell Telephone Company dba A...  2600 Camino Ramon - Room 3E000                  San Ramon                     94583                          CA  10114432            TD214U001                    UST Removal   Stand Alone Tank  1/20/2011 12:00:00 AM   1/1/1988 12:00:00 AM                        1           Diesel                  1000  Double Wall                Steel                   Flexible  Conventional Suction            Double Walled                    NaN                       NaN             Yes         Yes              No               Yes                     15-20%
1  Non-Government                  Other                1                 0              0  Metropolitan Recycling, LLC.  2601 S Mount Vernon Ave   Bakersfield        93307             CA          9           No        35.3271740       -118.9671960       Metropolitan Recycling Corporation                PO Box 2716             Bakersfield                  93303                       CA       Metropolitan Recycling Corporation                     PO Box 2716                Bakersfield                     93303                          CA  10117948                #9981  Confirmed/Updated Information   Stand Alone Tank                    NaN  4/15/2002 12:00:00 AM                        1           Diesel                   550  Single Wall                Steel                        NaN                   NaN                      NaN                    NaN                       NaN              No          No              No               NaN                     90-95%
2  Non-Government  Motor Vehicle Fueling              NaN                 0              0        COMMUTER SHELL SERVICE              355 ALMA ST     PALO ALTO        94301             CA          9           No        37.4446490       -122.1653590                    Shell Oil Products US   20945 S. Wilmington Ave.                  Carson                  90810                       CA                                      NaN                             NaN                        NaN                       NaN                         NaN  10078102  135736 Waste Oil #8  Confirmed/Updated Information   Stand Alone Tank                    NaN                    NaN                      NaN  Other Petroleum                   550  Double Wall           Fiberglass                        NaN                   NaN                      NaN                    NaN                       NaN              No         Yes              No               NaN                     15-20%
```

## statewide/GeoTrackerPermittedUST.zip :: PermittedUSTReadMe.txt

columns (2): The file contained in this export is TAB delimited and can be imported/viewed using Microsoft Excel,  Microsoft Access or any other program that can access TAB delimited data.
```
  The file contained in this export is TAB delimited and can be imported/viewed using Microsoft Excel  Microsoft Access or any other program that can access TAB delimited data.
0  permitted_ust.txt - Contains data pe...                                                                                                 NaN                                  
1  permitted_ust_tanks.txt - Contains d...                                                                                                 NaN                                  
2  The data can be opened in Excel usin...                                                                                                 NaN                                  
```

## geo_by_county/SanFranciscoGeoXY.zip :: SanFranciscoGeoXY.txt

columns (13): COUNTY, GLOBAL_ID, FIELD_PT_NAME, FIELD_PT_CLASS, XY_SURVEY_DATE, LATITUDE, LONGITUDE, XY_METHOD, XY_DATUM, XY_ACC_VAL, XY_SURVEY_ORG, GPS_EQUIP_TYPE, XY_SURVEY_DESC
```
          COUNTY     GLOBAL_ID FIELD_PT_NAME FIELD_PT_CLASS XY_SURVEY_DATE    LATITUDE     LONGITUDE XY_METHOD XY_DATUM XY_ACC_VAL               XY_SURVEY_ORG GPS_EQUIP_TYPE              XY_SURVEY_DESC
0  San Francisco  T10000017511        SWB-10             SB     2023-05-17  37.8049456  -122.4330845      CGPS    NAD83          3  "CAL VADA SURVEYING, INC."           L530  "CSRC DATA POINT ""P181"""
1  San Francisco  T10000017511        SWB-09             SB     2023-05-17   37.804907  -122.4333122      CGPS    NAD83          3  "CAL VADA SURVEYING, INC."           L530  "CSRC DATA POINT ""P181"""
2  San Francisco  T10000017511        SWB-08             SB     2023-05-17   37.804199   -122.432936      CGPS    NAD83          3  "CAL VADA SURVEYING, INC."           L530  "CSRC DATA POINT ""P181"""
```

## geo_by_county/SanFranciscoGeoZ.zip :: SanFranciscoGeoZ.txt

columns (12): COUNTY, GLOBAL_ID, FIELD_PT_NAME, ELEV_SURVEY_DATE, ELEVATION, ELEV_METHOD, ELEV_DATUM, ELEV_ACC_VAL, ELEV_SURVEY_ORG, RISER_HT, ELEV_DESC, EFFECTIVE_DATE
```
          COUNTY     GLOBAL_ID FIELD_PT_NAME ELEV_SURVEY_DATE ELEVATION ELEV_METHOD ELEV_DATUM ELEV_ACC_VAL               ELEV_SURVEY_ORG RISER_HT                                ELEV_DESC EFFECTIVE_DATE
0  San Francisco  T10000008940          MW-3       2017-12-07     13.91        CGPS         29           .3  Virgil Chavez Land Surveying      NaN  a disk set up in a step at Mason & C...            NaN
1  San Francisco  T10000008940          MW-2       2017-12-07     13.68        CGPS         29           .3  Virgil Chavez Land Surveying      NaN  a disk set up in a step at Mason & C...            NaN
2  San Francisco  T10000008940          MW-1       2017-12-07     14.22        CGPS         29           .3  Virgil Chavez Land Surveying      NaN  a disk set up in a step at Mason & C...            NaN
```

## geo_by_county/TulareGeoWell.zip :: TulareGeoWell.txt

columns (11): COUNTY, GLOBAL_ID, FIELD_POINT_NAME, STATUS, GW_MEAS_DATE, DTFPROD, DTW, RISER_HT, TOT_DEPTH, GW_MEAS_DESC, SHEEN
```
   COUNTY     GLOBAL_ID FIELD_POINT_NAME STATUS GW_MEAS_DATE DTFPROD     DTW RISER_HT TOT_DEPTH GW_MEAS_DESC SHEEN
0  Tulare  AGC100012325       KBWQA00025    ACT   2024-08-14     NaN     160      NaN       160          NaN     N
1  Tulare  AGC100012325       KBWQA00026    ACT   2024-08-14     NaN     297      NaN       297          NaN     N
2  Tulare  AGC100012328           IR1000    ACT   2021-10-04     NaN  56.144      NaN       NaN          NaN     N
```

## geo_by_county/SanFranciscoFieldPoints.zip :: SanFranciscoFieldPoints.txt

columns (8): COUNTY, GLOBAL_ID, FIELD_PT_NAME, FIELD POINT CLASS, ALTERNATIVE FACILITY ID, DEPTH - TOP OF CASING TO WELL SCREEN (FT), LENGTH OF WELL SCREEN (FT), FIELD POINT DESCRIPTION
```
          COUNTY     GLOBAL_ID FIELD_PT_NAME                        FIELD POINT CLASS ALTERNATIVE FACILITY ID DEPTH - TOP OF CASING TO WELL SCREEN (FT) LENGTH OF WELL SCREEN (FT)                  FIELD POINT DESCRIPTION
0  San Francisco  T10000002730        9187-N  Underground Storage Tank, Tank Pit L...                     NaN                                      NaN                         NaN  UST Removal Soil Sample: North End @...
1  San Francisco  T10000002730     9187-BAY3           Excavation Confirmation Sample                     NaN                                      NaN                         NaN  Confirmation Gab Groundwater Sample:...
2  San Francisco  T10000002730      USTEX_GW           Excavation Confirmation Sample                     NaN                                      NaN                         NaN  Baseline Grab Groundwater Sample: US...
```

## edf_by_county/KingsEDF.zip :: KingsEDF.txt

columns (23): COUNTY, GLOBAL_ID, FIELD_PT_NAME, LOGDATE, LOGTIME, LOGCODE, SAMPID, MATRIX, LABWO , LABCODE, LABSAMPID, ANMCODE, LABLOTCTL, ANADATE, BASIS, PARLABEL, PARVAL, PARVQ, LABDL, REPDL, UNITS, DILFAC, LNOTE
```
  COUNTY     GLOBAL_ID FIELD_PT_NAME     LOGDATE LOGTIME LOGCODE      SAMPID MATRIX   LABWO  LABCODE   LABSAMPID ANMCODE LABLOTCTL     ANADATE BASIS PARLABEL PARVAL PARVQ LABDL REPDL UNITS DILFAC LNOTE
0  Kings  AGC100012334          QCFB  2023-08-14    0835    LSCE  WSJRC10024     WQ  59639-1    EEAM  59639-3_19  E353.2     71406  2023-08-28     N  NO3NO2N   .038     <  .038    .1  MG/L      1   NaN
1  Kings  AGC100012334    WSJRC00002  2022-07-18    1125    LSCE  WSJRC00002      W  11761-1    EEAM  11761-9_10  A2320B     12902  2022-08-01     N      ALK    140     =   .49     2  MG/L      1   NaN
2  Kings  AGC100012334    WSJRC00002  2022-07-18    1125    LSCE  WSJRC00002      W  11761-1    EEAM   11761-9_4  A2540C     14840  2022-08-24     N      TDS   1000     =   8.4    20  MG/L      1    BU
```

## EDF code value counts from KingsEDF.zip (first 759,402 rows)

### PARLABEL (top 80 of 907)

```
PARLABEL
EBZ            17332.0
BZ             17327.0
BZME           17326.0
XYLENES        12978.0
DCA12          11498.0
DCBZ14          9974.0
DCBZ12          9973.0
CLBZ            9959.0
TCE             9895.0
PCE             9890.0
VC              9889.0
DCE11           9886.0
TCA111          9886.0
TCA112          9886.0
PCA             9885.0
CTCL            9880.0
DCA11           9878.0
DCPA12          9878.0
DCE12T          9878.0
BDCME           9874.0
TBME            9874.0
DBCME           9871.0
MTLNCL          9865.0
CLME            9854.0
BRME            9850.0
DCP13C          9842.0
DCP13T          9834.0
TCLME           9833.0
CLEA            9822.0
FC11            9721.0
DCBZ13          9626.0
FC12            9208.0
MTBE            7875.0
EDB             6053.0
CEVETH          5423.0
SO4             5337.0
CL              5179.0
MG              5061.0
CA              5052.0
K               5044.0
DCE12C          4675.0
TDS             4584.0
STY             4481.0
SI              4269.0
ALKB            4164.0
ALKC            4152.0
TCB124          4107.0
ACE             4010.0
HCBU            3976.0
XYLENES1314     3959.0
XYLO            3912.0
CDS             3858.0
DIPE            3823.0
ALK             3803.0
TBA             3780.0
NAPH            3740.0
TAME            3736.0
ETBE            3734.0
TCPR123         3658.0
PHCG            3532.0
DBMA            3489.0
DBCP            3475.0
TC1112          3465.0
BRCLME          3431.0
MEK             3188.0
MIBK            3169.0
HXO2            3017.0
VA              2885.0
TOC             2808.0
IME             2553.0
DCP11           2455.0
DCPA22          2446.0
DCPA13          2446.0
DCBE14T         2433.0
NO3N            2256.0
GRO             2233.0
ACRAMD          2154.0
TMB135          1892.0
TMB124          1892.0
ETHANOL         1787.0
```

### MATRIX (top 80 of 17)

```
MATRIX
WG    244871.0
W     206335.0
WQ    115697.0
WL     89128.0
SO     47172.0
V      40418.0
GV      5973.0
AX      2422.0
GS      2344.0
AA      1955.0
SX      1211.0
AI       949.0
WX       539.0
AD       252.0
DU        72.0
WW        52.0
WP        11.0
```

### UNITS (top 80 of 25)

```
UNITS
UG/L         606193.0
MG/L          46394.0
PPBV          41692.0
MG/KG         32878.0
UG/KG         14205.0
PPMV           5911.0
UG/M3          4690.0
NG/L           2779.0
PPB            1632.0
MG/M3           931.0
PERCENT         851.0
%V/V            488.0
PH UNITS        356.0
UMHOS/CM        187.0
PCI/L            84.0
%/V              34.0
MEQ/L            30.0
NONE             30.0
LAIU             15.0
MGCACO3/L         7.0
PERMIL            6.0
CFU/ML            5.0
DEG F             1.0
DEG C             1.0
MMHOS/CM          1.0
```

### PARVQ (top 80 of 8)

```
PARVQ
ND    492968.0
<     155177.0
=     103018.0
TI      6067.0
DN      1577.0
IN       475.0
>        113.0
NR         6.0
```

### analyte map check (codes from common.ANALYTES present in this county)

```
benzene        ['BZ']
toluene        ['BZME']
ethylbenzene   ['EBZ']
xylenes        ['XYLENES']
mtbe           ['MTBE']
tba            ['TBA']
tphg           ['GROC6C10', 'GROC4C12', 'GASOLINE', 'GROC6C12', 'PHCG', 'GRO', 'GROC5C12']
tphd           ['DROC13C22', 'DROC10C28', 'DRO', 'DROC12C22', 'DIESEL2', 'PHCD', 'DROC10C23', 'DROC12C24']
motoroil       ['MOIL', 'TPHMOTOROIL']
tce            ['TCE']
pce            ['PCE']
cis12dce       ['DCE12C']
vinylchloride  ['VC']
dioxane14      ['DIOXANE14']
cr6            ['CR6']
chromium       ['CR']
lead           ['PB']
arsenic        ['AS']
nitrate        ['NO3NO2N', 'NO3', 'NO3N']
perchlorate    []
pfoa           ['PFOA']
pfos           ['PFOS_A']
tca111         ['TCA111']
dca12          ['DCA12']
dce11          ['DCE11']
edb            ['EDB']
naphthalene    ['NAPH']
```

Top codes not in the map (check for missed analytes): ['DCBZ14', 'DCBZ12', 'CLBZ', 'TCA112', 'PCA', 'CTCL', 'DCA11', 'DCPA12', 'DCE12T', 'BDCME', 'TBME', 'DBCME', 'MTLNCL', 'CLME', 'BRME', 'DCP13C', 'DCP13T', 'TCLME', 'CLEA', 'FC11', 'DCBZ13', 'FC12', 'CEVETH', 'SO4', 'CL', 'MG', 'CA', 'K', 'TDS', 'STY', 'SI', 'ALKB', 'ALKC', 'TCB124', 'ACE', 'HCBU', 'XYLENES1314', 'XYLO', 'CDS', 'DIPE', 'ALK', 'TAME', 'ETBE', 'TCPR123', 'DBMA', 'DBCP', 'TC1112', 'BRCLME', 'MEK', 'MIBK', 'HXO2', 'VA', 'TOC', 'IME', 'DCP11', 'DCPA22', 'DCPA13', 'DCBE14T', 'ACRAMD', 'TMB135']

## cuf/raw captures


