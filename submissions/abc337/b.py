# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:54:12 2024

@author: s.ykym
"""

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
s = input()
len(s)
for i in range(len(s)-1):
    if s[i] == s[i+1]:
