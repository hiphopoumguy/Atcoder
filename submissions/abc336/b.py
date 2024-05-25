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
sin2 = []
count = 0
while True:
    tmp = n % 2
    sin2.append(tmp)
    n //= 2
    if n == 0:
        break
    
