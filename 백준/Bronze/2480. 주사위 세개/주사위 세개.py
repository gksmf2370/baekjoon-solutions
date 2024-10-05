a, b, c=map(int,input().split())

result=0
if a==b and b==c and c==a:
    result=10000+a*1000
elif a!=b and b!=c and c!=a: # 6 2 5
    if a>b:
        if a>c:
            result=a*100
    if b>c:
        if b>a:
            result=b*100
    if c>a:
        if c>b:
            result=c*100
else:
    if a==b or a==c:
        result=1000+a*100
    else:
        result=1000+b*100
print(result)
