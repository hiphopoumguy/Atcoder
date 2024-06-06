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
k, g, m = map(int, input().split())
glass = 0
cup = 0
for _ in range(k):
    if glass == g:
        glass = 0
    elif cup == 0:
        cup = m
    elif g - glass > cup:
        glass += cup
