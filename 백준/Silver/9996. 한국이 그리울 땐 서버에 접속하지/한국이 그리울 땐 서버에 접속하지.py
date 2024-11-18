import re
import sys
n = int(sys.stdin.readline().strip())
x = sys.stdin.readline().strip().strip()

regex = "^" + x.replace("*", ".*") + "$"

for _ in range(n):
    a = sys.stdin.readline().strip()
    if re.match(regex, a):
        print("DA")
    else:
        print("NE")