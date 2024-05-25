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
max_diff = 0
shoulder = 0
for i in range(n):
    a, b = map(int, input().split())
    diff = b - a
    shoulder += a
    if max_diff <= diff:
        max_diff = diff
        max_head = b
