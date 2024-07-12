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

a.sort()
ans = 10 ** 9
for i in range(k+1):
    ans = min(a[i+n-k-1] - a[i], ans)
print(ans)
