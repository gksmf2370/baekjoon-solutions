import sys
# 3번소 2번, 4번소 1번

a = int(sys.stdin.readline().strip())
dic ={}
cnt = 0
for _ in range(a):
    c, num = list(map(int,sys.stdin.readline().strip().split()))

    if c in dic:

        if dic[c] != num:
            cnt +=1
            dic[c] = num
    else:
        dic[c] = num
    
print(cnt)