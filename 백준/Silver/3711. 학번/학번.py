import sys

n= int(sys.stdin.readline().strip())

for _ in range(n):
    st = int(sys.stdin.readline().strip())
    stack=[]
    for i in range(st):
        a=int(sys.stdin.readline().strip())
        stack.append(a)
    c=1
    while(True):
        result = set([x % c for x in stack])
        if len(result) ==len(stack):
            break
        c +=1
    print(c)