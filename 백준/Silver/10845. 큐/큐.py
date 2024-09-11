import sys
from queue import Queue

n= int(sys.stdin.readline().strip())

Q =Queue()

for _ in range(n):
    a = sys.stdin.readline().strip().split()
    if a[0] =='push':
        Q.put(a[1])

    elif a[0] == 'pop':
        if Q.empty():
            print(-1)
        else:
            print(Q.get())

    elif a[0] == 'size':
        print(Q.qsize())
    
    elif a[0] == 'empty':
        if Q.empty():
            print(1)
        else:
            print(0)

    elif a[0] =='front':
        if Q.empty():
            print(-1)
        else:
            print(Q.queue[0])
    
    elif a[0] =='back':
        if Q.empty():
            print(-1)
        else:
            print(Q.queue[-1])