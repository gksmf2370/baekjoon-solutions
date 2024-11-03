import sys

def combination(n, k):
    if k > n - k:  
        k = n - k

    result = 1
    for i in range(k):
        result *= n - i
        result //= i + 1
    
    return result

while True:
    a, b = map(int, sys.stdin.readline().strip().split())
    if a == 0 and b == 0:
        break
    print(combination(a, b))