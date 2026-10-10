"""Build assets/idcard.svg — a developer ID card with the embedded profile photo."""
import base64, os

PHOTO = "assets/profile.jpg"
OUT = "assets/idcard.svg"

with open(PHOTO, "rb") as f:
    b64 = base64.b64encode(f.read()).decode()
data_uri = f"data:image/jpeg;base64,{b64}"

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="420" height="560" viewBox="0 0 420 560" role="img" aria-label="Developer ID card">
  <defs>
    <linearGradient id="card" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#042a3a"/>
      <stop offset="1" stop-color="#001018"/>
    </linearGradient>
    <linearGradient id="acc" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#FF4103"/>
      <stop offset="1" stop-color="#ff8a5c"/>
    </linearGradient>
    <clipPath id="pfp"><circle cx="210" cy="238" r="78"/></clipPath>
    <style>
      .mono {{ font-family:'Consolas','SF Mono',monospace; }}
      .sans {{ font-family:'Segoe UI',Arial,sans-serif; }}
    </style>
  </defs>

  <!-- lanyard -->
  <rect x="196" y="0" width="28" height="70" fill="url(#acc)"/>
  <rect x="188" y="64" width="44" height="16" rx="4" fill="#0d4255"/>
  <circle cx="210" cy="86" r="7" fill="#8aa4b0"/>

  <!-- card body -->
  <rect x="40" y="92" width="340" height="440" rx="26" fill="url(#card)" stroke="#0d4255" stroke-width="2"/>
  <rect x="40" y="92" width="340" height="60" rx="26" fill="#FF4103" fill-opacity="0.12"/>
  <text x="64" y="129" class="mono" font-size="14" fill="#ff8a5c">DEVELOPER ID</text>
  <text x="356" y="129" text-anchor="end" class="mono" font-size="14" fill="#8aa4b0">#DE-01</text>

  <!-- photo -->
  <circle cx="210" cy="238" r="84" fill="none" stroke="url(#acc)" stroke-width="4"/>
  <image href="{data_uri}" x="132" y="160" width="156" height="156" clip-path="url(#pfp)" preserveAspectRatio="xMidYMid slice"/>

  <!-- name + role -->
  <text x="210" y="352" text-anchor="middle" class="sans" font-size="26" font-weight="800" fill="#eaf2f5">Ashish Kumar Rajpoot</text>
  <text x="210" y="380" text-anchor="middle" class="mono" font-size="15" fill="#FF4103">DATA ENGINEER</text>

  <!-- details -->
  <line x1="72" y1="406" x2="348" y2="406" stroke="#0d4255" stroke-width="1.5"/>
  <text x="72" y="438" class="mono" font-size="13" fill="#8aa4b0">BASE</text>
  <text x="348" y="438" text-anchor="end" class="sans" font-size="14" fill="#eaf2f5">Delhi &amp; Noida, IN</text>
  <text x="72" y="470" class="mono" font-size="13" fill="#8aa4b0">FOCUS</text>
  <text x="348" y="470" text-anchor="end" class="sans" font-size="14" fill="#eaf2f5">Pipelines &amp; Agentic AI</text>
  <text x="72" y="502" class="mono" font-size="13" fill="#8aa4b0">SINCE</text>
  <text x="348" y="502" text-anchor="end" class="sans" font-size="14" fill="#eaf2f5">2023</text>
</svg>'''

os.makedirs("assets", exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print("Wrote", OUT, os.path.getsize(OUT), "bytes")
