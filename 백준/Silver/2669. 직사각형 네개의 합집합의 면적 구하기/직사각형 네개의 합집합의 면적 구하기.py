import sys
input = sys.stdin.readline

tile = [[0] * 100 for _ in range(100)]

for _ in range(4): 
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            tile[i][j] = 1

result = sum(sum(row) for row in tile)

print(result)