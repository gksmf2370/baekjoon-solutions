import sys
a = int(sys.stdin.readline().strip())
dic = {'Q1':0, 'Q2':0, 'Q3':0, 'Q4':0 ,'AXIS':0}
for _ in range(a):

    b = list(map(int,sys.stdin.readline().strip().split()))
    if b[0] == 0 or b[1] == 0:
        dic['AXIS'] += 1
    elif b[0] > 0:
        if b[1] >0:
            dic['Q1'] +=1
        elif b[1] <0:
            dic['Q4'] +=1
    elif b[0] <0:
        if b[1] > 0:
            dic['Q2'] +=1
        elif b[1] <0:
            dic['Q3'] +=1
    
for k,v in dic.items():
    print(f'{k}: {v}')
