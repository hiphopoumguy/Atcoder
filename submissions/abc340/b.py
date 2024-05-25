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

Q = int(input())
q = [list(map(int, input().split())) for l in range(Q)]

ans = []
for i in range(Q):
    if q[i][0] == 1:
        ans.append(q[i][1])
    else:
        print(ans[-q[i][1]])
