import { useState } from "react";
import { Search, Code2, Moon, Image, FileText, Lock, Globe } from "lucide-react";
import { Input } from "@/components/ui/input";
import { Card, CardContent } from "@/components/ui/card";

interface Tool {
  id: string;
  name: string;
  desc: string;
  cat: "dev" | "islamic" | "media" | "text" | "security" | "seo";
}

const tools: Tool[] = [
  { id: "code-editor", name: "Code Editor", desc: "Live HTML/CSS/JS editor with preview", cat: "dev" },
  { id: "dns-checker", name: "DNS Checker", desc: "Check A, AAAA, MX, TXT, NS records", cat: "seo" },
  { id: "minifier", name: "HTML/CSS/JS Minifier", desc: "Compress code in real-time", cat: "dev" },
  { id: "beautifier", name: "Code Beautifier", desc: "Format HTML, CSS, JS, JSON", cat: "dev" },
  { id: "json-validator", name: "JSON Validator", desc: "Validate and view JSON tree", cat: "dev" },
  { id: "regex-tester", name: "Regex Tester", desc: "Test regex with match highlight", cat: "dev" },
  { id: "base64", name: "Base64 Encoder", desc: "Encode/decode text & files", cat: "security" },
  { id: "url-encoder", name: "URL Encoder", desc: "Encode/decode URI parameters", cat: "security" },
  { id: "color-picker", name: "Color Picker", desc: "HEX/RGB/HSL + palette generator", cat: "dev" },
  { id: "gradient", name: "CSS Gradient", desc: "Linear/radial gradient builder", cat: "dev" },
  { id: "box-shadow", name: "Box Shadow", desc: "Shadow generator with sliders", cat: "dev" },
  { id: "qr-code", name: "QR Code Generator", desc: "Generate QR from text/URL", cat: "text" },
  { id: "password", name: "Password Generator", desc: "Strong random passwords", cat: "security" },
  { id: "hash", name: "Hash Generator", desc: "MD5, SHA-256 via Web Crypto", cat: "security" },
  { id: "word-counter", name: "Word Counter", desc: "Count words, chars, reading time", cat: "text" },
  { id: "case-converter", name: "Case Converter", desc: "UPPER, lower, Title, camelCase", cat: "text" },
  { id: "lorem", name: "Lorem Ipsum", desc: "Dummy text generator", cat: "text" },
  { id: "markdown", name: "Markdown to HTML", desc: "Convert Markdown to HTML", cat: "text" },
  { id: "timestamp", name: "Unix Timestamp", desc: "Epoch to date converter", cat: "dev" },
  { id: "image-compressor", name: "Image Compressor", desc: "Compress & resize in browser", cat: "media" },
  { id: "prayer-times", name: "Prayer Times", desc: "Auto prayer schedule by location", cat: "islamic" },
  { id: "qibla", name: "Qibla Finder", desc: "Compass to Ka'bah direction", cat: "islamic" },
  { id: "quran", name: "Digital Al-Qur'an", desc: "Read 30 Juz with translation", cat: "islamic" },
  { id: "tasbih", name: "Digital Tasbih", desc: "Dhikr counter 33/99/100", cat: "islamic" },
  { id: "zakat", name: "Zakat Calculator", desc: "Maal, income, gold, fitrah", cat: "islamic" },
  { id: "asmaul-husna", name: "99 Names of Allah", desc: "Asmaul Husna with audio", cat: "islamic" },
  { id: "hijri", name: "Hijri Converter", desc: "Gregorian to Hijri date", cat: "islamic" },
  { id: "dua-library", name: "Dua Library", desc: "Duas with Arabic & translation", cat: "islamic" },
  { id: "mosque-finder", name: "Mosque Finder", desc: "Find nearby mosques via GPS", cat: "islamic" },
  { id: "arabic-keyboard", name: "Arabic Keyboard", desc: "Virtual Arabic keyboard", cat: "islamic" },
];

const cats = [
  { key: "all", label: "All", icon: Globe },
  { key: "dev", label: "Developer", icon: Code2 },
  { key: "islamic", label: "Islamic", icon: Moon },
  { key: "media", label: "Media", icon: Image },
  { key: "text", label: "Text", icon: FileText },
  { key: "security", label: "Security", icon: Lock },
  { key: "seo", label: "SEO", icon: Globe },
];

export function ToolsGrid({ t, onOpenTool }: { t: (k: string) => string; onOpenTool: (id: string) => void }) {
  const [query, setQuery] = useState("");
  const [cat, setCat] = useState("all");

  const filtered = tools.filter(
    (tool) =>
      (cat === "all" || tool.cat === cat) &&
      (tool.name.toLowerCase().includes(query.toLowerCase()) ||
        tool.desc.toLowerCase().includes(query.toLowerCase()))
  );

  return (
    <section className="mx-auto max-w-7xl px-4 py-12">
      <div className="mb-6 flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <h2 className="font-serif text-2xl font-bold text-slate-900 dark:text-white sm:text-3xl">
            {t("toolsTitle")}
          </h2>
          <p className="mt-1 text-sm text-slate-500 dark:text-slate-400">{t("toolsSub")}</p>
        </div>
        <div className="relative w-full sm:w-72">
          <Search className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-slate-400" />
          <Input
            placeholder={t("search")}
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            className="pl-9"
          />
        </div>
      </div>

      <div className="mb-6 flex flex-wrap gap-2">
        {cats.map((c) => {
          const Icon = c.icon;
          return (
            <button
              key={c.key}
              onClick={() => setCat(c.key)}
              className={`inline-flex items-center gap-1.5 rounded-full px-3 py-1.5 text-xs font-semibold transition ${
                cat === c.key
                  ? "bg-teal-600 text-white shadow-sm"
                  : "bg-slate-100 text-slate-600 hover:bg-slate-200 dark:bg-slate-800 dark:text-slate-300 dark:hover:bg-slate-700"
              }`}
            >
              <Icon className="h-3.5 w-3.5" />
              {c.label}
            </button>
          );
        })}
      </div>

      {filtered.length === 0 ? (
        <div className="rounded-2xl border border-dashed border-slate-300 bg-slate-50 py-16 text-center dark:border-slate-700 dark:bg-slate-900">
          <p className="text-sm text-slate-500 dark:text-slate-400">No tools found.</p>
        </div>
      ) : (
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
          {filtered.map((tool) => (
            <Card
              key={tool.id}
              className="group cursor-pointer border-slate-200 transition hover:-translate-y-0.5 hover:border-teal-300 hover:shadow-md dark:border-slate-800 dark:hover:border-teal-700"
              onClick={() => onOpenTool(tool.id)}
            >
              <CardContent className="p-5">
                <div className="mb-3 flex h-10 w-10 items-center justify-center rounded-xl bg-teal-50 text-teal-600 transition group-hover:bg-teal-600 group-hover:text-white dark:bg-teal-900/40 dark:text-teal-400">
                  <Code2 className="h-5 w-5" />
                </div>
                <h3 className="font-semibold text-slate-900 dark:text-white">{tool.name}</h3>
                <p className="mt-1 text-xs text-slate-500 dark:text-slate-400">{tool.desc}</p>
                <span className="mt-3 inline-block text-xs font-semibold text-teal-600 dark:text-teal-400">
                  {t("open")} →
                </span>
              </CardContent>
            </Card>
          ))}
        </div>
      )}
    </section>
  );
}