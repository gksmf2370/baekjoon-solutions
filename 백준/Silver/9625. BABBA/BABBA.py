import sys

a =int(sys.stdin.readline().strip())

# 46를 미리담아놓을 dp생성
dp = [[0,0] for _ in range(46)]

dp[1] = [0,1]
dp[2] = [1,1]

for n in range(3,a+1):
    dp[n][0] = dp[n-1][1]
    dp[n][1] = dp[n-1][1]+dp[n-2][1]

print(dp[a][0],dp[a][1])