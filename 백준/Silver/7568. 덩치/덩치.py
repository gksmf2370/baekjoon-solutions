import sys
n = int(sys.stdin.readline().strip())
stack =[]
for _ in range(n):
    a = list(map(int,sys.stdin.readline().strip().split()))
    stack.append(a)


ranks = [1] * n # 초기 등수 1

for i in range(n):
    for j in range(n):
        if i != j:
            if stack[i][0] < stack[j][0] and stack[i][1] < stack[j][1]:
                ranks[i] += 1

for rank in ranks:
    print(rank)