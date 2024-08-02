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
H, W = map(int, input().split())
Si, Sj = map(int, input().split())
Si -= 1
Sj -= 1
Grid = [input() for _ in range(H)]
X = input()

for x in X:
    if x == 'R' and Sj < W-1 and Grid[Si][Sj+1] == '.':
        Sj += 1
