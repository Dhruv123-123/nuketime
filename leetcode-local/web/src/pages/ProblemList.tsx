import { useEffect, useMemo, useState } from 'react';
import { Link, useParams, useSearchParams, useNavigate } from 'react-router-dom';
import { api, ProblemListResult, Stats, StudyList, ProblemRow } from '../api';
import StatusIcon from '../components/StatusIcon';

const DIFFS = ['Easy', 'Medium', 'Hard'] as const;
const PAGE_SIZE = 50;

export default function ProblemList() {
  const { listId } = useParams();
  const nav = useNavigate();
  const [sp, setSp] = useSearchParams();
  const q = sp.get('q') || '';
  const difficulty = sp.get('difficulty') || '';
  const status = sp.get('status') || '';
  const tags = sp.get('tags') || '';
  const sort = sp.get('sort') || 'id';
  const order = sp.get('order') || 'asc';
  const page = Number(sp.get('page') || 1);

  const [data, setData] = useState<ProblemListResult | null>(null);
  const [allTags, setAllTags] = useState<{ name: string; count: number }[]>([]);
  const [stats, setStats] = useState<Stats | null>(null);
  const [lists, setLists] = useState<StudyList[]>([]);
  const [recent, setRecent] = useState<ProblemRow[]>([]);
  const [tagOpen, setTagOpen] = useState(false);
  const [search, setSearch] = useState(q);
  const [loading, setLoading] = useState(false);

  useEffect(() => { api.tags().then(setAllTags); api.stats().then(setStats); api.lists().then(setLists); api.recent().then(setRecent); }, [listId]);
  useEffect(() => { setSearch(q); }, [q]);
  useEffect(() => {
    setLoading(true);
    api.problems({ q, difficulty, status, tags, sort, order, page, pageSize: PAGE_SIZE, list: listId })
      .then(setData).finally(() => setLoading(false));
  }, [q, difficulty, status, tags, sort, order, page, listId]);

  const set = (patch: Record<string, string>) => {
    const next = new URLSearchParams(sp);
    for (const [k, v] of Object.entries(patch)) { if (v) next.set(k, v); else next.delete(k); }
    if (!('page' in patch)) next.delete('page');
    setSp(next);
  };
  const toggleTag = (t: string) => {
    const cur = tags ? tags.split(',') : [];
    set({ tags: (cur.includes(t) ? cur.filter(x => x !== t) : [...cur, t]).join(',') });
  };
  const sortBy = (col: string) => set({ sort: col, order: sort === col && order === 'asc' ? 'desc' : 'asc' });
  const totalPages = data ? Math.max(1, Math.ceil(data.total / PAGE_SIZE)) : 1;
  const selectedTags = useMemo(() => (tags ? tags.split(',') : []), [tags]);
  const currentList = lists.find(l => l.id === listId);

  const pickRandom = async () => {
    const r = await api.random({ difficulty, tags, unsolved: '1' });
    nav(`/problems/${r.slug}`);
  };

  return (
    <div className="h-full overflow-auto">
      <div className="max-w-[1280px] mx-auto px-4 py-5 flex gap-6">
        <div className="flex-1 min-w-0">
          {currentList && (
            <div className="mb-4 p-4 rounded-lg" style={{ background: 'var(--panel)' }}>
              <div className="flex items-center justify-between">
                <div>
                  <h1 className="text-lg font-semibold">{currentList.name}</h1>
                  <p className="text-sm text-gray-400">{currentList.description}</p>
                </div>
                <div className="text-right text-sm"><b className="text-white">{currentList.solved}</b> / {currentList.count} solved</div>
              </div>
              <div className="mt-3 h-1.5 rounded bg-[#3a3a3a] overflow-hidden"><div className="h-full" style={{ width: `${(100 * currentList.solved) / Math.max(1, currentList.count)}%`, background: 'var(--accent)' }} /></div>
            </div>
          )}

          {/* filters */}
          <div className="flex flex-wrap items-center gap-2 mb-3">
            <form onSubmit={e => { e.preventDefault(); set({ q: search }); }} className="flex-1 min-w-[220px]">
              <input type="search" placeholder="Search by title or number…" className="w-full" value={search} onChange={e => setSearch(e.target.value)} />
            </form>
            <select value={difficulty} onChange={e => set({ difficulty: e.target.value })}>
              <option value="">Difficulty</option>
              {DIFFS.map(d => <option key={d} value={d}>{d}</option>)}
            </select>
            <select value={status} onChange={e => set({ status: e.target.value })}>
              <option value="">Status</option>
              <option value="todo">Todo</option>
              <option value="attempted">Attempted</option>
              <option value="solved">Solved</option>
            </select>
            <button type="button" className="btn btn-ghost" onClick={() => setTagOpen(o => !o)}>Tags {selectedTags.length ? `(${selectedTags.length})` : ''} ▾</button>
            <button type="button" className="btn btn-ghost" onClick={pickRandom} title="Random unsolved problem matching the current filters">🎲 Pick one</button>
            {(q || difficulty || status || tags) && <button type="button" className="btn btn-ghost" onClick={() => setSp(new URLSearchParams())}>Reset</button>}
          </div>
          {tagOpen && (
            <div className="mb-3 p-3 rounded-lg flex flex-wrap gap-1.5 max-h-56 overflow-auto" style={{ background: 'var(--panel)' }}>
              {allTags.map(t => (
                <button key={t.name} className={`chip ${selectedTags.includes(t.name) ? 'chip-active' : ''}`} onClick={() => toggleTag(t.name)}>
                  {t.name} <span className="ml-1 opacity-60">{t.count}</span>
                </button>
              ))}
            </div>
          )}
          {selectedTags.length > 0 && !tagOpen && (
            <div className="mb-3 flex flex-wrap gap-1.5">{selectedTags.map(t => <button key={t} className="chip chip-active" onClick={() => toggleTag(t)}>{t} ✕</button>)}</div>
          )}

          {/* table */}
          <div className="rounded-lg overflow-hidden" style={{ background: 'var(--panel)' }}>
            <table className="w-full text-sm">
              <thead>
                <tr className="text-left text-gray-400 text-xs border-b" style={{ borderColor: 'var(--border)' }}>
                  <th className="px-3 py-2 w-10">Status</th>
                  <th className="px-3 py-2 cursor-pointer select-none" onClick={() => sortBy('id')}>Title {sort === 'id' && (order === 'asc' ? '↑' : '↓')}</th>
                  <th className="px-3 py-2 w-24 cursor-pointer select-none" onClick={() => sortBy('acceptance')}>Acceptance {sort === 'acceptance' && (order === 'asc' ? '↑' : '↓')}</th>
                  <th className="px-3 py-2 w-24 cursor-pointer select-none" onClick={() => sortBy('difficulty')}>Difficulty {sort === 'difficulty' && (order === 'asc' ? '↑' : '↓')}</th>
                  <th className="px-3 py-2 w-64 hidden lg:table-cell">Tags</th>
                </tr>
              </thead>
              <tbody className={loading ? 'pulse' : ''}>
                {data?.items.map((p, i) => (
                  <tr key={p.slug} className="border-b last:border-0 hover:bg-[#2f2f2f]" style={{ borderColor: '#2f2f2f', background: i % 2 ? 'transparent' : '#2a2a2a' }}>
                    <td className="px-3 py-2 text-center"><StatusIcon status={p.status} /></td>
                    <td className="px-3 py-2"><Link to={`/problems/${p.slug}`} className="hover:text-blue-400">{p.id}. {p.title}</Link></td>
                    <td className="px-3 py-2 text-gray-300">{p.acRate || '—'}</td>
                    <td className={`px-3 py-2 diff-${p.difficulty}`}>{p.difficulty}</td>
                    <td className="px-3 py-2 hidden lg:table-cell">
                      <div className="flex flex-wrap gap-1">{p.tags.slice(0, 3).map(t => <button key={t} className="chip" onClick={() => toggleTag(t)}>{t}</button>)}{p.tags.length > 3 && <span className="chip">+{p.tags.length - 3}</span>}</div>
                    </td>
                  </tr>
                ))}
                {data && data.items.length === 0 && <tr><td colSpan={5} className="px-3 py-8 text-center text-gray-400">No problems match. {!data.total && !q && 'Did you run the scraper? (npm run scrape)'}</td></tr>}
              </tbody>
            </table>
          </div>
          {data && (
            <div className="flex items-center justify-between mt-3 text-sm text-gray-400">
              <span>{data.total} problems</span>
              <div className="flex items-center gap-2">
                <button className="btn btn-ghost" disabled={page <= 1} onClick={() => set({ page: String(page - 1) })}>‹ Prev</button>
                <span>{page} / {totalPages}</span>
                <button className="btn btn-ghost" disabled={page >= totalPages} onClick={() => set({ page: String(page + 1) })}>Next ›</button>
              </div>
            </div>
          )}
        </div>

        {/* sidebar */}
        <aside className="w-72 shrink-0 hidden md:block space-y-4">
          {stats && <ProgressCard stats={stats} />}
          <div className="p-4 rounded-lg" style={{ background: 'var(--panel)' }}>
            <h3 className="text-sm font-semibold mb-2">Study lists</h3>
            <ul className="space-y-1.5 text-sm">
              <li><Link to="/" className={`block px-2 py-1 rounded hover:bg-[#3a3a3a] ${!listId ? 'bg-[#3a3a3a]' : ''}`}>All problems</Link></li>
              {lists.map(l => (
                <li key={l.id}><Link to={`/lists/${l.id}`} className={`flex justify-between px-2 py-1 rounded hover:bg-[#3a3a3a] ${listId === l.id ? 'bg-[#3a3a3a]' : ''}`}><span>{l.name}</span><span className="text-gray-400">{l.solved}/{l.count}</span></Link></li>
              ))}
            </ul>
          </div>
          {recent.length > 0 && (
            <div className="p-4 rounded-lg" style={{ background: 'var(--panel)' }}>
              <h3 className="text-sm font-semibold mb-2">Recent</h3>
              <ul className="space-y-1 text-sm">
                {recent.map(p => <li key={p.slug} className="flex items-center gap-2 truncate"><StatusIcon status={p.status} size={12} /><Link to={`/problems/${p.slug}`} className="truncate hover:text-blue-400">{p.id}. {p.title}</Link></li>)}
              </ul>
            </div>
          )}
        </aside>
      </div>
    </div>
  );
}

function ProgressCard({ stats }: { stats: Stats }) {
  const total = Math.max(1, stats.totalAll);
  const e = (100 * stats.solved.Easy) / total, m = e + (100 * stats.solved.Medium) / total, h = m + (100 * stats.solved.Hard) / total;
  return (
    <div className="p-4 rounded-lg flex items-center gap-4" style={{ background: 'var(--panel)' }}>
      <div className="ring" style={{ ['--e' as string]: `${e}%`, ['--m' as string]: `${m}%`, ['--h' as string]: `${h}%` }}>
        <div><div className="text-center"><div className="text-xl font-semibold leading-none">{stats.solvedTotal}</div><div className="text-[10px] text-gray-400">Solved</div></div></div>
      </div>
      <div className="text-xs space-y-1.5 flex-1">
        {(['Easy', 'Medium', 'Hard'] as const).map(d => (
          <div key={d} className="flex justify-between"><span className={`diff-${d}`}>{d}</span><span><b className="text-white">{stats.solved[d]}</b> / {stats.total[d]}</span></div>
        ))}
        <div className="flex justify-between text-gray-400"><span>Attempted</span><span>{stats.attempted}</span></div>
      </div>
    </div>
  );
}
