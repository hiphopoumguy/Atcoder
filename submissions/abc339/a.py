#!/usr/bin/env python3
import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import cache
from fractions import Fraction
from itertools import accumulate, combinations, permutations, product
from sortedcontainers import SortedSet, SortedList, SortedDict
mod = 998244353

s = input()
mx = 0
cnt = 0
for i, x in enumerate(s):
    if x == '.':
        if mx < cnt:
            ans = i
            mx = cnt
        cnt = 0
