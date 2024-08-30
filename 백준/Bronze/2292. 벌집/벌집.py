# 수정코드
a = int(input())

if a == 1:
    print(1)
else:
    cnt = 1
    start = 2
    while start <= a:
        start += 6 * cnt
        cnt += 1
    print(cnt)