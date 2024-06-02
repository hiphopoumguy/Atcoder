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

from collections import Counter

N = int(input())
A = sorted(map(int, input().split()))
M = 10**6

a = [0] * (M + 1)
#�ݐϘa
for x in A:
