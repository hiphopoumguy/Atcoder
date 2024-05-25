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

n = int(input())
process = []
for _ in range(n):
    l, r = map(int, input().split())
    process.append((l, 's'))
    process.append((r, 'e'))
    
process.sort(key=lambda x: (x[0], x[1] == 'e'))

