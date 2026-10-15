// Turn a problem's exampleTestcases + parsed example outputs into judge tests.

export function isDesign(meta) {
  return !!(meta && (meta.systemdesign || meta.classname));
}

/** Parse a single LeetCode-format value line. Falls back to the raw string. */
export function parseValue(line) {
  const s = line.trim();
  if (s === '') return '';
  try { return JSON.parse(s); } catch { /* fallthrough */ }
  // LeetCode sometimes prints single-quoted strings / chars in examples
  if (/^'.*'$/.test(s)) return s.slice(1, -1);
  return s;
}

/** Number of input lines one test case consumes. */
export function linesPerTest(meta) {
  if (isDesign(meta)) return 2;
  const n = meta?.params?.length || 1;
  return n;
}

/**
 * Split raw testcase text (newline separated values) into tests.
 * Returns [{ args: [...] }] for function problems, [{ ops, args }] for design problems.
 */
export function splitTestcases(raw, meta) {
  const lines = (raw || '').replace(/\r/g, '').split('\n').filter(l => l.trim() !== '');
  const per = linesPerTest(meta);
  const tests = [];
  for (let i = 0; i + per <= lines.length; i += per) {
    const chunk = lines.slice(i, i + per);
    if (isDesign(meta)) tests.push({ ops: parseValue(chunk[0]), args: parseValue(chunk[1]), raw: chunk.join('\n') });
    else tests.push({ args: chunk.map(parseValue), raw: chunk.join('\n') });
  }
  return tests;
}

/**
 * Build the judge tests for a problem: example inputs paired with expected
 * outputs parsed from the statement. Expected may be null when unknown.
 */
export function buildExampleTests(problem) {
  const meta = problem.metaData;
  const tests = splitTestcases(problem.exampleTestcases, meta);
  const outs = (problem.examples || []).map(e => e.output);
  return tests.map((t, i) => ({ ...t, expected: outs[i] ?? null, index: i }));
}

export function buildCustomTests(raw, problem) {
  const meta = problem.metaData;
  return splitTestcases(raw, meta).map((t, i) => ({ ...t, expected: null, index: i, custom: true }));
}

/** Types the harnesses know how to construct/serialize. */
const BASE_TYPES = new Set(['integer', 'int', 'long', 'double', 'float', 'boolean', 'bool', 'string', 'character', 'char', 'void', 'ListNode', 'TreeNode']);

export function normalizeType(t) {
  return String(t || '').trim();
}

export function baseType(t) {
  let s = normalizeType(t);
  // strip list<...> wrappers and [] suffixes
  for (;;) {
    const m = /^list<(.*)>$/i.exec(s);
    if (m) { s = m[1].trim(); continue; }
    if (s.endsWith('[]')) { s = s.slice(0, -2); continue; }
    break;
  }
  return s;
}

export function typeSupported(t) {
  return BASE_TYPES.has(baseType(t));
}

const NON_ALGO = new Set(['Database', 'Shell', 'Concurrency', 'pandas', 'JavaScript']);
const ALLOWED_IDS = new Set(['Solution', 'List', 'Optional', 'ListNode', 'TreeNode', 'None', 'Definition', 'True', 'False', 'Dict', 'Set', 'Tuple', 'Deque', 'Counter', 'Any', 'Iterator', 'Iterable', 'Callable', 'Sequence', 'Union', 'Int', 'Str', 'Float', 'Bool']);

/** Whether our harnesses can drive this problem at all. */
export function judgeSupport(meta, problem = null) {
  if (!meta) return { supported: false, reason: 'No metadata for this problem.' };
  if (problem && NON_ALGO.has(problem.category)) return { supported: false, reason: `${problem.category} problems are not runnable by the local judge` };
  if (meta.manual) {
    // LeetCode drives these with a hand-written harness (custom Node classes, cycles,
    // interactive APIs...). We only take the ones whose inputs are plain values.
    const types = [...(meta.params || []).map(p => p.type), meta.return?.type || 'void'];
    if (types.some(t => /ListNode|TreeNode|Nested/.test(String(t)))) return { supported: false, reason: 'needs LeetCode\'s custom node wiring (cycles, shared nodes, custom Node classes)' };
    const snippet = problem?.codeSnippets?.python3 || '';
    const ids = new Set((snippet.match(/\b[A-Z][A-Za-z0-9]*\b/g) || []).filter(x => !ALLOWED_IDS.has(x)));
    if (ids.size) return { supported: false, reason: `uses a custom API/class (${[...ids].slice(0, 3).join(', ')})` };
  }
  if (isDesign(meta)) {
    const types = [];
    for (const p of meta.constructor?.params || []) types.push(p.type);
    for (const m of meta.methods || []) { for (const p of m.params || []) types.push(p.type); types.push(m.return?.type || 'void'); }
    const bad = types.filter(t => !typeSupported(t));
    if (bad.length) return { supported: false, reason: `Unsupported type(s): ${[...new Set(bad)].join(', ')}` };
    return { supported: true };
  }
  if (!meta.name) return { supported: false, reason: 'Interactive / special problem without a plain function signature.' };
  const types = [...(meta.params || []).map(p => p.type), meta.return?.type || 'void'];
  const bad = types.filter(t => !typeSupported(t));
  if (bad.length) return { supported: false, reason: `Unsupported type(s): ${[...new Set(bad)].join(', ')}` };
  return { supported: true };
}
