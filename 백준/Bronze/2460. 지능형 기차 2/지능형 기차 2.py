import sys
stops = []
for _ in range(10):
    a,b = map(int,sys.stdin.readline().strip().split())
    stops.append((a,b))

dp = [0] * 11  # 모든역
for i in range(1, 11):
    a, b = stops[i-1]
    dp[i] = dp[i-1] + b - a

print(max(dp))
    