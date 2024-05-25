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

n, t = map(int, input().split())
d = defaultdict(int)
d[0] = n
s = [0] * (n+1)
ans = 1
for i in range(t):
    a, b = map(int, input().split())
    
    d[s[a]] -= 1
    if d[s[a]] == 0:
