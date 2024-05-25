import sys
from collections import deque
input = sys.stdin.readline
mod = 998244353

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
H, W = map(int, input().split())
G = []
for _ in range(H):
    G.append(list(input().rstrip('\n')))

for i in range(H):
    for j in range(W):
        if G[i][j] != "#":
            for di, dj in dir:
                ni, nj = i+di, j+dj
                if 0 <= ni < H and 0 <= nj < W:
                    if G[ni][nj] == "#":
                        G[i][j] = "*"

ANS = 1
