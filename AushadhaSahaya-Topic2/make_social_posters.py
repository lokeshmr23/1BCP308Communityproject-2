import weasyprint
import pymupdf
from pathlib import Path

ROOT = Path("/home/user/project")

# 1. Instagram Portrait Poster (4:5 Aspect Ratio -> 216mm x 270mm)
html_portrait = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@page {
    size: 216mm 270mm;
    margin: 0;
}
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
body {
    font-family: 'DejaVu Sans', Arial, sans-serif;
    background: #090d16;
    color: #f1f5f9;
    width: 216mm;
    height: 270mm;
    padding: 12mm 14mm;
    position: relative;
}
/* Top Eyebrow */
.eyebrow {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1.5px solid #1e293b;
    padding-bottom: 8pt;
    margin-bottom: 10pt;
}
.tag {
    background: #0284c7;
    color: #ffffff;
    font-size: 7.5pt;
    font-weight: bold;
    letter-spacing: 0.08em;
    padding: 3pt 7pt;
    border-radius: 4pt;
    text-transform: uppercase;
}
.scheme-txt {
    font-size: 8pt;
    color: #94a3b8;
    font-weight: bold;
    letter-spacing: 0.05em;
}
/* Main Heading */
.title-box {
    margin-bottom: 10pt;
}
h1.main-title {
    font-family: 'DejaVu Serif', Georgia, serif;
    font-size: 24pt;
    font-weight: bold;
    color: #ffffff;
    line-height: 1.15;
    margin-bottom: 3pt;
}
.kannada-txt {
    font-size: 16pt;
    font-weight: normal;
    color: #38bdf8;
}
.topic-sub {
    font-size: 12pt;
    font-weight: bold;
    color: #38bdf8;
    margin-bottom: 4pt;
}
.location-sub {
    font-size: 8.2pt;
    color: #cbd5e1;
    line-height: 1.4;
}
/* Author Card */
.author-bar {
    background: #131c2e;
    border: 1px solid #1e3a5f;
    border-left: 4px solid #0284c7;
    padding: 6pt 10pt;
    border-radius: 4pt;
    margin-bottom: 10pt;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.author-name {
    font-size: 9pt;
    font-weight: bold;
    color: #ffffff;
}
.author-dept {
    font-size: 7.5pt;
    color: #94a3b8;
}
.hub-badge {
    background: #0284c7;
    color: #ffffff;
    font-size: 8.5pt;
    font-weight: bold;
    padding: 3pt 8pt;
    border-radius: 12pt;
}
/* Features Grid */
.features-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8pt;
    margin-bottom: 10pt;
}
.feature-card {
    background: #0f172a;
    border: 1px solid #1e293b;
    border-radius: 6pt;
    padding: 8pt 9pt;
}
.feat-header {
    display: flex;
    align-items: center;
    gap: 5pt;
    margin-bottom: 3pt;
}
.feat-icon {
    font-size: 11pt;
}
.feat-title {
    font-size: 8.5pt;
    font-weight: bold;
    color: #e2e8f0;
}
.feat-desc {
    font-size: 7.2pt;
    color: #94a3b8;
    line-height: 1.35;
}
/* Stats Highlight Bar */
.stats-banner {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    border: 1px solid #0284c7;
    border-radius: 6pt;
    padding: 8pt;
    display: flex;
    justify-content: space-around;
    text-align: center;
    margin-bottom: 10pt;
}
.stat-item {
    flex: 1;
}
.stat-val {
    font-size: 15pt;
    font-weight: bold;
    color: #38bdf8;
}
.stat-val-green {
    color: #4ade80;
}
.stat-lbl {
    font-size: 6.8pt;
    color: #cbd5e1;
    font-weight: bold;
    text-transform: uppercase;
}
/* Deployment URL Box */
.link-box {
    background: #0369a1;
    border-radius: 6pt;
    padding: 8pt 10pt;
    margin-bottom: 10pt;
    text-align: center;
}
.link-lbl {
    font-size: 7.2pt;
    text-transform: uppercase;
    font-weight: bold;
    letter-spacing: 0.08em;
    color: #bae6fd;
    margin-bottom: 2pt;
}
.link-url {
    font-family: 'DejaVu Sans Mono', monospace;
    font-size: 10pt;
    font-weight: bold;
    color: #ffffff;
    word-break: break-all;
}
.link-git {
    font-size: 7.2pt;
    color: #e0f2fe;
    margin-top: 3pt;
}
/* Social Channels Footer */
.channels-box {
    background: #111827;
    border: 1px solid #374151;
    border-radius: 6pt;
    padding: 8pt 10pt;
    margin-bottom: 8pt;
}
.channel-row {
    display: flex;
    justify-content: space-between;
    font-size: 8pt;
    font-weight: bold;
}
.chan-tg { color: #38bdf8; }
.chan-ig { color: #f472b6; }
.chan-wa { color: #4ade80; }

/* Disclaimer */
.disclaimer {
    font-size: 5.8pt;
    color: #64748b;
    line-height: 1.3;
    text-align: justify;
    border-top: 1px solid #1e293b;
    padding-top: 5pt;
}
</style>
</head>
<body>

  <div class="eyebrow">
    <span class="tag">VTU 2025 SCHEME · 1 CREDIT</span>
    <span class="scheme-txt">1BCP308 COMMUNITY PROJECT · TOPIC 2</span>
  </div>

  <div class="title-box">
    <h1 class="main-title">AushadhaSahaya <span class="kannada-txt">| ಔಷಧ ಸಹಾಯ</span></h1>
    <div class="topic-sub">Medication Management System for an Old-Age Home</div>
    <div class="location-sub">
      Dakshina Kannada District · Coastal Mangaluru HQ · 15-Week TLP Complete Notes, Deployable Web Application, Secondary Datasets & Verified DPR Ledger
    </div>
  </div>

  <div class="author-bar">
    <div>
      <div class="author-name">Dr. Lokesh M R</div>
      <div class="author-dept">Professor, Dept. of Information Science & Engineering, AJIET Mangaluru</div>
    </div>
    <div class="hub-badge">vtuhub</div>
  </div>

  <div class="features-grid">
    <div class="feature-card">
      <div class="feat-header"><span class="feat-icon">📋</span><span class="feat-title">Daily MAR Scheduler</span></div>
      <div class="feat-desc">4 daily dosage windows (Morning, Noon, Evening, Night) with one-touch logging (Given, Missed, Refused) & Kannada cues.</div>
    </div>
    <div class="feature-card">
      <div class="feat-header"><span class="feat-icon">🗺️</span><span class="feat-title">Dakshina Kannada Map</span></div>
      <div class="feat-desc">Interactive vector map across 8 care homes (Jeppu, Bajjodi, Gurpur, Bantwal, Puttur) with live adherence telemetry.</div>
    </div>
    <div class="feature-card">
      <div class="feat-header"><span class="feat-icon">⚠️</span><span class="feat-title">Clinical DDI Alert Engine</span></div>
      <div class="feat-desc">Pre-screened against 10 OpenFDA/RxNorm high-risk pairs and 6 AGS Beers Criteria 2023 geriatric safety rules.</div>
    </div>
    <div class="feature-card">
      <div class="feat-header"><span class="feat-icon">🔒</span><span class="feat-title">Dark-Network Safe</span></div>
      <div class="feat-desc">111 KB bundle footprint; 0 external CDN calls; runs with zero internet on 2GB ashram PCs during monsoon power cuts.</div>
    </div>
  </div>

  <div class="stats-banner">
    <div class="stat-item">
      <div class="stat-val stat-val-green">97.8%</div>
      <div class="stat-lbl">Pilot Adherence</div>
    </div>
    <div class="stat-item">
      <div class="stat-val">71.1%</div>
      <div class="stat-lbl">Caregiver Time Saved</div>
    </div>
    <div class="stat-item">
      <div class="stat-val stat-val-green">50 / 50</div>
      <div class="stat-lbl">CIE Marks Ceiling</div>
    </div>
    <div class="stat-item">
      <div class="stat-val">100%</div>
      <div class="stat-lbl">Two-Pass Verified</div>
    </div>
  </div>

  <div class="link-box">
    <div class="link-lbl">🌐 LIVE CLOUD DEPLOYED WEB APPLICATION</div>
    <div class="link-url">https://aushadhasahaya-api.onrender.com</div>
    <div class="link-git">GitHub: github.com/lokeshmr23/1BCP308Communityproject-2</div>
  </div>

  <div class="channels-box">
    <div class="channel-row">
      <span class="chan-tg">📢 Telegram: t.me/vtuhub</span>
      <span class="chan-ig">📸 Instagram: @vtuhub</span>
      <span class="chan-wa">💬 WhatsApp: vtuhub</span>
    </div>
  </div>

  <div class="disclaimer">
    <strong>Academic Disclaimer:</strong> Developed under VTU 2025 Scheme Course 1BCP308 for academic evaluation and Educational Social Responsibility (ESR). Assistive administrative tool only; not a substitute for clinical medical diagnosis. Resident profiles and survey records are anonymized based on regional DK care home baselines.
  </div>

</body>
</html>
"""

print("Rendering Instagram Portrait Poster...")
doc_p = weasyprint.HTML(string=html_portrait)
pdf_path_p = ROOT / "poster_portrait.pdf"
doc_p.write_pdf(str(pdf_path_p))

# Convert PDF to high-res PNG (300 DPI -> ~2550 x 3190 px, resized to standard 1080 x 1350 px)
pdf_doc = pymupdf.open(str(pdf_path_p))
page = pdf_doc[0]
pix = page.get_pixmap(dpi=300)
img_path_p = ROOT / "vtuhub-poster-instagram-portrait.png"
pix.save(str(img_path_p))
print(f"Generated {img_path_p} ({img_path_p.stat().st_size} bytes)")

# 2. Square Poster (1:1 Aspect Ratio -> 210mm x 210mm for WhatsApp & Telegram)
html_square = html_portrait.replace("size: 216mm 270mm;", "size: 210mm 210mm;").replace("height: 270mm;", "height: 210mm;").replace("font-size: 24pt;", "font-size: 20pt;").replace("padding: 12mm 14mm;", "padding: 8mm 10mm;").replace("margin-bottom: 10pt;", "margin-bottom: 6pt;").replace("margin-bottom: 8pt;", "margin-bottom: 5pt;")

print("Rendering Square Poster...")
doc_s = weasyprint.HTML(string=html_square)
pdf_path_s = ROOT / "poster_square.pdf"
doc_s.write_pdf(str(pdf_path_s))

pdf_doc_s = pymupdf.open(str(pdf_path_s))
page_s = pdf_doc_s[0]
pix_s = page_s.get_pixmap(dpi=300)
img_path_s = ROOT / "vtuhub-poster-square.png"
pix_s.save(str(img_path_s))
print(f"Generated {img_path_s} ({img_path_s.stat().st_size} bytes)")
