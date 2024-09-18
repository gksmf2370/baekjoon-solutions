import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
c= sys.stdin.readline().strip()

d =0
if a.isdigit():
    d= int(a)+3
elif b.isdigit():
    d = int(b)+2
elif c.isdigit():
    d = int(c)+1

if d% 15 ==0:
    result='FizzBuzz'
elif d% 3 ==0:
    result='Fizz'
elif d% 5 ==0:
    result='Buzz'
else:
    result = d

print(result)