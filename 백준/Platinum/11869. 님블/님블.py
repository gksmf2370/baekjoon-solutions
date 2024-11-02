import sys

def nim(a):
    nim_sum = 0
    for i in a:
        nim_sum ^= i
    
    if nim_sum != 0:
        return "koosaga"
    else:
        return "cubelover"

n = int(sys.stdin.readline().strip())  
a = list(map(int, sys.stdin.readline().strip().split())) 

print(nim(a))