import sys
def gcd(e,f):
    if f == 0:
        return e
    return gcd(f, e%f)

a , b = map(int, sys.stdin.readline().strip().split())
c , d = map(int, sys.stdin.readline().strip().split())

e =a*d + b*c
f = b*d
gcd_result = gcd(e,f)
print(e//gcd_result, f//gcd_result)