import sys
# 1234567    2번인덱스         전체 7
# 3 124567   4번인덱스         전체6 
# 6 12457    1번인덱스         전체5
# 2 1457     3번 인덱스        전체4
# 7 145      2번 인덱스        전체3
# 5 14       0번 인덱스        전체2
# 1 4        0번 인덱스        전체1
# 4
a = list(map(int,sys.stdin.readline().strip().split()))

stack = []

b = list(range(1,a[0]+1))
num = 0
for _ in range(a[0]):
    num =(a[1]-1+num) % len(b)

    c=b.pop(num)
    stack.append(c)

print("<" + ", ".join(map(str, stack)) + ">")

