#!/usr/bin/env python3
import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from fractions import Fraction
from itertools import accumulate, combinations, permutations, product
mod = 998244353
n = int(input())
num = 0
ans = [[0] * n for _ in range(n)]
for i in range(0, n//2):
    for j in range(i, n-i):
        num += 1
        ans[i][j] = num
    
    for j in range(i+1, n-i):
        num += 1
        ans[j][n-i-1] = num
