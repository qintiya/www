import { useEffect, useRef } from "react";

type AdSlotProps = {
  slot: string;
  label: string;
  format?: "auto" | "fluid" | "autorelaxed";
  layout?: "in-article";
  layoutKey?: string;
  minHeight?: number;
};

declare global {
  interface Window {
    adsbygoogle?: unknown[];
  }
}

export function AdSlot({
  slot,
  label,
  format = "auto",
  layout,
  layoutKey,
  minHeight = 100,
}: AdSlotProps) {
  const pushed = useRef(false);

  useEffect(() => {
    if (pushed.current) return;
    pushed.current = true;
    try {
      (window.adsbygoogle = window.adsbygoogle || []).push({});
    } catch {
      /* AdSense not loaded yet */
    }
  }, []);

  return (
    <div className="mx-auto max-w-7xl px-4 py-6">
      {/* {label} */}
      <div
        className="relative flex items-center justify-center overflow-hidden rounded-2xl border border-dashed border-slate-300 bg-slate-100/60 dark:border-slate-700 dark:bg-slate-900/60"
        style={{ minHeight }}
      >
        <ins
          className="adsbygoogle"
          style={{ display: "block", width: "100%" }}
          data-ad-client="ca-pub-5407249785989200"
          data-ad-slot={slot}
          data-ad-format={format}
          data-ad-layout={layout}
          data-ad-layout-key={layoutKey}
          data-full-width-responsive="true"
        />
        <span className="pointer-events-none absolute text-xs font-medium uppercase tracking-wider text-slate-400">
          {label}
        </span>
      </div>
    </div>
  );
}