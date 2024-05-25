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
def f(x, y):
    x4 = x // 4
    y2 = y // 2
    s = x4 * 4 * y2 * 2
    xx = x % 4
    yy = y % 2
    #x•ûŒü‚Ì‚Í‚Ý‚¾‚µ
    if xx >= 1:
        s += y2 * 3 + yy * 2
    if xx >= 2:
