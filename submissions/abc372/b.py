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
M = int(input())
L = []
for i in range(10**5):
    if 3**i <= 10**5:
        L.append(3**i)
    else:
        break
ans = []
for i in range(len(L)-1, -1, -1):
    x = M // L[i]
