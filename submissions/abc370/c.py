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
S = input()
T = input()
S = list(S)
T = list(T)
X = []
for i in range(len(S)):
    if S[i] > T[i]:
        S[i] = T[i]
        x = "".join(S)
        X.append([x])
