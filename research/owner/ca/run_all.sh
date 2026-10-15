#!/usr/bin/env bash
# Single entry point for the California powered-brownfield experiment.
#   ./run_all.sh                      download everything (~5 GB), build, backtest, simulate
#   SKIP_DOWNLOAD=1 ./run_all.sh      reuse what is in $CA_DATA
#   CA_DATA=/path CA_JOBS=3 ./run_all.sh
# Needs ~30 GB free disk for the EDF stream and ~12 GB RAM at CA_JOBS=3.
set -euo pipefail
cd "$(dirname "$0")"
export CA_DATA="${CA_DATA:-$PWD/data}"
export CA_WORK="${CA_WORK:-$CA_DATA/work}"
export CA_RESULTS="${CA_RESULTS:-$PWD/results}"
mkdir -p "$CA_DATA" "$CA_WORK" "$CA_RESULTS"
python3 -m pip install -q pandas numpy scipy scikit-learn lightgbm lxml 2>/dev/null || true

step() { echo; echo "=== $(date +%H:%M:%S) $1"; }
step "download";   if [ "${SKIP_DOWNLOAD:-0}" != "1" ]; then python3 download.py "$@"; fi
step "schema";     python3 schema.py
step "sites";      python3 build_sites.py
step "edf";        python3 build_edf.py
step "geo";        python3 build_geo.py
step "panel";      python3 build_panel.py
step "backtest";   python3 backtest.py
step "buy_sim";    python3 buy_sim.py
cp "$CA_WORK/SCHEMA.md" "$CA_RESULTS/SCHEMA.md" 2>/dev/null || true
step "done"; ls -la "$CA_RESULTS"
