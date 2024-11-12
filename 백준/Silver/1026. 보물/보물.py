import sys
n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
b = list(map(int, sys.stdin.readline().strip().split()))

a.sort(reverse=True)  
b.sort()              

result = sum(x * y for x,y  in zip(a, b))
print(result)
