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

ans = 1
for i in range(10**7):
    cubic = i ** 3
    if cubic > n:
        break
    char_cubic = str(cubic)
    if char_cubic == char_cubic[::-1]:
        ans = cubic
