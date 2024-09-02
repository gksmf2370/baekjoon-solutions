import sys

a= int(sys.stdin.readline().strip())

if a == 1:
    b = int(sys.stdin.readline().strip())

    print(b**2)
else:
    b = list(map(int,sys.stdin.readline().strip().split()))
    result = min(b)*max(b)
    print(result)