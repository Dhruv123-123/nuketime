import express from 'express';
import path from 'node:path';
import fs from 'node:fs';
import { fileURLToPath } from 'node:url';
import { loadProblems, allProblems, getProblem, getTags, queryProblems, randomProblem, summarize, problemText, DATA_DIR } from './problems.js';
import * as store from './store.js';
import { runJudge } from './judge/index.js';
import { buildExampleTests, buildCustomTests, judgeSupport, isDesign } from './judge/testcases.js';
import { LANGUAGE_LIST, getLanguage } from './judge/langs/index.js';
import { problemFlags } from './judge/compare.js';
import { STUDY_LISTS } from './lists.js';
import { aiConfig, buildSystemPrompt, streamChat } from './ai.js';


const __dirname = path.dirname(fileURLToPath(import.meta.url));
// Load .env from the project root (or the server dir) without a dependency.
for (const f of [path.resolve(__dirname, '../../.env'), path.resolve(__dirname, '../.env')]) {
  try { process.loadEnvFile(f); break; } catch { /* no .env there */ }
}
const PORT = Number(process.env.PORT || 3000);
const app = express();
app.set('trust proxy', true);

// ---------- optional password gate (set APP_PASSWORD when exposing this to the internet) ----------
// Anyone who can reach the app can run code on this machine and use your AI key, so
// never host it publicly without a password.
const APP_PASSWORD = process.env.APP_PASSWORD || '';
const APP_USER = process.env.APP_USER || 'admin';
app.get('/api/health', (req, res) => res.json({ ok: true, problems: allProblems().length, uptime: Math.round(process.uptime()) }));
if (APP_PASSWORD) {
  app.use((req, res, next) => {
    const h = req.headers.authorization || '';
    if (h.startsWith('Basic ')) {
      const [u, ...rest] = Buffer.from(h.slice(6), 'base64').toString('utf8').split(':');
      if (u === APP_USER && rest.join(':') === APP_PASSWORD) return next();
    }
    res.setHeader('WWW-Authenticate', 'Basic realm="leetcode-local", charset="UTF-8"');
    res.status(401).send('Authentication required');
  });
} else if (process.env.NODE_ENV === 'production') {
  console.warn('[security] APP_PASSWORD is not set: anyone who can reach this server can run code and use your AI key.');
}

app.use(express.json({ limit: '2mb' }));
app.use('/images', express.static(path.join(DATA_DIR, 'images'), { maxAge: '30d' }));

const n = loadProblems();
console.log(`[problems] loaded ${n} problems from ${DATA_DIR}`);

const lists = STUDY_LISTS.map(l => ({ ...l, slugs: [...new Set(l.slugs)].filter(s => getProblem(s)) }));

const parseList = v => (v ? String(v).split(',').map(s => s.trim()).filter(Boolean) : []);

// ---------- problems ----------
app.get('/api/problems', (req, res) => {
  const q = req.query;
  let ids = null;
  if (q.list) { const l = lists.find(x => x.id === q.list); if (l) ids = new Set(l.slugs); }
  const result = queryProblems({
    q: q.q || '', difficulty: parseList(q.difficulty), tags: parseList(q.tags), status: q.status || '',
    statusOf: store.statusOf, sort: q.sort || 'id', order: q.order || 'asc',
    page: Math.max(1, Number(q.page) || 1), pageSize: Math.min(200, Math.max(1, Number(q.pageSize) || 50)), ids,
  });
  res.json(result);
});

app.get('/api/problems/random', (req, res) => {
  const p = randomProblem({ difficulty: parseList(req.query.difficulty), tags: parseList(req.query.tags), statusOf: store.statusOf, unsolvedOnly: req.query.unsolved === '1' });
  if (!p) return res.status(404).json({ error: 'no problems match' });
  res.json({ slug: p.slug });
});

app.get('/api/problems/:slug', (req, res) => {
  const p = getProblem(req.params.slug);
  if (!p) return res.status(404).json({ error: 'not found' });
  const support = judgeSupport(p.metaData, p);
  const flags = problemFlags(problemText(p), p.metaData);
  res.json({
    ...p,
    similar: (p.similar || []).map(s => ({ ...s, available: !!getProblem(s.slug) })),
    progress: store.entry(p.slug),
    drafts: store.drafts(p.slug),
    judge: { ...support, design: isDesign(p.metaData), anyOrder: flags.anyOrder, multipleAnswers: flags.multipleAnswers },
    exampleTests: buildExampleTests(p).map(t => ({ input: t.raw, expected: t.expected })),
    neighbors: neighbors(p),
  });
});

function neighbors(p) {
  const all = allProblems();
  const i = all.findIndex(x => x.slug === p.slug);
  return { prev: i > 0 ? { slug: all[i - 1].slug, id: all[i - 1].id } : null, next: i < all.length - 1 ? { slug: all[i + 1].slug, id: all[i + 1].id } : null };
}

app.get('/api/problems/:slug/submissions', (req, res) => res.json(store.submissions(req.params.slug)));

app.put('/api/problems/:slug/draft', (req, res) => {
  const { lang, code } = req.body || {};
  if (!getProblem(req.params.slug) || !lang || typeof code !== 'string') return res.status(400).json({ error: 'bad request' });
  store.saveDraft(req.params.slug, lang, code);
  res.json({ ok: true });
});

app.post('/api/problems/:slug/progress', (req, res) => {
  const p = getProblem(req.params.slug);
  if (!p) return res.status(404).json({ error: 'not found' });
  const patch = {};
  if (req.body.status && ['todo', 'attempted', 'solved'].includes(req.body.status)) { patch.status = req.body.status; if (req.body.status === 'solved') patch.solvedAt = patch.solvedAt || Date.now(); }
  if (typeof req.body.starred === 'boolean') patch.starred = req.body.starred;
  if (typeof req.body.note === 'string') patch.note = req.body.note;
  res.json(store.setEntry(p.slug, patch));
});

// ---------- run / submit ----------
async function judgeRequest(req, res, isSubmit) {
  const p = getProblem(req.params.slug);
  if (!p) return res.status(404).json({ error: 'not found' });
  const { lang, code, testcases } = req.body || {};
  if (!getLanguage(lang)) return res.status(400).json({ error: `unsupported language ${lang}` });
  if (typeof code !== 'string') return res.status(400).json({ error: 'code required' });
  let tests;
  if (!isSubmit && typeof testcases === 'string' && testcases.trim()) {
    tests = buildCustomTests(testcases, p);
    // Reuse expected outputs for custom inputs that match the examples verbatim.
    const ex = buildExampleTests(p);
    for (const t of tests) { const m = ex.find(e => e.raw === t.raw); if (m) t.expected = m.expected; }
  } else tests = buildExampleTests(p);
  const t0 = Date.now();
  const result = await runJudge({ problem: p, langId: lang, code, tests });
  result.wallMs = Date.now() - t0;
  if (isSubmit) {
    store.saveDraft(p.slug, lang, code);
    const rec = store.recordSubmission(p.slug, { lang, status: result.status, code, runtimeMs: result.runtimeMs, counts: result.counts, passed: result.counts?.passed || 0, total: result.tests.length, wallMs: result.wallMs });
    result.submission = rec;
    result.progress = store.entry(p.slug);
  }
  res.json(result);
}
app.post('/api/problems/:slug/run', (req, res) => judgeRequest(req, res, false));
app.post('/api/problems/:slug/submit', (req, res) => judgeRequest(req, res, true));

// ---------- AI assistant ----------
app.get('/api/ai/status', (req, res) => { const c = aiConfig(); res.json({ configured: c.configured, model: c.model, reasoning: c.reasoning }); });

app.post('/api/ai/chat', async (req, res) => {
  const { slug, lang = 'python3', code = '', mode = 'chat', messages = [], lastResult = null, hintLevel = 1 } = req.body || {};
  const p = getProblem(slug);
  if (!p) return res.status(404).json({ error: 'not found' });
  if (!Array.isArray(messages) || !messages.length) return res.status(400).json({ error: 'messages required' });
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('X-Accel-Buffering', 'no');
  res.flushHeaders?.();
  const send = obj => res.write(`data: ${JSON.stringify(obj)}\n\n`);
  const ac = new AbortController();
  res.on('close', () => { if (!res.writableFinished) ac.abort(); });
  try {
    const system = buildSystemPrompt({ problem: p, lang, code, mode, lastResult, hintLevel });
    for await (const ev of streamChat({ system, messages, signal: ac.signal })) send(ev);
  } catch (e) {
    if (!ac.signal.aborted) send({ error: e.message });
  }
  res.end();
});

// ---------- misc ----------
app.get('/api/tags', (req, res) => res.json(getTags()));
app.get('/api/languages', (req, res) => res.json(LANGUAGE_LIST));
app.get('/api/lists', (req, res) => res.json(lists.map(l => ({ id: l.id, name: l.name, description: l.description, count: l.slugs.length, solved: l.slugs.filter(s => store.statusOf(s) === 'solved').length }))));
app.get('/api/stats', (req, res) => res.json(store.stats(allProblems())));
app.get('/api/settings', (req, res) => res.json(store.getSettings()));
app.put('/api/settings', (req, res) => res.json(store.setSettings(req.body || {})));
app.get('/api/recent', (req, res) => {
  const rows = Object.entries(store.allProgress()).filter(([, e]) => e.lastAt).sort((a, b) => b[1].lastAt - a[1].lastAt).slice(0, 10)
    .map(([slug, e]) => { const p = getProblem(slug); return p ? { ...summarize(p, e.status), lastAt: e.lastAt } : null; }).filter(Boolean);
  res.json(rows);
});
app.post('/api/reload', (req, res) => res.json({ loaded: loadProblems() }));

// ---------- static frontend (production build) ----------
const dist = path.resolve(__dirname, '../../web/dist');
if (fs.existsSync(dist)) {
  app.use(express.static(dist));
  app.get(/^(?!\/api\/).*/, (req, res) => res.sendFile(path.join(dist, 'index.html')));
} else {
  app.get('/', (req, res) => res.type('text').send('leetcode-local API is running. Build the web app (npm run build) or run the Vite dev server (npm run dev).'));
}

app.use((err, req, res, next) => { // eslint-disable-line no-unused-vars
  console.error(err);
  res.status(500).json({ error: err.message || 'internal error' });
});

app.listen(PORT, () => console.log(`leetcode-local listening on http://localhost:${PORT}`));
