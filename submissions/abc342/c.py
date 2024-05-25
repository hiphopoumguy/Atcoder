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
n = int(input())
s = input()
q = int(input())

alphabet = "abcdefghijklmnopqrstuvwxyz"
change = "abcdefghijklmnopqrstuvwxyz"
for _ in range(q):
    c, d = input().split()
    change = change.replace(c, d)

