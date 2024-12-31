import sys
input = sys.stdin.read

def division(start_row, start_col, size):
    if size == 1:  # 픽셀 하나일 때
        print(arr[start_row][start_col], end="")
        return
    num = arr[start_row][start_col]

    
    for row in range(start_row, start_row + size):
        for col in range(start_col, start_col + size):
            if num != arr[row][col]:
                print("(", end="")
                half = size // 2
                division(start_row, start_col, half)  # 왼쪽 위
                division(start_row, start_col + half, half)  # 오른쪽 위
                division(start_row + half, start_col, half)  # 왼쪽 아래
                division(start_row + half, start_col + half, half)  # 오른쪽 아래
                print(")", end="")
                return

    # 모두 같은 값일 때
    print(arr[start_row][start_col], end="")
    return


lines = input().splitlines()
n = int(lines[0])
arr = [list(map(int, list(lines[i + 1].strip()))) for i in range(n)]


division(0, 0, n)
