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

s = input()
t = input()
len_s = abs(ord(s[0]) - ord(s[1]))
len_t = abs(ord(t[0]) - ord(t[1]))
if len_s == len_t or len_s + len_t == 5:
    print("Yes")
else:
    print("No")

