import sys

a =int(sys.stdin.readline().strip())

##10**6 를 담아둘것
dp = [0]*1000001

for i in range(2, a+1):
 
    dp[i] = dp[i-1] + 1

    # 빼는 경우와 나누는경우의 최소값 선택
    # 2로 떨어질때
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

    # 3으로 떨어질때
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[a])
