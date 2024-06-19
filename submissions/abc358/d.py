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
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b)
ans = 0
bi = 0
for i in range(n):
    if bi == m:
