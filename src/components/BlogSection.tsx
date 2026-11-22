import { Copy, Share2, Volume2 } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { toast } from "sonner";

const posts = [
  { id: 1, cat: "Web Dev", title: "Modern React Patterns in 2025", excerpt: "Explore the latest patterns for building scalable React applications with hooks and server components." },
  { id: 2, cat: "Islamic", title: "Understanding Zakat in the Digital Age", excerpt: "How to calculate and distribute zakat using modern tools and accurate nisab references." },
  { id: 3, cat: "CSS", title: "Mastering CSS Grid & Flexbox", excerpt: "A practical guide to building responsive layouts with modern CSS layout modules." },
  { id: 4, cat: "SEO", title: "Technical SEO Checklist for Developers", excerpt: "Core Web Vitals, structured data, and everything developers need for search visibility." },
  { id: 5, cat: "Fiqh", title: "Prayer Times & Modern Calculation Methods", excerpt: "Comparing astronomical calculation methods used by major Islamic authorities worldwide." },
  { id: 6, cat: "JavaScript", title: "Web Crypto API Deep Dive", excerpt: "Implementing secure hashing and encryption directly in the browser with crypto.subtle." },
];

export function BlogSection({ t, onListen }: { t: (k: string) => string; onListen: (text: string) => void }) {
  const copy = (text: string) => {
    navigator.clipboard.writeText(text);
    toast.success(t("copied"));
  };

  const share = async (title: string) => {
    const url = window.location.href;
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

  return (
    <section className="mx-auto max-w-7xl px-4 py-12">
      <div className="mb-6">
        <h2 className="font-serif text-2xl font-bold text-slate-900 dark:text-white sm:text-3xl">
          {t("blogTitle")}
        </h2>
        <p className="mt-1 text-sm text-slate-500 dark:text-slate-400">{t("blogSub")}</p>
      </div>

      <div className="grid gap-6 lg:grid-cols-3">
        <Card className="overflow-hidden border-slate-200 lg:col-span-2 dark:border-slate-800">
          <div className="aspect-video bg-gradient-to-br from-teal-500 to-emerald-700" />
          <CardContent className="p-6">
            <span className="inline-block rounded-full bg-teal-50 px-2.5 py-0.5 text-xs font-semibold text-teal-700 dark:bg-teal-900/40 dark:text-teal-400">
              {posts[0].cat}
            </span>
            <h3 className="mt-3 font-serif text-xl font-bold text-slate-900 dark:text-white">{posts[0].title}</h3>
            <p className="mt-2 text-sm text-slate-600 dark:text-slate-400">{posts[0].excerpt}</p>
            <div className="mt-4 flex gap-2">
              <Button size="sm" variant="outline" onClick={() => share(posts[0].title)}>
                <Share2 className="mr-1 h-3.5 w-3.5" /> {t("share")}
              </Button>
              <Button size="sm" variant="outline" onClick={() => onListen(posts[0].excerpt)}>
                <Volume2 className="mr-1 h-3.5 w-3.5" /> {t("listen")}
              </Button>
            </div>
          </CardContent>
        </Card>

        <div className="grid gap-4">
          {posts.slice(1, 4).map((post) => (
            <Card key={post.id} className="border-slate-200 dark:border-slate-800">
              <CardContent className="p-4">
                <span className="text-xs font-semibold text-teal-600 dark:text-teal-400">{post.cat}</span>
                <h3 className="mt-1 text-sm font-semibold text-slate-900 dark:text-white">{post.title}</h3>
                <p className="mt-1 line-clamp-2 text-xs text-slate-500 dark:text-slate-400">{post.excerpt}</p>
                <div className="mt-2 flex gap-1.5">
                  <button onClick={() => share(post.title)} className="text-xs text-slate-500 hover:text-teal-600">
                    <Share2 className="h-3.5 w-3.5" />
                  </button>
                  <button onClick={() => onListen(post.excerpt)} className="text-xs text-slate-500 hover:text-teal-600">
                    <Volume2 className="h-3.5 w-3.5" />
                  </button>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>

      <div className="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {posts.slice(4).map((post) => (
          <Card key={post.id} className="border-slate-200 dark:border-slate-800">
            <CardContent className="p-5">
              <span className="text-xs font-semibold text-teal-600 dark:text-teal-400">{post.cat}</span>
              <h3 className="mt-1 font-semibold text-slate-900 dark:text-white">{post.title}</h3>
              <p className="mt-1 text-xs text-slate-500 dark:text-slate-400">{post.excerpt}</p>
            </CardContent>
          </Card>
        ))}
      </div>
    </section>
  );
}