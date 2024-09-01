import sys
def factorial(n):
    cnt = 1
    for i in range(1,n+1):
        cnt *= i
    return cnt

def bino_coef(n,k):
    fac_n = factorial(n)
    fac_k = factorial(k)
    fac_nk = factorial(n-k)

    result = fac_n/(fac_k*fac_nk)
    return int(result)

a = int(sys.stdin.readline().strip())

for _ in range(a):
    b = list(map(int,sys.stdin.readline().strip().split()))
    print(bino_coef(b[1],b[0]))    