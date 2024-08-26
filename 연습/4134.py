import sys
def is_prime(n):
    if n < 2:
        return False # 0과 1은 소수가 아니다
    for i in range(2, int(n**0.5) + 1):
        if n % i ==0:
            return False
    return True
    
a= int(sys.stdin.readline().strip())

for _ in range(a):
    b = int(sys.stdin.readline().strip())

    if is_prime(b):  # 소수면 그대로 출력
        print(b)
    else:
        i = b +1
        while True:
            if is_prime(i):
                print(i)
                break
            i +=1