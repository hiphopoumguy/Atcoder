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

n, a = map(int, input().split())
t = list(map(int, input().split()))
time = 0
for i in range(n):
    if t[i] < time:
        time += a
    else:
        time = t[i] + a
        
