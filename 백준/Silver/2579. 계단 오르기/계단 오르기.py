import sys

n=int(sys.stdin.readline().strip())

a = [0] * (n + 1)  
for i in range(1, n + 1):
    a[i] = int(sys.stdin.readline().strip())


dp = [0] * (301)

if n == 1:
    print(a[1])

else:

    dp[1] = a[1]
    dp[2] = a[1] + a[2]
    if n > 2:
        dp[3] = max(a[1] + a[3], a[2] +a[3])

    for i in range(4, n + 1):
        dp[i] = max(dp[i-2], dp[i-3] + a[i-1]) + a[i]

    print(dp[n])