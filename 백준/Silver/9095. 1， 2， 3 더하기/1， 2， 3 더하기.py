import sys

a =int(sys.stdin.readline().strip())

# 10를 미리담아놓을 dp생성
dp = [0]*11
dp[1] = 1
dp[2] =2
dp[3] =4

for _ in range(a):
    b = int(sys.stdin.readline().strip())

    for i in range(4, b+1):
        dp[i] = dp[i-1]+ dp[i-2] + dp[i-3]  # dp[4] = dp[3]+ dp[2] + dp[1] = 4+2+1 = 7 

    print(dp[b])