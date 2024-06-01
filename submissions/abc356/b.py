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
x = [list(map(int, input().split())) for _ in range(n)]
sum = [0]*m
for i in range(n):
    for j in range(m):
        sum[j] += x[i][j]
for i in range(m):
    if sum[i] < a[i]:
        print("No")
