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
import pypyjit

sys.setrecursionlimit(10**6)
pypyjit.set_param("max_unroll_recursion=-1")  #Ä‹AŠÖ”‚ğ‚ğ‘‚­‚·‚éˆ—
mod = 998244353
n = int(input())
a = list(map(int, input().split()))
row = [a[0]]

def loop(row):
    if len(row) <= 1:
