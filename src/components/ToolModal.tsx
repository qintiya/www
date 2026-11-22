import { useState } from "react";
import { X, Copy } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Label } from "@/components/ui/label";
import { toast } from "sonner";

export function ToolModal({ toolId, onClose, t }: { toolId: string; onClose: () => void; t: (k: string) => string }) {
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");

  const copy = () => {
    navigator.clipboard.writeText(output);
    toast.success(t("copied"));
  };

  const run = () => {
    try {
      switch (toolId) {
        case "base64":
          setOutput(btoa(unescape(encodeURIComponent(input))));
          break;
        case "url-encoder":
          setOutput(encodeURIComponent(input));
          break;
        case "minifier":
          setOutput(input.replace(/\s+/g, " ").replace(/\/\*[\s\S]*?\*\//g, "").trim());
          break;
        case "case-converter":
          setOutput(input.toUpperCase());
          break;
        case "word-counter": {
          const words = input.trim() ? input.trim().split(/\s+/).length : 0;
          setOutput(`Words: ${words} | Chars: ${input.length} | Reading: ${Math.ceil(words / 200)} min`);
          break;
        }
        case "lorem":
          setOutput("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.");
          break;
        case "markdown":
          setOutput(input.replace(/^# (.*)$/gm, "<h1>$1</h1>").replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>").replace(/\*(.*?)\*/g, "<em>$1</em>"));
          break;
        case "timestamp":
          setOutput(new Date(Number(input) * 1000).toISOString());
          break;
        case "json-validator":
          JSON.parse(input);
          setOutput("✓ Valid JSON\n" + JSON.stringify(JSON.parse(input), null, 2));
          break;
        case "regex-tester": {
          const re = new RegExp(input, "g");
          setOutput("Pattern compiled successfully.");
          break;
        }
        case "password": {
          const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*";
          let pwd = "";
          for (let i = 0; i < 16; i++) pwd += chars[Math.floor(Math.random() * chars.length)];
          setOutput(pwd);
          break;
        }
        case "hash":
          crypto.subtle.digest("SHA-256", new TextEncoder().encode(input)).then((buf) => {
            const hash = Array.from(new Uint8Array(buf)).map((b) => b.toString(16).padStart(2, "0")).join("");
            setOutput(hash);
          });
          break;
        default:
          setOutput("Tool output will appear here. Enter input and click Run.");
      }
    } catch (e) {
      setOutput("Error: " + (e as Error).message);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4" onClick={onClose}>
      <div
        className="max-h-[90vh] w-full max-w-2xl overflow-y-auto rounded-2xl border border-slate-200 bg-white p-6 shadow-2xl dark:border-slate-800 dark:bg-slate-900"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="mb-4 flex items-center justify-between">
          <h2 className="font-serif text-xl font-bold capitalize text-slate-900 dark:text-white">
            {toolId.replace(/-/g, " ")}
          </h2>
          <button onClick={onClose} className="rounded-lg p-2 text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-800">
            <X className="h-5 w-5" />
          </button>
        </div>

        <div className="space-y-4">
          <div>
            <Label>Input</Label>
            <Textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Enter your input here..."
              className="mt-1 min-h-32"
            />
          </div>
          <div className="flex gap-2">
            <Button onClick={run} className="bg-teal-600 text-white hover:bg-teal-700">
              Run Tool
            </Button>
            <Button variant="outline" onClick={copy}>
              <Copy className="mr-1 h-4 w-4" /> {t("copy")}
            </Button>
          </div>
          <div>
            <Label>Output</Label>
            <pre className="mt-1 max-h-64 overflow-auto rounded-xl border border-slate-200 bg-slate-50 p-4 text-sm text-slate-800 dark:border-slate-800 dark:bg-slate-950 dark:text-slate-200">
              {output || "Output will appear here..."}
            </pre>
          </div>
        </div>
      </div>
    </div>
  );
}