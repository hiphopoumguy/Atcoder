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

s = input()
if s[0].isupper():
    if s[1:].islower() or len(s) == 1:
        print('Yes')
        sys.exit()
print('No')
