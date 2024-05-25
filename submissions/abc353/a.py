import sys
n = int(input())
h = list(map(int, input().split()))
left = h[0]
for i, x in enumerate(h[1:]):
  if left < x:
    print(i+2)
    sys.exit()
print(-1)
