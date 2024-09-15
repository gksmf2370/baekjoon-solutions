import sys

a = int(sys.stdin.readline().strip())

if a & 1:
    print('SK')
else:
    print('CY')