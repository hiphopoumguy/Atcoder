#!/usr/bin/env python3
import sys
import math
import bisect
import numpy as np
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from fractions import Fraction
from itertools import accumulate, combinations, permutations, product
mod = 998244353

n, q = map(int, input().split())
dragon = [[n, 0]]
for i in range(n-1, 0, -1):
    dragon.append([i, 0])
for _ in range(q):
    q1, q2 = map(str, input().split())
    
    if q1 == '2':
        str_dragon = map(str, dragon[-(int(q2))])
