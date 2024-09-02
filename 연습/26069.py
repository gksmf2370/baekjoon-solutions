import sys

a = int(sys.stdin.readline().strip())

c = set()
for i in range(a):
    b = sys.stdin.readline().strip().split()
    if 'ChongChong' in b:
        c.add(b[0])
        c.add(b[1])

    if b[0] in c:
        c.add(b[1])
    if b[1] in c:
        c.add(b[0])
        
print(len(c))