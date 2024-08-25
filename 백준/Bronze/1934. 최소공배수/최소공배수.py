import sys
a= int(sys.stdin.readline().strip())

for _ in range(a):
    c, d = map(int,sys.stdin.readline().strip().split())
    x, y = c, d
    while y != 0:
        temp = x
        x = y
        y = temp % y
    print(c * d // x)