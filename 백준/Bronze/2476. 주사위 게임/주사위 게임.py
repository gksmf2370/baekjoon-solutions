import sys
input = sys.stdin.read

data = input().splitlines()[1:]
max_prize = 0

for line in data:
    a, b, c = sorted(map(int, line.split()))
    
    if a == b == c:
        prize = 10000 + a * 1000
    elif a == b or b == c:
        prize = 1000 + b * 100
    else:
        prize = c * 100
    
    max_prize = max(max_prize, prize)

print(max_prize)