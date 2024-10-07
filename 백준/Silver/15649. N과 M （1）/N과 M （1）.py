import sys
a, b = map(int, sys.stdin.readline().strip().split())
dp = []
visited = [False] * a

def back(a, b, i=0):
    if b == i:
        print(*dp)
        return True
    for j in range(a):
        if not visited[j]:  # 중복 선택 방지를 위해 방문 여부 확인
            visited[j] = True
            dp.append(j + 1)
            back(a, b, i + 1)
            dp.pop()
            visited[j] = False

back(a, b)