import sys

a=int(sys.stdin.readline().strip())

baseball = [list(map(int,sys.stdin.readline().strip().split()))for _ in range(a)]

cnt = 0
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i==j or j==k or k==i:
                continue

            for ball in baseball:

                x,y,z = map(int,str(ball[0]))

                st_count, ball_count = 0,0

                # 첫번째 자리
                if x == i:
                    st_count +=1
                elif (y ==i or z==i):
                    ball_count +=1
                
                # 두번째 자리
                if y== j :
                    st_count +=1
                elif (x ==j or z==j):
                    ball_count +=1

                # 세번째 자리
                if z==k :
                    st_count +=1
                elif (x==k or y ==k):
                    ball_count +=1
                
                if not( ball[1] == st_count and ball[2] == ball_count):
                    break
            else:
                cnt +=1
    
print(cnt)