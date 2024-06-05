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
re = [int("1" * i) for i in range(1, 13)]
s = set()
for i in range(12):
    for j in range(12):
        for k in range(12):
            s.add(re[i] + re[j] + re[k])
print(sorted(s)[n-1])
