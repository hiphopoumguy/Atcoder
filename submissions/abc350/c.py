# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:09:03 2024

@author: s.ykym
"""

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
a = list(map(int, input().split()))
