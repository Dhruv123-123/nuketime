
# ---- leetcode-local driver (auto-generated, not part of your solution) ----
def _lc_main():
    import sys, json, time, traceback, threading
    from collections import deque
    _out = sys.stdout
    spec = json.loads(sys.stdin.read())

    def to_list(arr):
        if arr is None:
            return None
        dummy = ListNode(0)
        cur = dummy
        for x in arr:
            cur.next = ListNode(x)
            cur = cur.next
        return dummy.next

    def to_tree(arr):
        if not arr or arr[0] is None:
            return None
        root = TreeNode(arr[0])
        q = deque([root])
        i = 1
        while q and i < len(arr):
            node = q.popleft()
            if i < len(arr) and arr[i] is not None:
                node.left = TreeNode(arr[i]); q.append(node.left)
            i += 1
            if i < len(arr) and arr[i] is not None:
                node.right = TreeNode(arr[i]); q.append(node.right)
            i += 1
        return root

    def build(v, t):
        t = (t or '').strip()
        if v is None:
            return None
        if t.lower().startswith('list<') and t.endswith('>'):
            return [build(x, t[5:-1]) for x in v]
        if t.endswith('[]'):
            return [build(x, t[:-2]) for x in v]
        if t == 'ListNode':
            return to_list(v)
        if t == 'TreeNode':
            return to_tree(v)
        if t in ('double', 'float') and isinstance(v, int) and not isinstance(v, bool):
            return float(v)
        return v

    def ser(o, depth=0):
        if o is None or isinstance(o, (bool, int, str)):
            return o
        if isinstance(o, float):
            if o != o or o in (float('inf'), float('-inf')):
                return str(o)
            return o
        if depth > 200:
            return '<too deep>'
        if hasattr(o, 'val') and hasattr(o, 'next') and not hasattr(o, 'left'):
            res, cur, n = [], o, 0
            while cur is not None and n < 100000:
                res.append(ser(cur.val, depth + 1)); cur = cur.next; n += 1
            return res
        if hasattr(o, 'val') and hasattr(o, 'left') and hasattr(o, 'right'):
            res, q = [], deque([o])
            while q:
                node = q.popleft()
                if node is None:
                    res.append(None)
                else:
                    res.append(ser(node.val, depth + 1)); q.append(node.left); q.append(node.right)
                if len(res) > 200000:
                    break
            while res and res[-1] is None:
                res.pop()
            return res
        if isinstance(o, dict):
            return {str(k): ser(v, depth + 1) for k, v in o.items()}
        if isinstance(o, (list, tuple, deque)):
            return [ser(x, depth + 1) for x in o]
        if isinstance(o, (set, frozenset)):
            return [ser(x, depth + 1) for x in o]
        if hasattr(o, '__iter__'):
            try:
                return [ser(x, depth + 1) for x in o]
            except Exception:
                pass
        return str(o)

    def emit(i, payload):
        sys.stdout.flush()
        _out.write('\n\x1e\x1eLC_RESULT ' + json.dumps({'i': i, **payload}) + '\n')
        _out.flush()

    def fmt_exc():
        tb = traceback.format_exc()
        lines = [l for l in tb.splitlines() if 'driver.py' not in l and '_lc_main' not in l]
        return '\n'.join(lines)[-4000:]

    for i, test in enumerate(spec['tests']):
        _out.write('\x1e\x1eLC_BEGIN %d\n' % i)
        _out.flush()
        t0 = time.perf_counter()
        try:
            if spec['kind'] == 'design':
                cls = globals()[spec['classname']]
                ops, argss = test['ops'], test['args']
                ctor_types = spec.get('ctorTypes') or []
                obj = cls(*[build(a, ctor_types[k] if k < len(ctor_types) else '') for k, a in enumerate(argss[0])])
                outs = [None]
                for op, a in zip(ops[1:], argss[1:]):
                    m = spec['methods'].get(op) or {}
                    ptypes = m.get('params') or []
                    r = getattr(obj, op)(*[build(x, ptypes[k] if k < len(ptypes) else '') for k, x in enumerate(a)])
                    outs.append(None if (m.get('return') or 'void') == 'void' else ser(r))
                ms = (time.perf_counter() - t0) * 1000
                emit(i, {'ok': True, 'out': outs, 'ms': ms})
            else:
                sol = Solution()
                fn = getattr(sol, spec['name'])
                args = [build(a, t) for a, t in zip(test['args'], spec['paramTypes'])]
                r = fn(*args)
                if r is None and spec.get('returnType') in ('ListNode', 'TreeNode'):
                    r = []
                ms = (time.perf_counter() - t0) * 1000
                mut = ser(args[0]) if args else None
                emit(i, {'ok': True, 'out': ser(r), 'mut': mut, 'ms': ms})
        except Exception:
            ms = (time.perf_counter() - t0) * 1000
            emit(i, {'ok': False, 'error': fmt_exc(), 'ms': ms})


if __name__ == '__main__':
    import threading as _th
    _th.stack_size(512 * 1024 * 1024)
    _t = _th.Thread(target=_lc_main)
    _t.start()
    _t.join()
