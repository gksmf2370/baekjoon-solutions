import sys
nan = []
for _ in range(9):
    a = int(sys.stdin.readline().strip())
    nan.append(a)

total = sum(nan)

for i in range(9):
    for j in range(i + 1, 9):
        if total - (nan[i] + nan[j]) == 100:
            # 역순으로 제거 (j가 i보다 큰 인덱스이므로 먼저 제거)
            nan.pop(j)
            nan.pop(i)
            nan.sort()
            for height in nan:
                print(height)
            sys.exit()  # 프로그램 종료