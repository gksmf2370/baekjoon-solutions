import sys
a, b = map(int,sys.stdin.readline().strip().split())

c = [sys.stdin.readline().strip() for _ in range(a)]

d = [sys.stdin.readline().strip() for _ in range(b)]

dogam = {}

for i, name in enumerate(c, start=1):
    dogam[i] = name

dogam2 = {v:k for k,v in dogam.items()}
for j in d:
    if j.isdigit():
        print(dogam.get(int(j)))
    else:
        print(dogam2.get(j))