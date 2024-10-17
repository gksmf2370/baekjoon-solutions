import sys
a, b = map(int, sys.stdin.readline().strip().split())
dp = []
visited = [False] * a

def back(a, b, i=0, start=0):
    if b == i:
        print(*dp)
        return True
    for j in range(start, a):  
        if not visited[j]:  
            visited[j] = True
            dp.append(j + 1)
            back(a, b, i + 1, j + 1)  
            dp.pop()
            visited[j] = False

back(a, b)
