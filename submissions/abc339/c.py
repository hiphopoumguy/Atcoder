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
a = list(map(int, input().split()))
now = 0
mn = 0
for x in a:
    now += x
    mn = min(mn, now)

print(now - mn)
