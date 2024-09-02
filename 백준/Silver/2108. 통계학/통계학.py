import sys
from collections import defaultdict

a = int(sys.stdin.readline().strip())
dic = defaultdict(int)
for _ in range(a):
    b = int(sys.stdin.readline().strip())
    dic[b] += 1

# 산술평균
sm = sum(k * v for k, v in dic.items())
print(int(round(sm / a, 0)))

# 중앙값
sort = sorted(dic.keys())
mid_idx = (a // 2)
sorted_list = []
for k in sort:
    sorted_list.extend([k] * dic[k])
print(sorted_list[mid_idx])

# 최빈값
max_freq = max(dic.values())
mode_candidates = [k for k, v in dic.items() if v == max_freq]
mode_candidates.sort()

if len(mode_candidates) > 1:
    print(mode_candidates[1])
else:
    print(mode_candidates[0])

# 범위
print(max(sort) - min(sort))