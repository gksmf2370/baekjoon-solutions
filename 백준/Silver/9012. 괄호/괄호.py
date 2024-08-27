import sys
a = int(sys.stdin.readline().strip())

for _ in range(a):
    b = sys.stdin.readline().strip()
    stack =[]
    check = True

    for i in b:
        if i == '(' :
            stack.append(i)
        elif i == ')':
            if len(stack):
                stack.pop()
            else:
                check = False
                break
    
    if not check or stack:
        print('NO')
    else: 
        print('YES')
        