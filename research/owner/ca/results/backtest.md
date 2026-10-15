# California closure backtest

Panel: 96,761 site-snapshots, 27,956 sites. Base rate by T: {2004: 0.247, 2007: 0.297, 2010: 0.386, 2013: 0.386, 2016: 0.279, 2019: 0.225}


## Temporal (train T<=2013, test 2016+2019)

| scorer | AUC | top-decile lift | P@100 |
|---|---|---|---|
| lookup case_type x county | 0.7631 | 2.111 | 0.45 |
| lookup case_type x status x years-open | 0.7684 | 2.933 | 0.88 |
| LightGBM structured only | 0.8417 | 3.25 | 1.0 |
| LightGBM everything | 0.8457 | 3.203 | 0.98 |

## Spatial (leave counties out, pooled)

| scorer | AUC | lift | P@100 |
|---|---|---|---|
| L1 | 0.4591 | 0.992 | 0.33 |
| L2 | 0.694 | 2.016 | 0.83 |
| S | 0.7684 | 2.377 | 0.98 |
| F | 0.7941 | 2.499 | 0.98 |

lust_only: auc_L1=0.5522, auc_L2=0.6629, auc_S=0.7616, auc_F=0.7785

non_lust: auc_L1=0.6714, auc_L2=0.6367, auc_S=0.8053, auc_F=0.8013

with_edf_only: auc_L1=0.6991, auc_L2=0.7547, auc_S=0.8149, auc_F=0.8439

by_T_2016: auc_L1=0.7574, auc_L2=0.7645, auc_S=0.8535, auc_F=0.8594

by_T_2019: auc_L1=0.7658, auc_L2=0.7724, auc_S=0.824, auc_F=0.8265

## Importance share: {'edf': 0.275, 'text': 0.216, 'geo': 0.033, 'neighbours': 0.031, 'struct': 0.446}

Top features: agency, county, case_type, edf_last_year, w_benzene_max_3y, yrs_since_regact, years_open, status_at_T, w_tphg_max_3y, nb_rate, m_tok_SOIL_VAPOR, nb_n, n_contam, lat, n_status_changes, edf_n_years, lon, txt6, txt23, txt15

## Time to closure (closed sites): {'n_train': 24191, 'n_test': 5449, 'median_ttc_test': 1.92, 'mae_model': 1.125, 'mae_lookup': 1.264, 'spearman_model': 0.339, 'spearman_lookup': -0.01}

## Cost: no Cleanup Fund table parsed (cuf.pkl empty)

## Verdict: {'temporal_gain_over_best_lookup': 0.0773, 'temporal_gain_over_structured_ml': 0.004, 'spatial_gain_over_best_lookup': 0.1001, 'spatial_gain_over_structured_ml': 0.0257, 'passes_kill_bar': False, 'kill_bar': 'F - max(L1,L2) >= 0.05 AUC (temporal) and F - S >= 0.02'}
