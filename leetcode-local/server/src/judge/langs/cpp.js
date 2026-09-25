// Generates the C++ main() that drives the user's Solution / design class.
import { isDesign } from '../testcases.js';

export function cppType(t) {
  t = (t || '').trim();
  const m = /^list<(.*)>$/i.exec(t);
  if (m) return `vector<${cppType(m[1])}>`;
  if (t.endsWith('[]')) return `vector<${cppType(t.slice(0, -2))}>`;
  switch (t) {
    case 'integer': case 'int': return 'int';
    case 'long': return 'long long';
    case 'double': case 'float': return 'double';
    case 'boolean': case 'bool': return 'bool';
    case 'string': return 'string';
    case 'character': case 'char': return 'char';
    case 'ListNode': return 'ListNode*';
    case 'TreeNode': return 'TreeNode*';
    case 'void': return 'void';
    default: return 'lc::Json';
  }
}

export function cppDriver(spec) {
  const L = [];
  L.push('', '// ---- leetcode-local driver (auto-generated) ----');
  L.push('int main() {');
  L.push('  std::ios::sync_with_stdio(true);');
  L.push('  std::string __in((std::istreambuf_iterator<char>(std::cin)), std::istreambuf_iterator<char>());');
  L.push('  lc::Json __spec = lc::parse(__in);');
  L.push('  const auto& __tests = __spec["tests"].arr();');
  L.push('  for (size_t __i = 0; __i < __tests.size(); ++__i) {');
  L.push('    lc::begin(__i); auto __t0 = std::chrono::steady_clock::now();');
  L.push('    try {');
  if (isDesign(spec)) {
    const ctor = spec.ctorTypes.map((t, k) => `lc::from<${cppType(t)}>(__args[0][${k}])`).join(', ');
    L.push('      const auto& __ops = __tests[__i]["ops"].arr(); const auto& __args = __tests[__i]["args"].arr();');
    L.push(`      ${spec.classname}* __obj = new ${spec.classname}(${ctor});`);
    L.push('      std::string __out = "[null";');
    L.push('      for (size_t __j = 1; __j < __ops.size(); ++__j) {');
    L.push('        const std::string& __op = __ops[__j].str(); const auto& __a = __args[__j];');
    L.push('        __out += ",";');
    let first = true;
    for (const [name, m] of Object.entries(spec.methods)) {
      const call = `__obj->${name}(${m.params.map((t, k) => `lc::from<${cppType(t)}>(__a[${k}])`).join(', ')})`;
      L.push(`        ${first ? '' : 'else '}if (__op == "${name}") { ${m.return === 'void' ? `${call}; __out += "null";` : `__out += lc::dump(${call});`} }`);
      first = false;
    }
    L.push('        else { __out += "null"; }');
    L.push('      }');
    L.push('      __out += "]";');
    L.push('      lc::result(__i, __out, "null", __t0);');
  } else {
    const params = spec.paramTypes;
    L.push('      const auto& __a = __tests[__i]["args"].arr();');
    params.forEach((t, k) => L.push(`      ${cppType(t)} __p${k} = lc::from<${cppType(t)}>(__a[${k}]);`));
    L.push('      Solution __sol;');
    const call = `__sol.${spec.name}(${params.map((_, k) => `__p${k}`).join(', ')})`;
    const mut = params.length ? `lc::dump(__p0)` : '"null"';
    if (spec.returnType === 'void') {
      L.push(`      ${call};`);
      L.push(`      lc::result(__i, "null", ${mut}, __t0);`);
    } else {
      L.push(`      auto __r = ${call};`);
      L.push(`      lc::result(__i, lc::dump(__r), ${mut}, __t0);`);
    }
  }
  L.push('    } catch (const std::exception& e) { lc::error(__i, std::string("exception: ") + e.what(), __t0); }');
  L.push('      catch (...) { lc::error(__i, "unknown exception", __t0); }');
  L.push('  }');
  L.push('  return 0;');
  L.push('}');
  return L.join('\n');
}
