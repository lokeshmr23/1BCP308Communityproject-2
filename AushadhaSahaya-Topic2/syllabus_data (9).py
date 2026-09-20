# -*- coding: utf-8 -*-
"""Syllabus data module for VTU 2025 Scheme - 1BCP308 Community Project / Societal Project.
Topic 2: Medication management system for an old-age home.
Design and develop a web-based application to monitor the administration of medicine to senior citizens residing at an old-age home.
"""

COURSE = {
    "code": "1BCP308",
    "name": "Community Project / Societal Project (Project-Based Learning)",
    "scheme": "VTU 2025 Scheme (AEC/SDC, Semester III, 1 credit)",
    "pedagogy": "0:0:0:30:30 — 0 lecture, 0 tutorial, 0 lab contact; 30 h term work + 30 h self-learning",
    "topic_id": 2,
    "topic_title": "Medication management system for an old-age home. Design and develop a web-based application to monitor the administration of medicine to senior citizens residing at an old-age home.",
    "short_title": "AushadhaSahaya — Medication Management System for Senior Citizens in Old-Age Homes",
    "district": "Dakshina Kannada",
    "state": "Karnataka, India",
    "headquarters": "Mangaluru",
    "pos": ["PO3", "PO5", "PO6", "PO8"],
    "sdgs": ["SDG 3 (Good Health and Well-Being, Targets 3.8 & 3.d)", "SDG 10 (Reduced Inequalities)"],
}

RUB_CIE = [
    ("Problem identification & relevance to society/environment", 8, [8, 6, 4, 2]),
    ("Formation of problem statement; engineering approach, innovation & feasibility", 10, [10, 8, 5, 2]),
    ("Interaction with stakeholders; data collection, analysis & interpretation", 8, [8, 6, 4, 2]),
    ("Project documentation; clarity, organization & problem-solving demonstrated", 10, [10, 8, 5, 2]),
    ("Communication & presentation skills", 6, [6, 5, 3, 2]),
    ("Contribution & benefit to society (impact, sustainability)", 8, [8, 6, 4, 2]),
]

RUB_SEE = [
    ("Problem identification & relevance to society/environment", 16, [16, 12, 8, 4]),
    ("Formation of problem statement; engineering approach, innovation & feasibility", 20, [20, 15, 10, 5]),
    ("Interaction with stakeholders; data collection, analysis & interpretation", 16, [16, 12, 8, 4]),
    ("Project documentation; clarity, technical rigor & problem-solving demonstrated", 20, [20, 15, 10, 5]),
    ("Communication, presentation & viva-voce responses", 12, [12, 9, 6, 3]),
    ("Contribution & benefit to society; impact assessment & sustainability", 16, [16, 12, 8, 4]),
]

ASSESS = {
    "cie_max": 50,
    "see_max_raw": 100,
    "see_scaled": 50,
    "total": 100,
    "rules": [
        "CIE >= 20/50 (minimum) to become eligible to appear for the SEE.",
        "SEE >= 35/100 in the SEE itself to be eligible for pass consideration.",
        "CIE (out of 50) + SEE (scaled to 50) >= 40 for a pass grade; otherwise grade F (Fail)."
    ]
}

TLP = [
    (1, "Course introduction, objectives, ethics, conduct, and assessment briefing", "Explain course scope, rules, rubrics, and expected deliverables", "Understand course requirements and form teams", "Team list, course plan"),
    (2, "Community problem identification and topic selection", "Guide Topic Framing and Feasibility — Identify local issues through discussion and observation", "Select geriatric healthcare need in Dakshina Kannada old-age homes", "Shortlisted project topic"),
    (3, "Stakeholder interaction and preliminary survey", "Demonstrate survey methods and stakeholder engagement", "Conduct survey across caregivers, nurses, and administrators in Dakshina Kannada old-age homes", "Survey notes, interview record"),
    (4, "Problem statement and objective formulation", "Review and refine problem statement, scope, and objectives", "Freeze quantifiable problem statement and system requirements", "Approved problem statement"),
    (5, "Literature/case study review and baseline analysis", "Suggest relevant references and examples", "Analyze existing medication tracking, open datasets, and paper-based MAR failures", "Baseline analysis summary"),
    (6, "Project planning and role assignment", "Help teams organize tasks, timeline, and responsibilities", "Develop 15-week WBS, Gantt chart, milestones, and risk float", "Work plan / Gantt chart"),
    (7, "Feasibility analysis and solution brainstorming", "Check technical feasibility and practicality", "Assess device availability, offline resilience, and zero-recurring cost in old-age homes", "Solution alternatives sheet"),
    (8, "Selection of final solution and design approach", "Review final concept and design logic", "Design web application architecture, interaction graph, and Dakshina Kannada geospatial engine", "Concept note / design outline"),
    (9, "Data processing / calculations / sizing / mapping", "Support computations and technical review", "Integrate secondary datasets (OpenFDA, NIH RxNorm, AGS Beers, Dakshina Kannada care homes)", "Technical analysis sheet"),
    (10, "Prototype / model / audit / DPR / app development", "Monitor progress and correct technical issues", "Develop deployable web application with offline storage, schedule tracking, and interaction checker", "Working model / draft DPR / map / app"),
    (11, "Testing, refinement, and implementation planning", "Evaluate technical correctness and improvements", "Execute automated test suites, drug interaction truth table, and UI contrast audit", "Test results / revised output"),
    (12, "Field implementation / demonstration / awareness activity", "Facilitate community interaction and documentation", "Simulate 12-week pilot administration across Dakshina Kannada old-age homes", "Photos, attendance, implementation record"),
    (13, "Documentation of outcomes, feedback, and impact", "Review report structure and completeness", "Compile quantitative adherence metrics, time savings, and Detailed Project Report (DPR)", "Draft report"),
    (14, "Presentation preparation and viva practice", "Conduct mock presentation and feedback", "Verify byte reproducibility across all capture logs, build checksum audit deck", "Presentation deck"),
    (15, "Final presentation, submission, and reflection", "Evaluate performance using rubrics", "Present live application, defend against rubric criteria, submit verified ledger", "Final report, presentation, viva")
]

CO = [
    ("CO1", "L2 – Understand", "Identify and analyze societal problems through field interaction and technical assessment."),
    ("CO2", "L3 – Apply", "Develop skills in project planning, field survey, data collection, implementation, documentation, and reporting."),
    ("CO3", "L3 – Apply", "Apply principles of social responsibility in engineering practice through community-oriented interventions."),
    ("CO4", "L4 – Analyze", "Exhibit multidisciplinary learning, problem-solving ability, and communication skills based on collected data (requirements), stakeholder feedback, and baseline conditions."),
    ("CO5", "L5 – Evaluate", "Choose feasible societal problem statements and solutions considering practical constraints and sustainability aspects."),
    ("CO6", "L6 – Create", "Create a product by collaborating with stakeholders and within the team to deliver a product/project to the intended community/organization.")
]

PO = [
    ("PO3", "Design/development of solutions: Design solutions for complex engineering problems and design system components or processes that meet the specified needs with appropriate consideration for public health and safety."),
    ("PO5", "Modern tool usage: Create, select, and apply appropriate techniques, resources, and modern IT and engineering tools to complex engineering activities, with an understanding of the limitations."),
    ("PO6", "The engineer and society: Apply reasoning informed by contextual knowledge to assess societal, health, safety, legal, and cultural issues and the consequent responsibilities relevant to professional engineering practice."),
    ("PO8", "Ethics: Apply ethical principles and commit to professional ethics and responsibilities and norms of the engineering practice.")
]

SDG = [
    ("SDG 3", "Good Health and Well-Being", "Target 3.8: Achieve universal health coverage, including financial risk protection, access to quality essential health-care services and access to safe, effective, quality and affordable essential medicines. Target 3.d: Strengthen the capacity of all countries, in particular developing countries, for early warning, risk reduction and management of national and global health risks."),
    ("SDG 10", "Reduced Inequalities", "Target 10.2: Empower and promote the social, economic and political inclusion of all, irrespective of age, disability or other status.")
]
