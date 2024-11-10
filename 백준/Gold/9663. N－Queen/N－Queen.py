import sys

n = int(sys.stdin.readline().strip())
cnt = 0

column = [False] * n
diag1 = [False] * (2 * n - 1)  # 왼쪽 대각선
diag2 = [False] * (2 * n - 1)  # 오른쪽 대각선

def dfs(row):
    global cnt
    if row == n:
        cnt += 1
        return

    for col in range(n):
        # 현재 열, 대각선에 퀸이 놓일 수 있는지 확인
        if not column[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
            # 퀸을 배치
            column[col] = diag1[row + col] = diag2[row - col + n - 1] = True
            dfs(row + 1)
            # 퀸 제거
            column[col] = diag1[row + col] = diag2[row - col + n - 1] = False

dfs(0)
print(cnt)
