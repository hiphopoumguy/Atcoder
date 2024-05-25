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
A = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    ans = []
    for j in range(n):
        if A[i][j] == 1:
            ans.append(j+1)
    print(* ans)
