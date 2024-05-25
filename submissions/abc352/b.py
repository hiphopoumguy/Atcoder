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
t = input()
s_i = 0
ans = []
for i in range(len(t)):
    if s[s_i] == t[i]:
        ans.append(i+1)
        s_i += 1

print(*ans)
