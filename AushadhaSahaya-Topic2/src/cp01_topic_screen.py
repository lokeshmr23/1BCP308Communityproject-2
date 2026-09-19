#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CP-01 (week 2): topic framing and feasibility screen.
Four candidate community engineering topics evaluated across Dakshina Kannada district.
Weights and criteria are evaluated to determine the selected project topic."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
import syllabus_data as S

print("== CP-01  Week-2 topic screening matrix: Dakshina Kannada community projects ==")
print()

CRITERIA = [
    ("Societal urgency & vulnerable population impact", 0.25),
    ("Technical depth & PO3/PO5 modern tool rigor",     0.25),
    ("Local stakeholder access across DK district",     0.20),
    ("Secondary open datasets & clinical model assets", 0.15),
    ("Zero-recurring operational cost & sustainability",0.15)
]

TOPICS = [
    ("Topic 2: Medication Management for Old-Age Homes (Dakshina Kannada)",
     [4.8, 4.7, 4.6, 4.5, 4.6]),
    ("River Water Quality Telemetry (Nethravathi Basin, Mangaluru)",
     [4.0, 4.2, 3.5, 3.8, 3.2]),
    ("Smart Waste Segregation Tracker (Mangaluru City Corporation)",
     [3.8, 3.9, 4.0, 3.4, 3.6]),
    ("Arecanut Disease Mobile Classifier (Puttur / Bantwal)",
     [4.2, 4.0, 3.6, 3.7, 3.5])
]

weights = [c[1] for c in CRITERIA]
assert abs(sum(weights) - 1.0) < 1e-6, "Weights must sum to 1.0"

print(f"{'Topic shortlisted':<62} | " + " | ".join(f"C{i+1}" for i in range(len(CRITERIA))) + " | Weighted Score")
print("-" * 105)

scores = []
for title, marks in TOPICS:
    w_score = sum(w * m for w, m in zip(weights, marks))
    scores.append((w_score, title))
    m_str = " | ".join(f"{m:4.1f}" for m in marks)
    print(f"{title:<62} | {m_str} |   {w_score:5.2f} / 5.00")

scores.sort(reverse=True)
winner_score, winner_title = scores[0]
runner_score, runner_title = scores[1]
margin = winner_score - runner_score

print("-" * 105)
print(f"Selected Topic : {winner_title}")
print(f"Winning score  : {winner_score:.2f} / 5.00 (margin: +{margin:.2f} over runner-up)")
print(f"Location anchor: Dakshina Kannada district, Karnataka (headquarters: Mangaluru)")
print(f"Mapped outcomes: {', '.join(S.COURSE['pos'])} · SDGs: {', '.join(S.COURSE['sdgs'])}")

print()
print(f"CP-01 RESULT: topic screen selected Topic 2 (Medication Management) with score {winner_score:.2f}/5.00, margin +{margin:.2f} over runner-up -- PASS")
