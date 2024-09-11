import sys
result=0
max=0
for _ in range(4):
    a,b = list(map(int,sys.stdin.readline().strip().split()))
    result= result+b-a
    if result>=max :
        max=result
print(max)