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
    
    if not check or stack:   # 리스트는 비어 있지 않으면 True , if not check:는 check가 false와 같다.
        print('NO')
    else: 
        print('YES')
        