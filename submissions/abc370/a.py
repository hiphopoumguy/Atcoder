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
L, R = map(int, input().split())
if L == 1 and R == 0:
    print('Yes')
elif L == 0 and R == 1:
    print("No")
else:
    print("Invalid")
