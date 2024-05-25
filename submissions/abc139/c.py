N = int(input())
H = list(map(int, input().split()))

max_count = 0
count = 0

for i in range(N-1):
    if H[i] >= H[i+1]:
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 0
if count > max_count:
    max_count = count
print(max_count)
