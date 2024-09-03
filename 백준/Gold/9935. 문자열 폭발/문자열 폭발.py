import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

stack =[]

for i in a:
    stack.append(i)

    if len(stack) >= len(b) and ''.join(stack[-len(b):]) ==b:
        del stack[-len(b):]

if stack:
    print(''.join(stack))
else:
    print('FRULA')