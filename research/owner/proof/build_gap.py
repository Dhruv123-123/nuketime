#!/usr/bin/env python3
"""Build a list of active ingredients approved in the EU (EMA centralised) and/or Japan (PMDA)
that have no US (FDA) approval in the same data.

Inputs are local copies of public datasets (see README.md for exact URLs and snapshot dates):
  --drugcentral DIR   DrugCentral v54 parquet tables (approval, structures, synonyms, struct2atc,
                      atc, ob_product, struct2obprod)
  --epar CSV          EMA EPAR export (TidyTuesday 2023-03-14 copy of
                      Medicines_output_european_public_assessment_reports.xlsx)
  --atc CSV           WHO ATC-DDD index (fabkury/atcd copy, 2026-04-25)
  --crl CSV           Hand-coded FDA CRL table (hmw0905/CRL-Deficiency-Analysis crl_long2.csv)
  --post-us CSV       Small manual list of US approvals after the data snapshot (analyst memory,
                      unverified) used only to FLAG rows, never to drop them silently.
  --out DIR           Where gap_list.csv and backtest.csv are written.

Requires pandas and pyarrow. Run with `python -I`.
"""
import argparse
import difflib
import re
import sys
from pathlib import Path

import pandas as pd

# ----------------------------------------------------------------------------------------------
# Name normalisation
# ----------------------------------------------------------------------------------------------
SALT_WORDS = {
    "hydrochloride", "dihydrochloride", "monohydrochloride", "hcl", "hydrobromide", "hydroiodide",
    "sodium", "disodium", "trisodium", "potassium", "dipotassium", "calcium", "magnesium", "zinc",
    "lithium", "aluminium", "aluminum", "ammonium",
    "mesylate", "mesilate", "dimesylate", "dimesilate", "besylate", "besilate", "tosylate",
    "tosilate", "edisylate", "edisilate", "napsylate", "napsilate", "isethionate", "esylate",
    "esilate", "maleate", "hydrogen", "fumarate", "hemifumarate", "tartrate", "bitartrate",
    "hydrogentartrate", "succinate", "hemisuccinate", "citrate", "dihydrogen", "acetate",
    "diacetate", "sulfate", "sulphate", "hemisulfate", "bisulfate", "phosphate", "diphosphate",
    "nitrate", "lactate", "gluconate", "malate", "oxalate", "embonate", "pamoate", "stearate",
    "trifluoroacetate", "bromide", "chloride", "iodide", "meglumine", "trometamol",
    "tromethamine", "olamine", "ethanolamine", "diolamine", "choline", "benzoate", "salicylate",
    "carbonate", "bicarbonate", "hydrogencarbonate", "glycinate", "lysinate", "arginine",
    "hydrate", "monohydrate", "dihydrate", "trihydrate", "tetrahydrate", "pentahydrate",
    "hemihydrate", "sesquihydrate", "anhydrous", "solvate", "ethanolate", "propylene", "glycol",
    "free", "base", "acid",
    # esters / pro-moiety suffixes that do not change the active moiety for "ever approved" purposes
    "furoate", "propionate", "dipropionate", "valerate", "butyrate", "palmitate", "decanoate",
    "enanthate", "undecanoate", "cipionate", "cypionate", "hexanoate", "axetil", "pivoxil",
    "medoxomil", "mofetil", "micronised", "micronized", "liposomal", "pegylated", "monohydrated",
}
# 'acid' is stripped only when the remainder is still a word (e.g. "obeticholic acid" ->
# "obeticholic"); both forms are indexed, so this widens matching rather than narrowing it.


def basic_norm(s: str) -> str:
    s = str(s).lower().strip()
    s = s.replace("‐", "-").replace("–", "-").replace(" ", " ")
    s = s.replace("sulph", "sulf")
    s = re.sub(r"\(.*?\)", " ", s)              # drop "(as hydrochloride)" etc.
    s = re.sub(r"\[.*?\]", " ", s)
    s = re.sub(r"-[a-z]{4}$", "", s)             # US biologic suffix e.g. "-hziy"
    s = re.sub(r"[^a-z0-9 \-]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def strip_salts(s: str) -> str:
    toks = [t for t in s.split(" ") if t]
    kept = [t for t in toks if t not in SALT_WORDS]
    return " ".join(kept) if kept else s


def keys_for(name: str) -> set:
    """All lookup keys for a name: normalised and salt-stripped, with and without spaces/hyphens."""
    b = basic_norm(name)
    out = set()
    for v in {b, strip_salts(b)}:
        if not v:
            continue
        out.add(v)
        out.add(v.replace("-", " "))
        out.add(v.replace(" ", "").replace("-", ""))
    return out


def split_ingredients(s: str) -> list:
    """Split an EPAR active-substance string into single ingredients."""
    if not isinstance(s, str) or not s.strip():
        return []
    s = re.sub(r"\(.*?\)", " ", s)
    parts = re.split(r"\s*/\s*|;\s*|,\s*|\s+and\s+|\s+\+\s+", s.lower())
    return [p.strip() for p in parts if p and p.strip() and len(p.strip()) > 2]


VACCINE_RX = re.compile(r"vaccin|virus|antigen|toxoid|strain|polysaccharide|conjugate|pertussis|"
                        r"pertactin|haemagglutin|hemagglutin|fimbri|serotype|bordetella|neisseria|"
                        r"haemophilus|influenzae|pneumoniae|meningitidis|ebola|zoster|rotavirus|"
                        r"papilloma|sars-cov|spike|mrna|dengue|chikungunya|cholera|typhoid|rabies|"
                        r"encephalitis|anthracis")
CELL_GENE_RX = re.compile(r"autologous|allogeneic|cells?\b|leucel|\bcel\b|temcel|parvovec|vec\b|"
                          r"tiparvovec|gene |transduced|chondrocyte|stem|darvadstrocel")
BIO_RX = re.compile(r"mab\b|cept\b|\b(alfa|beta|gamma|delta|zeta|theta|epsilon|pegol)\b|ase\b|"
                    r"cog\b|ermin\b|grastim|immunoglobulin|toxin|insulin|human |recombinant|fibrinogen|"
                    r"thrombin|inhibitor|protein|factor|calcitonin|serum|extract|powder|bark|enzyme|"
                    r"globulin|albumin|heparin|nyxthracis|semen|pancrea|cartilage|interferon|alfacon")


SIMPLE = {"zinc", "lysine", "potassium hydrogen carbonate", "taurine", "sodium selenite", "yttrium",
          "lutetium", "fytic acid"}


def classify(name: str, atc: str) -> str:
    n = str(name).lower()
    if n in SIMPLE:
        return "simple_substance_or_radionuclide"
    if str(atc).startswith("J07") or VACCINE_RX.search(n):
        return "vaccine_or_antigen"
    if CELL_GENE_RX.search(n):
        return "cell_or_gene_therapy"
    if BIO_RX.search(n):
        return "biologic_or_natural_product"
    return "small_molecule_or_peptide"


# ----------------------------------------------------------------------------------------------
# Loaders
# ----------------------------------------------------------------------------------------------
def load_drugcentral(d: Path):
    appr = pd.read_parquet(d / "approval.parquet")
    appr["approval"] = pd.to_datetime(appr["approval"], errors="coerce")
    st = pd.read_parquet(d / "structures.parquet", columns=["id", "name", "cas_reg_no", "status"])
    syn = pd.read_parquet(d / "synonyms.parquet")
    s2a = pd.read_parquet(d / "struct2atc.parquet")
    atc = pd.read_parquet(d / "atc.parquet")
    ob = pd.read_parquet(d / "ob_product.parquet")
    s2o = pd.read_parquet(d / "struct2obprod.parquet")

    # synonym index: key -> set(struct_id)
    idx = {}
    def add(name, sid):
        for k in keys_for(name):
            idx.setdefault(k, set()).add(int(sid))
    for r in st.itertuples():
        add(r.name, r.id)
    for r in syn.dropna(subset=["id"]).itertuples():
        add(r.name, r.id)

    first = (appr.dropna(subset=["approval"]).groupby(["struct_id", "type"]).approval.min()
             .unstack())
    fda_first = first.get("FDA")
    ema_first = first.get("EMA")
    pmda_first = first.get("PMDA")

    ob_structs = set(s2o.struct_id.astype(int))
    ob_first = (s2o.merge(ob[["id", "approval_date"]], left_on="prod_id", right_on="id")
                .assign(d=lambda x: pd.to_datetime(x.approval_date, errors="coerce"))
                .groupby("struct_id").d.min())
    # Orange Book ingredient strings (covers moieties DrugCentral did not map to a structure)
    ob_keys = set()
    for ing in ob.ingredient.dropna().unique():
        for part in re.split(r";\s*", ing):
            ob_keys |= keys_for(part)

    atc_by_struct = (s2a.groupby("struct_id").atc_code.apply(lambda x: ";".join(sorted(set(x)))))
    names = st.set_index("id").name
    return dict(idx=idx, fda_first=fda_first, ema_first=ema_first, pmda_first=pmda_first,
                ob_structs=ob_structs, ob_first=ob_first, ob_keys=ob_keys,
                atc_by_struct=atc_by_struct, names=names, atc=atc, appr=appr)


def load_who_atc(p: Path):
    a = pd.read_csv(p, dtype=str)
    lvl5 = a[a.atc_code.str.len() == 7]
    by_name = {}
    for r in lvl5.itertuples():
        for k in keys_for(r.atc_name):
            by_name.setdefault(k, set()).add(r.atc_code)
    labels = dict(zip(a.atc_code, a.atc_name))
    return by_name, labels


# ----------------------------------------------------------------------------------------------
def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--drugcentral", required=True, type=Path)
    ap.add_argument("--epar", required=True, type=Path)
    ap.add_argument("--atc", required=True, type=Path)
    ap.add_argument("--crl", required=True, type=Path)
    ap.add_argument("--post-us", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    a = ap.parse_args(argv)

    dc = load_drugcentral(a.drugcentral)
    who_by_name, atc_labels = load_who_atc(a.atc)
    idx = dc["idx"]

    idx_keys = sorted(k for k in idx if len(k) >= 8)
    fuzzy_used = {}

    def resolve(name):
        sids = set()
        for k in keys_for(name):
            sids |= idx.get(k, set())
        if not sids:
            # spelling-variant fallback (e.g. EPAR typo "voxilaprevi"); exact keys tried first
            k0 = strip_salts(basic_norm(name))
            if len(k0) >= 8:
                for m in difflib.get_close_matches(k0, idx_keys, n=3, cutoff=0.9):
                    a_t, b_t = k0.split(), m.split()
                    diff = [(x, y) for x, y in zip(a_t, b_t) if x != y]
                    # accept only a single-token spelling variant of a long token
                    if len(a_t) == len(b_t) and len(diff) == 1 and min(map(len, diff[0])) >= 6 \
                            and difflib.SequenceMatcher(None, *diff[0]).ratio() >= 0.9:
                        sids = set(idx[m])
                        fuzzy_used[name] = m
                        break
        return sids

    def us_first_date(sids, name):
        """Earliest US date (FDA approval table or Orange Book product) for any matched structure.
        Returns (date or NaT, evidence)."""
        dates = []
        for s in sids:
            if dc["fda_first"] is not None and s in dc["fda_first"].index and pd.notna(dc["fda_first"][s]):
                dates.append(dc["fda_first"][s])
            if s in dc["ob_first"].index and pd.notna(dc["ob_first"][s]):
                dates.append(dc["ob_first"][s])
        if dates:
            return min(dates), "drugcentral_fda_or_orangebook"
        if any(s in dc["ob_structs"] for s in sids):
            return pd.NaT, "orangebook_product_no_date"
        if keys_for(name) & dc["ob_keys"]:
            return pd.NaT, "orangebook_name_match"
        return None, ""

    # ---------------- EU (EMA centralised) ----------------
    e = pd.read_csv(a.epar)
    e = e[(e.category == "human") & e.marketing_authorisation_date.notna()]
    e = e[~e.generic.fillna(False).astype(bool) & ~e.biosimilar.fillna(False).astype(bool)]
    e["ma_date"] = pd.to_datetime(e.marketing_authorisation_date, errors="coerce")
    rows = []
    for r in e.itertuples():
        src = r.common_name if isinstance(r.common_name, str) else r.active_substance
        for ing in split_ingredients(src):
            rows.append(dict(ingredient_raw=ing, ma_date=r.ma_date, product=r.medicine_name,
                             mah=r.marketing_authorisation_holder_company_name,
                             status=r.authorisation_status, orphan=bool(r.orphan_medicine),
                             conditional=bool(r.conditional_approval),
                             exceptional=bool(r.exceptional_circumstances),
                             atc=r.atc_code if isinstance(r.atc_code, str) else "",
                             ta=r.therapeutic_area if isinstance(r.therapeutic_area, str) else "",
                             n_ingredients=len(split_ingredients(src))))
    eu = pd.DataFrame(rows)
    eu["key"] = eu.ingredient_raw.map(lambda s: strip_salts(basic_norm(s)))
    eu["struct_ids"] = eu.ingredient_raw.map(lambda s: tuple(sorted(resolve(s))))

    # entity key: DrugCentral structure if resolved, else normalised name
    eu["entity"] = [("DC:" + ",".join(map(str, s))) if s else ("NAME:" + k)
                    for s, k in zip(eu.struct_ids, eu.key)]

    def agg_eu(g):
        g = g.sort_values("ma_date")
        return pd.Series(dict(
            ingredient=g.key.iloc[0],
            struct_ids=g.struct_ids.iloc[0],
            eu_first_date=g.ma_date.min(),
            eu_products="; ".join(dict.fromkeys(g["product"])),
            eu_mah="; ".join(dict.fromkeys(g.mah.dropna())),
            eu_status="authorised" if (g.status == "authorised").any() else "withdrawn_only",
            eu_orphan=g.orphan.any(), eu_conditional=g.conditional.any(),
            eu_exceptional=g.exceptional.any(),
            eu_only_in_combination=(g.n_ingredients > 1).all(),
            eu_atc="; ".join(sorted({x for x in g.atc if x})),
            therapeutic_area="; ".join(dict.fromkeys(t.strip() for x in g.ta for t in x.split(";") if t.strip())),
        ))
    eu_ent = eu.groupby("entity").apply(agg_eu, include_groups=False).reset_index()

    # add EMA approvals that only DrugCentral knows (structure-keyed)
    if dc["ema_first"] is not None:
        known = {s for t in eu_ent.struct_ids for s in t}
        extra = []
        for sid, d in dc["ema_first"].dropna().items():
            if int(sid) in known:
                continue
            extra.append(dict(entity=f"DC:{int(sid)}", ingredient=dc["names"].get(sid, ""),
                              struct_ids=(int(sid),), eu_first_date=d, eu_products="",
                              eu_mah="", eu_status="(drugcentral only)", eu_orphan=None,
                              eu_conditional=None, eu_exceptional=None,
                              eu_only_in_combination=False, eu_atc="", therapeutic_area=""))
        eu_ent = pd.concat([eu_ent, pd.DataFrame(extra)], ignore_index=True)
    # where EPAR date is missing/later than DrugCentral's EMA date, keep the earlier
    if dc["ema_first"] is not None:
        def dc_ema(t):
            ds = [dc["ema_first"][s] for s in t if s in dc["ema_first"].index and pd.notna(dc["ema_first"][s])]
            return min(ds) if ds else pd.NaT
        eu_ent["eu_first_date"] = [min(x for x in [a_, dc_ema(t)] if pd.notna(x)) if (pd.notna(a_) or pd.notna(dc_ema(t))) else pd.NaT
                                   for a_, t in zip(eu_ent.eu_first_date, eu_ent.struct_ids)]

    # ---------------- Japan (PMDA, DrugCentral only) ----------------
    jp = {}
    if dc["pmda_first"] is not None:
        for sid, d in dc["pmda_first"].dropna().items():
            jp[int(sid)] = d

    # ---------------- assemble all ex-US entities ----------------
    ent = eu_ent.copy()
    ent["jp_first_date"] = [min([jp[s] for s in t if s in jp], default=pd.NaT) for t in ent.struct_ids]
    eu_structs = {s for t in ent.struct_ids for s in t}
    jp_only = [dict(entity=f"DC:{s}", ingredient=dc["names"].get(s, ""), struct_ids=(s,),
                    eu_first_date=pd.NaT, jp_first_date=d) for s, d in jp.items() if s not in eu_structs]
    ent = pd.concat([ent, pd.DataFrame(jp_only)], ignore_index=True)

    us = [us_first_date(set(t), n) for t, n in zip(ent.struct_ids, ent.ingredient)]
    ent["us_first_date"] = [u[0] if u[0] is not None else pd.NaT for u in us]
    ent["us_evidence"] = [u[1] for u in us]
    ent["us_found"] = [u[0] is not None for u in us]
    ent["match_method"] = ["drugcentral_structure" if t else "name_only" for t in ent.struct_ids]
    ent.loc[ent.ingredient.isin(fuzzy_used), "match_method"] = "drugcentral_fuzzy"
    ent["product_class"] = [classify(n, c) for n, c in zip(ent.ingredient, ent.get("eu_atc", pd.Series([""] * len(ent))).fillna(""))]

    # ATC: EPAR code, else DrugCentral struct2atc, else WHO name lookup
    def atc_for(row):
        if isinstance(row.get("eu_atc"), str) and row["eu_atc"]:
            return row["eu_atc"]
        codes = set()
        for s in row["struct_ids"]:
            if s in dc["atc_by_struct"].index:
                codes |= set(dc["atc_by_struct"][s].split(";"))
        if not codes:
            for k in keys_for(row["ingredient"]):
                codes |= who_by_name.get(k, set())
        return "; ".join(sorted(codes))
    ent["atc_codes"] = ent.apply(atc_for, axis=1)
    first_code = ent.atc_codes.str.split(";").str[0].str.strip().fillna("")
    ent["atc_l1"] = first_code.str[:1].map(lambda c: atc_labels.get(c, "") if c else "")
    ent["atc_l2"] = first_code.str[:3].map(lambda c: atc_labels.get(c, "") if c else "")

    ent["regions"] = [("EU" if pd.notna(eu_d) else "") + ("+" if pd.notna(eu_d) and pd.notna(jp_d) else "") + ("JP" if pd.notna(jp_d) else "")
                      for eu_d, jp_d in zip(ent.eu_first_date, ent.jp_first_date)]

    # ---------------- CRL join (US rejection on record) ----------------
    crl = pd.read_csv(a.crl)
    crl_ev = crl.drop_duplicates("event_id")[["event_id", "product_name", "sponsor", "crl_date"]]
    crl_ev["norm"] = crl_ev.product_name.map(basic_norm)
    def crl_hits(name):
        k = strip_salts(basic_norm(name))
        if len(k) < 5:
            return ""
        pat = re.compile(r"\b" + re.escape(k) + r"\b")
        h = crl_ev[crl_ev.norm.str.contains(pat)]
        return "; ".join(f"{p} ({s}, {d})" for p, s, d in zip(h.product_name, h.sponsor, h.crl_date))

    # ---------------- post-snapshot US flag (manual, unverified) ----------------
    post = pd.read_csv(a.post_us, comment="#")
    post_keys = {}
    for r in post.itertuples():
        for k in keys_for(r.ingredient):
            post_keys[k] = f"{r.us_brand} {r.us_approval} [{r.source}]"
    def post_flag(name):
        for k in keys_for(name):
            if k in post_keys:
                return post_keys[k]
        return ""

    gap = ent[~ent.us_found].copy()
    gap["us_crl_on_record"] = gap.ingredient.map(crl_hits)
    gap["us_approved_after_snapshot_manual"] = gap.ingredient.map(post_flag)
    gap["eu_first_year"] = pd.to_datetime(gap.eu_first_date).dt.year.astype("Int64")
    gap["jp_first_year"] = pd.to_datetime(gap.jp_first_date).dt.year.astype("Int64")
    gap["drugcentral_struct_ids"] = gap.struct_ids.map(lambda t: ";".join(map(str, t)))
    cols = ["ingredient", "product_class", "regions", "eu_first_year", "eu_first_date", "jp_first_year", "jp_first_date",
            "eu_products", "eu_mah", "eu_status", "eu_orphan", "eu_conditional", "eu_exceptional",
            "eu_only_in_combination", "atc_codes", "atc_l1", "atc_l2", "therapeutic_area",
            "match_method", "drugcentral_struct_ids", "us_crl_on_record",
            "us_approved_after_snapshot_manual"]
    gap = gap[cols].sort_values(["regions", "eu_first_date", "jp_first_date", "ingredient"])
    gap["eu_first_date"] = pd.to_datetime(gap.eu_first_date).dt.date
    gap["jp_first_date"] = pd.to_datetime(gap.jp_first_date).dt.date
    a.out.mkdir(parents=True, exist_ok=True)
    gap.to_csv(a.out / "gap_list.csv", index=False)

    # ---------------- back-test ----------------
    targets = ["pitolisant", "amifampridine", "deflazacort", "vamorolone", "tafamidis", "migalastat",
               "ivabradine", "sugammadex", "stiripentol", "afamelanotide", "carglumic acid",
               "eslicarbazepine acetate", "retigabine", "cholic acid", "idebenone", "ataluren",
               "dinutuximab beta", "eliglustat", "lumacaftor", "trientine tetrahydrochloride"]
    bt = []
    for t in targets:
        sids = resolve(t)
        m = ent[ent.struct_ids.map(lambda x: bool(set(x) & sids)) | (ent.ingredient == strip_salts(basic_norm(t)))]
        eu_d = m.eu_first_date.min() if len(m) else pd.NaT
        jp_d = m.jp_first_date.min() if len(m) else pd.NaT
        usd, ev = us_first_date(sids, t)
        if usd is None:
            usd = pd.NaT
        exfirst = min([x for x in [eu_d, jp_d] if pd.notna(x)], default=pd.NaT)
        if pd.isna(exfirst):
            verdict = "MISSED: no EU-centralised or PMDA record in data"
        elif pd.isna(usd):
            verdict = "ON CURRENT LIST (no US approval in data)" if ev == "" else "US record without date"
        elif exfirst < usd:
            verdict = f"WOULD FLAG for {(usd - exfirst).days / 365.25:.1f} yrs before US approval (date reconstruction)"
        else:
            verdict = "NOT FLAGGED: US approval came first"
        bt.append(dict(drug=t, eu_first=eu_d.date() if pd.notna(eu_d) else "",
                       jp_first=jp_d.date() if pd.notna(jp_d) else "",
                       us_first=usd.date() if pd.notna(usd) else "", us_evidence=ev, verdict=verdict))
    bt = pd.DataFrame(bt)
    bt.to_csv(a.out / "backtest.csv", index=False)

    # ---------------- summary ----------------
    g = gap
    print("ex-US entities considered:", len(ent), "| EU:", ent.eu_first_date.notna().sum(),
          "| JP:", ent.jp_first_date.notna().sum())
    print("gap list rows:", len(g))
    print(g.regions.value_counts().to_string())
    print(g.product_class.value_counts().to_string())
    sm = g[g.product_class == "small_molecule_or_peptide"]
    print("small molecule/peptide by region:", sm.regions.value_counts().to_dict())
    print("small molecule/peptide, EU still authorised:", ((sm.eu_status == "authorised")).sum(),
          "| not flagged by manual post-snapshot list:", ((sm.us_approved_after_snapshot_manual == "")).sum())
    print("fuzzy-matched names:", fuzzy_used)
    print("EU-authorised (not withdrawn-only):", (g.eu_status == "authorised").sum())
    print("EU orphan:", (g.eu_orphan == True).sum())
    print("only in EU combination products:", (g.eu_only_in_combination == True).sum())
    print("matched to DrugCentral structure:", (g.match_method == "drugcentral_structure").sum())
    print("with US CRL on record:", (g.us_crl_on_record != "").sum())
    print("flagged US-approved after snapshot (manual):", (g.us_approved_after_snapshot_manual != "").sum())
    print(g.atc_l1.replace("", "(no ATC)").value_counts().to_string())
    print(bt.to_string())
    return 0


if __name__ == "__main__":
    sys.exit(main())
