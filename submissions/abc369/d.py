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
A = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(N + 1)]

# 初期値の設定
dp[1][0] = 0  # 最初に倒さない場合
dp[1][1] = A[0]  # 最初に倒す場合

for i in range(2, N + 1):
