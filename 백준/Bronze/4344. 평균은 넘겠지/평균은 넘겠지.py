import sys
a = int(sys.stdin.readline().strip())
for _ in range(a):
    b = list(map(int,sys.stdin.readline().strip().split()))
    mean = sum(b[1:])/(len(b)-1)
    cnt=0
    for i in b[1:]:
        if i>mean:
            cnt +=1
    print(round(cnt/(len(b)-1)*100,3),'%',sep='')