import sys
import pypyjit

sys.setrecursionlimit(10**6)
pypyjit.set_param("max_unroll_recursion=-1")

N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
used = [False] * N


def dfs(u):
    used[u] = True
    res = 1
    for v in g[u]:
        if not used[v]:
            res += dfs(v)
