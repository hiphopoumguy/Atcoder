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

Sab, Sac, Sbc = map(str, input().split())
if Sab == '<':
    if Sac == '>':
        print('A')
    elif Sbc == '<':
        print('B')
    else:
        print('C')
else:
