import sys

def check_paper(x, y, size):
    global white, blue
    color = paper[x][y]
    

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                new_size = size // 2     # 색이 다르면 4등분
                check_paper(x, y, new_size)  # 1사분면
                check_paper(x, y + new_size, new_size) #2사분면
                check_paper(x + new_size, y, new_size) #3사분면
                check_paper(x + new_size, y + new_size, new_size) #3사분면
                return True

    # 영역이 모두 같은 색이면 색 카운트
    if color == 0:
        white += 1
    else:
        blue += 1


n = int(sys.stdin.readline().strip())
paper = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
white, blue = 0, 0

check_paper(0, 0, n)
print(white)
print(blue)