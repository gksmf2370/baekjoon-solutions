from queue import Queue
import sys
a = int(sys.stdin.readline().strip())

Q = Queue()
    

for i in range(1, a + 1):
    Q.put(i)

while Q.qsize() > 1:

    Q.get()

    Q.put(Q.get())


print(Q.get())