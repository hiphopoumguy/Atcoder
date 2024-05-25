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
xy = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    dist = 0
    for j in range(n):
        if i == j:
            continue
        ukrid = math.sqrt(abs((xy[i][0]-xy[j][0]) ** 2) + abs((xy[i][1]-xy[j][1]) ** 2))
        if dist < ukrid:
            dist = ukrid
