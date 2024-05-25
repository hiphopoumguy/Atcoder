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

n = int(input())
ac = [list(map(int, input().split())) for _ in range(n)]

d = defaultdict(lambda: 10 ** 9)
for i in range(n):
    d[ac[i][1]] = min(d[ac[i][1]], ac[i][0])
    
print(max(d.values()))
