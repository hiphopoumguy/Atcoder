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
S = input()
count = [0] * 26
tmp = 1
if N == 1:
    print('1')
    sys.exit()
    
for i in range(1, N):
    if S[i] == S[i-1]:
