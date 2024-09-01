import sys
a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
c = int(sys.stdin.readline().strip())

result = a*b*c
dic ={}
for idx, value in enumerate(str(result)):
    if value in dic:
        dic[value] +=1

    else:
        dic[value] = 1
for i in range(10):
    print(dic.get(str(i), 0))