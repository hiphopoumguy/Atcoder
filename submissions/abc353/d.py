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
ans = 0
keta = 0
for i, x in enumerate(a[::-1]):
    ans += (n-i-1)*x + x*keta
    keta += 10**len(str(x))
    
print(ans%mod)
