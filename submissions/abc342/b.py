#!/usr/bin/env python3
import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from fractions import Fraction
from itertools import accumulate, combinations, permutations, product
mod = 998244353

n = int(input())
p = list(map(int, input().split()))
re_p = [0] * (n+1)
for i in range(n):
    re_p[p[i]] = i
q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    if re_p[a] > re_p[b]:
        print(b)
