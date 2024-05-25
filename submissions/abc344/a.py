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
flag = 0
for i in range(len(s)):
    if s[i] == '|' and flag == 0:
        flag = 1
        x = i
    if s[i] == '|' and flag == 1:
        y = i+1
print(s[:x] + s[y:])
