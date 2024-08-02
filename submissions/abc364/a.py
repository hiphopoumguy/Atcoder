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
before = 'a'
for i in range(N-1):
    s = input()
    
    if s == before == 'sweet':
        print("No")
        sys.exit()
        
