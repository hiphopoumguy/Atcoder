n, y = map(int, input().split())
flag = 0
for i in range(0, n+1, 1):
    for j in range(0, n+1, 1):
            if (i*10000 + j*5000 + (n-i-j)*1000 == y) & (i + j <= n):
                flag = 1
                print(i, j, n-i-j)
                break
    else:
        continue
    break
if(flag == 0):
    print("-1 -1 -1")
