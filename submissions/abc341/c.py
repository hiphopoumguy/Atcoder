#!/usr/bin/env python3
import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from fractions import Fraction
from itertools import accumulate, combinations, permutations, product
mod = 998244353
h, w, n = map(int, input().split())
t = input()
s = ([input() for _ in range(h)])

ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '#': #‰‰ñ…–vƒ}ƒ“
            continue
        y = i
        x = j
