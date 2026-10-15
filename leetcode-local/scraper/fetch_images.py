#!/usr/bin/env python3
"""
Mirror images referenced by problem statements into data/images so the app
works fully offline. The server rewrites <img src> to /images/<file> when the
file exists locally.

Usage: python3 scraper/fetch_images.py [--concurrency 8]
"""
import argparse
import hashlib
import json
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

ROOT = os.path.join(os.path.dirname(__file__), '..', 'data')
PROBLEMS = os.path.join(ROOT, 'problems')
IMAGES = os.path.join(ROOT, 'images')
IMG_RE = re.compile(r'<img[^>]+src="([^"]+)"')


def local_name(url: str) -> str:
    ext = os.path.splitext(url.split('?')[0])[1].lower() or '.img'
    if len(ext) > 6:
        ext = '.img'
    return hashlib.sha1(url.encode()).hexdigest()[:16] + ext


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--concurrency', type=int, default=8)
    args = ap.parse_args()
    os.makedirs(IMAGES, exist_ok=True)
    urls = set()
    for fn in os.listdir(PROBLEMS):
        if not fn.endswith('.json'):
            continue
        with open(os.path.join(PROBLEMS, fn), encoding='utf-8') as f:
            content = json.load(f).get('content') or ''
        for u in IMG_RE.findall(content):
            if u.startswith('http'):
                urls.add(u)
    todo = [u for u in urls if not os.path.exists(os.path.join(IMAGES, local_name(u)))]
    print(f'{len(urls)} image urls, {len(todo)} to download')
    s = requests.Session()
    s.headers.update({'User-Agent': 'Mozilla/5.0', 'Referer': 'https://leetcode.com/'})

    def get(u):
        for attempt in range(4):
            try:
                r = s.get(u, timeout=30)
                if r.status_code == 200 and r.content:
                    tmp = os.path.join(IMAGES, local_name(u) + '.tmp')
                    with open(tmp, 'wb') as f:
                        f.write(r.content)
                    os.replace(tmp, os.path.join(IMAGES, local_name(u)))
                    return True
                if r.status_code == 404:
                    return False
            except Exception:
                pass
            time.sleep(1.5 * (attempt + 1))
        return False

    ok = 0
    with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        futs = {ex.submit(get, u): u for u in todo}
        for i, fut in enumerate(as_completed(futs), 1):
            ok += bool(fut.result())
            if i % 100 == 0 or i == len(todo):
                print(f'  [{i}/{len(todo)}] ok={ok}', flush=True)
    index = {u: local_name(u) for u in urls if os.path.exists(os.path.join(IMAGES, local_name(u)))}
    with open(os.path.join(ROOT, 'images.json'), 'w') as f:
        json.dump(index, f, indent=0, sort_keys=True)
    print(f'done: {len(index)} images available locally')


if __name__ == '__main__':
    main()
