// Per-user state kept as plain JSON files under data/user (no database needed).
import fs from 'node:fs';
import path from 'node:path';
import { DATA_DIR } from './problems.js';

// Persistent user state. Point LC_USER_DIR at a mounted volume when hosting online.
const USER_DIR = process.env.LC_USER_DIR ? path.resolve(process.env.LC_USER_DIR) : path.join(DATA_DIR, 'user');
const PROGRESS = path.join(USER_DIR, 'progress.json');
const SUBS_DIR = path.join(USER_DIR, 'submissions');
const DRAFTS_DIR = path.join(USER_DIR, 'drafts');
const SETTINGS = path.join(USER_DIR, 'settings.json');

for (const d of [USER_DIR, SUBS_DIR, DRAFTS_DIR]) fs.mkdirSync(d, { recursive: true });

function readJson(file, fallback) {
  try { return JSON.parse(fs.readFileSync(file, 'utf8')); } catch { return fallback; }
}
function writeJson(file, obj) {
  const tmp = file + '.tmp';
  fs.writeFileSync(tmp, JSON.stringify(obj, null, 2));
  fs.renameSync(tmp, file);
}

let progress = readJson(PROGRESS, {});   // slug -> { status, solvedAt, attempts, lastLang, starred, note }

export function statusOf(slug) { return progress[slug]?.status || 'todo'; }
export function entry(slug) { return progress[slug] || { status: 'todo' }; }
export function allProgress() { return progress; }

export function setEntry(slug, patch) {
  progress[slug] = { ...(progress[slug] || { status: 'todo' }), ...patch };
  writeJson(PROGRESS, progress);
  return progress[slug];
}

export function recordSubmission(slug, sub) {
  const file = path.join(SUBS_DIR, `${slug}.json`);
  const list = readJson(file, []);
  const rec = { id: Date.now().toString(36) + Math.random().toString(36).slice(2, 6), at: Date.now(), ...sub };
  list.unshift(rec);
  writeJson(file, list.slice(0, 200));
  const cur = entry(slug);
  const patch = { attempts: (cur.attempts || 0) + 1, lastLang: sub.lang, lastAt: rec.at };
  if (sub.status === 'Accepted') { patch.status = 'solved'; patch.solvedAt = cur.solvedAt || rec.at; }
  else if (cur.status !== 'solved') patch.status = 'attempted';
  setEntry(slug, patch);
  return rec;
}

export function submissions(slug) {
  return readJson(path.join(SUBS_DIR, `${slug}.json`), []);
}

const safe = s => String(s).replace(/[^a-z0-9_-]/gi, '_');

export function saveDraft(slug, lang, code) {
  fs.writeFileSync(path.join(DRAFTS_DIR, `${safe(slug)}.${safe(lang)}`), code);
}
export function loadDraft(slug, lang) {
  try { return fs.readFileSync(path.join(DRAFTS_DIR, `${safe(slug)}.${safe(lang)}`), 'utf8'); } catch { return null; }
}
export function drafts(slug) {
  const out = {};
  for (const f of fs.readdirSync(DRAFTS_DIR)) {
    if (f.startsWith(safe(slug) + '.')) out[f.slice(safe(slug).length + 1)] = fs.readFileSync(path.join(DRAFTS_DIR, f), 'utf8');
  }
  return out;
}

export function getSettings() { return readJson(SETTINGS, { lang: 'python3', theme: 'dark', fontSize: 14 }); }
export function setSettings(patch) { const s = { ...getSettings(), ...patch }; writeJson(SETTINGS, s); return s; }

export function stats(problems) {
  const total = { Easy: 0, Medium: 0, Hard: 0 };
  const solved = { Easy: 0, Medium: 0, Hard: 0 };
  let attempted = 0;
  for (const p of problems) {
    total[p.difficulty] = (total[p.difficulty] || 0) + 1;
    const st = statusOf(p.slug);
    if (st === 'solved') solved[p.difficulty] = (solved[p.difficulty] || 0) + 1;
    else if (st === 'attempted') attempted++;
  }
  // streak: distinct days with an accepted submission, counting back from today
  const days = new Set();
  for (const [slug, e] of Object.entries(progress)) if (e.solvedAt) days.add(new Date(e.solvedAt).toDateString());
  let streak = 0; const d = new Date();
  while (days.has(d.toDateString())) { streak++; d.setDate(d.getDate() - 1); }
  return { total, solved, attempted, solvedTotal: Object.values(solved).reduce((a, b) => a + b, 0), totalAll: Object.values(total).reduce((a, b) => a + b, 0), streak, solvedDays: [...days] };
}
