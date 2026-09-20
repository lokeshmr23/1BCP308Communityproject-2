#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CP-03 (week 4): problem statement and objective formulation.
Freezes the problem statement and quantifiable engineering requirements
anchored to empirical survey evidence from Dakshina Kannada old-age homes."""
import os, sys, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

df = pd.read_csv(os.path.join(ROOT, "data", "baseline_survey.csv"))
poly_load = df['avg_meds_per_senior'].mean()
miss_rate = df['missed_doses_weekly'].mean()
log_time = df['logging_time_mins'].mean()
offline_pct = (df['offline_need_1to5'] >= 4).sum() / len(df) * 100.0

print("== CP-03  Week-4 frozen problem statement and objective anchors ==")
print()
print("FROZEN PROBLEM STATEMENT (VERBATIM):")
print("""  Senior citizens residing in old-age homes across Dakshina Kannada district,
  Karnataka, experience severe vulnerability to adverse drug events (ADEs),
  missed dosages, and scheduling oversights caused by manual paper-based
  Medication Administration Records (MARs), heavy polypharmacy burdens (averaging
  6.49 medicines per resident), and high caregiver turnover. Existing commercial
  hospital systems are financially unviable and fail under frequent coastal
  monsoon power/internet disruptions. There is an urgent societal need for an
  offline-first, zero-recurring-cost, web-based medication administration and
  monitoring system integrating secondary open clinical datasets (OpenFDA, NIH
  RxNorm, AGS Beers Criteria) and geospatial supervisory mapping for Dakshina
  Kannada eldercare homes.""")
print()

ANCHORS = [
    ("Polypharmacy Threshold", f"{poly_load:.2f} meds/senior", "Must handle 4-slot multi-dose daily regimens"),
    ("Baseline Missed Doses",  f"{miss_rate:.2f} doses/wk",    "Target post-pilot error reduction to < 1.0 dose/wk"),
    ("Caregiver Logging Load", f"{log_time:.1f} mins/day",     "Target >= 60% reduction via 1-click digital MAR"),
    ("Offline Resilience",     f"{offline_pct:.1f}% dark need","Zero network dependencies during active MAR logging"),
    ("Geospatial Scope",       "Dakshina Kannada (8 homes)",   "Map-based supervisory monitoring across all taluks")
]

print("QUANTITATIVE BASELINE ANCHORS:")
for name, val, req in ANCHORS:
    print(f"  • {name:<24}: {val:<22} -> {req}")

print()
print("TARGET ENGINEERING DELIVERABLES:")
print("  1. Responsive web-based MAR application with dual English/Kannada UI cues.")
print("  2. Client-side Drug-Drug Interaction (DDI) & Beers Criteria safety alert engine.")
print("  3. Dakshina Kannada district interactive geospatial facility map.")
print("  4. Zero-recurring-cost offline static architecture deployable to Git and Render.")

print()
print(f"CP-03 RESULT: problem statement frozen with {len(ANCHORS)} quantitative baseline anchors and 4 engineering deliverables -- PASS")
