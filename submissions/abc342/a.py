S=input()

# 1�񂵂��o�����Ȃ��������ǂ��ɂ��邩���ׂ�
for i in range(len(S)):
  if S.count(S[i])==1:
    print(i+1)
    exit()
