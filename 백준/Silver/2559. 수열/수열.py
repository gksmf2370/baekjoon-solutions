import sys

a = list(map(int,sys.stdin.readline().strip().split()))

b = list(map(int,sys.stdin.readline().strip().split()))

c = sum(b[:a[1]])
result = c

for i in range(a[1],a[0]):
    c += b[i] - b[i-a[1]]
    result = max(result, c)

print(result)