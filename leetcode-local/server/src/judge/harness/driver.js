
// ---- leetcode-local driver (auto-generated, not part of your solution) ----
(function __lcMain() {
  const fs = require('fs');
  const spec = JSON.parse(fs.readFileSync(0, 'utf8'));
  const write = (s) => fs.writeSync(1, s);

  function toList(arr) {
    if (arr == null) return null;
    const dummy = new ListNode(0); let cur = dummy;
    for (const x of arr) { cur.next = new ListNode(x); cur = cur.next; }
    return dummy.next;
  }
  function toTree(arr) {
    if (!arr || !arr.length || arr[0] == null) return null;
    const root = new TreeNode(arr[0]); const q = [root]; let qi = 0, i = 1;
    while (qi < q.length && i < arr.length) {
      const node = q[qi++];
      if (i < arr.length && arr[i] != null) { node.left = new TreeNode(arr[i]); q.push(node.left); }
      i++;
      if (i < arr.length && arr[i] != null) { node.right = new TreeNode(arr[i]); q.push(node.right); }
      i++;
    }
    return root;
  }
  function build(v, t) {
    t = (t || '').trim();
    if (v == null) return null;
    if (/^list</i.test(t) && t.endsWith('>')) return v.map(x => build(x, t.slice(5, -1)));
    if (t.endsWith('[]')) return v.map(x => build(x, t.slice(0, -2)));
    if (t === 'ListNode') return toList(v);
    if (t === 'TreeNode') return toTree(v);
    return v;
  }
  function ser(o, depth = 0) {
    if (o === undefined) return null;
    if (o === null || typeof o === 'number' || typeof o === 'string' || typeof o === 'boolean') {
      if (typeof o === 'number' && !Number.isFinite(o)) return String(o);
      return o;
    }
    if (typeof o === 'bigint') return Number(o);
    if (depth > 200) return '<too deep>';
    if (Array.isArray(o)) return o.map(x => ser(x, depth + 1));
    if (o instanceof Map) { const r = {}; for (const [k, v] of o) r[String(k)] = ser(v, depth + 1); return r; }
    if (o instanceof Set) return [...o].map(x => ser(x, depth + 1));
    if (ArrayBuffer.isView(o)) return Array.from(o);
    if (typeof o === 'object' && 'val' in o && 'next' in o && !('left' in o)) {
      const res = []; let cur = o, n = 0;
      while (cur && n < 100000) { res.push(ser(cur.val, depth + 1)); cur = cur.next; n++; }
      return res;
    }
    if (typeof o === 'object' && 'val' in o && 'left' in o && 'right' in o) {
      const res = []; const q = [o]; let qi = 0;
      while (qi < q.length && res.length < 200000) {
        const node = q[qi++];
        if (node == null) res.push(null);
        else { res.push(ser(node.val, depth + 1)); q.push(node.left); q.push(node.right); }
      }
      while (res.length && res[res.length - 1] === null) res.pop();
      return res;
    }
    if (typeof o === 'object') { const r = {}; for (const k of Object.keys(o)) r[k] = ser(o[k], depth + 1); return r; }
    return String(o);
  }
  function emit(i, payload) { write('\n\x1e\x1eLC_RESULT ' + JSON.stringify({ i, ...payload }) + '\n'); }
  function fmtErr(e) {
    const s = (e && e.stack) ? String(e.stack) : String(e);
    return s.split('\n').filter(l => !/driver\.js|__lcMain|node:internal/.test(l)).join('\n').slice(0, 4000);
  }

  spec.tests.forEach((test, i) => {
    write('\x1e\x1eLC_BEGIN ' + i + '\n');
    const t0 = process.hrtime.bigint();
    try {
      if (spec.kind === 'design') {
        const Cls = eval(spec.classname);
        const ctorTypes = spec.ctorTypes || [];
        const obj = new Cls(...test.args[0].map((a, k) => build(a, ctorTypes[k])));
        const outs = [null];
        for (let j = 1; j < test.ops.length; j++) {
          const op = test.ops[j]; const m = spec.methods[op] || {}; const pt = m.params || [];
          const r = obj[op](...(test.args[j] || []).map((a, k) => build(a, pt[k])));
          outs.push((m.return || 'void') === 'void' ? null : ser(r));
        }
        emit(i, { ok: true, out: outs, ms: Number(process.hrtime.bigint() - t0) / 1e6 });
      } else {
        const fn = eval(spec.name);
        const args = test.args.map((a, k) => build(a, spec.paramTypes[k]));
        let r = fn(...args);
        if (r == null && (spec.returnType === 'ListNode' || spec.returnType === 'TreeNode')) r = [];
        emit(i, { ok: true, out: ser(r), mut: args.length ? ser(args[0]) : null, ms: Number(process.hrtime.bigint() - t0) / 1e6 });
      }
    } catch (e) {
      emit(i, { ok: false, error: fmtErr(e), ms: Number(process.hrtime.bigint() - t0) / 1e6 });
    }
  });
})();
