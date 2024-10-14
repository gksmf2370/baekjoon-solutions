import sys
n = int(sys.stdin.readline().strip())
for _ in range(n):
    a = list(sys.stdin.readline().strip().split())
    result = float(a[0])  
    for i in a[1:]:  
        if i == '@':
            result *= 3
        elif i == '%':
            result += 5
        elif i == '#':
            result -= 7
    print(f'{result:.2f}')