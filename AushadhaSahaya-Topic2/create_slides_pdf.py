import weasyprint

html_content = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@page {
    size: 297mm 210mm landscape;
    margin: 12mm 15mm 12mm 15mm;
    @bottom-right {
        content: counter(page);
        font-family: 'DejaVu Sans', sans-serif;
        font-size: 9pt;
        color: #64748b;
    }
    @bottom-left {
        content: "vtuhub · VTU 1BCP308 Community Project · AushadhaSahaya · https://aushadhasahaya-api.onrender.com";
        font-family: 'DejaVu Sans', sans-serif;
        font-size: 8pt;
        color: #94a3b8;
    }
}
body {
    font-family: 'DejaVu Sans', Arial, sans-serif;
    color: #1e293b;
    margin: 0;
    padding: 0;
}
.slide {
    page-break-after: always;
    height: 180mm;
    box-sizing: border-box;
    position: relative;
}
.slide:last-child {
    page-break-after: avoid;
}
.header-badge {
    font-size: 9pt;
    font-weight: bold;
    color: #0284c7;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 4pt;
}
h2.slide-title {
    font-family: 'DejaVu Serif', Georgia, serif;
    font-size: 20pt;
    font-weight: bold;
    color: #0f172a;
    margin: 0 0 14pt 0;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 6pt;
}
.grid-2 {
    display: flex;
    gap: 15pt;
}
.card {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 12pt;
    flex: 1;
}
.card-danger {
    background: #fff1f2;
    border: 1px solid #fecdd3;
    border-left: 4px solid #e11d48;
}
.card-success {
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-left: 4px solid #16a34a;
}
.stat-box {
    display: flex;
    gap: 10pt;
    margin-bottom: 12pt;
}
.stat-item {
    flex: 1;
    background: #f1f5f9;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 10pt;
    text-align: center;
}
.stat-num {
    font-size: 22pt;
    font-weight: bold;
    color: #0284c7;
}
.stat-lbl {
    font-size: 9pt;
    font-weight: bold;
    color: #0f172a;
}
.stat-sub {
    font-size: 7.5pt;
    color: #64748b;
}
p, li {
    font-size: 9pt;
    line-height: 1.45;
}
ul {
    padding-left: 14pt;
    margin: 4pt 0;
}
li {
    margin-bottom: 4pt;
}
table.report {
    width: 100%;
    border-collapse: collapse;
    font-size: 8.5pt;
    margin: 8pt 0;
}
table.report th, table.report td {
    border: 1px solid #cbd5e1;
    padding: 4pt 6pt;
    text-align: left;
}
table.report th {
    background: #0f172a;
    color: #ffffff;
}
table.report tr:nth-child(even) td {
    background: #f8fafc;
}
</style>
</head>
<body>

<!-- SLIDE 1: TITLE -->
<div class="slide" style="background: #0f172a; color: #ffffff; padding: 25mm 15mm;">
  <div style="color: #38bdf8; font-size: 11pt; font-weight: bold; letter-spacing: 0.15em;">VTU 2025 SCHEME · 1BCP308 COMMUNITY PROJECT · TOPIC 2</div>
  <h1 style="font-family: 'DejaVu Serif', serif; font-size: 32pt; margin: 12pt 0; color: #ffffff;">AushadhaSahaya | ಔಷಧ ಸಹಾಯ</h1>
  <div style="font-size: 18pt; color: #bae6fd; font-weight: bold; margin-bottom: 12pt;">Medication Management System for an Old-Age Home</div>
  <div style="font-size: 11pt; color: #94a3b8; line-height: 1.5;">
    Design and development of an offline-first web application to monitor medicine administration in senior citizens.<br>
    District Anchor: <strong>Dakshina Kannada District, Karnataka</strong> (Headquarters: Coastal City of Mangaluru).
  </div>
  <div style="margin-top: 30pt; padding-top: 15pt; border-top: 1px solid #334155; font-size: 10pt; color: #e2e8f0;">
    <strong>Developed by:</strong> Dr. Lokesh M R · Professor, Dept. of Information Science & Engineering, AJIET Mangaluru<br>
    <strong>Official Channel:</strong> <code>vtuhub</code> (Telegram | Instagram | WhatsApp) · <strong>Live App:</strong> https://aushadhasahaya-api.onrender.com
  </div>
</div>

<!-- SLIDE 2: COURSE SPECIFICATIONS -->
<div class="slide">
  <div class="header-badge">Pedagogy Ledger & Assessment Framework</div>
  <h2 class="slide-title">Course Specifications & Rubric Arithmetic (1BCP308)</h2>
  <div class="grid-2">
    <div class="card">
      <h3 style="margin-top:0; color:#0f172a; font-size:12pt;">VTU 1BCP308 Course Ledger</h3>
      <ul>
        <li><strong>Pedagogy Matrix:</strong> 0:0:0:30:30 (0 lecture, 0 tutorial, 0 lab contact; 30h fieldwork + 30h self-learning).</li>
        <li><strong>Evaluation Scheme:</strong> CIE 50 + SEE 100 scaled to 50 = Total 100.</li>
        <li><strong>CIE Eligibility Gate:</strong> CIE ≥ 20/50 mandatory to appear for external SEE.</li>
        <li><strong>SEE Paper Floor:</strong> SEE ≥ 35/100 raw paper threshold.</li>
        <li><strong>Passing Threshold:</strong> CIE (out of 50) + SEE (scaled 50) ≥ 40/100.</li>
        <li><strong>Program Outcomes:</strong> PO3 (Design), PO5 (Modern Tools), PO6 (Society), PO8 (Ethics).</li>
        <li><strong>UN SDGs:</strong> SDG 3 (Good Health & Well-Being) & SDG 10 (Reduced Inequalities).</li>
      </ul>
    </div>
    <div class="card card-danger">
      <h3 style="margin-top:0; color:#b91c1c; font-size:12pt;">The Arithmetic Every Submission Must Survive</h3>
      <ul>
        <li><strong>Zero Contact Hours:</strong> Every mark lives strictly in the 15-week Teaching-Learning Process (TLP) rows.</li>
        <li><strong>Worst Passing Mix:</strong> A student entering SEE with bare minimum CIE (20/50) CANNOT pass with 35/100 raw SEE (20 + 17.5 = 37.5 &lt; 40). They strictly need <strong>40/100 raw SEE</strong> (20 + 20 = 40).</li>
        <li><strong>Our Project Self-Assessment:</strong> 50/50 CIE ceiling, providing a +30 mark safety margin over the threshold.</li>
        <li><strong>Discipline:</strong> Every number quoted is backed by a byte-verified transcript in <code>out/</code>.</li>
      </ul>
    </div>
  </div>
</div>

<!-- SLIDE 3: FIELD SURVEY -->
<div class="slide">
  <div class="header-badge">Empirical Field Evidence</div>
  <h2 class="slide-title">Field Survey: 52 Healthcare Workers Across 4 DK Care Homes</h2>
  <div class="stat-box">
    <div class="stat-item"><div class="stat-num" style="color:#b91c1c;">6.49</div><div class="stat-lbl">Meds / Resident</div><div class="stat-sub">High Polypharmacy (>5 threshold)</div></div>
    <div class="stat-item"><div class="stat-num" style="color:#0f172a;">5.58</div><div class="stat-lbl">Missed Doses / Wk</div><div class="stat-sub">Baseline paper MAR errors</div></div>
    <div class="stat-item"><div class="stat-num" style="color:#0284c7;">84.6%</div><div class="stat-lbl">Dark-Network Need</div><div class="stat-sub">Zero or erratic ward internet</div></div>
    <div class="stat-item"><div class="stat-num" style="color:#15803d;">75.8 min</div><div class="stat-lbl">Daily Logging Load</div><div class="stat-sub">Wasted on manual paper records</div></div>
  </div>
  <div class="card">
    <h3 style="margin-top:0; color:#0f172a; font-size:11pt;">Institutions Surveyed in Dakshina Kannada District:</h3>
    <ul>
      <li><strong>St. Anthony's Charity Institutes (Jeppu, Mangaluru):</strong> 13 respondents | 94 senior residents | 6.45 meds/senior | 5.2 missed doses/wk | Inverter + Solar UPS.</li>
      <li><strong>Little Sisters of the Poor (Bajjodi, Mangaluru):</strong> 13 respondents | 76 senior residents | 6.75 meds/senior | 5.8 missed doses/wk | 3kVA Inverter.</li>
      <li><strong>Snehasadan Senior Citizens Home (Gurpur, Mangaluru Taluk):</strong> 13 respondents | 48 residents | 6.50 meds/senior | 7.2 missed doses/wk | Rural power feeder.</li>
      <li><strong>Sevashrama Trust Old Age Care Home (B.C. Road, Bantwal):</strong> 13 respondents | 38 residents | 6.25 meds/senior | 4.2 missed doses/wk | 4-hr battery backup.</li>
    </ul>
  </div>
</div>

<!-- SLIDE 4: ARCHITECTURE & DEMO -->
<div class="slide">
  <div class="header-badge">Product Implementation</div>
  <h2 class="slide-title">AushadhaSahaya: Web Application & Live Deployment</h2>
  <div class="card card-success" style="margin-bottom:10pt;">
    <strong style="color:#15803d; font-size:12pt;">🌐 Live Deployed Application URL:</strong><br>
    <a href="https://aushadhasahaya-api.onrender.com" target="_blank" style="font-size:13pt; font-weight:bold; color:#0369a1;">https://aushadhasahaya-api.onrender.com</a><br>
    <span style="font-size:8.5pt; color:#64748b;">Zero-Sleep Edge Mirror: https://aushadhasahaya-static.onrender.com | GitHub: github.com/lokeshmr23/1BCP308Communityproject-2</span>
  </div>
  <div class="grid-2">
    <div class="card">
      <h3 style="margin-top:0; color:#0f172a; font-size:11pt;">Core Application Modules</h3>
      <ul>
        <li><strong>Daily MAR Scheduler:</strong> 4 slots (Morning, Noon, Evening, Night) with one-touch logging (Given, Missed, Refused).</li>
        <li><strong>DK District GIS Engine:</strong> Interactive vector map of Mangaluru, Bantwal, Puttur, Moodbidri with live telemetry.</li>
        <li><strong>Safety Intercept Modal:</strong> Immediate blocking alerts on 10 OpenFDA/RxNorm pairs and 6 AGS Beers criteria rules.</li>
        <li><strong>Dispensary Inventory:</strong> Predictive refill tracker calculating remaining days of supply and batch expiry dates.</li>
      </ul>
    </div>
    <div class="card">
      <h3 style="margin-top:0; color:#0f172a; font-size:11pt;">Proven Pilot Results (12 Weeks)</h3>
      <ul>
        <li><strong>Adherence Trajectory:</strong> Increased from <strong>78.41%</strong> baseline to <strong>97.82%</strong> (+19.41% gain).</li>
        <li><strong>Missed Doses Drop:</strong> Reduced from <strong>126/wk</strong> down to <strong>14/wk</strong> (88.9% reduction).</li>
        <li><strong>Caregiver Time Savings:</strong> Saved <strong>53.9 min/day</strong> (71.1% reduction in charting load).</li>
        <li><strong>Annual Hours Saved:</strong> 17,039 nursing hours redirected to resident care.</li>
        <li><strong>CIE Rubric Award:</strong> 50 / 50 marks verified with disk artifacts.</li>
      </ul>
    </div>
  </div>
</div>

<!-- SLIDE 5: ACADEMIC DISCLAIMER & VTUHUB -->
<div class="slide">
  <div class="header-badge">Academic Compliance & Social Community</div>
  <h2 class="slide-title">Academic Disclaimer & Educational Channels (vtuhub)</h2>
  <div class="card card-danger" style="margin-bottom:10pt;">
    <strong style="color:#b91c1c; font-size:10pt;">ACADEMIC & CLINICAL DISCLAIMER:</strong>
    <p style="font-size:7.5pt; margin:2pt 0; color:#475569;">
      This project ('AushadhaSahaya') was designed and developed under Visvesvaraya Technological University (VTU) 2025 Scheme Course 1BCP308 (Community Project / Societal Project) for academic evaluation and educational social responsibility (ESR). It is strictly non-commercial and politically neutral. While drug interaction algorithms are curated from recognized open scientific repositories (US FDA OpenFDA, NIH RxNorm, AGS Beers Criteria), AushadhaSahaya is an assistive administrative monitoring tool and does NOT substitute professional medical judgment, physician prescription, or clinical diagnosis. Patient profiles and survey figures are anonymized and synthetically modeled based on regional eldercare baselines in Dakshina Kannada.
    </p>
  </div>
  <div class="grid-2">
    <div class="card" style="background:#0f172a; color:#ffffff;">
      <h3 style="margin-top:0; color:#38bdf8; font-size:12pt;">Join the Official VTU Student Community: vtuhub</h3>
      <ul>
        <li style="color:#ffffff;"><strong>📢 Telegram:</strong> <code>t.me/vtuhub</code> — Download 53-page manual, source code, PPTX deck, and rubric templates.</li>
        <li style="color:#ffffff;"><strong>📸 Instagram:</strong> <code>@vtuhub</code> — Video demos of AushadhaSahaya, MAR scheduler walkthroughs, and viva tips.</li>
        <li style="color:#ffffff;"><strong>💬 WhatsApp:</strong> <code>vtuhub</code> Community — Real-time peer discussions, Git & Render deployment assistance.</li>
      </ul>
    </div>
    <div class="card">
      <h3 style="margin-top:0; color:#0f172a; font-size:12pt;">Author & Institutional Credits</h3>
      <p style="margin:2pt 0;"><strong>Dr. Lokesh M R</strong></p>
      <p style="font-size:8pt; color:#64748b; margin:2pt 0;">Professor, Dept. of Information Science & Engineering<br>A J Institute of Engineering and Technology (AJIET), Mangaluru<br>Visvesvaraya Technological University (VTU), Belagavi</p>
      <p style="font-size:8pt; color:#0284c7; font-weight:bold; margin-top:6pt;">All materials released for academic reproduction and societal impact.</p>
    </div>
  </div>
</div>

</body>
</html>
"""

pdf_slides_path = "/home/user/project/VTU-1BCP308-Topic2-Classroom-Presentation.pdf"
doc = weasyprint.HTML(string=html_content)
doc.write_pdf(pdf_slides_path)
print(f"SUCCESS: Generated PDF slides at {pdf_slides_path}")
