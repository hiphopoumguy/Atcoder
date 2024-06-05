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
r = sorted(list(map(int, input().split())))

sum = [r[0]]
for i in range(1, n):
    sum.append(r[i]+sum[i-1])

for _ in range(q):
    query = int(input())
    print(bisect.bisect_right(sum, query))
