a, m, l, r = map(int, input().split())

l -= a
r -= a
y = r // m - (l - 1) // m
print(y)

