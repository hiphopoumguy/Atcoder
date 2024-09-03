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
N,K = map(int,input().split())
graph = [set() for _ in range(N)]
for _ in range(N-1):
  a,b = map(int,input().split())
  a -= 1
  b -= 1
  graph[a].add(b)
  graph[b].add(a)
V = set(list(map(lambda x: int(x)-1,input().split())))

