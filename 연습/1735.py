import sys
# 재귀함수 방식

def gcd(e,f):
    if f == 0:
        return e
    return gcd(f, e%f)

# 반복문

def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

a , b = map(int, sys.stdin.readline().strip().split())
c , d = map(int, sys.stdin.readline().strip().split())

e =a*d + b*c
f = b*d
gcd_result = gcd(e,f)
print(e//gcd_result, f//gcd_result)