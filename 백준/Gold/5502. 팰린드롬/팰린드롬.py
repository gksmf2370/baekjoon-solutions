import sys

n = int(sys.stdin.readline().strip())
b = sys.stdin.readline().strip()

revers = b[::-1]

dp = [0] * (n + 1) #LCS

for i in range(1, n + 1):
    prev = 0  # 이전값 저장
    for j in range(1, n + 1):
        temp = dp[j]  #현재값 저장
        if b[i - 1] == revers[j - 1]:
            dp[j] = prev + 1
        else:
            dp[j] = max(dp[j], dp[j - 1])
        prev = temp 

print(n - dp[n])