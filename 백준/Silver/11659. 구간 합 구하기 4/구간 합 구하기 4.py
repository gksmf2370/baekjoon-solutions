import sys
from collections import deque

n, m = map(int,sys.stdin.readline().strip().split())
b = list(map(int,sys.stdin.readline().strip().split()))

# 누적 합 배열 생성
pre_sum = [0] * (n + 1)
for i in range(1, n+1):
    pre_sum[i] = pre_sum[i-1] + b[i-1]
# n= 5이면 pre_sum = [0, 5, 9 , 12, 14 , 15]

for _ in range(m):
    c = list(map(int, sys.stdin.readline().strip().split()))
    start, end = c[0], c[1]
    # 구간 합 계산
    result = pre_sum[end] - pre_sum[start - 1]
    print(result)
