import sys

a = list(map(int, sys.stdin.readline().strip().split()))
c = {}
for _ in range(a[0]):
    b = sys.stdin.readline().strip()
    if len(b) >= a[1]:
        if b in c:
            c[b] += 1
        else:
            c[b] = 1

result = sorted(c.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for k, v in result:
    print(k)