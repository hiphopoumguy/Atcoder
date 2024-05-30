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
n, t = map(int, input().split())
a = list(map(int, input().split()))
bingo = []
for i in range(0, n):
    bingo.append([])
    x = n * i
    for j in range(1, n+1):
        bingo[i].append(x+j)

row_cnt = [0] * n
