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
X = list(input())
cnt = 0
while X[-1] == '0':
    X.pop()
    cnt += 1
if cnt == 3:
    X.pop()
print("".join(X))
