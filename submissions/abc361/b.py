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
a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())

if (max(a, g) < min(d, j)) and (max(b, h) < min(e, k)) and (max(c, i) < min(f, l)):
    print("Yes")
else:
    print("No")
