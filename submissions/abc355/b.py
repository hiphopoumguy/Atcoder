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

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = a + b
a = sorted(a)
c = sorted(c)

for i in range(len(c)-1):
