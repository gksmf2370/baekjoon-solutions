import sys
n = int(sys.stdin.readline().strip())
t = list(map(int, sys.stdin.readline().strip().split()))


t.sort()

total_time = 0
c_time = 0
for time in t:
    c_time += time
    total_time += c_time

print(total_time)
