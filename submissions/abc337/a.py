#!/usr/bin/env python3
import sys
import numpy as np
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from fractions import Fraction
from itertools import accumulate, combinations, permutations, product
mod = 998244353

N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
if np.sum(x) > np.sum(y):
    print("Takahashi")
elif np.sum(x) == np.sum(y):
    print("Draw")
else:
    print("Aoki")
