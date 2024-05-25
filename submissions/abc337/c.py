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
A = list(map(int, input().split()))
reverse = [0] * (n+1)
for i in range(n):
    if A[i] == -1:
        x = i + 1
    else:
        reverse[A[i]] = i + 1
ans = [x]
for i in range(n-1):
