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
N, Q = map(int, input().split())
S = input()
cnt = 0
for i in range(N-2):
    if S[i:i+3] == "ABC":
        cnt += 1
S = list(S)
for i in range(Q):
    X, C = map(str, input().split())
    X = int(X)-1
