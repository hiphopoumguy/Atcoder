# �W�����͂���̓��͂��󂯎��
import sys
input = sys.stdin.read

# ���͂�ǂݎ��
data = input().strip().split('\n')

# �ŏ��̍s��N
N = int(data[0])

# �J�[�h�̏���ۑ����郊�X�g
cards = []

# N��̋����ƃR�X�g��ǂݎ��
for i in range(1, N+1):
    A, C = map(int, data[i].split())
    cards.append((A, C, i))

cards.sort()
ans = []

