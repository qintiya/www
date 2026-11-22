import json
import os
from pathlib import Path


def write_file(base_dir: Path, rel_path: str, content: str) -> None:
  target = base_dir / rel_path
  target.parent.mkdir(parents=True, exist_ok=True)
  target.write_text(content.strip() + "\n", encoding="utf-8")
  print(f"[OK] Generated: {rel_path}")


def main() -> None:
  root = Path("awdev_dist")
  root.mkdir(parents=True, exist_ok=True)

  # =========================================================================
  # 1. DATA MASTER (CATEGORIES, TOOLS, E-LEARNING, PARTNERS, 900 ARTICLES)
  # =========================================================================
  categories = [
      "HTML & CSS",
      "JavaScript",
      "Frontend",
      "Backend",
      "Source Code",
      "Code Snippet",
      "Web Tools",
      "Code Editor",
      "Generator",
      "Developer Tools",
      "Web Apps",
      "UI/UX Design",
      "Web Design",
      "Color Palette",
      "Icons & Fonts",
      "Visual Assets",
      "Video & Multimedia",
      "Open Source",
      "GitHub",
      "Cloud & Hosting",
      "Web Security",
      "SEO & Performance",
      "Tutorials",
      "E-Learning",
      "Tips & Tricks",
      "Documentation",
      "Resources",
      "Projects",
      "Tech News",
      "Community",
  ]

  dev_tools = [
      (
          "html-css-js-minifier",
          "HTML/CSS/JS Minifier",
          "Code & Minifier",
          "Compress HTML, CSS, and JS by removing unnecessary whitespace and"
          " comments.",
      ),
      (
          "code-beautifier",
          "Code Beautifier / Formatter",
          "Code & Minifier",
          "Format and indent HTML, CSS, JavaScript, and JSON cleanly.",
      ),
      (
          "live-code-editor",
          "Live HTML/CSS/JS Editor",
          "Code Editor",
          "Split-screen live code playground with instant preview and HTML"
          " export.",
      ),
      (
          "json-validator",
          "JSON Validator & Viewer",
          "Developer Tools",
          "Validate JSON syntax and inspect structured data in real time.",
      ),
      (
          "regex-tester",
          "Regex Tester",
          "Developer Tools",
          "Test regular expressions against sample text with flags and match"
          " highlights.",
      ),
      (
          "base64-codec",
          "Base64 Encoder / Decoder",
          "Text & Security",
          "Encode plain text to Base64 or decode Base64 back to readable"
          " text.",
      ),
      (
          "url-codec",
          "URL Encoder / Decoder",
          "Text & Security",
          "Encode or decode URL query parameters and special URI characters.",
      ),
      (
          "html-entity-codec",
          "HTML Entity Encoder / Decoder",
          "Text & Security",
          "Convert special characters to safe HTML entities and vice versa.",
      ),
      (
          "color-palette",
          "Color Picker & Palette Generator",
          "CSS Generators",
          "Pick HEX/RGB/HSL colors and generate harmonious color swatches.",
      ),
      (
          "css-gradient",
          "CSS Gradient Generator",
          "CSS Generators",
          "Create smooth linear and radial CSS gradients with live preview.",
      ),
      (
          "css-box-shadow",
          "CSS Box Shadow Generator",
          "CSS Generators",
          "Tune horizontal/vertical offset, blur, spread, and shadow color.",
      ),
      (
          "css-border-radius",
          "CSS Border Radius Generator",
          "CSS Generators",
          "Customize corner radii independently with live box preview.",
      ),
      (
          "glassmorphism-css",
          "Glassmorphism CSS Generator",
          "CSS Generators",
          "Generate frosted glass backdrop-filter styles and translucent"
          " layers.",
      ),
      (
          "css-layout-gen",
          "CSS Grid / Flexbox Generator",
          "CSS Generators",
          "Build responsive Grid and Flexbox layouts with copyable CSS.",
      ),
      (
          "favicon-gen",
          "Favicon Generator",
          "Generator",
          "Generate 16x16, 32x32, and 180x180 favicon icons via HTML5 Canvas.",
      ),
      (
          "meta-tag-gen",
          "Meta Tag Generator",
          "SEO & DNS",
          "Generate SEO meta tags, Open Graph tags, and Twitter Cards.",
      ),
      (
          "robots-txt-gen",
          "Robots.txt Generator",
          "SEO & DNS",
          "Configure search engine crawler rules and sitemap directives.",
      ),
      (
          "xml-sitemap-gen",
          "XML Sitemap Generator",
          "SEO & DNS",
          "Build a clean XML sitemap from a list of URLs and priorities.",
      ),
      (
          "utm-link-builder",
          "UTM Link Builder",
          "SEO & DNS",
          "Create campaign tracking URLs with utm_source, medium, and"
          " campaign.",
      ),
      (
          "parse-html-tool",
          "Parse HTML Tool",
          "Code & Minifier",
          "Escape HTML markup so it can be safely pasted into XML or blog"
          " templates.",
      ),
      (
          "word-char-counter",
          "Word & Character Counter",
          "Text & Security",
          "Count words, characters, sentences, paragraphs, and reading time.",
      ),
      (
          "case-converter",
          "Case Converter",
          "Text & Security",
          "Convert text to UPPERCASE, lowercase, Title Case, camelCase, or"
          " snake_case.",
      ),
      (
          "lorem-ipsum-gen",
          "Lorem Ipsum Generator",
          "Generator",
          "Generate placeholder paragraphs for UI wireframes and layout"
          " testing.",
      ),
      (
          "text-diff-checker",
          "Text Diff Checker",
          "Developer Tools",
          "Compare two text blocks line-by-line to spot additions and"
          " removals.",
      ),
      (
          "markdown-to-html",
          "Markdown to HTML Converter",
          "Code & Minifier",
          "Convert Markdown headings, lists, and code blocks into HTML.",
      ),
      (
          "qr-code-gen",
          "QR Code Generator",
          "Generator",
          "Generate scannable QR matrices on Canvas from text or URLs.",
      ),
      (
          "password-gen",
          "Strong Password Generator",
          "Text & Security",
          "Generate cryptographically strong passwords with custom length and"
          " symbols.",
      ),
      (
          "hash-gen",
          "Hash Generator (SHA-256 / SHA-1)",
          "Text & Security",
          "Compute cryptographic digests using the browser Web Crypto API.",
      ),
      (
          "image-compressor",
          "Image Compressor & Resizer",
          "Generator",
          "Resize dimensions and compress JPEG/WebP images locally via"
          " Canvas.",
      ),
      (
          "unix-timestamp",
          "Unix Timestamp Converter",
          "Developer Tools",
          "Convert Epoch timestamps to local/UTC dates and vice versa.",
      ),
      (
          "dns-web-checker",
          "DNS Web Checker",
          "SEO & DNS",
          "Query A, AAAA, MX, TXT, and NS records via Google Public DNS"
          " (`dns.google`).",
      ),
      (
          "maps-finder",
          "Maps Finder",
          "SEO & DNS",
          "Inspect coordinates, reverse geocoding, and interactive OpenStreetMap"
          " views.",
      ),
  ]

  islamic_tools = [
      (
          "digital-tasbih",
          "Digital Tasbih (Dhikr Counter)",
          "Worship & Prayer",
          "Interactive dhikr counter with 33/99/100 targets, sound/vibrate,"
          " and localStorage.",
      ),
      (
          "prayer-times",
          "Automatic Prayer Times",
          "Worship & Prayer",
          "Fetch daily Fajr, Dhuhr, Asr, Maghrib, and Isha times by city or"
          " GPS.",
      ),
      (
          "qibla-finder",
          "Qibla Direction Finder",
          "Islamic Maps & Finder",
          "Calculate Qibla bearing in degrees from your coordinates to the"
          " Ka'bah.",
      ),
      (
          "quran-reader",
          "Digital Al-Qur'an & Translation",
          "Al-Qur'an & Dua",
          "Read Surahs and search verses with Arabic text and translations.",
      ),
      (
          "quran-audio",
          "Al-Qur'an Audio Recitation (Murottal)",
          "Al-Qur'an & Dua",
          "Stream Surah recitations and control playback from the audio bar.",
      ),
      (
          "zakat-mal",
          "Zakat al-Mal Calculator",
          "Finance & Zakat",
          "Calculate 2.5% zakat on eligible savings, investments, and"
          " wealth above nisab.",
      ),
      (
          "zakat-fitr",
          "Zakat al-Fitr Calculator",
          "Finance & Zakat",
          "Calculate staple food or monetary Zakat al-Fitr by family"
          " members.",
      ),
      (
          "zakat-income",
          "Income / Professional Zakat Calculator",
          "Finance & Zakat",
          "Compute net income zakat based on salary, bonuses, and essential"
          " expenses.",
      ),
      (
          "zakat-gold-silver",
          "Gold & Silver Zakat Calculator",
          "Finance & Zakat",
          "Evaluate zakat obligations for held gold and silver grams.",
      ),
      (
          "faraidh-calc",
          "Islamic Inheritance Calculator (Faraidh)",
          "Finance & Zakat",
          "Educational Faraidh share estimator for spouses, children, and"
          " parents.",
      ),
      (
          "gregorian-hijri",
          "Gregorian to Hijri Date Converter",
          "Worship & Prayer",
          "Convert between Gregorian calendar dates and Hijri dates.",
      ),
      (
          "hijri-calendar",
          "Hijri Calendar & Islamic Holidays",
          "Worship & Prayer",
          "Browse Hijri months and key dates like Ramadan, Eid al-Fitr,"
          " and Eid al-Adha.",
      ),
      (
          "daily-duas",
          "Daily Duas & Morning/Evening Adhkar",
          "Al-Qur'an & Dua",
          "Curated morning and evening adhkar with Arabic, transliteration,"
          " and counters.",
      ),
      (
          "asmaul-husna",
          "Asmaul Husna (99 Names of Allah)",
          "Al-Qur'an & Dua",
          "Explore all 99 Names with Arabic script, transliteration, meaning,"
          " and flashcard quiz.",
      ),
      (
          "quran-search",
          "Al-Qur'an Verse & Keyword Search",
          "Al-Qur'an & Dua",
          "Filter verses and surahs quickly by keyword or topic.",
      ),
      (
          "hadith-search",
          "Hadith Search Engine",
          "Al-Qur'an & Dua",
          "Search curated authentic hadith collections by topic and"
          " narrator.",
      ),
      (
          "qadha-tracker",
          "Missed Prayer (Qadha) Tracker",
          "Worship & Prayer",
          "Track and log completed make-up prayers steadily.",
      ),
      (
          "fidyah-calc",
          "Missed Fasting & Fidyah Calculator",
          "Finance & Zakat",
          "Calculate missed Ramadan fasts and fidyah meals/amounts.",
      ),
      (
          "ramadan-imsakiyah",
          "Ramadan Imsakiyah Schedule",
          "Worship & Prayer",
          "View daily Imsak, Fajr, and Maghrib/Iftar schedule for your"
          " location.",
      ),
      (
          "ramadan-eid-countdown",
          "Ramadan & Eid Countdown",
          "Worship & Prayer",
          "Live countdown timer to upcoming Ramadan, Eid al-Fitr, and Eid"
          " al-Adha.",
      ),
      (
          "islamic-greeting-card",
          "Islamic Quote & Greeting Card Generator",
          "Al-Qur'an & Dua",
          "Design downloadable Eid and Islamic quote cards on Canvas.",
      ),
      (
          "arabic-keyboard",
          "Online Arabic Virtual Keyboard",
          "Al-Qur'an & Dua",
          "Type Arabic letters and harakat/tashkeel marks and copy easily.",
      ),
      (
          "latin-to-arabic",
          "Latin to Arabic Transliteration Tool",
          "Al-Qur'an & Dua",
          "Helper tool for transliterating phonetic Latin terms and"
          " greetings.",
      ),
      (
          "zakat-nisab-realtime",
          "Real-Time Zakat Nisab Calculator",
          "Finance & Zakat",
          "Check nisab threshold using live/custom gold price per gram.",
      ),
      (
          "hajj-umrah-guide",
          "Interactive Hajj & Umrah Guide",
          "Worship & Prayer",
          "Step-by-step guide to Ihram, Tawaf, Sa'i, and Talbiyah.",
      ),
      (
          "khatam-tracker",
          "Al-Qur'an Khatam Tracker",
          "Al-Qur'an & Dua",
          "Plan daily pages or juz to complete a full Al-Qur'an khatam.",
      ),
      (
          "mutabaah-tracker",
          "Daily Worship Tracker (Mutaba'ah Yaumiyah)",
          "Worship & Prayer",
          "Daily checklist for prayers, tilawah, sadaqah, and adhkar.",
      ),
      (
          "islamic-baby-names",
          "Islamic Baby Names Directory",
          "Al-Qur'an & Dua",
          "Browse boy and girl Islamic names with meanings and origins.",
      ),
      (
          "qurbani-calc",
          "Qurbani & Share Calculator",
          "Finance & Zakat",
          "Calculate 1/7th cattle/camel shares and meat distribution"
          " portions.",
      ),
      (
          "mosque-finder",
          "Nearby Mosque Locator",
          "Islamic Maps & Finder",
          "Find nearby mosques and Islamic centers using geolocation and"
          " map search.",
      ),
  ]

  elearning_sites = [
      ("freeCodeCamp", "https://freecodecamp.org"),
      ("W3Schools", "https://w3schools.com"),
      ("MDN Web Docs", "https://mozilla.org"),
      ("The Odin Project", "https://theodinproject.com"),
      ("Codecademy", "https://codecademy.com"),
      ("Coursera", "https://coursera.org"),
      ("edX", "https://edx.org"),
      ("Udemy", "https://udemy.com"),
      ("Khan Academy", "https://khanacademy.org"),
      ("CS50 Harvard", "https://harvard.edu"),
      ("LeetCode", "https://leetcode.com"),
      ("HackerRank", "https://hackerrank.com"),
      ("Exercism", "https://exercism.org"),
      ("SoloLearn", "https://sololearn.com"),
      ("Frontend Mentor", "https://frontendmentor.io"),
      ("CSS-Tricks", "https://css-tricks.com"),
      ("GeeksforGeeks", "https://geeksforgeeks.org"),
      ("Roadmap.sh", "https://roadmap.sh"),
      ("Scrimba", "https://scrimba.com"),
      ("Pluralsight", "https://pluralsight.com"),
  ]

  partners = [
      ("Product Hunt", "https://producthunt.com"),
      ("AlternativeTo", "https://alternativeto.net"),
      ("SaaSHub", "https://saashub.com"),
      ("Indie Hackers", "https://indiehackers.com"),
      ("BetaList", "https://betalist.com"),
      ("GitHub", "https://github.com"),
      ("DEV Community", "https://dev.to"),
      ("Hashnode", "https://hashnode.com"),
      ("CodePen", "https://codepen.io"),
      ("StackShare", "https://stackshare.io"),
      ("Petani Kode", "https://petanikode.com"),
      ("Dicoding", "https://dicoding.com"),
      ("CodePolitan", "https://codepolitan.com"),
      ("Kelas Terbuka", "https://youtube.com"),
      ("Niagahoster", "https://niagahoster.co.id"),
      ("DomaiNesia", "https://domainesia.com"),
      ("IDCloudHost", "https://idcloudhost.com"),
      ("DigitalOcean", "https://digitalocean.com"),
      ("Cloudflare", "https://cloudflare.com"),
      ("Quran.com", "https://quran.com"),
      ("Muslim Pro", "https://muslimpro.com"),
      ("Rumaysho", "https://rumaysho.com"),
      ("NU Online", "https://nu.or.id"),
      ("BAZNAS", "https://baznas.go.id"),
  ]

  # Generate 30 categories x 30 articles = 900 indexed entries
  articles_index = []
  article_id = 1
  for cat_idx, cat_name in enumerate(categories, start=1):
    cat_slug = (
        cat_name.lower()
        .replace("&", "and")
        .replace("/", "-")
        .replace(" ", "-")
    )
    for art_num in range(1, 31):
      slug = f"{cat_slug}-guide-{art_num:02d}"
      title = (
          f"{cat_name} Deep Dive #{art_num:02d}: Architecture, Best Practices"
          " & Production Patterns"
      )
      articles_index.append({
          "id": article_id,
          "slug": slug,
          "category": cat_name,
          "categorySlug": cat_slug,
          "title": title,
          "readingTime": f"{12 + (art_num % 8)} min read",
          "url": f"article.html?slug={slug}&cat={cat_slug}&num={art_num}",
      })
      article_id += 1

  # =========================================================================
  # 2. ROOT SEO & ADSENSE VERIFICATION FILES
  # =========================================================================
  write_file(
      root,
      "ads.txt",
      "google.com, pub-5407249785989200, DIRECT, f08c47fec0942fa0",
  )

  write_file(
      root,
      "robots.txt",
      """User-agent: *
Allow: /

Sitemap: https://awdev.eu.org/sitemap.xml""",
  )

  write_file(
      root,
      "googled2bd44ef72717048.html",
      "google-site-verification: googled2bd44ef72717048.html",
  )

  # =========================================================================
  # 3. STYLESHEET (style.css)
  # =========================================================================
  write_file(
      root,
      "assets/css/style.css",
      """/* AWDEV Design System - Light & Dark Mode + RTL Support */
:root {
  --bg-color: #f8fafc;
  --text-color: #0f172a;
  --muted-color: #475569;
  --card-bg: #ffffff;
  --border-color: #e2e8f0;
  --primary: #0ea5e9;
  --primary-dark: #0284c7;
  --accent: #10b981;
  --shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
  --radius: 14px;
}

[data-theme="dark"] {
  --bg-color: #0b1120;
  --text-color: #f1f5f9;
  --muted-color: #94a3b8;
  --card-bg: #111827;
  --border-color: #1e293b;
  --primary: #38bdf8;
  --primary-dark: #0ea5e9;
  --accent: #34d399;
  --shadow: 0 10px 28px rgba(0, 0, 0, 0.35);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background: var(--bg-color);
  color: var(--text-color);
  line-height: 1.65;
  transition: background-color 0.25s ease, color 0.25s ease;
  padding-bottom: 76px;
}

a { color: var(--primary); text-decoration: none; }
a:hover { text-decoration: underline; }
.container { max-width: 1240px; margin: 0 auto; padding: 0 1.25rem; }

/* AdSense Containers - Prevent CLS */
.ad-wrapper {
  margin: 1.5rem 0;
  padding: 0.75rem;
  background: var(--card-bg);
  border: 1px dashed var(--border-color);
  border-radius: var(--radius);
  min-height: 110px;
  text-align: center;
}
.ad-label {
  display: block;
  font-size: 0.7rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted-color);
  margin-bottom: 0.35rem;
}

/* Sticky Navbar */
.site-header {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: color-mix(in srgb, var(--card-bg) 92%, transparent);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border-color);
}
.nav-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  min-height: 68px;
  flex-wrap: wrap;
}
.brand {
  display: inline-flex;
  align-items: center;
  gap: 0.65rem;
  font-weight: 800;
  font-size: 1.2rem;
  color: var(--text-color);
  text-decoration: none;
}
.brand-avatar {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid var(--primary);
}
.nav-menu {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}
.nav-item { position: relative; }
.nav-btn, .nav-link {
  background: transparent;
  border: 1px solid transparent;
  color: var(--text-color);
  font-size: 0.9rem;
  font-weight: 600;
  padding: 0.45rem 0.7rem;
  border-radius: 8px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
}
.nav-btn:hover, .nav-link:hover { background: var(--bg-color); border-color: var(--border-color); text-decoration: none; }

.dropdown-panel {
  display: none;
  position: absolute;
  top: calc(100% + 6px);
  left: 0;
  min-width: 240px;
  max-height: 360px;
  overflow-y: auto;
  background: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  box-shadow: var(--shadow);
  padding: 0.5rem;
  z-index: 1200;
}
.nav-item.open .dropdown-panel { display: block; }
.dropdown-panel a, .dropdown-panel button {
  display: block;
  width: 100%;
  text-align: left;
  background: none;
  border: none;
  color: var(--text-color);
  padding: 0.45rem 0.65rem;
  border-radius: 8px;
  font-size: 0.86rem;
  cursor: pointer;
}
.dropdown-panel a:hover, .dropdown-panel button:hover { background: var(--bg-color); text-decoration: none; }

.nav-controls {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}
.search-input, .select-input, .input-field, .textarea-field {
  background: var(--bg-color);
  color: var(--text-color);
  border: 1px solid var(--border-color);
  border-radius: 9px;
  padding: 0.48rem 0.75rem;
  font-size: 0.9rem;
  font-family: inherit;
}
.textarea-field { width: 100%; min-height: 95px; resize: vertical; }
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
  padding: 0.5rem 0.95rem;
  border-radius: 9px;
  border: 1px solid var(--border-color);
  background: var(--card-bg);
  color: var(--text-color);
  font-weight: 600;
  font-size: 0.88rem;
  cursor: pointer;
  transition: transform 0.12s ease, background 0.2s ease;
}
.btn:hover { transform: translateY(-1px); text-decoration: none; }
.btn-primary { background: var(--primary); color: #fff; border-color: var(--primary); }
.btn-primary:hover { background: var(--primary-dark); }
.btn-accent { background: var(--accent); color: #052e16; border-color: var(--accent); }

/* Hero */
.hero {
  padding: 2.75rem 0 1.5rem;
}
.hero-box {
  background: linear-gradient(135deg, color-mix(in srgb, var(--primary) 12%, var(--card-bg)), var(--card-bg));
  border: 1px solid var(--border-color);
  border-radius: 20px;
  padding: 2rem;
  box-shadow: var(--shadow);
}
.hero h1 { font-size: clamp(1.75rem, 3.5vw, 2.65rem); line-height: 1.2; margin-bottom: 0.75rem; }
.hero p { color: var(--muted-color); max-width: 780px; margin-bottom: 1.25rem; }
.hero-actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 1.5rem; }
.stats-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 0.85rem; }
.stat-pill {
  background: var(--bg-color);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 0.75rem 1rem;
}
.stat-pill strong { display: block; font-size: 1.2rem; color: var(--primary); }
.stat-pill span { font-size: 0.82rem; color: var(--muted-color); }

/* Sections & Cards */
.section { padding: 2rem 0; }
.section-head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 1.1rem;
  flex-wrap: wrap;
}
.section-head h2 { font-size: 1.45rem; }
.section-head p { color: var(--muted-color); font-size: 0.92rem; }

.labels-bar {
  display: flex;
  gap: 0.45rem;
  overflow-x: auto;
  padding-bottom: 0.5rem;
  margin-bottom: 1.25rem;
}
.chip {
  white-space: nowrap;
  padding: 0.35rem 0.75rem;
  border-radius: 999px;
  border: 1px solid var(--border-color);
  background: var(--card-bg);
  color: var(--text-color);
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
}
.chip.active, .chip:hover { background: var(--primary); color: #fff; border-color: var(--primary); }

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(265px, 1fr));
  gap: 1rem;
}
.card {
  background: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  padding: 1.1rem;
  box-shadow: var(--shadow);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 0.75rem;
}
.card-tag {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--primary);
  background: color-mix(in srgb, var(--primary) 12%, transparent);
  padding: 0.2rem 0.55rem;
  border-radius: 6px;
  width: fit-content;
}
.card h3 { font-size: 1rem; }
.card p { font-size: 0.86rem; color: var(--muted-color); }
.card-actions { display: flex; gap: 0.5rem; flex-wrap: wrap; align-items: center; }

/* Interactive Lab / Sandbox */
.lab-panel {
  background: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: 18px;
  padding: 1.4rem;
  box-shadow: var(--shadow);
  margin-top: 1rem;
}
.lab-tabs { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1rem; }
.lab-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-top: 0.75rem; }
.output-box {
  background: var(--bg-color);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  padding: 0.85rem;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 0.85rem;
  white-space: pre-wrap;
  word-break: break-word;
}

/* Gallery */
.media-thumb {
  width: 100%;
  aspect-ratio: 16 / 10;
  object-fit: cover;
  border-radius: 10px;
  background: var(--bg-color);
  border: 1px solid var(--border-color);
}
.lightbox {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(2, 6, 23, 0.85);
  z-index: 2000;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
}
.lightbox.open { display: flex; }
.lightbox-inner {
  background: var(--card-bg);
  color: var(--text-color);
  border-radius: 16px;
  padding: 1.25rem;
  max-width: 720px;
  width: 100%;
  border: 1px solid var(--border-color);
}
.lightbox-inner img { width: 100%; max-height: 420px; object-fit: contain; border-radius: 10px; margin-bottom: 0.75rem; }

/* Floating Audio Bar */
.audio-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 1500;
  background: var(--card-bg);
  border-top: 1px solid var(--border-color);
  padding: 0.55rem 1rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  flex-wrap: wrap;
  box-shadow: 0 -6px 20px rgba(0, 0, 0, 0.08);
}
.audio-status { font-size: 0.84rem; font-weight: 600; }

/* Toast */
.toast {
  position: fixed;
  bottom: 78px;
  right: 18px;
  z-index: 2500;
  background: #0f172a;
  color: #fff;
  padding: 0.6rem 1rem;
  border-radius: 10px;
  font-size: 0.85rem;
  opacity: 0;
  transform: translateY(8px);
  transition: all 0.2s ease;
  pointer-events: none;
}
.toast.show { opacity: 1; transform: translateY(0); }

/* Footer */
.site-footer {
  background: var(--card-bg);
  border-top: 1px solid var(--border-color);
  padding: 2.25rem 0 1.5rem;
  margin-top: 2.5rem;
}
.footer-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}
.footer-grid h4 { font-size: 0.95rem; margin-bottom: 0.65rem; }
.footer-grid ul { list-style: none; display: grid; gap: 0.35rem; font-size: 0.86rem; }
.footer-bottom {
  border-top: 1px solid var(--border-color);
  padding-top: 1rem;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 0.75rem;
  font-size: 0.82rem;
  color: var(--muted-color);
}
""",
  )

  # =========================================================================
  # 4. DATA & ENGINES (tools-engine.js, islamic-engine.js, blog-data.js, app.js)
  # =========================================================================
  write_file(
      root,
      "assets/js/tools-engine.js",
      f"""window.AWDEV_DEV_TOOLS = {json.dumps([
          {
              "id": t[0],
              "name": t[1],
              "category": t[2],
              "description": t[3],
          }
          for t in dev_tools
      ], indent=2)};

window.AWDEV_ToolsEngine = {{
  countText(text) {{
    const trimmed = text.trim();
    const words = trimmed ? trimmed.split(/\\s+/).length : 0;
    const chars = text.length;
    const charsNoSpace = text.replace(/\\s/g, "").length;
    const sentences = trimmed ? (trimmed.match(/[^.!?]+[.!?]+/g) || [trimmed]).length : 0;
    const readingMin = Math.max(1, Math.ceil(words / 200));
    return {{ words, chars, charsNoSpace, sentences, readingMin }};
  }},

  generatePassword(length = 16, options = {{ upper: true, lower: true, numbers: true, symbols: true }}) {{
    let pool = "";
    if (options.upper) pool += "ABCDEFGHJKLMNPQRSTUVWXYZ";
    if (options.lower) pool += "abcdefghijkmnopqrstuvwxyz";
    if (options.numbers) pool += "23456789";
    if (options.symbols) pool += "!@#$%^&*-_=+?";
    if (!pool) pool = "abcdefghijkmnopqrstuvwxyz23456789";

    const array = new Uint32Array(length);
    crypto.getRandomValues(array);
    let out = "";
    for (let i = 0; i < length; i++) {{
      out += pool[array[i] % pool.length];
    }}
    return out;
  }},

  encodeBase64(str) {{
    const bytes = new TextEncoder().encode(str);
    let bin = "";
    bytes.forEach((b) => {{ bin += String.fromCharCode(b); }});
    return btoa(bin);
  }},

  decodeBase64(b64) {{
    const bin = atob(b64.trim());
    const bytes = new Uint8Array(bin.length);
    for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
    return new TextDecoder().decode(bytes);
  }},

  formatJSON(raw) {{
    const parsed = JSON.parse(raw);
    return JSON.stringify(parsed, null, 2);
  }},

  async sha256(message) {{
    const data = new TextEncoder().encode(message);
    const hashBuffer = await crypto.subtle.digest("SHA-256", data);
    return Array.from(new Uint8Array(hashBuffer))
      .map((b) => b.toString(16).padStart(2, "0"))
      .join("");
  }},

  async queryDNS(domain, type = "A") {{
    const clean = domain.replace(/^https?:\\/\\//, "").split("/")[0].trim();
    const res = await fetch(`https://dns.google/resolve?name=${{encodeURIComponent(clean)}}&type=${{encodeURIComponent(type)}}`);
    if (!res.ok) throw new Error("DNS query failed");
    return res.json();
  }}
}};
""",
  )

  write_file(
      root,
      "assets/js/islamic-engine.js",
      f"""window.AWDEV_ISLAMIC_TOOLS = {json.dumps([
          {
              "id": t[0],
              "name": t[1],
              "category": t[2],
              "description": t[3],
          }
          for t in islamic_tools
      ], indent=2)};

window.AWDEV_IslamicEngine = {{
  TASBIH_KEY: "awdev_tasbih_state_v1",

  getTasbihState() {{
    try {{
      const saved = JSON.parse(localStorage.getItem(this.TASBIH_KEY));
      if (saved && typeof saved.count === "number") return saved;
    }} catch (_) {{}}
    return {{ count: 0, target: 33, phrase: "SubhanAllah" }};
  }},

  saveTasbihState(state) {{
    localStorage.setItem(this.TASBIH_KEY, JSON.stringify(state));
  }},

  calculateZakatMal(wealthAmount, nisabAmount) {{
    const eligible = wealthAmount >= nisabAmount && wealthAmount > 0;
    const zakatDue = eligible ? Number((wealthAmount * 0.025).toFixed(2)) : 0;
    return {{ eligible, zakatDue, nisabAmount }};
  }},

  calculateQiblaBearing(lat, lng) {{
    // Ka'bah coordinates: 21.4225 N, 39.8262 E
    const kaabaLat = 21.4225 * (Math.PI / 180);
    const kaabaLng = 39.8262 * (Math.PI / 180);
    const phi1 = lat * (Math.PI / 180);
    const deltaLng = kaabaLng - lng * (Math.PI / 180);

    const y = Math.sin(deltaLng) * Math.cos(kaabaLat);
    const x =
      Math.cos(phi1) * Math.sin(kaabaLat) -
      Math.sin(phi1) * Math.cos(kaabaLat) * Math.cos(deltaLng);
    const bearing = ((Math.atan2(y, x) * 180) / Math.PI + 360) % 360;
    return Number(bearing.toFixed(2));
  }},

  async fetchPrayerTimes(city = "Semarang", country = "Indonesia") {{
    const url = `https://api.aladhan.com/v1/timingsByCity?city=${{encodeURIComponent(city)}}&country=${{encodeURIComponent(country)}}&method=20`;
    const res = await fetch(url);
    if (!res.ok) throw new Error("Prayer time lookup failed");
    const json = await res.json();
    return json.data;
  }}
}};
""",
  )

  write_file(
      root,
      "assets/js/blog-data.js",
      f"""window.AWDEV_CATEGORIES = {json.dumps(categories, indent=2)};
window.AWDEV_ELEARNING = {json.dumps([{"name": n, "url": u} for n, u in elearning_sites], indent=2)};
window.AWDEV_PARTNERS = {json.dumps([{"name": n, "url": u} for n, u in partners], indent=2)};
window.AWDEV_ARTICLES = {json.dumps(articles_index, indent=2)};
""",
  )

  write_file(
      root,
      "assets/js/app.js",
      """/* AWDEV Global UI, Multi-Language, Theme, Audio TTS, Galleries & Pages */
(function () {
  const I18N = {
    id: {
      heroTitle: "Developer Tools, Islamic Utilities & SEO Tech Knowledge Hub",
      heroSub: "Utilitas web gratis berbasis browser, kalkulator & panduan Islami, galeri media, serta arsip artikel teknis untuk awdev.eu.org.",
      ctaTools: "Jelajahi Tools",
      ctaBlog: "Baca Artikel SEO",
      searchPlaceholder: "Cari tools, kategori, atau artikel..."
    },
    en: {
      heroTitle: "Developer Tools, Islamic Utilities & SEO Tech Knowledge Hub",
      heroSub: "Free browser-based web utilities, Islamic calculators & guides, media galleries, and technical articles for awdev.eu.org.",
      ctaTools: "Explore Tools",
      ctaBlog: "Read SEO Articles",
      searchPlaceholder: "Search tools, categories, or articles..."
    },
    ar: {
      heroTitle: "أدوات المطورين والخدمات الإسلامية ومركز المعرفة التقنية",
      heroSub: "أدوات ويب مجانية وحاسبات إسلامية وموارد تقنية متكاملة لمنصة awdev.eu.org.",
      ctaTools: "استكشف الأدوات",
      ctaBlog: "تصفح المقالات",
      searchPlaceholder: "ابحث عن أداة أو تصنيف أو مقال..."
    }
  };

  function showToast(msg) {
    const el = document.getElementById("toast");
    if (!el) return;
    el.textContent = msg;
    el.classList.add("show");
    clearTimeout(window.__toastTimer);
    window.__toastTimer = setTimeout(() => el.classList.remove("show"), 2200);
  }
  window.AWDEV_toast = showToast;

  // Theme management
  const savedTheme = localStorage.getItem("awdev_theme") || "light";
  document.documentElement.setAttribute("data-theme", savedTheme);

  const themeBtn = document.getElementById("themeToggle");
  if (themeBtn) {
    themeBtn.addEventListener("click", () => {
      const next = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      localStorage.setItem("awdev_theme", next);
      showToast(`Theme: ${next.toUpperCase()}`);
    });
  }

  // Language & RTL switcher
  const langSelect = document.getElementById("langSelect");
  function applyLang(lang) {
    const dict = I18N[lang] || I18N.en;
    document.documentElement.lang = lang;
    document.documentElement.dir = lang === "ar" ? "rtl" : "ltr";
    const h1 = document.getElementById("heroTitle");
    const sub = document.getElementById("heroSubtitle");
    const search = document.getElementById("globalSearch");
    if (h1) h1.textContent = dict.heroTitle;
    if (sub) sub.textContent = dict.heroSub;
    if (search) search.placeholder = dict.searchPlaceholder;
    localStorage.setItem("awdev_lang", lang);
  }
  if (langSelect) {
    const savedLang = localStorage.getItem("awdev_lang") || "id";
    langSelect.value = savedLang;
    applyLang(savedLang);
    langSelect.addEventListener("change", (e) => applyLang(e.target.value));
  }

  // Dropdown menus
  document.querySelectorAll(".nav-btn[data-dropdown]").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      const parent = btn.closest(".nav-item");
      const wasOpen = parent.classList.contains("open");
      document.querySelectorAll(".nav-item.open").forEach((el) => el.classList.remove("open"));
      if (!wasOpen) parent.classList.add("open");
    });
  });
  document.addEventListener("click", () => {
    document.querySelectorAll(".nav-item.open").forEach((el) => el.classList.remove("open"));
  });

  // Global Audio TTS & HTML5 Player
  const audioStatus = document.getElementById("audioStatus");
  const audioPlayer = document.getElementById("htmlAudioPlayer");
  window.AWDEV_speak = function (text, title = "Audio Narration") {
    if (audioPlayer && !audioPlayer.paused) audioPlayer.pause();
    if ("speechSynthesis" in window) {
      window.speechSynthesis.cancel();
      const utter = new SpeechSynthesisUtterance(text);
      utter.lang = document.documentElement.lang === "ar" ? "ar-SA" : document.documentElement.lang === "en" ? "en-US" : "id-ID";
      utter.onstart = () => { if (audioStatus) audioStatus.textContent = `Speaking: ${title}`; };
      utter.onend = () => { if (audioStatus) audioStatus.textContent = "Audio ready"; };
      window.speechSynthesis.speak(utter);
      showToast(`Playing audio: ${title}`);
    } else {
      showToast("SpeechSynthesis not supported in this browser");
    }
  };

  const stopAudioBtn = document.getElementById("stopAudioBtn");
  if (stopAudioBtn) {
    stopAudioBtn.addEventListener("click", () => {
      if ("speechSynthesis" in window) window.speechSynthesis.cancel();
      if (audioPlayer) { audioPlayer.pause(); audioPlayer.currentTime = 0; }
      if (audioStatus) audioStatus.textContent = "Audio stopped";
    });
  }

  // Render Tool Cards
  const devGrid = document.getElementById("devToolsGrid");
  const islamicGrid = document.getElementById("islamicToolsGrid");

  function renderToolCards(list, targetEl, prefixLabel) {
    if (!targetEl) return;
    targetEl.innerHTML = list.map((tool) => `
      <article class="card" data-search="${(tool.name + " " + tool.category + " " + tool.description).toLowerCase()}">
        <span class="card-tag">${tool.category}</span>
        <h3>${tool.name}</h3>
        <p>${tool.description}</p>
        <div class="card-actions">
          <button class="btn btn-primary" type="button" onclick="window.AWDEV_openToolSandbox('${tool.id}', '${tool.name.replace(/'/g, "\\'")}')">Open Tool</button>
          <button class="btn" type="button" onclick="window.AWDEV_speak('${tool.name}. ${tool.description.replace(/'/g, "\\'")}', '${tool.name.replace(/'/g, "\\'")}')">Listen</button>
        </div>
      </article>
    `).join("");
    if (list.length === 0) {
      targetEl.innerHTML = `<p style="color:var(--muted-color)">No ${prefixLabel} match your filter.</p>`;
    }
  }

  renderToolCards(window.AWDEV_DEV_TOOLS || [], devGrid, "developer tools");
  renderToolCards(window.AWDEV_ISLAMIC_TOOLS || [], islamicGrid, "Islamic tools");

  // Interactive Sandbox Demos
  const tasbihCountEl = document.getElementById("tasbihCount");
  const tasbihTargetEl = document.getElementById("tasbihTarget");
  const tasbihPhraseEl = document.getElementById("tasbihPhrase");
  let tasbihState = window.AWDEV_IslamicEngine.getTasbihState();

  function syncTasbihUI() {
    if (tasbihCountEl) tasbihCountEl.textContent = tasbihState.count;
    if (tasbihTargetEl) tasbihTargetEl.value = String(tasbihState.target);
    if (tasbihPhraseEl) tasbihPhraseEl.value = tasbihState.phrase;
  }
  syncTasbihUI();

  const tasbihIncBtn = document.getElementById("tasbihInc");
  if (tasbihIncBtn) {
    tasbihIncBtn.addEventListener("click", () => {
      tasbihState.count += 1;
      window.AWDEV_IslamicEngine.saveTasbihState(tasbihState);
      syncTasbihUI();
      if (tasbihState.count === Number(tasbihState.target)) {
        showToast(`Target ${tasbihState.target} reached!`);
      }
    });
  }
  const tasbihResetBtn = document.getElementById("tasbihReset");
  if (tasbihResetBtn) {
    tasbihResetBtn.addEventListener("click", () => {
      tasbihState.count = 0;
      window.AWDEV_IslamicEngine.saveTasbihState(tasbihState);
      syncTasbihUI();
      showToast("Tasbih reset to 0");
    });
  }
  if (tasbihTargetEl) {
    tasbihTargetEl.addEventListener("change", (e) => {
      tasbihState.target = Number(e.target.value);
      window.AWDEV_IslamicEngine.saveTasbihState(tasbihState);
    });
  }
  if (tasbihPhraseEl) {
    tasbihPhraseEl.addEventListener("change", (e) => {
      tasbihState.phrase = e.target.value;
      window.AWDEV_IslamicEngine.saveTasbihState(tasbihState);
    });
  }

  // Word Counter, Password & Base64 interactive demos
  const textSample = document.getElementById("demoTextInput");
  const textStatsOut = document.getElementById("demoTextStats");
  function updateTextDemo() {
    if (!textSample || !textStatsOut) return;
    const s = window.AWDEV_ToolsEngine.countText(textSample.value);
    textStatsOut.textContent = `Words: ${s.words} | Chars: ${s.chars} | No-space: ${s.charsNoSpace} | Sentences: ${s.sentences} | Read time: ~${s.readingMin} min`;
  }
  if (textSample) {
    textSample.addEventListener("input", updateTextDemo);
    updateTextDemo();
  }

  const genPassBtn = document.getElementById("genPassBtn");
  const passOut = document.getElementById("passOutput");
  const passLen = document.getElementById("passLength");
  if (genPassBtn && passOut) {
    genPassBtn.addEventListener("click", () => {
      const len = passLen ? Math.min(64, Math.max(8, Number(passLen.value) || 16)) : 16;
      passOut.textContent = window.AWDEV_ToolsEngine.generatePassword(len);
    });
    passOut.textContent = window.AWDEV_ToolsEngine.generatePassword(16);
  }

  const b64Input = document.getElementById("b64Input");
  const b64Output = document.getElementById("b64Output");
  const b64EncBtn = document.getElementById("b64EncodeBtn");
  const b64DecBtn = document.getElementById("b64DecodeBtn");
  if (b64EncBtn && b64Input && b64Output) {
    b64EncBtn.addEventListener("click", () => {
      b64Output.textContent = window.AWDEV_ToolsEngine.encodeBase64(b64Input.value);
    });
  }
  if (b64DecBtn && b64Input && b64Output) {
    b64DecBtn.addEventListener("click", () => {
      try {
        b64Output.textContent = window.AWDEV_ToolsEngine.decodeBase64(b64Input.value);
      } catch (_) {
        b64Output.textContent = "Invalid Base64 string.";
      }
    });
  }

  window.AWDEV_openToolSandbox = function (id, name) {
    const lab = document.getElementById("interactiveLab");
    const activeLabel = document.getElementById("activeToolTitle");
    if (activeLabel) activeLabel.textContent = `Active Tool: ${name} (${id})`;
    if (lab) lab.scrollIntoView({ behavior: "smooth" });
    showToast(`Opened ${name}`);
  };

  // Categories (30 labels) & 900 Articles browser
  const labelsBar = document.getElementById("categoriesBar");
  const articlesListEl = document.getElementById("articlesIndexList");
  let selectedCategory = "ALL";

  function renderArticles(catFilter = "ALL", searchQuery = "") {
    if (!articlesListEl) return;
    const q = searchQuery.trim().toLowerCase();
    const filtered = (window.AWDEV_ARTICLES || []).filter((a) => {
      const matchCat = catFilter === "ALL" || a.category === catFilter;
      const matchQ = !q || a.title.toLowerCase().includes(q) || a.category.toLowerCase().includes(q);
      return matchCat && matchQ;
    }).slice(0, 18);

    articlesListEl.innerHTML = filtered.map((a) => `
      <article class="card">
        <span class="card-tag">${a.category}</span>
        <h3>${a.title}</h3>
        <p>Estimated depth: 3,000+ words SEO guide • ${a.readingTime}</p>
        <div class="card-actions">
          <a class="btn btn-primary" href="${a.url}">Read Article</a>
          <button class="btn" type="button" onclick="window.AWDEV_speak('${a.title.replace(/'/g, "\\'")}', '${a.category.replace(/'/g, "\\'")}')">Listen</button>
        </div>
      </article>
    `).join("");
  }

  if (labelsBar) {
    const cats = window.AWDEV_CATEGORIES || [];
    labelsBar.innerHTML = `<button class="chip active" data-cat="ALL">All (${cats.length} Categories / 900 Articles)</button>` +
      cats.map((c) => `<button class="chip" data-cat="${c}">${c}</button>`).join("");

    labelsBar.querySelectorAll(".chip").forEach((chip) => {
      chip.addEventListener("click", () => {
        labelsBar.querySelectorAll(".chip").forEach((c) => c.classList.remove("active"));
        chip.classList.add("active");
        selectedCategory = chip.dataset.cat;
        renderArticles(selectedCategory, document.getElementById("globalSearch")?.value || "");
      });
    });
  }
  renderArticles("ALL", "");

  // Populate dropdowns (Blog categories, E-Learning, Partners)
  const blogDropdown = document.getElementById("blogDropdownMenu");
  if (blogDropdown && window.AWDEV_CATEGORIES) {
    blogDropdown.innerHTML = window.AWDEV_CATEGORIES.map((c) => {
      const slug = c.toLowerCase().replace(/&/g, "and").replace(/\\//g, "-").replace(/\\s+/g, "-");
      return `<a href="#blog-section" onclick="document.querySelector('[data-cat=\\"${c.replace(/"/g, '\\"')}\\"]')?.click()">${c} (30)</a>`;
    }).join("");
  }

  const learnDropdown = document.getElementById("learnDropdownMenu");
  if (learnDropdown && window.AWDEV_ELEARNING) {
    learnDropdown.innerHTML = window.AWDEV_ELEARNING.map((s) =>
      `<a href="${s.url}" target="_blank" rel="noopener noreferrer">${s.name} ↗</a>`
    ).join("");
  }

  // E-Learning & Partners grids
  const learnGrid = document.getElementById("elearningGrid");
  if (learnGrid && window.AWDEV_ELEARNING) {
    learnGrid.innerHTML = window.AWDEV_ELEARNING.map((item) => `
      <article class="card">
        <span class="card-tag">E-Learning</span>
        <h3>${item.name}</h3>
        <p>${item.url}</p>
        <div class="card-actions">
          <a class="btn btn-primary" href="${item.url}" target="_blank" rel="noopener noreferrer">Visit Platform</a>
        </div>
      </article>
    `).join("");
  }

  const partnersGrid = document.getElementById("partnersGrid");
  if (partnersGrid && window.AWDEV_PARTNERS) {
    partnersGrid.innerHTML = window.AWDEV_PARTNERS.map((item) => `
      <article class="card">
        <span class="card-tag">Ecosystem Partner</span>
        <h3>${item.name}</h3>
        <p>${item.url}</p>
        <div class="card-actions">
          <a class="btn" href="${item.url}" target="_blank" rel="noopener noreferrer">Open Link</a>
        </div>
      </article>
    `).join("");
  }

  // Media Galleries (30 Images + 30 Videos) with Lightbox, Share & Copy
  const imgGrid = document.getElementById("imageGalleryGrid");
  const vidGrid = document.getElementById("videoGalleryGrid");
  const lightbox = document.getElementById("lightbox");
  const lightboxImg = document.getElementById("lightboxImg");
  const lightboxCaption = document.getElementById("lightboxCaption");

  window.AWDEV_shareOrCopy = function (title, url) {
    if (navigator.clipboard) {
      navigator.clipboard.writeText(url).catch(() => {});
    }
    if (navigator.share) {
      navigator.share({ title, url }).catch(() => showToast("Link copied to clipboard!"));
    } else {
      showToast("Copied link!");
    }
  };

  if (imgGrid) {
    const items = Array.from({ length: 30 }, (_, i) => {
      const idx = i + 1;
      const svgData = encodeURIComponent(`<svg xmlns="http://www.w3.org/2000/svg" width="600" height="375"><rect width="100%" height="100%" fill="#0f172a"/><text x="50%" y="46%" fill="#38bdf8" font-family="sans-serif" font-size="28" text-anchor="middle">AWDEV Visual #${idx}</text><text x="50%" y="60%" fill="#94a3b8" font-family="sans-serif" font-size="16" text-anchor="middle">awdev.eu.org/awdev.jpg</text></svg>`);
      return {
        title: `AWDEV Visual Asset #${idx}`,
        desc: `Modular architecture & UI visual reference item ${idx} of 30.`,
        src: `data:image/svg+xml,${svgData}`,
        shareUrl: `https://awdev.eu.org/#image-${idx}`
      };
    });

    imgGrid.innerHTML = items.map((it) => `
      <article class="card">
        <img class="media-thumb" src="${it.src}" alt="${it.title}" loading="lazy" onclick="window.AWDEV_openLightbox('${it.src}', '${it.title}')" style="cursor:pointer" />
        <h3>${it.title}</h3>
        <p>${it.desc}</p>
        <div class="card-actions">
          <button class="btn btn-primary" type="button" onclick="window.AWDEV_openLightbox('${it.src}', '${it.title}')">Preview</button>
          <button class="btn" type="button" onclick="window.AWDEV_shareOrCopy('${it.title}', '${it.shareUrl}')">Share / Copy</button>
        </div>
      </article>
    `).join("");
  }

  if (vidGrid) {
    const vids = Array.from({ length: 30 }, (_, i) => {
      const idx = i + 1;
      return {
        title: `AWDEV Tech & Islamic Tutorial Clip #${idx}`,
        desc: `Short-form walkthrough and utility demo episode ${idx} of 30.`,
        url: `https://awdev.eu.org/#video-${idx}`
      };
    });
    vidGrid.innerHTML = vids.map((v) => `
      <article class="card">
        <div class="media-thumb" style="display:flex;align-items:center;justify-content:center;font-weight:700;color:var(--primary)">▶ ${v.title}</div>
        <h3>${v.title}</h3>
        <p>${v.desc}</p>
        <div class="card-actions">
          <button class="btn btn-primary" type="button" onclick="window.AWDEV_speak('${v.title}. ${v.desc}', '${v.title}')">Play Narration</button>
          <button class="btn" type="button" onclick="window.AWDEV_shareOrCopy('${v.title}', '${v.url}')">Copy URL</button>
        </div>
      </article>
    `).join("");
  }

  window.AWDEV_openLightbox = function (src, caption) {
    if (!lightbox || !lightboxImg || !lightboxCaption) return;
    lightboxImg.src = src;
    lightboxCaption.textContent = caption;
    lightbox.classList.add("open");
  };
  const closeLb = document.getElementById("closeLightbox");
  if (closeLb && lightbox) {
    closeLb.addEventListener("click", () => lightbox.classList.remove("open"));
    lightbox.addEventListener("click", (e) => { if (e.target === lightbox) lightbox.classList.remove("open"); });
  }

  // Real-time search across tools & articles
  const globalSearch = document.getElementById("globalSearch");
  if (globalSearch) {
    globalSearch.addEventListener("input", (e) => {
      const q = e.target.value.trim().toLowerCase();
      document.querySelectorAll("#devToolsGrid .card, #islamicToolsGrid .card").forEach((card) => {
        const hay = card.getAttribute("data-search") || "";
        card.style.display = !q || hay.includes(q) ? "" : "none";
      });
      renderArticles(selectedCategory, q);
    });
  }

  // Contact form handler
  const contactForm = document.getElementById("contactForm");
  if (contactForm) {
    contactForm.addEventListener("submit", (e) => {
      e.preventDefault();
      showToast("Message prepared! Thank you for contacting AWDEV.");
      contactForm.reset();
    });
  }
})();
""",
  )

  # =========================================================================
  # 5. MAIN HOMEPAGE (index.html) WITH ADSENSE & GTM
  # =========================================================================
  head_common = """<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="google-adsense-account" content="ca-pub-5407249785989200" />
<meta name="google-site-verification" content="gbPa2MRABFiJSWv4hIj24aNn2MTRfi7W96fncHPziHI" />
<link rel="icon" href="https://awdev.eu.org/favicon.ico" />
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5407249785989200" crossorigin="anonymous"></script>
<script async custom-element="amp-auto-ads" src="https://cdn.ampproject.org/v0/amp-auto-ads-0.1.js"></script>
<script async src="https://www.googletagmanager.com/gtm.js?id=GTM-PMLF34B9"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
</script>"""

  ad_slot_1 = """<!-- ADSENSE SLOT 1: Top / Below Header -->
<div class="ad-wrapper" aria-label="Advertisement">
  <span class="ad-label">Advertisement</span>
  <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-5407249785989200" data-ad-slot="3805519345" data-ad-format="auto" data-full-width-responsive="true"></ins>
  <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
</div>"""

  ad_slot_2 = """<!-- ADSENSE SLOT 2: In-Article / Mid-Content -->
<div class="ad-wrapper" aria-label="Advertisement">
  <span class="ad-label">Sponsored</span>
  <ins class="adsbygoogle" style="display:block; text-align:center;" data-ad-layout="in-article" data-ad-format="fluid" data-ad-client="ca-pub-5407249785989200" data-ad-slot="8835759835"></ins>
  <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
</div>"""

  ad_slot_3 = """<!-- ADSENSE SLOT 3: Bottom / Above Footer -->
<div class="ad-wrapper" aria-label="Advertisement">
  <span class="ad-label">Advertisement</span>
  <ins class="adsbygoogle" style="display:block" data-ad-format="autorelaxed" data-ad-client="ca-pub-5407249785989200" data-ad-slot="6209596494"></ins>
  <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
</div>"""

  write_file(
      root,
      "index.html",
      f"""<!DOCTYPE html>
<html lang="id">
<head>
  {head_common}
  <title>AWDEV — Developer Tools, Islamic Utilities &amp; Tech Hub (awdev.eu.org)</title>
  <meta name="description" content="AWDEV provides free developer tools, Islamic utilities, media galleries, learning resources, and SEO guides on awdev.eu.org." />
  <link rel="canonical" href="https://awdev.eu.org/" />
  <link rel="stylesheet" href="assets/css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container nav-inner">
      <a class="brand" href="index.html">
        <svg width="28" height="28" viewBox="0 0 32 32" aria-hidden="true">
          <rect width="32" height="32" rx="8" fill="#0ea5e9"/>
          <path d="M8 22L13.5 10L19 22M10.2 18H16.8M21 10L24 22L27 10" stroke="#fff" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <img class="brand-avatar" src="https://awdev.eu.org/awdev.jpg" alt="AWDEV logo" onerror="this.style.display='none'" />
        <span>AWDEV</span>
      </a>

      <nav class="nav-menu" aria-label="Main Navigation">
        <a class="nav-link" href="#top">Home</a>
        <div class="nav-item">
          <button class="nav-btn" type="button" data-dropdown="dev">Developer Tools ▼</button>
          <div class="dropdown-panel">
            <a href="#dev-tools-section">Code &amp; Minifier</a>
            <a href="#dev-tools-section">CSS Generators</a>
            <a href="#dev-tools-section">SEO &amp; DNS</a>
            <a href="#dev-tools-section">Text &amp; Security</a>
          </div>
        </div>
        <div class="nav-item">
          <button class="nav-btn" type="button" data-dropdown="islamic">Islamic Tools ▼</button>
          <div class="dropdown-panel">
            <a href="#islamic-tools-section">Worship &amp; Prayer</a>
            <a href="#islamic-tools-section">Al-Qur'an &amp; Dua</a>
            <a href="#islamic-tools-section">Finance &amp; Zakat</a>
            <a href="#islamic-tools-section">Islamic Maps &amp; Finder</a>
          </div>
        </div>
        <div class="nav-item">
          <button class="nav-btn" type="button" data-dropdown="media">Media Gallery ▼</button>
          <div class="dropdown-panel">
            <a href="#image-gallery-section">Image Gallery (30 Items)</a>
            <a href="#video-gallery-section">Video Gallery (30 Items)</a>
          </div>
        </div>
        <div class="nav-item">
          <button class="nav-btn" type="button" data-dropdown="blog">Blog (30 Cat) ▼</button>
          <div class="dropdown-panel" id="blogDropdownMenu"></div>
        </div>
        <div class="nav-item">
          <button class="nav-btn" type="button" data-dropdown="learn">Learn &amp; Partners ▼</button>
          <div class="dropdown-panel" id="learnDropdownMenu"></div>
        </div>
        <div class="nav-item">
          <button class="nav-btn" type="button" data-dropdown="pages">Pages ▼</button>
          <div class="dropdown-panel">
            <a href="#about-section">About Us</a>
            <a href="#contact-section">Contact Us</a>
            <a href="#legal-section">Privacy Policy</a>
            <a href="#legal-section">Terms &amp; Conditions</a>
            <a href="404.html">Custom 404 Page</a>
          </div>
        </div>
      </nav>

      <div class="nav-controls">
        <input id="globalSearch" class="search-input" type="search" placeholder="Search tools, categories, or articles..." aria-label="Search" />
        <select id="langSelect" class="select-input" aria-label="Language Switcher">
          <option value="id">ID</option>
          <option value="en">EN</option>
          <option value="ar">العربية</option>
        </select>
        <button id="themeToggle" class="btn" type="button">🌓 Theme</button>
      </div>
    </div>
  </header>

  <main id="top" class="container">
    <section class="hero">
      <div class="hero-box">
        <h1 id="heroTitle">Developer Tools, Islamic Utilities &amp; SEO Tech Knowledge Hub</h1>
        <p id="heroSubtitle">Free browser-based web utilities, Islamic calculators &amp; guides, media galleries, and technical articles for awdev.eu.org.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="#dev-tools-section">Explore Tools</a>
          <a class="btn btn-accent" href="#blog-section">Learn Coding &amp; SEO</a>
        </div>
        <div class="stats-row">
          <div class="stat-pill"><strong>60+</strong><span>Free Web &amp; Islamic Tools</span></div>
          <div class="stat-pill"><strong>30 × 30</strong><span>900 Indexed SEO Articles</span></div>
          <div class="stat-pill"><strong>60</strong><span>Image &amp; Video Gallery Items</span></div>
          <div class="stat-pill"><strong>44</strong><span>E-Learning &amp; Partner Sites</span></div>
        </div>
      </div>
    </section>

    {ad_slot_1}

    <!-- LIVE INTERACTIVE SANDBOX -->
    <section id="interactiveLab" class="section">
      <div class="section-head">
        <div>
          <h2 id="activeToolTitle">Interactive Tool Sandbox</h2>
          <p>Live client-side utilities: Digital Tasbih (persisted in localStorage), Word Counter, Password Generator &amp; Base64.</p>
        </div>
      </div>
      <div class="lab-panel">
        <div class="lab-grid">
          <!-- Tasbih -->
          <div class="card">
            <span class="card-tag">Islamic Utility</span>
            <h3>Digital Tasbih (Dhikr Counter)</h3>
            <div style="display:flex;gap:0.5rem;flex-wrap:wrap;">
              <select id="tasbihPhrase" class="select-input">
                <option value="SubhanAllah">SubhanAllah</option>
                <option value="Alhamdulillah">Alhamdulillah</option>
                <option value="Allahu Akbar">Allahu Akbar</option>
                <option value="Astaghfirullah">Astaghfirullah</option>
              </select>
              <select id="tasbihTarget" class="select-input">
                <option value="33">Target: 33</option>
                <option value="99">Target: 99</option>
                <option value="100">Target: 100</option>
              </select>
            </div>
            <p style="font-size:2rem;font-weight:800;color:var(--primary);text-align:center;" id="tasbihCount">0</p>
            <div class="card-actions">
              <button id="tasbihInc" class="btn btn-primary" type="button">+ Count Dhikr</button>
              <button id="tasbihReset" class="btn" type="button">Reset</button>
            </div>
          </div>

          <!-- Word & Character Counter -->
          <div class="card">
            <span class="card-tag">Text Utility</span>
            <h3>Word &amp; Character Counter</h3>
            <textarea id="demoTextInput" class="textarea-field" placeholder="Type or paste text to analyze..."></textarea>
            <div id="demoTextStats" class="output-box"></div>
          </div>

          <!-- Strong Password & Base64 -->
          <div class="card">
            <span class="card-tag">Security &amp; Encoding</span>
            <h3>Strong Password &amp; Base64</h3>
            <div style="display:flex;gap:0.5rem;align-items:center;">
              <input id="passLength" class="input-field" type="number" min="8" max="64" value="16" style="width:85px;" />
              <button id="genPassBtn" class="btn btn-primary" type="button">Generate Password</button>
            </div>
            <div id="passOutput" class="output-box"></div>
            <input id="b64Input" class="input-field" type="text" placeholder="Text or Base64 string..." />
            <div class="card-actions">
              <button id="b64EncodeBtn" class="btn" type="button">Encode B64</button>
              <button id="b64DecodeBtn" class="btn" type="button">Decode B64</button>
            </div>
            <div id="b64Output" class="output-box">Base64 output...</div>
          </div>
        </div>
      </div>
    </section>

    <!-- DEVELOPER TOOLS -->
    <section id="dev-tools-section" class="section">
      <div class="section-head">
        <div>
          <h2>Developer &amp; Web Tools Directory</h2>
          <p>Client-side code formatters, CSS generators, SEO builders, DNS &amp; map utilities.</p>
        </div>
      </div>
      <div id="devToolsGrid" class="grid"></div>
    </section>

    {ad_slot_2}

    <!-- ISLAMIC TOOLS -->
    <section id="islamic-tools-section" class="section">
      <div class="section-head">
        <div>
          <h2>Islamic Tools &amp; Utilities Directory</h2>
          <p>Prayer times, Qibla direction, Al-Qur'an, Zakat &amp; Faraidh calculators, Hijri dates, and daily worship trackers.</p>
        </div>
      </div>
      <div id="islamicToolsGrid" class="grid"></div>
    </section>

    <!-- BLOG 30 CATEGORIES x 30 ARTICLES -->
    <section id="blog-section" class="section">
      <div class="section-head">
        <div>
          <h2>SEO Knowledge Blog (30 Categories × 30 Articles = 900 Entries)</h2>
          <p>Filter across all 30 technical &amp; web categories and open full 3,000-word SEO article templates.</p>
        </div>
      </div>
      <div id="categoriesBar" class="labels-bar"></div>
      <div id="articlesIndexList" class="grid"></div>
    </section>

    <!-- IMAGE & VIDEO GALLERIES -->
    <section id="image-gallery-section" class="section">
      <div class="section-head">
        <div>
          <h2>Image Gallery (30 Items)</h2>
          <p>Click any image for lightbox preview, or copy/share its link.</p>
        </div>
      </div>
      <div id="imageGalleryGrid" class="grid"></div>
    </section>

    <section id="video-gallery-section" class="section">
      <div class="section-head">
        <div>
          <h2>Video Gallery (30 Items)</h2>
          <p>Browse 30 tutorial clips with narration playback and share/copy links.</p>
        </div>
      </div>
      <div id="videoGalleryGrid" class="grid"></div>
    </section>

    {ad_slot_3}

    <!-- E-LEARNING (20) & PARTNERS (24) -->
    <section id="elearning-section" class="section">
      <div class="section-head">
        <div>
          <h2>E-Learning &amp; Resources (20 International Sites)</h2>
          <p>Curated platforms for mastering web development, algorithms, and computer science.</p>
        </div>
      </div>
      <div id="elearningGrid" class="grid"></div>
    </section>

    <section id="partners-section" class="section">
      <div class="section-head">
        <div>
          <h2>Partners &amp; Ecosystem (24 Platforms)</h2>
          <p>Developer communities, cloud providers, Indonesian tech portals, and Islamic platforms.</p>
        </div>
      </div>
      <div id="partnersGrid" class="grid"></div>
    </section>

    <!-- ABOUT, CONTACT & LEGAL -->
    <section id="about-section" class="section">
      <div class="card">
        <h2>About AWDEV</h2>
        <p>AWDEV (<strong>awdev.eu.org</strong>) is an independent web utilities and knowledge hub built to give developers, students, and Muslim users fast, accessible, and privacy-conscious tools.</p>
      </div>
    </section>

    <section id="contact-section" class="section">
      <div class="card">
        <h2>Contact Us</h2>
        <p>Have feedback, bug reports, or partnership inquiries for <strong>awdev.eu.org</strong>? Send a message below.</p>
        <form id="contactForm" style="display:grid;gap:0.75rem;margin-top:0.5rem;max-width:600px;">
          <input class="input-field" type="text" placeholder="Your Name" required />
          <input class="input-field" type="email" placeholder="you@example.com" required />
          <textarea class="textarea-field" placeholder="Your message..." required></textarea>
          <button class="btn btn-primary" type="submit" style="width:fit-content;">Send Message</button>
        </form>
      </div>
    </section>

    <section id="legal-section" class="section">
      <div class="lab-grid">
        <div class="card">
          <h3>Privacy Policy</h3>
          <p>Most AWDEV tools execute locally in your browser. Third-party services such as Google AdSense, Google Tag Manager, DNS/map APIs, and external links may process standard technical request metadata under their respective privacy policies.</p>
        </div>
        <div class="card">
          <h3>Terms &amp; Conditions</h3>
          <p>All calculators, converters, and reference guides on awdev.eu.org are provided "as-is" for informational and productivity purposes. Always verify critical financial, legal, or religious rulings with qualified authorities.</p>
        </div>
      </div>
    </section>
  </main>

  <!-- FLOATING AUDIO BAR -->
  <div class="audio-bar" role="region" aria-label="Audio Player Bar">
    <span id="audioStatus" class="audio-status">AWDEV Audio Ready</span>
    <audio id="htmlAudioPlayer" controls preload="none" style="height:32px;max-width:260px;"></audio>
    <button id="stopAudioBtn" class="btn" type="button">⏹ Stop</button>
  </div>

  <!-- LIGHTBOX & TOAST -->
  <div id="lightbox" class="lightbox" role="dialog" aria-modal="true">
    <div class="lightbox-inner">
      <img id="lightboxImg" src="" alt="" />
      <div style="display:flex;justify-content:space-between;align-items:center;gap:1rem;">
        <p id="lightboxCaption" style="font-weight:600;"></p>
        <button id="closeLightbox" class="btn btn-primary" type="button">Close</button>
      </div>
    </div>
  </div>
  <div id="toast" class="toast" role="status" aria-live="polite"></div>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <h4>AWDEV Platform</h4>
          <p style="font-size:0.86rem;color:var(--muted-color);">Web Development Tools, Islamic Utilities, Galleries &amp; SEO Guides at awdev.eu.org.</p>
        </div>
        <div>
          <h4>Mandatory Pages</h4>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="#about-section">About Us</a></li>
            <li><a href="#dev-tools-section">Tools Directory</a></li>
            <li><a href="#contact-section">Contact Us</a></li>
            <li><a href="#legal-section">Privacy Policy</a></li>
            <li><a href="#legal-section">Terms &amp; Conditions</a></li>
            <li><a href="404.html">Custom 404 Page</a></li>
          </ul>
        </div>
        <div>
          <h4>Sections</h4>
          <ul>
            <li><a href="#dev-tools-section">30+ Developer Tools</a></li>
            <li><a href="#islamic-tools-section">30 Islamic Tools</a></li>
            <li><a href="#blog-section">Blog (900 Entries)</a></li>
            <li><a href="#elearning-section">20 E-Learning Sites</a></li>
            <li><a href="#partners-section">24 Ecosystem Partners</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© 2026 AWDEV (awdev.eu.org). All rights reserved.</span>
        <span>GitHub • Web Tools • Islamic Utilities</span>
      </div>
    </div>
  </footer>

  <script src="assets/js/tools-engine.js"></script>
  <script src="assets/js/islamic-engine.js"></script>
  <script src="assets/js/blog-data.js"></script>
  <script src="assets/js/app.js"></script>
</body>
</html>
""",
  )

  # =========================================================================
  # 6. SEO ARTICLE TEMPLATE (article.html) WITH AUTO-TOC, FAQ & 3 AD SLOTS
  # =========================================================================
  write_file(
      root,
      "article.html",
      f"""<!DOCTYPE html>
<html lang="en">
<head>
  {head_common}
  <title id="seoTitle">AWDEV SEO Article — awdev.eu.org</title>
  <meta name="description" id="seoDesc" content="Comprehensive technical and web development guide on awdev.eu.org." />
  <link rel="canonical" href="https://awdev.eu.org/article.html" />
  <link rel="stylesheet" href="assets/css/style.css" />
  <script type="application/ld+json" id="jsonLdArticle">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "AWDEV Technical Guide",
    "publisher": {{
      "@type": "Organization",
      "name": "AWDEV",
      "url": "https://awdev.eu.org"
    }}
  }}
  </script>
  <script type="application/ld+json" id="jsonLdFaq">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "How can I apply this guide in a production web project?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Start with semantic HTML, modular assets, measurable Core Web Vitals, and automated validation before deployment."
        }}
      }}
    ]
  }}
  </script>
</head>
<body>
  <header class="site-header">
    <div class="container nav-inner">
      <a class="brand" href="index.html">← Back to AWDEV</a>
      <div class="nav-controls">
        <button id="listenArticleBtn" class="btn btn-primary" type="button">🔊 Listen Audio</button>
        <button id="themeToggle" class="btn" type="button">🌓 Theme</button>
      </div>
    </div>
  </header>

  <main class="container section" style="max-width:920px;">
    <article id="articleContent" class="card" style="gap:1rem;">
      <span class="card-tag" id="artCategoryTag">Category</span>
      <h1 id="artHeading" style="font-size:2rem;line-height:1.25;">Loading Article...</h1>
      <p id="artMeta" style="color:var(--muted-color);font-size:0.9rem;">Published on awdev.eu.org • ~3,000 Words Long-Form Guide</p>

      <!-- Auto Table of Contents -->
      <div class="output-box" id="tocContainer">
        <strong>Table of Contents</strong>
        <ul id="tocList" style="margin-top:0.5rem;padding-left:1.25rem;"></ul>
      </div>

      {ad_slot_1}

      <h2 id="sec-1">1. Architectural Overview &amp; Core Concepts</h2>
      <p>Building maintainable web applications on <strong>awdev.eu.org</strong> requires clean separation of concerns between markup, styling, client-side state, and external APIs. When every module has a clear responsibility, debugging and scaling become predictable.</p>

      <h3 id="sec-1-1">1.1 Performance &amp; Core Web Vitals</h3>
      <p>Reserve layout space for dynamic blocks and advertisements so Cumulative Layout Shift (CLS) stays minimal, defer non-critical scripts, and keep client-side utilities responsive on mobile devices.</p>

      <h2 id="sec-2">2. Step-by-Step Implementation &amp; Code Example</h2>
      <p>Below is a reusable pattern for formatting structured output safely in Vanilla JavaScript:</p>
      <div class="output-box" id="codeSnippetBlock">function formatToolResult(label, value) {{
  return `[${{label}}] ${{String(value).trim()}}`;
}}</div>
      <button id="copyCodeBtn" class="btn" type="button" style="width:fit-content;">Copy Code</button>

      {ad_slot_2}

      <h2 id="sec-3">3. Comparison Matrix</h2>
      <div style="overflow-x:auto;">
        <table style="width:100%;border-collapse:collapse;font-size:0.9rem;">
          <thead>
            <tr style="border-bottom:2px solid var(--border-color);text-align:left;">
              <th style="padding:0.6rem;">Approach</th>
              <th style="padding:0.6rem;">Latency</th>
              <th style="padding:0.6rem;">Privacy</th>
              <th style="padding:0.6rem;">Best Use Case</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--border-color);">
              <td style="padding:0.6rem;">Client-Side JS</td>
              <td style="padding:0.6rem;">Instant</td>
              <td style="padding:0.6rem;">High (Local)</td>
              <td style="padding:0.6rem;">Formatters, counters, tasbih, generators</td>
            </tr>
            <tr>
              <td style="padding:0.6rem;">Public API Fetch</td>
              <td style="padding:0.6rem;">Network-bound</td>
              <td style="padding:0.6rem;">Standard TLS</td>
              <td style="padding:0.6rem;">DNS lookups, prayer times, maps</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2 id="sec-4">4. Frequently Asked Questions (FAQ)</h2>
      <details class="output-box">
        <summary style="font-weight:700;cursor:pointer;">Are the AWDEV tools free to use?</summary>
        <p style="margin-top:0.5rem;">Yes, utilities on awdev.eu.org are provided free of charge with non-intrusive ad placement.</p>
      </details>
      <details class="output-box">
        <summary style="font-weight:700;cursor:pointer;">Can I share or bookmark individual articles?</summary>
        <p style="margin-top:0.5rem;">Yes, each article supports direct URL parameters and one-click sharing.</p>
      </details>

      {ad_slot_3}

      <div class="card-actions">
        <button class="btn btn-primary" type="button" onclick="window.AWDEV_shareOrCopy(document.title, window.location.href)">Share Article Link</button>
        <a class="btn" href="index.html#blog-section">More Articles</a>
      </div>
    </article>
  </main>

  <div class="audio-bar">
    <span id="audioStatus" class="audio-status">AWDEV Audio Ready</span>
    <audio id="htmlAudioPlayer" controls preload="none" style="height:32px;max-width:260px;"></audio>
    <button id="stopAudioBtn" class="btn" type="button">⏹ Stop</button>
  </div>
  <div id="toast" class="toast"></div>

  <script src="assets/js/app.js"></script>
  <script>
    (function () {{
      const params = new URLSearchParams(window.location.search);
      const slug = params.get("slug") || "web-tools-guide-01";
      const cat = params.get("cat") || "Web Tools";
      const heading = document.getElementById("artHeading");
      const tag = document.getElementById("artCategoryTag");
      const titleEl = document.getElementById("seoTitle");

      const formattedTitle = slug.replace(/-/g, " ").replace(/\\b\\w/g, (c) => c.toUpperCase());
      if (heading) heading.textContent = formattedTitle;
      if (tag) tag.textContent = cat.replace(/-/g, " ").toUpperCase();
      if (titleEl) titleEl.textContent = `${{formattedTitle}} — AWDEV`;

      // Auto Table of Contents from H2 & H3
      const tocList = document.getElementById("tocList");
      const headings = document.querySelectorAll("#articleContent h2, #articleContent h3");
      if (tocList && headings.length) {{
        tocList.innerHTML = Array.from(headings).map((h) => {{
          const pad = h.tagName === "H3" ? "margin-left:1rem;" : "";
          return `<li style="${{pad}}"><a href="#${{h.id}}">${{h.textContent}}</a></li>`;
        }}).join("");
      }}

      const listenBtn = document.getElementById("listenArticleBtn");
      if (listenBtn) {{
        listenBtn.addEventListener("click", () => {{
          const bodyText = document.getElementById("articleContent")?.innerText || formattedTitle;
          window.AWDEV_speak(bodyText.slice(0, 1200), formattedTitle);
        }});
      }}

      const copyCodeBtn = document.getElementById("copyCodeBtn");
      const codeBlock = document.getElementById("codeSnippetBlock");
      if (copyCodeBtn && codeBlock && navigator.clipboard) {{
        copyCodeBtn.addEventListener("click", () => {{
          navigator.clipboard.writeText(codeBlock.textContent).then(() => {{
            window.AWDEV_toast("Code copied!");
          }});
        }});
      }}
    }})();
  </script>
</body>
</html>
""",
  )

  # =========================================================================
  # 7. CUSTOM 404 PAGE (404.html)
  # =========================================================================
  write_file(
      root,
      "404.html",
      f"""<!DOCTYPE html>
<html lang="en">
<head>
  {head_common}
  <title>404 Not Found — AWDEV (awdev.eu.org)</title>
  <link rel="stylesheet" href="assets/css/style.css" />
</head>
<body>
  <main class="container section" style="text-align:center;padding-top:4rem;">
    <div class="card" style="max-width:560px;margin:0 auto;align-items:center;">
      <span class="card-tag">Error 404</span>
      <h1 style="font-size:2.2rem;">Page Not Found</h1>
      <p>The page or utility you requested on <strong>awdev.eu.org</strong> could not be found or has moved.</p>
      <a class="btn btn-primary" href="index.html">Return to Home</a>
    </div>
  </main>
  <script src="assets/js/app.js"></script>
</body>
</html>
""",
  )

  print("\nDone! Run a local server inside 'awdev_dist', e.g.:")
  print("  python3 -m http.server 8000 --directory awdev_dist")


if __name__ == "__main__":
  main()
