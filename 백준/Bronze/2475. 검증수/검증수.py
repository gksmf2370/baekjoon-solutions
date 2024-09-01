import sys
a = list(map(int,sys.stdin.readline().strip().split()))
cnt=0
for i in a:
    cnt +=i**2
print(cnt%10)