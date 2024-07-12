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
S = input()

for i, s in enumerate(S):
    if s == 'R':
        Ri = i
    if s == 'M':
        Mi = i

if Ri < Mi:
    print('Yes')
