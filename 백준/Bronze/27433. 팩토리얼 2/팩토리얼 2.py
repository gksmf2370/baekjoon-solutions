import sys
def factorial(n):
    if n<=1:
        k = 1
    else:
        k = factorial(n-1) * n
    return k

a = int(sys.stdin.readline().strip())

print(factorial(a))