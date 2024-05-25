n = int(input())
a = list(map(int, input().split()))
for count in range(10000):
    for i in range(n):
        if(a[i] % 2 == 1): break
        a[i] /= 2
    else:
        continue
    break
    
print(count)
