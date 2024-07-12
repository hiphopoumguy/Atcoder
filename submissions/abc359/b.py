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
cnt = 0
for i in range(2*N-2):
    if A[i] == A[i+2]:
        cnt += 1
        
print(cnt)
