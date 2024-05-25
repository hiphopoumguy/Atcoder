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

N = int(input())
A = list(map(int, input().split()))
for i in range(N-1):
    S, T = map(int, input().split())
    A[i+1] += (A[i] // S)* T
print(A[-1])
