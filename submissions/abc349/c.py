# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 21:27:19 2024

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
s = input()
T = input()
t = str.lower(T)
