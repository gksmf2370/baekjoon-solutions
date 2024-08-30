import sys
from collections import deque

a= int(sys.stdin.readline().strip())

d = deque()

for _ in range(a):
    b = list(map(int,sys.stdin.readline().strip().split()))

    if b[0] == 1:
        d.appendleft(b[1])

    elif b[0] == 2:
        d.append(b[1])
    
    elif b[0] == 3:
        if len(d):
            print(d.popleft())
        else:
            print(-1)          
    elif b[0] == 4:
        if len(d):
            print(d.pop())
        else:
            print(-1)

    elif b[0] == 5:
        print(len(d))

    elif b[0] == 6:
        if len(d):
            print(0)
        else:
            print(1)

    elif b[0] == 7:
        if len(d):
            print(d[0])
        else:
            print(-1)

    elif b[0] == 8:
        if len(d):
            print(d[-1])
        else:
            print(-1)