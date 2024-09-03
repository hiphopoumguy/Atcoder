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
while len([a for a in A if a > 0]) > 1:
    A = sorted(A, reverse=True) 

    A[0] -= 1
    A[1] -= 1
    cnt += 1
