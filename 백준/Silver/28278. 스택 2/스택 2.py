import sys
b=[]

a= int(sys.stdin.readline().strip())
for _ in range(a):
    c = list(map(int,sys.stdin.readline().strip().split()))
    if c[0] == 1:
        b.append(c[1])

    elif c[0] == 2:
        if len(b) != 0:
            print(b.pop())
        else:
            print(-1)
    elif c[0] == 3:
        print(len(b))

    elif c[0] == 4:
        if len(b) != 0:
            print(0)
        else:
            print(1)
    elif c[0] == 5:
        if len(b) != 0:
            print(b[-1])
        else:
            print(-1)