// Loads scraped problems from data/problems/*.json into memory and exposes
// list / detail / tag queries.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
export const DATA_DIR = process.env.LC_DATA_DIR || path.resolve(__dirname, '../../data');
const PROBLEMS_DIR = path.join(DATA_DIR, 'problems');

let problems = [];          // full records, sorted by id
let bySlug = new Map();
let tagCounts = new Map();

const TEXT_CACHE = new Map();

export function stripHtml(html) {
  if (!html) return '';
  return html
    .replace(/<\s*(br|\/p|\/pre|\/div|\/li|\/tr)\s*\/?>/gi, '\n')
    .replace(/<[^>]+>/g, '')
    .replace(/&nbsp;/g, ' ')
    .replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&amp;/g, '&');
}

export function problemText(p) {
  let t = TEXT_CACHE.get(p.slug);
  if (t === undefined) { t = stripHtml(p.content).toLowerCase(); TEXT_CACHE.set(p.slug, t); }
  return t;
}

let imageIndex = {};
function localizeImages(html) {
  if (!html) return html;
  return html.replace(/<img([^>]+)src="([^"]+)"/g, (m, pre, url) => {
    const f = imageIndex[url];
    return f ? `<img${pre}src="/images/${f}" data-src="${url}"` : m;
  });
}

export function loadProblems() {
  try { imageIndex = JSON.parse(fs.readFileSync(path.join(DATA_DIR, 'images.json'), 'utf8')); } catch { imageIndex = {}; }
  if (!fs.existsSync(PROBLEMS_DIR)) {
    console.warn(`[problems] ${PROBLEMS_DIR} does not exist. Run: npm run scrape`);
    problems = []; bySlug = new Map(); tagCounts = new Map();
    return 0;
  }
  const files = fs.readdirSync(PROBLEMS_DIR).filter(f => f.endsWith('.json'));
  const out = [];
  for (const f of files) {
    try {
      const p = JSON.parse(fs.readFileSync(path.join(PROBLEMS_DIR, f), 'utf8'));
      if (!p.slug) continue;
      p.content = localizeImages(p.content);
      out.push(p);
    } catch (e) {
      console.warn(`[problems] failed to parse ${f}: ${e.message}`);
    }
  }
  out.sort((a, b) => a.id - b.id);
  problems = out;
  bySlug = new Map(out.map(p => [p.slug, p]));
  tagCounts = new Map();
  for (const p of out) for (const t of p.tags || []) tagCounts.set(t, (tagCounts.get(t) || 0) + 1);
  TEXT_CACHE.clear();
  return out.length;
}

export function allProblems() { return problems; }
export function getProblem(slug) { return bySlug.get(slug); }
export function getTags() {
  return [...tagCounts.entries()].map(([name, count]) => ({ name, count })).sort((a, b) => b.count - a.count);
}

// Lightweight row for the problem table.
export function summarize(p, status) {
  return {
    id: p.id,
    title: p.title,
    slug: p.slug,
    difficulty: p.difficulty,
    tags: p.tags || [],
    acRate: p.stats?.acRate || null,
    likes: p.likes ?? null,
    dislikes: p.dislikes ?? null,
    status: status || 'todo',
  };
}

/**
 * Query the in-memory problem set.
 * opts: { q, difficulty: ['Easy'], tags: ['Array'], status, statusOf(slug)->status, sort, order, page, pageSize, ids:Set }
 */
export function queryProblems(opts) {
  const { q = '', difficulty = [], tags = [], status = '', statusOf = () => 'todo', sort = 'id', order = 'asc', page = 1, pageSize = 50, ids = null } = opts;
  const ql = q.trim().toLowerCase();
  const qId = /^\d+$/.test(ql) ? Number(ql) : null;
  let rows = problems.filter(p => {
    if (ids && !ids.has(p.slug)) return false;
    if (difficulty.length && !difficulty.includes(p.difficulty)) return false;
    if (tags.length && !tags.every(t => (p.tags || []).includes(t))) return false;
    if (ql) {
      if (qId !== null) { if (p.id !== qId && !p.title.toLowerCase().includes(ql)) return false; }
      else if (!p.title.toLowerCase().includes(ql) && !p.slug.includes(ql)) return false;
    }
    if (status && statusOf(p.slug) !== status) return false;
    return true;
  });
  const dir = order === 'desc' ? -1 : 1;
  const diffRank = { Easy: 0, Medium: 1, Hard: 2 };
  const acNum = p => parseFloat(p.stats?.acRate || '0');
  const sorters = {
    id: (a, b) => (a.id - b.id) * dir,
    title: (a, b) => a.title.localeCompare(b.title) * dir,
    difficulty: (a, b) => ((diffRank[a.difficulty] - diffRank[b.difficulty]) || (a.id - b.id)) * dir,
    acceptance: (a, b) => ((acNum(a) - acNum(b)) || (a.id - b.id)) * dir,
    likes: (a, b) => (((a.likes || 0) - (b.likes || 0)) || (a.id - b.id)) * dir,
  };
  rows.sort(sorters[sort] || sorters.id);
  const total = rows.length;
  const start = (page - 1) * pageSize;
  const items = rows.slice(start, start + pageSize).map(p => summarize(p, statusOf(p.slug)));
  return { items, total, page, pageSize };
}

export function randomProblem(filter = {}) {
  const { difficulty = [], tags = [], statusOf = () => 'todo', unsolvedOnly = false } = filter;
  const pool = problems.filter(p =>
    (!difficulty.length || difficulty.includes(p.difficulty)) &&
    (!tags.length || tags.every(t => (p.tags || []).includes(t))) &&
    (!unsolvedOnly || statusOf(p.slug) !== 'solved'));
  if (!pool.length) return null;
  return pool[Math.floor(Math.random() * pool.length)];
}
