import sys

def hanoi(n, start, mid, end):
    if n==1:
        print(start, end)

    else:
        hanoi(n-1, start, end, mid)
        print(start, end)
        hanoi(n-1, mid, start, end)

a = int(sys.stdin.readline().strip())

# 이동횟수 
print(2**a - 1)
hanoi(a, 1, 2 , 3)