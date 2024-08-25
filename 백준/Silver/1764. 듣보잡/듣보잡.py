import sys
a, b = map(int,sys.stdin.readline().strip().split())

a = set(sys.stdin.readline().strip() for _ in range(a))

b = set(sys.stdin.readline().strip() for _ in range(b))
c= []

for i in b:
    if i in a:
        c.append(i)
c.sort()
print(len(c))
for i in c:
    print(i)