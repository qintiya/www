import { useState } from "react";
import { Copy, Share2, Play, Volume2 } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { toast } from "sonner";

const images = Array.from({ length: 30 }, (_, i) => ({
  id: i + 1,
  title: `Islamic Art ${i + 1}`,
  desc: `Beautiful geometric pattern #${i + 1}`,
  url: `https://picsum.photos/seed/awdev-img-${i + 1}/600/400`,
}));

const videos = Array.from({ length: 30 }, (_, i) => ({
  id: i + 1,
  title: `Video ${i + 1}`,
  desc: `Educational content #${i + 1}`,
  url: `https://picsum.photos/seed/awdev-vid-${i + 1}/600/400`,
}));

export function GallerySection({ t, onListen }: { t: (k: string) => string; onListen: (text: string) => void }) {
  const [tab, setTab] = useState<"images" | "videos">("images");
  const [lightbox, setLightbox] = useState<string | null>(null);

  const copy = (text: string) => {
    navigator.clipboard.writeText(text);
    toast.success(t("copied"));
  };

  const share = async (title: string, url: string) => {
    if (navigator.share) {
      try {
        await navigator.share({ title, url });
      } catch {
        /* cancelled */
      }
    } else {
      copy(url);
    }
  };

  const items = tab === "images" ? images : videos;

  return (
    <section className="bg-slate-100/60 py-12 dark:bg-slate-900/40">
      <div className="mx-auto max-w-7xl px-4">
        <div className="mb-6 flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
          <div>
            <h2 className="font-serif text-2xl font-bold text-slate-900 dark:text-white sm:text-3xl">
              {t("galleryTitle")}
            </h2>
            <p className="mt-1 text-sm text-slate-500 dark:text-slate-400">{t("gallerySub")}</p>
          </div>
          <div className="flex gap-2">
            <button
              onClick={() => setTab("images")}
              className={`rounded-lg px-4 py-2 text-sm font-semibold transition ${
                tab === "images" ? "bg-teal-600 text-white" : "bg-white text-slate-600 dark:bg-slate-800 dark:text-slate-300"
              }`}
            >
              {t("images")} (30)
            </button>
            <button
              onClick={() => setTab("videos")}
              className={`rounded-lg px-4 py-2 text-sm font-semibold transition ${
                tab === "videos" ? "bg-teal-600 text-white" : "bg-white text-slate-600 dark:bg-slate-800 dark:text-slate-300"
              }`}
            >
              {t("videos")} (30)
            </button>
          </div>
        </div>

        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
          {items.map((item) => (
            <Card key={item.id} className="overflow-hidden border-slate-200 dark:border-slate-800">
              <div
                className="relative aspect-video cursor-pointer overflow-hidden bg-slate-200 dark:bg-slate-800"
                onClick={() => setLightbox(item.url)}
              >
                <img src={item.url} alt={item.title} loading="lazy" className="h-full w-full object-cover transition hover:scale-105" />
                {tab === "videos" && (
                  <span className="absolute inset-0 flex items-center justify-center bg-black/30">
                    <span className="flex h-12 w-12 items-center justify-center rounded-full bg-white/90 text-teal-700">
                      <Play className="h-5 w-5" />
                    </span>
                  </span>
                )}
              </div>
              <CardContent className="p-4">
                <h3 className="text-sm font-semibold text-slate-900 dark:text-white">{item.title}</h3>
                <p className="mt-0.5 text-xs text-slate-500 dark:text-slate-400">{item.desc}</p>
                <div className="mt-3 flex gap-1.5">
                  <Button size="sm" variant="outline" className="h-7 px-2 text-xs" onClick={() => share(item.title, item.url)}>
                    <Share2 className="mr-1 h-3 w-3" /> {t("share")}
                  </Button>
                  <Button size="sm" variant="outline" className="h-7 px-2 text-xs" onClick={() => copy(item.url)}>
                    <Copy className="mr-1 h-3 w-3" /> {t("copy")}
                  </Button>
                  <Button size="sm" variant="outline" className="h-7 px-2 text-xs" onClick={() => onListen(item.desc)}>
                    <Volume2 className="h-3 w-3" />
                  </Button>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>

      {lightbox && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 p-4"
          onClick={() => setLightbox(null)}
        >
          <img src={lightbox} alt="preview" className="max-h-full max-w-full rounded-xl" />
        </div>
      )}
    </section>
  );
}