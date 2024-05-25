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

input = sys.stdin.read
data = input().strip().split('\n')
N = int(data[0])
users = []
for i in range(1, N+1):
    S, C = data[i].split()
    C = int(C)
    users.append((S, C))

