import sys

a = int(sys.stdin.readline().strip())
# 10이 곱해진 갯수를 보면된다

cnt=0
i = 5  #
while a // i > 0: 
    cnt += a // i
    i *= 5 # 5의 제곱만큼커짐 

print(cnt)