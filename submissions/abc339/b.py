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

h, w, n = map(int, input().split())

hokutounansei = [(-1, 0), (0, 1), (1, 0), (0, -1)]
grid = []
for x in range(h):
    grid.append(['.']*w)
now = [0, 0]
dir = 0
for _ in range(n):
