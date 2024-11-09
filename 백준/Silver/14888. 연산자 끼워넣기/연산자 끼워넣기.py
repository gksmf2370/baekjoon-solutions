import sys
n = int(sys.stdin.readline().strip())  
numbers = list(map(int, sys.stdin.readline().strip().split()))  
operators = list(map(int, sys.stdin.readline().strip().split())) 


max_value = -float('inf')
min_value = float('inf')


def backtrack(index, current_result):
    global max_value, min_value, operators 
    if index == n:
        max_value = max(max_value, current_result)
        min_value = min(min_value, current_result)
        return
    
    if operators[0] > 0:  # 덧셈
        operators[0] -= 1
        backtrack(index + 1, current_result + numbers[index])
        operators[0] += 1

    if operators[1] > 0:  # 뺄셈
        operators[1] -= 1
        backtrack(index + 1, current_result - numbers[index])
        operators[1] += 1

    if operators[2] > 0:  # 곱셈
        operators[2] -= 1
        backtrack(index + 1, current_result * numbers[index])
        operators[2] += 1

    if operators[3] > 0:  # 나눗셈
        operators[3] -= 1

        if current_result < 0:
            backtrack(index + 1, -(-current_result // numbers[index]))
        else:
            backtrack(index + 1, current_result // numbers[index])
        operators[3] += 1

backtrack(1, numbers[0])

print(max_value)
print(min_value)
