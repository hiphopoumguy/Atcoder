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

#ìôî‰êîóÒ
m = len(str(n))
r = pow(10, m, mod)

ans = n * ((1 - pow(r, Çé, mod)) * pow(1 - r, -1, mod)) % mod

print(ans)
