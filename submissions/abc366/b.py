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
N = int(input())
S = [input() for _ in range(N)]
M = max(map(len, S))
T = [["*"] * N for _ in range(M)]
for i in range(N):
    for j in range(len(S[i])):
        T[j][N - i - 1] = S[i][j]
for i in range(M):
    while T[i][-1] == "*":
        T[i].pop()
