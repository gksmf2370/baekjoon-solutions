import sys

def gcd(a,b):
    if a% b == 0:
        return b
    return gcd(b, a%b)

a , b = map(int, sys.stdin.readline().strip().split())

result = a*b // gcd(a,b)

print(result)