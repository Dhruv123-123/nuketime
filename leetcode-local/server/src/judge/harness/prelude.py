# ---- leetcode-local prelude (auto-generated, not part of your solution) ----
import sys, json, time, traceback, threading, io, os, math, re, bisect, heapq, functools, itertools, collections, string, random, operator
from typing import *
from collections import defaultdict, deque, Counter, OrderedDict
from functools import lru_cache, cache, reduce
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, product, accumulate
from math import inf, gcd, sqrt, ceil, floor, log2
from bisect import bisect_left, bisect_right, insort
try:
    from sortedcontainers import SortedList, SortedDict, SortedSet  # noqa: F401
except Exception:  # pragma: no cover
    pass
import sys as _sys
_sys.setrecursionlimit(1_000_000)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"ListNode({self.val})"


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"TreeNode({self.val})"


# ---- end prelude ----
