import sys

A, B = map(int, input().split())
i = 0
while(1):
    if ((A-1)*i+1) >= B:
        print(i)
        sys.exit()
    i += 1
