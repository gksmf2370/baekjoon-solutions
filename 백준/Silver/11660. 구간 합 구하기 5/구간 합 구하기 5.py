import sys
a, b = map(int, sys.stdin.readline().strip().split())

stack = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(a)]

stack_sum = [[0] * (a + 1) for _ in range(a + 1)]

for i in range(1, a + 1):
    for j in range(1, a + 1):
        stack_sum[i][j] = stack[i-1][j-1] + stack_sum[i-1][j] + stack_sum[i][j-1] - stack_sum[i-1][j-1]

for _ in range(b):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    result = stack_sum[x2][y2] - stack_sum[x1-1][y2] - stack_sum[x2][y1-1] + stack_sum[x1-1][y1-1]
    print(result)

