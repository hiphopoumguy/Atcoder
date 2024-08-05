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
def can_distribute(N, M, A, x):
    # •â•Šzmin(x, A_i)‚Ì‘˜a‚ğŒvZ
    total = 0
    for a in A:
        total += min(x, a)
        if total > M:
            return False
    return total <= M

def find_mx(N, M, A):
