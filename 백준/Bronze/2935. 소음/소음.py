import sys

a = int(sys.stdin.readline().strip())
b = sys.stdin.readline().strip()
c = int(sys.stdin.readline().strip())

if b =='*':
    print(a*c)
else:
    print(a+c)