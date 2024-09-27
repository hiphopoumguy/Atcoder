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

N, M = map(int, input().split())
home = defaultdict(int)
for i in range(M):
    A, B = map(str, input().split())
    A = int(A)
    if home[A] == 1 or B == 'F':
        print('No')
    else:
            print("Yes")
