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

Q = int(input())
counter = Counter()
ans = 0

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        if counter[q[1]] == 0:
            ans += 1
