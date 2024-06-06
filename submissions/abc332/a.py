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
n, s, k = map(int, input().split())
charge = 0
for _ in range(n):
    p, q = map(int, input().split())
    charge += p * q

if charge < s:
    charge += k
print(charge)
