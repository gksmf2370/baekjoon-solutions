import sys

n=int(sys.stdin.readline().strip())

arr = list(map(int,sys.stdin.readline().strip().split()))

dp = [0] * n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + arr[i], arr[i])

print(max(dp))