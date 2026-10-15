#!/usr/bin/env python3
"""
Scrape LeetCode problems (free / non-premium) via the public GraphQL API into
data/problems/<id>-<slug>.json.

Usage:
  python3 scraper/scrape.py                      # all free easy + medium + hard
  python3 scraper/scrape.py --difficulty easy,medium --hard-limit 300
  python3 scraper/scrape.py --resume             # skip problems already on disk
  python3 scraper/scrape.py --only two-sum,lru-cache

Only the problem statement, starter code, example test cases and metadata are
fetched. Premium problems (isPaidOnly) are skipped because their content is not
available without a subscription. Be nice to LeetCode: keep concurrency low.
"""
import argparse
import html as htmlmod
import json
import os
import random
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

GRAPHQL = "https://leetcode.com/graphql"
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Referer": "https://leetcode.com/problemset/",
    "Origin": "https://leetcode.com",
}

LIST_QUERY = """
query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
  problemsetQuestionList: questionList(categorySlug: $categorySlug, limit: $limit, skip: $skip, filters: $filters) {
    total: totalNum
    questions: data {
      questionId
      questionFrontendId
      title
      titleSlug
      difficulty
      isPaidOnly
      acRate
      topicTags { name slug }
    }
  }
}
"""

DETAIL_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    title
    titleSlug
    difficulty
    isPaidOnly
    content
    exampleTestcases
    sampleTestCase
    metaData
    codeSnippets { lang langSlug code }
    hints
    similarQuestions
    topicTags { name slug }
    stats
    likes
    dislikes
    categoryTitle
  }
}
"""

_thread_local = threading.local()


def session() -> requests.Session:
    s = getattr(_thread_local, "s", None)
    if s is None:
        s = requests.Session()
        s.headers.update(HEADERS)
        _thread_local.s = s
    return s


def gql(query: str, variables: dict, retries: int = 6):
    delay = 1.5
    last_err = None
    for attempt in range(retries):
        try:
            r = session().post(GRAPHQL, json={"query": query, "variables": variables}, timeout=30)
            if r.status_code == 200:
                body = r.json()
                if "errors" in body and not body.get("data"):
                    raise RuntimeError(body["errors"])
                return body["data"]
            if r.status_code in (429, 403, 500, 502, 503, 504):
                last_err = f"HTTP {r.status_code}"
            else:
                r.raise_for_status()
        except Exception as e:  # noqa: BLE001
            last_err = e
        time.sleep(delay + random.random())
        delay = min(delay * 2, 30)
    raise RuntimeError(f"giving up: {last_err}")


def fetch_list(difficulty: str | None = None):
    out = []
    skip, limit = 0, 100
    filters = {}
    if difficulty:
        filters["difficulty"] = difficulty.upper()
    while True:
        data = gql(LIST_QUERY, {"categorySlug": "", "limit": limit, "skip": skip, "filters": filters})
        page = data["problemsetQuestionList"]
        out.extend(page["questions"])
        skip += limit
        if skip >= page["total"] or not page["questions"]:
            break
    return out


TAG_RE = re.compile(r"<[^>]+>")


def html_to_text(s: str) -> str:
    s = re.sub(r"<\s*(br|/p|/pre|/div|/li|/tr)\s*/?>", "\n", s, flags=re.I)
    s = TAG_RE.sub("", s)
    s = htmlmod.unescape(s).replace("\xa0", " ")
    return s


EXAMPLE_RE = re.compile(
    r"Input:?\s*(?P<input>.*?)\n\s*Output:?\s*(?P<output>.*?)(?=\n\s*(?:Explanation|Explaination|Example|Constraints|Note|Follow[- ]up)\b|\n\s*\n|\Z)",
    re.S | re.I,
)


def parse_examples(content: str | None):
    """Pull (input, output) pairs out of the problem statement's examples."""
    if not content:
        return []
    text = html_to_text(content)
    examples = []
    for m in EXAMPLE_RE.finditer(text):
        inp = " ".join(line.strip() for line in m.group("input").strip().splitlines() if line.strip())
        outp = m.group("output").strip()
        # keep the first line for single-line answers, but allow multi-line matrices
        outp = "\n".join(line.strip() for line in outp.splitlines() if line.strip())
        if outp:
            examples.append({"input": inp, "output": outp})
    return examples


def fetch_detail(slug: str) -> dict:
    q = gql(DETAIL_QUERY, {"titleSlug": slug})["question"]
    if q is None:
        raise RuntimeError(f"no question for slug {slug}")
    meta = None
    try:
        meta = json.loads(q["metaData"]) if q.get("metaData") else None
    except json.JSONDecodeError:
        meta = None
    stats = None
    try:
        stats = json.loads(q["stats"]) if q.get("stats") else None
    except json.JSONDecodeError:
        pass
    similar = []
    try:
        similar = json.loads(q["similarQuestions"]) if q.get("similarQuestions") else []
    except json.JSONDecodeError:
        pass
    return {
        "id": int(q["questionFrontendId"]),
        "internalId": int(q["questionId"]),
        "title": q["title"],
        "slug": q["titleSlug"],
        "difficulty": q["difficulty"],
        "paidOnly": bool(q["isPaidOnly"]),
        "category": q.get("categoryTitle"),
        "tags": [t["name"] for t in q.get("topicTags") or []],
        "tagSlugs": [t["slug"] for t in q.get("topicTags") or []],
        "content": q.get("content"),
        "exampleTestcases": q.get("exampleTestcases") or "",
        "sampleTestCase": q.get("sampleTestCase") or "",
        "examples": parse_examples(q.get("content")),
        "metaData": meta,
        "codeSnippets": {c["langSlug"]: c["code"] for c in (q.get("codeSnippets") or [])},
        "hints": q.get("hints") or [],
        "similar": [{"title": s["title"], "slug": s["titleSlug"], "difficulty": s["difficulty"]} for s in similar],
        "stats": {
            "acRate": (stats or {}).get("acRate"),
            "totalAccepted": (stats or {}).get("totalAcceptedRaw"),
            "totalSubmissions": (stats or {}).get("totalSubmissionRaw"),
        },
        "likes": q.get("likes"),
        "dislikes": q.get("dislikes"),
        "url": f"https://leetcode.com/problems/{q['titleSlug']}/",
        "scrapedAt": int(time.time()),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "data", "problems"))
    ap.add_argument("--difficulty", default="easy,medium,hard", help="comma list of easy,medium,hard")
    ap.add_argument("--hard-limit", type=int, default=0, help="only take the N lowest-numbered hard problems (0 = all)")
    ap.add_argument("--limit", type=int, default=0, help="stop after N problems total (debug)")
    ap.add_argument("--concurrency", type=int, default=4)
    ap.add_argument("--resume", action="store_true", help="skip slugs already written to --out")
    ap.add_argument("--only", default="", help="comma list of slugs to fetch (ignores other filters)")
    ap.add_argument("--include-paid", action="store_true", help="try premium problems too (content will be empty)")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    wanted = {d.strip().lower() for d in args.difficulty.split(",") if d.strip()}

    print("Fetching problem list...", flush=True)
    if args.only:
        targets = [{"titleSlug": s.strip(), "difficulty": "?", "questionFrontendId": "?", "isPaidOnly": False}
                   for s in args.only.split(",") if s.strip()]
    else:
        listing = fetch_list()
        print(f"  {len(listing)} problems on LeetCode", flush=True)
        targets = []
        hard_seen = 0
        for q in sorted(listing, key=lambda x: int(x["questionFrontendId"])):
            if q["isPaidOnly"] and not args.include_paid:
                continue
            d = q["difficulty"].lower()
            if d not in wanted:
                continue
            if d == "hard" and args.hard_limit and hard_seen >= args.hard_limit:
                continue
            if d == "hard":
                hard_seen += 1
            targets.append(q)
    if args.limit:
        targets = targets[: args.limit]

    existing = set()
    if args.resume:
        for fn in os.listdir(args.out):
            if fn.endswith(".json"):
                existing.add(fn.rsplit("-", 1)[-1][:-5] if False else fn)
    # existing filenames are "<id>-<slug>.json"; match on slug
    existing_slugs = {fn[:-5].split("-", 1)[1] for fn in existing if "-" in fn}
    todo = [t for t in targets if not (args.resume and t["titleSlug"] in existing_slugs)]
    print(f"  {len(targets)} selected, {len(todo)} to fetch", flush=True)

    ok = fail = 0
    failures = []
    lock = threading.Lock()

    def work(q):
        slug = q["titleSlug"]
        detail = fetch_detail(slug)
        if detail["paidOnly"] and not detail["content"]:
            return slug, "paid"
        fn = os.path.join(args.out, f"{detail['id']}-{slug}.json")
        tmp = fn + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(detail, f, ensure_ascii=False)
        os.replace(tmp, fn)
        return slug, "ok"

    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        futs = {ex.submit(work, q): q for q in todo}
        for i, fut in enumerate(as_completed(futs), 1):
            q = futs[fut]
            try:
                slug, status = fut.result()
                with lock:
                    if status == "ok":
                        ok += 1
                    else:
                        fail += 1
                        failures.append((slug, status))
            except Exception as e:  # noqa: BLE001
                with lock:
                    fail += 1
                    failures.append((q["titleSlug"], str(e)))
            if i % 25 == 0 or i == len(todo):
                el = time.time() - t0
                print(f"  [{i}/{len(todo)}] ok={ok} fail={fail} {el:.0f}s", flush=True)

    manifest = {
        "scrapedAt": int(time.time()),
        "selected": len(targets),
        "fetched": ok,
        "failed": failures,
        "difficulties": sorted(wanted),
        "hardLimit": args.hard_limit,
    }
    with open(os.path.join(args.out, "..", "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"Done. ok={ok} fail={fail}")
    if failures:
        print("Failures:")
        for s, e in failures[:50]:
            print("  ", s, e)


if __name__ == "__main__":
    main()
