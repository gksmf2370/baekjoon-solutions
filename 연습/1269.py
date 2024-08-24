import sys
a, b =map(int ,sys.stdin.readline().strip().split())

c = set(sys.stdin.readline().strip().split())

d = set(sys.stdin.readline().strip().split())

print(len(c-d)+len(d-c))

# difference 메소드 이용가능
c.difference(d)      
d.difference(c)