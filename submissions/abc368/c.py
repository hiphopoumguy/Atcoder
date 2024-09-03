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
H = list(map(int, input().split()))
T = 0

for h in H:
    if T % 3 == 1:
        if h > 1:
            T += 2
            h -= 4
