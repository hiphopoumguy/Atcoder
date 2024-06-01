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

n, m = map(int, input().split())

result = 0
    
# 各ビット位置について計算
for bit in range(61):
    bit_mask = 1 << bit
    total_count = 0
        
