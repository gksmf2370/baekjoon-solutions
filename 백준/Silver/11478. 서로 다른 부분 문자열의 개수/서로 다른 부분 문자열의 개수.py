import sys
a = sys.stdin.readline().strip()
b = set()

for i in range(1, len(a)+1):
    for j in range(len(a)):
        b.add(a[j:j+i])

print(len(b))