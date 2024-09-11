import sys

n= int(sys.stdin.readline().strip())

stack = []
nlist =[]
for _ in range(n):
    a = int(sys.stdin.readline().strip())
    nlist.append(a)

num = 1 # 현재값
ans = []
b = 1

for i in nlist:
    while num <= i:
        ans.append('+')
        stack.append(num)
        num +=1
    
    if stack[-1] > i:
        b =0

    if stack[-1] == i:
        ans.append('-')
        stack.pop()

if b==1:
    for i in ans:
        print(i)
else:
    print('NO')