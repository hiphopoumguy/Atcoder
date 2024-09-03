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
A = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(N + 1)]

# ‰Šú’l‚Ìİ’è
dp[1][0] = 0  # Å‰‚É“|‚³‚È‚¢ê‡
dp[1][1] = A[0]  # Å‰‚É“|‚·ê‡

for i in range(2, N + 1):
