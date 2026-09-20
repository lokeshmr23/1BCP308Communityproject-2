/**
 * Dakshina Kannada District Interactive Geospatial Map Engine
 * Renders SVG map of Dakshina Kannada with coastal Mangaluru HQ,
 * taluk boundary paths, Nethravathi & Gurupura river lines,
 * and interactive facility markers for senior old-age homes.
 */

const DK_MAP_CONFIG = {
  viewBox: "0 0 800 700",
  center: { lat: 12.87, lng: 75.05 },
  scale: {
    minLat: 12.50,
    maxLat: 13.18,
    minLng: 74.78,
    maxLng: 75.52
  }
};

function latLngToSvg(lat, lng) {
  // Map geographical lat/lng to SVG canvas coords
  // Latitude goes North (+) -> y decreases
  // Longitude goes East (+) -> x increases
  const { minLat, maxLat, minLng, maxLng } = DK_MAP_CONFIG.scale;
  const x = ((lng - minLng) / (maxLng - minLng)) * 700 + 50;
  const y = ((maxLat - lat) / (maxLat - minLat)) * 580 + 60;
  return { x: Math.round(x), y: Math.round(y) };
}

function renderDakshinaKannadaMap(containerId, facilities, onSelectFacility) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let svg = `
    <svg viewBox="${DK_MAP_CONFIG.viewBox}" class="dk-district-svg" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="arabianSeaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#e0f2fe"/>
          <stop offset="100%" stop-color="#bae6fd"/>
        </linearGradient>
        <linearGradient id="districtBg" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#f8fafc"/>
          <stop offset="100%" stop-color="#f1f5f9"/>
        </linearGradient>
        <filter id="pinShadow" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="1" dy="2" stdDeviation="2" flood-opacity="0.3"/>
        </filter>
      </defs>

      <!-- Arabian Sea (West Coast) -->
      <path d="M 0,0 L 140,0 Q 120,200 135,380 Q 110,500 125,700 L 0,700 Z" fill="url(#arabianSeaGrad)" opacity="0.6"/>
      <text x="35" y="340" transform="rotate(-90 35,340)" class="map-sea-label">ARABIAN SEA (ಅರಬ್ಬೀ ಸಮುದ್ರ)</text>

      <!-- District Outer Boundary -->
      <polygon points="
        140,40 280,30 420,50 560,90 730,160 760,260 780,420 740,580 650,680 480,670 320,620 180,560 125,480 135,340 120,180
      " fill="url(#districtBg)" stroke="#94a3b8" stroke-width="2.5" stroke-dasharray="none"/>

      <!-- Taluk Boundaries & Regions -->
      <!-- 1. Mangaluru Taluk (Coastal West & Urban HQ) -->
      <path d="M 140,40 L 260,35 L 290,160 L 240,300 L 135,340 L 120,180 Z" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="1.5" class="taluk-poly" data-taluk="Mangaluru"/>
      <text x="180" y="160" class="taluk-title">MANGALURU</text>
      <text x="180" y="175" class="taluk-subtitle">(ಮಂಗಳೂರು HQ)</text>

      <!-- 2. Moodbidri Taluk (North) -->
      <path d="M 260,35 L 420,50 L 460,180 L 290,160 Z" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.5" class="taluk-poly" data-taluk="Moodbidri"/>
      <text x="340" y="110" class="taluk-title">MOODBIDRI</text>
      <text x="340" y="125" class="taluk-subtitle">(ಮೂಡುಬಿದಿರೆ)</text>

      <!-- 3. Belthangady Taluk (North-East Foothills) -->
      <path d="M 420,50 L 560,90 L 730,160 L 680,310 L 490,260 L 460,180 Z" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="1.5" class="taluk-poly" data-taluk="Belthangady"/>
      <text x="560" y="190" class="taluk-title">BELTHANGADY</text>
      <text x="560" y="205" class="taluk-subtitle">(ಬೆಳ್ತಂಗಡಿ - Ujire)</text>

      <!-- 4. Bantwal Taluk (Central Corridor) -->
      <path d="M 290,160 L 460,180 L 490,260 L 430,380 L 280,350 L 240,300 Z" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" class="taluk-poly" data-taluk="Bantwal"/>
      <text x="330" y="270" class="taluk-title">BANTWAL</text>
      <text x="330" y="285" class="taluk-subtitle">(ಬಂಟ್ವಾಳ B.C. Road)</text>

      <!-- 5. Puttur Taluk (South Central) -->
      <path d="M 280,350 L 430,380 L 520,370 L 540,510 L 370,530 L 280,450 Z" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="1.5" class="taluk-poly" data-taluk="Puttur"/>
      <text x="400" y="440" class="taluk-title">PUTTUR</text>
      <text x="400" y="455" class="taluk-subtitle">(ಪುತ್ತೂರು)</text>

      <!-- 6. Kadaba Taluk (South East Foothills) -->
      <path d="M 520,370 L 680,310 L 750,420 L 650,510 L 540,510 Z" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.5" class="taluk-poly" data-taluk="Kadaba"/>
      <text x="600" y="420" class="taluk-title">KADABA</text>
      <text x="600" y="435" class="taluk-subtitle">(ಕಡಬ)</text>

      <!-- 7. Sullia Taluk (Far South East) -->
      <path d="M 370,530 L 540,510 L 650,510 L 740,580 L 650,680 L 480,670 L 320,620 Z" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="1.5" class="taluk-poly" data-taluk="Sullia"/>
      <text x="510" y="590" class="taluk-title">SULLIA</text>
      <text x="510" y="605" class="taluk-subtitle">(ಸುಳ್ಯ)</text>

      <!-- River Paths: Nethravathi & Phalguni / Gurupura -->
      <!-- Gurupura River -->
      <path d="M 330,120 Q 240,140 160,220" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4,2"/>
      <text x="210" y="140" class="river-label">Phalguni / Gurupura R.</text>
      <!-- Nethravathi River flowing through Belthangady, Bantwal to Mangaluru Estuary -->
      <path d="M 640,240 Q 480,280 340,310 Q 240,310 150,335" fill="none" stroke="#0284c7" stroke-width="3" stroke-linecap="round"/>
      <text x="360" y="325" class="river-label">Nethravathi River (ನೇತ್ರಾವತಿ ನದಿ)</text>

      <!-- Mangaluru Port / Urban Indicator -->
      <circle cx="150" cy="310" r="7" fill="#0369a1" stroke="#ffffff" stroke-width="2"/>
      <text x="162" y="315" class="city-hq-label">MANGALURU CITY (ಮುಖ್ಯ ಕಛೇರಿ)</text>

      <!-- Facility Markers Layer -->
      <g id="facilityMarkers">
  `;

  // Plot each old-age home
  facilities.forEach((fac, idx) => {
    const pt = latLngToSvg(fac.lat, fac.lng);
    const color = fac.taluk === "Mangaluru" ? "#0284c7" : "#0d9488";
    
    svg += `
      <g class="map-pin-group" data-id="${fac.id}" transform="translate(${pt.x}, ${pt.y})" style="cursor: pointer;" onclick="window.onMapPinClick('${fac.id}')">
        <!-- Pulse ring -->
        <circle cx="0" cy="0" r="16" fill="${color}" opacity="0.2" class="pin-pulse"/>
        <!-- Marker pin -->
        <circle cx="0" cy="0" r="11" fill="${color}" stroke="#ffffff" stroke-width="2.5" filter="url(#pinShadow)"/>
        <text x="0" y="4" text-anchor="middle" fill="#ffffff" font-size="9" font-weight="bold">${idx + 1}</text>
        <!-- Label tooltip card -->
        <g class="pin-tooltip">
          <rect x="-85" y="-38" width="170" height="26" rx="5" fill="#1e293b" opacity="0.95"/>
          <text x="0" y="-21" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="600">${fac.name.split("(")[0].trim()}</text>
        </g>
      </g>
    `;
  });

  svg += `
      </g>
      <!-- Map Legend -->
      <g transform="translate(40, 600)" class="map-legend">
        <rect x="0" y="0" width="220" height="75" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" opacity="0.95"/>
        <text x="10" y="18" font-size="11" font-weight="bold" fill="#0f172a">Dakshina Kannada Eldercare Map</text>
        <circle cx="18" cy="36" r="6" fill="#0284c7"/>
        <text x="32" y="40" font-size="10" fill="#334155">Mangaluru Taluk Homes (4)</text>
        <circle cx="18" cy="56" r="6" fill="#0d9488"/>
        <text x="32" y="60" font-size="10" fill="#334155">Other Taluk Homes (Bantwal, Puttur, etc.)</text>
      </g>
    </svg>
  `;

  container.innerHTML = svg;

  window.onMapPinClick = function(facId) {
    if (onSelectFacility) onSelectFacility(facId);
  };
}
