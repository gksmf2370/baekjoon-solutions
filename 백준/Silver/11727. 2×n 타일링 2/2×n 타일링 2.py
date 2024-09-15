import sys
# 입력이 1000

a =int(sys.stdin.readline().strip())

# 1000를 미리담아놓을 dp생성
dp = [0]*1001

dp[1] = 1
dp[2] =3
dp[3] = 5

for i in range(4, a+1):
    dp[i] = dp[i-1]+ 2*dp[i-2]  # dp[3] = dp[2] + dp[1]

print(dp[a]%10007)