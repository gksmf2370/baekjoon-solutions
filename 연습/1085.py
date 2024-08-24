#x,y 에 있고 오른쪽 위 꼭짓점은 w.h에있다
x, y ,w, h = map(int,input().split())
c=0
d=0
if w-x < x:
    c = w-x
elif w -x >= x:
    c = x

if h-y < y:
    d = h - y
elif h-y >= y:
    d = y

if d<c:
    print(d)
else: print(c)