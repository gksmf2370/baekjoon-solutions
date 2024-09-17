import sys

n = int(sys.stdin.readline().strip())
result=0

for _ in range(n) :
  a, b = map(int, sys.stdin.readline().strip().split())
  result += b%a

print(result)