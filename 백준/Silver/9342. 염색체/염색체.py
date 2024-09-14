import sys
import re

def check(s):
    p = re.compile('^[A-F]{,1}A+F+C+[A-F]{,1}$')
    res = p.match(s)
    return "Good" if res== None else "Infected!"

a = int(sys.stdin.readline().strip())

for _ in range(a):
    b = sys.stdin.readline().strip()
    print(check(b))