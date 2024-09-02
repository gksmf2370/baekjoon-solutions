import sys

def pabonach(n):
    if n <= 1:
        return n
    return pabonach(n-1) + pabonach(n-2)

a = int(sys.stdin.readline().strip())
print(pabonach(a))