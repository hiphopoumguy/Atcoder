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

n, l, r = map(int, input().split())
ans = []

for i in range(1, l):
    ans.append(i)
    
for i in range(r, l-1, -1):
    ans.append(i)

