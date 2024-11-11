import sys

cnt = int(sys.stdin.readline().strip())
a = list(map(int,sys.stdin.readline().strip().split()))
b=[0]*cnt
if a[0] == 1:
    b[0] = 1
elif a[0] == 0:
    b[0] = -1

for i in range(1,len(a)):
    if a[i] ==1:
        b[i] = b[i-1]+1
    elif a[i] ==0:
        b[i] = b[i-1]-1

print(sum(b))