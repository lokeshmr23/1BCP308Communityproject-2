import weasyprint
import pymupdf
from pathlib import Path

ROOT = Path("/home/user/project")

# Inline SVGs for crisp rendering without system emoji glitches
SVG_PIN = '''<svg style="vertical-align: middle; margin-right: 3px;" width="13" height="13" viewBox="0 0 24 24" fill="#38bdf8"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 0 1 0-5 2.5 2.5 0 0 1 0 5z"/></svg>'''
SVG_GLOBE = '''<svg style="vertical-align: middle; margin-right: 4px;" width="14" height="14" viewBox="0 0 24 24" fill="#fef08a"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1a2 2 0 0 0 2 2v1.93zm6.9-2.54A8 8 0 0 0 20 12c0-.7-.09-1.38-.26-2.03l-4.74 4.74A2 2 0 0 0 14 16v2a1 1 0 0 0 1 1c1.07 0 2.06-.52 2.9-1.61zM18 10V9a2 2 0 0 0-2-2h-3V5a1 1 0 0 0-1-1 8 8 0 0 0-4.63 1.47l4.08 4.08A2 2 0 0 1 12 11h4a2 2 0 0 0 2-1z"/></svg>'''
SVG_TG = '''<svg style="vertical-align: middle; margin-right: 4px;" width="15" height="15" viewBox="0 0 24 24" fill="#38bdf8"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69a.2.2 0 0 0-.05-.18c-.06-.05-.14-.03-.21-.02-.09.02-1.49.95-4.22 2.79-.4.27-.76.41-1.08.4-.36-.01-1.04-.2-1.55-.37-.63-.2-1.12-.31-1.08-.66.02-.18.27-.36.75-.55 2.92-1.27 4.86-2.11 5.83-2.51 2.78-1.16 3.35-1.36 3.73-1.36.08 0 .27.02.39.12.1.08.13.19.14.27-.01.06.01.24 0 .38z"/></svg>'''
SVG_IG = '''<svg style="vertical-align: middle; margin-right: 4px;" width="15" height="15" viewBox="0 0 24 24" fill="#f472b6"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/></svg>'''
SVG_WA = '''<svg style="vertical-align: middle; margin-right: 4px;" width="15" height="15" viewBox="0 0 24 24" fill="#4ade80"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2zm.01 1.67c4.54 0 8.24 3.7 8.24 8.24 0 2.2-.86 4.27-2.42 5.83a8.18 8.18 0 0 1-5.82 2.41c-1.42 0-2.82-.37-4.06-1.1l-.29-.17-3.02.79.81-2.95-.19-.3a8.18 8.18 0 0 1-1.25-4.51c0-4.54 3.7-8.24 8.24-8.24zm4.52 11.64c-.25-.12-1.47-.72-1.7-.81-.23-.08-.39-.12-.56.12-.17.25-.64.81-.79.97-.14.17-.29.19-.54.06-.25-.12-1.05-.39-2-1.23-.74-.66-1.24-1.47-1.39-1.72-.14-.25-.02-.38.11-.5.11-.11.25-.29.37-.43.12-.14.17-.25.25-.41.08-.17.04-.31-.02-.43s-.56-1.34-.76-1.84c-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.23.25-.87.85-.87 2.07 0 1.22.89 2.4 1.01 2.57.12.17 1.75 2.67 4.24 3.75.59.26 1.05.41 1.41.53.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.68-1.18.21-.58.21-1.07.15-1.18-.06-.11-.22-.17-.47-.29z"/></svg>'''
SVG_WARN = '''<svg style="vertical-align: middle; margin-right: 3px;" width="11" height="11" viewBox="0 0 24 24" fill="#f59e0b"><path d="M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z"/></svg>'''

# 1. Instagram Portrait Poster (4:5)
html_portrait = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@page {{
    size: 216mm 270mm;
    margin: 0;
}}
* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}
body {{
    font-family: 'DejaVu Sans', 'Gubbi', 'Lohit Kannada', sans-serif;
    background-color: #080f24;
    color: #ffffff;
    width: 216mm;
    height: 270mm;
    padding: 9mm 11mm;
}}
.header-box {{
    background: #0f1c3d;
    border: 2px solid #2563eb;
    border-radius: 5mm;
    padding: 3mm 5mm;
    margin-bottom: 3.5mm;
}}
.header-table {{
    width: 100%;
    border-collapse: collapse;
}}
.header-table td {{
    vertical-align: middle;
}}
.vtu-badge {{
    background: #f59e0b;
    color: #0b1120;
    font-size: 10pt;
    font-weight: 900;
    padding: 1.5mm 4.5mm;
    border-radius: 3.5mm;
    display: inline-block;
    letter-spacing: 0.04em;
}}
.scheme-text {{
    font-size: 10.5pt;
    font-weight: 800;
    color: #93c5fd;
    padding-left: 3mm;
}}
.hub-badge {{
    background: #2563eb;
    color: #ffffff;
    font-size: 13pt;
    font-weight: 900;
    padding: 1.5mm 6mm;
    border-radius: 4mm;
    letter-spacing: 0.05em;
    float: right;
}}
.hero-card {{
    background: linear-gradient(180deg, #101f42 0%, #0d1730 100%);
    border: 2px solid #1e3a8a;
    border-radius: 5mm;
    padding: 4mm 5mm;
    text-align: center;
    margin-bottom: 3.5mm;
}}
.hero-tagline {{
    font-size: 10pt;
    font-weight: 800;
    color: #38bdf8;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 1.5mm;
}}
.hero-title {{
    font-size: 27pt;
    font-weight: 900;
    color: #ffffff;
    line-height: 1.15;
    margin-bottom: 1.5mm;
}}
.kannada-txt {{
    font-family: 'Gubbi', 'Lohit Kannada', sans-serif;
    color: #fbbf24;
    font-weight: bold;
}}
.hero-sub {{
    font-size: 12.5pt;
    font-weight: 700;
    color: #f1f5f9;
    line-height: 1.35;
    margin-bottom: 2mm;
}}
.geo-pill {{
    display: inline-block;
    background: #192a4d;
    border: 1.5px solid #38bdf8;
    color: #38bdf8;
    font-size: 9.5pt;
    font-weight: 800;
    padding: 1.2mm 4.5mm;
    border-radius: 3.5mm;
}}
.author-box {{
    background: #111e3b;
    border: 1.5px solid #2563eb;
    border-left: 5.5mm solid #f59e0b;
    border-radius: 3.5mm;
    padding: 2.5mm 4.5mm;
    margin-bottom: 3.5mm;
}}
.author-table {{
    width: 100%;
    border-collapse: collapse;
}}
.author-table td {{
    vertical-align: middle;
}}
.author-name {{
    font-size: 12pt;
    font-weight: 900;
    color: #ffffff;
}}
.author-dept {{
    font-size: 9.5pt;
    font-weight: 600;
    color: #93c5fd;
    margin-top: 0.5mm;
}}
.author-role {{
    background: #f59e0b;
    color: #0b1120;
    font-size: 8.5pt;
    font-weight: 900;
    padding: 1.2mm 3.5mm;
    border-radius: 2.5mm;
    text-transform: uppercase;
    float: right;
}}
.metrics-table {{
    width: 100%;
    border-collapse: separate;
    border-spacing: 2.5mm 0;
    margin-bottom: 3.5mm;
}}
.metric-cell {{
    width: 25%;
    background: #0d1935;
    border: 2px solid #1d4ed8;
    border-radius: 4mm;
    padding: 2.5mm 1mm;
    text-align: center;
}}
.metric-cell.green {{
    border-color: #10b981;
    background: #092323;
}}
.metric-cell.gold {{
    border-color: #f59e0b;
    background: #251d0d;
}}
.metric-val {{
    font-size: 21pt;
    font-weight: 900;
    line-height: 1;
    margin-bottom: 1.5mm;
}}
.col-green {{ color: #34d399; }}
.col-blue {{ color: #38bdf8; }}
.col-gold {{ color: #fbbf24; }}
.metric-tag {{
    font-size: 8.5pt;
    font-weight: 800;
    color: #ffffff;
    text-transform: uppercase;
    letter-spacing: 0.02em;
}}
.features-table {{
    width: 100%;
    border-collapse: separate;
    border-spacing: 2.5mm 2.5mm;
    margin-bottom: 3.5mm;
}}
.feature-cell {{
    width: 50%;
    background: #0f1c3a;
    border: 1.5px solid #2563eb;
    border-radius: 4mm;
    padding: 3mm 4mm;
    vertical-align: top;
}}
.feat-h {{
    font-size: 10.5pt;
    font-weight: 800;
    color: #38bdf8;
    margin-bottom: 1.2mm;
}}
.feat-p {{
    font-size: 9pt;
    font-weight: 600;
    color: #ffffff;
    line-height: 1.35;
}}
.feat-p span {{
    color: #fbbf24;
    font-weight: 700;
}}
.url-box {{
    background: #0284c7;
    border: 2px solid #7dd3fc;
    border-radius: 4.5mm;
    padding: 3mm 4mm;
    text-align: center;
    margin-bottom: 3mm;
}}
.url-top {{
    font-size: 9.5pt;
    font-weight: 900;
    color: #fef08a;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 1.2mm;
}}
.url-addr {{
    font-family: 'DejaVu Sans Mono', Consolas, monospace;
    font-size: 13pt;
    font-weight: 900;
    color: #ffffff;
    background: #034c7b;
    padding: 1.2mm 4mm;
    border-radius: 3mm;
    display: inline-block;
    letter-spacing: 0.03em;
}}
.repo-txt {{
    font-size: 9.2pt;
    font-weight: 700;
    color: #ffffff;
    margin-top: 1.2mm;
}}
.repo-txt span {{
    color: #fef08a;
}}
.social-box {{
    background: #0e172e;
    border: 1.5px solid #334155;
    border-radius: 4mm;
    padding: 2.5mm 4mm;
    margin-bottom: 2.5mm;
}}
.social-table {{
    width: 100%;
    border-collapse: collapse;
    text-align: center;
}}
.social-table td {{
    font-size: 9.5pt;
    font-weight: 800;
}}
.tg-col {{ color: #38bdf8; }}
.ig-col {{ color: #f472b6; }}
.wa-col {{ color: #4ade80; }}
.disclaimer-box {{
    font-size: 6.8pt;
    color: #94a3b8;
    line-height: 1.35;
    text-align: center;
    border-top: 1px solid #1e293b;
    padding-top: 2mm;
}}
.disclaimer-box span {{
    color: #f59e0b;
    font-weight: 800;
}}
</style>
</head>
<body>

  <!-- HEADER -->
  <div class="header-box">
    <table class="header-table">
      <tr>
        <td style="width: 75%;">
          <span class="vtu-badge">VTU 2025 SCHEME</span>
          <span class="scheme-text">1BCP308 COMMUNITY PROJECT · TOPIC 2</span>
        </td>
        <td style="width: 25%; text-align: right;">
          <span class="hub-badge">vtuhub</span>
        </td>
      </tr>
    </table>
  </div>

  <!-- TITLE -->
  <div class="hero-card">
    <div class="hero-tagline">Complete Classroom Manual · Deployed Web App · Secondary Datasets</div>
    <h1 class="hero-title">AushadhaSahaya <span class="kannada-txt">| ಔಷಧ ಸಹಾಯ</span></h1>
    <div class="hero-sub">Medication Management & Safety Monitor for Senior Citizens in Old-Age Homes</div>
    <div class="geo-pill">{SVG_PIN} Dakshina Kannada District Study · Mangaluru Regional Care Homes</div>
  </div>

  <!-- AUTHOR -->
  <div class="author-box">
    <table class="author-table">
      <tr>
        <td style="width: 75%;">
          <div class="author-name">Dr. Lokesh M R</div>
          <div class="author-dept">Professor, Dept. of Information Science & Engineering, AJIET Mangaluru</div>
        </td>
        <td style="width: 25%; text-align: right;">
          <span class="author-role">Project Mentor</span>
        </td>
      </tr>
    </table>
  </div>

  <!-- 4 STATS ROW -->
  <table class="metrics-table">
    <tr>
      <td class="metric-cell green">
        <div class="metric-val col-green">97.8%</div>
        <div class="metric-tag">Adherence Rate</div>
      </td>
      <td class="metric-cell">
        <div class="metric-val col-blue">71.1%</div>
        <div class="metric-tag">Time Saved</div>
      </td>
      <td class="metric-cell gold">
        <div class="metric-val col-gold">50 / 50</div>
        <div class="metric-tag">CIE Ceiling</div>
      </td>
      <td class="metric-cell green">
        <div class="metric-val col-green">100%</div>
        <div class="metric-tag">Reproducible</div>
      </td>
    </tr>
  </table>

  <!-- 2x2 FEATURES TABLE -->
  <table class="features-table">
    <tr>
      <td class="feature-cell">
        <div class="feat-h">1. Daily MAR Administration</div>
        <div class="feat-p">4 dosage windows (Morning, Noon, Evening, Night) with <span>Kannada cues</span> and 1-click status logging.</div>
      </td>
      <td class="feature-cell">
        <div class="feat-h">2. Clinical Safety Alert Engine</div>
        <div class="feat-p">Integrated <span>OpenFDA / RxNorm</span> high-risk interactions and <span>AGS Beers Criteria 2023</span> rules.</div>
      </td>
    </tr>
    <tr>
      <td class="feature-cell">
        <div class="feat-h">3. Dakshina Kannada Vector Map</div>
        <div class="feat-p">Interactive district SVG map tracking <span>8 care facilities</span> across Mangaluru, Bantwal & Puttur.</div>
      </td>
      <td class="feature-cell">
        <div class="feat-h">4. Complete 53-Page Manual & Slides</div>
        <div class="feat-p">15-Week TLP step-by-step chapters, verified outputs, <span>viva voce Q&A</span>, and 16-slide deck.</div>
      </td>
    </tr>
  </table>

  <!-- LIVE URL -->
  <div class="url-box">
    <div class="url-top">{SVG_GLOBE} Live Cloud Deployed Web Application</div>
    <div class="url-addr">https://aushadhasahaya-api.onrender.com</div>
    <div class="repo-txt">GitHub Repository: <span>github.com/lokeshmr23/1BCP308Communityproject-2</span></div>
  </div>

  <!-- SOCIAL CHANNELS -->
  <div class="social-box">
    <table class="social-table">
      <tr>
        <td class="tg-col">{SVG_TG} Telegram: <strong>t.me/vtuhub</strong></td>
        <td class="ig-col">{SVG_IG} Instagram: <strong>@vtuhub</strong></td>
        <td class="wa-col">{SVG_WA} WhatsApp: <strong>vtuhub</strong></td>
      </tr>
    </table>
  </div>

  <!-- DISCLAIMER -->
  <div class="disclaimer-box">
    <span>{SVG_WARN} Academic Notice:</span> Developed under VTU 2025 Scheme Course 1BCP308 for educational evaluation and Educational Social Responsibility (ESR). Assistive administrative tool; not a substitute for clinical medical diagnosis.
  </div>

</body>
</html>
"""

# 2. Square Poster (1:1)
html_square = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@page {{
    size: 210mm 210mm;
    margin: 0;
}}
* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}
body {{
    font-family: 'DejaVu Sans', 'Gubbi', 'Lohit Kannada', sans-serif;
    background-color: #080f24;
    color: #ffffff;
    width: 210mm;
    height: 210mm;
    padding: 6mm 8mm;
}}
.header-box {{
    background: #0f1c3d;
    border: 2px solid #2563eb;
    border-radius: 4mm;
    padding: 2mm 4mm;
    margin-bottom: 2.5mm;
}}
.header-table {{
    width: 100%;
    border-collapse: collapse;
}}
.header-table td {{
    vertical-align: middle;
}}
.vtu-badge {{
    background: #f59e0b;
    color: #0b1120;
    font-size: 8.5pt;
    font-weight: 900;
    padding: 1.2mm 3.5mm;
    border-radius: 3mm;
    display: inline-block;
}}
.scheme-text {{
    font-size: 9.5pt;
    font-weight: 800;
    color: #93c5fd;
    padding-left: 2.5mm;
}}
.hub-badge {{
    background: #2563eb;
    color: #ffffff;
    font-size: 11pt;
    font-weight: 900;
    padding: 1.2mm 5mm;
    border-radius: 3mm;
    float: right;
}}
.hero-card {{
    background: linear-gradient(180deg, #101f42 0%, #0d1730 100%);
    border: 1.5px solid #1e3a8a;
    border-radius: 4mm;
    padding: 2.5mm 4mm;
    text-align: center;
    margin-bottom: 2.5mm;
}}
.hero-tagline {{
    font-size: 8pt;
    font-weight: 800;
    color: #38bdf8;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 0.8mm;
}}
.hero-title {{
    font-size: 21pt;
    font-weight: 900;
    color: #ffffff;
    line-height: 1.15;
    margin-bottom: 1mm;
}}
.kannada-txt {{
    font-family: 'Gubbi', 'Lohit Kannada', sans-serif;
    color: #fbbf24;
    font-weight: bold;
}}
.hero-sub {{
    font-size: 10pt;
    font-weight: 700;
    color: #f1f5f9;
    line-height: 1.3;
    margin-bottom: 1.2mm;
}}
.geo-pill {{
    display: inline-block;
    background: #192a4d;
    border: 1px solid #38bdf8;
    color: #38bdf8;
    font-size: 8pt;
    font-weight: 800;
    padding: 0.8mm 3.5mm;
    border-radius: 2.5mm;
}}
.author-box {{
    background: #111e3b;
    border: 1.5px solid #2563eb;
    border-left: 4.5mm solid #f59e0b;
    border-radius: 3mm;
    padding: 1.8mm 3.5mm;
    margin-bottom: 2.5mm;
}}
.author-table {{
    width: 100%;
    border-collapse: collapse;
}}
.author-table td {{
    vertical-align: middle;
}}
.author-name {{
    font-size: 10.5pt;
    font-weight: 900;
    color: #ffffff;
}}
.author-dept {{
    font-size: 8.2pt;
    font-weight: 600;
    color: #93c5fd;
}}
.author-role {{
    background: #f59e0b;
    color: #0b1120;
    font-size: 7.5pt;
    font-weight: 900;
    padding: 1mm 3mm;
    border-radius: 2mm;
    text-transform: uppercase;
    float: right;
}}
.metrics-table {{
    width: 100%;
    border-collapse: separate;
    border-spacing: 2mm 0;
    margin-bottom: 2.5mm;
}}
.metric-cell {{
    width: 25%;
    background: #0d1935;
    border: 1.5px solid #1d4ed8;
    border-radius: 3mm;
    padding: 2mm 1mm;
    text-align: center;
}}
.metric-cell.green {{
    border-color: #10b981;
    background: #092323;
}}
.metric-cell.gold {{
    border-color: #f59e0b;
    background: #251d0d;
}}
.metric-val {{
    font-size: 16pt;
    font-weight: 900;
    line-height: 1;
    margin-bottom: 0.8mm;
}}
.col-green {{ color: #34d399; }}
.col-blue {{ color: #38bdf8; }}
.col-gold {{ color: #fbbf24; }}
.metric-tag {{
    font-size: 7.2pt;
    font-weight: 800;
    color: #ffffff;
    text-transform: uppercase;
}}
.features-table {{
    width: 100%;
    border-collapse: separate;
    border-spacing: 2mm 2mm;
    margin-bottom: 2.5mm;
}}
.feature-cell {{
    width: 50%;
    background: #0f1c3a;
    border: 1.5px solid #2563eb;
    border-radius: 3mm;
    padding: 2.2mm 3mm;
    vertical-align: top;
}}
.feat-h {{
    font-size: 8.8pt;
    font-weight: 800;
    color: #38bdf8;
    margin-bottom: 0.8mm;
}}
.feat-p {{
    font-size: 7.6pt;
    font-weight: 600;
    color: #ffffff;
    line-height: 1.3;
}}
.feat-p span {{
    color: #fbbf24;
    font-weight: 700;
}}
.url-box {{
    background: #0284c7;
    border: 2px solid #7dd3fc;
    border-radius: 3.5mm;
    padding: 2.2mm 3mm;
    text-align: center;
    margin-bottom: 2.2mm;
}}
.url-top {{
    font-size: 8pt;
    font-weight: 900;
    color: #fef08a;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 0.8mm;
}}
.url-addr {{
    font-family: 'DejaVu Sans Mono', Consolas, monospace;
    font-size: 11pt;
    font-weight: 900;
    color: #ffffff;
    background: #034c7b;
    padding: 1mm 3.5mm;
    border-radius: 2.5mm;
    display: inline-block;
    letter-spacing: 0.02em;
}}
.repo-txt {{
    font-size: 7.8pt;
    font-weight: 700;
    color: #ffffff;
    margin-top: 0.8mm;
}}
.repo-txt span {{
    color: #fef08a;
}}
.social-box {{
    background: #0e172e;
    border: 1.5px solid #334155;
    border-radius: 3mm;
    padding: 1.8mm 3mm;
    margin-bottom: 1.8mm;
}}
.social-table {{
    width: 100%;
    border-collapse: collapse;
    text-align: center;
}}
.social-table td {{
    font-size: 8.2pt;
    font-weight: 800;
}}
.tg-col {{ color: #38bdf8; }}
.ig-col {{ color: #f472b6; }}
.wa-col {{ color: #4ade80; }}
.disclaimer-box {{
    font-size: 6pt;
    color: #94a3b8;
    line-height: 1.3;
    text-align: center;
    border-top: 1px solid #1e293b;
    padding-top: 1.5mm;
}}
.disclaimer-box span {{
    color: #f59e0b;
    font-weight: 800;
}}
</style>
</head>
<body>

  <!-- HEADER -->
  <div class="header-box">
    <table class="header-table">
      <tr>
        <td style="width: 75%;">
          <span class="vtu-badge">VTU 2025 SCHEME</span>
          <span class="scheme-text">1BCP308 COMMUNITY PROJECT · TOPIC 2</span>
        </td>
        <td style="width: 25%; text-align: right;">
          <span class="hub-badge">vtuhub</span>
        </td>
      </tr>
    </table>
  </div>

  <!-- TITLE -->
  <div class="hero-card">
    <div class="hero-tagline">Complete Classroom Manual · Deployed Web App · Secondary Datasets</div>
    <h1 class="hero-title">AushadhaSahaya <span class="kannada-txt">| ಔಷಧ ಸಹಾಯ</span></h1>
    <div class="hero-sub">Medication Management & Safety Monitor for Senior Citizens in Old-Age Homes</div>
    <div class="geo-pill">{SVG_PIN} Dakshina Kannada District Study · Mangaluru Regional Care Homes</div>
  </div>

  <!-- AUTHOR -->
  <div class="author-box">
    <table class="author-table">
      <tr>
        <td style="width: 75%;">
          <div class="author-name">Dr. Lokesh M R</div>
          <div class="author-dept">Professor, Dept. of Information Science & Engineering, AJIET Mangaluru</div>
        </td>
        <td style="width: 25%; text-align: right;">
          <span class="author-role">Project Mentor</span>
        </td>
      </tr>
    </table>
  </div>

  <!-- 4 STATS ROW -->
  <table class="metrics-table">
    <tr>
      <td class="metric-cell green">
        <div class="metric-val col-green">97.8%</div>
        <div class="metric-tag">Adherence Rate</div>
      </td>
      <td class="metric-cell">
        <div class="metric-val col-blue">71.1%</div>
        <div class="metric-tag">Time Saved</div>
      </td>
      <td class="metric-cell gold">
        <div class="metric-val col-gold">50 / 50</div>
        <div class="metric-tag">CIE Ceiling</div>
      </td>
      <td class="metric-cell green">
        <div class="metric-val col-green">100%</div>
        <div class="metric-tag">Reproducible</div>
      </td>
    </tr>
  </table>

  <!-- 2x2 FEATURES TABLE -->
  <table class="features-table">
    <tr>
      <td class="feature-cell">
        <div class="feat-h">1. Daily MAR Administration</div>
        <div class="feat-p">4 dosage windows with <span>Kannada cues</span> & 1-click status logging.</div>
      </td>
      <td class="feature-cell">
        <div class="feat-h">2. Clinical Safety Alert Engine</div>
        <div class="feat-p">Integrated <span>OpenFDA / RxNorm</span> & <span>AGS Beers Criteria 2023</span>.</div>
      </td>
    </tr>
    <tr>
      <td class="feature-cell">
        <div class="feat-h">3. Dakshina Kannada Vector Map</div>
        <div class="feat-p">Interactive district SVG map tracking <span>8 care facilities</span>.</div>
      </td>
      <td class="feature-cell">
        <div class="feat-h">4. Complete 53-Page Book & Slides</div>
        <div class="feat-p">15-Week TLP step-by-step chapters, <span>viva voce Q&A</span>, and presentation deck.</div>
      </td>
    </tr>
  </table>

  <!-- LIVE URL -->
  <div class="url-box">
    <div class="url-top">{SVG_GLOBE} Live Cloud Deployed Web Application</div>
    <div class="url-addr">https://aushadhasahaya-api.onrender.com</div>
    <div class="repo-txt">GitHub: <span>github.com/lokeshmr23/1BCP308Communityproject-2</span></div>
  </div>

  <!-- SOCIAL CHANNELS -->
  <div class="social-box">
    <table class="social-table">
      <tr>
        <td class="tg-col">{SVG_TG} Telegram: <strong>t.me/vtuhub</strong></td>
        <td class="ig-col">{SVG_IG} Instagram: <strong>@vtuhub</strong></td>
        <td class="wa-col">{SVG_WA} WhatsApp: <strong>vtuhub</strong></td>
      </tr>
    </table>
  </div>

  <!-- DISCLAIMER -->
  <div class="disclaimer-box">
    <span>{SVG_WARN} Academic Notice:</span> VTU 2025 Scheme 1BCP308 Educational Social Responsibility (ESR) project. Assistive tool; not clinical diagnosis.
  </div>

</body>
</html>
"""

print("Rendering Instagram Portrait Poster (4:5)...")
doc_p = weasyprint.HTML(string=html_portrait)
pdf_path_p = ROOT / "poster_portrait_v4.pdf"
doc_p.write_pdf(str(pdf_path_p))
pdf_doc_p = pymupdf.open(str(pdf_path_p))
pix_p = pdf_doc_p[0].get_pixmap(dpi=300)
img_path_p = ROOT / "vtuhub-poster-instagram-portrait.png"
pix_p.save(str(img_path_p))
print("Saved portrait:", img_path_p)

print("Rendering Square Poster (1:1)...")
doc_s = weasyprint.HTML(string=html_square)
pdf_path_s = ROOT / "poster_square_v4.pdf"
doc_s.write_pdf(str(pdf_path_s))
pdf_doc_s = pymupdf.open(str(pdf_path_s))
pix_s = pdf_doc_s[0].get_pixmap(dpi=300)
img_path_s = ROOT / "vtuhub-poster-square.png"
pix_s.save(str(img_path_s))
print("Saved square:", img_path_s)
