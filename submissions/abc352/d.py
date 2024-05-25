from collections import deque

def Sliding_Window_Minimum(A, L):
    ans = []
    q = deque()
    for i, a in enumerate(A):
        while q and a <= q[-1][1]: #新しい値より大きいqを削除
            q.pop()
        q.append([i, a])
        if i >= L - 1: #Lを超えたらansが出始める
            ans.append(q[0][1]) #1番左(最小値)
        if q and q[0][0] <= i + 1 - L: #最小値のインデックスが検索範囲を超えたら消去
            q.popleft()
    return ans


n, k = map(int, input().split())
P = list(map(lambda x: int(x) - 1, input().split()))
rev = [0] * n
for i in range(n):
    rev[P[i]] = i
