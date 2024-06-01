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
n, m, k = map(int, input().split())
x = [list(map(str, input().split())) for _ in range(m)]
test = []
for i in range(m):
    c = int(x[i][0])
    keys = list(map(int, x[i][1:c+1]))
    r = x[i][c+1]
    test.append((c, keys, r))

valid_combinations = 0
