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
if n == 0:
    print('#')
    sys.exit()
    
grid = [['#']*3**n for _ in range(3**n)]
for i in range(3**n):
    for j in range(3**n):
        for k in range(1, 7):
