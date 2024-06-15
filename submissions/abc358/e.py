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
K = int(input())
C = list(map(int, input().split()))

fact = [1] * (K + 1)
for i in range(K):
    fact[i + 1] = fact[i] * (i + 1) % mod
ifact = [1] * (K + 1)
ifact[K] = pow(fact[K], -1, mod)
for i in range(K, 0, -1):
    ifact[i - 1] = ifact[i] * i % mod
