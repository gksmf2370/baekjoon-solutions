import sys

a=int(sys.stdin.readline().strip())

cnt=1
for i in range(1,a+1):
    cnt *= i

print(cnt)