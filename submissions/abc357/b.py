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
upper = 0
s = input()
for c in s:
    if c.isupper():
        upper += 1
if upper > len(s) // 2:
    print(s.upper())
else:
    print(s.lower())
