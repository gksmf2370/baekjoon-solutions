import sys
from itertools import combinations_with_replacement
a,b = map(int,sys.stdin.readline().strip().split())

for i in combinations_with_replacement(range(1, a+1), b):
    print(*i)
