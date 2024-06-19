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
stalls = [input().strip() for _ in range(n)]

stall_sets = []
for stall in stalls:
    stall_set = set(i for i, char in enumerate(stall) if char == 'o')
    stall_sets.append(stall_set)
all_flavors = set(range(m))

min_stalls = n
