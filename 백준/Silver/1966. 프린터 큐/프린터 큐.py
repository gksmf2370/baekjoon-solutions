import sys

n = int(sys.stdin.readline().strip())
for _ in range(n):
    a, b = map(int,sys.stdin.readline().strip().split())
    que=list(map(int,sys.stdin.readline().strip().split()))

    result=1
    while que:
        if que[0] < max(que):
            que.append(que.pop(0))
        
        else:
            if b ==0:
                break

            que.pop(0)
            result +=1
        
        b = b-1 if b>0 else len(que)-1
    
    print(result)