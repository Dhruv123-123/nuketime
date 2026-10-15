import { Link, NavLink, Outlet, useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { api, Stats } from '../api';

export default function Layout() {
  const nav = useNavigate();
  const [stats, setStats] = useState<Stats | null>(null);
  useEffect(() => {
    const load = () => api.stats().then(setStats).catch(() => {});
    load();
    window.addEventListener('lc:progress', load);
    return () => window.removeEventListener('lc:progress', load);
  }, []);
  const pick = async () => { const r = await api.random(); nav(`/problems/${r.slug}`); };
  return (
    <div className="h-full flex flex-col">
      <header className="h-12 shrink-0 flex items-center gap-4 px-4 border-b" style={{ borderColor: 'var(--border)', background: 'var(--panel)' }}>
        <Link to="/" className="flex items-center gap-2 font-semibold text-[15px]">
          <span className="text-xl">⚡</span> LeetCode <span className="text-[var(--accent)]">Local</span>
        </Link>
        <nav className="flex items-center gap-1 text-sm">
          <NavLink to="/" end className={({ isActive }) => `px-3 py-1.5 rounded-md ${isActive ? 'bg-[#3a3a3a] text-white' : 'text-gray-300 hover:text-white'}`}>Problems</NavLink>
          <NavLink to="/lists/blind-75" className={({ isActive }) => `px-3 py-1.5 rounded-md ${isActive ? 'bg-[#3a3a3a] text-white' : 'text-gray-300 hover:text-white'}`}>Blind 75</NavLink>
          <NavLink to="/lists/neetcode-core" className={({ isActive }) => `px-3 py-1.5 rounded-md ${isActive ? 'bg-[#3a3a3a] text-white' : 'text-gray-300 hover:text-white'}`}>Core patterns</NavLink>
        </nav>
        <div className="flex-1" />
        {stats && (
          <div className="text-xs text-gray-300 flex items-center gap-3">
            <span><b className="text-white">{stats.solvedTotal}</b> / {stats.totalAll} solved</span>
            {stats.streak > 0 && <span title="days in a row with an accepted submission">🔥 {stats.streak}</span>}
          </div>
        )}
        <button className="btn btn-ghost" onClick={pick} title="Pick a random problem">🎲 Random</button>
      </header>
      <main className="flex-1 min-h-0">
        <Outlet />
      </main>
    </div>
  );
}
