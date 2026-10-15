# Proof 1: drugs approved in the EU or Japan but never in the US

Built 15 Oct 2026 for lane A in `lane_wild.md` (and candidate 2 in `lane_bio.md`). This is the first working
version of the "approved abroad, never approved in the US" list. It runs end to end on public data. The
data is stale, though: the US side stops in **August 2023**. Read the limitations before using any row.

## What is here

| File | What it is |
|---|---|
| `build_gap.py` | The pipeline: name normalisation, entity resolution, joins, classification and back-test. Needs pandas and pyarrow (pyarrow was installed with pip). |
| `gap_list.csv` | 296 ingredients with an EU-centralised or Japanese approval and no US approval in the data. One row per ingredient. |
| `backtest.csv` | Result for 20 drugs that were approved in Europe first and later in the US (or that are still EU only). |
| `us_post_snapshot_manual.csv` | 16 US approvals the data misses, **from memory and not verified**. They only fill a flag column; no row is dropped because of them. |

To rerun (raw data stays in the scratchpad, outside the repo):

```
python3 -I build_gap.py --drugcentral <dir>/drugcentral_2026-10-01/x \
  --epar <dir>/tidytuesday_2023-03-14/drugs.csv --atc <dir>/who_atc_fabkury/atc_2026-04-25.csv \
  --crl <dir>/crl_hmw0905/crl_long2.csv --post-us us_post_snapshot_manual.csv --out .
```

## Counts

| | Rows |
|---|---|
| Ex-US ingredients considered | 1,143 (964 EU-centralised, 496 PMDA) |
| **Gap list (no US approval in the data)** | **296**: 183 EU only, 92 Japan only, 21 EU and Japan |
| By class | 123 small molecule or peptide; 76 biologic or natural product; 66 vaccine or antigen; 23 cell or gene therapy; 8 simple substance or radionuclide |
| Small molecules not caught by the manual US flag | **112**: 27 EU only, 7 EU and Japan, 78 Japan only |
| Of the 34 EU small molecules | 26 still authorised in the EU, 5 EU orphan, 8 withdrawn in the EU |
| Rows with a US CRL in the hand-coded CRL table | 5 (landiolol, vadadustat, sofpironium, Nuceiva's botulinum toxin A, NexoBrid) |

**Treat only the small-molecule rows as real.** The US side has no Purple Book and no vaccine data, so
most biologic, vaccine and cell or gene therapy rows are false positives. NovoSeven, BeneFIX, Kymriah,
Yescarta and Luxturna, for example, are all sold in the US.

The 34 EU small molecules look plausible on a hand read. The list includes ataluren, idebenone,
vernakalant, vildagliptin, agomelatine, parecoxib, atosiban, mifamurtide, pixantrone, vinflunine,
temoporfin, padeliporfin, delamanid, filgotinib, roxadustat, volanesorsen, bulevirtide, linzagolix,
tegafur/gimeracil/oteracil and melatonin. Several of these have known US failures (CRLs for
vernakalant, filgotinib, roxadustat, volanesorsen and bulevirtide). That is a useful feature for the
model, and also a warning: "never approved in the US" often means "tried and failed".

The 78 Japan-only small molecules (for example pemafibrate, imeglimin, mirogabalin, dotinurad,
esaxerenone, valemetostat, tucidinostat, ensitrelvir, rebamipide, loxoprofen and teneligliptin) are the
part US business-development teams are least likely to watch.

## Back-test (`backtest.csv`)

**I could not run a true point-in-time back-test.** I found no data snapshot from before 2016-2019.
DrugCentral v54 is dated 2023-11-01 (all six GitHub mirrors from 2026 hold the same v54), and the EPAR
table is a single copy from 2023-03. What I did instead was a **date reconstruction**: for each drug, I
used the approval dates in the 2023 data to ask "on the day before US approval, did it have an EU or
Japanese approval and no US approval?" This shows the logic would have caught the drug. It does not
prove that a 2016-era dataset would have contained the record, because later data can fill in old
records.

- **Would have been flagged:** 12 of the 20 drugs.
  - pitolisant: EU 2016-03-31, US 2019-08-14, flagged 3.4 years ahead.
  - amifampridine: EU 2009-12-23, US 2018-11-28, flagged 8.9 years ahead.
  - The other 10, with lead times from 0.2 to 11.6 years: tafamidis, migalastat, ivabradine,
    sugammadex, stiripentol, afamelanotide, carglumic acid, eslicarbazepine, retigabine and cholic
    acid.
- **Missed: deflazacort.** It was approved only through EU national procedures (Italy, Spain and
  others), never by the EMA, so it is not in any dataset I could reach. This is the biggest coverage
  hole. Fixing it needs the national registers (ANSM, AIFA, AEMPS, BfArM), and all of them were
  blocked from here.
- **Missed: vamorolone.** Both datasets end before its approvals: FDA 2023-10, EU 2023-12. As far as I
  know (from memory) the US approved it first, so it was never a Europe-first case and is a poor
  back-test target.
- **Correctly not flagged:** eliglustat, lumacaftor and trientine tetrahydrochloride. The US approved
  each of them first; trientine's salt is stripped so it matches Syprine from 1985.
- **Still on the list:** idebenone, ataluren and dinutuximab beta.

## Data sources (all fetched 15 Oct 2026 through github.com or raw.githubusercontent.com)

1. **DrugCentral v54** (dbversion dated 2023-11-01). It provides the approval table with first FDA, EMA
   and PMDA dates per structure, Orange Book products, synonyms and ATC codes. I used a Parquet
   mirror at
   `https://github.com/scriptogre/biomedical-data/releases/download/drugcentral/2026-10-01/drugcentral.tar.gz`
   (tag commit f385dc7b, 985 MB, sha256 fc8fe82b…fdd32, which matches the published checksum). The
   mirror was exported from DrugCentral's public Postgres. I extracted 15 small tables.
   - In this copy, FDA approvals run to 2023-08-18, EMA to 2023-07-26 and PMDA to 2023-12-23.
2. **EMA EPAR table**, `Medicines_output_european_public_assessment_reports.xlsx`, as cleaned by
   TidyTuesday:
   `https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2023/2023-03-14/drugs.csv`
   (repo HEAD b2258ae9, sha256 b6ef5c0d…). It has 1,988 rows, and the latest authorisation in it is
   dated 2023-02-20. It gives the INN, ATC, therapeutic area, orphan and conditional flags, MAH and
   status.
3. **WHO ATC index, 2026-04-25**, scraped by fabkury/atcd:
   `https://raw.githubusercontent.com/fabkury/atcd/master/WHO%20ATC-DDD%202026-04-25.csv`
   (HEAD c5c68334, sha256 93dac139…). I used it for ATC labels and as a fallback lookup from name to
   ATC code.
4. **FDA CRLs, hand-coded** by hmw0905:
   `https://raw.githubusercontent.com/hmw0905/CRL-Deficiency-Analysis/cf7f55f5…/dashboard_data/crl_long2.csv`
   (sha256 f7fc88c1…). It holds 401 CRL events from 2002 to 2026, with product name, sponsor, date and
   deficiency domain or subtype. It is a third-party coding, not the openFDA set.
5. **Open Targets Platform drug tables, Oct 2026** (ChEMBL-based), from the same scriptogre mirror
   (`opentargets/2026-10-01`, sha256 f48f385c…). I downloaded and inspected them but **did not use
   them**: they mark "approved" with no region.

## Could not fetch (blocked by the proxy, or no mirror found)

- **US sources:** Drugs@FDA, the Orange Book after 2023, the Purple Book, openFDA (including the CRL
  API) and the FDA novel-approvals pages.
- **Other regulators and registries:** EMA live downloads, PMDA lists, the EU national registers,
  ChEMBL/EBI FTP, DrugBank, Wikidata, ClinicalTrials.gov, Hugging Face (the Every Cure drug list) and
  Zenodo/Figshare.
- **What I found on GitHub:** no current Drugs@FDA or Orange Book mirror. The only NDC directory copy
  I found holds 73 rows.

## Limitations

1. **The US side is about three years stale.** FDA data ends 2023-08-18, so anything approved in the US
   since then still shows as a gap. `us_post_snapshot_manual.csv` flags 16 rows. 11 are post-snapshot
   approvals I recall: Vafseo, Rapiblyk, Grafapex, Sofdra, Vyalev (×2), Anzupgo, Omvoh, Bimzelx,
   Pombiliti and Nemluvio. The other 5 are matching gaps: isavuconazonium, Ga-68 DOTATOC, ferric
   citrate, NeoTect and Galzin. None of these is verified. Getting a 2026 Drugs@FDA file is the first
   fix to make.
2. **Biologics are unreliable** because there is no Purple Book. See the class column.
3. **EU coverage is centralised procedure only**, as the deflazacort miss shows. Older drugs approved
   nationally, often the cheapest licensing targets, are missing entirely.
4. **Japan coverage depends on DrugCentral's PMDA table** (496 ingredients). It is not the full PMDA
   list, and there is no China, Korea, India or Brazil data.
5. **Entity resolution is rule-based.** It does INN lower-casing, salt and ester stripping,
   sulph→sulf, removal of biologic suffixes, DrugCentral synonym lookup, and a guarded fuzzy match for
   single-token typos (it fixed EPAR's "voxilaprevi" and "ledispavir"). Isavuconazole and ferric
   citrate show the remaining failure mode: the US approved a prodrug or a different salt name that
   DrugCentral files under a different structure.
6. **"No US approval" does not mean "NCE-eligible and available".** The list does not check patents,
   who owns the asset, or whether the foreign sponsor has already filed in the US.

## Grid-queue attrition backtest (separate proof, same folder)

`load_queues.py` and `attrition_backtest.py` test whether public interconnection-queue data predicts which
projects withdraw next year and where capacity frees up. Data: Berkeley Lab "Queued Up" workbooks, end-2024
(`keanuhea/interconnection-queue-analysis`, `data/LBNL_Ix_Queue_Data_File_thru2024_v2.xlsx`) and end-2025
(`tiwari-nikita/grid-storage-analysis`, `data/raw/LBNL_Ix_Queue_Data_File_thru2025.xlsx`) on GitHub.

    python3 -I load_queues.py thru2024.xlsx thru2025.xlsx a.pkl b.pkl
    python3 -I attrition_backtest.py a.pkl b.pkl attrition_results.json

Result (`attrition_results.json`): model AUC 0.721 vs 0.727 for a type x study-phase lookup (leave one region
out), and 0.629 vs 0.648 on the temporal test. No edge from public queue lists alone.
