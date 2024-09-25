import sys

n= int(sys.stdin.readline().strip())

for _ in range(n):
    a= sys.stdin.readline()
    cnt =0
    for i in range(len(a)-3):
        if a[i:i+3] =='WOW':
            cnt +=1
    
    print(cnt)