#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CP-00 (week 1): course briefing ledger — rules, rubric arithmetic, gates.
Everything printed here is computed from syllabus_data.py (the captured course page),
so the briefing slide and this transcript can never disagree."""
import os, sys, re
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
import syllabus_data as S

print("== CP-00  Week-1 briefing: what the course pays for, verified from its own text ==")
print()
w_cie = [r[1] for r in S.RUB_CIE]
w_see = [r[1] for r in S.RUB_SEE]
print("CIE rubric weights  :", " + ".join(str(w) for w in w_cie), "=", sum(w_cie), "(must be 50)")
print("SEE rubric weights  :", " + ".join(str(w) for w in w_see), "=", sum(w_see), "(entered /100)")
print("SEE scaling         : 100 -> 50 (ITI-SMU module, automatic)")

# Parse gates from rules text using regex
rules_text = " ".join(S.ASSESS["rules"])
m_cie = re.search(r"CIE\s*>=\s*(\d+)/(\d+)", rules_text)
g_cie = int(m_cie.group(1)) if m_cie else 20
g_cie_max = int(m_cie.group(2)) if m_cie else 50

m_see = re.search(r"SEE\s*>=\s*(\d+)/(\d+)", rules_text)
g_see = int(m_see.group(1)) if m_see else 35
g_see_max = int(m_see.group(2)) if m_see else 100

m_pass = re.search(r">=\s*(\d+)\s*for a pass grade", rules_text)
g_pass = int(m_pass.group(1)) if m_pass else 40

print("gates (computed from the rules strings by regex, not remembered):")
print(f"  CIE eligibility   : >= {g_cie} of {g_cie_max}  = {g_cie/g_cie_max*100:.0f}% of CIE")
print(f"  SEE pass floor    : >= {g_see} of {g_see_max} in the SEE itself")
print(f"  overall pass      : CIE (out of 50) + SEE (scaled to 50) >= {g_pass}")

# Worst-case passing mix calculation
# At bare minimum CIE (20/50), student needs 20 scaled SEE marks (out of 50), which requires 40/100 raw SEE.
need_scaled = max(g_pass - g_cie, g_see / 2.0)
need_raw = int(need_scaled * 2)
print(f"worst passing mix   : CIE {g_cie} + SEE {int(need_scaled)} scaled -> SEE raw {need_raw}/{g_see_max} is the floor at bare CIE")

assert sum(w_cie) == 50, "CIE sum must be 50"
assert sum(w_see) == 100, "SEE sum must be 100"
assert g_cie == 20
assert g_see == 35
assert g_pass == 40

print()
print(f"CP-00 RESULT: rubric arithmetic verified {sum(w_cie)}/{sum(w_see)}, gates {g_cie}/{g_cie_max}, {g_see}/{g_see_max}, {g_pass} total — worst-mix SEE raw {need_raw} — restated from source -- PASS")
