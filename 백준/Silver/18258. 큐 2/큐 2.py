from queue import Queue
import sys

a = int(sys.stdin.readline().strip())

Q = Queue()

for _ in range(a):
    b = sys.stdin.readline().strip().split()
    if b[0] == 'push':
        Q.put(b[1])
    elif b[0] == 'pop':
        if Q.qsize():
            print(Q.get())
        else:
            print(-1)
    elif b[0] == 'size':
        print(Q.qsize())
    
    elif b[0] == 'empty':
        if Q.qsize():
            print(0)
        else:
            print(1)

    elif b[0] == 'front':
        if Q.qsize():
            print(Q.queue[0])
        else:
            print(-1)

    elif b[0] == 'back':
        if Q.qsize():
            print(Q.queue[-1])
        else:
            print(-1)