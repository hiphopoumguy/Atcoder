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

ans = []
while(1):
    x = int(input())
    ans.append(x)
    
    if x == 0:
        break

[print(ans[-i-1]) for i in range(len(ans))]
