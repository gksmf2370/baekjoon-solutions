import sys

a = int(sys.stdin.readline().strip())
c = set()
cnt = 0

for _ in range(a):
    b = sys.stdin.readline().strip()
    if b == 'ENTER':
        c = set()  
    else:
        if b not in c:  
            c.add(b)
            cnt += 1  

print(cnt)