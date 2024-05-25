# 標準入力からの入力を受け取る
import sys
input = sys.stdin.read

# 入力を読み取る
data = input().strip().split('\n')

# 最初の行はN
N = int(data[0])

# カードの情報を保存するリスト
cards = []

# N回の強さとコストを読み取る
for i in range(1, N+1):
    A, C = map(int, data[i].split())
    cards.append((A, C, i))

cards.sort()
ans = []

