import { useMemo, useState } from "react";
import { Search, Volume2, Code2, Palette, Globe, Lock, Moon, BookOpen, Calculator, MapPin, ArrowRight } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

type Tool = {
  slug: string;
  name: string;
  desc: string;
  category: "code" | "css" | "seo" | "text" | "worship" | "quran" | "finance" | "maps";
  icon: typeof Code2;
};

const tools: Tool[] = [
  { slug: "code-editor", name: "Live Code Editor", desc: "Split-screen HTML/CSS/JS playground with instant preview and download.", category: "code", icon: Code2 },
  { slug: "dns-checker", name: "DNS Web Checker", desc: "Query A, AAAA, MX, TXT, NS records via Google Public DNS.", category: "seo", icon: Globe },
  { slug: "minifier", name: "HTML/CSS/JS Minifier", desc: "Strip whitespace and comments from your source in real time.", category: "code", icon: Code2 },
  { slug: "beautifier", name: "Code Beautifier", desc: "Re-indent HTML, CSS, JS and JSON for readability.", category: "code", icon: Code2 },
  { slug: "json-validator", name: "JSON Validator", desc: "Validate syntax and explore a collapsible tree view.", category: "code", icon: Code2 },
  { slug: "regex-tester", name: "Regex Tester", desc: "Test patterns with live match highlighting.", category: "code", icon: Code2 },
  { slug: "base64", name: "Base64 Encoder / Decoder", desc: "Convert text and files to Base64 and back.", category: "text", icon: Lock },
  { slug: "url-encoder", name: "URL Encoder / Decoder", desc: "Encode and decode URI parameters safely.", category: "text", icon: Lock },
  { slug: "html-entity", name: "HTML Entity Encoder", desc: "Convert symbols to HTML entities and back.", category: "text", icon: Lock },
  { slug: "color-picker", name: "Color Picker & Palette", desc: "Pick HEX/RGB/HSL and generate 5 harmonious palettes.", category: "css", icon: Palette },
  { slug: "gradient-generator", name: "CSS Gradient Generator", desc: "Build linear and radial gradients with live preview.", category: "css", icon: Palette },
  { slug: "box-shadow", name: "CSS Box Shadow Generator", desc: "Tune X, Y, blur and spread with sliders.", category: "css", icon: Palette },
  { slug: "border-radius", name: "Border Radius Generator", desc: "Adjust all four corners of a CSS radius.", category: "css", icon: Palette },
  { slug: "glassmorphism", name: "Glassmorphism Generator", desc: "Craft frosted-glass effects with backdrop-filter.", category: "css", icon: Palette },
  { slug: "grid-flex", name: "Grid / Flexbox Generator", desc: "Visually build column and row layouts.", category: "css", icon: Palette },
  { slug: "favicon", name: "Favicon Generator", desc: "Convert uploads to 16, 32 and 180px icons via Canvas.", category: "seo", icon: Globe },
  { slug: "meta-tag", name: "Meta Tag Generator", desc: "Produce SEO, Open Graph and Twitter Card tags.", category: "seo", icon: Globe },
  { slug: "robots-txt", name: "Robots.txt Generator", desc: "Compose crawler rules for search engines.", category: "seo", icon: Globe },
  { slug: "sitemap", name: "XML Sitemap Generator", desc: "Build a valid XML sitemap from a URL list.", category: "seo", icon: Globe },
  { slug: "utm-builder", name: "UTM Link Builder", desc: "Create campaign tracking URLs in seconds.", category: "seo", icon: Globe },
  { slug: "word-counter", name: "Word & Character Counter", desc: "Count words, characters, sentences and reading time.", category: "text", icon: Lock },
  { slug: "case-converter", name: "Case Converter", desc: "UPPER, lower, Title, camelCase and snake_case.", category: "text", icon: Lock },
  { slug: "lorem-ipsum", name: "Lorem Ipsum Generator", desc: "Generate dummy paragraphs for mockups.", category: "text", icon: Lock },
  { slug: "text-diff", name: "Text Diff Checker", desc: "Compare two texts line by line.", category: "text", icon: Lock },
  { slug: "markdown", name: "Markdown to HTML", desc: "Convert Markdown syntax to copy-ready HTML.", category: "code", icon: Code2 },
  { slug: "qr-code", name: "QR Code Generator", desc: "Create QR codes from text or URL and download PNG.", category: "code", icon: Code2 },
  { slug: "password", name: "Strong Password Generator", desc: "Random passwords with length and symbol options.", category: "text", icon: Lock },
  { slug: "hash", name: "Hash Generator (MD5, SHA-256)", desc: "Hash text with the Web Crypto API.", category: "text", icon: Lock },
  { slug: "image-compressor", name: "Image Compressor & Resizer", desc: "Compress and resize images in the browser.", category: "code", icon: Code2 },
  { slug: "timestamp", name: "Unix Timestamp Converter", desc: "Convert Epoch time to local/UTC and back.", category: "code", icon: Code2 },
  { slug: "maps-finder", name: "Maps Finder", desc: "Find GPS coordinates and addresses on a live map.", category: "maps", icon: MapPin },
  { slug: "country-finder", name: "Maps Country Finder", desc: "Country info, capital, flag and currency.", category: "maps", icon: MapPin },
  { slug: "arabic-keyboard", name: "Arabic Keyboard", desc: "Virtual Arabic keyboard with tashkeel and copy.", category: "quran", icon: BookOpen },
  { slug: "calligraphy", name: "Calligraphy Tools", desc: "Arabic calligraphy in Diwani, Thuluth, Naskh and Kufi.", category: "quran", icon: BookOpen },
  { slug: "mosque-finder", name: "Mosque Finder", desc: "Locate nearby mosques via OpenStreetMap.", category: "maps", icon: MapPin },
  { slug: "islamic-school", name: "Islamic School Finder", desc: "Find madrasahs and pesantren on a map.", category: "maps", icon: MapPin },
  { slug: "prayer-log", name: "Log Your Daily Prayers", desc: "Track the five daily prayers and sunnah with progress.", category: "worship", icon: Moon },
  { slug: "dua-library", name: "Dua Library", desc: "Searchable duas with Arabic, transliteration and meaning.", category: "quran", icon: BookOpen },
  { slug: "duas-occasions", name: "Duas for Every Occasion", desc: "Travel, eating, sleep, illness, rain and more.", category: "quran", icon: BookOpen },
  { slug: "asmaul-husna", name: "99 Names of Allah", desc: "Arabic, Latin, meaning and audio for each name.", category: "quran", icon: BookOpen },
  { slug: "asma-quiz", name: "Learn the Asma ul-Husna", desc: "Interactive quiz and flashcards for memorisation.", category: "quran", icon: BookOpen },
  { slug: "finance-obligations", name: "Finance & Obligations", desc: "Zakat, fidyah, kafarat and nazar calculators.", category: "finance", icon: Calculator },
  { slug: "zakat", name: "Zakat Calculator", desc: "Maal, income, gold, silver and fitrah with nisab.", category: "finance", icon: Calculator },
  { slug: "prayer-times", name: "Automatic Prayer Times", desc: "City or GPS-based schedule via Aladhan API.", category: "worship", icon: Moon },
  { slug: "qibla", name: "Qibla Direction Finder", desc: "Compass bearing from your coordinates to the Ka'bah.", category: "worship", icon: Moon },
  { slug: "quran-reader", name: "Digital Al-Qur'an", desc: "Read all 30 Juz with translation.", category: "quran", icon: BookOpen },
  { slug: "quran-audio", name: "Al-Qur'an Audio Recitation", desc: "Murottal per surah with selectable reciters.", category: "quran", icon: BookOpen },
  { slug: "faraidh", name: "Islamic Inheritance Calculator", desc: "Distribute estate according to Faraidh rules.", category: "finance", icon: Calculator },
  { slug: "hijri-converter", name: "Gregorian to Hijri Converter", desc: "Convert dates between Gregorian and Hijri.", category: "worship", icon: Moon },
  { slug: "hijri-calendar", name: "Hijri Calendar", desc: "Monthly Hijri calendar with Islamic holidays.", category: "worship", icon: Moon },
  { slug: "tasbih", name: "Digital Tasbih", desc: "Dhikr counter with 33/99/100 targets and vibration.", category: "worship", icon: Moon },
  { slug: "adhkar", name: "Morning & Evening Adhkar", desc: "Guided daily remembrance with counters.", category: "worship", icon: Moon },
  { slug: "quran-search", name: "Al-Qur'an Verse Search", desc: "Search verses by translation keyword.", category: "quran", icon: BookOpen },
  { slug: "hadith-search", name: "Hadith Search Engine", desc: "Search across major hadith collections.", category: "quran", icon: BookOpen },
  { slug: "qadha-tracker", name: "Missed Prayer Tracker", desc: "Track and plan your qadha prayers.", category: "worship", icon: Moon },
  { slug: "fasting-fidyah", name: "Missed Fasting & Fidyah", desc: "Calculate Ramadan debts and fidyah amounts.", category: "finance", icon: Calculator },
  { slug: "imsakiyah", name: "Ramadan Imsakiyah", desc: "Imsak and iftar schedule for Ramadan.", category: "worship", icon: Moon },
  { slug: "ramadan-countdown", name: "Ramadan & Eid Countdown", desc: "Count down to Ramadan, Eid al-Fitr and Eid al-Adha.", category: "worship", icon: Moon },
  { slug: "greeting-card", name: "Islamic Greeting Card", desc: "Generate downloadable Islamic greeting images.", category: "quran", icon: BookOpen },
  { slug: "transliteration", name: "Latin to Arabic Transliteration", desc: "Convert Latin text to Arabic script.", category: "quran", icon: BookOpen },
  { slug: "nisab-live", name: "Real-Time Zakat Nisab", desc: "Nisab threshold based on today's gold price.", category: "finance", icon: Calculator },
  { slug: "hajj-guide", name: "Interactive Hajj & Umrah Guide", desc: "Step-by-step rites with talbiyah and tawaf duas.", category: "worship", icon: Moon },
  { slug: "khatam-tracker", name: "Al-Qur'an Khatam Tracker", desc: "Plan and track your Qur'an completion target.", category: "quran", icon: BookOpen },
];

const categories = [
  { key: "all", label: "allCategories" },
  { key: "code", label: "code" },
  { key: "css", label: "css" },
  { key: "seo", label: "seo" },
  { key: "text", label: "text" },
  { key: "worship", label: "worship" },
  { key: "quran", label: "quran" },
  { key: "finance", label: "finance" },
  { key: "maps", label: "maps" },
] as const;

export function ToolGrid({
  t,
  onListen,
  onOpen,
}: {
  t: (k: string) => string;
  onListen: (text: string) => void;
  onOpen: (slug: string) => void;
}) {
  const [query, setQuery] = useState("");
  const [cat, setCat] = useState<string>("all");

  const filtered = useMemo(() => {
    return tools.filter((tool) => {
      const matchCat = cat === "all" || tool.category === cat;
      const matchQuery =
        query.trim() === "" ||
        tool.name.toLowerCase().includes(query.toLowerCase()) ||
        tool.desc.toLowerCase().includes(query.toLowerCase());
      return matchCat && matchQuery;
    });
  }, [query, cat]);

  return (
    <section className="mx-auto max-w-7xl px-4 py-16">
      <div className="flex flex-col gap-4 lg:flex-row lg:items-end lg:justify-between">
        <div>
          <h2 className="font-serif text-3xl font-bold tracking-tight">{t("devToolsTitle")}</h2>
          <p className="mt-2 max-w-2xl text-sm text-slate-500 dark:text-slate-400">{t("devToolsDesc")}</p>
        </div>
        <div className="relative w-full lg:w-80">
          <Search className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-slate-400" />
          <Input
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder={t("search")}
            className="pl-9"
          />
        </div>
      </div>

      <div className="mt-6 flex flex-wrap gap-2">
        {categories.map((c) => (
          <button
            key={c.key}
            onClick={() => setCat(c.key)}
            className={`rounded-full px-4 py-1.5 text-xs font-semibold transition ${
              cat === c.key
                ? "bg-teal-600 text-white shadow-sm"
                : "bg-slate-100 text-slate-600 hover:bg-teal-50 hover:text-teal-700 dark:bg-slate-800 dark:text-slate-300"
            }`}
          >
            {t(c.label)}
          </button>
        ))}
      </div>

      {filtered.length === 0 ? (
        <div className="mt-12 rounded-2xl border border-dashed border-slate-300 bg-slate-50 p-12 text-center dark:border-slate-700 dark:bg-slate-900">
          <p className="text-sm text-slate-500 dark:text-slate-400">{t("noResults")}</p>
        </div>
      ) : (
        <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
          {filtered.map((tool) => {
            const Icon = tool.icon;
            return (
              <div
                key={tool.slug}
                className="group flex flex-col rounded-2xl border border-slate-200 bg-white p-5 shadow-sm transition hover:-translate-y-0.5 hover:border-teal-300 hover:shadow-md dark:border-slate-800 dark:bg-slate-900 dark:hover:border-teal-700"
              >
                <div className="flex items-start justify-between">
                  <span className="flex h-10 w-10 items-center justify-center rounded-xl bg-teal-50 text-teal-700 dark:bg-teal-950 dark:text-teal-400">
                    <Icon className="h-5 w-5" />
                  </span>
                  <button
                    onClick={() => onListen(`${tool.name}. ${tool.desc}`)}
                    className="rounded-lg p-1.5 text-slate-400 transition hover:bg-teal-50 hover:text-teal-600 dark:hover:bg-slate-800"
                    aria-label={t("listen")}
                  >
                    <Volume2 className="h-4 w-4" />
                  </button>
                </div>
                <h3 className="mt-4 text-sm font-semibold">{tool.name}</h3>
                <p className="mt-1 flex-1 text-xs leading-relaxed text-slate-500 dark:text-slate-400">{tool.desc}</p>
                <Button
                  size="sm"
                  variant="ghost"
                  className="mt-4 justify-start px-0 text-teal-700 hover:bg-transparent hover:text-teal-800 dark:text-teal-400"
                  onClick={() => onOpen(tool.slug)}
                >
                  Open tool <ArrowRight className="ml-1 h-3.5 w-3.5" />
                </Button>
              </div>
            );
          })}
        </div>
      )}
    </section>
  );
}