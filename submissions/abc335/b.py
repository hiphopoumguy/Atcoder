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
for i in range(n+1):
    for j in range(n+1):
        for k in range(n+1):
            if i+j+k <= n:
                print("{} {} {}".format(i, j, k))

