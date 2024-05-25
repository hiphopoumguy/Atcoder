S=input()

# 1‰ñ‚µ‚©oŒ»‚µ‚È‚¢•¶š‚ª‚Ç‚±‚É‚ ‚é‚©’²‚×‚é
for i in range(len(S)):
  if S.count(S[i])==1:
    print(i+1)
    exit()
