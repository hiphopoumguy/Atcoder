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
A = list(map(int, input().split()))
A.sort()
ans = sum(A) * (n - 1)
for i, a in enumerate(A):
    cnt = bisect.bisect_left(A, 10**8 - a)
    cnt = max(cnt, i + 1)
    ans -= (n - cnt) * 10**8
print(ans)
