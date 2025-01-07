import sys
input = sys.stdin.readline

a, b = map(int, input().split())

numbers = [True] * (a + 1)  
count = 0

for i in range(2, a + 1):
    if numbers[i]:  
        for j in range(i, a + 1, i):
            if numbers[j]:
                numbers[j] = False  
                count += 1
                if count == b:  
                    print(j)
                    break
