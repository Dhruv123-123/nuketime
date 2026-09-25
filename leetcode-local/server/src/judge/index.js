// Runs user code against tests in a temp directory and produces verdicts.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import crypto from 'node:crypto';
import { spawn } from 'node:child_process';
import { getLanguage, buildSpec } from './langs/index.js';
import { judgeTest, problemFlags } from './compare.js';
import { judgeSupport } from './testcases.js';
import { problemText } from '../problems.js';

const BEGIN = /\x1e\x1eLC_BEGIN (\d+)\n/g;
const RESULT = /\x1e\x1eLC_RESULT (.*)\n/g;
const MAX_STDOUT = 8000;

function exec({ cmd, args }, { cwd, input, timeoutMs, env }) {
  return new Promise(resolve => {
    const child = spawn(cmd, args, { cwd, env: { ...process.env, ...env }, stdio: ['pipe', 'pipe', 'pipe'], detached: process.platform !== 'win32' });
    let stdout = '', stderr = '', killed = false;
    const t0 = Date.now();
    const timer = setTimeout(() => { killed = true; try { process.kill(-child.pid, 'SIGKILL'); } catch { /* */ } try { child.kill('SIGKILL'); } catch { /* */ } }, timeoutMs);
    child.stdout.on('data', d => { if (stdout.length < 2_000_000) stdout += d; });
    child.stderr.on('data', d => { if (stderr.length < 200_000) stderr += d; });
    child.on('error', e => { clearTimeout(timer); const msg = e.code === 'ENOENT' ? `Cannot find \`${cmd}\` on this machine. Install it (see README) or use the Docker setup.` : e.message; resolve({ code: -1, stdout, stderr: stderr + '\n' + msg, killed, ms: Date.now() - t0 }); });
    child.on('close', (code, signal) => { clearTimeout(timer); resolve({ code, signal, stdout, stderr, killed, ms: Date.now() - t0 }); });
    if (input != null) { child.stdin.on('error', () => {}); child.stdin.end(input); } else child.stdin.end();
  });
}

/** Parse the marker protocol out of stdout into per-test {result, stdout}. */
function parseOutput(stdout, n) {
  const per = Array.from({ length: n }, () => ({ result: null, stdout: '' }));
  // Split into segments at BEGIN markers.
  const segs = stdout.split(/\x1e\x1eLC_BEGIN (\d+)\n/);
  // segs: [pre, idx, body, idx, body, ...]
  for (let k = 1; k + 1 < segs.length; k += 2) {
    const i = Number(segs[k]);
    let body = segs[k + 1];
    let result = null;
    const m = /\n?\x1e\x1eLC_RESULT (.*)\n?/s.exec(body);
    if (m) {
      try { result = JSON.parse(m[1].split('\n')[0]); } catch { result = null; }
      body = body.slice(0, m.index);
    }
    if (i < n) { per[i].result = result; per[i].stdout = body.length > MAX_STDOUT ? body.slice(0, MAX_STDOUT) + '\n...[truncated]' : body; }
  }
  return per;
}

/**
 * Run code for a problem.
 * @param {{problem, langId, code, tests}} p tests: [{args|ops+args, expected, raw, index}]
 * @returns {Promise<{status, compileError?, tests:[...], runtimeMs, summary}>}
 */
export async function runJudge({ problem, langId, code, tests }) {
  const lang = getLanguage(langId);
  if (!lang) return { status: 'Unsupported Language', tests: [], message: `Language ${langId} is not supported by the local judge.` };
  const support = judgeSupport(problem.metaData, problem);
  if (!support.supported) return { status: 'Not Judgeable', tests: [], message: support.reason };
  if (!tests.length) return { status: 'No Tests', tests: [], message: 'No test cases found.' };

  const spec = buildSpec(problem.metaData, tests);
  const flags = problemFlags(problemText(problem), problem.metaData);
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'lc-judge-'));
  try {
    const prep = lang.prepare(code, spec);
    for (const f of prep.files) fs.writeFileSync(path.join(dir, f.name), f.content);
    if (prep.compile) {
      const c = await exec(prep.compile, { cwd: dir, timeoutMs: 60000 });
      if (c.code !== 0) {
        if (c.code === -1) return { status: 'Judge Error', tests: [], message: c.stderr.trim() };
        return { status: 'Compile Error', compileError: (c.stdout + c.stderr).slice(0, 8000).replace(new RegExp(dir.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g'), ''), tests: [] };
      }
    }
    const timeoutMs = lang.timeLimitMs + 1500 * tests.length;
    const r = await exec(prep.run, { cwd: dir, input: JSON.stringify(spec), timeoutMs });
    const per = parseOutput(r.stdout, tests.length);
    const results = tests.map((t, i) => {
      const { result, stdout } = per[i];
      const base = { index: i, input: t.raw, stdout, expected: t.expected, custom: !!t.custom };
      if (!result) {
        // Process died / timed out before this test reported.
        const startedNext = per.slice(i + 1).some(p => p.result) ;
        if (r.killed && !startedNext) return { ...base, status: 'timeout', error: `Time Limit Exceeded (${Math.round(timeoutMs / 1000)}s for all tests)` };
        return { ...base, status: 'error', error: (r.stderr.trim() || (r.signal ? `Process killed by ${r.signal}${r.signal === 'SIGSEGV' ? ' (segmentation fault / stack overflow)' : ''}` : `Process exited with code ${r.code} before reporting a result`)).slice(0, 4000) };
      }
      if (!result.ok) return { ...base, status: 'error', error: result.error, ms: result.ms };
      const outDisplay = flags.returnsVoid ? result.mut : result.out;
      if (t.expected == null) return { ...base, status: 'unchecked', output: outDisplay, ms: result.ms };
      const v = judgeTest(result, t.expected, flags);
      return { ...base, status: v.status, output: outDisplay, expected: v.expectedDisplay ?? t.expected, ms: result.ms };
    });
    const counts = { passed: 0, failed: 0, error: 0, timeout: 0, unchecked: 0, unverified: 0 };
    for (const x of results) counts[x.status] = (counts[x.status] || 0) + 1;
    let status;
    if (counts.timeout) status = 'Time Limit Exceeded';
    else if (counts.error) status = 'Runtime Error';
    else if (counts.failed) status = 'Wrong Answer';
    else if (counts.passed && !counts.unverified) status = 'Accepted';
    else if (counts.unverified) status = 'Finished (multiple valid answers; not auto-verified)';
    else status = 'Finished';
    const runtimeMs = results.reduce((a, x) => a + (x.ms || 0), 0);
    return { status, tests: results, counts, runtimeMs, stderr: r.stderr.slice(0, 4000), flags };
  } finally {
    fs.rm(dir, { recursive: true, force: true }, () => {});
  }
}
