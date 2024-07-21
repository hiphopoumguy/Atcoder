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
r, g, b = map(int, input().split())
c = input()
if c == "Red":
    print(min(g, b))
elif c == "Green":
    print(min(r, b))
else:
    print(min(r, g))
