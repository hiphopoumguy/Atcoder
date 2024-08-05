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
Y = int(input())

if Y % 4 != 0:
    print('365')
else:
    if Y % 100 != 0:
        print('366')
    elif Y % 100 == 0 and Y % 400 != 0:
        print('365')
    elif Y % 400 == 0:
