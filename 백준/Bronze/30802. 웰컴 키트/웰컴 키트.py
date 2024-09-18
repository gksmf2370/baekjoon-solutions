import sys

n = int(sys.stdin.readline().strip())

a = list(map(int,sys.stdin.readline().strip().split()))
b, c = map(int,sys.stdin.readline().strip().split())

result = 0

for i in a:
    if i ==0:
        continue
    elif i <=b:
        result +=1
    elif i%b ==0:
        result += i//b
    else:
        result += i//b +1

print(result)
print(f'{n//c} {n%c}')