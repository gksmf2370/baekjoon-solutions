import sys

a,b,c = map(int,sys.stdin.readline().strip().split())

result = pow(a,b,c)

print(result)