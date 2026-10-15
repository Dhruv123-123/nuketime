import { useEffect, useRef, useState } from 'react';
import { marked } from 'marked';
import { JudgeResult, api } from '../api';

export type AiMode = 'hint' | 'explain' | 'debug' | 'review' | 'solve' | 'chat';
interface Msg { role: 'user' | 'assistant'; content: string; mode?: AiMode; streaming?: boolean; error?: string }

const ACTIONS: { mode: AiMode; label: string; title: string; prompt: string }[] = [
  { mode: 'hint', label: '💡 Hint', title: 'One progressive hint (no solution)', prompt: 'Give me a hint.' },
  { mode: 'explain', label: '📖 Explain problem', title: 'Explain what is being asked and walk through example 1', prompt: 'Explain this problem to me.' },
  { mode: 'debug', label: '🐞 Debug my code', title: 'Uses your latest run/submit result', prompt: 'My code is failing. What is wrong?' },
  { mode: 'review', label: '🔍 Review solution', title: 'Complexity, correctness risks, improvements', prompt: 'Review my solution.' },
  { mode: 'solve', label: '🧩 Show solution', title: 'Full solution in your current language', prompt: 'Show me the full solution and explain it.' },
];

marked.setOptions({ gfm: true, breaks: false });

const storageKey = (slug: string) => `lc:ai:${slug}`;

export default function AiPanel({ slug, lang, code, lastResult, onInsertCode }: { slug: string; lang: string; code: string; lastResult: JudgeResult | null; onInsertCode: (code: string) => void }) {
  const [status, setStatus] = useState<{ configured: boolean; model: string } | null>(null);
  const [msgs, setMsgs] = useState<Msg[]>([]);
  const [input, setInput] = useState('');
  const [busy, setBusy] = useState(false);
  const abortRef = useRef<AbortController | null>(null);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => { api.aiStatus().then(setStatus).catch(() => setStatus({ configured: false, model: '' })); }, []);
  useEffect(() => {
    try { const raw = localStorage.getItem(storageKey(slug)); setMsgs(raw ? JSON.parse(raw) : []); } catch { setMsgs([]); }
    abortRef.current?.abort();
    setBusy(false);
  }, [slug]);
  useEffect(() => {
    try { localStorage.setItem(storageKey(slug), JSON.stringify(msgs.filter(m => !m.streaming).slice(-40))); } catch { /* ignore */ }
    bottomRef.current?.scrollIntoView({ block: 'end' });
  }, [msgs, slug]);

  const send = async (mode: AiMode, text: string) => {
    if (busy || !text.trim()) return;
    const hintLevel = msgs.filter(m => m.role === 'user' && m.mode === 'hint').length + 1;
    const history = [...msgs.filter(m => !m.error), { role: 'user' as const, content: text, mode }];
    setMsgs([...history, { role: 'assistant', content: '', streaming: true }]);
    setBusy(true);
    const ac = new AbortController(); abortRef.current = ac;
    let acc = '';
    try {
      await api.aiChat({ slug, lang, code, mode, hintLevel, lastResult, messages: history.map(({ role, content }) => ({ role, content })) }, (ev) => {
        if (ev.delta) { acc += ev.delta; setMsgs(m => [...m.slice(0, -1), { role: 'assistant', content: acc, streaming: true }]); }
        if (ev.error) throw new Error(ev.error);
      }, ac.signal);
      setMsgs(m => [...m.slice(0, -1), { role: 'assistant', content: acc }]);
    } catch (e) {
      const msg = (e as Error).name === 'AbortError' ? 'Stopped.' : (e as Error).message;
      setMsgs(m => [...m.slice(0, -1), { role: 'assistant', content: acc, error: msg }]);
    } finally { setBusy(false); abortRef.current = null; }
  };

  if (status && !status.configured) {
    return (
      <div className="text-sm space-y-3">
        <p className="text-gray-300">The AI assistant is not configured.</p>
        <p className="text-gray-400">Create a <code className="mono">.env</code> file in <code className="mono">leetcode-local/</code> (see <code className="mono">.env.example</code>) with your Azure OpenAI endpoint, key and deployment name, then restart the server.</p>
        <pre className="mono text-xs p-3 rounded" style={{ background: '#1e1e1e' }}>{`AZURE_OPENAI_ENDPOINT=https://<resource>.services.ai.azure.com\nAZURE_OPENAI_API_KEY=...\nAZURE_OPENAI_MODEL=<deployment>`}</pre>
      </div>
    );
  }

  return (
    <div className="h-full flex flex-col text-sm">
      <div className="flex flex-wrap gap-1.5 mb-3">
        {ACTIONS.map(a => (
          <button key={a.mode} className="btn btn-ghost !py-1 !px-2.5 text-xs" title={a.title} disabled={busy || (a.mode === 'debug' && !lastResult)} onClick={() => send(a.mode, a.prompt)}>{a.label}</button>
        ))}
        <div className="flex-1" />
        {msgs.length > 0 && <button className="text-xs text-gray-400 hover:text-white" onClick={() => { abortRef.current?.abort(); setMsgs([]); }}>Clear</button>}
      </div>
      <div className="flex-1 overflow-auto space-y-3 pr-1">
        {msgs.length === 0 && (
          <div className="text-gray-400 text-xs leading-relaxed">
            Ask anything about this problem or your code. The assistant sees the statement, your current code and your latest run result.
            {status?.model && <div className="mt-1 opacity-70">Model: {status.model}</div>}
          </div>
        )}
        {msgs.map((m, i) => (
          <div key={i} className={`rounded-lg px-3 py-2 ${m.role === 'user' ? 'ml-6' : 'mr-2'}`} style={{ background: m.role === 'user' ? '#2f3f5f' : '#1e1e1e' }}>
            {m.role === 'user'
              ? <div className="whitespace-pre-wrap">{m.content}</div>
              : <AssistantMessage content={m.content} streaming={!!m.streaming} error={m.error} onInsertCode={onInsertCode} />}
          </div>
        ))}
        <div ref={bottomRef} />
      </div>
      <form className="mt-3 flex gap-2" onSubmit={e => { e.preventDefault(); const t = input; setInput(''); send('chat', t); }}>
        <input type="text" className="flex-1" placeholder={busy ? 'Thinking…' : 'Ask a question… (Enter to send)'} value={input} onChange={e => setInput(e.target.value)} disabled={busy} />
        {busy
          ? <button type="button" className="btn btn-ghost" onClick={() => abortRef.current?.abort()}>■ Stop</button>
          : <button type="submit" className="btn btn-blue" disabled={!input.trim()}>Send</button>}
      </form>
    </div>
  );
}

function AssistantMessage({ content, streaming, error, onInsertCode }: { content: string; streaming: boolean; error?: string; onInsertCode: (c: string) => void }) {
  const html = marked.parse(content || '') as string;
  const codeBlocks = [...content.matchAll(/```[\w+-]*\n([\s\S]*?)```/g)].map(m => m[1]);
  return (
    <div>
      {content ? <div className="statement ai-md" dangerouslySetInnerHTML={{ __html: html }} /> : streaming ? <span className="pulse text-gray-400">Thinking…</span> : null}
      {streaming && content && <span className="pulse text-gray-500">▍</span>}
      {error && <div className="mt-1 text-xs" style={{ color: '#ffb4b4' }}>{error}</div>}
      {!streaming && codeBlocks.length > 0 && (
        <div className="mt-2 flex gap-2">
          {codeBlocks.map((c, i) => <button key={i} className="btn btn-ghost !py-0.5 text-xs" onClick={() => onInsertCode(c)} title="Replace the editor contents with this code">⤵ Insert code{codeBlocks.length > 1 ? ` ${i + 1}` : ''} into editor</button>)}
        </div>
      )}
    </div>
  );
}
