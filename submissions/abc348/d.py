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

h, w = map(int, input().split())
grid = [input() for _ in range(h)]
for i in range(h):
    grid[i] = '#' + grid[i] + '#'
grid.insert(0, "#" * (w+2))
grid.append("#" * (w+2))
for i in range(h+2):
    for j in range(w+2):
        if grid[i][j] == 'S':
