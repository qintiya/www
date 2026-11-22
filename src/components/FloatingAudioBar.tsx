import { useEffect, useState } from "react";
import { Volume2, X, Pause, Play } from "lucide-react";

export function FloatingAudioBar({ text, onClose }: { text: string | null; onClose: () => void }) {
  const [speaking, setSpeaking] = useState(false);

  useEffect(() => {
    if (!text) return;
    if ("speechSynthesis" in window) {
      window.speechSynthesis.cancel();
      const utter = new SpeechSynthesisUtterance(text);
      utter.onend = () => setSpeaking(false);
      utter.onstart = () => setSpeaking(true);
      window.speechSynthesis.speak(utter);
      setSpeaking(true);
    }
    return () => {
      if ("speechSynthesis" in window) window.speechSynthesis.cancel();
    };
  }, [text]);

  if (!text) return null;

  const toggle = () => {
    if (!("speechSynthesis" in window)) return;
    if (speaking) {
      window.speechSynthesis.pause();
      setSpeaking(false);
    } else {
      window.speechSynthesis.resume();
      setSpeaking(true);
    }
  };

  return (
    <div className="fixed bottom-4 left-1/2 z-50 flex w-full max-w-xl -translate-x-1/2 items-center gap-3 rounded-2xl border border-slate-200 bg-white/95 px-4 py-3 shadow-xl backdrop-blur dark:border-slate-800 dark:bg-slate-900/95">
      <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-xl bg-teal-100 text-teal-700 dark:bg-teal-900/50 dark:text-teal-400">
        <Volume2 className="h-4 w-4" />
      </span>
      <p className="line-clamp-1 flex-1 text-sm text-slate-700 dark:text-slate-300">{text}</p>
      <button onClick={toggle} className="rounded-lg p-2 text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-800">
        {speaking ? <Pause className="h-4 w-4" /> : <Play className="h-4 w-4" />}
      </button>
      <button onClick={onClose} className="rounded-lg p-2 text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-800">
        <X className="h-4 w-4" />
      </button>
    </div>
  );
}