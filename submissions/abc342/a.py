S=input()

# 1回しか出現しない文字がどこにあるか調べる
for i in range(len(S)):
  if S.count(S[i])==1:
    print(i+1)
    exit()
