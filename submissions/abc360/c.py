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
N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

mx = [0]*N

for i in range(N):
    mx[A[i]-1] = max(mx[A[i]-1], W[i])
    
print(sum(W)-sum(mx))
