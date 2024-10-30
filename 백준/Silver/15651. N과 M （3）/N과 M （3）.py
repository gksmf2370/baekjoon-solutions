import sys
a, b = map(int, sys.stdin.readline().strip().split())
dp = []

def back(a, b, i=0):
    if b == i:
        print(*dp)
        return
    for j in range(a):
        dp.append(j + 1)
        back(a, b, i + 1)
        dp.pop()

back(a, b)
