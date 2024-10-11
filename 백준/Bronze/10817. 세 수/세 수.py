import sys

stack = list(map(int,sys.stdin.readline().strip().split()))
stack.sort()
print(stack[1])