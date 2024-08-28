import sys
a = int(sys.stdin.readline().strip())

b = list(map(int,sys.stdin.readline().strip().split()))

# 5 4 1 3 2 입력
# b = [5 4 1 3 2]
number =1
stack = []
stack2 = []
for i in b:

    if i == number:
        stack2.append(i)
        number +=1
        for i in range(len(stack)):
            if stack[-1] == number:
                stack2.append(stack.pop())
                number +=1
        continue
        
    else:
        stack.append(i)

if len(stack) == 0:
    print('Nice')
else:
    print('Sad')

