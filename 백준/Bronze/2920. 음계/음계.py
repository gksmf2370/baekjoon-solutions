import sys
a = list(map(int,sys.stdin.readline().strip().split()))

if a[0] == 1:
    if a == sorted(a):
        print('ascending')
    else:
        print('mixed')

elif a[0] == 8:
    if a == sorted(a, reverse=True):
        print('descending')
    else:
        print('mixed')

else:
    print('mixed')