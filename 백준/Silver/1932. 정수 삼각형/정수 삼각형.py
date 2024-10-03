import sys

n = int(sys.stdin.readline().strip())

stack=[]

for i in range(n):
    stack.append(list(map(int,sys.stdin.readline().strip().split())))


for i in range(1,n):
    for j in range(0, i+1):
        if j ==0:
            stack[i][0] = stack[i-1][0] + stack[i][0]
        elif j == i:
            stack[i][j] = stack[i-1][j-1] + stack[i][j]
        else:
            stack[i][j] = max(stack[i-1][j-1], stack[i-1][j]) + stack[i][j]

print(max(stack[n-1]))