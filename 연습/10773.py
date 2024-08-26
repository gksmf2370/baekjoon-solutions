import sys
a = int(sys.stdin.readline().strip())
b=[]
for _ in range(a):
    c=int(sys.stdin.readline().strip())
    if c !=0:
        b.append(c)
    else:
        b.pop()
print(sum(b))