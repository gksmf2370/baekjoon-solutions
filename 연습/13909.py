import sys
import math # math함수 사용
a = int(sys.stdin.readline().strip())
# 1번째 사람은 1의 배수인 1,2,3번 창문을 연다 (1,1,1)
# 2번째 사람은 2의 배수인 2번 창문을 닫는다.(1, 0, 1)
# 3번째 사람은 3의 배수인 3번 창문을 닫는다 (1, 0, 0)
# 마지막으로 열려 있는 창문의 개수는 1개

result = math.isqrt(a) # math.isqrt(a) : a의 정수 제곱근을 반환한다. n 이하의 가장 큰 정수를 반환환
print(result)

# 반복문으로도 간으하다

i = 1
count =0
while i*i <= a:
    count +=1
    i +=1
print(count)