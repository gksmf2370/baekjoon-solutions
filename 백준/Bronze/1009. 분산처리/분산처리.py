import sys
a = int(sys.stdin.readline().strip())

for _ in range(a):
    b = list(map(int,sys.stdin.readline().strip().split()))
    c = b[0]%10

    if c ==0:
        print(10)
    elif c ==1 or c==5 or c==6:
        print(c)
    elif c==4 or c==9:
        if b[1]%2==0:
            print((c**2)%10)
        else:
            print(c)
    else:
        if b[1]%4 ==0:
            print(c**4%10)
        else:
            print(c**(b[1]%4)%10)