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

n, q = map(int, input().split())
A = list(map(int, input().split()))
d = defaultdict(int)
ans = []
for a in A:
    d[a] += 1
    
for a in range(n+1):
    if d[a] == 0:
