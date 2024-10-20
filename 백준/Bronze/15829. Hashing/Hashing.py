import sys

n = int(sys.stdin.readline().strip())
a = sys.stdin.readline().strip()
result =0

for i in range(n):
    result += (ord(a[i]) - 96) * (31 ** i) # askii a는 97

result %= 1234567891
print(result)