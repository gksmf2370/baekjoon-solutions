import sys
# 외적을 이용
a = list(map(int,sys.stdin.readline().strip().split()))
b = list(map(int,sys.stdin.readline().strip().split()))
c = list(map(int,sys.stdin.readline().strip().split()))

result = (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) -(b[0]*a[1]+ c[0]*b[1] + a[0]*c[1])

if result > 0:# 반시계
    print(1)
elif result < 0: #시계
    print(-1)
else:
    print(0)