import { useState } from "react";
import { Share2, Copy, X, Play } from "lucide-react";
import { Button } from "@/components/ui/button";
import { toast } from "sonner";

const images = Array.from({ length: 30 }, (_, i) => ({
  id: i + 1,
  title: `Design Showcase ${i + 1}`,
  desc: `A curated interface concept exploring modern layout, colour, and typography for web products.`,
  src: `https://picsum.photos/seed/awdev-img-${i + 1}/800/600`,
}));

const videos = Array.from({ length: 30 }, (_, i) => ({
  id: i + 1,
  title: `Tutorial Video ${i + 1}`,
  desc: `Walkthrough covering practical techniques for building and shipping modern web applications.`,
  src: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
}));

export function Gallery({ t }: { t: (k: string) => string }) {
  const [tab, setTab] = useState<"images" | "videos">("images");
  const [lightbox, setLightbox] = useState<{ src: string; title: string; desc: string } | null>(null);

  const share = async (title: string, url: string) => {
    if (navigator.share) {
      try {
        await navigator.share({ title, url });
      } catch {
        /* cancelled */
      }
    } else {
      window.open(`https://wa.me/?text=${encodeURIComponent(title + " " + url)}`, "_blank");
    }
  };

  const copy = (url: string) => {
    navigator.clipboard.writeText(url);
    toast.success(t("copied"));
  };

  return (
    <section className="mx-auto max-w-7xl px-4 py-16">
      <div className="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <h2 className="font-serif text-3xl font-bold tracking-tight">{t("galleryTitle")}</h2>
          <p className="mt-2 text-sm text-slate-500 dark:text-slate-400">{t("galleryDesc")}</p>
        </div>
        <div className="flex gap-2">
          <button
            onClick={() => setTab("images")}
            className={`rounded-full px-4 py-1.5 text-xs font-semibold transition ${
              tab === "images" ? "bg-teal-600 text-white" : "bg-slate-100 text-slate-600 dark:bg-slate-800 dark:text-slate-300"
            }`}
          >
            {t("images")} (30)
          </button>
          <button
            onClick={() => setTab("videos")}
            className={`rounded-full px-4 py-1.5 text-xs font-semibold transition ${
              tab === "videos" ? "bg-teal-600 text-white" : "bg-slate-100 text-slate-600 dark:bg-slate-800 dark:text-slate-300"
            }`}
          >
            {t("videos")} (30)
          </button>
        </div>
      </div>

      {tab === "images" ? (
        <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
          {images.map((img) => (
            <div key={img.id} className="group overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm transition hover:shadow-md dark:border-slate-800 dark:bg-slate-900">
              <button onClick={() => setLightbox(img)} className="block w-full">
                <img src={img.src} alt={`${img.title} — ${img.desc}`} loading="lazy" className="aspect-video w-full object-cover transition group-hover:scale-105" />
              </button>
              <div className="p-4">
                <h3 className="text-sm font-semibold">{img.title}</h3>
                <p className="mt-1 line-clamp-2 text-xs text-slate-500 dark:text-slate-400">{img.desc}</p>
                <div className="mt-3 flex items-center gap-2">
                  <Button size="sm" variant="outline" onClick={() => share(img.title, img.src)}>
                    <Share2 className="mr-1 h-3.5 w-3.5" /> {t("share")}
                  </Button>
                  <Button size="sm" variant="ghost" onClick={() => copy(img.src)}>
                    <Copy className="mr-1 h-3.5 w-3.5" /> {t("copyLink")}
                  </Button>
                </div>
              </div>
            </div>
          ))}
        </div>
      ) : (
        <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {videos.map((vid) => (
            <div key={vid.id} className="overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm transition hover:shadow-md dark:border-slate-800 dark:bg-slate-900">
              <div className="relative">
                <video controls preload="metadata" className="aspect-video w-full bg-slate-900">
                  <source src={vid.src} type="video/mp4" />
                </video>
                <span className="pointer-events-none absolute left-3 top-3 flex items-center gap-1 rounded-full bg-black/60 px-2 py-1 text-xs text-white">
                  <Play className="h-3 w-3" /> Video
                </span>
              </div>
              <div className="p-4">
                <h3 className="text-sm font-semibold">{vid.title}</h3>
                <p className="mt-1 line-clamp-2 text-xs text-slate-500 dark:text-slate-400">{vid.desc}</p>
                <div className="mt-3 flex items-center gap-2">
                  <Button size="sm" variant="outline" onClick={() => share(vid.title, vid.src)}>
                    <Share2 className="mr-1 h-3.5 w-3.5" /> {t("share")}
                  </Button>
                  <Button size="sm" variant="ghost" onClick={() => copy(vid.src)}>
                    <Copy className="mr-1 h-3.5 w-3.5" /> {t("copyLink")}
                  </Button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      {lightbox && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 p-4" onClick={() => setLightbox(null)}>
          <div className="relative max-w-4xl" onClick={(e) => e.stopPropagation()}>
            <button onClick={() => setLightbox(null)} className="absolute -top-10 right-0 text-white">
              <X className="h-6 w-6" />
            </button>
            <img src={lightbox.src} alt={lightbox.title} className="max-h-[75vh] w-full rounded-2xl object-contain" />
            <div className="mt-4 text-white">
              <h3 className="font-serif text-xl font-bold">{lightbox.title}</h3>
              <p className="mt-1 text-sm text-slate-300">{lightbox.desc}</p>
            </div>
          </div>
        </div>
      )}
    </section>
  );
}