#!/usr/bin/env python3
import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from fractions import Fraction
from itertools import accumulate, combinations, permutations, product
mod = 998244353

N = int(input())
graph = [[] for _ in range(N)]

for i in range(N-1):
    A, B, X = map(int, input().split())
    graph[i].append((i+1, A)) #(道，コスト)
    graph[i].append((X-1, B))

INF = 10 ** 185

