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
a, b = map(int, input().split())
if (a == 1 and b == 2) or (a == 2 and b == 1):
    print("3")
elif (a == 1 and b == 3) or (a == 3 and b == 1):
    print("2")
elif (a == 2 and b == 3) or (a == 3 and b == 2):
    print("1")
else:
    print("-1")
    
