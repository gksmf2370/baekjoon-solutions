import math
import sys

a = sys.stdin.readline().strip()

cnt = [0] * 10

for i in a:
    cnt[int(i)] += 1
six_nine = cnt[6] + cnt[9]
cnt[6] = cnt[9] = math.ceil(six_nine / 2)
result = max(cnt)
print(result)
