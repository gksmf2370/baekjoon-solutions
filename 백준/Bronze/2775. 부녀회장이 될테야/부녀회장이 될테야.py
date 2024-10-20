import sys
n = int(sys.stdin.readline().strip())  

for _ in range(n):
    a = int(sys.stdin.readline().strip())  # 층수
    b = int(sys.stdin.readline().strip())  # 호수

    dp = [[0] * (b+1) for _ in range(a+1)]

    for i in range(1, b+1):
        dp[0][i] = i

    for floor in range(1, a+1):
        for room in range(1, b+1):
            dp[floor][room] = dp[floor][room-1] + dp[floor-1][room]

    print(dp[a][b])
