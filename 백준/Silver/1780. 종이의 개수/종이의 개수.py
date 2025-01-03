import sys
input = sys.stdin.readline

# 값이 같은지 
def is_same(x, y, n):
    first_value = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != first_value:
                return False, None
    return True, first_value

def divide(x, y, n):
    same, value = is_same(x, y, n)
    if same:
       
        if value == -1:
            counts[0] += 1
        elif value == 0:
            counts[1] += 1
        else:
            counts[2] += 1
    else:
        # 3등분 후 9개 구역으로 나누어 재귀 호출
        size = n // 3
        for i in range(3):
            for j in range(3):
                divide(x + i * size, y + j * size, size)

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]


counts = [0, 0, 0]

divide(0, 0, N)

print(counts[0])
print(counts[1])
print(counts[2])
