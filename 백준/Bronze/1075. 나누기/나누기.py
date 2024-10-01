import sys


a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())

a = (a // 100) * 100


for i in range(100):
    if (a + i) % b == 0:

        print(f"{i:02d}")
        break