import sys
from collections import deque


a=int(sys.stdin.readline().strip())
b=list(map(int,sys.stdin.readline().strip().split()))
c=list(map(int,sys.stdin.readline().strip().split()))
d=int(sys.stdin.readline().strip())
e=list(map(int,sys.stdin.readline().strip().split()))

questack = deque()

for i in range(a):
    if b[i] == 0:
        questack.append(c[i])
for i in e:
    questack.appendleft(i)
    print(questack.pop(), end=' ')


