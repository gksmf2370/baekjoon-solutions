import sys
a = int(sys.stdin.readline().strip())

for _ in range(a):
    b = list(sys.stdin.readline().strip())
    cnt = 0
    result=0
    for i in b:
        if i =='O':
            cnt +=1
            result += cnt
        elif i =='X':
            cnt =0

    print(result)
