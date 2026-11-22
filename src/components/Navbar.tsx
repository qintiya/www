import { useState } from "react";
import { Code2, ChevronDown, Moon, Sun, Globe, Menu, X } from "lucide-react";
import { Button } from "@/components/ui/button";
import type { Lang } from "@/lib/i18n";

type MenuItem = { label: string; items?: string[] };

const menus: MenuItem[] = [
  { label: "home" },
  {
    label: "devTools",
    items: ["Code & Minifier", "CSS Generators", "SEO & DNS", "Text & Security", "Full-Stack Suite", "API Testers"],
  },
  {
    label: "islamicTools",
    items: ["Worship & Prayer", "Al-Qur'an & Dua", "Finance & Zakat", "Islamic Maps & Finder"],
  },
  { label: "media", items: ["Image Gallery (30)", "Video Gallery (30)", "Audio Hub"] },
  { label: "blog", items: ["Tech", "Islamic", "SEO", "Web Dev", "AI & ML", "Career"] },
  { label: "learn", items: ["20 Learning Sites", "24 Ecosystem Partners"] },
  { label: "pages", items: ["About Us", "Contact Us", "Privacy Policy", "Terms & Conditions", "404"] },
];

export function Navbar({
  lang,
  setLang,
  dark,
  setDark,
  t,
}: {
  lang: Lang;
  setLang: (l: Lang) => void;
  dark: boolean;
  setDark: (d: boolean) => void;
  t: (k: string) => string;
}) {
  const [open, setOpen] = useState<string | null>(null);
  const [mobile, setMobile] = useState(false);

  return (
    <header className="sticky top-0 z-50 border-b border-slate-200 bg-white/85 backdrop-blur-md dark:border-slate-800 dark:bg-slate-950/85">
      <div className="mx-auto flex max-w-7xl items-center justify-between gap-4 px-4 py-3">
        <a href="#" className="flex items-center gap-2">
          <span className="flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-br from-teal-500 to-emerald-600 text-white shadow-sm">
            <Code2 className="h-5 w-5" />
          </span>
          <span className="font-serif text-xl font-bold tracking-tight">
            AW<span className="text-teal-600 dark:text-teal-400">DEV</span>
          </span>
        </a>

        <nav className="hidden items-center gap-1 lg:flex">
          {menus.map((menu) => (
            <div
              key={menu.label}
              className="relative"
              onMouseEnter={() => setOpen(menu.label)}
              onMouseLeave={() => setOpen(null)}
            >
              <button className="flex items-center gap-1 rounded-lg px-3 py-2 text-sm font-medium text-slate-600 transition hover:bg-teal-50 hover:text-teal-700 dark:text-slate-300 dark:hover:bg-slate-800">
                {t(menu.label)}
                {menu.items && <ChevronDown className="h-3.5 w-3.5" />}
              </button>
              {menu.items && open === menu.label && (
                <div className="absolute left-0 top-full w-60 rounded-xl border border-slate-200 bg-white p-2 shadow-lg dark:border-slate-800 dark:bg-slate-900">
                  {menu.items.map((item) => (
                    <a
                      key={item}
                      href="#"
                      className="block rounded-lg px-3 py-2 text-sm text-slate-600 transition hover:bg-teal-50 hover:text-teal-700 dark:text-slate-300 dark:hover:bg-slate-800"
                    >
                      {item}
                    </a>
                  ))}
                </div>
              )}
            </div>
          ))}
        </nav>

        <div className="flex items-center gap-2">
          <div className="hidden items-center gap-1 rounded-lg border border-slate-200 p-0.5 sm:flex dark:border-slate-800">
            {(["id", "en", "ar"] as Lang[]).map((l) => (
              <button
                key={l}
                onClick={() => setLang(l)}
                className={`rounded-md px-2 py-1 text-xs font-semibold uppercase transition ${
                  lang === l ? "bg-teal-600 text-white" : "text-slate-500 hover:text-teal-600"
                }`}
              >
                {l}
              </button>
            ))}
          </div>
          <Button variant="ghost" size="icon" onClick={() => setDark(!dark)} aria-label={t("theme")}>
            {dark ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
          </Button>
          <Button variant="ghost" size="icon" className="lg:hidden" onClick={() => setMobile(!mobile)} aria-label="Menu">
            {mobile ? <X className="h-4 w-4" /> : <Menu className="h-4 w-4" />}
          </Button>
        </div>
      </div>

      {mobile && (
        <div className="border-t border-slate-200 bg-white px-4 py-3 lg:hidden dark:border-slate-800 dark:bg-slate-950">
          {menus.map((menu) => (
            <div key={menu.label} className="py-1">
              <p className="px-2 py-1 text-xs font-semibold uppercase tracking-wide text-slate-400">{t(menu.label)}</p>
              {menu.items?.map((item) => (
                <a key={item} href="#" className="block rounded-lg px-3 py-1.5 text-sm text-slate-600 dark:text-slate-300">
                  {item}
                </a>
              ))}
            </div>
          ))}
          <div className="mt-3 flex items-center gap-1">
            <Globe className="h-4 w-4 text-slate-400" />
            {(["id", "en", "ar"] as Lang[]).map((l) => (
              <button
                key={l}
                onClick={() => setLang(l)}
                className={`rounded-md px-2 py-1 text-xs font-semibold uppercase ${
                  lang === l ? "bg-teal-600 text-white" : "text-slate-500"
                }`}
              >
                {l}
              </button>
            ))}
          </div>
        </div>
      )}
    </header>
  );
}