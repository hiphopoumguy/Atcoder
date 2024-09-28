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
A, B, C = map(int, input().split())
if B < C:
    if B < A < C:
        print('No')
    else:
        print('Yes')
else:
    if C < A < B:
        print("Yes")
    else:
