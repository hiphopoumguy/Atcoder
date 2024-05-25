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
w, b = map(int, input().split())
s = "wbwbwwbwbwbw"
S = ((w+b) // len(s) + 2) * s
length_S = len(S)
for start in range(length_S):
    for end in range(start + 1, length_S + 1):
        substring = S[start:end]
        count_w = substring.count('w')
        count_b = substring.count('b')

