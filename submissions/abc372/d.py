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
H = list(map(int, input().split()))
stock = [] # ‚‚¢ƒrƒ‹‚ğc‚·
ans = []
for h in H[::-1]:
    ans.append(len(stock))
    while stock and stock[-1] < h:
        stock.pop()
    stock.append(h)
print(*ans[::-1])
