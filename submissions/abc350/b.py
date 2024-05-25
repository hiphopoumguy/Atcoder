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
t = list(map(int, input().split()))
d = defaultdict(int)

for x in t:
    if d[x] == 0:
        d[x] = 1
    elif d[x] == 1:
        d[x] = 0

