import sys

a = int(sys.stdin.readline().strip())

for _ in range(a):
    b = list(map(int, sys.stdin.readline().strip().split()))


    floor = b[2] % b[0]
    room = b[2] // b[0] + 1

    if floor == 0:
        floor = b[0]
        room -= 1

    print(f"{floor}{room:02d}")
