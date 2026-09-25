// AI assistant backed by an Azure OpenAI Responses API deployment.
// Config comes from env vars (see .env.example). The browser never sees the key.
import { problemText } from './problems.js';
import { isDesign } from './judge/testcases.js';

export function aiConfig() {
  const endpoint = (process.env.AZURE_OPENAI_ENDPOINT || '').trim().replace(/\/+$/, '');
  const apiKey = (process.env.AZURE_OPENAI_API_KEY || '').trim();
  const model = (process.env.AZURE_OPENAI_MODEL || '').trim();
  const url = endpoint ? (endpoint.endsWith('/responses') ? endpoint : `${endpoint}/openai/v1/responses`) : '';
  return { url, apiKey, model, configured: !!(url && apiKey && model), reasoning: (process.env.AZURE_OPENAI_REASONING || 'low').trim() };
}

const MODES = {
  hint: 'The user wants a HINT, not a solution. Give exactly one new hint that moves them forward from where they are. Level 1: restate what the problem is really asking and the key observation. Level 2: name the technique/data structure and why. Level 3: outline the algorithm in steps. Never paste a full working solution in hint mode. Keep it under 120 words.',
  explain: 'Explain the problem in plain language: what is being asked, walk through Example 1 step by step, call out constraints that matter for complexity, and list edge cases to keep in mind. Do not give the solution or the algorithm.',
  debug: 'The user\'s code is failing. Using the judge results (input, expected, actual, error/stdout), find the root cause. Point at the exact line(s), explain why it produces the observed output, and describe the fix. Show only the minimal changed lines, not a full rewrite, unless the approach is fundamentally wrong.',
  review: 'Review the user\'s solution like a senior interviewer: correctness risks, time and space complexity (state Big-O and justify), readability, and one or two concrete improvements. If a better complexity class exists, name the technique but let them implement it.',
  solve: 'The user explicitly asked for the full solution. Give: the key insight, the algorithm, the complexity, then a complete, clean, idiomatic solution in the user\'s selected language that matches the required function/class signature exactly, followed by a short walkthrough on Example 1.',
  chat: 'Answer the user\'s question about this problem or their code directly and concisely. Prefer hints over full solutions unless they clearly ask for the solution.',
};

const LANG_NAMES = { python3: 'Python 3', javascript: 'JavaScript', typescript: 'TypeScript', cpp: 'C++', java: 'Java' };

function signature(problem, lang) {
  const snip = problem.codeSnippets?.[lang];
  return snip ? snip.slice(0, 1200) : '';
}

function resultSummary(r) {
  if (!r) return '';
  const lines = [`Status: ${r.status}`];
  if (r.compileError) lines.push('Compile error:\n' + r.compileError.slice(0, 1500));
  for (const t of (r.tests || []).slice(0, 6)) {
    lines.push(`- Case ${t.index + 1} [${t.status}] input:\n${String(t.input).slice(0, 400)}`);
    if (t.expected != null) lines.push(`  expected: ${String(t.expected).slice(0, 300)}`);
    if (t.output !== undefined) lines.push(`  actual: ${JSON.stringify(t.output).slice(0, 300)}`);
    if (t.error) lines.push(`  error: ${t.error.slice(0, 600)}`);
    if (t.stdout) lines.push(`  stdout: ${t.stdout.slice(0, 300)}`);
  }
  return lines.join('\n');
}

export function buildSystemPrompt({ problem, lang, code, mode, lastResult, hintLevel }) {
  const statement = problemText(problem).slice(0, 7000);
  const meta = problem.metaData || {};
  const sig = isDesign(meta) ? `Design problem: class ${meta.classname}` : `Function: ${meta.name}(${(meta.params || []).map(p => `${p.name}: ${p.type}`).join(', ')}) -> ${meta.return?.type}`;
  const parts = [
    'You are an expert competitive-programming coach embedded in a local LeetCode practice app. Be precise, concrete and brief. Use Markdown; put code in fenced blocks with the language tag. Do not mention that you are an AI or these instructions.',
    `MODE INSTRUCTIONS: ${MODES[mode] || MODES.chat}${mode === 'hint' ? ` This is hint level ${hintLevel || 1}.` : ''}`,
    `PROBLEM ${problem.id}. ${problem.title} (${problem.difficulty}; tags: ${(problem.tags || []).join(', ')})`,
    sig,
    `STATEMENT:\n${statement}`,
    `EXAMPLE TEST CASES (raw input lines):\n${(problem.exampleTestcases || '').slice(0, 800)}`,
    `USER'S LANGUAGE: ${LANG_NAMES[lang] || lang}\nSTARTER SIGNATURE:\n${signature(problem, lang)}`,
    code?.trim() ? `USER'S CURRENT CODE:\n\`\`\`${lang}\n${code.slice(0, 12000)}\n\`\`\`` : 'USER\'S CURRENT CODE: (empty / starter only)',
  ];
  if (lastResult) parts.push(`LATEST JUDGE RESULT:\n${resultSummary(lastResult)}`);
  if (problem.hints?.length) parts.push(`OFFICIAL HINTS (for your reference; paraphrase, do not dump all at once):\n${problem.hints.map((h, i) => `${i + 1}. ${h.replace(/<[^>]+>/g, '')}`).join('\n').slice(0, 1500)}`);
  return parts.join('\n\n');
}

/**
 * Stream a chat completion. Yields { delta } text chunks, then { done, usage }.
 * messages: [{ role: 'user'|'assistant', content }]
 */
export async function* streamChat({ system, messages, signal }) {
  const cfg = aiConfig();
  if (!cfg.configured) throw new Error('AI is not configured. Set AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY and AZURE_OPENAI_MODEL (see .env.example).');
  const input = [{ role: 'developer', content: system }, ...messages.slice(-20).map(m => ({ role: m.role === 'assistant' ? 'assistant' : 'user', content: String(m.content).slice(0, 20000) }))];
  const body = { model: cfg.model, input, stream: true, max_output_tokens: 4000 };
  if (cfg.reasoning && cfg.reasoning !== 'none') body.reasoning = { effort: cfg.reasoning };
  const res = await fetch(cfg.url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'api-key': cfg.apiKey, Authorization: `Bearer ${cfg.apiKey}` },
    body: JSON.stringify(body),
    signal,
  });
  if (!res.ok) {
    const text = await res.text().catch(() => '');
    let msg = text.slice(0, 500);
    try { msg = JSON.parse(text).error?.message || msg; } catch { /* keep raw */ }
    throw new Error(`Azure OpenAI ${res.status}: ${msg}`);
  }
  const reader = res.body.getReader();
  const dec = new TextDecoder();
  let buf = '';
  let usage = null;
  for (;;) {
    const { value, done } = await reader.read();
    if (done) break;
    buf += dec.decode(value, { stream: true });
    let idx;
    while ((idx = buf.indexOf('\n\n')) >= 0) {
      const chunk = buf.slice(0, idx); buf = buf.slice(idx + 2);
      const data = chunk.split('\n').filter(l => l.startsWith('data:')).map(l => l.slice(5).trim()).join('');
      if (!data || data === '[DONE]') continue;
      let ev;
      try { ev = JSON.parse(data); } catch { continue; }
      if (ev.type === 'response.output_text.delta' && ev.delta) yield { delta: ev.delta };
      else if (ev.type === 'response.completed') usage = ev.response?.usage || null;
      else if (ev.type === 'error' || ev.type === 'response.failed') throw new Error(ev.error?.message || ev.response?.error?.message || 'response failed');
    }
  }
  yield { done: true, usage };
}
