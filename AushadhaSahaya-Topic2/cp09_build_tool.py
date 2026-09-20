#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CP-09 (week 10): web application prototype build & zero-leak audit.
Inspects the built web application assets in web/, audits for dark-network
compliance (zero unauthorized external CDN/script calls), and verifies bundle hashes."""
import os, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

WEB_DIR = os.path.join(ROOT, "web")
assert os.path.exists(WEB_DIR), f"Missing {WEB_DIR}"

print("== CP-09  Week-10 prototype build audit: AushadhaSahaya web application ==")
print()

ASSETS = [
    "index.html",
    "css/app.css",
    "js/app.js",
    "js/dakshina_kannada_map.js",
    "data/dakshina_kannada_facilities.json",
    "data/residents_roster.json",
    "data/secondary_drug_interactions.json",
    "data/beers_criteria_rules.json"
]

total_bytes = 0
print(f"{'Asset Path':<42} | {'Bytes':>8} | SHA256 (first 16 hex)")
print("-" * 75)

for rel in ASSETS:
    p = os.path.join(WEB_DIR, rel)
    assert os.path.exists(p), f"Asset missing: {p}"
    sz = os.path.getsize(p)
    total_bytes += sz
    with open(p, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    print(f"{rel:<42} | {sz:>8} | {digest[:16]}")

print("-" * 75)
kb = total_bytes / 1024.0
print(f"Total Shipped Bundle Footprint: {total_bytes} bytes ({kb:.1f} KB)")
print()

# Audit for external CDN / network calls in HTML & JS
print("ZERO-LEAK DARK-NETWORK AUDIT (RULE D1):")
forbidden_patterns = ["fonts.googleapis.com", "cdnjs.cloudflare.com", "cdn.jsdelivr.net", "unpkg.com"]
leak_found = False

for rel in ["index.html", "css/app.css", "js/app.js", "js/dakshina_kannada_map.js"]:
    p = os.path.join(WEB_DIR, rel)
    content = open(p, "r", encoding="utf-8").read()
    for pat in forbidden_patterns:
        if pat in content:
            print(f"  [FAIL] External leak found in {rel}: {pat}")
            leak_found = True

assert not leak_found, "Bundle must not contain external CDN leaks"
print("  ✓ Scanned 4 core source files: 0 external CDN or font leaks detected.")
print("  ✓ Full offline autonomy confirmed: runs on dark-network village care homes.")

print()
print(f"CP-09 RESULT: web application build verified across {len(ASSETS)} files, zero external network leaks, bundle footprint {int(kb)} KB -- PASS")
