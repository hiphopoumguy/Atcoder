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
d = int(input())
ans = d
list = []
for x in range(0, 2*10**6):
    list.append(x**2)

for x2 in list:
    y = d - x2
    yi = bisect.bisect_left(list, y)
    ans = min(ans, abs(x2+list[yi-1]-d), abs(x2+list[yi]-d))
