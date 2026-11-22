import { useEffect, useRef, useState } from "react";
import { Volume2, Play, Pause, Square, X } from "lucide-react";
import { Button } from "@/components/ui/button";

export function AudioBar({ text, onClose }: { text: string | null; onClose: () => void }) {
  const [speaking, setSpeaking] = useState(false);
  const [paused, setPaused] = useState(false);
  const [rate, setRate] = useState(1);
  const utterRef = useRef<SpeechSynthesisUtterance | null>(null);

  useEffect(() => {
    if (!text) return;
    window.speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.rate = rate;
    u.onend = () => setSpeaking(false);
    utterRef.current = u;
    window.speechSynthesis.speak(u);
    setSpeaking(true);
    setPaused(false);
  }, [text]);

  useEffect(() => {
    if (utterRef.current) utterRef.current.rate = rate;
  }, [rate]);

  if (!text) return null;

  const toggle = () => {
    if (paused) {
      window.speechSynthesis.resume();
      setPaused(false);
    } else {
      window.speechSynthesis.pause();
      setPaused(true);
    }
  };

  const stop = () => {
    window.speechSynthesis.cancel();
    setSpeaking(false);
    onClose();
  };

  return (
    <div className="fixed bottom-4 left-1/2 z-50 w-full max-w-2xl -translate-x-1/2 px-4">
      <div className="flex items-center gap-3 rounded-2xl border border-slate-200 bg-white/95 p-3 shadow-lg backdrop-blur dark:border-slate-800 dark:bg-slate-900/95">
        <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-xl bg-teal-600 text-white">
          <Volume2 className="h-4 w-4" />
        </span>
        <div className="min-w-0 flex-1">
          <p className="truncate text-sm font-medium">{text}</p>
          <div className="mt-1 flex items-center gap-2">
            <span className="text-xs text-slate-400">Speed</span>
            <input type="range" min={0.5} max={2} step={0.1} value={rate} onChange={(e) => setRate(Number(e.target.value))} className="w-24" />
            <span className="text-xs text-slate-500">{rate.toFixed(1)}x</span>
          </div>
        </div>
        <Button size="icon" variant="ghost" onClick={toggle} disabled={!speaking}>
          {paused ? <Play className="h-4 w-4" /> : <Pause className="h-4 w-4" />}
        </Button>
        <Button size="icon" variant="ghost" onClick={stop}>
          <Square className="h-4 w-4" />
        </Button>
        <Button size="icon" variant="ghost" onClick={onClose}>
          <X className="h-4 w-4" />
        </Button>
      </div>
    </div>
  );
}