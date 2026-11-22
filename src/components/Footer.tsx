import { Code2, Mail, Globe, Send } from "lucide-react";

export function Footer({ t }: { t: (k: string) => string }) {
  const cols = [
    { title: t("devTools"), links: ["Code Editor", "Minifier", "DNS Checker", "QR Code", "Password Generator"] },
    { title: t("islamicTools"), links: ["Prayer Times", "Qibla Finder", "Al-Qur'an", "Zakat Calculator", "Digital Tasbih"] },
    { title: t("media"), links: ["Image Gallery", "Video Gallery", "Audio Hub"] },
    { title: t("pages"), links: ["About Us", "Contact Us", "Privacy Policy", "Terms & Conditions", "404"] },
  ];

  return (
    <footer className="border-t border-slate-200 bg-white dark:border-slate-800 dark:bg-slate-950">
      <div className="mx-auto grid max-w-7xl gap-8 px-4 py-12 sm:grid-cols-2 lg:grid-cols-5">
        <div className="lg:col-span-1">
          <div className="flex items-center gap-2">
            <span className="flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-br from-teal-500 to-emerald-600 text-white">
              <Code2 className="h-5 w-5" />
            </span>
            <span className="font-serif text-xl font-bold tracking-tight">
              AW<span className="text-teal-600 dark:text-teal-400">DEV</span>
            </span>
          </div>
          <p className="mt-3 text-sm text-slate-500 dark:text-slate-400">
            Full-stack developer tools and Islamic utilities — all in your browser.
          </p>
          <div className="mt-4 flex gap-2">
            <a href="https://github.com" target="_blank" rel="noopener noreferrer" className="rounded-lg border border-slate-200 p-2 text-slate-500 transition hover:text-teal-600 dark:border-slate-800">
              <Globe className="h-4 w-4" />
            </a>
            <a href="https://twitter.com" target="_blank" rel="noopener noreferrer" className="rounded-lg border border-slate-200 p-2 text-slate-500 transition hover:text-teal-600 dark:border-slate-800">
              <Send className="h-4 w-4" />
            </a>
            <a href="mailto:hello@awdev.eu.org" className="rounded-lg border border-slate-200 p-2 text-slate-500 transition hover:text-teal-600 dark:border-slate-800">
              <Mail className="h-4 w-4" />
            </a>
          </div>
        </div>
        {cols.map((col) => (
          <div key={col.title}>
            <h4 className="text-sm font-semibold">{col.title}</h4>
            <ul className="mt-3 space-y-2">
              {col.links.map((link) => (
                <li key={link}>
                  <a href="#" className="text-sm text-slate-500 transition hover:text-teal-600 dark:text-slate-400">
                    {link}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
      <div className="border-t border-slate-200 py-6 text-center text-xs text-slate-400 dark:border-slate-800">
        © {new Date().getFullYear()} AWDEV — awdev.eu.org. All rights reserved.
      </div>
    </footer>
  );
}