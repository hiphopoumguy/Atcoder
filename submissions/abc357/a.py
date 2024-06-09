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
n, m = map(int, input().split())
h = list(map(int, input().split()))
conv = m
for i in range(n):
    conv -= h[i]
    if conv < 0:
        print(i)
        sys.exit()
print(i+1)
