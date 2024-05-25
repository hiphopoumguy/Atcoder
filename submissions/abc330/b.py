n, l, r = map(int, input().split())
a = list(map(int, input().split()))
ans = [] * n
for x in a:
    if x < l:
       ans.append(l) 
    elif x > r:
       ans.append(r)
    else:
       ans.append(x)
print(* ans)
