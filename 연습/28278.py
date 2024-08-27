# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 3: 스택에 들어있는 정수의 개수를 출력한다.
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
import sys
b=[]

a= int(sys.stdin.readline().strip())
for _ in range(a):
    c = list(map(int,sys.stdin.readline().strip().split()))
    if c[0] == 1:
        b.append(c[1])

    elif c[0] == 2:
        if len(b) != 0:
            print(b.pop())
        else:
            print(-1)
    elif c[0] == 3:
        print(len(b))

    elif c[0] == 4:
        if len(b) != 0:
            print(0)
        else:
            print(1)
    elif c[0] == 5:
        if len(b) != 0:
            print(b[-1])
        else:
            print(-1)