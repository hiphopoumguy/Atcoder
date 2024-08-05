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

mx_i = A.index(max(A))
del A[mx_i]
sec_i = A.index(max(A))
if sec_i >= mx_i:
    print(sec_i+2)
else:
    print(sec_i+1)
