import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';
import Editor from '@monaco-editor/react';
import { Panel, PanelGroup, PanelResizeHandle } from 'react-resizable-panels';
import { api, JudgeResult, Language, Problem, Submission, TestResult } from '../api';
import StatusIcon from '../components/StatusIcon';

type LeftTab = 'description' | 'submissions' | 'hints' | 'similar' | 'notes';
type BottomTab = 'testcase' | 'result';

const LS = {
  get: (k: string, d: string) => { try { return localStorage.getItem(k) ?? d; } catch { return d; } },
  set: (k: string, v: string) => { try { localStorage.setItem(k, v); } catch { /* ignore */ } },
};

function paramLabels(p: Problem): string[] {
  const m = p.metaData;
  if (!m) return ['input'];
  if (m.classname || m.systemdesign) return ['operations', 'arguments'];
  return (m.params || []).map(x => x.name);
}

function fmt(v: unknown): string {
  if (v === undefined) return 'undefined';
  if (typeof v === 'string') return JSON.stringify(v);
  try { return JSON.stringify(v); } catch { return String(v); }
}

const STATUS_COLOR: Record<string, string> = {
  Accepted: 'var(--accent)', 'Wrong Answer': 'var(--hard)', 'Runtime Error': 'var(--hard)', 'Compile Error': 'var(--medium)',
  'Time Limit Exceeded': 'var(--medium)', 'Not Judgeable': 'var(--muted)', Finished: '#60a5fa',
};
const statusColor = (s: string) => STATUS_COLOR[s] || (s.startsWith('Finished') ? '#60a5fa' : 'var(--muted)');

export default function ProblemPage() {
  const { slug = '' } = useParams();
  const nav = useNavigate();
  const [problem, setProblem] = useState<Problem | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [languages, setLanguages] = useState<Language[]>([]);
  const [lang, setLang] = useState<string>(LS.get('lc:lang', 'python3'));
  const [code, setCode] = useState('');
  const [fontSize, setFontSize] = useState<number>(Number(LS.get('lc:fontSize', '14')));
  const [leftTab, setLeftTab] = useState<LeftTab>('description');
  const [bottomTab, setBottomTab] = useState<BottomTab>('testcase');
  const [cases, setCases] = useState<string[][]>([]);
  const [activeCase, setActiveCase] = useState(0);
  const [result, setResult] = useState<JudgeResult | null>(null);
  const [activeResult, setActiveResult] = useState(0);
  const [running, setRunning] = useState<'run' | 'submit' | null>(null);
  const [submissions, setSubmissions] = useState<Submission[]>([]);
  const [note, setNote] = useState('');
  const saveTimer = useRef<number | null>(null);
  const codeRef = useRef(code);
  codeRef.current = code;

  // load problem
  useEffect(() => {
    setProblem(null); setResult(null); setError(null); setBottomTab('testcase'); setActiveCase(0);
    api.languages().then(setLanguages);
    api.problem(slug).then(p => {
      setProblem(p);
      setCases(p.exampleTests.map(t => t.input.split('\n')));
      setNote(p.progress.note || '');
      document.title = `${p.id}. ${p.title} · LeetCode Local`;
    }).catch(e => setError(e.message));
  }, [slug]);

  // pick code for current language: draft > snippet
  useEffect(() => {
    if (!problem) return;
    const draft = problem.drafts[lang];
    setCode(draft ?? problem.codeSnippets[lang] ?? `// no starter code for ${lang}`);
  }, [problem, lang]);

  useEffect(() => { if (leftTab === 'submissions' && problem) api.submissions(problem.slug).then(setSubmissions); }, [leftTab, problem]);

  const scheduleSave = useCallback((value: string) => {
    if (!problem) return;
    if (saveTimer.current) window.clearTimeout(saveTimer.current);
    saveTimer.current = window.setTimeout(() => { api.saveDraft(problem.slug, lang, value).catch(() => {}); }, 1200);
  }, [problem, lang]);

  const onCode = (v: string | undefined) => { const val = v ?? ''; setCode(val); scheduleSave(val); };
  const changeLang = (l: string) => {
    if (problem) api.saveDraft(problem.slug, lang, codeRef.current).catch(() => {});
    setLang(l); LS.set('lc:lang', l);
    if (problem) setProblem({ ...problem, drafts: { ...problem.drafts, [lang]: codeRef.current } });
  };
  const resetCode = () => {
    if (!problem) return;
    if (!confirm('Reset the editor to the starter code? Your current code for this language will be discarded.')) return;
    const snip = problem.codeSnippets[lang] ?? '';
    setCode(snip); api.saveDraft(problem.slug, lang, snip).catch(() => {});
  };

  const testcaseText = () => cases.map(c => c.join('\n')).join('\n');

  const run = useCallback(async () => {
    if (!problem || running) return;
    setRunning('run'); setBottomTab('result'); setActiveResult(0);
    try { setResult(await api.run(problem.slug, lang, codeRef.current, testcaseText())); }
    catch (e) { setResult({ status: 'Error', tests: [], message: (e as Error).message }); }
    finally { setRunning(null); }
  }, [problem, lang, running, cases]);

  const submit = useCallback(async () => {
    if (!problem || running) return;
    setRunning('submit'); setBottomTab('result'); setActiveResult(0);
    try {
      const r = await api.submit(problem.slug, lang, codeRef.current);
      setResult(r);
      if (r.progress) setProblem(p => (p ? { ...p, progress: r.progress! } : p));
      window.dispatchEvent(new Event('lc:progress'));
      if (leftTab === 'submissions') api.submissions(problem.slug).then(setSubmissions);
    } catch (e) { setResult({ status: 'Error', tests: [], message: (e as Error).message }); }
    finally { setRunning(null); }
  }, [problem, lang, running, leftTab]);

  // shortcuts: Ctrl+' run, Ctrl+Enter submit
  useEffect(() => {
    const h = (e: KeyboardEvent) => {
      if ((e.ctrlKey || e.metaKey) && e.key === "'") { e.preventDefault(); run(); }
      if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') { e.preventDefault(); submit(); }
    };
    window.addEventListener('keydown', h);
    return () => window.removeEventListener('keydown', h);
  }, [run, submit]);

  const toggleStar = async () => {
    if (!problem) return;
    const pr = await api.progress(problem.slug, { starred: !problem.progress.starred });
    setProblem({ ...problem, progress: pr });
  };
  const saveNote = async () => { if (problem) setProblem({ ...problem, progress: await api.progress(problem.slug, { note }) }); };
  const markStatus = async (status: 'todo' | 'solved') => {
    if (!problem) return;
    setProblem({ ...problem, progress: await api.progress(problem.slug, { status }) });
    window.dispatchEvent(new Event('lc:progress'));
  };

  const labels = useMemo(() => (problem ? paramLabels(problem) : []), [problem]);
  const monacoLang = languages.find(l => l.id === lang)?.monaco || 'plaintext';

  if (error) return <div className="p-8 text-center text-gray-400">Problem not found: {error}. <Link className="text-blue-400" to="/">Back to list</Link></div>;
  if (!problem) return <div className="p-8 text-center text-gray-400 pulse">Loading…</div>;

  const firstFail = result?.tests.find(t => t.status !== 'passed');

  return (
    <div className="h-full flex flex-col">
      {/* top bar */}
      <div className="h-10 shrink-0 flex items-center gap-2 px-3 border-b text-sm" style={{ borderColor: 'var(--border)', background: 'var(--panel)' }}>
        <Link to="/" className="text-gray-300 hover:text-white">☰ Problem List</Link>
        <button className="btn btn-ghost !py-0.5 !px-2" disabled={!problem.neighbors.prev} onClick={() => nav(`/problems/${problem.neighbors.prev!.slug}`)} title="Previous problem">‹</button>
        <button className="btn btn-ghost !py-0.5 !px-2" disabled={!problem.neighbors.next} onClick={() => nav(`/problems/${problem.neighbors.next!.slug}`)} title="Next problem">›</button>
        <div className="flex-1" />
        <button className="btn btn-ghost" onClick={run} disabled={!!running || !problem.judge.supported} title="Ctrl+'">{running === 'run' ? '⏳' : '▶'} Run</button>
        <button className="btn btn-primary" onClick={submit} disabled={!!running || !problem.judge.supported} title="Ctrl+Enter">{running === 'submit' ? '⏳' : '☁'} Submit</button>
        <div className="flex-1" />
        <a href={problem.url} target="_blank" rel="noreferrer" className="text-gray-400 hover:text-white text-xs">Open on LeetCode ↗</a>
      </div>

      <PanelGroup direction="horizontal" className="flex-1 min-h-0">
        {/* LEFT */}
        <Panel defaultSize={45} minSize={25}>
          <div className="h-full flex flex-col" style={{ background: 'var(--panel)' }}>
            <div className="flex border-b overflow-x-auto" style={{ borderColor: 'var(--border)' }}>
              {(['description', 'submissions', 'hints', 'similar', 'notes'] as LeftTab[]).map(t => (
                <div key={t} className={`tab ${leftTab === t ? 'tab-active' : ''}`} onClick={() => setLeftTab(t)}>
                  {t === 'description' ? '📄 Description' : t === 'submissions' ? '🕘 Submissions' : t === 'hints' ? `💡 Hints${problem.hints.length ? ` (${problem.hints.length})` : ''}` : t === 'similar' ? '🔗 Similar' : '📝 Notes'}
                </div>
              ))}
            </div>
            <div className="flex-1 overflow-auto p-4">
              {leftTab === 'description' && (
                <div>
                  <div className="flex items-start gap-2">
                    <h1 className="text-lg font-semibold flex-1">{problem.id}. {problem.title}</h1>
                    <button onClick={toggleStar} className="text-lg" title="Star">{problem.progress.starred ? '⭐' : '☆'}</button>
                  </div>
                  <div className="flex flex-wrap items-center gap-2 mt-2 text-xs">
                    <span className={`chip diff-${problem.difficulty}`}>{problem.difficulty}</span>
                    <span className="chip flex items-center gap-1"><StatusIcon status={problem.progress.status} size={12} /> {problem.progress.status}</span>
                    {problem.stats.acRate && <span className="chip">Acceptance {problem.stats.acRate}</span>}
                    {problem.likes != null && <span className="chip">👍 {problem.likes.toLocaleString()}</span>}
                    {problem.judge.design && <span className="chip">design</span>}
                  </div>
                  {!problem.judge.supported && (
                    <div className="mt-3 p-3 rounded text-xs" style={{ background: '#3a2f1a', color: '#ffd28a' }}>
                      The local judge can't run this problem automatically ({problem.judge.reason}). You can still write and save code here; mark it solved manually when done.
                    </div>
                  )}
                  <div className="statement mt-4" dangerouslySetInnerHTML={{ __html: problem.content || '<p><i>No statement available (premium problem?).</i></p>' }} />
                  <div className="mt-6 pt-4 border-t flex flex-wrap gap-1.5" style={{ borderColor: 'var(--border)' }}>
                    {problem.tags.map(t => <Link key={t} to={`/?tags=${encodeURIComponent(t)}`} className="chip hover:bg-[#4b5563]">{t}</Link>)}
                  </div>
                  <div className="mt-4 flex gap-2 text-xs">
                    {problem.progress.status !== 'solved'
                      ? <button className="btn btn-ghost" onClick={() => markStatus('solved')}>Mark as solved</button>
                      : <button className="btn btn-ghost" onClick={() => markStatus('todo')}>Mark as unsolved</button>}
                  </div>
                </div>
              )}
              {leftTab === 'submissions' && <SubmissionsTab subs={submissions} onLoad={s => { changeLang(s.lang); setCode(s.code); scheduleSave(s.code); }} />}
              {leftTab === 'hints' && (
                <div className="space-y-3">
                  {problem.hints.length === 0 && <p className="text-gray-400 text-sm">No hints for this problem.</p>}
                  {problem.hints.map((h, i) => <Hint key={i} i={i} html={h} />)}
                </div>
              )}
              {leftTab === 'similar' && (
                <ul className="space-y-2 text-sm">
                  {problem.similar.length === 0 && <li className="text-gray-400">No similar problems listed.</li>}
                  {problem.similar.map(s => (
                    <li key={s.slug} className="flex justify-between gap-2">
                      {s.available ? <Link className="hover:text-blue-400" to={`/problems/${s.slug}`}>{s.title}</Link> : <span className="text-gray-500" title="Not available locally (premium?)">{s.title} 🔒</span>}
                      <span className={`diff-${s.difficulty} text-xs`}>{s.difficulty}</span>
                    </li>
                  ))}
                </ul>
              )}
              {leftTab === 'notes' && (
                <div className="h-full flex flex-col gap-2">
                  <textarea className="flex-1 min-h-[300px] w-full resize-none" placeholder="Your notes for this problem (approach, pitfalls, complexity)…" value={note} onChange={e => setNote(e.target.value)} onBlur={saveNote} />
                  <div className="text-xs text-gray-400">Saved automatically when you leave the field.</div>
                </div>
              )}
            </div>
          </div>
        </Panel>
        <PanelResizeHandle className="resize-handle w-1" />

        {/* RIGHT */}
        <Panel defaultSize={55} minSize={30}>
          <PanelGroup direction="vertical">
            <Panel defaultSize={62} minSize={20}>
              <div className="h-full flex flex-col" style={{ background: '#1e1e1e' }}>
                <div className="h-9 shrink-0 flex items-center gap-2 px-2 border-b text-xs" style={{ borderColor: 'var(--border)', background: 'var(--panel)' }}>
                  <span className="text-gray-400">‹/› Code</span>
                  <select value={lang} onChange={e => changeLang(e.target.value)} className="!py-0.5">
                    {languages.map(l => <option key={l.id} value={l.id}>{l.name}</option>)}
                  </select>
                  <div className="flex-1" />
                  <button className="btn btn-ghost !py-0.5" onClick={() => { const s = Math.max(10, fontSize - 1); setFontSize(s); LS.set('lc:fontSize', String(s)); }} title="Smaller font">A−</button>
                  <button className="btn btn-ghost !py-0.5" onClick={() => { const s = Math.min(24, fontSize + 1); setFontSize(s); LS.set('lc:fontSize', String(s)); }} title="Larger font">A+</button>
                  <button className="btn btn-ghost !py-0.5" onClick={resetCode} title="Reset to starter code">↺ Reset</button>
                </div>
                <div className="flex-1 min-h-0">
                  <Editor
                    height="100%"
                    theme="lc-dark"
                    language={monacoLang}
                    path={`${problem.slug}.${lang}`}
                    value={code}
                    onChange={onCode}
                    options={{ fontSize, minimap: { enabled: false }, scrollBeyondLastLine: false, automaticLayout: true, tabSize: lang === 'python3' ? 4 : 4, insertSpaces: true, wordWrap: 'off', renderLineHighlight: 'line', fontFamily: 'ui-monospace, SFMono-Regular, Menlo, Consolas, monospace', fontLigatures: true, padding: { top: 8 } }}
                  />
                </div>
              </div>
            </Panel>
            <PanelResizeHandle className="resize-handle h-1" />
            <Panel defaultSize={38} minSize={15}>
              <div className="h-full flex flex-col" style={{ background: 'var(--panel)' }}>
                <div className="flex items-center border-b" style={{ borderColor: 'var(--border)' }}>
                  <div className={`tab ${bottomTab === 'testcase' ? 'tab-active' : ''}`} onClick={() => setBottomTab('testcase')}>✔ Testcase</div>
                  <div className={`tab ${bottomTab === 'result' ? 'tab-active' : ''}`} onClick={() => setBottomTab('result')}>▶ Test Result</div>
                  <div className="flex-1" />
                  {running && <span className="text-xs text-gray-400 pr-3 pulse">{running === 'run' ? 'Running…' : 'Judging…'}</span>}
                </div>
                <div className="flex-1 overflow-auto p-3">
                  {bottomTab === 'testcase' && (
                    <TestcaseEditor labels={labels} cases={cases} active={activeCase} setActive={setActiveCase} setCases={setCases}
                      onReset={() => { setCases(problem.exampleTests.map(t => t.input.split('\n'))); setActiveCase(0); }} />
                  )}
                  {bottomTab === 'result' && (
                    running && !result ? <div className="text-gray-400 text-sm pulse">Running your code…</div>
                    : !result ? <div className="text-gray-400 text-sm">Run your code to see results here. Shortcuts: <kbd className="mono">Ctrl+'</kbd> run, <kbd className="mono">Ctrl+Enter</kbd> submit.</div>
                    : <ResultView result={result} labels={labels} active={activeResult} setActive={setActiveResult} firstFail={firstFail} />
                  )}
                </div>
              </div>
            </Panel>
          </PanelGroup>
        </Panel>
      </PanelGroup>
    </div>
  );
}

function Hint({ i, html }: { i: number; html: string }) {
  const [open, setOpen] = useState(false);
  return (
    <div className="rounded border" style={{ borderColor: 'var(--border)' }}>
      <button className="w-full text-left px-3 py-2 text-sm font-medium" onClick={() => setOpen(o => !o)}>{open ? '▾' : '▸'} Hint {i + 1}</button>
      {open && <div className="statement px-3 pb-3 text-sm" dangerouslySetInnerHTML={{ __html: html }} />}
    </div>
  );
}

function SubmissionsTab({ subs, onLoad }: { subs: Submission[]; onLoad: (s: Submission) => void }) {
  const [open, setOpen] = useState<string | null>(null);
  if (!subs.length) return <p className="text-gray-400 text-sm">No submissions yet.</p>;
  return (
    <table className="w-full text-sm">
      <thead><tr className="text-xs text-gray-400 text-left"><th className="py-1">Status</th><th>Language</th><th>Runtime</th><th>When</th><th /></tr></thead>
      <tbody>
        {subs.map(s => (
          <>
            <tr key={s.id} className="border-t cursor-pointer hover:bg-[#2f2f2f]" style={{ borderColor: 'var(--border)' }} onClick={() => setOpen(open === s.id ? null : s.id)}>
              <td className="py-2 font-medium" style={{ color: statusColor(s.status) }}>{s.status}<div className="text-[11px] text-gray-400 font-normal">{s.passed}/{s.total} cases</div></td>
              <td>{s.lang}</td>
              <td>{s.runtimeMs != null ? `${s.runtimeMs < 1 ? '<1' : Math.round(s.runtimeMs)} ms` : '—'}</td>
              <td className="text-gray-400 text-xs">{new Date(s.at).toLocaleString()}</td>
              <td><button className="btn btn-ghost !py-0.5 text-xs" onClick={e => { e.stopPropagation(); onLoad(s); }}>Load</button></td>
            </tr>
            {open === s.id && <tr key={s.id + 'c'}><td colSpan={5}><pre className="mono text-xs p-3 rounded overflow-auto max-h-80" style={{ background: '#1e1e1e' }}>{s.code}</pre></td></tr>}
          </>
        ))}
      </tbody>
    </table>
  );
}

function TestcaseEditor({ labels, cases, active, setActive, setCases, onReset }: {
  labels: string[]; cases: string[][]; active: number; setActive: (i: number) => void; setCases: (c: string[][]) => void; onReset: () => void;
}) {
  const cur = cases[active] || [];
  const update = (li: number, v: string) => { const next = cases.map(c => [...c]); next[active][li] = v; setCases(next); };
  const add = () => { if (cases.length >= 12) return; setCases([...cases, [...(cases[active] || labels.map(() => ''))]]); setActive(cases.length); };
  const remove = (i: number) => { if (cases.length <= 1) return; const next = cases.filter((_, k) => k !== i); setCases(next); setActive(Math.max(0, Math.min(active, next.length - 1))); };
  return (
    <div>
      <div className="flex flex-wrap items-center gap-1.5 mb-3">
        {cases.map((_, i) => (
          <span key={i} className={`chip cursor-pointer group ${i === active ? 'chip-active' : ''}`} onClick={() => setActive(i)}>
            Case {i + 1}{cases.length > 1 && <button className="ml-1.5 opacity-40 hover:opacity-100" onClick={e => { e.stopPropagation(); remove(i); }} title="Remove case">✕</button>}
          </span>
        ))}
        <button className="chip hover:bg-[#4b5563]" onClick={add} title="Add a case (copies the current one)">+</button>
        <div className="flex-1" />
        <button className="text-xs text-gray-400 hover:text-white" onClick={onReset}>Reset to examples</button>
      </div>
      <div className="space-y-2">
        {labels.map((label, li) => (
          <div key={li}>
            <div className="text-xs text-gray-400 mb-1">{label} =</div>
            <textarea className="w-full case-input resize-y" rows={1} style={{ minHeight: 32 }} value={cur[li] ?? ''} onChange={e => update(li, e.target.value.replace(/\n/g, ''))} spellCheck={false} />
          </div>
        ))}
      </div>
    </div>
  );
}

function ResultView({ result, labels, active, setActive, firstFail }: { result: JudgeResult; labels: string[]; active: number; setActive: (i: number) => void; firstFail?: TestResult }) {
  const tests = result.tests;
  const t = tests[active];
  const dot = (s: string) => s === 'passed' ? 'var(--accent)' : s === 'unchecked' || s === 'unverified' ? '#60a5fa' : 'var(--hard)';
  const inputLines = t ? t.input.split('\n') : [];
  return (
    <div className="text-sm">
      <div className="flex items-baseline gap-3 mb-2">
        <span className="text-lg font-semibold" style={{ color: statusColor(result.status) }}>{result.status}</span>
        {result.runtimeMs != null && <span className="text-xs text-gray-400">Runtime: {result.runtimeMs < 1 ? '<1' : Math.round(result.runtimeMs)} ms{result.wallMs ? ` · wall ${result.wallMs} ms` : ''}</span>}
        {result.counts && <span className="text-xs text-gray-400">{result.counts.passed}/{tests.length} passed</span>}
      </div>
      {result.message && <div className="p-3 rounded text-xs mb-3" style={{ background: '#3a2f1a', color: '#ffd28a' }}>{result.message}</div>}
      {result.compileError && <pre className="mono text-xs p-3 rounded whitespace-pre-wrap mb-3" style={{ background: '#3b1f1f', color: '#ffb4b4' }}>{result.compileError}</pre>}
      {result.flags?.multipleAnswers && <div className="text-[11px] text-gray-400 mb-2">This problem accepts multiple valid answers, so a mismatch with the example output is shown as “unverified” rather than wrong.</div>}
      {result.flags?.anyOrder && <div className="text-[11px] text-gray-400 mb-2">Order-insensitive comparison enabled (the statement says any order is fine).</div>}
      {tests.length > 0 && (
        <div className="flex flex-wrap gap-1.5 mb-3">
          {tests.map((x, i) => (
            <span key={i} className={`chip cursor-pointer ${i === active ? 'chip-active' : ''}`} onClick={() => setActive(i)}>
              <span className="mr-1.5 inline-block w-2 h-2 rounded-full" style={{ background: dot(x.status) }} />Case {i + 1}
            </span>
          ))}
        </div>
      )}
      {t && (
        <div className="space-y-2">
          {t.error && <pre className="mono text-xs p-3 rounded whitespace-pre-wrap" style={{ background: '#3b1f1f', color: '#ffb4b4' }}>{t.error}</pre>}
          {inputLines.map((line, li) => (
            <Block key={li} label={`Input: ${labels[li] ?? ''} =`} value={line} />
          ))}
          {t.stdout && <Block label="Stdout" value={t.stdout.replace(/\n$/, '')} />}
          {'output' in t && <Block label="Output" value={fmt(t.output)} color={t.status === 'failed' ? 'var(--hard)' : undefined} />}
          {t.expected != null && <Block label={t.status === 'unchecked' ? 'Expected (from statement, not auto-compared)' : t.status === 'unverified' ? 'Example output (multiple answers accepted)' : 'Expected'} value={t.expected} color={t.status === 'passed' ? 'var(--accent)' : undefined} />}
          {t.expected == null && t.status === 'unchecked' && <div className="text-xs text-gray-400">Custom input: no expected output to compare against.</div>}
        </div>
      )}
      {!t && !result.compileError && !result.message && firstFail && <div className="text-xs text-gray-400">See case {firstFail.index + 1}.</div>}
    </div>
  );
}

function Block({ label, value, color }: { label: string; value: string; color?: string }) {
  return (
    <div>
      <div className="text-xs text-gray-400 mb-1">{label}</div>
      <pre className="mono text-xs px-3 py-2 rounded whitespace-pre-wrap break-all" style={{ background: '#1e1e1e', color }}>{value}</pre>
    </div>
  );
}
