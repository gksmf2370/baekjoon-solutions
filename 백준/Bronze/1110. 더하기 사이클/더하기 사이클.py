import sys

n = int(sys.stdin.readline().strip()) 
num = n  
count = 0  

while True:
    a = num // 10 
    b = num % 10  
    c = (a + b) % 10 
    num = (b * 10) + c  
    count += 1  
    if num == n:
        break

print(count)