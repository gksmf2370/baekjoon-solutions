n = int(input())  
cnt = 0

for _ in range(n):
    word = input()
    stack = []
    for char in word:
        if stack and stack[-1] == char:
            stack.pop() 
        else:
            stack.append(char)
    if not stack: 
        cnt += 1

print(cnt)
