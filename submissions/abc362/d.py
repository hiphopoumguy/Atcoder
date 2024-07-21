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

N, M = map(int, input().split())
A = list(map(int, input().split()))

graph = [[] for _ in range(N)]

for _ in range(M):
    U, V, B  = map(int, input().split())
    U -= 1
    V -= 1
