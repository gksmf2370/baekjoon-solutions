import sys
a = int(sys.stdin.readline().strip())
b = sys.stdin.readline().strip().split()
c = int(sys.stdin.readline().strip())
d = sys.stdin.readline().strip().split()

count = {}

for i in b:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

result = []
for i in d:
    result.append(str(count.get(i,0)))

print(' '.join(result))