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
d = dict()

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        d[s[i:j]] = 1
        
print(len(d))
