import sys
def factiorial(n):
    cnt = 1
    for i in range(1,n+1):
        cnt *= i
    
    return(cnt)

def bino_coef(n,k):
    
    fac_n = factiorial(n)
    fac_k = factiorial(k)
    fac_nk = factiorial(n-k)

    result = fac_n/(fac_k*fac_nk)
    return result


a =list(map(int,sys.stdin.readline().strip().split()))

print(int(bino_coef(a[0],a[1])))
