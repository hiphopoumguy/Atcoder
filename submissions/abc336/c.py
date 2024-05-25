import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from fractions import Fraction
from itertools import accumulate, combinations, permutations, product
mod = 998244353

n = int(input()) - 1
sin5 = []
while True:
    tmp = n % 5
    sin5.append(tmp)
    n //= 5
    if n == 0:
        break
ans = 0
for i in range(len(sin5)):
    ans += (sin5[i]*2) * (10**i)
