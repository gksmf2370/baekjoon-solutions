import sys
num =[]
a= int(sys.stdin.readline().strip())
for _ in range(a):
    b=int(sys.stdin.readline().strip())
    num.append(b)
num_list=sorted(num,reverse=True)
for i in num_list:
    print(i)