from collections import deque

def Sliding_Window_Minimum(A, L):
    ans = []
    q = deque()
    for i, a in enumerate(A):
        while q and a <= q[-1][1]: #�V�����l���傫��q���폜
            q.pop()
        q.append([i, a])
        if i >= L - 1: #L�𒴂�����ans���o�n�߂�
            ans.append(q[0][1]) #1�ԍ�(�ŏ��l)
        if q and q[0][0] <= i + 1 - L: #�ŏ��l�̃C���f�b�N�X�������͈͂𒴂��������
            q.popleft()
    return ans


n, k = map(int, input().split())
P = list(map(lambda x: int(x) - 1, input().split()))
rev = [0] * n
for i in range(n):
    rev[P[i]] = i
