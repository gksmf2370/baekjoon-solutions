import sys

# dp로 풀기
dp0 = [0] * 41  # 0이 출력되는 횟수를 저장
dp1 = [0] * 41  # 1이 출력되는 횟수를 저장

dp0[0], dp1[0] = 1, 0  # fib(0) 호출 시 0의 횟수
dp0[1], dp1[1] = 0, 1  # fib(1) 호출 시 1의 횟수

# 피보나치 결과에 따른 0과 1 호출 횟수를 미리 계산
for i in range(2, 41):
    dp0[i] = dp0[i-1] + dp0[i-2]
    dp1[i] = dp1[i-1] + dp1[i-2]

a = int(sys.stdin.readline().strip())
for _ in range(a):
    b = int(sys.stdin.readline().strip())
    print(dp0[b], dp1[b])