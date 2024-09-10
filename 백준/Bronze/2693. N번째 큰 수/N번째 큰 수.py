import sys
a = int(sys.stdin.readline().strip())
for _ in range(a):
    b = list(map(int,sys.stdin.readline().strip().split()))
    c = sorted(b,reverse=True)
    print(c[2])