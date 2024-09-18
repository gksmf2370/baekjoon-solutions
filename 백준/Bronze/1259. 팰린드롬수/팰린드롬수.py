import sys
while True:
    result = 'yes'
    a=sys.stdin.readline().strip()
    if a =='0' :
        break
    for  i in range(len(a)//2):
        if a[i]!=a[-(i+1)]:
            result='no'
            break
    print(result)