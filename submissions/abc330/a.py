n, l = map(int, input().split())
a = list(map(int, input().split()))

print(sum(a[i] >= l for i in range(n)))
