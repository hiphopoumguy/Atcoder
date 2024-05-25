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
for i in s:
    d[i] += 1
for i in range(101):
    ans_count = 0
    for char, cnt in d.items():
        if i == cnt:
            ans_count += 1
