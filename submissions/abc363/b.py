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
N, T, P = map(int, input().split())
L = list(map(int, input().split()))

L = sorted(L)

ans = max(0, T-L[-P])
print(ans)
