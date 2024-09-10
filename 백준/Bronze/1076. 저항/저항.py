import sys
def register(a):
    if a =='brown':
        stack1.append('1')
    elif a == 'red':
        stack1.append('2')
    elif a == 'orange':
        stack1.append('3')
    elif a == 'yellow':
        stack1.append('4')
    elif a == 'green':
        stack1.append('5')
    elif a == 'blue':
        stack1.append('6')
    elif a == 'violet':
        stack1.append('7')
    elif a == 'grey':
        stack1.append('8')
    elif a == 'white':
        stack1.append('9')
    else:
        stack1.append('0')

stack1 =[]
a = sys.stdin.readline().strip()
register(a)
b = sys.stdin.readline().strip()
register(b)
c = sys.stdin.readline().strip()
register(c)

result = int(stack1[0]+stack1[1])*pow(10,int(stack1[2]))
print(result)