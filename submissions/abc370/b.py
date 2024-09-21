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
A = [[0] for _ in range(N)]
for i in range(N):
    A[i] = list(map(int, input().split()))
genso = 0
for i in range(0, N):
    genso = A[max(genso, i)][min(genso, i)]-1
print(genso+1)
