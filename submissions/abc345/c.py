#!/usr/bin/env python3
import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import cache
from fractions import Fraction
from itertools import accumulate, combinations, permutations, product
from sortedcontainers import SortedSet, SortedList, SortedDict
mod = 998244353
s = input()
d = defaultdict(int)
choice = len(s) * (len(s)-1) // 2
ans = choice

for c in s:
    d[c] += 1

for c in d:
    ans -= int(d[c]) * int(d[c]-1) // 2
