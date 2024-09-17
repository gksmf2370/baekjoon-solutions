import sys

a = list(map(int,sys.stdin.readline().strip().split()))
a.sort()

for i in range(len(a)):
    print(a[i], end=' ')