// Compare a harness result against the expected output parsed from the statement.

const EPS = 1e-5;

function isNum(x) { return typeof x === 'number' && Number.isFinite(x); }

export function deepEqual(a, b) {
  if (a === b) return true;
  if (a === null || b === null || a === undefined || b === undefined) return (a ?? null) === (b ?? null);
  if (isNum(a) && isNum(b)) return Math.abs(a - b) <= EPS * Math.max(1, Math.abs(a), Math.abs(b));
  if (typeof a === 'boolean' || typeof b === 'boolean') return a === b;
  if (typeof a === 'string' || typeof b === 'string') return String(a) === String(b);
  if (Array.isArray(a) && Array.isArray(b)) {
    if (a.length !== b.length) return false;
    for (let i = 0; i < a.length; i++) if (!deepEqual(a[i], b[i])) return false;
    return true;
  }
  if (typeof a === 'object' && typeof b === 'object') {
    const ka = Object.keys(a), kb = Object.keys(b);
    if (ka.length !== kb.length) return false;
    return ka.every(k => deepEqual(a[k], b[k]));
  }
  return false;
}

export function canon(x) {
  if (Array.isArray(x)) return '[' + x.map(canon).join(',') + ']';
  if (isNum(x)) return String(Math.round(x * 1e6) / 1e6);
  return JSON.stringify(x);
}

const byCanon = (a, b) => (canon(a) < canon(b) ? -1 : canon(a) > canon(b) ? 1 : 0);
function sortedOuter(x) {
  if (!Array.isArray(x)) return x;
  return [...x].sort(byCanon);
}
function deepSorted(x) {
  if (!Array.isArray(x)) return x;
  return x.map(deepSorted).sort(byCanon);
}
/** True when every nested array inside x is already in canonical sorted order. */
function innerSorted(x) {
  if (!Array.isArray(x)) return true;
  return x.every(e => {
    if (!Array.isArray(e)) return true;
    for (let i = 1; i < e.length; i++) if (byCanon(e[i - 1], e[i]) > 0) return false;
    return innerSorted(e);
  });
}

/** Parse the expected-output string from a statement example. */
export function parseExpected(raw) {
  if (raw === null || raw === undefined) return { kind: 'unknown' };
  let s = String(raw).trim();
  // "2, nums = [1,2,_]" style (in-place array problems that return k)
  const m = /^(-?\d+)\s*,\s*\w+\s*=\s*(\[.*\])\s*$/s.exec(s);
  if (m) {
    try {
      const arr = JSON.parse(m[2].replace(/_/g, 'null'));
      return { kind: 'k-prefix', k: Number(m[1]), prefix: arr.slice(0, Number(m[1])) };
    } catch { /* fallthrough */ }
  }
  // Strip trailing commentary like "[1,2]  (explanation)"
  try { return { kind: 'value', value: JSON.parse(s) }; } catch { /* fallthrough */ }
  // single-quoted strings / chars
  if (/^'.*'$/.test(s)) return { kind: 'value', value: s.slice(1, -1) };
  // bare words that are obviously strings
  if (/^[A-Za-z_][\w ]*$/.test(s) && !/^(true|false|null)$/i.test(s)) return { kind: 'value', value: s };
  if (/^(true|false)$/i.test(s)) return { kind: 'value', value: s.toLowerCase() === 'true' };
  // Sometimes the output is followed by an explanation on the same line: "3 (because ...)"
  const firstTok = /^(-?\d+(?:\.\d+)?|\[.*?\]|".*?")/s.exec(s);
  if (firstTok) { try { return { kind: 'value', value: JSON.parse(firstTok[1]), loose: true }; } catch { /* ignore */ } }
  return { kind: 'unknown', raw: s };
}

/**
 * Decide the verdict for one test.
 * result: { ok, out, mut, error }, expected: raw expected string, flags: { anyOrder, multipleAnswers, returnsVoid }
 * Returns { status: 'passed'|'failed'|'error'|'unchecked'|'unverified', expectedDisplay }
 */
export function judgeTest(result, expectedRaw, flags = {}) {
  if (!result || !result.ok) return { status: 'error', expectedDisplay: expectedRaw ?? null };
  const exp = parseExpected(expectedRaw);
  const actual = flags.returnsVoid ? result.mut : result.out;
  if (exp.kind === 'unknown') return { status: 'unchecked', expectedDisplay: expectedRaw ?? null };
  if (exp.kind === 'k-prefix') {
    const k = result.out;
    const arr = Array.isArray(result.mut) ? result.mut.slice(0, exp.k) : null;
    const ok = k === exp.k && arr && deepEqual(arr, exp.prefix);
    return { status: ok ? 'passed' : 'failed', expectedDisplay: `${exp.k}, first ${exp.k} elements = ${JSON.stringify(exp.prefix)}` };
  }
  let ok = deepEqual(actual, exp.value);
  if (!ok && flags.anyOrder && Array.isArray(actual) && Array.isArray(exp.value)) {
    ok = deepEqual(sortedOuter(actual), sortedOuter(exp.value));
    // If the statement's expected inner groups are themselves sorted (group anagrams,
    // 3Sum, subsets...), inner order is not significant either. Permutation-style
    // answers have unsorted inner arrays and keep strict inner order.
    if (!ok && innerSorted(exp.value)) ok = deepEqual(deepSorted(actual), deepSorted(exp.value));
  }
  if (!ok && typeof exp.value === 'string' && typeof actual !== 'string') {
    ok = canon(actual) === exp.value; // e.g. expected "abc" vs char array
  }
  if (ok) return { status: 'passed', expectedDisplay: JSON.stringify(exp.value) };
  if (flags.multipleAnswers) return { status: 'unverified', expectedDisplay: JSON.stringify(exp.value) };
  return { status: 'failed', expectedDisplay: JSON.stringify(exp.value) };
}

export function problemFlags(problemTextLower, meta) {
  const t = problemTextLower || '';
  return {
    anyOrder: /in any order|any order/.test(t),
    multipleAnswers: /return any (of them|one|valid|answer)|any valid (answer|solution)|any (such|possible|correct) (answer|solution)|multiple (valid |possible |correct )?(answers|solutions)|there (may be|are|can be) (multiple|many|several) (valid |possible |correct )?(answers|solutions)|any of (the )?(valid )?answers/.test(t),
    returnsVoid: (meta?.return?.type || '') === 'void',
  };
}
