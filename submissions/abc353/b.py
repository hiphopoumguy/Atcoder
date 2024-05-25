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

n, k = map(int, input().split())
a = list(map(int, input().split()))
cap = k
ans = 1
for i in range(n):
    if cap >= a[i]:
        cap = cap - a[i]
    else:
        ans += 1
