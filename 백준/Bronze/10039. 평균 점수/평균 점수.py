import sys
result =0
for _ in range(5):
    a = int(sys.stdin.readline().strip())
    if a< 40:
        a=40
    result +=a
print(int(result/5))