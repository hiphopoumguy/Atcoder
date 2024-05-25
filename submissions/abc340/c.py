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
@lru_cache
def re(N):
    if N == 1:
        return 0
    else:
        return re((N+1)//2) + re(N//2) + N
ans = re(N)
print(ans)
