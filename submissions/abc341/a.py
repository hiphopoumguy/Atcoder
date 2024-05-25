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
ans = []
for i in range(N):
    ans.append('10')
ans.append('1')

print(''.join(ans))
