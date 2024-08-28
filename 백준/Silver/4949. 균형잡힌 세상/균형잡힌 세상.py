import sys

while True:
    a = sys.stdin.readline().rstrip()
    stack=[]
    check = True
    if a == '.':
        break

    for i in a:
        if i =='[' or i == '(' :
            stack.append(i)
        elif i ==']':
            if len(stack) == 0:
                check = False
                break

            elif stack[-1] == '[':
                stack.pop()
            else:
                check = False
                break
        elif i ==')':
            if len(stack) == 0:
                check = False
                break

            elif stack[-1] == '(':
                stack.pop()
            else:
                check = False
                break


    if not check or stack:
        print('no')
    else:
        print('yes')
