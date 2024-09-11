import sys

a = sys.stdin.readline().strip()
result = 0
n=len(a)

for idx,c in enumerate(reversed(a)):
    if c.isdigit():
        b=int(c)*16**idx
        result +=b
    else:
        b=(ord(c)-55)*16**idx
        result +=b
print(result)