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
R = int(input())
if 0 <= R <= 99:
    print(100-R)
elif 100 <= R <= 199:
    print(200-R)
else:
    print(300-R)
