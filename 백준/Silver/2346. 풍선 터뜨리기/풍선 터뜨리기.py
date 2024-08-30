import sys
from collections import deque

a = int(sys.stdin.readline().strip())

d = deque(enumerate(map(int,sys.stdin.readline().strip().split())))

stack = []

while d:
    # 현재 풍선의 위치와 숫자를 꺼냄
    idx, move = d.popleft()
    stack.append(idx+1) 

    if not d:
        break

    if move > 0:
        d.rotate(-(move-1)) # 이미 rotate(-1)이 되었다 따라서 한칸 적게 rotate해야함
    else:
        d.rotate(-move)

print(' '.join(map(str, stack)))