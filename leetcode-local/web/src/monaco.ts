// Bundle Monaco locally (no CDN) so the app works fully offline.
import * as monaco from 'monaco-editor';
import { loader } from '@monaco-editor/react';
import editorWorker from 'monaco-editor/esm/vs/editor/editor.worker?worker';
import tsWorker from 'monaco-editor/esm/vs/language/typescript/ts.worker?worker';

self.MonacoEnvironment = {
  getWorker(_: unknown, label: string) {
    if (label === 'typescript' || label === 'javascript') return new tsWorker();
    return new editorWorker();
  },
};

// Keep TS/JS diagnostics quiet: LeetCode snippets rely on globals (ListNode, TreeNode) the editor can't see.
monaco.languages.typescript.javascriptDefaults.setDiagnosticsOptions({ noSemanticValidation: true, noSyntaxValidation: false });
monaco.languages.typescript.typescriptDefaults.setDiagnosticsOptions({ noSemanticValidation: true, noSyntaxValidation: false });
monaco.languages.typescript.typescriptDefaults.setCompilerOptions({ target: monaco.languages.typescript.ScriptTarget.ES2020, allowNonTsExtensions: true, noEmit: true });

monaco.editor.defineTheme('lc-dark', {
  base: 'vs-dark', inherit: true,
  rules: [],
  colors: { 'editor.background': '#1e1e1e', 'editorLineNumber.foreground': '#5a5a5a', 'editor.lineHighlightBackground': '#2a2a2a' },
});

loader.config({ monaco });
(window as unknown as { monaco: typeof monaco }).monaco = monaco; // handy for debugging / scripting
export { monaco };
