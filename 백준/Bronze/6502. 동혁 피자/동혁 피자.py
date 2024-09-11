import sys
import math
i = 1  
while True:
    a = list(map(int, sys.stdin.readline().strip().split()))
    if a[0] == 0:
        break
    r, w, l = a  # 반지름, 너비, 높이
    nubi = math.sqrt(w ** 2 + l ** 2)
    if 2 * r >= nubi:
        print(f'Pizza {i} fits on the table.')
    else:
        print(f'Pizza {i} does not fit on the table.')
    i += 1 