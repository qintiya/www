import { useState, useEffect, useMemo } from "react";
import { Navbar } from "@/components/Navbar";
import { Footer } from "@/components/Footer";
import { Hero } from "@/components/Hero";
import { ToolGrid } from "@/components/ToolGrid";
import { ToolPage } from "@/components/ToolPage";
import { Gallery } from "@/components/Gallery";
import { AdSlot } from "@/components/AdSlot";
import { AudioBar } from "@/components/AudioBar";
import { dictionaries, type Lang } from "@/lib/i18n";

export default function App() {
  const [lang, setLang] = useState<Lang>("en");
  const [dark, setDark] = useState(false);
  const [speakText, setSpeakText] = useState<string | null>(null);
  const [activeTool, setActiveTool] = useState<string | null>(null);

  useEffect(() => {
    const saved = localStorage.getItem("awdev-lang") as Lang | null;
    if (saved) setLang(saved);
    const savedTheme = localStorage.getItem("awdev-theme");
    if (savedTheme === "dark") setDark(true);
  }, []);

  useEffect(() => {
    localStorage.setItem("awdev-lang", lang);
    document.documentElement.dir = lang === "ar" ? "rtl" : "ltr";
    document.documentElement.lang = lang;
  }, [lang]);

  useEffect(() => {
    localStorage.setItem("awdev-theme", dark ? "dark" : "light");
    document.documentElement.classList.toggle("dark", dark);
  }, [dark]);

  const t = useMemo(() => {
    const dict = dictionaries[lang];
    return (key: string) => dict[key] ?? dictionaries.en[key] ?? key;
  }, [lang]);

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900 transition-colors dark:bg-slate-950 dark:text-slate-100">
      <Navbar lang={lang} setLang={setLang} dark={dark} setDark={setDark} t={t} />
      <main>
        {activeTool ? (
          <ToolPage slug={activeTool} onBack={() => setActiveTool(null)} onListen={setSpeakText} t={t} />
        ) : (
          <>
            <Hero t={t} />
            <AdSlot slot="1111111111" label="ADSENSE SLOT 1" />
            <ToolGrid t={t} onListen={setSpeakText} onOpen={setActiveTool} />
            <AdSlot slot="2222222222" label="ADSENSE SLOT 2" />
            <Gallery t={t} />
            <AdSlot slot="3333333333" label="ADSENSE SLOT 3" />
          </>
        )}
      </main>
      <Footer t={t} />
      <AudioBar text={speakText} onClose={() => setSpeakText(null)} />
    </div>
  );
}