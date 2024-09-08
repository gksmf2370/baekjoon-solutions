import sys
a = int(sys.stdin.readline().strip())

name = [sys.stdin.readline().strip() for _ in range(a)]

b = list(name[0]) # 비교할 파일

for i in range(1,a):
    for j in range(len(b)):
        if b[j] != name[i][j]:
            b[j] = '?'

print(''.join(b))