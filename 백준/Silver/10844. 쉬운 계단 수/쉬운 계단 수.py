import sys

MOD = 1_000_000_000
n = int(sys.stdin.readline().strip())

dp = [[0] * 10 for _ in range(n + 1)]


for j in range(1, 10):  
    dp[1][j] = 1


for i in range(2, n + 1):  
    for j in range(10):   
        if j > 0:
            dp[i][j] += dp[i - 1][j - 1]
        if j < 9:
            dp[i][j] += dp[i - 1][j + 1]

        dp[i][j] %= MOD  # MOD로 나머지 연산을 수행하여 값이 너무 커지지 않도록 함
        

result = sum(dp[n]) % MOD
print(result)