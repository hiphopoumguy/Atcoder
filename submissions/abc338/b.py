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

s = list(input())
ans = ''
count = [0] * 26

for c in s:
    count[ord(c) - ord('a')] += 1
print(chr(count.index(max(count)) + ord('a')))

