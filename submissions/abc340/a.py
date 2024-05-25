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

a, b, d = map(int, input().split())
ans = []
for i in range(a, b+1, d):
    ans.append(i)
    
print(*ans)
