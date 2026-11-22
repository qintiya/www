import { useState } from "react";
import { ArrowLeft, Volume2, Copy, Play, RefreshCw } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Label } from "@/components/ui/label";
import { toast } from "sonner";

type Props = {
  slug: string;
  onBack: () => void;
  onListen: (text: string) => void;
  t: (k: string) => string;
};

const toolMeta: Record<string, { title: string; desc: string; article: string[]; links: { label: string; url: string }[] }> = {
  "code-editor": {
    title: "Live Code Editor",
    desc: "Write HTML, CSS and JavaScript in a split-screen playground with instant preview.",
    article: [
      "A live code editor is the fastest way to prototype an idea without leaving the browser. AWDEV's editor renders your HTML, CSS and JavaScript in a sandboxed iframe the moment you stop typing, so you can iterate on layout, styling and behaviour in real time.",
      "The editor is split into three panes: markup, styles and scripts. Each pane is independent, which means you can paste a snippet of CSS from a design system and immediately see how it interacts with your existing HTML structure.",
      "Because everything runs client-side, nothing you type is uploaded to a server. This makes the tool safe for experimenting with proprietary snippets, API keys in mock form, or client work under NDA.",
      "When you are happy with the result, click Download HTML to export a single self-contained file that you can drop into any static host — GitHub Pages, Netlify, Cloudflare Pages or a plain S3 bucket.",
      "For deeper work, pair the editor with the Minifier to shrink your output before shipping, and the Beautifier to reformat code you inherited from a teammate.",
    ],
    links: [
      { label: "MDN — HTML reference", url: "https://developer.mozilla.org/en-US/docs/Web/HTML" },
      { label: "MDN — CSS reference", url: "https://developer.mozilla.org/en-US/docs/Web/CSS" },
      { label: "MDN — JavaScript guide", url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript" },
      { label: "Can I use — browser support", url: "https://caniuse.com/" },
      { label: "CodePen — community pens", url: "https://codepen.io/" },
      { label: "JSFiddle — playground", url: "https://jsfiddle.net/" },
      { label: "StackBlitz — full IDE", url: "https://stackblitz.com/" },
    ],
  },
  "dns-checker": {
    title: "DNS Web Checker",
    desc: "Query A, AAAA, MX, TXT and NS records using Google Public DNS.",
    article: [
      "DNS is the phone book of the internet. When a visitor types your domain, a resolver walks a chain of records to find the IP address that should serve the request. A single misconfigured record can take a site offline for hours.",
      "This tool queries Google Public DNS over HTTPS, which means results are consistent regardless of your local resolver cache. You can inspect A records (IPv4), AAAA records (IPv6), MX records (mail routing), TXT records (SPF, DKIM, verification tokens) and NS records (authoritative nameservers).",
      "Use it to verify a migration before you flip the switch: check that the new A record resolves, that MX records still point at your mail provider, and that TXT records for SPF and DMARC are intact.",
      "TXT records are especially useful for debugging email deliverability. A missing SPF record will send your transactional email straight to spam, and a malformed DKIM key will cause signature failures at the receiving end.",
      "For production monitoring, combine this checker with an uptime service and a DNS propagation map so you can see how quickly changes roll out across the globe.",
    ],
    links: [
      { label: "Google Public DNS", url: "https://dns.google/" },
      { label: "Cloudflare DNS docs", url: "https://developers.cloudflare.com/dns/" },
      { label: "ICANN — DNS explained", url: "https://www.icann.org/resources/pages/dns-2012-02-01-en" },
      { label: "MXToolbox — DNS lookup", url: "https://mxtoolbox.com/DNSLookup.aspx" },
      { label: "RFC 1035 — DNS spec", url: "https://www.rfc-editor.org/rfc/rfc1035" },
      { label: "DNSViz — DNSSEC analysis", url: "https://dnsviz.net/" },
      { label: "Let's Encrypt — TLS guide", url: "https://letsencrypt.org/docs/" },
    ],
  },
  "zakat": {
    title: "Zakat Calculator",
    desc: "Calculate Zakat on wealth, income, gold, silver and fitrah using current nisab.",
    article: [
      "Zakat is the third pillar of Islam and one of the most precise financial obligations in the faith. It is a fixed percentage — 2.5% — on wealth that exceeds the nisab threshold and has been held for one lunar year.",
      "The nisab is the minimum amount of wealth that makes a Muslim liable for Zakat. It is measured against 85 grams of gold or 595 grams of silver. Because gold and silver prices fluctuate, the nisab changes daily.",
      "This calculator supports four common forms of Zakat: Zakat al-Maal on savings and investments, Zakat on income, Zakat on gold and silver, and Zakat al-Fitr paid at the end of Ramadan.",
      "Enter your assets — cash, bank balances, gold, silver, stocks, business inventory — and your liabilities, then compare the net figure against the nisab. If you exceed the threshold, 2.5% is due.",
      "For Zakat al-Fitr, the amount is a fixed measure of staple food per person, typically equivalent to a small cash amount in your local currency. Consult a qualified scholar for complex cases involving pensions, crypto or business partnerships.",
    ],
    links: [
      { label: "Islamic Relief — Zakat guide", url: "https://islamic-relief.org/zakat/" },
      { label: "Muslim Aid — Zakat", url: "https://www.muslimaid.org/what-we-do/religious-dues/zakat/" },
      { label: "Aladhan API — prayer times", url: "https://aladhan.com/prayer-times-api" },
      { label: "Quran.com — Surah Al-Tawbah", url: "https://quran.com/9" },
      { label: "Sunnah.com — hadith on Zakat", url: "https://sunnah.com/search?q=zakat" },
      { label: "Zakat Foundation", url: "https://www.zakat.org/" },
      { label: "Islamic Finance — overview", url: "https://www.investopedia.com/terms/i/islamic-finance.asp" },
    ],
  },
};

const fallbackMeta = {
  title: "AWDEV Tool",
  desc: "A free browser-based utility from AWDEV.",
  article: [
    "This tool runs entirely in your browser. No data is uploaded, no account is required, and no tracking scripts are attached to your input.",
    "Every AWDEV utility is designed to be fast, private and offline-friendly. Once the page has loaded, most tools continue to work even if your connection drops.",
    "Use the Listen button to hear a spoken summary of the tool, and the Copy button to grab the result to your clipboard.",
    "For developers, the source of every tool is small enough to audit in a few minutes. If you spot a bug or want a new feature, reach out via the contact page.",
    "Bookmark this page and check back regularly — new tools are added every month based on user requests.",
  ],
  links: [
    { label: "MDN Web Docs", url: "https://developer.mozilla.org/" },
    { label: "web.dev — best practices", url: "https://web.dev/" },
    { label: "Can I use", url: "https://caniuse.com/" },
    { label: "Stack Overflow", url: "https://stackoverflow.com/" },
    { label: "GitHub — open source", url: "https://github.com/" },
    { label: "Dev.to — community", url: "https://dev.to/" },
    { label: "freeCodeCamp", url: "https://www.freecodecamp.org/" },
  ],
};

export function ToolPage({ slug, onBack, onListen, t }: Props) {
  const meta = toolMeta[slug] ?? fallbackMeta;
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");

  const run = () => {
    if (slug === "minifier") {
      setOutput(input.replace(/\/\*[\s\S]*?\*\/|\/\/.*/g, "").replace(/\s+/g, " ").trim());
    } else if (slug === "base64") {
      try {
        setOutput(btoa(unescape(encodeURIComponent(input))));
      } catch {
        setOutput("Invalid input");
      }
    } else if (slug === "url-encoder") {
      setOutput(encodeURIComponent(input));
    } else if (slug === "case-converter") {
      setOutput(input.toUpperCase());
    } else if (slug === "word-counter") {
      const words = input.trim() ? input.trim().split(/\s+/).length : 0;
      setOutput(`Words: ${words} | Characters: ${input.length} | Reading time: ${Math.ceil(words / 200)} min`);
    } else {
      setOutput(input);
    }
  };

  const copy = () => {
    navigator.clipboard.writeText(output || input);
    toast.success(t("copied"));
  };

  return (
    <div className="mx-auto max-w-7xl px-4 py-10">
      <button
        onClick={onBack}
        className="mb-6 inline-flex items-center gap-2 text-sm font-medium text-slate-500 transition hover:text-teal-600 dark:text-slate-400"
      >
        <ArrowLeft className="h-4 w-4" /> Back to tools
      </button>

      <div className="grid gap-8 lg:grid-cols-12">
        <div className="lg:col-span-8">
          <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div className="flex items-start justify-between gap-4">
              <div>
                <h1 className="font-serif text-3xl font-bold tracking-tight">{meta.title}</h1>
                <p className="mt-2 text-sm text-slate-500 dark:text-slate-400">{meta.desc}</p>
              </div>
              <Button variant="outline" size="sm" onClick={() => onListen(`${meta.title}. ${meta.desc}`)}>
                <Volume2 className="mr-1 h-3.5 w-3.5" /> {t("listen")}
              </Button>
            </div>

            <div className="mt-6 space-y-4">
              <div>
                <Label htmlFor="tool-input">Input</Label>
                <Textarea
                  id="tool-input"
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  placeholder="Paste or type your content here..."
                  className="mt-2 min-h-32 font-mono text-sm"
                />
              </div>
              <div className="flex flex-wrap gap-2">
                <Button onClick={run} className="bg-teal-600 hover:bg-teal-700">
                  <Play className="mr-1 h-4 w-4" /> Run
                </Button>
                <Button variant="outline" onClick={() => { setInput(""); setOutput(""); }}>
                  <RefreshCw className="mr-1 h-4 w-4" /> Reset
                </Button>
                <Button variant="outline" onClick={copy}>
                  <Copy className="mr-1 h-4 w-4" /> {t("copy")}
                </Button>
              </div>
              <div>
                <Label htmlFor="tool-output">Output</Label>
                <Textarea
                  id="tool-output"
                  value={output}
                  readOnly
                  placeholder="Result will appear here..."
                  className="mt-2 min-h-32 font-mono text-sm"
                />
              </div>
            </div>
          </div>

          <article className="mt-8 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <h2 className="font-serif text-2xl font-bold tracking-tight">Tutorial: How to use {meta.title}</h2>
            <div className="prose prose-slate mt-4 max-w-none dark:prose-invert">
              {meta.article.map((p, i) => (
                <p key={i} className="mt-4 text-sm leading-relaxed text-slate-600 dark:text-slate-400">
                  {p}
                </p>
              ))}
            </div>
          </article>
        </div>

        <aside className="lg:col-span-4">
          <div className="sticky top-24 space-y-6">
            <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
              <h3 className="text-sm font-semibold uppercase tracking-wide text-slate-400">Table of Contents</h3>
              <ul className="mt-3 space-y-2 text-sm">
                <li><a href="#tool" className="text-teal-700 hover:underline dark:text-teal-400">1. Tool interface</a></li>
                <li><a href="#tutorial" className="text-teal-700 hover:underline dark:text-teal-400">2. Tutorial</a></li>
                <li><a href="#links" className="text-teal-700 hover:underline dark:text-teal-400">3. External resources</a></li>
                <li><a href="#faq" className="text-teal-700 hover:underline dark:text-teal-400">4. FAQ</a></li>
              </ul>
            </div>

            <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
              <h3 className="text-sm font-semibold uppercase tracking-wide text-slate-400">External Resources</h3>
              <ul className="mt-3 space-y-2 text-sm">
                {meta.links.map((link) => (
                  <li key={link.url}>
                    <a
                      href={link.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-teal-700 hover:underline dark:text-teal-400"
                    >
                      {link.label}
                    </a>
                  </li>
                ))}
              </ul>
            </div>

            <div className="rounded-2xl border border-slate-200 bg-teal-50 p-6 shadow-sm dark:border-slate-800 dark:bg-teal-950/40">
              <h3 className="text-sm font-semibold">Related tools</h3>
              <ul className="mt-3 space-y-2 text-sm">
                <li><a href="#" className="text-teal-700 hover:underline dark:text-teal-400">Minifier</a></li>
                <li><a href="#" className="text-teal-700 hover:underline dark:text-teal-400">Beautifier</a></li>
                <li><a href="#" className="text-teal-700 hover:underline dark:text-teal-400">QR Code Generator</a></li>
              </ul>
            </div>
          </div>
        </aside>
      </div>
    </div>
  );
}