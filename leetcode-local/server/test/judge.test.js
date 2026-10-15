import { test } from 'node:test';
import assert from 'node:assert/strict';
import { loadProblems, getProblem } from '../src/problems.js';
import { runJudge } from '../src/judge/index.js';
import { buildExampleTests } from '../src/judge/testcases.js';

loadProblems();

const SOLUTIONS = {
  'two-sum': {
    python3: `class Solution:\n    def twoSum(self, nums, target):\n        seen = {}\n        for i, x in enumerate(nums):\n            if target - x in seen: return [seen[target-x], i]\n            seen[x] = i\n`,
    javascript: `var twoSum = function(nums, target) { const m = new Map(); for (let i = 0; i < nums.length; i++) { if (m.has(target - nums[i])) return [m.get(target - nums[i]), i]; m.set(nums[i], i); } };`,
    typescript: `function twoSum(nums: number[], target: number): number[] { const m = new Map<number, number>(); for (let i = 0; i < nums.length; i++) { const j = m.get(target - nums[i]); if (j !== undefined) return [j, i]; m.set(nums[i], i); } return []; }`,
    cpp: `class Solution {\npublic:\n    vector<int> twoSum(vector<int>& nums, int target) {\n        unordered_map<int,int> m; for (int i = 0; i < (int)nums.size(); i++) { auto it = m.find(target - nums[i]); if (it != m.end()) return {it->second, i}; m[nums[i]] = i; } return {};\n    }\n};`,
    java: `class Solution {\n    public int[] twoSum(int[] nums, int target) {\n        Map<Integer,Integer> m = new HashMap<>(); for (int i = 0; i < nums.length; i++) { Integer j = m.get(target - nums[i]); if (j != null) return new int[]{j, i}; m.put(nums[i], i); } return new int[0];\n    }\n}`,
  },
  'add-two-numbers': {
    python3: `class Solution:\n    def addTwoNumbers(self, l1, l2):\n        d = ListNode(); cur = d; c = 0\n        while l1 or l2 or c:\n            s = c + (l1.val if l1 else 0) + (l2.val if l2 else 0)\n            cur.next = ListNode(s % 10); cur = cur.next; c = s // 10\n            l1 = l1.next if l1 else None; l2 = l2.next if l2 else None\n        return d.next\n`,
    javascript: `var addTwoNumbers = function(l1, l2) { const d = new ListNode(); let cur = d, c = 0; while (l1 || l2 || c) { const s = c + (l1 ? l1.val : 0) + (l2 ? l2.val : 0); cur.next = new ListNode(s % 10); cur = cur.next; c = Math.floor(s / 10); l1 = l1 && l1.next; l2 = l2 && l2.next; } return d.next; };`,
    cpp: `class Solution {\npublic:\n    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) { ListNode d; ListNode* cur = &d; int c = 0; while (l1 || l2 || c) { int s = c + (l1 ? l1->val : 0) + (l2 ? l2->val : 0); cur->next = new ListNode(s % 10); cur = cur->next; c = s / 10; if (l1) l1 = l1->next; if (l2) l2 = l2->next; } return d.next; }\n};`,
    java: `class Solution {\n    public ListNode addTwoNumbers(ListNode l1, ListNode l2) { ListNode d = new ListNode(), cur = d; int c = 0; while (l1 != null || l2 != null || c != 0) { int s = c + (l1 != null ? l1.val : 0) + (l2 != null ? l2.val : 0); cur.next = new ListNode(s % 10); cur = cur.next; c = s / 10; if (l1 != null) l1 = l1.next; if (l2 != null) l2 = l2.next; } return d.next; }\n}`,
  },
  'lru-cache': {
    python3: `class LRUCache:\n    def __init__(self, capacity: int):\n        self.c = capacity; self.d = OrderedDict()\n    def get(self, key: int) -> int:\n        if key not in self.d: return -1\n        self.d.move_to_end(key); return self.d[key]\n    def put(self, key: int, value: int) -> None:\n        self.d[key] = value; self.d.move_to_end(key)\n        if len(self.d) > self.c: self.d.popitem(last=False)\n`,
    javascript: `var LRUCache = function(capacity) { this.c = capacity; this.m = new Map(); };\nLRUCache.prototype.get = function(key) { if (!this.m.has(key)) return -1; const v = this.m.get(key); this.m.delete(key); this.m.set(key, v); return v; };\nLRUCache.prototype.put = function(key, value) { this.m.delete(key); this.m.set(key, value); if (this.m.size > this.c) this.m.delete(this.m.keys().next().value); };`,
    cpp: `class LRUCache {\n    int cap; list<pair<int,int>> l; unordered_map<int, list<pair<int,int>>::iterator> m;\npublic:\n    LRUCache(int capacity) : cap(capacity) {}\n    int get(int key) { auto it = m.find(key); if (it == m.end()) return -1; l.splice(l.begin(), l, it->second); return it->second->second; }\n    void put(int key, int value) { auto it = m.find(key); if (it != m.end()) { it->second->second = value; l.splice(l.begin(), l, it->second); return; } l.push_front({key, value}); m[key] = l.begin(); if ((int)l.size() > cap) { m.erase(l.back().first); l.pop_back(); } }\n};`,
    java: `class LRUCache {\n    LinkedHashMap<Integer,Integer> m; int cap;\n    public LRUCache(int capacity) { cap = capacity; m = new LinkedHashMap<>(16, 0.75f, true); }\n    public int get(int key) { return m.getOrDefault(key, -1); }\n    public void put(int key, int value) { m.put(key, value); if (m.size() > cap) { int k = m.keySet().iterator().next(); m.remove(k); } }\n}`,
  },
  'rotate-image': {
    python3: `class Solution:\n    def rotate(self, matrix):\n        matrix[:] = [list(r) for r in zip(*matrix[::-1])]\n`,
    javascript: `var rotate = function(matrix) { const n = matrix.length; const r = matrix.map(row => row.slice()); for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) matrix[j][n-1-i] = r[i][j]; };`,
    cpp: `class Solution {\npublic:\n    void rotate(vector<vector<int>>& matrix) { int n = matrix.size(); auto r = matrix; for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) matrix[j][n-1-i] = r[i][j]; }\n};`,
    java: `class Solution {\n    public void rotate(int[][] matrix) { int n = matrix.length; int[][] r = new int[n][]; for (int i = 0; i < n; i++) r[i] = matrix[i].clone(); for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) matrix[j][n-1-i] = r[i][j]; }\n}`,
  },
  'remove-duplicates-from-sorted-array': {
    python3: `class Solution:\n    def removeDuplicates(self, nums):\n        k = 0\n        for x in nums:\n            if k == 0 or nums[k-1] != x: nums[k] = x; k += 1\n        return k\n`,
    javascript: `var removeDuplicates = function(nums) { let k = 0; for (const x of nums) { if (k === 0 || nums[k-1] !== x) nums[k++] = x; } return k; };`,
    cpp: `class Solution {\npublic:\n    int removeDuplicates(vector<int>& nums) { int k = 0; for (int x : nums) if (k == 0 || nums[k-1] != x) nums[k++] = x; return k; }\n};`,
    java: `class Solution {\n    public int removeDuplicates(int[] nums) { int k = 0; for (int x : nums) if (k == 0 || nums[k-1] != x) nums[k++] = x; return k; }\n}`,
  },
  'median-of-two-sorted-arrays': {
    python3: `class Solution:\n    def findMedianSortedArrays(self, a, b):\n        c = sorted(a + b); n = len(c)\n        return (c[n//2] + c[(n-1)//2]) / 2\n`,
    javascript: `var findMedianSortedArrays = function(a, b) { const c = [...a, ...b].sort((x, y) => x - y); const n = c.length; return (c[Math.floor(n/2)] + c[Math.floor((n-1)/2)]) / 2; };`,
    cpp: `class Solution {\npublic:\n    double findMedianSortedArrays(vector<int>& a, vector<int>& b) { vector<int> c(a); c.insert(c.end(), b.begin(), b.end()); sort(c.begin(), c.end()); int n = c.size(); return (c[n/2] + c[(n-1)/2]) / 2.0; }\n};`,
    java: `class Solution {\n    public double findMedianSortedArrays(int[] a, int[] b) { int[] c = new int[a.length + b.length]; System.arraycopy(a, 0, c, 0, a.length); System.arraycopy(b, 0, c, a.length, b.length); Arrays.sort(c); int n = c.length; return (c[n/2] + c[(n-1)/2]) / 2.0; }\n}`,
  },
  'invert-binary-tree': {
    python3: `class Solution:\n    def invertTree(self, root):\n        if root: root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)\n        return root\n`,
    javascript: `var invertTree = function(root) { if (!root) return null; const l = invertTree(root.left); root.left = invertTree(root.right); root.right = l; return root; };`,
    cpp: `class Solution {\npublic:\n    TreeNode* invertTree(TreeNode* root) { if (!root) return nullptr; TreeNode* l = invertTree(root->left); root->left = invertTree(root->right); root->right = l; return root; }\n};`,
    java: `class Solution {\n    public TreeNode invertTree(TreeNode root) { if (root == null) return null; TreeNode l = invertTree(root.left); root.left = invertTree(root.right); root.right = l; return root; }\n}`,
  },
  'number-of-islands': {
    python3: `class Solution:\n    def numIslands(self, grid):\n        n, m = len(grid), len(grid[0]); c = 0\n        def dfs(i, j):\n            if 0 <= i < n and 0 <= j < m and grid[i][j] == '1':\n                grid[i][j] = '0'; dfs(i+1,j); dfs(i-1,j); dfs(i,j+1); dfs(i,j-1)\n        for i in range(n):\n            for j in range(m):\n                if grid[i][j] == '1': c += 1; dfs(i, j)\n        return c\n`,
    javascript: `var numIslands = function(grid) { const n = grid.length, m = grid[0].length; let c = 0; const dfs = (i, j) => { if (i < 0 || j < 0 || i >= n || j >= m || grid[i][j] !== '1') return; grid[i][j] = '0'; dfs(i+1,j); dfs(i-1,j); dfs(i,j+1); dfs(i,j-1); }; for (let i = 0; i < n; i++) for (let j = 0; j < m; j++) if (grid[i][j] === '1') { c++; dfs(i, j); } return c; };`,
    cpp: `class Solution {\npublic:\n    void dfs(vector<vector<char>>& g, int i, int j) { if (i < 0 || j < 0 || i >= (int)g.size() || j >= (int)g[0].size() || g[i][j] != '1') return; g[i][j] = '0'; dfs(g,i+1,j); dfs(g,i-1,j); dfs(g,i,j+1); dfs(g,i,j-1); }\n    int numIslands(vector<vector<char>>& grid) { int c = 0; for (int i = 0; i < (int)grid.size(); i++) for (int j = 0; j < (int)grid[0].size(); j++) if (grid[i][j] == '1') { c++; dfs(grid, i, j); } return c; }\n};`,
    java: `class Solution {\n    void dfs(char[][] g, int i, int j) { if (i < 0 || j < 0 || i >= g.length || j >= g[0].length || g[i][j] != '1') return; g[i][j] = '0'; dfs(g,i+1,j); dfs(g,i-1,j); dfs(g,i,j+1); dfs(g,i,j-1); }\n    public int numIslands(char[][] grid) { int c = 0; for (int i = 0; i < grid.length; i++) for (int j = 0; j < grid[0].length; j++) if (grid[i][j] == '1') { c++; dfs(grid, i, j); } return c; }\n}`,
  },
  'valid-anagram': {
    python3: `class Solution:\n    def isAnagram(self, s, t):\n        return sorted(s) == sorted(t)\n`,
    javascript: `var isAnagram = function(s, t) { return s.split('').sort().join('') === t.split('').sort().join(''); };`,
    cpp: `class Solution {\npublic:\n    bool isAnagram(string s, string t) { sort(s.begin(), s.end()); sort(t.begin(), t.end()); return s == t; }\n};`,
    java: `class Solution {\n    public boolean isAnagram(String s, String t) { char[] a = s.toCharArray(), b = t.toCharArray(); Arrays.sort(a); Arrays.sort(b); return Arrays.equals(a, b); }\n}`,
  },
  'group-anagrams': {
    python3: `class Solution:\n    def groupAnagrams(self, strs):\n        d = defaultdict(list)\n        for s in strs: d[''.join(sorted(s))].append(s)\n        return list(d.values())\n`,
    javascript: `var groupAnagrams = function(strs) { const m = new Map(); for (const s of strs) { const k = s.split('').sort().join(''); if (!m.has(k)) m.set(k, []); m.get(k).push(s); } return [...m.values()]; };`,
    cpp: `class Solution {\npublic:\n    vector<vector<string>> groupAnagrams(vector<string>& strs) { unordered_map<string, vector<string>> m; for (auto& s : strs) { string k = s; sort(k.begin(), k.end()); m[k].push_back(s); } vector<vector<string>> r; for (auto& p : m) r.push_back(p.second); return r; }\n};`,
    java: `class Solution {\n    public List<List<String>> groupAnagrams(String[] strs) { Map<String, List<String>> m = new HashMap<>(); for (String s : strs) { char[] c = s.toCharArray(); Arrays.sort(c); m.computeIfAbsent(new String(c), k -> new ArrayList<>()).add(s); } return new ArrayList<>(m.values()); }\n}`,
  },
};

const LANGS = ['python3', 'javascript', 'typescript', 'cpp', 'java'];

for (const [slug, sols] of Object.entries(SOLUTIONS)) {
  for (const lang of LANGS) {
    const code = sols[lang] || (lang === 'typescript' ? sols.javascript : null);
    if (!code) continue;
    test(`${slug} [${lang}]`, async () => {
      const problem = getProblem(slug);
      assert.ok(problem, `problem ${slug} not loaded`);
      const tests = buildExampleTests(problem);
      const r = await runJudge({ problem, langId: lang, code, tests });
      const detail = JSON.stringify(r.tests.map(t => ({ s: t.status, out: t.output, exp: t.expected, err: t.error })), null, 0);
      assert.equal(r.status, 'Accepted', `${r.status}: ${r.compileError || ''} ${detail}`);
    });
  }
}

test('C++ design class with vector& constructor argument compiles and runs', async () => {
  const problem = getProblem('shuffle-an-array');
  const code = 'class Solution {\n    vector<int> orig;\npublic:\n    Solution(vector<int>& nums) : orig(nums) {}\n    vector<int> reset() { return orig; }\n    vector<int> shuffle() { return orig; }\n};';
  const r = await runJudge({ problem, langId: 'cpp', code, tests: buildExampleTests(problem) });
  assert.notEqual(r.status, 'Compile Error', r.compileError);
  assert.deepEqual(r.tests[0].output[2], [1, 2, 3]);
});

test('wrong answer is detected', async () => {
  const problem = getProblem('two-sum');
  const r = await runJudge({ problem, langId: 'python3', code: 'class Solution:\n    def twoSum(self, nums, target):\n        return [0, 0]\n', tests: buildExampleTests(problem) });
  assert.equal(r.status, 'Wrong Answer');
});

test('runtime error is reported', async () => {
  const problem = getProblem('two-sum');
  const r = await runJudge({ problem, langId: 'javascript', code: 'var twoSum = function(nums, target) { return nums.foo.bar; };', tests: buildExampleTests(problem) });
  assert.equal(r.status, 'Runtime Error');
  assert.match(r.tests[0].error, /TypeError/);
});

test('compile error is reported', async () => {
  const problem = getProblem('two-sum');
  const r = await runJudge({ problem, langId: 'cpp', code: 'class Solution { public: vector<int> twoSum(vector<int>& nums, int target) { return oops; } };', tests: buildExampleTests(problem) });
  assert.equal(r.status, 'Compile Error');
});

test('infinite loop hits the time limit', async () => {
  const problem = getProblem('two-sum');
  const r = await runJudge({ problem, langId: 'python3', code: 'class Solution:\n    def twoSum(self, nums, target):\n        while True: pass\n', tests: buildExampleTests(problem).slice(0, 1) });
  assert.equal(r.status, 'Time Limit Exceeded');
});

test('stdout is captured per test', async () => {
  const problem = getProblem('two-sum');
  const r = await runJudge({ problem, langId: 'python3', code: 'class Solution:\n    def twoSum(self, nums, target):\n        print("hi", nums)\n        return [0, 1]\n', tests: buildExampleTests(problem).slice(0, 1) });
  assert.match(r.tests[0].stdout, /hi \[2, 7, 11, 15\]/);
});
