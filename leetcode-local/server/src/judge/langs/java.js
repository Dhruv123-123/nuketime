// Generates the Java driver body inserted into Main.java.tmpl.
import { isDesign } from '../testcases.js';

export function javaType(t) {
  t = (t || '').trim();
  const m = /^list<(.*)>$/i.exec(t);
  if (m) return `List<${boxed(javaType(m[1]))}>`;
  if (t.endsWith('[]')) return `${javaType(t.slice(0, -2))}[]`;
  switch (t) {
    case 'integer': case 'int': return 'int';
    case 'long': return 'long';
    case 'double': case 'float': return 'double';
    case 'boolean': case 'bool': return 'boolean';
    case 'string': return 'String';
    case 'character': case 'char': return 'char';
    case 'ListNode': return 'ListNode';
    case 'TreeNode': return 'TreeNode';
    case 'void': return 'void';
    default: return 'Object';
  }
}
function boxed(t) {
  return { int: 'Integer', long: 'Long', double: 'Double', boolean: 'Boolean', char: 'Character' }[t] || t;
}

const conv = (t, expr) => `(${javaType(t)}) LC.from(${expr}, "${t}")`;

export function javaDriver(spec) {
  const L = [];
  L.push('    public static void main(String[] args) throws Exception {');
  L.push('        Thread t = new Thread(null, () -> { try { run(); } catch (Throwable e) { e.printStackTrace(); } }, "main", 1L << 29);');
  L.push('        t.start(); t.join(); System.out.flush();');
  L.push('    }');
  L.push('    @SuppressWarnings("unchecked")');
  L.push('    static void run() throws Exception {');
  L.push('        String in = new String(System.in.readAllBytes(), java.nio.charset.StandardCharsets.UTF_8);');
  L.push('        Map<String,Object> spec = (Map<String,Object>) LC.parse(in);');
  L.push('        List<Object> tests = (List<Object>) spec.get("tests");');
  L.push('        for (int i = 0; i < tests.size(); i++) {');
  L.push('            Map<String,Object> test = (Map<String,Object>) tests.get(i);');
  L.push('            LC.begin(i); long t0 = System.nanoTime();');
  L.push('            try {');
  if (isDesign(spec)) {
    L.push('                List<Object> ops = (List<Object>) test.get("ops"); List<Object> argss = (List<Object>) test.get("args");');
    L.push('                List<Object> a0 = (List<Object>) argss.get(0);');
    const ctor = spec.ctorTypes.map((t, k) => conv(t, `a0.get(${k})`)).join(', ');
    L.push(`                ${spec.classname} obj = new ${spec.classname}(${ctor});`);
    L.push('                StringBuilder out = new StringBuilder("[null");');
    L.push('                for (int j = 1; j < ops.size(); j++) {');
    L.push('                    String op = (String) ops.get(j); List<Object> a = (List<Object>) argss.get(j); out.append(",");');
    let first = true;
    for (const [name, m] of Object.entries(spec.methods)) {
      const call = `obj.${name}(${m.params.map((t, k) => conv(t, `a.get(${k})`)).join(', ')})`;
      L.push(`                    ${first ? '' : 'else '}if (op.equals("${name}")) { ${m.return === 'void' ? `${call}; out.append("null");` : `out.append(LC.dump(${call}));`} }`);
      first = false;
    }
    L.push('                    else out.append("null");');
    L.push('                }');
    L.push('                out.append("]");');
    L.push('                LC.result(i, out.toString(), "null", t0);');
  } else {
    L.push('                List<Object> a = (List<Object>) test.get("args");');
    spec.paramTypes.forEach((t, k) => L.push(`                ${javaType(t)} p${k} = ${conv(t, `a.get(${k})`)};`));
    L.push('                Solution sol = new Solution();');
    const call = `sol.${spec.name}(${spec.paramTypes.map((_, k) => `p${k}`).join(', ')})`;
    const mut = spec.paramTypes.length ? 'LC.dump(p0)' : '"null"';
    if (spec.returnType === 'void') {
      L.push(`                ${call};`);
      L.push(`                LC.result(i, "null", ${mut}, t0);`);
    } else {
      L.push(`                var r = ${call};`);
      const dumpFn = (spec.returnType === 'ListNode' || spec.returnType === 'TreeNode') ? 'LC.dumpNode' : 'LC.dump';
      L.push(`                LC.result(i, ${dumpFn}(r), ${mut}, t0);`);
    }
  }
  L.push('            } catch (Throwable e) { LC.error(i, e, t0); }');
  L.push('        }');
  L.push('    }');
  return L.join('\n');
}
