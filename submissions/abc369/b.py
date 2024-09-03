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
N = int(input())
NL, NR = 0, 0
tired = 0
for _ in range(N):
    A, B = map(str, input().split())
    A = int(A)
    if NL == 0 and B == 'L':
        NL = A
    elif NR == 0 and B == 'R':
        NR = A
