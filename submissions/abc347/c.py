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
n, a, b = map(int, input().split())
d = list(map(int, input().split()))

week = a+b
D = sorted([x % week for x in d])
D.append(week + D[0])
for i in range(n):
    if D[i+1] - D[i] > b:
        print("Yes")
        sys.exit()
