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
s = list(map(int, input()))
c = list(map(int, input().split()))
cost0 = [0] * n #0101...
cost1 = [0] * n #1010...
ans = 10 ** 18
if s[0] == 1:
    cost0[0] = c[0]
else:
    cost1[0] = c[0]
