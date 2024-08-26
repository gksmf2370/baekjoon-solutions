import sys
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

a = int(sys.stdin.readline().strip())

b= [int(sys.stdin.readline().strip()) for _ in range(a)]

c = []
for i in range(a-1):
    c.append(b[i+1]-b[i])

gcd_result = c[0]
for i in range(1, len(c)):
    gcd_result = gcd(gcd_result, c[i])

count = (b[-1]-b[0]) // gcd_result + 1 -a

print(count)

