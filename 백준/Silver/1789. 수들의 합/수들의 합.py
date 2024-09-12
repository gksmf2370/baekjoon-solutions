import sys

a= int(sys.stdin.readline().strip())
b=1
result=0
#200 
while result<=a:
    result +=b
    b +=1

print(b-2)