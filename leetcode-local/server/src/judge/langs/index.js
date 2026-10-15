// Language registry. Each language knows how to assemble a runnable program
// from the user's code + a harness, and how to compile/run it.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';
import { isDesign } from '../testcases.js';
import { cppDriver } from './cpp.js';
import { javaDriver } from './java.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const HARNESS = path.resolve(__dirname, '../harness');
const read = f => fs.readFileSync(path.join(HARNESS, f), 'utf8');

/** Build the spec object the dynamic-language drivers read from stdin. */
export function buildSpec(meta, tests) {
  if (isDesign(meta)) {
    const methods = {};
    for (const m of meta.methods || []) methods[m.name] = { params: (m.params || []).map(p => p.type), return: m.return?.type || 'void' };
    return {
      kind: 'design',
      classname: meta.classname,
      ctorTypes: (meta.constructor?.params || []).map(p => p.type),
      methods,
      tests: tests.map(t => ({ ops: t.ops, args: t.args })),
    };
  }
  return {
    kind: 'function',
    name: meta.name,
    paramTypes: (meta.params || []).map(p => p.type),
    returnType: meta.return?.type || 'void',
    tests: tests.map(t => ({ args: t.args })),
  };
}

const WIN = process.platform === 'win32';

/** Pick the Python executable once (python3 on POSIX, often just `python` on Windows). */
function detectPython() {
  for (const c of [process.env.LC_PYTHON, 'python3', 'python'].filter(Boolean)) {
    try { const r = spawnSync(c, ['--version'], { encoding: 'utf8' }); if (r.status === 0 && /Python 3/.test(r.stdout + r.stderr)) return c; } catch { /* next */ }
  }
  return 'python3';
}
export const PYTHON = detectPython();

/**
 * Build a run command. On POSIX we raise the stack limit (deep recursion is normal in
 * these problems) through a tiny sh wrapper; on Windows we spawn the program directly.
 */
const RUN = (cmd, args) => (WIN ? { cmd, args } : { cmd: 'sh', args: ['-c', 'ulimit -s unlimited 2>/dev/null || ulimit -s 1048576 2>/dev/null; exec "$0" "$@"', cmd, ...args] });
const COMPILE = (cmd, args) => ({ cmd, args });

export const LANGUAGES = {
  python3: {
    id: 'python3', name: 'Python 3', monaco: 'python', snippetKey: 'python3', supported: true,
    timeLimitMs: 10000,
    prepare(code, spec) {
      return {
        files: [{ name: 'main.py', content: read('prelude.py') + '\n' + code + '\n' + read('driver.py') }],
        run: RUN(PYTHON, ['main.py']),
      };
    },
  },
  javascript: {
    id: 'javascript', name: 'JavaScript', monaco: 'javascript', snippetKey: 'javascript', supported: true,
    timeLimitMs: 10000,
    prepare(code, spec) {
      return {
        files: [{ name: 'main.js', content: read('prelude.js') + code + '\n' + read('driver.js') }],
        run: RUN(process.execPath, ['--stack-size=65500', 'main.js']),
      };
    },
  },
  typescript: {
    id: 'typescript', name: 'TypeScript', monaco: 'typescript', snippetKey: 'typescript', supported: true,
    timeLimitMs: 10000,
    prepare(code, spec) {
      // Node 22 strips types natively; the harness itself is plain JS.
      const prelude = read('prelude.js').replace(/^function ListNode\(val, next\)/m, 'function ListNode(val?: any, next?: any)')
        .replace(/^function TreeNode\(val, left, right\)/m, 'function TreeNode(val?: any, left?: any, right?: any)');
      const driver = read('driver.js').replace('const fs = require', "const fs = require");
      return {
        files: [{ name: 'main.ts', content: '// @ts-nocheck\n' + prelude + code + '\n' + driver }],
        run: RUN(process.execPath, ['--stack-size=65500', '--experimental-strip-types', '--no-warnings', 'main.ts']),
      };
    },
  },
  cpp: {
    id: 'cpp', name: 'C++', monaco: 'cpp', snippetKey: 'cpp', supported: true,
    timeLimitMs: 6000,
    prepare(code, spec) {
      return {
        files: [
          { name: 'lc.hpp', content: read('lc.hpp') },
          { name: 'main.cpp', content: '#include "lc.hpp"\n// ---- your solution ----\n' + code + '\n' + cppDriver(spec) },
        ],
        compile: COMPILE('g++', ['-std=c++20', '-O2', '-o', 'main', 'main.cpp']),
        run: RUN(WIN ? 'main.exe' : './main', []),
      };
    },
  },
  java: {
    id: 'java', name: 'Java', monaco: 'java', snippetKey: 'java', supported: true,
    timeLimitMs: 10000,
    prepare(code, spec) {
      return {
        files: [{ name: 'Main.java', content: read('Main.java.tmpl').replace('/*__USER_CODE__*/', code).replace('/*__DRIVER__*/', javaDriver(spec)) }],
        compile: COMPILE('javac', ['-Xlint:none', '-encoding', 'UTF-8', 'Main.java']),
        run: { cmd: 'java', args: ['-Xss512m', '-XX:+UseSerialGC', '-XX:TieredStopAtLevel=1', '-Dfile.encoding=UTF-8', 'Main'] },
      };
    },
  },
};

export const LANGUAGE_LIST = Object.values(LANGUAGES).map(l => ({ id: l.id, name: l.name, monaco: l.monaco, supported: l.supported }));
export function getLanguage(id) { return LANGUAGES[id]; }
