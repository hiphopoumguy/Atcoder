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
xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())

xa, ya = xa + 1000, ya + 1000
xb, yb = xb + 1000, yb + 1000
xc, yc = xc + 1000, yc + 1000

AB = (xa - xb) ** 2 + (ya - yb) ** 2
BC = (xb - xc) ** 2 + (yb - yc) ** 2
