export type Difficulty = 'Easy' | 'Medium' | 'Hard';
export type Status = 'todo' | 'attempted' | 'solved';

export interface ProblemRow {
  id: number; title: string; slug: string; difficulty: Difficulty; tags: string[]; acRate: string | null;
  likes: number | null; dislikes: number | null; status: Status; lastAt?: number;
}
export interface ProblemListResult { items: ProblemRow[]; total: number; page: number; pageSize: number }

export interface MetaParam { name: string; type: string }
export interface MetaData {
  name?: string; params?: MetaParam[]; return?: { type: string };
  classname?: string; constructor?: { params: MetaParam[] }; methods?: { name: string; params: MetaParam[]; return: { type: string } }[]; systemdesign?: boolean;
}
export interface Problem {
  id: number; title: string; slug: string; difficulty: Difficulty; tags: string[]; content: string | null;
  exampleTestcases: string; examples: { input: string; output: string }[]; metaData: MetaData | null;
  codeSnippets: Record<string, string>; hints: string[]; similar: { title: string; slug: string; difficulty: Difficulty; available: boolean }[];
  stats: { acRate: string | null; totalAccepted: number | null; totalSubmissions: number | null }; likes: number | null; dislikes: number | null; url: string;
  progress: ProgressEntry; drafts: Record<string, string>;
  judge: { supported: boolean; reason?: string; design: boolean; anyOrder: boolean; multipleAnswers: boolean };
  exampleTests: { input: string; expected: string | null }[];
  neighbors: { prev: { slug: string; id: number } | null; next: { slug: string; id: number } | null };
}
export interface ProgressEntry { status: Status; solvedAt?: number; attempts?: number; lastLang?: string; lastAt?: number; starred?: boolean; note?: string }

export type TestStatus = 'passed' | 'failed' | 'error' | 'timeout' | 'unchecked' | 'unverified';
export interface TestResult {
  index: number; input: string; stdout: string; expected: string | null; custom: boolean; status: TestStatus;
  output?: unknown; error?: string; ms?: number;
}
export interface JudgeResult {
  status: string; tests: TestResult[]; counts?: Record<TestStatus, number>; runtimeMs?: number; compileError?: string; message?: string;
  stderr?: string; wallMs?: number; submission?: Submission; progress?: ProgressEntry; flags?: { anyOrder: boolean; multipleAnswers: boolean };
}
export interface Submission { id: string; at: number; lang: string; status: string; code: string; runtimeMs?: number; passed: number; total: number }
export interface Language { id: string; name: string; monaco: string; supported: boolean }
export interface Stats { total: Record<Difficulty, number>; solved: Record<Difficulty, number>; attempted: number; solvedTotal: number; totalAll: number; streak: number }
export interface StudyList { id: string; name: string; description: string; count: number; solved: number }
export interface Settings { lang: string; theme: string; fontSize: number }

async function j<T>(url: string, init?: RequestInit): Promise<T> {
  const r = await fetch(url, { headers: { 'Content-Type': 'application/json' }, ...init });
  if (!r.ok) {
    let msg = r.statusText;
    try { msg = (await r.json()).error || msg; } catch { /* ignore */ }
    throw new Error(msg);
  }
  return r.json();
}

export const api = {
  problems: (params: Record<string, string | number | undefined>) => {
    const qs = new URLSearchParams();
    for (const [k, v] of Object.entries(params)) if (v !== undefined && v !== '' && v !== null) qs.set(k, String(v));
    return j<ProblemListResult>(`/api/problems?${qs}`);
  },
  problem: (slug: string) => j<Problem>(`/api/problems/${slug}`),
  random: (params: Record<string, string> = {}) => j<{ slug: string }>(`/api/problems/random?${new URLSearchParams(params)}`),
  submissions: (slug: string) => j<Submission[]>(`/api/problems/${slug}/submissions`),
  saveDraft: (slug: string, lang: string, code: string) => j(`/api/problems/${slug}/draft`, { method: 'PUT', body: JSON.stringify({ lang, code }) }),
  run: (slug: string, lang: string, code: string, testcases?: string) => j<JudgeResult>(`/api/problems/${slug}/run`, { method: 'POST', body: JSON.stringify({ lang, code, testcases }) }),
  submit: (slug: string, lang: string, code: string) => j<JudgeResult>(`/api/problems/${slug}/submit`, { method: 'POST', body: JSON.stringify({ lang, code }) }),
  progress: (slug: string, patch: Partial<ProgressEntry>) => j<ProgressEntry>(`/api/problems/${slug}/progress`, { method: 'POST', body: JSON.stringify(patch) }),
  tags: () => j<{ name: string; count: number }[]>('/api/tags'),
  languages: () => j<Language[]>('/api/languages'),
  lists: () => j<StudyList[]>('/api/lists'),
  stats: () => j<Stats>('/api/stats'),
  recent: () => j<ProblemRow[]>('/api/recent'),
  settings: () => j<Settings>('/api/settings'),
  aiStatus: () => j<{ configured: boolean; model: string }>('/api/ai/status'),
  /** Streams server-sent events from the AI endpoint; onEvent receives {delta}|{done}|{error}. */
  aiChat: async (body: Record<string, unknown>, onEvent: (ev: { delta?: string; done?: boolean; error?: string }) => void, signal?: AbortSignal) => {
    const r = await fetch('/api/ai/chat', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body), signal });
    if (!r.ok || !r.body) { let msg = r.statusText; try { msg = (await r.json()).error || msg; } catch { /* ignore */ } throw new Error(msg); }
    const reader = r.body.getReader(); const dec = new TextDecoder(); let buf = '';
    for (;;) {
      const { value, done } = await reader.read();
      if (done) break;
      buf += dec.decode(value, { stream: true });
      let i: number;
      while ((i = buf.indexOf('\n\n')) >= 0) {
        const line = buf.slice(0, i).trim(); buf = buf.slice(i + 2);
        if (line.startsWith('data:')) { try { onEvent(JSON.parse(line.slice(5))); } catch { /* skip */ } }
      }
    }
  },
  saveSettings: (patch: Partial<Settings>) => j<Settings>('/api/settings', { method: 'PUT', body: JSON.stringify(patch) }),
};
