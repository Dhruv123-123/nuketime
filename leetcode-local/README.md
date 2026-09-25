# LeetCode Local

A self-hosted LeetCode clone you can run offline: every free problem scraped from
leetcode.com (statement, examples, starter code in 19 languages, hints, tags,
acceptance, likes), a LeetCode-style UI with a Monaco editor, and a local judge
that runs your code in **Python 3, JavaScript, TypeScript, C++ and Java** against
the statement's example cases, with custom test cases, submissions history,
progress tracking, notes and study lists (Blind 75, NeetCode-style patterns,
Top Interview starter).

```
3,276 problems  ·  837 Easy  ·  1,656 Medium  ·  783 Hard  ·  3,073 auto-judgeable
```

> Problem statements are © LeetCode. This is for personal practice only.
> The scraper only uses LeetCode's public GraphQL endpoint for free (non-premium)
> problems and mirrors the statement images so the app works offline.

## Quick start

Requirements: Node ≥ 20 and Python 3 (for the scraper and Python judge). For the
other languages install what you want to use: `g++`, a JDK (`javac`/`java`).
TypeScript uses Node's built-in type stripping (Node ≥ 22.6).

```bash
cd leetcode-local
npm install
npm run build          # builds the web app once
npm start              # http://localhost:3000
```

Development mode (hot reload for the UI, API on :3000, UI on :5173):

```bash
npm run dev
```

### Docker (all compilers included)

```bash
docker compose up --build   # http://localhost:3000
```

Your progress, drafts and submissions are stored in `data/user/` (git-ignored),
so they survive rebuilds.

## Scraping / refreshing problems

The repo ships with the scraped data in `data/problems/` (one JSON per problem)
and mirrored images in `data/images/`. To refresh or re-scrape:

```bash
npm run scrape                                   # all free easy+medium+hard, resumable
python3 scraper/scrape.py --difficulty easy,medium --hard-limit 300
python3 scraper/scrape.py --only two-sum,lru-cache
python3 scraper/fetch_images.py                  # mirror statement images locally
```

Then restart the server (or `POST /api/reload`).

## How the judge works

- The example test cases from each problem (`exampleTestcases`) are paired with
  the expected outputs parsed from the statement. LeetCode's hidden tests are
  not public, so **Run** and **Submit** both use the examples plus any custom
  cases you add. A submission that passes all examples counts as *Accepted* and
  marks the problem solved.
- Each language has a harness that builds `ListNode`/`TreeNode` inputs from the
  LeetCode array notation, calls your `Solution` method (or drives a design
  class through its op list), serializes the result back and captures your
  `print`/`console.log`/`cout` output per test case. Void, in-place problems
  (`rotate`, `sortColors`, `removeDuplicates` with `k, nums = [...]`) are handled.
- Comparison is tolerant of float error, and when the statement says the answer
  can be returned in *any order* the comparison is order-insensitive. Problems
  that accept *multiple valid answers* show a mismatch as "unverified" rather
  than wrong.
- Time limit ≈ 10 s per run (plus 1.5 s per case). Code runs directly on your
  machine in a temp dir with no sandbox, exactly like running it yourself, so use
  the Docker setup if you want isolation.
- Not runnable locally (you can still write code and mark them solved): SQL /
  pandas / shell / concurrency problems, the "JavaScript" category, and the ~30
  problems that need LeetCode's custom node wiring (n-ary `Node`, graph `Node`,
  random pointers, linked-list cycles, interactive APIs). The UI tells you when
  a problem is in that group.

Optional: `pip install sortedcontainers` to get `SortedList` in Python like on
LeetCode.

## AI assistant (Azure OpenAI)

The **✨ AI** tab on every problem gives you a coach that sees the statement, your
current code and your latest run result: progressive **hints** (never the full
answer), **explain problem**, **debug my code** (root-causes failing cases),
**review solution** (complexity + improvements), **show solution**, and free
chat. Responses stream in, and any code block can be inserted into the editor.

It talks to an Azure OpenAI deployment through the Responses API. Put your
credentials in `leetcode-local/.env` (git-ignored; see `.env.example`):

```
AZURE_OPENAI_ENDPOINT=https://<resource>.services.ai.azure.com   # or the full /openai/v1/responses URL
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_MODEL=<deployment name>
AZURE_OPENAI_REASONING=low        # none | low | medium | high (reasoning models)
```

The key stays on the server; the browser only talks to `/api/ai/chat`. Chat
history is kept per problem in your browser.

## Keyboard shortcuts

| Keys | Action |
| --- | --- |
| `Ctrl + '` | Run against the test cases |
| `Ctrl + Enter` | Submit |

## Layout

```
scraper/          scrape.py (problems) · fetch_images.py (images)
data/problems/    one JSON per problem (statement, examples, snippets, metadata)
data/images/      mirrored statement images
data/user/        your progress, drafts, submissions, notes (git-ignored)
server/           Express API + judge (src/judge/langs, src/judge/harness)
web/              React + Vite + Tailwind + Monaco UI
```

### API

`GET /api/problems?q=&difficulty=Easy,Medium&tags=Array&status=solved&sort=acceptance&order=desc&page=1&list=blind-75`
`GET /api/problems/:slug` · `POST /api/problems/:slug/run` `{lang, code, testcases?}` ·
`POST /api/problems/:slug/submit` `{lang, code}` · `GET /api/problems/:slug/submissions` ·
`PUT /api/problems/:slug/draft` · `POST /api/problems/:slug/progress` `{status|starred|note}` ·
`GET /api/problems/random` · `GET /api/tags` · `GET /api/lists` · `GET /api/stats` · `GET /api/languages`

## Tests

```bash
npm test     # runs reference solutions in all 5 languages through the judge
```
