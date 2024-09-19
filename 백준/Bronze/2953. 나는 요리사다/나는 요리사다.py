import sys
result = 0
num = 0
for _ in range(5):
    a = list(map(int,sys.stdin.readline().strip().split()))
    if sum(a) >result:
        result=sum(a)
        num = _+1

print(num, result)
