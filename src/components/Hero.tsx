import { ArrowRight, Sparkles, Zap, Shield, BookOpen } from "lucide-react";
import { Button } from "@/components/ui/button";

export function Hero({ t }: { t: (k: string) => string }) {
  const stats = [
    { label: t("statTools"), value: "70+" },
    { label: t("statArticles"), value: "900" },
    { label: t("statCategories"), value: "30" },
    { label: t("statPartners"), value: "44" },
  ];

  return (
    <section className="relative overflow-hidden border-b border-slate-200 bg-gradient-to-br from-teal-50 via-emerald-50 to-slate-50 dark:border-slate-800 dark:from-slate-900 dark:via-slate-900 dark:to-slate-950">
      <div className="absolute -right-24 -top-24 h-72 w-72 rounded-full bg-teal-200/40 blur-3xl dark:bg-teal-900/30" />
      <div className="absolute -bottom-32 -left-24 h-80 w-80 rounded-full bg-emerald-200/40 blur-3xl dark:bg-emerald-900/20" />

      <div className="relative mx-auto grid max-w-7xl gap-10 px-4 py-16 lg:grid-cols-12 lg:py-24">
        <div className="lg:col-span-7">
          <span className="inline-flex items-center gap-2 rounded-full border border-teal-200 bg-white/70 px-3 py-1 text-xs font-semibold text-teal-700 backdrop-blur dark:border-teal-800 dark:bg-slate-900/70 dark:text-teal-300">
            <Sparkles className="h-3.5 w-3.5" /> awdev.eu.org
          </span>
          <h1 className="mt-5 font-serif text-4xl font-bold leading-tight tracking-tight sm:text-5xl lg:text-6xl">
            {t("heroTitle")}
          </h1>
          <p className="mt-5 max-w-2xl text-base leading-relaxed text-slate-600 dark:text-slate-400">
            {t("heroSubtitle")}
          </p>
          <div className="mt-8 flex flex-wrap gap-3">
            <Button size="lg" className="bg-teal-600 hover:bg-teal-700">
              {t("heroCta")} <ArrowRight className="ml-2 h-4 w-4" />
            </Button>
            <Button size="lg" variant="outline">
              {t("heroCta2")}
            </Button>
          </div>

          <div className="mt-10 grid grid-cols-2 gap-4 sm:grid-cols-4">
            {stats.map((s) => (
              <div key={s.label} className="rounded-xl border border-slate-200 bg-white/70 p-3 backdrop-blur dark:border-slate-800 dark:bg-slate-900/70">
                <p className="font-serif text-2xl font-bold text-teal-700 dark:text-teal-400">{s.value}</p>
                <p className="text-xs text-slate-500 dark:text-slate-400">{s.label}</p>
              </div>
            ))}
          </div>
        </div>

        <div className="lg:col-span-5">
          <div className="grid gap-4">
            {[
              { icon: Zap, title: t("fullstack"), desc: t("fullstackDesc"), tint: "from-teal-500 to-emerald-600" },
              { icon: Shield, title: "Privacy First", desc: "Every tool runs in your browser. No uploads, no tracking, no accounts.", tint: "from-emerald-500 to-green-600" },
              { icon: BookOpen, title: "Islamic Utilities", desc: "Prayer times, Qibla, Qur'an, Zakat, Tasbih and more — built with care.", tint: "from-cyan-500 to-teal-600" },
            ].map((card) => {
              const Icon = card.icon;
              return (
                <div key={card.title} className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm transition hover:shadow-md dark:border-slate-800 dark:bg-slate-900">
                  <div className="flex items-start gap-4">
                    <span className={`flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-gradient-to-br ${card.tint} text-white`}>
                      <Icon className="h-5 w-5" />
                    </span>
                    <div>
                      <h3 className="text-sm font-semibold">{card.title}</h3>
                      <p className="mt-1 text-sm text-slate-500 dark:text-slate-400">{card.desc}</p>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </section>
  );
}