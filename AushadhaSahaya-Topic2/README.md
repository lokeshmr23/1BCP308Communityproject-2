# AushadhaSahaya | ಔಷಧ ಸಹಾಯ
### Medication Management System for Old-Age Homes in Dakshina Kannada District
**VTU 2025 Scheme · 1BCP308 Community Project / Societal Project (Topic 2)**

Web-based application designed to monitor the administration of medicine to senior citizens residing at old-age homes across Dakshina Kannada district, Karnataka, India (headquarters in coastal Mangaluru).

---

## 🌟 Key Features

1. **Daily Medication Administration Record (MAR):** 4 daily time-slots (Morning, Noon, Evening, Night) with one-touch logging (`Administered`, `Delayed`, `Missed`, `Refused`), caregiver accountability, and patient safety checks.
2. **Interactive Dakshina Kannada District Map:** Scalable vector map displaying all taluks (Mangaluru Coastal HQ, Bantwal, Moodbidri, Belthangady, Puttur, Kadaba, Sullia) with clickable facility pins, active resident census, and adherence telemetry.
3. **Secondary Open-Source Datasets Integration:**
   - **OpenFDA & NIH RxNorm:** 10 high-risk geriatric Drug-Drug Interaction (DDI) pairs.
   - **AGS Beers Criteria 2023:** 6 high-risk geriatric medication classes (e.g. long-acting benzodiazepines, NSAIDs, TCAs).
   - **WHO Essential Medicines for Older Adults:** Core formulary guidance.
   - **Karnataka Directorate of Senior Citizens:** Official registry of 8 licensed care facilities in Dakshina Kannada.
4. **Offline-First Zero-Leak Architecture:** Fully self-contained client-side bundle (<115 KB) with `LocalStorage` state caching; runs continuously during coastal monsoon power/broadband blackouts.
5. **Predictive Refill & Dispensary Inventory:** Automatic warnings when pill stock drops below safe threshold.
6. **Reproducible Machine Evidence:** 15 Teaching-Learning Process (TLP) week programs with two-pass byte-identical capture verification.

---

## 🚀 Deployment & Local Execution

### Local Python Server:
```bash
python3 server.py
# Server starts at http://localhost:8080 (or port set via PORT env)
```

### Render Deployment:
1. Push repository to GitHub or GitLab.
2. In Render, select **New + → Blueprint** and select `render.yaml`, or **New + → Static Site** pointing to publish directory `./web`.
3. Set build command to `./render-build.sh`.
4. Deploy with free tier and automatic zero-spin-down static CDN hosting.
